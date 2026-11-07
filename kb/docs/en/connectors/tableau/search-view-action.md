---
url: 'https://docs.workato.com/en/connectors/tableau/search-view-action.md'
description: >-
  The Search views action returns all site views that match the search criteria
  you provide.
---

# Tableau - Search views action

The **Search views** action returns all site views that match the search criteria you provide.

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
| View ID | The unique identifier for the view. |
| Name | The name of the view. |
| Content URL | The URL path to access the view. |
| Created at | A timestamp indicating when the view was created. |
| Updated at | A timestamp of the most recent update to the view. |
| View URL name | The user-friendly name used in the view’s URL. |
| Sheet type | Indicates whether the view is a Dashboard, Story, or Worksheet. |
| Favorites total | The total number of times the view has been marked as a favorite by users. |
| Tags | A list of tags associated with the view. |
| Workbook ID | The unique identifier for the workbook. |
| Workbook name | The name of the workbook. |
| Workbook content URL | The URL path to access the workbook. |
| Show tabs | Indicates whether the workbook displays sheet tabs. |
| Size | The file size of the workbook. |
| Workbook created at | A timestamp indicating when the workbook was created. |
| Workbook updated at | A timestamp of the most recent update to the workbook. |
| Sheet count | The total number of sheets in the workbook. |
| Has extracts | Indicates whether the workbook contains extracted data. |
| Workbook tags | A list of tags associated with the workbook. |
| Owner ID | The unique identifier for the owner. |
| Owner name | The username of the owner. |
| Owner email | The email address of the owner. |
| Owner full name | The full name of the owner. |
| Owner site role | The role of the owner within the Tableau site. |
| Owner last login | A timestamp of the owner's last login to Tableau. |
| Project ID | The unique identifier for the project. |
| Project name | The name of the project. |
| Project description | A brief description of the project. |
| Total view count | The total number of times the view has been accessed. |
| Pagination | Information about the paginated response. |
| Page number | The current page number of the paginated list. |
| Page size | The number of items per page in the paginated list. |
| Total available | The total number of available records in the dataset. |

---
