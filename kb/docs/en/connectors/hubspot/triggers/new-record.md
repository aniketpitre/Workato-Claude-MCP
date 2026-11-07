---
url: 'https://docs.workato.com/en/connectors/hubspot/triggers/new-record.md'
description: >-
  The New record trigger polls HubSpot for new records of the object type you
  specify.
---

# HubSpot - New record trigger

The **New record** trigger polls HubSpot for new records of the object type you specify. It processes each record as a separate job.

This trigger supports the following objects:

- Contact
- Company
- Deal
- Product
- Ticket
- Line Item
- Quote
- Custom Objects

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object you plan to monitor. |
| Properties | Select the object properties you plan to retrieve. If this field is left blank, the trigger returns HubSpot's default properties for the selected **Object** type. This trigger supports [custom properties](https://knowledge.HubSpot.com/properties/create-and-edit-properties?hubs_content=knowledge.HubSpot.com%2Fproperties%2Fhubspots-default-contact-properties&hubs_content-cta=kb-breadcrumbs__item). |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| ID | The HubSpot ID of the object. |
| Date created | The timestamp indicating when the object was created. |
| Date updated | The timestamp indicating when the object was last updated. |
| Archived | Indicates whether the object is archived. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> In addition to the preceding fields, the **New record** trigger provides a datatree with attributes and values for the specified **Object**. Additional fields depend on the **Properties** you select. Refer to HubSpot's [Properties](https://knowledge.HubSpot.com/crm/topics?hubs_content=knowledge.HubSpot.com/properties/hubspots-default-contact-properties&hubs_content-cta=kb-breadcrumbs__item#properties) guide for more information about retrievable properties.

---
