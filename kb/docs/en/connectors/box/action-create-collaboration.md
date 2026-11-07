---
url: 'https://docs.workato.com/en/connectors/box/action-create-collaboration.md'
description: >-
  The Create collaboration action creates a collaboration on a file or folder in
  Box.
---

# Box - Create collaboration action

The **Create collaboration** action creates a collaboration on a file or folder in Box. You can invite users or groups, assign roles, and control whether collaborators can view folder paths. A business or enterprise Box account is required to collaborate with groups. Inviting a group to collaborate doesn't generate an email notification.

## Input

| Input field | Description |
| --- | --- |
| Item | Specify the item to collaborate on. |
| File or folder ID | Enter the ID of the file or folder. You can find this at the end of the Box URL. |
| Group ID | Enter the group ID from the Box Admin console. Required if collaborating with a group. |
| Email ID of collaborator | Enter the email ID of the collaborator. The collaborator doesn't need an existing Box account. |
| Notify | Select whether to send a notification email to the user. |
| Role | Enter the role for the collaborator. |
| Can view path | Set to `Yes` to allow the collaborator to see the full ancestral path of the folder. This applies only to folders. |

## Output

| Output field | Description |
| --- | --- |
| Type | Type of the collaboration object. |
| ID | Unique identifier of the collaboration. |
| Created by | User who created the collaboration. |
| Created at | Timestamp when the collaboration was created. |
| Modified at | Timestamp when the collaboration was last modified. |
| Expires at | Timestamp when the collaboration expires, if applicable. |
| Acknowledged at | Timestamp when the collaboration was acknowledged. |
| Status | Status of the collaboration. |
| Accessible by | User or group granted access. |
| Role | Role assigned to the collaborator. |
| Item | File or folder that the collaboration applies to. |

---
