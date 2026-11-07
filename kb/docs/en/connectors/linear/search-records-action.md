---
url: 'https://docs.workato.com/en/connectors/linear/search-records-action.md'
description: >-
  The Search records action enables you to retrieve a list of records that match
  your search criteria from Linear.
---

# Linear - Search records action

The **Search records** action enables you to retrieve a list of records that match your search criteria from Linear.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve a list of records. Fields load dynamically based on the object you select. |

For example, if you select **Project** as your object, the following input schema becomes available:

| Input field | Description |
| --- | --- |
| Use custom filter | Allows users to define their criteria to refine the search. |
| Before | Specify the date to filter records before this date. |
| After | Specify the date range to filter records after this date. |
| First | Specify the quotas results to the first entries. |
| Last | Specify the quotas results to the last entries. |
| Include archived | Option to include or exclude archived items in the search results. |
| Order by | Options to sort the results based on selected fields. |
| Select fields to retrieve | Select all fields (including the nested object fields) to return in the response. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, if you select **Project** as your object, the following output schema becomes available. Use the **Select fields to retrieve** input field to specify the fields (including nested object fields) to return in the response.

| Output field | Description |
| --- | --- |
| ID | The unique ID of the project. |
| Created at | The time the project was created. |
| Updated at | The time the project was updated. |
| Archived at | The time at which the entity was archived. |
| Update reminder frequency in weeks | The n-weekly frequency at which to prompt for updates. When not set, reminders are inherited from the workspace. |
| Update reminder frequency | The frequency at which to prompt for updates. When not set, reminders are inherited from the workspace. |
| Frequency resolution | The resolution of the reminder frequency. |
| Update reminders day | The day on which to prompt for updates. |
| Update reminders hour | The hour at which to prompt for updates. |
| Name | The name of the project. |
| Description | The project description. |
| Slug ID | The project's unique URL slug. |
| Icon | The project icon. |
| Color | The project's color. |
| Project update reminders paused until at | The time until which project update reminders are paused. |
| Start date | The estimated start date of the project. |
| Start date resolution | The resolution of the project's start date. |
| Target date | The estimated completion date of the project. |
| Target date resolution | The resolution of the project's estimated completion date. |
| Started at | The time at which the project was moved into the started state. |
| Completed at | The time at which the project was moved into a completed state. |
| Canceled at | The time at which the project was moved into the canceled state. |
| Auto archived at | The time at which the project was automatically archived by the auto-pruning process. |
| Trashed | A flag that indicates whether the project is in the trash bin. |
| Sort order | The sort order for the project within the organization. |
| Priority sort order | The sort order for the project within the organization when ordered by priority. |
| Priority | The priority of the project. |
| Health | The health of the project. |
| Health updated at | The time at which the project health was updated. |
| Progress history | The progress history of the project. |
| Current progress | The current progress of the project. |
| URL | The project URL. |
| Progress | The overall progress of the project. |
| Scope | The overall scope (total estimated points) of the project. |
| Content | The project's content in Markdown format. |
| Content state | The project's content. |
| Priority label | The priority label of the project. |
| End cursor | Cursor representing the last result in the paginated results. |
| Start cursor | Cursor representing the first result in the paginated results. |
| Has next page | Indicates if there are more results when paginating forward. |
| Has Previous page | Indicates if there are more results when paginating backward. |

---
