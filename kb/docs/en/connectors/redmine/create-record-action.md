---
url: 'https://docs.workato.com/en/connectors/redmine/create-record-action.md'
description: The Create record action creates an issue in a Redmine project.
---

# Redmine - Create record action

The **Create record** action creates an issue in a Redmine project you select.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type. **Issue** is the only supported object type. |
| Project | Select the project the issue belongs to. Click **Use custom value** to enter a project ID manually. |
| Subject | Enter the subject of the issue. |
| Tracker | Select the tracker of the issue, such as **Bug** or **Feature**. Click **Use custom value** to enter a tracker ID manually. |
| Status | Select the status of the issue. Click **Use custom value** to enter a status ID manually. |
| Priority | Select the priority of the issue. Click **Use custom value** to enter a priority ID manually. |
| Description | Enter the description of the issue. |
| Assigned to | Select the user or group to assign the issue to. Select a **Project** first to list the project's members. Click **Use custom value** to enter an ID manually. |
| Due date | Enter the date the issue is due. |
| Uploads | Files to attach to the issue. Use the [Upload file](/en/connectors/redmine/upload-file-action) action first, then map its **Token** into the **Token** field for each file. Optionally enter a **File name** and **Description**, and select a **Content type**. Click **Use custom value** to enter a MIME type manually. For example, `image/webp`. Redmine 7.1.0 and later ignore **Content type** and detect it from the file. |
| Custom fields | Enter a **Custom field ID** and **Value** for each custom field to set on the issue. |

## Output

This action returns many output fields. Refer to the [Redmine documentation](https://www.redmine.org/projects/redmine/wiki/Rest_Issues) for a representative set of output fields.

---
