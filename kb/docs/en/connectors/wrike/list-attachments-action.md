---
url: 'https://docs.workato.com/en/connectors/wrike/list-attachments-action.md'
description: >-
  The List attachments batch action in the Wrike connector retrieves attachments
  for the entire workspace or filtered by a specific task or folder.
---

# Wrike - List attachments action (batch)

The **List attachments** batch action retrieves Wrike attachments for the entire workspace or filtered by task or folder.

## Input

| Input field | Description |
| --- | --- |
| Created date range | Filter attachments by creation date. Required when retrieving attachments from the entire Wrike account. The date range must be less than **31 days**. |
| Retrieve attachment URLs | Select **Yes** to generate temporary URLs for the attachments. The URLs are valid for **24 hours**. Defaults to **No**. |
| Retrieve past versions? | Select **Yes** to include previous versions of the attachments. Defaults to **No**. |
| Folder ID | Enter a folder ID to retrieve attachments from a specific folder. Toggle to **Task ID** to retrieve attachments from a specific task. |

## Output

| Output field | Description |
| --- | --- |
| Attachments list | List of retrieved attachments. |
| Attachment ID | Unique identifier for the attachment. |
| Author ID | Unique identifier of the user who uploaded the attachment. |
| File name | Name of the attachment file. |
| Created date | Timestamp indicating when the attachment was created. |
| Version | Version number of the attachment. |
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
| List size | Total number of attachments retrieved in the batch. |
| List index | Position of the current attachment in the batch. |

---
