---
url: 'https://docs.workato.com/en/connectors/wrike/create-approval-action.md'
description: >-
  The Create approval action in the Wrike connector starts an approval process
  for a folder or task that you specify.
---

# Wrike - Create approval action

The **Create approval** action starts a Wrike approval process for a folder or task that you specify.

## Input

| Input field | Description |
| --- | --- |
| Folder ID | Enter the ID of the folder where the approval is created. Toggle to **Task ID** to create approval on a task instead. This field is required. |
| Description | Provide a description for the approval. |
| Due date | Set a due date for the approval. |
| Approvers | Select a list of approver user IDs to assign to this approval request. If left blank, the approval is created in **draft** status. |
| Attachments list | Map a list of attachment IDs to include in the approval process. |
| Auto finish on approve? | Select **Yes** to automatically finish the approval when all approvers approve the request. Defaults to **Yes**. |
| Auto finish on reject? | Select **Yes** to automatically finish the approval when some approvers reject the request. Defaults to **Yes**. |

## Output

| Output field | Description |
| --- | --- |
| Approval ID | Unique identifier for the created approval. |
| Task ID | Unique identifier for the associated task, if applicable. |
| Folder ID | Unique identifier for the associated folder. |
| Author ID | Unique identifier of the user who created the approval. |
| Title | Name of the approval. |
| Description | Description of the approval, if applicable. |
| Updated date | Timestamp indicating when the approval was last updated. |
| Due date | Timestamp indicating when the approval is due. |
| Review ID | Unique identifier for the associated review. |
| Decisions | List of decisions made on the approval. |
| Status | Current status of the approval. |
| Attachment IDs | List of attachments associated with the approval. |
| Type | Type of approval. |
| Auto finish on approve | Indicates whether the approval automatically finishes when approved. |
| Auto finish on reject | Indicates whether the approval automatically finishes when rejected. |
| Finished | Indicates whether the approval is marked as finished. |
| Finisher ID | Unique identifier of the user who finalized the approval. |

---
