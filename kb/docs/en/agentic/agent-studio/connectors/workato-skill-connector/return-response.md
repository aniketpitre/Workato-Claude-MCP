---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-skill-connector/return-response.md
description: Ends a skill and sends a result to the calling AI system.
---

# Workato Skill connector - Return response action

The **Return response** action ends a skill and sends a result to the calling AI system. Include this action as the last step of every skill. Any steps that follow it don't run because this action terminates the job. The calling AI system receives no structured response and the skill call fails if a skill doesn't include this action.

> **PREREQUISITES**
> 
> You must configure the [Start workflow](/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow) trigger before configuring this action. The trigger defines the fields available in the **Response** field.

## Input

| Input field | Description |
| --- | --- |
| Response | Enter the values to return to the calling AI system. The fields in this object are defined in the **What information does this skill send back?** field of the [Start workflow](/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow) trigger. |

## Output

| Output field | Description |
| --- | --- |
| Response | Echoes the values returned to the calling AI system. Use this output if a downstream step needs to log or post-process what the skill sent back. |

## Stream large results

The **Return response** action has a maximum response size of 250 KB. Responses that exceed 250 KB cause the action to fail with a `Result is too big` error. Reduce the response size to stay under the quota.

Alternatively, pass the content as a streamable datapill, such as a File contents datapill, into the response field. Workato automatically streams the content to the calling AI system in chunks. Refer to [File streaming](/en/features/file-streaming) for more information about streamable datapills.

## Binary content

Result fields don't support binary file content. To work around this limitation, upload the file earlier in the recipe to a file storage location your agent can access, such as Workato file storage, Amazon S3, or Google Drive. Then return the file URL or ID as a string field. The agent retrieves the file using that reference. This pattern keeps the result payload small and avoids the 250 KB result size quota.
