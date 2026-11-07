---
url: 'https://docs.workato.com/en/connectors/wrike/update-approval-action.md'
description: >-
  The Update approval action in the Wrike connector modifies an existing
  approval process that you identify by its ID in Wrike.
---

# Wrike - Update approval action

The **Update approval** action modifies an existing approval process in Wrike.

## Input

| Input field | Description |
| --- | --- |
| Approval ID | Enter the ID of the approval to update. |
| Description | Provide a description for the approval. |
| Due date | Set a due date for the approval. |
| Add approvers | Select a list of approver user IDs to add to the approval request. |
| Remove approvers | Select a list of approver user IDs to remove from the approval request. |
| Add attachments | Map a list of attachment IDs to include in the approval process. |
| Remove attachments | Map a list of attachment IDs to remove from the approval process. |
| Auto finish on approve? | Select **Yes** to automatically finish the approval when all approvers approve the request. Defaults to **Yes**. |
| Auto finish on reject? | Select **Yes** to automatically finish the approval when some approvers reject the request. Defaults to **Yes**. |

## Output

| Output field | Description |
| --- | --- |
| Updated approval details | List of updated approval details. |
| Approval ID | Unique identifier for the updated approval. |
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
