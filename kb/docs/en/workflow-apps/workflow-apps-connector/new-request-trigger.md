---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-request-trigger.md
description: >-
  Configure the New request trigger to run a recipe in real time when a new
  request is created in a Workflow app or its data table.
---

# New request trigger

The **New request** (real-time) trigger runs when there is a new request in a Workflow app.

This trigger also runs when a user creates a new record manually in a workflow app's corresponding [data table](/en/data-tables).

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Choose a Workflow app to check for new requests. |
| When first started this recipe should pick up events from | Get new requests since a particular date/time. Leave empty to get new requests since one hour ago. Once the recipe has been run or tested, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

You can also toggle **Set trigger condition** to only process trigger events matching conditions you specify.

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Change ID | The ID number that corresponds to the Workflow app's corresponding data table. |
| Request | This JSON object represents a record in a Workflow app. It includes metadata and links to related objects. |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Created by (Request) | A nested JSON object within the Request object. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested JSON object within the Created by object. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Stage (Request) | A nested JSON object within the Request object. |
| Stage ID (Stage) | The ID of the group this task is assigned to. |
| Group name (Stage) | The name of the group this task is assigned to. |
| Created at | The date the record was created. |
| Updated at | The date the record was most recently updated. |
