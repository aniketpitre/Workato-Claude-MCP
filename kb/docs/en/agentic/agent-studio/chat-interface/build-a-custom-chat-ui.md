---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/chat-interface/build-a-custom-chat-ui.md
description: >-
  A step-by-step build for a custom chat UI on the Headless API, including
  backend, SSE render loop, event handlers, and recovery.
---

# Build a custom chat UI

This guide demonstrates how to build an end-to-end custom chat interface on the [Headless API](/en/agentic/agent-studio/chat-interface/headless-api). Building a UI requires calling endpoints, a backend that holds credentials safely, and a frontend that turns the Server-Sent Events (SSE) stream into a live, trustworthy conversation.

Use this guide alongside the [Headless API reference](/en/agentic/agent-studio/chat-interface/headless-api) for endpoint details and the [Custom interface API walkthrough](/en/agentic/agent-studio/chat-interface/chain-headless-api-requests) for the request sequence.

## Build overview

Use this guide to build a backend that holds credentials and proxies requests and a browser frontend that streams a genie conversation into live cards and message bubbles. Build in the following order:

- [Step 1: Stand up a backend](#step-1-backend) between the browser and the API.
- [Step 2: Open the stream and run a render loop](#step-2-render-loop) that dispatches each event.
- [Step 3: Handle each event type](#step-3-skill-events), such as skill activity, approvals, connection requests, and messages.
- [Step 4: Track state and recover](#step-7-state-and-recovery) after reloads and dropped streams.

Each step builds on the previous one. The render loop in step 2 is the spine: every later step is a handler the loop dispatches into.

## Step 1: Put a backend between the browser and the API

Don't call the Headless API directly from the browser. Stand up a small same-origin backend that the browser talks to, and let the backend talk to Workato. This protects credentials and avoids cross-origin (CORS) problems.

- **Don't expose the Developer API token (`wrkaus-…`)** in client-side code. It's a builder secret used only for provisioning. The browser should only ever see the public OAuth `client_id` and the end user's own OAuth access token.
- **Relay the OAuth token exchange through the backend.** The browser runs the PKCE flow and receives the authorization `code`, then your backend exchanges the `code` (and later the `refresh_token`) at `id.workato.com/oauth/token`. This keeps token handling server-side and avoids cross-origin requests to the identity host.
- **For API-key integrations, inject auth on the backend.** The backend holds the API key and adds the `Authorization` and `X-IDP-User-Id` headers to each runtime request, then proxies the SSE stream back to the browser.

> **CHOOSE OAUTH FOR USER-FACING UIS**
> 
> Use OAuth 2.0 (PKCE) for any UI that real users sign in to. API-key auth uses a single static key for all callers, so it's only appropriate for trusted server-to-server backends, not browsers. See [Authentication](/en/agentic/agent-studio/chat-interface/headless-api#authentication).

## Step 2: Open the stream and run a render loop

When the user sends a message, your backend calls [Send a message](/en/agentic/agent-studio/chat-interface/headless-api#send-a-message) with `stream: true` and proxies the SSE response to the browser. The frontend reads that stream and dispatches each event to a handler. This loop is the core of the UI, and everything else is a handler it calls.

Read the stream line by line, track the current `event:` type, parse each `data:` line as JSON, and dispatch on the type. A blank line separates events. For example:

```js
// `response` is the proxied SSE stream from your backend.
let currentEvent = null;
for await (const line of readLines(response.body)) {
  if (line.startsWith("event:")) {
    currentEvent = line.slice(6).trim();
  } else if (line.startsWith("data:")) {
    dispatch(currentEvent, JSON.parse(line.slice(5).trim()));
  }
}

function dispatch(type, data) {
  switch (type) {
    case "processing.started":               showTypingIndicator();        break;
    case "skill.running":
    case "skill.completed":
    case "skill.failed":                      updateSkillCard(data);        break;
    case "skill.confirmation_required":       renderApprovalCard(data);     break;
    case "runtime_connection.auth_required":  renderConnectionCard(data);   break;
    case "agent.message":                     renderMessage(data);          break;
    case "processing.finished":               endTurn();                    break;
    default:                                  break;  // ignore system.ping and unknown types
  }
}
```

The following table maps each event to what your UI does with it. The steps after it implement each handler.

| Event | Carries | What your UI does |
| --- | --- | --- |
| `processing.started` |  | Shows a typing indicator |
| `skill.` `running` / `skill.` `completed` / `skill.` `failed` | `skill` `_name`, `skill_id` | Creates or updates a skill card, keyed by `skill_name` |
| `skill.` `confirmation` `_required` | `call_id`, `skill_name`, `skill` `_parameters` | Shows an approval card with parameters and Approve and Reject buttons |
| `runtime_connection` `.auth_required` | `runtime_connection` `_attempt_id`, `auth_link` | Open `auth_link.url`, then poll for completion (see Step 5) |
| `agent.message` | `message_id`, `message` | Renders a chat bubble. De-duplicate by `message_id` and render markdown |
| `processing.` `finished` |  | Ends the turn and removes the typing indicator |
| `system.ping` |  | Ignores. This is a keep-alive sent during long or paused turns |

> **IGNORE UNKNOWN EVENT TYPES**
> 
> Treat any event type you don't recognize as a no-op, as the `default` case above does. This keeps your UI forward-compatible and absorbs keep-alive events like `system.ping`.

## Step 3: Handle skill events

For each skill the genie runs, render a single card that updates in place across its lifecycle. For example, `running` to `completed`, or `failed`, rather than appending a new item per event.

- **Key cards by `skill_name`, not `call_id`.** `skill.running` and `skill.completed` typically don't carry a `call_id` — only `skill_name` and `skill_id` (in the form `recipe:<numeric_id>`). Only `skill.confirmation_required` is guaranteed to include `call_id`.
- **Handle parallel tool calls**: When the genie runs several skills at once, you receive a single `skill.running` but a `skill.completed` for each skill. If a `skill.completed` or `skill.failed` arrives for a `skill_name` with no existing card, create the card so every call is represented. Don't assume a `running` event precedes a terminal event. Some runtime versions also emit `skill.stopped` in place of `skill.completed`, which you should treat as a terminal success.
- **Don't render results from `skill.completed`**: This event doesn't include a structured `result`. The genie feeds the result to the model internally and reflects it in the next `agent.message`. Show the card transitioning to `completed` for feedback, and let the agent message carry the data. If you need the structured output, for example, to draw a chart, fetch the recipe's job output server-side through the Developer API. Refer to [Correlate skill IDs](#correlate-skill-ids) for more information.

## Step 4: Handle approvals

When a skill needs confirmation, the genie emits `skill.confirmation_required` and pauses the turn. Render the skill card in an `awaiting` state and expand it:

- Show the resolved parameters from the event's `skill_parameters` field as a key/value list, so the user can verify what the genie is about to submit.
- Add **Approve** and **Reject** buttons with real visual weight, not small inline icons.
- Resolve the request with [Approve or reject a skill](/en/agentic/agent-studio/chat-interface/headless-api#approve-or-reject-a-skill), passing the event's `call_id`. The same stream resumes after you post a resolution.
- Render the approval card once and update it in place. If your UI polls for events rather than holding the SSE stream open, don't rebuild the turn on every poll. Most polls during a pause return only heartbeats, and continuously recreating the card can drop clicks on the Approve button. Skip re-rendering when the content is unchanged, or render the card into its own node that the event-list re-render doesn't overwrite.

When the user rejects, the genie's next `agent.message` can quote the `rejection_reason` verbatim. Send a generic reason (or none) if you don't want the user's words echoed back into the conversation.

## Step 5: Handle connection requests

The genie emits `runtime_connection.auth_required`, then pauses the turn, when a skill requires the end user's own credentials for an upstream system (Verified User Access). The event carries both a `runtime_connection_attempt_id` and an `auth_link` with the authentication URL.

- Render a card in an `awaiting` state with a button that opens `auth_link.url`, for example `Connect to your account`. Apply the same render-once, update-in-place rule as approval cards so the button stays clickable. If the link has expired, fetch a fresh one with [Get a runtime connection link](/en/agentic/agent-studio/chat-interface/headless-api#get-a-runtime-connection-link) using the `runtime_connection_attempt_id`.
- **Detect when the connection completes** by polling [Get a runtime connection link](/en/agentic/agent-studio/chat-interface/headless-api#get-a-runtime-connection-link) until `status` is `authorized`, or by polling [Get a conversation](/en/agentic/agent-studio/chat-interface/headless-api#get-a-conversation) until `state` leaves `skill_processing`.
- The open SSE stream does **not** deliver the resumed turn after the user authenticates. It emits only `system.ping`, then a `system.stream_interrupted`. Once the connection completes, read the resumed reply from [message history](/en/agentic/agent-studio/chat-interface/headless-api#get-messages) (de-duplicate by `message_id`); see [step 7](#step-7-state-and-recovery).

Because the user completes the login out-of-band and often takes longer than the stream's idle window, treat the dropped stream as expected here — recover from persisted state rather than assuming the turn failed.

## Step 6: Render agent messages

Render `agent.message` events as chat bubbles, with two things to handle:

- **De-duplicate by `message_id`**: The same message can arrive on both the SSE stream and the [message history](/en/agentic/agent-studio/chat-interface/headless-api#get-messages) endpoint when you reconnect. Keep a set of seen `message_id` values.
- **Render markdown**: Message text is typically markdown, such as bold, lists, links, and occasional code. Render it with a markdown library or a small inline renderer. If your bubble style uses `white-space: pre-wrap`, set `white-space: normal` on the markdown container so block elements lay out correctly.

Anchor the typing indicator to the bottom of the message list: re-anchor it below any skill cards you append, so the user sees their message, then live skill activity, then the reply replacing the indicator.

## Step 7: Track state and recover

Show the conversation's overall state (for example, a status pill) by deriving it from the latest event, falling back to [Get a conversation](/en/agentic/agent-studio/chat-interface/headless-api#get-a-conversation) when you reconnect. The conversation `state` is one of `idle`, `ai_running`, `skill_processing`, or `awaiting_approval`. A runtime-connection pause keeps `state` at `skill_processing`; `awaiting_approval` indicates a `skill.confirmation_required` pause.

Rebuild the conversation from persisted data on a reload or dropped stream rather than assuming the live stream is the only source. Complete the following steps to rebuild the conversation:

1. Fetch the [message history](/en/agentic/agent-studio/chat-interface/headless-api#get-messages) and the persisted events from [Get events](/en/agentic/agent-studio/chat-interface/headless-api#get-events).
   
2. Merge and order the two lists by `created_at` (events also carry a per-run `seq_num`).
   
3. De-duplicate messages by `message_id`, then replay the merged list through the same handlers from steps 3–6.
   

All event types, including `skill.*` and `processing.*`, persist for 24 hours, so you can reconstruct a full timeline from [Get events](/en/agentic/agent-studio/chat-interface/headless-api#get-events). The one exception is a turn resumed after a runtime-connection (Verified User Access) pause: the resumed events aren't in [Get events](/en/agentic/agent-studio/chat-interface/headless-api#get-events), so recover that reply from [message history](/en/agentic/agent-studio/chat-interface/headless-api#get-messages) instead. Refer to [Rebuild a conversation timeline](/en/agentic/agent-studio/chat-interface/headless-api-troubleshooting#rebuild-a-conversation-timeline).

## Putting it together

A complete custom chat UI has four components in the following order:

- A **backend** that holds credentials and proxies requests
- A **render loop** that dispatches the SSE stream
- A **handler per event type** that drives cards and bubbles
- A **recovery** that rebuilds from persisted data.

You can send a message, confirm a skill card appears and an `agent.message` renders, approve a skill that requires confirmation, then reload mid-turn and confirm the timeline rebuilds to ensure your build works as expected.

Three invariants are worth restating, because each is a place a naive build breaks:

- Key skill cards by `skill_name`, because terminal skill events often omit `call_id`.
- Treat `processing.finished` as the end of the turn, and ignore unknown event types.
- On reload, rebuild from [Get events](/en/agentic/agent-studio/chat-interface/headless-api#get-events) and [message history](/en/agentic/agent-studio/chat-interface/headless-api#get-messages). Don't treat the live stream as the only source.

## Correlate skill IDs across surfaces

The same skill is identified differently depending on where you look, which matters when you correlate a live tool call back to a skill or job record, for example, to fetch a skill's structured output server-side:

| Surface | Skill identifier |
| --- | --- |
| Headless SSE events | `skill_id` as `recipe:<numeric_id>` |
| Developer API skills (`/api/agentic/skills`) | `skl-…` handle, with the numeric recipe ID as `provider_id` |
| Developer API recipes (`/api/recipes/:id`) | numeric recipe ID |

Match by `skill_name` where you can — it's the most reliable key across surfaces. To map an SSE `skill_id` to a skill record, strip the `recipe:` prefix and match the numeric ID against the skill's `provider_id`.
