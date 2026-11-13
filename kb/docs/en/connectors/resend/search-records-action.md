---
url: 'https://docs.workato.com/en/connectors/resend/search-records-action.md'
description: Retrieve a list of emails or sending domains from Resend.
---

# Resend - Search records action

The **Search records** action retrieves a list of records from Resend. Select **Email** to list emails or **Domain** to list sending domains.

## Input

Input fields dynamically generate based on the **Object type** you select.

| Input field | Description |
| --- | --- |
| Object type | Select the type of record to search. Options are **Email** or **Domain**. |
| Limit | Optional. Enter the number of records to return, from `1` to `100`. Defaults to `20` if left blank. |
| After | Optional. Enter the ID of the record after which to return results. You can't use this field with **Before**. Leave blank to start from the first record. |
| Before | Optional. Enter the ID of the record before which to return results. You can't use this field with **After**. |

## Output

Output fields dynamically generate based on the **Object type** you select. Refer to the Resend [API](https://resend.com/docs/api-reference/introduction) documentation for more information on available output fields. The following fields are common to all objects:

| Output field | Description |
| --- | --- |
| Object | The type of response. For example, `list`. |
| Has more | Whether more records exist beyond the ones returned. |
| Records | The list of records that match the search. |
| Email ID or Domain ID (Records) | The unique ID of the record. The field appears as **Email ID** for emails and **Domain ID** for domains. |
| Created at (Records) | The date and time the record was created. |

---
