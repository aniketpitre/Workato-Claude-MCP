---
url: 'https://docs.workato.com/en/connectors/pardot/get-object-details-action.md'
description: >-
  Retrieve the details of an object from Salesforce Account Engagement (Pardot),
  such as a prospect or email template.
---

# Salesforce Account Engagement (Pardot) - Get object details action

The **Get object details** action retrieves the details of an object in Salesforce Account Engagement (Pardot), such as a prospect or email template.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the object to retrieve. |
| ID | Enter the unique ID of the object to retrieve. |
| Fields | Enter the fields to return, separated by commas. |

## Output

Output fields dynamically generate based on the object you select. Refer to the Salesforce [Account Engagement API](https://developer.salesforce.com/docs/marketing/pardot/overview) documentation for more information on available output fields. The following field is common to all objects.

| Output field | Description |
| --- | --- |
| ID | The object's unique ID. |

---
