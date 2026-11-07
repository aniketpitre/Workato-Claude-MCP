---
url: 'https://docs.workato.com/en/connectors/filevine/search-records-action.md'
description: >-
  The Search records action retrieves records from Filevine based on the
  selected object, project type, and section criteria.
---

# Filevine - Search records action

The **Search records** action retrieves a list of records from Filevine that match the object type, project type ID, and section you specify.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the Filevine object to search. |
| Project type ID | Select the ID of the project type to filter the results. |
| Sections | Select the section within the project type to search in. |

Additional input fields may appear depending on the selected object type.

## Output

| Output field | Description |
| --- | --- |
| Links | Navigation links for paginated results. |
| Count | Number of records returned in the current response. |
| Offset | Offset used for paginating the results. |
| Last ID | ID of the last record in the current result set. |
| Limit | Maximum number of records returned per request. |
| Has more | Indicates whether more records are available. |
| Requested fields | Fields requested for each record. |
| Items | List of records that match the search criteria. |

---
