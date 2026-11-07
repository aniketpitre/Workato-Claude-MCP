---
url: 'https://docs.workato.com/en/mcp/mcp-app-development.md'
description: >-
  Build a Workato MCP app with HTML and JavaScript, including the SDK
  connection, calling tools, Content Security Policy, and debugging.
---

# MCP app development

Use this documentation to understand conceptual information and follow specific guidelines to build a Workato MCP app with HTML and JavaScript. MCP app development includes an SDK connection, calling tools from inside the app, Content Security Policy configuration, design patterns, and debugging.

## How an MCP app works

An MCP app is a single HTML document that the MCP server serves to the client. The client renders it in a sandboxed iframe inside the chat.

The most important concept to understand is the relationship between the LLM and the app:

- The **LLM calls the linked tool once** to launch the app. This is the only time the LLM is involved in rendering.
- **The app calls tools directly** through the SDK after the app loads. The LLM doesn't mediate these calls.
- The app is the interaction surface. The user views, sorts, filters, and acts on data inside the app, not through additional LLM turns.

The linked tool is called by the LLM once to open the app, then the app takes over. This shapes how you design tools and write app code. The linked tool's input schema only needs the parameters required to launch the app, not the full interaction payload.

> **NEED AN EXAMPLE?**
> 
> Refer to the [GitHub interactive images MCP app](/en/getting-started/use-cases/mcp/github-mcp-app) use case for a step-by-step guide on how to create an MCP app that enables you to view, pan, and zoom your GitHub repo images directly in your LLM, such as ChatGPT, Claude, or Cursor.

## Prerequisites

Confirm that you have the following configuration before you write MCP app code:

- An MCP server with at least one tool, backed by a running recipe. Refer to [Create an MCP server](/en/mcp/mcp-servers#create-an-mcp-server) for more information.
- An MCP App linked to a tool. Refer to [Add an MCP app](/en/mcp/mcp-apps#add-an-mcp-app) for more information.
- A client that supports MCP apps, such as Claude.

## MCP app structure

An MCP app must have the following three parts at minimum:

- An SDK import
- A connection
- Render logic

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <!-- Load external libraries from a CDN. Every external domain must be
       declared in the Content security policy. -->
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body>
  <div id="app">Connecting...</div>

  <!-- type="module" is required. Top-level await only works in a module script. -->
  <script type="module">
    import { App } from 'https://cdn.jsdelivr.net/npm/@modelcontextprotocol/ext-apps@1.3.1/dist/src/app-with-deps.js';

    const app = new App({ name: 'My App', version: '1.0.0' });
    app.ontoolresult = () => {};

    // Await the connection before calling any tool or rendering data.
    await app.connect();

    document.getElementById('app').textContent = 'Connected';
  </script>
</body>
</html>
```

### SDK connection

The MCP app uses the MCP apps SDK (`@modelcontextprotocol/ext-apps`) to communicate with the client. This requires the following configuration:

- The script tag must use `type="module"`. The top-level `await app.connect()` throws a syntax error in a regular script.
- `app.connect()` handles the handshake, host context, and session. **Await it before** you call any tool or render data that depends on a tool result. Rendering before the connection resolves fails silently.
- Set `app.ontoolresult` before you connect to suppress the SDK's default tool-result rendering.
- Pin the SDK to a specific version in the import URL. Refer to the [cdn.jsdelivr.net](https://cdn.jsdelivr.net/npm/@modelcontextprotocol/ext-apps/) documentation for the current stable release.

## Call tools from the MCP app

The MCP calls tools on the same MCP server using `app.callServerTool` after it connects. Workato wraps tool results in two layers that you must unwrap.

```javascript
async function callTool(toolName, params) {
  const raw = await app.callServerTool({ name: toolName, arguments: params });

  // Layer 1 — MCP envelope. Prefer the typed structuredContent.
  // Fall back to the text content as a JSON string.
  let parsed = raw && raw.structuredContent;
  if (!parsed) {
    const text = raw && raw.content && raw.content[0] && raw.content[0].text;
    parsed = text ? JSON.parse(text) : raw;
  }

  // Layer 2 — Workato Skill wrapper. Skills wrap the recipe output under a
  // `result` key. API recipes don't. This normalizes both.
  return parsed && parsed.result ? parsed.result : parsed;
}

// Example: load and render a list.
const data = await callTool('search_records', { query: '' });
renderRecords(data.items);
```

Use the following guidelines to call tools:

- Use `app.callServerTool({ name, arguments })`. Arguments go in the `arguments` field.
- The tool name must match the tool exactly, including capitalization. Workato derives the tool name from the asset name and preserves case. A skill named `Search Records` becomes the tool `Search_Records`, not `search_records`. Verify the exact name in **AI Hub > Enterprise MCP > \[server\] > Tools** before you write the call.
- Reading `raw.items` directly returns `undefined`. The data is nested inside the envelope. Unwrap both layers.

## Configure the Content Security Policy

The MCP app runs in a sandboxed iframe with a strict Content Security Policy (CSP). Every external domain your app contacts for scripts, styles, fonts, images, network requests, or nested frames must be declared or the browser silently blocks it.

Expand the **Content security policy** section when you add or edit an MCP app and add each external domain to the relevant field:

| Field | Controls |
| --- | --- |
| Connect domains | Network requests (`fetch`, `XHR`, WebSocket) |
| Resource domains | Scripts, styles, fonts, images |
| Frame domains | Nested iframes. For example, an embedded video. |
| Base URI domains | Allowed base URIs for the document |

The most common mistake is loading the SDK or a CSS framework from `cdn.jsdelivr.net` without adding it to the resource domains. The result is a blank app with no obvious error. Check the CSP if your app renders blank or unstyled.

> **ADD EVERY DOMAIN YOU TOUCH**
> 
> If your app embeds images from an image CDN or videos from a streaming service, add those domains too. Use your browser's developer tools network tab to find domains that fail to load.

## Design patterns

### Token-efficient tools

The MCP app architecture lets you separate what the LLM sees from what the user sees. The LLM only needs enough information to route the request and launch the app. The rich data that populates the app can bypass the LLM entirely.

This allows you to design following tool types:

- A **launch tool** that the LLM calls. This returns a slim acknowledgment, such as a count and a status, not the full dataset.
- A **data tool** that the app calls from `app.connect()` to fetch the full payload.

This keeps large datasets out of the LLM's context, which reduces token usage and latency on list and detail apps. Add a rendering instruction to the launch tool's description to stop the LLM from restating the data in chat:

````plaintext
The result of this tool is rendered as an interactive MCP app in the chat. The MCP app is the response. Don't list, summarize, or restate the returned items in your text reply.

### Client-side data derivation {: #client-side-data-derivation :}

Compute display-only data, such as filter options or category counts, in the MCP app's JavaScript rather than in the recipe. The recipe returns the raw records, and the app derives the rest. This keeps the recipe simple and avoids the constraints of the recipe formula engine.

```javascript
// Derive filter options from the records the app already has.
function deriveFilters(items) {
  return [
    { name: 'Status', values: [...new Set(items.map(i => i.status))] },
    { name: 'Priority', values: [...new Set(items.map(i => i.priority))] }
  ].filter(g => g.values.length > 0);
}
````

### Keyboard interaction

MCP apps inherit no default keyboard behavior. Add the interactions users expect, such as the following:

- Make clickable cards focusable with `tabindex="0"` and respond to Enter and Space, not just clicks.
- In a comment or message field, submit on Enter and insert a newline on Shift+Enter.
- Close modals on Escape.

### Resize within the chat panel

The browser fullscreen API is blocked inside the MCP app iframe because the host doesn't grant the required permission. Toggle the MCp app's `max-height` between a compact cap and `100vh` with a button to give users more room. The MCP app expands to fill the available chat panel without leaving the iframe.

## Test and debug

Use this section to test and debug your MCP app.

### Use a debug panel during development

Add a visible log element to your app while developing so you can see the SDK connection state and raw tool results. Ensure that you review and complete the following items before you proceed to production:

- Delete the debug element from the HTML.
- Delete the related styles.
- Replace the logging function body so it does nothing.

### The client caches the app per chat

The client doesn't refresh the MCP app in an existing chat after you edit and save MCP app code. The MCP app is pinned to the version that was current when the chat first rendered it. You must start a new chat to load the latest code. Reloading the browser tab isn't enough.

### Verify the deployed code

Add a visible version marker to your MCP app's header and bump it on every save to confirm which code is live. The marker tells you at a glance whether you're looking at the latest deploy when you trigger the app.

## Production checklist

Confirm the following before you share an MCP app:

- The recipe behind every linked tool is running.
- The tool names in your `callServerTool` calls match the server exactly, including case.
- Every external domain is declared in the content security policy.
- Launch-tool descriptions are explicit trigger conditions, not vague capability labels.
- The debug panel and any version marker are removed.
- You tested end to end in a new chat.

## Known limitations

MCP apps have the following limitations:

- **Fullscreen is unavailable**: The browser fullscreen API is blocked in the sandboxed iframe. Use a resize toggle instead.
- **App state doesn't persist**: MCP apps run in a sandboxed iframe. Chat history persists, but the MCP app's internal state, such as saved filters or form inputs, resets on navigation. Persist state through a tool backed by a data store if you need it to persist.
- **Verified user access and token authentication are mutually exclusive**: A tool that requires [verified user access](/en/mcp/verified-user-access) can't use token authentication. Refer to [MCP authentication](/en/mcp/mcp-authentication) for available access methods.

---
