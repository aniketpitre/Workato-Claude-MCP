---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-custom-object-record-by-id-action.md
description: >-
  The Get custom object record by ID action in the Zendesk connector lets you
  retrieve details about a specific record found by Zendesk ID.
---

# Zendesk - Get custom object record by ID action

Zendesk allows you to configure custom objects to model, store, and retrieve objects that are not native to Zendesk (for example, Tickets, Users, Organization). Refer to [Zendesk custom objects](/en/connectors/zendesk/custom-objects) for more information.

This action retrieves details about a specific custom object record that matches a search by Zendesk ID. Only records in your Zendesk instance that matches the criteria will be returned. This action fails if a record with the provided ID does not exist.

> **VERSION DEPRECATION**
> 
> A previous version of this action worked with Zendesk's legacy custom objects, which Zendesk removed on July 27, 2026. That version is now deprecated. It remains available in existing recipes and continues to function for legacy custom object records. New recipes use the updated version, which works with Zendesk's current Custom Objects API.
> 
> You can update an existing recipe step by selecting the **Get custom object record by ID** action and choosing the version without the **Deprecated** tag in the **Action** tab.

## Input

| Input field | Description |
| --- | --- |
| Custom object | Select a custom object type to retrieve. |
| ID | Enter the unique Zendesk ID of the custom object record. |

## Output

The output of this action contains the full set of columns from the selected custom object type.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID for the custom object record. This is automatically assigned when the record is created. |
| Name | The name of the record. |
| Custom object key | The key of the custom object type. |
| External ID | A unique identifier from another system. |
| Created by user ID | The unique Zendesk ID of the user who created this record. |
| Updated by user ID | The unique Zendesk ID of the user who last updated this record. |
| Date created | The time the custom object record was created. |
| Date updated | The time the custom object record was updated. |
| Custom object fields | Includes data of custom object custom fields. |
