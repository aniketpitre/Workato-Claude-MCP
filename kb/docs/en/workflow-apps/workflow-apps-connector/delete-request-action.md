---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/delete-request-action.md
description: >-
  Configure the Delete request action to remove a request from a Workflow app by
  its record ID using the Workflow apps connector.
---

# Delete request

Delete a request from a Workflow app.

## Input

| Input Field | Description |
| --- | --- |
| Workflow app | Select a Workflow app in which to delete a request. |
| Record ID | The ID of the record you plan to delete. You can map this in using a datapill from a trigger or action from the Workflow apps connector. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Success | Whether the record is deleted successfully. Available values include `True` or `False`. |
