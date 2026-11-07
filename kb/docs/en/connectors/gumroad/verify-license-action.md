---
url: 'https://docs.workato.com/en/connectors/gumroad/verify-license-action.md'
description: >-
  Verify a license key for a product in Gumroad and optionally avoid consuming a
  use.
---

# Gumroad - Verify license action

The **Verify license** action verifies a license key for a product in Gumroad. Each verification increments the license key's use count by default.

## Input

| Input field | Description |
| --- | --- |
| Product ID | Select the product the license key belongs to. Alternatively, enter the product ID. |
| License key | Enter the license key to verify. |
| Increment uses count | Optional. Set to `false` for a read-only check that doesn't consume a use. Defaults to `true` if left blank. |

## Output

The following are a representative set of output fields. Refer to the Gumroad [API](https://app.gumroad.com/api) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Success | A boolean value (`true` or `false`) that indicates whether the license key is valid. |
| Message | A message from Gumroad about the result. This field is blank when Gumroad doesn't return a message. |
| Uses | The number of times the license key has been used. |
| Purchase | The purchase the license key belongs to. |
| Sale ID (Purchase) | The unique ID of the sale. |
| Product ID (Purchase) | The unique ID of the product. |
| Product name (Purchase) | The name of the product. |
| Email (Purchase) | The buyer's email address. |
| License key (Purchase) | The license key for the purchase. |
| Refunded (Purchase) | A boolean value (`true` or `false`) that indicates whether the sale was refunded. |

---
