---
url: 'https://docs.workato.com/en/connectors/gitlab/assign-issue-to-epic-action.md'
description: The Assign an issue to epic action assigns an issue to an epic in GitLab.
---

# GitLab - Assign an issue to epic action

The **Assign an issue to epic** action assigns an issue to an epic in GitLab. If the issue belongs to another epic, the issue is unassigned from that epic.

## Input

| Input field | Description |
| --- | --- |
| Group | Select a group from the drop-down menu or enter a name. |
| Epic Internal ID | Enter the epic internal ID. |
| Issue ID | Enter the global issue ID used by the API. For example, `193053965`. |

## Output

| Output field | Description |
| --- | --- |
| ID | The top-level group ID. |
| Epic ID | The ID assigned to a parent epic. |
| Epic Work Item ID | The ID (often exposed as a Global ID) for objects managed under the unified Work Items system. |
| Epic Internal ID | The ID assigned to an epic within the context of a specific group, rather than a global, system-wide ID. |
| Epic Title | The name used to identify the epic. |
| Epic State | The epic lifecycle status. Options include `opened` and `closed`. |
| Issue ID | The ID assigned to an issue within the scope of a project. |
| Issue Internal ID | A project-specific ID that resets for every project, typically starting at 1 for the first issue created in a repository. |
| Issue Project ID | The ID that identifies the specific project where an issue resides in GitLab. |
| Issue Title | The name used to identify the issue. |
| Issue State | The current lifecycle stage of the issue. Options include `opened`, `closed`, and `locked`. |

---
