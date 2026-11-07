---
url: 'https://docs.workato.com/en/connectors/wrike/upload-attachment-action.md'
description: >-
  The Upload attachment action in the Wrike connector uploads a file to a
  specified folder or task, with support for files up to 500 MB.
---

# Wrike - Upload attachment action

The **Upload attachment** action uploads an attachment to a specified folder or task in Wrike. This action supports file uploads up to **500 MB**.

## Input

| Input field | Description |
| --- | --- |
| Folder ID | Enter the ID of the folder where the attachment is uploaded. Toggle to **Task ID** to upload the attachment to a task instead. |
| File name | Enter the name of the attachment file. |
| File content | Provide the content of the attachment. |

## Output

| Output field | Description |
| --- | --- |
| Attachment ID | Unique identifier for the uploaded attachment. |
| Author ID | Unique identifier of the user who uploaded the attachment. |
| File name | Name of the uploaded attachment file. |
| Created date | Timestamp indicating when the attachment was created. |
| Version | Version number of the uploaded attachment. |
| Attachment type | Type of attachment. |
| Content type | MIME type of the attachment. |
| Size | File size of the attachment in bytes. |
| Task ID | Unique identifier of the associated task, if applicable. |
| Folder ID | Unique identifier of the associated folder, if applicable. |
| Comment ID | Unique identifier of the associated comment, if applicable. |
| ID of current attachment version | Unique identifier of the most recent version of the attachment. |
| Preview URL | URL to preview the attachment. |
| Download URL | URL to download the attachment. |
| Video playlist URL | URL to access the attachment as a video playlist, if applicable. |
| Review IDs | List of review IDs associated with the attachment. |
| Width | Width of the attachment, if applicable. |
| Height | Height of the attachment, if applicable. |
| ID of origin attachment version | Unique identifier of the original version of the attachment. |

---
