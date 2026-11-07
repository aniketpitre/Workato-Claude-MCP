---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/list-associations-batch.md
description: >-
  The List associations batch action in the HubSpot connector retrieves all
  associations for the specified object IDs, up to 2000 records.
---

# HubSpot - List associations action (batch)

The **List associations** batch action retrieves all associations for the specified object IDs. It accepts a list of maximum 2000 records. The action fails if you provide more than 2000 records.

## Input

| Input field | Description |
| --- | --- |
| From object | Select the source object type for the associations. |
| To object | Select the target object type to which the source object may be associated. |
| Input parameters | Expand this section to configure the list of source object IDs. |
| Input parameters source list | Input a list datapill representing the object IDs to use for the batch request. The maximum is 2000 records. |
| From object ID | Specify the object ID to list associations from. |
| After | Map the pagination token to retrieve the next page of results. |

## Output

| Output field | Description |
| --- | --- |
| Results | A list of association results returned by the action. Each result includes the associated records for a given object ID. |
| From | The source object in the association, including its ID. |
| Paging | Contains pagination details for retrieving the next set of results. |
| To | A list of associated objects linked to the source object. |
| Errors | A list of any errors that occurred during processing. |
| Status (errors) | The error status code, if applicable. |
| Category (errors) | The category or type of the error. |
| Sub category (errors) | A more specific classification of the error. |
| Message (errors) | A message describing the error. |
