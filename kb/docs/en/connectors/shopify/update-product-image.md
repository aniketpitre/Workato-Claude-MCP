---
url: 'https://docs.workato.com/en/connectors/shopify/update-product-image.md'
description: >-
  The Update product image action in the Shopify connector lets you update the
  image data of an existing product image.
---

# Shopify - Update product image action

This action updates the image data of a product image.

## Input

| Field | Description |
| --- | --- |
| Product ID | The ID of the product to which the images are attached. |
| Image ID | The ID of the image to be updated. |
| Position | Optional. The placement of this new image among other existing product images. 1 denotes primary image. By default the position is 1 (primary image). |
| Alt text | Optional. The alt tag of the image. |
| Variant IDs | Optional. The list of IDs of the product variants to attach the product image to. |

## Output

The output of this action is a datatree that contains information about the product image object.

Learn more about the [product image object](https://shopify.dev/api/admin-rest/2024-04/resources/product-image#resource-object).

---
