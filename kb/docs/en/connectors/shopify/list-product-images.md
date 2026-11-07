---
url: 'https://docs.workato.com/en/connectors/shopify/list-product-images.md'
description: >-
  The List product images action in the Shopify connector lets you retrieve a
  list of images attached to a product.
---

# Shopify - List product images action

This action retrieves a list of images attached to a product on Shopify.

## Input

| Field | Description |
| --- | --- |
| Product ID | The ID of the product to which the images are attached. |
| Fetch results after ID | Optional. When provided, only images with IDs following this ID are retrieved. |
| Return full data | Optional. If set to `yes/1`, the entire product image source is returned. Defaults to `false/0`. |

## Output

The output is a list of product image IDs if **Return full data** is set to `false`. Else, we should return a list of datatree that contains information about the product image object.

Learn more about the [product image object](https://shopify.dev/api/admin-rest/2024-04/resources/product-image#resource-object).

---
