---
url: 'https://docs.workato.com/en/connectors/shopify/search-products.md'
description: >-
  The Search products action in the Shopify connector lets you find products
  that match criteria such as vendor, title, type, or collection.
---

# Shopify - Search products action

This action searches for products in Shopify. All products that match the search criteria will be returned.

> **PRODUCT RESOURCE DEPRECATION NOTICE**
> 
> Listing, creating, updating, and deleting products is deprecated as of Shopify REST API version `2024-04`. For more information, refer to the [guide to the new product model](https://shopify.dev/docs/api/admin/migrate/new-product-model).

## Input

| Field | Description |
| --- | --- |
| Vendor | The name of the product's vendor. |
| Product title | The name of the product. |
| Product IDs | The unique product ID. You can search for multiple products using a comma-separated list of product IDs. |
| Handle | A unique human-friendly string for the product. Automatically generated from the product's title. |
| Product type | A categorization for the product used for filtering and searching products. |
| Collection ID | The collection that this product belongs to. |
| Created at (min) | Products created after this time will be retrieved. |
| Created at (max) | Products created before this time will be retrieved. |
| Updated at (min) | Products updated after this time will be retrieved. |
| Updated at (max) | Products updated before this time will be retrieved. |
| Published at (min) | Products published after this time will be retrieved. |
| Published at (max) | Products published before this time will be retrieved. |
| Published status | Select from the picklist or input your own value. Choose from `Published`, `Unpublished`, `Any`. |

## Output

The output to this action is a list of products. Each product includes the following datapills.

| Field | Description |
| --- | --- |
| ID | An unsigned 64-bit integer that's used as a unique identifier for the product. Each id is unique across the Shopify system. |
| Body html | A description of the product. Supports HTML formatting. |
| Product type | A categorization for the product used for filtering and searching products. |
| Title | The name of the product. |
| Handle | A unique human-friendly string for the product. Automatically generated from the product's title. |
| Published at | The date and time when the product was published. |
| Published scope | Whether the product is published to the Point of Sale channel. |
| Template suffix | The suffix of the Liquid template used for the product page. |
| Vendor | The name of the product's vendor. |
| Tags | A string of comma-separated tags that are used for filtering and search. A product can have up to 250 tags. Each tag can have up to 255 characters. |
| Options | The custom product property names like Size, Color, and Material. |
| Variants | A list of product variants, each representing a different version of the product. |
| Metafields | Information about metafields of the product. |
| Created at | The date and time when the product was created. |
| Updated at | The date and time when the product was last modified. |

---
