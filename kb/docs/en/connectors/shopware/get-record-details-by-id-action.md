---
url: >-
  https://docs.workato.com/en/connectors/shopware/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action enables you to retrieve details about a
  specific record in Shopware.
---

# Shopware - Get record details by ID action

The **Get record details by ID action** enables you to retrieve details about a specific record in Shopware.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve its details. Fields load dynamically based on the object you select. |
| ID | Enter the unique identifier of the object to retrieve data for. |

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
