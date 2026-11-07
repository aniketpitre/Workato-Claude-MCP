---
url: 'https://docs.workato.com/en/connectors/zendesk/get-group-by-name-action.md'
description: >-
  The Get group by name action in the Zendesk connector lets you retrieve
  details about a specific group found by name.
---

# Zendesk - Get group by name action

This action retrieves details about a specific group that matches a search by group name. Only records in your Zendesk instance that match the criteria are returned.

## Input

| Input field | Description |
| --- | --- |
| Group name | Enter the name of the group to search for. |

## Output

| Output field | Description |
| --- | --- |
| Group name | The name of the group. |
| Deleted | Whether the group has been deleted. |
| Group ID | The unique Zendesk ID of the group. This is automatically assigned when the group is created. |
| URL | The API URL of the group. |
| Date created | The time the group was created. |
| Date updated | The time the group was last updated. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-tickets-by-external-id-action.md
description: >-
  The Get list of tickets by external IDs action in the Zendesk connector lets
  you retrieve tickets that match a search by external IDs.
---

# Zendesk - Get list of tickets by external IDs action (batch)

This action retrieves a list of tickets that matches a search by external IDs. Only records in your Zendesk instance that match all the criteria are returned.

![Get list of tickets by external IDs action](/assets/get-ticket-external-id.CttVhkKE.png)_Get list of tickets by external IDs action_

## Input

| Input field | Description |
| --- | --- |
| External ID | The external ID of the tickets. You can query multiple external IDs with the `,` separator. |

## Output

The output of this action contains the full set of columns from the list of tickets. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. This is automatically assigned when the ticket is created. |
| Subject | The subject of the ticket. |
| Type | The type of ticket. Permitted values are `problem`, `incident`, `question`, or `task`. |
| Priority | The priority of the ticket. Permitted values are `urgent`, `high`, `normal`, or `low`. |
| Ticket custom fields | Includes data of ticket custom fields. |
| List size | The size of the list, corresponding to the number of tickets retrieved. |

Click here for a full list of [ticket outputs](/en/connectors/zendesk/ticket-fields#ticket-output-fields).

---

---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-organization-details-by-id-action.md
description: >-
  The Get organization details by ID action in the Zendesk connector lets you
  retrieve details about a specific organization found by ID.
---

# Zendesk - Get organization details by ID action

This action retrieves details about a specific organization that matches a search by organization ID. Only records in your Zendesk instance that matches the criteria will be returned.

![Get organization details by ID](/assets/get-organization-details-by-id.BH6Uw019.png)_Get organization details by ID_

## Input

| Input field | Description |
| --- | --- |
| Organization ID | The unique Zendesk ID of the organization. |

## Output

The output of this action contains the full set of columns from the selected organization. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the organization. This is automatically assigned when the organization is created. |
| Group ID | The unique Zendesk ID of the group of this organization. |
| Organization custom fields | Includes data of organization custom fields. |

Click here for a full list of [organization outputs](/en/connectors/zendesk/organization-fields#organization-output-fields).

---

---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-organization-by-external-id-action.md
description: >-
  The Get organizations by external IDs action in the Zendesk connector lets you
  retrieve organizations that match a search by external IDs.
---

# Zendesk - Get organizations by external IDs action (batch)

This action retrieves a list of organizations that matches a search by external IDs. Only records in your Zendesk instance that matches the criteria will be returned.

![Get organizations by external IDs action](/assets/get-organization-external-id.BK8UdyTt.png)_Get organizations by external IDs action_

## Input

| Input field | Description |
| --- | --- |
| External ID | The external ID of the organizations. You can query multiple external IDs with the `,` separator. |

## Output

The output of this action contains the full set of columns from the selected organizations. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the organization. This is automatically assigned when the organization is created. |
| Group ID | The unique Zendesk ID of the group of this organization. |
| Organization custom fields | Includes data of organization custom fields. |
| List size | The size of the list, corresponding to the number of organizations retrieved. |

Click here for a full list of [organization outputs](/en/connectors/zendesk/organization-fields#organization-output-fields).

---

---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-ticket-details-by-id-action.md
description: >-
  The Get ticket details by ID action in the Zendesk connector lets you retrieve
  a specific ticket that matches a search by ticket ID.
---

# Zendesk - Get ticket details by ID action

This action retrieves a specific ticket that matches a search by ticket ID. Only records in your Zendesk instance that matches the criteria will be returned.

![Get ticket details by ID action](/assets/get-ticket-details-by-id.Cg6bBfwr.png)_Get ticket details by ID action_

## Input

| Input field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. |

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
  https://docs.workato.com/en/connectors/zendesk/get-user-details-by-id-action.md
description: >-
  The Get user details by ID action in the Zendesk connector lets you retrieve
  details about a specific user that matches a search by user ID.
---

# Zendesk - Get user details by ID action

This action retrieves details about a specific user that matches a search by user ID. Only records in your Zendesk instance that matches the criteria will be returned.

![Get user details by ID action](/assets/get-user-by-id.CJ7LtXoL.png)_Get user details by ID action_

## Input

| Input field | Description |
| --- | --- |
| User ID | The unique Zendesk ID of the user. |

## Output

The output of this action contains the full set of columns from the selected user. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the user. This is automatically assigned when the user is created. |
| Role | The role of the user. Permitted values are `End-user`, `Agent`, or `Administrator`. |
| Email | The primary email of the user. |
| Organization ID | The unique Zendesk ID of the user's organization. If the user has more than one organization membership, it will display the user's default organization. |
| User custom fields | Includes data of user custom fields. |

Click here for a full list of [user outputs](/en/connectors/zendesk/user-fields#user-output-fields).

---
