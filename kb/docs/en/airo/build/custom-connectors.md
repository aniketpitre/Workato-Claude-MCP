---
url: 'https://docs.workato.com/en/airo/build/custom-connectors.md'
description: >-
  Build, review, save, and release Workato custom connectors from Claude Code,
  Claude Desktop, or Cursor through the AIRO MCP server.
---

# Build custom connectors with AIRO MCP

You can use the [AIRO MCP server](/en/airo/mcp) to create and edit custom connectors from an MCP client such as Claude Code, Claude Desktop, or Cursor. Describe the API and desired behavior in plain language, and AIRO writes and validates the Connector SDK code for the connection, actions, triggers, and schemas.

Refer to the [Connector SDK](/en/developing-connectors/sdk) documentation for the underlying SDK concepts and syntax.

## Prerequisites

- AIRO enabled in your workspace, with the [AIRO MCP server](/en/airo/mcp) connected to your MCP client.
- The Connector SDK privilege to create, edit, and publish custom connectors. Workato uses the privileges of your Workato account for OAuth 2.0 connections. Connections that authenticate with an API token perform actions with the workspace owner's identity and permissions. You also need the Connector SDK **Use in recipes** privilege to select the released connector while building recipes. Refer to [Connector SDK privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#connector-sdk).
- The target API documentation, including authentication, endpoints, request and response examples, pagination, and error behavior. If this is absent, your MCP client resorts to searching the internet for relevant API documentation, and you are responsible for verifying the API details it finds.
- A non-production account or safe test data when the API can create, update, or delete records.

Don't paste passwords, tokens, client secrets, or other credentials into a prompt or hard-code them in connector source. Define sensitive values as connection fields and store the actual values in a Workato connection.

## Available tools

AIRO MCP consists of the following tools that let your MCP client build and release connectors:

| Tool | What it does |
| --- | --- |
| `connector_builder_init_connector` | Creates a new connector. |
| `connector_builder_get_latest_connector_code` | Loads an existing connector's latest saved source into the session. |
| `connector_builder_read_connector_code` | Reads or searches the session's current source without changing it. |
| `connector_builder_apply_connector_code_patch` | Validates the updated code against SDK framework and rules, before updating the connector in the session. |
| `connector_builder_save_latest_connector_code` | Validates the complete connector, including code you didn't change, and stores a new version. |
| `connector_builder_get_unreleased_code_diff` | Compares the session's current source with the connector's latest released version. |
| `connector_builder_release_connector` | Validates and saves the current working copy, then releases it as the active version. |

Your MCP client may prompt you to approve operations that modify Workato, such as creating, editing, saving, or releasing a connector. Review the operation and the target connector before you approve it. Some clients let you pre-configure permission levels for each tool in the server settings instead. Confirm your AIRO MCP connection points to the intended workspace and environment before you start.

## Example: Build a weather-alert connector

This example creates a connector for the free [National Weather Service API](https://www.weather.gov/documentation/services-web-api). The API doesn't require an API key, but it does require a `User-Agent` header that identifies the application and provides contact information.

By the end of the example, the connector has:

- A connection field for a contact email.
- An action that retrieves active alerts for a state or territory.
- A polling trigger for newly issued active alerts.
- Saved versions that you can review before release.

AIRO can generate different valid implementations for the same request. As a result, the generated code, field names, and explanations may differ from the examples in this guide, even when the connector provides equivalent behavior.

### Create the connector and first action

Start by describing the connector and the first behavior for AIRO to build. Include the display title and API documentation.

```text
Build a custom connector named National Weather Service Alerts for the National Weather Service API. Use <https://www.weather.gov/documentation/services-web-api> as the API documentation. Set the connector's SDK `title` to `National Weather Service Alerts`. Add an action that retrieves active weather alerts for a state or territory.
```

AIRO creates the connector in your workspace immediately and binds the current session to it. It uses the API documentation available to the client to generate the connection and action, then validates the result.

> **CONNECTOR NAMING**
> 
> The connector record created in the workspace and the `title` key in the SDK source are separate. Set the SDK `title` explicitly so the intended display name appears when users select the connector in recipes.
> 
> Connector titles must be unique in a workspace. Choose a different title or add a qualifier, for example `(Custom)`, if the title is already in use.

For this API, the generated connection and request logic should include a contact field, a `User-Agent` header, and the active-alerts endpoint.

View the generated connection and action code

```ruby
connection: {
  fields: [
    {
      name: 'contact_email',
      label: 'Contact email',
      optional: false,
      hint: 'Used in the User-Agent header required by the National Weather Service API.'
    }
  ],
  authorization: { type: 'no_auth' },
  base_uri: lambda do |_connection|
    'https://api.weather.gov/'
  end
},

test: lambda do |connection|
  get('alerts/active').
    headers('User-Agent': "(workato-integration, #{connection['contact_email']})").
    params(area: 'CA')
end,

actions: {
  get_active_alerts: {
    title: 'Get active alerts',
    input_fields: lambda do
      [
        {
          name: 'area',
          label: 'State or territory code',
          optional: false,
          hint: 'Two-letter code, for example CA or NY.'
        }
      ]
    end,
    execute: lambda do |connection, input|
      response = get('alerts/active').
        headers('User-Agent': "(workato-integration, #{connection['contact_email']})").
        params(area: input['area']).
        after_error_response(/.*/) do |_code, body, _header, message|
          error("#{message}: #{body}")
        end

      { alerts: response['features'].map { |feature| feature['properties'] } }
    end,

    output_fields: lambda do
      [
        {
          name: 'alerts',
          type: 'array',
          of: 'object',
          properties: [
            { name: 'id' },
            { name: 'event' },
            { name: 'headline' },
            { name: 'severity' },
            { name: 'sent', type: 'date_time' },
            { name: 'expires', type: 'date_time' }
          ]
        }
      ]
    end
  }
}
```

Weather alerts don't fit a generic create, get, update, and delete pattern. An object-specific action, for example `get_active_alerts`, makes the connector easier to understand and use.

Review the generated code, then save the change as a version:

```text
Save this connector.
```

AIRO validates the complete connector and returns the saved version number and a link to the connector in Workato. The exact version number depends on the connector's save history.

### Add a polling trigger

Next, extend the connector with a polling trigger. You don't need to repeat the connector ID because the current session is already bound to the connector.

```text
Add a trigger for new active alerts in a state or territory.
```

AIRO adds the trigger to the existing connector and validates the updated SDK code.

View the generated trigger code

```ruby
triggers: {
  new_active_alert: {
    title: 'New active alert',
    input_fields: lambda do
      [
        {
          name: 'area',
          label: 'State or territory code',
          optional: false,
          hint: 'Two-letter code, for example CA or NY.'
        },
        {
          name: 'since',
          label: 'When first started, this recipe should pick up alerts from',
          type: 'timestamp',
          optional: true,
          sticky: true
        }
      ]
    end,
    poll: lambda do |connection, input, closure|
      closure = {} unless closure.present?

      sent_since = (closure['cursor'] || input['since'] || Time.now).to_time.utc.iso8601

      response = get('alerts/active').
        headers('User-Agent': "(workato-integration, #{connection['contact_email']})").
        params(area: input['area']).
        after_error_response(/.*/) do |_code, body, _header, message|
          error("#{message}: #{body}")
        end

      alerts = response['features'].
        map { |feature| feature['properties'] }.
        select { |alert| alert['sent'].to_time.utc.iso8601 > sent_since }

      closure['cursor'] = alerts.
        map { |alert| alert['sent'].to_time.utc.iso8601 }.
        max || sent_since

      {
        events: alerts,
        next_poll: closure,
        can_poll_more: false
      }
    end,
    dedup: lambda do |record|
      "#{record['id']}@#{record['sent']}"
    end,
    output_fields: lambda do
      [
        { name: 'id' },
        { name: 'event' },
        { name: 'headline' },
        { name: 'severity' },
        { name: 'sent', type: 'date_time' },
        { name: 'expires', type: 'date_time' }
      ]
    end
  }
}
```

Review the complete generated trigger, paying particular attention to its cursor handling, timestamp comparison, pagination, and deduplication logic. Then save the connector:

```text
Save this connector.
```

## Review and test before release

AIRO validates the generated Connector SDK code before you save it, including checking for Ruby syntax errors. Before release, review the complete implementation and test it in Workato to confirm that the connector behaves as expected with the target API. A successful validation doesn't replace API-specific review or runtime testing.

Complete these checks before release:

1. **Review the complete implementation.** Use the summary AIRO returns as an overview, then follow the returned Workato link to inspect the complete connector. Ask AIRO to explain any block you don't understand.
2. **Compare the implementation with the API documentation.** Verify the base URL, paths, authentication, headers, field names, request parameters, response shape, pagination, rate limits, and error responses.
3. **Create a test connection in Workato.** For this example, provide a contact email and confirm that the connection test succeeds.
4. **Run the action with safe input.** Use the SDK **Test code** tab to run the action. For example, request active alerts for `CA` and confirm that the returned fields match the declared output schema. Refer to [Use the Test code tab](/en/developing-connectors/sdk/quickstart/debugging#using-the-test-code-tab).
5. **Test the trigger.** Verify its initial `since` behavior, cursor updates, ordering, pagination, and deduplication. Runtime testing can reveal skipped or repeated events that aren't apparent from reviewing the code alone.
6. **Confirm the target environment.** Test in a development or test environment before releasing changes that existing recipes may use.

You can also ask AIRO for a focused review before release:

```text
Review the current connector for release readiness without changing it. Compare the connection, action, and trigger with the National Weather Service API documentation. Check the authentication, request paths and parameters, input and output schemas, response mapping, pagination, cursor behavior, deduplication, and error handling. Explain any risks you find and recommend changes.
```

## Release the connector

Ask AIRO to release the connector:

```text
Save and release these changes.
```

> **RELEASE HAS IMMEDIATE EFFECT IN ALL RECIPES**
> 
> Release makes a saved version the active version immediately, and every recipe that uses the connector starts using it.

AIRO reviews the unreleased changes, shows this warning with a summary of what's about to go live, and asks you to confirm before it releases the connector. Since this connector has no released version yet, AIRO reports this as a first release rather than a change summary. Each release needs its own explicit confirmation, no matter what you approved earlier. You can provide your own release note, or let AIRO suggest one from the diff.

AIRO tells you which of these happened:

- **Released.** The connector is now on the new version.
- **Already current.** The saved version was already active, so nothing changed.
- **Saved but unreleased.** The save succeeded but the release step failed afterward.
- **Rejected.** Validation findings blocked the save, so nothing was persisted.

A rejected or unreleased outcome means the active version didn't change. Resolve the reported issue and ask again.

Verify the following after the connector is released:

- The expected version is active.
- The connector appears under the value in its SDK `title` field.
- The connector is available to recipes in the intended environment.

## Check what changed before a later release

You can ask AIRO what changed any time you edit a connector after releasing it:

```text
What changed in this connector since the last release?
```

AIRO returns a summary grouped into breaking, added, and changed items, so you can scope your review to updates instead of the entire connector.

## Write effective prompts

Strong prompts provide the goal, the source of truth, the relevant connector context, important constraints, and a concrete result to verify.

A useful pattern is:

> **Goal** + **target connector or API** + **documentation or existing code to follow** + **requirements and constraints** + **acceptance checks**

Break a large connector into reviewable changes. Build and test the connection and one action first, save it, then add triggers or more complex actions. This makes validation findings and behavioral problems easier to isolate.

### Build a new connector

Name the target API, connector title, authentication, and first operation. A vague prompt such as "Build a connector for weather data" omits all four.

```text
Build a custom connector named National Weather Service Alerts for the National Weather Service API. Use <https://www.weather.gov/documentation/services-web-api> as the source of truth. Set the SDK `title` to `National Weather Service Alerts`. The API doesn't use an API key but requires a User-Agent with contact information. Add an action that retrieves active alerts for a two-letter state or territory code.
```

Also include the authentication type, required scopes, token refresh behavior, and a safe endpoint for testing the connection when the API requires authentication.

### Edit an existing connector

Name the connector ID, the component to change, the existing pattern to follow, and the expected result.

```text
Open connector 4821. Read its existing get-ticket action, then add an update-ticket action that follows the same object schema and error-handling pattern. Don't change unrelated actions. Validate the edit and summarize the exact blocks changed.
```

Use the numeric connector ID when names are ambiguous or duplicated. Save your work before you switch to a different connector, then open the new connector explicitly, so the session doesn't continue editing the previous one.

### Fix a failed save

Include the connector ID, full error text, affected component, and the most recent change.

```text
Open connector 4821. Its polling trigger returns the following validation error after my last edit: [paste the error]. Read the complete trigger, explain the cause, make the smallest safe correction, and validate the connector.
```

## Limitations

- AIRO MCP can't delete a custom connector. Delete an unused connector from the Workato UI. You must stop any active recipes that use the connector first. Refer to [Delete a custom connector](/en/developing-connectors/sdk/quickstart#deleting-a-custom-connector).
- AIRO MCP changes the connector through the MCP session, not by driving the Workato SDK editor, and it doesn't maintain a synchronized local source file. Each save writes a version you can then open and test in Workato.
- A save validates the complete connector, not only the latest edit. Findings elsewhere in the source can block the save until you resolve them.
- `connector_builder_get_unreleased_code_diff` compares only the source already open in the session. Open the connector first with `connector_builder_get_latest_connector_code` or `connector_builder_init_connector`.

## Troubleshooting

### AIRO created or opened the connector in the wrong place

Confirm the workspace and environment associated with the AIRO MCP connection. Reconnect to the intended target before you create or save anything else.

### An operation is denied

Confirm that the connected Workato user has the required Connector SDK privileges. AIRO MCP can't exceed the permissions of the connected user.

### A save fails on findings you didn't introduce

A save validates the complete source. Ask AIRO to list all current findings and identify which ones are outside the block you changed. Resolve the findings before saving. If you temporarily comment out code, review the functional impact before you save or release the connector.

### A save is rejected for size

Ask AIRO to identify repeated schemas or logic and reduce the source. Moving repeated field schemas into `object_definitions` is usually the largest reduction.

### AIRO can't find the connector by name

Use its numeric connector ID. Choose a unique title when another connector already uses the title you requested.

### The connection test fails even though the path looks correct

Check how `base_uri` and request paths combine. A request path that begins with `/` replaces any path segment in `base_uri`. For example, `https://host/api/v2/` combined with `/users` resolves from the host root instead of under `/api/v2/`. Use a trailing `/` in `base_uri` and omit the leading `/` from relative request paths to preserve the base path. Refer to [Configuring your base\_uri](/en/developing-connectors/sdk/sdk-reference/connection#configuring-your-base-uri).

### Release reports that the version is already current

The latest saved version was already the active version, so the release changed nothing. Expect this when you release the same saved version twice, whether from AIRO or [the Workato UI](/en/developing-connectors/sdk/quickstart/version-control#releasing-the-latest-version), without saving new edits in between.

### The connector was saved but recipes still use the old behavior

A saved version isn't active until it is released. Ask AIRO what changed since the last release, or open the connector in Workato and compare the latest saved version with the active released version.

---
