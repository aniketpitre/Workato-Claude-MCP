---
url: 'https://docs.workato.com/en/connectors/shopware/update-record-action.md'
description: >-
  The Update record action enables you to update the details of a specific
  record in the Shopware.
---

# Shopware - Update record action

The **Update record** action enables you to update the details of a specific record in the Shopware.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object type of the record you plan to update. Fields load dynamically based on the object you select. |

For example, if you select **Product** object, fields like **ID**, **Price**, **Tax ID**, **Name**, **Stock**, and **Product number** appear.

## Output

The output schema depends on the selected object. Use the output fields to map datapills to downstream steps.

For example, if you select the **Order** object, the output includes the following:

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the order. |
| Active | Indicates whether the order is active or not. |
| Customer number | The unique number of customer who placed the order. |
| Company | The company that placed the order. |
| Email | The email address of the company/customer that placed the order. |

---
