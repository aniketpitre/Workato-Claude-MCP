---
url: 'https://docs.workato.com/en/connectors/linear/new-record-trigger.md'
description: >-
  This trigger runs the recipe when a new record, such as an issue or project,
  is created in Linear.
---

# Linear - New record trigger

The **New record** trigger runs the recipe when a new record, such as an issue or project, is created in Linear.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve the details of a record. Fields load dynamically based on the object you select. |

For example, if you select **Project** as your object, the following input schema becomes available:

| Input field | Description |
| --- | --- |
| Select fields to retrieve | Select all fields (including the nested object fields) to return in the response. |
| When first started, this recipe should pick up events from | Set the date and time for the trigger to start picking up items when the recipe runs for the first time. Defaults to 1 hour ago if left blank. You can't change this value after the recipe runs or tests successfully. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, if you select **Project** as your object, the following output schema becomes available. Use the **Select fields to retrieve** input field to specify the fields (including nested object fields) to return in the response.

| Output field | Description |
| --- | --- |
| ID | The unique ID of the project. |
| Title | The project title. |
| Description | The project description. |
| Created at | The time the project was created. |
| Updated at | The time the project was updated. |

---

---
url: >-
  https://docs.workato.com/en/connectors/linear/new-or-updated-records-trigger.md
description: >-
  This trigger runs the recipe on Linear whenever a new record is created or
  updated, such as an issue or project.
---

# Linear - New/updated records trigger

The **New/updated records** trigger runs the recipe on Linear whenever a new record is created or updated, such as an issue or project.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve the details of a record. Fields load dynamically based on the object you select. |

For example, if you select **Project** as your object, the following input schema becomes available:

| Input field | Description |
| --- | --- |
| Select fields to retrieve | Select all fields (including the nested object fields) to return in the response. |
| When first started, this recipe should pick up events from | Set the date and time for the trigger to start picking up items when the recipe runs for the first time. Defaults to 1 hour ago if left blank. You can't change this value after the recipe runs or tests successfully. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, if you select **Project** as your object, the following output schema becomes available. Use the **Select fields to retrieve** input field to specify the fields (including nested object fields) to return in the response.

| Output field | Description |
| --- | --- |
| ID | The unique ID of the project. |
| Title | The project title. |
| Description | The project description. |
| Created at | The time the project was created. |
| Updated at | The time the project was updated. |

---
