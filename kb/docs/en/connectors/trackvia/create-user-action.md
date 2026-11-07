---
url: 'https://docs.workato.com/en/connectors/trackvia/create-user-action.md'
description: >-
  The Create user action in the TrackVia connector creates a new user from an
  email, first name, and last name you provide.
---

# TrackVia - Create user action

The **Create user** action creates a new user in TrackVia.

## Input

| Input field | Description |
| --- | --- |
| Email | Enter the email for the new user. |
| First name | Enter the new user's first name. |
| Last name | Enter the new user's last name. |

## Output

| Output field | Description |
| --- | --- |
| Record ID | Contains the user's first name, last name, and email. |
| Name | The user's name. |
| Address | The user's address. |
| City | The user's city. |
| State | The user's state. |
| Location | Contains information about the location of the user within TrackVia, such as their `Latitude` and `Longitude`. |
| Birthday | The user's birthday. |
| Status | The user's verification status. |
| Last User | The user who last updated the newly created user. |
| Created By User | The user who created the new user. |
| Updated | A timestamp indicating when the user was last updated. |
| Created | A timestamp indicating when the user was created. |
| ID | The TrackVia ID of the user. |
| Favorite app ID | The ID of the user's favorited TrackVia app. |

---

---
url: >-
  https://docs.workato.com/en/connectors/trackvia/delete-all-records-in-view-action.md
description: >-
  The Delete all records in view action in the TrackVia connector deletes every
  record in a TrackVia view you specify.
---

# TrackVia - Delete all records in view action

The **Delete all records in view** action deletes all records in a TrackVia view you specify. A TrackVia view is a set of filters and customizations linked to a data table in TrackVia. A table may have multiple linked views that expose different sets of information.

## Input

| Input field | Description |
| --- | --- |
| Application | Select the TrackVia application that contains the records you plan to delete. |
| View | Select the TrackVia view that contains the records you plan to delete. |

## Output

| Output field | Description |
| --- | --- |
| Status | Displays the status of the API request for the **Delete all records in view** action. |

---
