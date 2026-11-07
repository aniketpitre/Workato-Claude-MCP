---
url: 'https://docs.workato.com/en/connectors/shopify/get-store-metafields.md'
description: >-
  The Get store metafields action in the Shopify connector lets you retrieve all
  metafields associated with your store.
---

# Shopify - Get store metafields action

This action retrieves store metafields in Shopify.

## Input

There are no input fields for this action.

## Output

The output is a list of metafields. Each meta field includes the following datapills.

| Field | Description |
| --- | --- |
| ID | The unique ID of the metafield. |
| Key | Identifier for the metafield |
| Metafield name | A container for a set of metafields. |
| Value | The information to be stored as metadata. |
| Value type | For example, `integer`, `string`. |
| Description | A description of the information that the metafield contains. |
| Owner ID | The unique ID of the resource that the metafield is attached to. |
| Owner resource | The type of resource that the metafield is attached to. |
| Created at | The date and time when the metafield was created. |
| Updated at | The date and time when the metafield was updated. |

---
