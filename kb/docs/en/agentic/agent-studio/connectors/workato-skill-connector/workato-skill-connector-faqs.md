---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector-faqs.md
description: >-
  Frequently asked questions about the Workato Skill connector and the
  transition from the Workato Genie connector.
---

# Workato Skill connector - FAQs

Get answers to frequently asked questions about the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) and the transition from the Workato Genie connector.

Will my existing skills break?

No. Existing skills built on the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector) continue to function and remain available for assignment to genies.

The Workato Genie connector **Start workflow** trigger and **Return response** action are deprecated. They continue to work, but they don't receive new enhancements.

Do I have to migrate?

No. Migration is optional and at your own pace. New skills automatically use the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) regardless of where you create them. Refer to [Migrate an existing skill](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector#migrate-an-existing-skill) for the steps.

What happens when I create a new skill?

New skills automatically use the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) regardless of where you create them.

Will pre-built MCP servers I've already added change?

No. Existing pre-built MCP servers are unchanged. Newly added pre-built MCP servers will use the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector).

Can I use skills if I'm an MCP-only customer?

Yes. Customers on Business MCP and Enterprise MCP plans can create and use skills without an Agent Studio license.

Can I assign skills built on the Workato Skill connector to a genie?

Yes. Skills built on the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) are assignable to genies, just like skills built on the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector). The genie builder lists both skill types.

Can I change the trigger of a skill after creation?

Yes. Workato sets the **Start workflow** trigger as the default when you create a skill. However, after you configure the trigger, you can replace it with a different trigger to run the recipe from an external event instead of an agent invocation. This differs from skills built on the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector), where the trigger was fixed.

Replacing the **Start workflow** trigger permanently removes the skill from any genies and MCP servers it was assigned to, and you can't undo this action. The recipe editor prompts you for confirmation before you make this change. The fields defined in the original trigger's result schema remain available in the **Return response** action.

What's the maximum response size from a skill?

The **Return response** action has a maximum response size of 250 KB. You can pass larger results as a streamable datapill to work around this limitation. Refer to [Stream large results](/en/agentic/agent-studio/connectors/workato-skill-connector/return-response#streaming) for more information.

Can a skill return binary file content?

No. Result fields don't support binary file content. To work around this limitation, upload the file earlier in the recipe to a file storage location your agent can access, such as Workato file storage, Amazon S3, or Google Drive. Then return the file URL or ID as a string field. The agent retrieves the file using that reference.

Does the Developer API for skills still work?

Yes. The Developer API supports skills built on either the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector) or the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector). Refer to [Skills](/en/workato-api/agent-studio#skills) in the Workato API reference for endpoint details.
