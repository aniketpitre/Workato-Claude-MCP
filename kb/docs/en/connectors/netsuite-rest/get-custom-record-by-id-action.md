---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/get-custom-record-by-id-action.md
description: >-
  The Get custom record by ID action in the NetSuite REST connector lets you
  fetch a custom record by using the internal ID from NetSuite.
---

# NetSuite REST - Get custom record by ID action

The **Get custom record by ID** action allows you to fetch a custom record using the internal ID from NetSuite REST.

Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) guide for more information.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select a NetSuite custom record type, or toggle to enter a custom value. The list populates from the custom record types located in your account at **Customization > Records > Record Types**. |
| Internal ID | Provide the internal ID of the record to fetch. |

## Output

The output fields depend on the **Custom record** type you select. Common fields include the following:

| Output field | Description |
| --- | --- |
| Last modified by | The user who last modified the record. |
| Links | The related resource links for the record. |
| Owner | The owner of the record. |
| Reference Name | The reference name of the record. |

Additional fields appear based on the **Custom record** type you select.
