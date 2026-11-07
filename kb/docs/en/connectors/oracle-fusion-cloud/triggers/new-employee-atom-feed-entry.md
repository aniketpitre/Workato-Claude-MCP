---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/triggers/new-employee-atom-feed-entry.md
description: >-
  The New employee atom feed entry trigger detects and retrieves new
  employee-related events from Oracle Fusion Cloud's atom feed.
---

# Oracle Fusion Cloud - New employee atom feed entry trigger

The **New employee atom feed entry** trigger detects and retrieves new employee-related events from Oracle Fusion Cloud's atom feed.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. Minimum value allowed is five minutes. |
| Feed Title | Select the atom feed title to monitor for new employee events. Options include: New Hire, Termination, Person Basic Information Changed, Person Assignment Changed, Work Relationship Update, Work Relationship Cancellation, Workstructure Organization Changed, Workstructure Location Changed, Workstructure Job Changed, Workstructure Grade Changed, Workstructure Position Changed |
| When first started, this recipe should pick up events from | Specify the starting date and time from which to begin retrieving events. |
| Trigger on date field | Choose the date field (**Published** or **Updated**) to determine when the trigger fires for new or updated feed entries. The default is **Published**. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the atom feed entry event. |
| Title | The title of the atom feed entry, usually describing the nature of the employee event (for example, Update, Hire). |
| Summary | A brief summary of the event or change detected. |
| Content | Detailed event data including employee context, changed attributes, and flex fields. |
| Context (Content) | Employee context information such as Person ID, Person Name, Assignment, Dates, and other HR attributes. |
| Changed Attributes | List of fields that have changed, showing old and new values. |
| Flex Fields | Additional flex field data, including custom or extended HR attributes. |
| Updated | The timestamp when the atom feed entry was last updated. |
| Published | The timestamp when the atom feed entry was published. |
| Authors | Array of authors, typically listing the system or user that performed the change. |
| Links | Array of hyperlinks to related resources (for example, employee record URL). |
