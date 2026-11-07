---
url: 'https://docs.workato.com/en/connectors/wrike/search-approvals-action.md'
description: >-
  The Search approvals batch action in the Wrike connector retrieves approvals
  that match the filters you specify for use in later actions.
---

# Wrike - Search approvals action (batch)

The **Search approvals** batch action retrieves approvals from Wrike based on specific filters. You can use approval IDs in subsequent Wrike actions.

Use the [List approvals action](/en/connectors/wrike/list-approvals-action) to retrieve approvals associated with a specific folder or task ID.

## Input

| Input field | Description |
| --- | --- |
| Statuses | Select one or more statuses to filter approvals. |
| Updated date range | Filter approvals by last update date. |
| Approvers | Select a list of approver user IDs to filter approvals in the response. |
| Pending approvers | Select a list of pending approver user IDs to filter approvals in the response. |
| Limit | Limit the number of approvals returned in the response. |
| Page size | Set the page size for the number of approvals fetched in the response. |
| Next page token | Provide the next page token from a previous **Search approvals** step to retrieve the next set of approvals. |

## Output

| Output field | Description |
| --- | --- |
| Total number of records | Total number of approvals matching the search criteria. |
| Next page token | Token for retrieving the next set of results, if applicable. |
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
