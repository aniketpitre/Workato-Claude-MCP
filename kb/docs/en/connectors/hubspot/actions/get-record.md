---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/get-record.md'
description: >-
  The Get record action in the HubSpot connector lets you retrieve a HubSpot
  object by its ID and select which properties to return.
---

# HubSpot - Get record action

The **Get record** action allows you to retrieve a HubSpot object using its ID. You can select the properties you plan to retrieve from it.

This action supports the following objects:

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
| Object | Select which HubSpot object to retrieve. |
| ID | Provide the ID of the record to retrieve. |
| Fields to retrieve | Specify properties to return in the response. When left blank, only the default fields are returned. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the record. |
| Created at | The time the record was created. |
| Updated at | The time the record was updated |
| Archived | Indicates whether the record was archived, if applicable. |
| Archived at | The time the record was archived. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> This action also provides a datatree with attributes and values for the specified **Object**. Additional fields depend on what you specify in the **Fields to retrieve** field. Refer to HubSpot's [Properties](https://knowledge.HubSpot.com/properties/hubspots-default-contact-properties) guide for more information about retrievable properties.

---
