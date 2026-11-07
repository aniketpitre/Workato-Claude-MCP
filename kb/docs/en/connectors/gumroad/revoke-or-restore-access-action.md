---
url: >-
  https://docs.workato.com/en/connectors/gumroad/revoke-or-restore-access-action.md
description: >-
  Revoke or restore a buyer's access to the downloaded content for a sale in
  Gumroad.
---

# Gumroad - Revoke or restore access action

The **Revoke or restore access** action revokes or restores a buyer's access to the downloaded content for a sale in Gumroad.

## Input

| Input field | Description |
| --- | --- |
| Mode | Select **Revoke** to remove the buyer's content access, or **Restore** to re-enable it. |
| Sale ID | Select the sale whose content access you want to revoke or restore. Alternatively, enter the sale ID. |

## Output

The following are a representative set of output fields. Refer to the Gumroad [API](https://app.gumroad.com/api) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Success | A boolean value (`true` or `false`) that indicates whether the action updated the buyer's access. |
| Message | A message from Gumroad about the result. This field is blank when Gumroad doesn't return a message. |
| Sale | The sale whose content access the action updated. |
| ID (Sale) | The unique ID of the sale. |
| Email (Sale) | The buyer's email address. |
| Product ID (Sale) | The unique ID of the product. |
| Product name (Sale) | The name of the product. |
| License key (Sale) | The license key issued for the sale. |
| Created at (Sale) | The date and time the sale was created. |
| Access revoked (Sale) | A boolean value (`true` or `false`) that indicates whether the buyer's content access is revoked. |
