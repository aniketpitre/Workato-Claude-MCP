---
url: >-
  https://docs.workato.com/en/connectors/zendesk/delete-custom-object-record-action.md
description: >-
  The Delete custom object record action in the Zendesk connector selects a
  record by its Zendesk ID and deletes it from your instance.
---

# Zendesk - Delete custom object record action

Zendesk allows you to configure custom objects to model, store, and retrieve objects that are not native to Zendesk (for example, Tickets, Users, Organization). Refer to [Zendesk custom objects](/en/connectors/zendesk/custom-objects) for more information.

This action selects a specific custom object record by its Zendesk ID and deletes the record from your Zendesk instance. The specific record must exist in your Zendesk instance for this action to execute successfully.

> **VERSION DEPRECATION**
> 
> A previous version of this action worked with Zendesk's legacy custom objects, which Zendesk removed on July 27, 2026. That version is now deprecated. It remains available in existing recipes and continues to function for legacy custom object records. New recipes use the updated version, which works with Zendesk's current Custom Objects API.
> 
> You can update an existing recipe step by selecting the **Delete custom object record by ID** action and choosing the version without the **Deprecated** tag in the **Action** tab.

## Input

| Input field | Description |
| --- | --- |
| Custom object | Select the custom object type of the record to delete. |
| ID | Enter the unique Zendesk ID of the custom object record. |

## Output

There is no output for this action.
