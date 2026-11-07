---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/update-custom-record-action.md
description: >-
  The Update custom record action in the NetSuite REST connector lets you modify
  a custom record in NetSuite.
---

# NetSuite REST - Update custom record action

The **Update custom record** action allows you to modify a custom record in NetSuite REST.

Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) guide for more information.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select a NetSuite custom record type, or toggle to enter a custom value. The list populates from the custom record types located in your account at **Customization > Records > Record Types**. |
| Internal ID | The internal ID of the record to update. |

Additional optional fields appear based on the **Custom record** type you select.

## Output

| Output field | Description |
| --- | --- |
| Location | The location ID of the record updated. |
| Internal ID | The internal ID of the record updated. |
