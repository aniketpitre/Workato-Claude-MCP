---
url: 'https://docs.workato.com/en/connectors/felix/search-records-action.md'
description: >-
  The **Search records** action returns all records that matches your search
  criteria.
---

# Felix - Search records action

The **Search records** action returns all records that matches your search criteria. You can search for vendors, compliance documents, attached tags, and payment details.

## Input

| Input field | Description |
| --- | --- |
| Object | Required. Select the Felix object you plan to search for. |
| Page | Enter the page number to retrieve. |
| Per page | Enter the number of records to return per page. The maximum is 1000. |
| Last updated | Select or enter the date to show updated records from. |

## Output

| Output field | Description |
| --- | --- |
| Data | Details about the data associated with the search results. Such as, ID, title, status, validation, file, expiry date, provider, classification, commencement, dollar value, number, vendor ID, global vendor ID, compliance document type configuration ID, compliance document type ID, and compliance document type title. |
| Links | Details about links associated with the search results. Such as, link addresses. |
| Meta | Metadata associated with the search results. Such as, current page, from, last page, path, per page, to, and total. |

---
