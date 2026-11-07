---
url: 'https://docs.workato.com/en/agentic/skills/skill-design-best-practices.md'
description: >-
  Learn best practices for designing reliable skills that genies invoke
  correctly, receive the right inputs, and execute without failure.
---

# Skill design best practices

A genie is only as reliable as the skills it can access. A well-designed skill is invoked correctly, receives the right inputs, executes reliably, and returns exactly what the genie needs to continue the conversation. A poorly designed skill is invoked inconsistently, receives wrong or missing inputs, fails in hard-to-diagnose ways, and returns data the genie can't use effectively.

Most skill failures aren't LLM failures. They're design failures due to skills built around the wrong abstraction or the wrong input model that returns too much data. This page covers best practices for designing reliable skills.

## Design around user intent

The most common skill design mistake is building skills that mirror API endpoints rather than user intents. An API has create, read, update, and delete endpoints, so the builder creates four skills, one per endpoint. This seems logical, but produces a genie that forces users to think in terms of API operations rather than business outcomes.

A user doesn't want to `call the GET /accounts/{id} endpoint`. A user wants to `get an account summary before a call`.

Design each skill around what the user is trying to achieve, not what the underlying API exposes. A **Get Account Summary** skill should aggregate internally, call multiple Salesforce objects in the recipe and return a single clean object that contains everything the genie needs. The user and the genie see one skill that does one thing. The recipe handles the API complexity internally.

This best practice has three practical implications:

- **One skill per user intent, not one skill per API call**: A user's goal that requires calling three APIs should be handled inside one skill, not spread across three skills the genie has to chain together.
- **Name skills after what they do for the user, not what they do to the API**: **Get Account Summary in Salesforce** is a well-named skill. **GET accounts id opportunities contacts** isn't. The skill name is part of what the LLM reads when deciding whether to invoke it.
- **Return what the genie needs, not what the API returns**: The raw API response is typically not the correct skill output. Filter, transform, and aggregate inside the recipe before returning the result to the genie.

## Use business identifiers as inputs

Use business identifiers as inputs rather than internal IDs. An LLM can't manufacture internal system IDs, and doesn't know that the Salesforce account `Acme Corp` has the internal ID `001Hs00000KlMnOPQ`. A genie recognizes the business name when a user requests `get the Acme Corp account`, but it won't recognize the internal ID.

Skill inputs should use identifiers that users can provide naturally in conversation, such as account names, email addresses, ticket summaries, or product names. If the underlying API requires an internal ID, the skill should resolve the business identifier to the internal ID internally before calling the API.

**Recommended** ✅

```plaintext
Input: account_name (string)
Hint: The name of the account as it appears
      in Salesforce. Example: "Acme Corp".
      Use the account name from the user's
      message or from earlier in the
      conversation.
```

The recipe then searches Salesforce for the account by name, retrieves the internal ID, and uses it for the subsequent API call. The genie and the user don't see the internal ID.

This principle applies to all identifier types. User IDs should be resolved from email addresses. Ticket IDs should be resolved from ticket summaries or keys. Product IDs should be resolved from product names. Build the resolution logic into the skill and keep the genie's inputs in the language of business, not the language of APIs.

**Not recommended** ❌

```plaintext
Input: account_id (string)
Hint: The Salesforce internal account ID
      (18-character alphanumeric string)
```

## Filter skill output

Output should be lean and filtered. The LLM's context window is finite. Every field that a skill returns consumes context window space. A skill that returns the full API response object, with all fields, nested objects, metadata, and system fields, wastes context on data the genie doesn't use, reduces the space available for conversation history and other skill outputs, and can degrade response quality.

Explicitly filter the output to include only the fields the genie needs for the specific use case before the **Return response** step in every skill.

List the fields the genie needs to reason about or present to the user. Include only those fields in the output. Leave out fields you're not sure about. You can add fields if testing reveals something is missing.

Three field categories to exclude:

- **Internal system fields**: IDs, checksums, API version markers, and internal timestamps used for system operations. The genie doesn't need these.
- **Fields the user doesn't see**: Configuration fields, system flags, and audit metadata. Values shouldn't be in the output if the genie doesn't include the fields in a response to the user.
- **Redundant fields**: If the output includes both a formatted label and a raw value for the same data, such as `priority_label: High` and `priority_code: 3` include only the value the genie needs. Typically the genie needs the label.

## Return source URLs when citing knowledge

Include the source URL in the output when a skill retrieves information the genie may use to answer a user's question, such as a knowledge base article, a Confluence page, a policy document, or a support ticket. The genie uses this URL to cite its sources when presenting information to the user.

A genie that says `according to the Annual Leave Policy (link)` is more trustworthy than one that states a fact without attribution. Users who can verify the source are more likely to trust the answer and less likely to escalate to a human unnecessarily.

Include the source URL as a dedicated field in the skill output, not embedded in a text field. A dedicated field makes it easy for the genie to reference it consistently and for the skill description's output requirements to specify how it should be used.

## Log identifiers for downstream app events

Some skills create or retrieve records that may need to be referenced in a future conversation, such as a ticket that was created, an approval that was submitted, or an opportunity that was updated. For these skills, store the record's identifier and the current conversation ID in a data table before the skill returns its result.

This logging step makes app event-triggered follow-ups possible. When the ticket status changes and a recipe fires an app event to notify the user, it needs the conversation ID to resume the correct thread. There's no way to connect the external event back to the genie conversation where the record was created without the logging step.

The logging step belongs in the skill, between the API call and the return response step. It should store the following information at minimum:

- **External record identifier**: The ticket ID or the opportunity ID
- **Workato conversation ID**: Generated from the [Start workflow](/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow) trigger
- Requester's email or user ID
- Creation timestamp

This is a small addition to any skill but has significant downstream value for use cases that involve follow-up events on records created through the genie.

## Keep skills atomic

An atomic skill does one thing. It achieves one user intent, with one primary action, and returns one coherent result. Skills that try to do multiple things, such as creating a record, sending a notification, and logging the outcome, are harder to test, debug, and invoke correctly.

Decide whether actions belong in one skill or in a chain of skills when a use case requires multiple actions. The right choice depends on whether each action has independent value:

- **Actions are performed together and individually meaningless**: For example, a create action followed immediately by a notification should be one skill and handled internally.
- **Actions have independent value**: For example, creating a record and then optionally sending a notification should be separate skills that the genie chains based on user input.

The atomic principle doesn't mean skills must be simple. A **Get Account Summary** skill that calls five Salesforce objects and returns an aggregated result is complex internally but atomic from the genie's perspective. It does one thing. The complexity is contained inside the recipe.

## Design for reuse across genies

Skills can be assigned to multiple genies in any project. A **Create Ticket in Jira** skill built for an IT genie can also be assigned to an HR genie that needs to create IT tickets on behalf of employees. A **Get Account Summary in Salesforce** skill built for a sales genie can also be used by a customer success genie.

Keep the following in mind when building skills intended for reuse:

- **Use generic inputs where possible**: A skill that accepts a user email as input is more reusable than one hardcoded to retrieve data for a specific user. Parameterize anything that might vary across genies or use cases.
- **Avoid genie-specific logic in skills**: Logic that only applies to one genie's use case should be in the skill description or the job description, not hardcoded in the recipe. A recipe with hardcoded filters is harder to reuse than one that accepts filter parameters.
- **Name skills generically**: **Create Ticket in Jira** is reusable. **Create IT Helpdesk Ticket in Jira for IT Genie** isn't. The name should describe what the skill does, not which genie it was built for.

## Validate inputs before calling external systems

Add input validation steps at the beginning of skills, before an external API call, to catch obvious errors early. Validation steps that run in Workato are faster and cheaper than API calls that return errors from external systems.

Common validations include the following:

- **Required field presence**: Confirm that all required fields have been provided before proceeding. If a required field is missing, return an error message the genie can relay to the user. For example: `I need the start date to submit the leave request. Could you provide that?`
- **Format validation**: Confirm that date fields are in the expected format, that email addresses match a valid pattern, and that numeric fields are within expected ranges. A date passed as `next Monday` rather than `2026-04-14` can cause the API call to fail. Catching this in the recipe before the API call produces a cleaner error message.
- **Business rule validation**: Skills with write operations should validate business rules before calling the API. A leave request with a start date in the past should be flagged before the HR system rejects it. A discount above the approval threshold should trigger the approval workflow rather than being applied directly.

Validation failures should return a structured error message the genie can use to continue the conversation, asking the user to correct the input, rather than a raw API error the genie can't interpret meaningfully.

## Skill design for verified user access

Verified user access has a few practical implications for how skills are designed:

- **Don't ask users for their email or ID in the conversation**: The user's identity is available from the skill trigger context when verified user access is enabled. Field hints on identity-related inputs should specify: `Use the authenticated user email from the Skill trigger context - don't ask the user for their email address`. Asking users to provide their own identity in conversation is both unnecessary with verified user access and a security risk without.
  
- **Design for the first-time authentication experience**: The first time a user triggers a skill with verified user access enabled, they are prompted to authenticate. This is expected, but it can surprise users who didn't expect a connection prompt mid-conversation. The job description can include a note for the genie to prepare users: `Before using any skills that require your personal credentials, you may be asked to connect your account. This is a one-time step`.
  
- **Test skills with verified user access with a non-builder user account**: [Test mode](/en/agentic/agent-studio/test-genie) uses the builder's identity and credentials. Verified user access behavior, including the connection prompt, the child connection creation, and the scoped data retrieval, can only be fully tested by interacting with the genie as a real end user from the chat interface. Test skills using verified user access with a non-builder test account before deploying to production users.

---
