---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/create-custom-record-action.md
description: >-
  The Create custom record action in the NetSuite REST connector lets you create
  a custom record in NetSuite.
---

# NetSuite REST - Create custom record action

The **Create custom record** action allows you to insert a custom record into NetSuite REST.

Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) guide for more information.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select a NetSuite custom record type, or toggle to enter a custom value. The list populates from the custom record types located in your account at **Customization > Records > Record Types**. |
| Reference Name | Enter a reference name for the record. |

Additional optional fields appear based on the **Custom record** type you select.

## Output

| Output field | Description |
| --- | --- |
| Location | The location ID of the record created. |
| Internal ID | The internal ID of the record created. |
