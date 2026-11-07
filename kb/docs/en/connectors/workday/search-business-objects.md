---
url: 'https://docs.workato.com/en/connectors/workday/search-business-objects.md'
description: >-
  The Search business objects action (batch) searches business objects you
  specify in Workday.
---

# Workday - Search business objects (batch) action

The **Search business objects** action (batch) searches business objects you specify in Workday.

## Input

| Input field | Description |
| --- | --- |
| Business object | Select the [business object](#business-object-types) to search. |
| Request references | Use this section to retrieve specific instances of a business object and its associated data. |
| Response filter | Use this section to specify parameters to filter the response data. You can filter the returned data by dates and page attributes. |
| Fields with attributes | Select the fields that must have assigned attributes. These attributes are part of the XML tag of the selected field. |
| Fields with multiple values | Select the fields that repeat in the business object data. |

Additional or advanced input fields may be present for specific business objects.

How can I search for a worker using their Contingent Worker ID?

Complete the following steps to search for a worker by Contingent Worker ID:

1. Select **Workers** as the **Business object**.
   
2. Expand the **Request references** field.
   
3. Switch the **Worker reference employee ID** field to enter a custom value.
   
4. Enter `Contingent_Worker_ID:` and append the worker's employee ID in the **Worker reference employee ID** field.
   
   ![Search for a worker using their Contingent Worker ID](/assets/contingent-worker-id.C1bEAKpA.png)_Search for a worker by Contingent Worker ID_
   

### Business object types

This action supports searching Workday for the following business object types:

- Applicants
- Citizenship statuses
- Countries
- Job classification groups
- Job families
- Job family groups
- Locations
- Organizations
- Positions
- Student employment eligibility data
- Worker documents
- Workers

## Output

| Output field | Description |
| --- | --- |
| Data | An array containing the search results. The structure of the output depends on the selected business object. |
| Results | An object containing metadata about the search. |
| Total results (results) | The total number of records that match the search criteria. |
| Total pages (results) | The total number of pages in the search results. |
| Page results (results) | The number of records included on this page or batch. This also represents the number of records retrieved in this job. |
| Page (results) | The page number processed in this job. |

---
