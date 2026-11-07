---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-list-of-custom-object-records-by-external-id-action.md
description: >-
  The Get list of custom object records by external IDs action in the Zendesk
  connector lets you retrieve records that match a search by external IDs.
---

# Zendesk - Get list of custom object records by external IDs action (batch)

Zendesk allows you to configure custom objects to model, store, and retrieve objects that are not native to Zendesk (for example, Tickets, Users, Organization). Refer to [Zendesk custom objects](/en/connectors/zendesk/custom-objects) for more information.

This action retrieves a list of custom object records that matches a search by external IDs. Only results in your Zendesk instance that matches the criteria will be returned.

> **VERSION DEPRECATION**
> 
> A previous version of this action worked with Zendesk's legacy custom objects, which Zendesk removed on July 27, 2026. That version is now deprecated. It remains available in existing recipes and continues to function for legacy custom object records. New recipes use the updated version, which works with Zendesk's current Custom Objects API.
> 
> You can update an existing recipe step by selecting the **Get list of custom object records by external IDs** action and choosing the version without the **Deprecated** tag in the **Action** tab.

## Input

| Input field | Description |
| --- | --- |
| Custom object | Select a custom object type to retrieve. |
| External IDs | Enter a comma-separated list of external IDs to obtain corresponding record details. |

## Output

The output of this action contains the full set of columns from the selected custom object type.

| Output field | Description |
| --- | --- |
| Records | The list of custom object records that match the search. |
| ID (Records) | The unique Zendesk ID for the custom object record. This is automatically assigned when the record is created. |
| Name (Records) | The name of the record. |
| Custom object key (Records) | The key of the custom object type. |
| External ID (Records) | A unique identifier from another system. |
| Custom object fields (Records) | Includes data of custom object custom fields. |
| Created by user ID (Records) | The unique Zendesk ID of the user who created this record. |
| Updated by user ID (Records) | The unique Zendesk ID of the user who last updated this record. |
| Date created (Records) | The time the custom object record was created. |
| Date updated (Records) | The time the custom object record was updated. |
| List size | The size of the list, corresponding to the number of custom object records retrieved. |
| List index | The index of the current record within the list. |
| Total records | The total number of custom object records that matched the search. |
