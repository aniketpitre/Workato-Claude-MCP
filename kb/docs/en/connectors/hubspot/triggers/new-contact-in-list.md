---
url: 'https://docs.workato.com/en/connectors/hubspot/triggers/new-contact-in-list.md'
description: >-
  The New contact in list trigger in the HubSpot connector activates when a
  contact is added to a specified list, processing each contact as a job.
---

# HubSpot - New contact in list trigger

The **New contact in list** trigger activates when a contact is added to a specified list. On the initial run, the trigger pulls contacts added in the past hour. On subsequent runs, it checks for new contacts at each polling interval. Each contact is processed as a separate job.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Specify the earliest date and time to start fetching contacts added to the list. If left blank, the trigger retrieves contacts from the past hour. |
| List | Select the contact list you plan to monitor. The drop-down menu contains 500 contact lists. Alternatively, you can toggle this field and enter the HubSpot ID of the contact list. |
| Properties | Select the contact list properties you plan to retrieve. If this field is left blank, the trigger returns all properties. This trigger supports [custom properties](https://knowledge.HubSpot.com/properties/create-and-edit-properties?hubs_content=knowledge.HubSpot.com%2Fproperties%2Fhubspots-default-contact-properties&hubs_content-cta=kb-breadcrumbs__item). |
| Trigger poll interval | Optional. Set how often the trigger checks for new contacts. |

## Output

The **Contacts** object includes information about the new contact, such as the contact's ID, street address, city, and company name.

| Output field | Description |
| --- | --- |
| ID | The contact's unique ID |
| Created at | The date the contact was created in HubSpot. |
| Updated at | The most recent date that the contact list was updated. |
| Archived | Indicates whether the object is archived. |
| Last Modified Date | The most recent modification date for the contact. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> The **New contact in list** trigger also provides a datatree with the contact's attributes and values. Additional fields depend on the **Properties** you select. Refer to HubSpot's [Properties](https://knowledge.HubSpot.com/properties/hubspots-default-contact-properties) guide for more information about retrievable properties.

---
