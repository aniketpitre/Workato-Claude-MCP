---
url: 'https://docs.workato.com/en/connectors/pardot/search-objects-action.md'
description: >-
  Search for objects in Salesforce Account Engagement (Pardot), such as
  prospects or email templates.
---

# Salesforce Account Engagement (Pardot) - Search objects action

The **Search objects** action retrieves objects from Salesforce Account Engagement (Pardot) that match your search criteria, such as prospects or email templates.

## Input

Input fields dynamically generate based on the object you select. Refer to the Salesforce [Account Engagement API](https://developer.salesforce.com/docs/marketing/pardot/overview) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object type | Select the object to search for. |

## Output

Output fields dynamically generate based on the object you select. Refer to the Salesforce [Account Engagement API](https://developer.salesforce.com/docs/marketing/pardot/overview) documentation for more information on available output fields. The following fields are common to all objects.

| Output field | Description |
| --- | --- |
| Results | The objects that match your search. In API version 5, the field name matches the object you select, such as **Lists**. |
| Next page token | The token to retrieve the next page of results. The **Next page token** field is only available in API version 5. |
| Next page URL | The URL to retrieve the next page of results. The **Next page URL** field is only available in API version 5. |

---
