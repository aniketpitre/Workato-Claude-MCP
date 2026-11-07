---
url: >-
  https://docs.workato.com/en/connectors/zendesk/create-custom-object-record-action.md
description: >-
  The Create custom object record action in the Zendesk connector creates a
  single custom object record in your instance.
---

# Zendesk - Create custom object record action

Zendesk allows you to configure custom objects to model, store, and retrieve objects that are not native to Zendesk (for example, Tickets, Users, Organization). Refer to [Zendesk custom objects](/en/connectors/zendesk/custom-objects) for more information.

This action creates a single record of a custom object in your Zendesk instance.

> **VERSION DEPRECATION**
> 
> A previous version of this action worked with Zendesk's legacy custom objects, which Zendesk removed on July 27, 2026. That version is now deprecated. It remains available in existing recipes and continues to function for legacy custom object records. New recipes use the updated version, which works with Zendesk's current Custom Objects API.
> 
> You can update an existing recipe step by selecting the **Create custom object record** action and choosing the version without the **Deprecated** tag in the **Action** tab.

## Input

| Input field | Description |
| --- | --- |
| Custom object | Select a custom object type for your new record. |
| New record values | Provide the fields for the new custom object record. |
| Name (New record values) | Enter the name of the record. Required unless the custom object has a field designated as the display name. |
| External ID (New record values) | Enter the external ID to link this record to records in an external system. |
| Custom object fields (New record values) | Provide data for each custom field configured on the custom object type. |

## Output

The output of this action contains the full set of columns from the selected custom object type.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the custom object record. This is automatically assigned when the custom object record is created. |
| Name | The name of the record. |
| Custom object key | The key of the custom object type. |
| External ID | A unique identifier from another system. |
| Created by user ID | The unique Zendesk ID of the user who created this record. |
| Updated by user ID | The unique Zendesk ID of the user who last updated this record. |
| Date created | The time the custom object record was created. |
| Date updated | The time the custom object record was updated. |
| Custom object fields | Includes data of custom object custom fields. |
