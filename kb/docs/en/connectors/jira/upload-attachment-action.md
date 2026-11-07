---
url: 'https://docs.workato.com/en/connectors/jira/upload-attachment-action.md'
description: This action uploads an attachment to an existing issue.
---

# Jira - Upload attachment action

The **Upload attachment** action uploads an attachment to an existing issue.

## Input

| Input field | Description |
| --- | --- |
| Issue ID or key | Enter the ID or key of the issue to upload an attachment to. |
| File content | Enter a file content datapill from the output of a separate action, such as [Download attachment](/en/connectors/jira/download-attachment-action). Alternatively, you can enter file contents manually and append a `.txt` or `.csv` file extension in the **File name** field. |
| File name | Enter the file name of the attachment to upload. |

## Output

| Output field | Description |
| --- | --- |
| Self | The API URL of the uploaded attachment. |
| Filename | The name of the uploaded attachment. |
| Author | Contains information about the original author, including `Name` and `Account ID`. |
| Created | The date and time the attachment was created. |
| Size | The size of the attachment in bytes. |
| Mime type | The type and format of the attachment. |
| Content | A link to the attachment. |
| Thumbnails | A link to the attachment's thumbnail. |
| List size | The total number of attachments in the issue. |
| List index | The position of the current attachment in the list. |

---
