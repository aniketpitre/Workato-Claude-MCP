---
url: >-
  https://docs.workato.com/en/connectors/gumroad/enable-or-disable-license-action.md
description: >-
  Enable or disable a license key for a product in Gumroad. A disabled license
  key fails verification.
---

# Gumroad - Enable or disable license action

The **Enable or disable license** action enables or disables a license key for a product in Gumroad. A disabled license key fails verification.

## Input

| Input field | Description |
| --- | --- |
| Mode | Select **Enable** to activate the license key, or **Disable** to deactivate it. |
| Product ID | Select the product the license key belongs to. Alternatively, enter the product ID. |
| License key | Enter the license key to enable or disable. |

## Output

The following are a representative set of output fields. Refer to the Gumroad [API](https://app.gumroad.com/api) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Success | A boolean value (`true` or `false`) that indicates whether the action updated the license key. |
| Message | A message from Gumroad about the result. This field is blank when Gumroad doesn't return a message. |
| Uses | The number of times the license key has been used. |
| Purchase | The purchase the license key belongs to. |
| Sale ID (Purchase) | The unique ID of the sale. |
| Product ID (Purchase) | The unique ID of the product. |
| Product name (Purchase) | The name of the product. |
| Email (Purchase) | The buyer's email address. |
| License key (Purchase) | The license key for the purchase. |
| Refunded (Purchase) | A boolean value (`true` or `false`) that indicates whether the sale was refunded. |
