---
url: 'https://docs.workato.com/en/connectors/shopify/create-product.md'
description: >-
  The Create product action in the Shopify connector lets you create a product
  with details such as title, type, variants, options, and tags.
---

# Shopify - Create product action

This action creates a product in Shopify.

> **PRODUCT RESOURCE DEPRECATION NOTICE**
> 
> Listing, creating, updating, and deleting products is deprecated as of Shopify REST API version `2024-04`. For more information, refer to the [guide to the new product model](https://shopify.dev/docs/api/admin/migrate/new-product-model).

## Input

| Field | Description |
| --- | --- |
| Variants | If this product contains variants, provide information about the product variants. You can add product variants at a later time using the [Create product variant action](/en/connectors/shopify/create-product-variant). |
| Body html | A description of the product. Supports HTML formatting. |
| Product type | A categorization for the product used for filtering and searching products. |
| Title | The name of the product. |
| Handle | A unique human-friendly string for the product. Automatically generated from the product's title. |
| Published at | The date and time when the product was published. |
| Published scope | Whether the product is published to the Point of Sale channel. |
| Template suffix | The suffix of the Liquid template used for the product page. |
| Vendor | The name of the product's vendor. |
| Tags | A string of comma-separated tags that are used for filtering and search. A product can have up to 250 tags. Each tag can have up to 255 characters. |
| Options | The custom product property names like Size, Color, and Material. You can add up to 3 options of up to 255 characters each. |

## Output

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
