---
url: 'https://docs.workato.com/en/connectors/greenhouse/search-objects-v3.md'
description: >-
  The Search objects (v3) action retrieves records from Greenhouse using the v3
  API.
---

# Greenhouse - Search objects (v3) batch action

The **Search objects (v3)** batch action retrieves records from Greenhouse using the v3 API.

This action is available for OAuth 2.0 connections only.

## Input

Input fields are dynamically generated based on the selected endpoint.

| Input field | Description |
| --- | --- |
| Endpoint | Select the object type to search. For example, **Applications**, **Candidates**, or **Jobs**. |
| Cursor | Provide the cursor to retrieve the next page of results. Don't use other parameters when this is provided. |
| Page size | Specify the number of results to return per page. |
| IDs | Provide a comma-separated list of IDs to filter results. |

Additional input fields appear based on the selected endpoint. For example, selecting **Applications** displays filters such as **Candidate IDs** and **Job IDs**.

Refer to the [Greenhouse v3 object coverage guide](/en/connectors/greenhouse/object-coverage#create-object-v3) for supported objects and field-level details.

## Output

| Output field | Description |
| --- | --- |
| Results | List of records returned by the selected endpoint. |
| Next link | Link to retrieve the next page of results. |

---
