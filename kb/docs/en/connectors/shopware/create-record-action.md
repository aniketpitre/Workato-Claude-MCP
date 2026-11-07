---
url: 'https://docs.workato.com/en/connectors/shopware/create-record-action.md'
description: >-
  The Create record action enables you to create a specific record for an object
  in Shopware.
---

# Shopware - Create record action

The **Create record** action creates a record for a Shopware object. Currently, this action only supports creating product records.

## Input

| Input field | Description |
| --- | --- |
| Tax ID | Enter the unique tax identifier. This must be in UUID format. |
| Price | Specify the price of your product. |
| Net (price) | Specify the net price of the product. |
| Gross (price) | Specify the gross price of the product. |
| Currency ID (price) | Provide the unique currency identifier. This must be in UUID format. |
| Linked (price) | Select whether the product is linked or not. |
| Product number | Provide the unique number assigned to the product record to create. Define rules for the automatic assignment of every product creation per your number range. |
| Stock | Indicates the number of products available. |
| Name | Enter the name of the product. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the product. |
| Price | The price object detailing the prices of the product. |
| Product Number | The unique number of the product. |
| Restock time | The number of times the product has been restocked. |
| Currency ID | The unique currency identifier in UUID format. |
| Active | Indicates if the product is active. |
| Available | Indicates if the product is available. |
| Stock | Indicates the number of products available. |
| Translated | An object that indicates all descriptions and summaries available for the product in the language that they have been entered in. It doesn't indicate any translations of product descriptions. |

For more information on this action's output fields, refer to the [Shopware documentation](https://shopware.stoplight.io/docs/admin-api/1c10c832ff905-create-a-new-product-resources).

---

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

---
