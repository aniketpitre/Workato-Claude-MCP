---
url: 'https://docs.workato.com/en/connectors/clickup/update-record-action.md'
description: 'The **Update record** action updates any record in ClickUp, such as task.'
---

# ClickUp - Update record action

The **Update record** action updates any record in ClickUp, such as tasks.

## Input

The input fields load dynamically based on the selected object. For example, if you select the **Task track time** object, the following input fields are available.

| Input field | Description |
| --- | --- |
| Task ID | Select the name of the task from the drop-down menu. |
| Interval ID | Provide the interval ID. |
| Workspace/Team | Select the name of the workspace or team from the drop-down menu. |
| Custom task IDs | Select the boolean value from the drop-down menu. |
| Start | Select the start date and time from the calendar. |
| End | Select the end date and time from the calendar. |
| Time | Provide the time in milliseconds. |

## Output

The output fields load dynamically based on the selected object. For example, if the selected object is **Task track time**, then the following output fields are available.

| Output field | Description |
| --- | --- |
| Task track time ID | A unique ID associated with the **Task track time** returned by ClickUp. |

---

---
url: >-
  https://docs.workato.com/en/connectors/clickup/upload-task-attachment-action.md
description: >-
  The **Upload task attachment** action allows you to upload a task attachment
  in ClickUp.
---

# ClickUp - Upload task attachment action

The **Upload task attachment** action allows you to upload a task attachment in ClickUp.

## Input

| Input field | Description |
| --- | --- |
| Task ID | Select the task name from the drop-down menu. |
| Attachment | Provide the attachment to be uploaded. |
| Filename | Provide the filename of the attachment. |
| Team ID | Select the team from the drop-down menu. |
| Space ID | Select the space from the drop-down menu. |
| Folder ID | Select the folder from the drop-down menu. |
| List ID | Select the list from the drop-down menu. |
| Custom task IDs | Select the boolean value from the drop-down menu. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the uploaded attachment in ClickUp. |
| Version | Version number of the file if multiple versions are supported or tracked. |
| Date | Timestamp indicating when the attachment was uploaded. |
| Title | Name of the uploaded file. |
| Extension | File extension of the attachment (for example, `.pdf`, `.jpg`, `.docx`). |
| Thumbnail small | URL to a small-sized thumbnail preview of the file. |
| Thumbnail large | URL to a larger-sized thumbnail preview of the file. |
| URL | Direct link to download or access the uploaded attachment in ClickUp. |

---
