---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/create-records-batch.md'
description: >-
  The Create records batch action in the HubSpot connector lets you create
  records in batches for supported objects in your HubSpot instance.
---

# HubSpot - Create records action (batch)

The **Create records** batch action creates records in batches in HubSpot.

This action supports the following objects:

- Contacts
- Companies
- Deals
- Tickets
- Products
- Line items

## Input

| Input field | Description |
| --- | --- |
| Object | Specify which standard HubSpot object to create. |

Additional input fields are available based on the object you select.

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the batch operation. |
| Requested at | Timestamp indicating when the batch request was submitted. |
| Started at | Timestamp indicating when the batch processing began. |
| Completed at | Timestamp indicating when the batch processing finished. |
| Links | A set of URLs for retrieving the batch status or results. |
| Results | A list of records created by the batch operation. |
| ID (results) | The unique identifier of the created record. |
| Created at (results) | Timestamp indicating when the record was created. |
| Updated at (results) | Timestamp indicating when the record was last updated. |
| Archived (results) | Indicates whether the record is archived. |
| Archived at (results) | Timestamp indicating when the record was archived, if applicable. |
| Properties (results) | A collection of property values for the created record, based on the object schema. |

---
