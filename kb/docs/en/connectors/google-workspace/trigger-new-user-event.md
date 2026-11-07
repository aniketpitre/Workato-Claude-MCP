---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/trigger-new-user-event.md
description: >-
  The **New user event** trigger listens to new user related events that are
  created in your Google Workspace instance.
---

# Google Workspace - New user event trigger

The **New user event** trigger monitors your Google Workspace instance for new user related events. This trigger processes each event as a separate job.

### Input

| Input field | Description |
| --- | --- |
| User Event | Select the user event to monitor. Options include `User created`, `User deleted`, `User Admin status changed`, `User undeleted`, and `User updated.` |
| Domain | Select the domain to retrieve users from. Leave this field blank to retrieve users from all domains. |

### Output

The **Create object** action's output fields vary based on your selected Object type. Refer to [Google Workspace's API documentation](https://developers.google.com/workspace) for more information about the output fields for each type.
