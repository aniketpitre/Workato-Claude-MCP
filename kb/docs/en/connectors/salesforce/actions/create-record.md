---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/create-record.md'
description: This action creates a record in Salesforce.
---

# Salesforce - Create record action

This action creates a record in Salesforce.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to create. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

Additional fields load dynamically based on the selected object. Use these fields to specify the contents of the new record.

## Output

| Output fields | Description |
| --- | --- |
| Object ID | The Salesforce ID of the newly created object. |

---
