---
url: 'https://docs.workato.com/en/connectors/zendesk/solve-ticket-action.md'
description: >-
  The Solve ticket action in the Zendesk connector updates a ticket identified
  by its Zendesk ID and sets the status to solved.
---

# Zendesk - Solve ticket action

This action updates a specific ticket your Zendesk instance and sets the ticket's status to `solved`. The ticket is identified by its Zendesk ID.

Some ticket fields put constraints on a ticket's status. For example, Zendesk requires a non-`null` input for **assignee** and **group**, before allowing a ticket to be `solved`. Check that you have satisfied all default and custom preconditions before using this action.

![Solve ticket action](/assets/solve-ticket-action.Bcmg4g9R.png)_Solve ticket action_

## Input

| Input field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. |
| Ticket form | Select a ticket form to open **required** fields for that preconfigured ticket form. |
| Ticket custom fields | Provide data for the required custom fields. |

## Output

The output of this action contains the full set of columns from the selected ticket. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. This is automatically assigned when the ticket is created. |
| Subject | The subject of the ticket. |
| Type | The type of ticket. Permitted values are `problem`, `incident`, `question`, or `task`. |
| Priority | The priority of the ticket. Permitted values are `urgent`, `high`, `normal`, or `low`. |
| Ticket custom fields | Includes data of ticket custom fields. |

Click here for a full list of [ticket outputs](/en/connectors/zendesk/ticket-fields#ticket-output-fields).

---

---
url: >-
  https://docs.workato.com/en/connectors/zendesk/update-custom-object-record-action.md
description: >-
  The Update custom object record action in the Zendesk connector updates a
  record identified by its Zendesk ID in your instance.
---

# Zendesk - Update custom object record action

Zendesk allows you to configure custom objects to model, store, and retrieve objects that are not native to Zendesk (for example, Tickets, Users, Organization). Refer to [Zendesk custom objects](/en/connectors/zendesk/custom-objects) for more information.

This action updates a specific custom object record in your Zendesk instance. The record to edit is identified by its Zendesk ID.

> **VERSION DEPRECATION**
> 
> A previous version of this action worked with Zendesk's legacy custom objects, which Zendesk removed on July 27, 2026. That version is now deprecated. It remains available in existing recipes and continues to function for legacy custom object records. New recipes use the updated version, which works with Zendesk's current Custom Objects API.
> 
> You can update an existing recipe step by selecting the **Update custom object record** action and choosing the version without the **Deprecated** tag in the **Action** tab.

## Input

| Input field | Description |
| --- | --- |
| Custom object | Select the custom object type of the record to update. |
| ID | Enter the unique Zendesk ID of the custom object record. |
| Update record values | Provide the fields to update on the record. |
| Name (Update record values) | Enter the name of the record. |
| External ID (Update record values) | Enter the external ID to link this record to records in an external system. |
| Custom object fields (Update record values) | Provide data for each custom field configured on the custom object type. |

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

---
