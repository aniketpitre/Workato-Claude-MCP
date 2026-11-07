---
url: 'https://docs.workato.com/en/connectors/ramp/search-records-action.md'
description: >-
  List and filter Ramp records, with query parameters and result fields
  generated live from Ramp's own API schema for the object you select.
---

# Ramp - Search records action

The **Search records** action lists and filters records in Ramp.

> **CURSOR-BASED PAGINATION**
> 
> Ramp's list endpoints paginate with a cursor, not page numbers. Search filters commonly include a **Start** field (the ID to resume from) and a **Page size** field (2-10,000 results per page, default 1,000). The output's **Page** field includes a **Next** URL that fetches the following page when more results are available.

## Input

Input fields dynamically generate based on the object you select and the search operation. The following field is common to all objects. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of input fields.

| Input field | Description |
| --- | --- |
| Object | Select the Ramp object to search, for example **Transactions**, **Cards**, or **Users**. |

The following are a representative set of filters available after you select **Transactions**: `card_id`, `department_id`, `user_id`, `state`, `from_date`, `to_date`, and `page_size`.

## Output

Output fields dynamically generate based on the object you select. Refer to the Ramp [REST API](https://docs.ramp.com/developer-api/v1/api/) documentation for a list of output fields.

| Output field | Description |
| --- | --- |
| Data | An array of matching records, with fields matching the selected object's schema in Ramp's API. |
| Page | Pagination info. The **Next** field contains the URL to fetch the next page. The **Next** field is empty if there are no more results. |

The filter fields on this action narrow down _which records_ are returned, not _which fields_ come back for each one. Ramp's API doesn't support selecting a subset of fields, so every record in **Data** includes its complete set of fields.

---
