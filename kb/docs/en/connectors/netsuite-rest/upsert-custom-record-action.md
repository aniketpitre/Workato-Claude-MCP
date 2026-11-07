---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/upsert-custom-record-action.md
description: >-
  The Upsert custom record action in the NetSuite REST connector lets you upsert
  a custom record in NetSuite.
---

# NetSuite REST - Upsert custom record action

The **Upsert custom record** action allows you to upsert a custom record in NetSuite REST.

Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) guide for more information.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select a NetSuite custom record type, or toggle to enter a custom value. The list populates from the custom record types located in your account at **Customization > Records > Record Types**. |
| External ID | The external ID of the record to upsert. |

Additional optional fields appear based on the **Custom record** type you select.

## Output

| Output field | Description |
| --- | --- |
| Location | The location ID of the record upserted. |
| Internal ID | The internal ID of the record upserted. |
