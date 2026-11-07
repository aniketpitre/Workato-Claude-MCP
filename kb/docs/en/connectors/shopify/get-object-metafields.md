---
url: 'https://docs.workato.com/en/connectors/shopify/get-object-metafields.md'
description: >-
  The Get object metafields action in the Shopify connector lets you retrieve
  the metafields associated with an object in your store.
---

# Shopify - Get object metafields action

This action retrieves metafields about an object in Shopify.

## Input

| Field | Description |
| --- | --- |
| Object name | Select from the picklist or input your own value. Choose from `Product`, `Customer`, `Order`, `Variant`. |

## Output

The output is a list of metafields. Each metafield includes the following datapills.

| Field | Description |
| --- | --- |
| ID | The unique ID of the metafield. |
| Key | Identifier for the metafield |
| Metafield name | A container for a set of metafields. |
| Value | The information to be stored as metadata. |
| Value type | For example, 'integer', 'string' |
| Description | A description of the information that the metafield contains. |
| Owner ID | The unique ID of the resource that the metafield is attached to. |
| Owner resource | The type of resource that the metafield is attached to. |
| Created at | The date and time when the metafield was created. |
| Updated at | The date and time when the metafield was updated. |

---
