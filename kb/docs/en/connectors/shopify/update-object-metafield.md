---
url: 'https://docs.workato.com/en/connectors/shopify/update-object-metafield.md'
description: >-
  The Update object metafield action in the Shopify connector lets you update
  the metafields associated with an object in your store.
---

# Shopify - Update object metafield action

This action updates metafields of an object in Shopify.

## Input

| Field | Description |
| --- | --- |
| Object name | Select from the picklist or input your own value. Choose from `Product`, `Customer`, `Order`, `Variant`. |
| ID | Identifier for the metafield |
| Value | Provide the value to the metafield. |
| Value type | For example, `integer`, `string` |

## Output

| Field | Description |
| --- | --- |
| ID | The ID for the metafield. |
| Key | Identifier for the metafield |
| Metafield name | Provide a name for the metafield. |
| Value | The value for the metafield |
| Value type | For example, `integer`, `string` |
| Description | The description for the metafield. |
| Owner ID | The parent object ID of the owner of the metafield. |
| Owner resource | The parent object type. |
| Created at | When this metafield was created. |
| Updated at | When this metafield was last updated. |

---
