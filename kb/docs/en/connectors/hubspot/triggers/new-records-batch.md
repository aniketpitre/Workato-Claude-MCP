---
url: 'https://docs.workato.com/en/connectors/hubspot/triggers/new-records-batch.md'
description: >-
  The New records batch trigger checks HubSpot for newly created objects of the
  type you specify.
---

# HubSpot - New records trigger (batch)

The **New records** batch trigger checks HubSpot for newly created objects of the type you specify. It runs at each poll interval to detect and process new records. Each batch is processed as a separate job.

This trigger supports the following objects:

- Contact
- Company
- Deal
- Ticket

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object you plan to monitor. |
| Properties | Select the object properties you plan to retrieve. If this field is left blank, the trigger returns all properties. This trigger supports [custom properties](https://knowledge.HubSpot.com/properties/create-and-edit-properties?hubs_content=knowledge.HubSpot.com%2Fproperties%2Fhubspots-default-contact-properties&hubs_content-cta=kb-breadcrumbs__item). |
| Filter Groups | Add filters to specify conditions that a created record must meet to trigger a job. If you add multiple filter groups, they are evaluated using a logical `AND` operator. You can add up to two filter groups. You cannot use the created date as a property for filtering. |
| Batch size | Specify the number of records to return in each job. The minimum value is `1`, and the maximum value is `100`, which is also the default. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| Range | The range of records retrieved. |
| First ID | The ID of the first record in the retrieved batch. |
| Last ID | The ID of the last record in the retrieved batch. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> This trigger's remaining output fields vary based on your selected **Properties**. Refer to HubSpot's [Properties](https://knowledge.HubSpot.com/crm/topics?hubs_content=knowledge.HubSpot.com/properties/hubspots-default-contact-properties&hubs_content-cta=kb-breadcrumbs__item#properties) guide for more information about retrievable properties.

---
