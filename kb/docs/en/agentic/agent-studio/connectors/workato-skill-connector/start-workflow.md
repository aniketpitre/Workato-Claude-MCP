---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow.md
description: >-
  Receives a request from a calling AI system. Declares the input parameters the
  AI system supplies and the result schema it expects in return.
---

# Workato Skill connector - Start workflow trigger (real-time)

The **Start workflow** real-time trigger runs a recipe when a Workato Agent, MCP client, or other AI system calls the skill. The trigger declares the input parameters the caller must supply, the result schema it expects to receive, and any optional task metadata the skill receives.

The recipe editor opens with the **Start workflow** trigger by default when you create a skill. After you configure the trigger, you can replace it with a different trigger to run the recipe from an external event instead of an agent invocation. Replacing the trigger removes the recipe from any assigned genies and MCP servers.

## Input

| Input field | Description |
| --- | --- |
| Require user confirmation before executing skill? | Select whether the agent prompts the user for confirmation before it runs the skill. Use this option for skills that perform destructive or high-impact actions, such as updating customer records. Refer to [User confirmation](/en/agentic/skills/user-confirmation) for more information. |
| When should this skill run? | Enter a natural-language description of the skill. The AI system reads this description to decide when to call the skill. Write it from the AI system's perspective and include any context that helps it decide. Refer to [Skill design best practices](/en/agentic/skills/skill-design-best-practices) for best practices. |
| What inputs does this skill need to run? | Define the parameters the calling AI system provides when it runs the skill. Use JSON or add fields manually. Add a hint to each field to help the AI system fill it in correctly. Refer to the [File inputs](#file-inputs) section for information about how the AI system processes file parameters. |
| What information does this skill send back? | Define the output fields for this skill. Use JSON or add fields manually. After setting up all your actions, map the datapills to these fields in the **Return response** action. |
| Task metadata | Optional. Define the task metadata this skill receives from an agent when used with the [Assign task to genie](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/assign-task-to-genie) action in the Workato Genie connector. Tasks assigned to genies can include metadata, such as a customer ID or ticket number. The names defined here must exactly match the names in the **Assign task to genie** action. |

### File inputs

The agent passes a file reference to the skill instead of raw bytes when you add a **File** to the input parameter schema. The connector resolves the reference into a file object with `name`, `created`, `file_contents`, `file_type`, and `size` datapills you can use in subsequent recipe steps.

This pattern lets agents pass uploaded files, such as a PDF attached in Slack or an image dropped into Workato GO, into the skill. It also avoids inflating the agent's context window with binary content.

Refer to [Create a skill with a File input parameter](/en/agentic/agent-studio/upload-files-and-images#create-a-skill-recipe-with-a-file-input-parameter) for setup steps.

## Output

| Output field | Description |
| --- | --- |
| Parameters | The values the calling AI system supplied for this skill call. The schema for this object is defined in the **What inputs does this skill need to run?** input field. |
| Context | Information about the calling agent and the user that invoked it. Refer to [Context fields](#context-fields) for the available sub-fields. |
| Custom metadata | The task metadata attributes the calling agent supplied for this skill call. The schema for this object is defined in the **Task metadata** input field. |

### Context fields

The **Context** output field contains the following information about the calling agent and the user that invoked the skill:

- Genie ID
  
- The ID of the genie that called the skill.
  
- Genie name
  
- The display name of the genie that called the skill.
  
- Conversation ID
  
- The ID of the conversation in which the skill was called.
  
- Call ID
  
- The ID of the specific skill call.
  
- App type
  
- The chat application the user invoked the agent from, such as Slack or Microsoft Teams.
  
- App user ID
  
- The user's ID in the chat application.
  
- User ID
  
- The user's Workato user ID.
  
- User name
  
- The user's full name.
  
- User email
  
- The user's email address.
  
- User group IDs
  
- The Workato user group IDs the user belongs to.
  

You can use these fields to personalize skill behavior or enforce context-aware authorization. For example, you can use User group IDs to restrict destructive actions based on group membership.
