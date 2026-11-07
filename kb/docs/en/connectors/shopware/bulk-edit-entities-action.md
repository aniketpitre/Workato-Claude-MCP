---
url: 'https://docs.workato.com/en/connectors/shopware/bulk-edit-entities-action.md'
description: >-
  The Bulk edit entities action enables you to upsert or delete multiple records
  for an object in a single call.
---

# Shopware - Bulk edit entities action

The **Bulk edit entities** action enables you to upsert or delete multiple records for an object in a single call.

## Input

| Input field | Description |
| --- | --- |
| Entity | Select the object for which you intend to upsert/delete records. |
| Action | Select the action you intend to perform over the records of the object selected. Options include upsert or delete. |
| Payload | Enter the required payload for the selected action. |
| Indexing behaviour | Select whether to use queue indexing or disable indexing. |
| Fail on error | Specify whether the step in the recipe should fail on error or not. |

## Output

The output schema depends on the selected object. Use the output fields to map datapills to downstream steps.

For example, if you select the **Customer** object, the output includes the following:

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the customer. |
| Active | Indicates whether the customer is active or not. |
| Customer number | The unique number of the customer. |
| Company | The company that the customer represents. |
| Email | The email address of the customer. |

---
