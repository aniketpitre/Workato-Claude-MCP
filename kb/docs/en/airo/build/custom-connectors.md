---
url: 'https://docs.workato.com/en/airo/build/custom-connectors.md'
description: >-
  Use AIRO to build, review, and release Workato custom connectors, either
  directly in Workato or through an MCP client such as Claude Code, Claude
  Desktop, or Cursor.
---

# Build custom connectors with AIRO

You can build custom connectors with AIRO either in Workato or through an MCP client such as Claude Code, Claude Desktop, or Cursor. Describe the API and the connector behavior you need, and AIRO writes and validates the Connector SDK code for the connection, actions, triggers, and schemas for you to review and confirm.

Refer to the [Connector SDK](/en/developing-connectors/sdk) documentation for the underlying SDK concepts and syntax.

> **FEATURE AVAILABILITY**
> 
> - Building custom connectors with [AIRO MCP](/en/airo/mcp) is available in all workspaces with AIRO enabled, subject to the [prerequisites](#prerequisites).
>   
> - Building custom connectors with AIRO in Workato is available to select customers. Contact your Customer Success Representative to enable it in your workspace.
>   

## Prerequisites

Confirm that you have the following before you build a custom connector:

- AIRO enabled in your workspace.
- The Connector SDK privilege to create, edit, and publish custom connectors. MCP client connections use the privileges of your Workato account for OAuth 2.0, and connections that authenticate with an API token perform actions with the workspace owner's identity and permissions. You also need the Connector SDK **Use in recipes** privilege to select the released connector while building recipes. Refer to [Connector SDK privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#connector-sdk).
- The target API documentation, including authentication, endpoints, request and response examples, pagination, and error behavior. An MCP client searches the internet for documentation you don't supply. Check anything it finds against the API's official documentation, since search results can be outdated or cover a different version.
- A non-production account or safe test data when the API can create, update, or delete records.

Don't paste passwords, tokens, client secrets, or other credentials into a prompt or hard-code them in connector source. Define sensitive values as connection fields and store the actual values in a Workato connection.

Confirm that your AIRO MCP connection points to the intended workspace and environment before you start, and check whether your MCP client is set to approve AIRO MCP tools without prompting.

## Example: Build a weather-alert connector

This example creates a connector for the free [National Weather Service API](https://www.weather.gov/documentation/services-web-api). The API doesn't require an API key, but it does require a `User-Agent` header that identifies the application and provides contact information.

The finished connector has:

- A connection field for a contact email.
- An action that retrieves active alerts for a state or territory.
- A polling trigger for newly issued active alerts.
- Saved versions that you can review before release.

AIRO can generate different valid implementations for the same request. As a result, the generated code, field names, and explanations may differ from the examples in this guide, even when the connector provides equivalent behavior.

### Create the connector and first action

Open AIRO and describe the connector and the first behavior to build. Include the display title and API documentation.

- **In Workato**: Ask AIRO from anywhere in the platform. AIRO takes you to the Connector SDK editor to continue. AIRO can't search the web for API documentation yet, so provide it yourself. Upload the API documentation as a PDF, MD, or TXT file, or paste it into the chat if it's under 10,000 lines. Refer to [Supported file types and size](/en/airo/chat#supported-file-types-and-size).
- **In an MCP client**: [Connect the AIRO MCP server](/en/airo/mcp) to the client, then include a link to the API documentation in your prompt, for example `<https://www.weather.gov/documentation/services-web-api>`.

The Connector SDK editor shows the AIRO chat panel beside the connector code, so you can follow each change against the source as you build.

```text
Build a custom connector named National Weather Service Alerts for the National Weather Service API. Use the National Weather Service API documentation. Set the connector's SDK `title` to `National Weather Service Alerts`. Add an action that retrieves active weather alerts for a state or territory.
```

AIRO creates the connector in your workspace immediately. It uses the API documentation to generate the connection and action, then validates the result.

> **CONNECTOR NAMING**
> 
> The connector record created in the workspace and the `title` key in the SDK source are separate. Set the SDK `title` explicitly so the intended display name appears when users select the connector in recipes.
> 
> Connector titles must be unique in a workspace. Choose a different title or add a qualifier, for example `(Custom)`, if the title is already in use.

The generated connection and request logic for this API should include a contact field, a `User-Agent` header, and the active-alerts endpoint.

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

Review the generated code, then save the change as a version.

- **In Workato**: AIRO shows each change as a diff in the editor, with **Accept** and **Reject** on every changed block. Accept or reject them individually, or click **Accept all** or **Reject all** to handle the whole set. You can also click **Apply updates** in the chat. Click **Save** afterward to create a version.
- **In an MCP client**: Ask AIRO to save the connector. AIRO validates the complete connector and returns the saved version number, which depends on the connector's save history.

![The Connector SDK editor showing four diffs, each with Accept and Reject buttons, and an Accept all and Reject all control at the bottom](/assets/accept-or-reject-changes.Rh2MH6x4.png)_Accept or reject each changed block, or handle the whole set at once_

```text
Save this connector.
```

### Add a polling trigger

Next, extend the connector with a polling trigger. You don't need to repeat the connector name because AIRO continues with the connector you're building.

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

Review the complete generated trigger, especially its cursor handling, timestamp comparison, pagination, and deduplication logic. Then apply and save the changes the same way.

## Review and test before release

AIRO checks the generated code against the Connector SDK framework and for Ruby syntax errors before you save it. Review the complete implementation and test it in Workato before you release. A successful validation doesn't replace API-specific review or runtime testing.

Complete the following checks before release:

1. **Review the complete implementation.** Use the summary AIRO returns as an overview, then open the connector from **Tools > Connector SDK** to inspect the complete code. Ask AIRO to explain any block you don't understand.
2. **Compare the implementation with the API documentation.** Verify the base URL, paths, authentication, headers, field names, request parameters, response shape, pagination, rate limits, and error responses.
3. **Create a test connection in Workato.** For this example, provide a contact email and confirm that the connection test succeeds.
4. **Check the input fields as users see them.** The **Test code** tab renders the action's input fields the way they appear in a recipe. Confirm that labels, required fields, and picklists behave as intended before you release.
5. **Run the action with safe input.** Use the SDK **Test code** tab to run the action. For example, request active alerts for `CA` and confirm that the returned fields match the declared output schema. The console tab shows output from any `puts` statements in the connector code, and the network activity shows the requests the action sent. Refer to [Test actions and triggers](/en/developing-connectors/sdk/quickstart/debugging#testing-actions-and-triggers).
6. **Test the trigger.** Verify its initial `since` behavior, cursor updates, ordering, pagination, and deduplication. Runtime testing can reveal skipped or repeated events that aren't apparent from reviewing the code alone.
7. **Confirm the target environment.** Test in a development or test environment before releasing changes that existing recipes may use.

You can also ask AIRO for a focused review before release:

```text
Review the current connector for release readiness without changing it. Compare the connection, action, and trigger with the National Weather Service API documentation. Check the authentication, request paths and parameters, input and output schemas, response mapping, pagination, cursor behavior, deduplication, and error handling. Explain any risks you find and recommend changes.
```

## Release the connector

Release the connector from the Connector SDK editor or from an MCP client.

- **In Workato**: Click **Release latest version**. Refer to [Release the latest version](/en/developing-connectors/sdk/quickstart/version-control#releasing-the-latest-version).
- **In an MCP client**: Ask AIRO to release the connector.

```text
Save and release these changes.
```

> **RELEASE HAS IMMEDIATE EFFECT IN ALL RECIPES**
> 
> Release makes a saved version the active version immediately, and every recipe that uses the connector starts using it.

AIRO reviews the unreleased changes before it releases a connector from an MCP client. It shows this warning with a summary of what's about to go live and asks you to confirm. This connector doesn't have a released version yet, so AIRO reports a first release rather than a change summary. Each release needs its own explicit confirmation, no matter what you approved earlier. You can provide your own release note, or let AIRO suggest one from the diff.

AIRO reports one of the following outcomes:

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

## Restore a previous connector state

Each change AIRO makes in the Connector SDK editor adds a **Connector state** marker and a **View update details** button to the chat. **View update details** shows only what AIRO changed in that update. Click **Connector state** to open the **View previous connector state** screen, which compares that recorded state with the current code.

![A Connector state recorded marker in the AIRO chat panel, with a Restore button beside it](/assets/connector-state-marker.CVeItrUz.png)_Click **Connector state** to compare that state with the current code, or **Restore** to return to it directly_

Click **Restore** to return the connector to that state, either beside the **Connector state** marker in the chat or in the **View previous connector state** screen. AIRO asks you to confirm, then discards all changes made after that state.

![The View previous connector state screen comparing the previous and current connector code, with a confirmation dialog asking whether to restore to the before state](/assets/restore-previous-state.SldULeI8.png)_Compare a recorded state with the current code, then click **Restore** and confirm_

> **CONNECTOR STATES AND CONNECTOR VERSIONS**
> 
> **Connector states aren't the same as connector versions.** A new connector version is only created when you click **Save**.

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

Name the connector ID, the component to change, the existing pattern to follow, and the expected result. Open the connector from **Tools > Connector SDK** and use the AIRO chat panel on the **Source code** tab. AIRO shows the proposed change as a diff in the editor. Review it, accept or reject each changed block, then click **Save** to create a version.

```text
In connector 4821, read the existing get-ticket action, then add an update-ticket action that follows the same object schema and error-handling pattern. Don't change unrelated actions. Validate the edit and summarize the exact blocks changed.
```

Use the numeric connector ID to identify the connector you mean. The connector record name and the SDK `title` can differ, so a name alone may not point AIRO at the right connector. Save your work before you switch to a different connector.

### Fix a failed save

Include the connector ID, full error text, affected component, and the most recent change.

```text
In connector 4821, the polling trigger returns the following validation error after my last edit: [paste the error]. Read the complete trigger, explain the cause, make the smallest safe correction, and validate the connector.
```

## Limitations

- AIRO can't delete a custom connector. Delete an unused connector manually. You must stop any active recipes that use the connector first. Refer to [Delete a custom connector](/en/developing-connectors/sdk/quickstart#deleting-a-custom-connector).
- A save validates the complete connector, not only the latest edit. Findings elsewhere in the source can block the save until you resolve them.

## Troubleshooting

### AIRO created or opened the connector in the wrong place

Check the workspace and environment you're working in, or the ones associated with your AIRO MCP connection. Reconnect to the intended target before you create or save anything else.

### An operation is denied

Confirm that the Workato account AIRO operates under has the required Connector SDK privileges. AIRO can't exceed the permissions granted to that account.

### A save fails on findings you didn't introduce

A save validates the complete source. Ask AIRO to list all current findings and identify which ones are outside the block you changed. Resolve the findings before saving. If you temporarily comment out code, review the functional impact before you save or release the connector.

### A save is rejected for size

Ask AIRO to identify repeated schemas or logic and reduce the source. Moving repeated field schemas into `object_definitions` is usually the largest reduction.

### AIRO can't find the connector by name

Use its numeric connector ID. Choose a unique title when another connector already uses the title you requested.

### The connection test fails even though the path looks correct

Check how `base_uri` and request paths combine. A request path that begins with `/` replaces any path segment in `base_uri`. For example, `https://host/api/v2/` combined with `/users` resolves from the host root instead of under `/api/v2/`. Use a trailing `/` in `base_uri` and omit the leading `/` from relative request paths to preserve the base path. Refer to [Configuring your base\_uri](/en/developing-connectors/sdk/sdk-reference/connection#configuring-your-base-uri).

### Release reports that the version is already current

The latest saved version was already the active version, so the release changed nothing. Expect this when you release the same saved version twice, whether from AIRO or [in Workato](/en/developing-connectors/sdk/quickstart/version-control#releasing-the-latest-version), without saving new edits in between.

### The connector was saved but recipes still use the old behavior

A saved version isn't active until it is released. Ask AIRO what changed since the last release, or open the connector in Workato and compare the latest saved version with the active released version.

---
