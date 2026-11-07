---
url: 'https://docs.workato.com/en/connectors/wrike/get-attachment-meta-action.md'
description: >-
  The Get attachment metadata batch action in the Wrike connector retrieves
  metadata for an attachment, including current and past versions.
---

# Wrike - Get attachment metadata batch action

The **Get attachment metadata** batch action retrieves metadata information for an attachment in Wrike. Use the [Get record ID action](/en/connectors/wrike/get-record-id-action) to obtain an attachment ID from its permalink URL.

## Input

| Input field | Description |
| --- | --- |
| Attachment ID | Enter the attachment ID to retrieve metadata for. |
| Retrieve past versions? | Select **Yes** to retrieve previous versions of the attachment. Defaults to **No**. |

## Output

| Output field | Description |
| --- | --- |
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
| List size | Total number of items in the batch. |
| List index | Position of the current attachment in the batch. |

---
