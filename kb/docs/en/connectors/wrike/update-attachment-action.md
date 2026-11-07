---
url: 'https://docs.workato.com/en/connectors/wrike/update-attachment-action.md'
description: >-
  The Update attachment action in the Wrike connector overwrites an existing
  attachment, saving the new content as a new version of the file.
---

# Wrike - Update attachment action

The **Update attachment** action updates an existing attachment in Wrike. The previous content is overwritten, and the update is treated as a new version of the attachment.

You can access information about past and current versions of the attachment with the [Get attachment metadata](/en/connectors/wrike/get-attachment-meta-action) action.

## Input

| Input field | Description |
| --- | --- |
| Attachment ID | Enter the ID of the attachment to update. |
| File content | Provide the new attachment content. The API supports file sizes up to **500 MB**. |
| File name | Enter the new file name for the updated attachment. |

## Output

| Output field | Description |
| --- | --- |
| Attachment ID | Unique identifier for the updated attachment. |
| Author ID | Unique identifier of the user who uploaded the attachment. |
| File name | Name of the updated attachment file. |
| Created date | Timestamp indicating when the updated attachment was created. |
| Version | Version number of the updated attachment. |
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
