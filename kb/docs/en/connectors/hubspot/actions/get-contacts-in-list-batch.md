---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/get-contacts-in-list-batch.md
description: >-
  The Get contacts in list batch action in the HubSpot connector retrieves all
  details about contacts in a specific contact list.
---

# HubSpot - Get contacts in list action (batch)

The **Get contacts in list** batch action retrieves all details about contacts in a specific contact list in HubSpot.

## Input

| Input field | Description |
| --- | --- |
| List | List from which you plan to retrieve contacts. |
| Properties | The property of the contact that's returned in the response. For example, city, street address, and more. See the [Hubspot API Reference](https://developers.hubspot.com/docs/guides/api/crm/search) for a list of returned properties. |

## Output

| Output field | Description |
| --- | --- |
| ID | The HubSpot ID of the contact. |
| Created at | The timestamp when the contact was created. |
| Updated at | The most recent date that any property on a contact record was updated. |
| Archived | Indicates if the contact has been archived. |
| Last Modified Date | The most recent date that any property on a contact record was updated. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> This trigger also provides a datatree with the contact's attributes and values. Additional fields depend on the **Properties** you select. Refer to HubSpot's [Properties](https://knowledge.HubSpot.com/properties/hubspots-default-contact-properties) guide for more information about retrievable properties.
