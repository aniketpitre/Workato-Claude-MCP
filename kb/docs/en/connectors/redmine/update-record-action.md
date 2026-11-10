---
url: 'https://docs.workato.com/en/connectors/redmine/update-record-action.md'
description: The Update record action updates an issue in Redmine or adds a note to it.
---

# Redmine - Update record action

The **Update record** action updates an issue in Redmine by its ID. You can also use it to add a note to an issue.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type. **Issue** is the only supported object type. |
| Issue ID | Enter the ID of the issue you plan to update. |
| Notes | Enter a comment to add to the issue history. |
| Private notes | Select **Yes** to make the note private. |
| Project | Select the project you plan to move the issue to. Click **Use custom value** to enter a project ID manually. |
| Subject | Enter the new subject of the issue. |
| Tracker | Select the tracker of the issue. Click **Use custom value** to enter a tracker ID manually. |
| Status | Select the status of the issue. Click **Use custom value** to enter a status ID manually. |
| Priority | Select the priority of the issue. Click **Use custom value** to enter a priority ID manually. |
| Assigned to | Select the user or group to assign the issue to. Select a **Project** first to list its members. Click **Use custom value** to enter an ID manually. |
| Uploads | Files to attach to the issue. Use the [Upload file](/en/connectors/redmine/upload-file-action) action first, then map its **Token** into the **Token** field for each file. Optionally enter a **File name** and **Description**, and select a **Content type**. Click **Use custom value** to enter a MIME type manually. For example, `image/webp`. Redmine 7.1.0 and later ignore **Content type** and detect it from the file. |

## Output

The output contains the updated issue. Refer to the [Redmine documentation](https://www.redmine.org/projects/redmine/wiki/Rest_Issues) for a representative set of output fields.

---
