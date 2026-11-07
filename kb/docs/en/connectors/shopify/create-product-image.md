---
url: 'https://docs.workato.com/en/connectors/shopify/create-product-image.md'
description: >-
  The Create product image action in the Shopify connector lets you upload and
  attach an image to an existing product.
---

# Shopify - Create product image action

This action will upload and attach an image to an existing product.

## Input

| Field | Description |
| --- | --- |
| Product ID | The ID of the product to which the image is attached. |
| Image data | The image to be uploaded, which can be in the form of either the data string or the URL from which the image can be downloaded. |
| Image file name | Optional. The name of the image file. |
| Position | Optional. The placement of this new image among other existing product images. 1 denotes primary image. By default the position is 1 (primary image). |
| Alt text | Optional. The alt tag of the image. |
| Variant IDs | Optional. The list of IDs of the product variants to attach the product image to. |

## Output

The output of this action is a datatree that contains information about the new product image object.

Learn more about the [product image object](https://shopify.dev/api/admin-rest/2024-04/resources/product-image#resource-object).

---
