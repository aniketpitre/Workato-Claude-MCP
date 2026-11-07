---
url: 'https://docs.workato.com/en/connectors/felix/suspend-vendor-action.md'
description: >-
  The **Suspend vendor** action suspends a vendor that is currently approved and
  not suspended.
---

# Felix - Suspend vendor action

The **Suspend vendor** action suspends a vendor that is currently approved and not suspended.

## Input

| Input field | Description |
| --- | --- |
| Vendor Id | Required. Enter the numeric ID of the vendor to suspend. Must be an integer. |
| Comment | Optional. Enter a comment with the reason for suspension. Must be a string. |

## Output

| Output field | Description |
| --- | --- |
| Code | The error code associated with the job. Is either `204` or `422`. |
| Message | The message associated with the error code. Such as `Vendor is not approved`. |

---
