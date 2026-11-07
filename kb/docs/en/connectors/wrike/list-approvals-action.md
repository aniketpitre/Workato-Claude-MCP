---
url: 'https://docs.workato.com/en/connectors/wrike/list-approvals-action.md'
description: >-
  The List approvals batch action in the Wrike connector retrieves a list of
  approvals and their IDs for use in later Wrike actions.
---

# Wrike - List approvals action (batch)

The **List approvals** batch action retrieves a list of approvals from Wrike. You can use approval IDs in subsequent Wrike actions.

Use the [Search approvals action](/en/connectors/wrike/search-approvals-action) to retrieve approvals with specific filters.

## Input

| Input field | Description |
| --- | --- |
| Folder ID | Enter the ID of the folder to list its associated approvals. Toggle to **Task ID** to list approvals on a specific task instead. |

## Output

| Output field | Description |
| --- | --- |
| Approvals list | List of retrieved approvals. |
| Approval ID | Unique identifier for the approval. |
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
| List size | Total number of approvals retrieved in the batch. |
| List index | Position of the current approval in the batch. |

---
