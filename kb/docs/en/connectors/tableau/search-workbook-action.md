---
url: 'https://docs.workato.com/en/connectors/tableau/search-workbook-action.md'
description: >-
  The Search workbooks action retrieves all workbooks that match your search
  criteria.
---

# Tableau - Search workbooks action

The **Search workbooks** action retrieves all workbooks that match your search criteria.

## Input

| Input field | Description |
| --- | --- |
| Filter | Provide the filter conditions for the search action. Refer to Tableau's [Filtering and Sorting](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_filtering_and_sorting.htm) guide for more information. |
| Sort | Provide the sorting conditions for the search action. Refer to Tableau's [Filtering and Sorting](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_filtering_and_sorting.htm) guide for more information. |
| Page size | Provide the number of items to return in one response. |
| Page number | Provide the offset for paging. |

## Output

| Output field | Description |
| --- | --- |
| Workbook ID | The unique identifier for the workbook. |
| Name | The name of the workbook. |
| Content URL | The URL path to access the workbook. |
| Webpage URL | The full webpage URL to access the workbook in Tableau. |
| Created at | A timestamp indicating when the workbook was created. |
| Updated at | A timestamp of the most recent update to the workbook. |
| Sheet count | The total number of sheets in the workbook. |
| Has extracts | Indicates whether the workbook contains extracted data |
| Encrypt extracts | Indicates whether the workbook extracts are encrypted. |
| Default view ID | The unique identifier for the default view within the workbook. |
| Project ID | The unique identifier for the project. |
| Project name | The name of the project. |
| Project description | A brief description of the project. |
| Owner ID | The unique identifier for the owner. |
| Owner name | The username of the owner. |
| Owner email | The email address of the owner. |
| Owner full name | The full name of the owner. |
| Owner last login | A timestamp of the owner's last login to Tableau. |
| Owner site role | The role of the owner within the Tableau site. |
| Tags | A list of tags associated with the workbook. |
| Acceleration enabled | Indicates whether data acceleration is enabled for the workbook. |
| Page number | The current page number of the paginated list. |
| Page size | The number of items per page in the paginated list. |
| Total available | The total number of available records in the dataset. |

---
