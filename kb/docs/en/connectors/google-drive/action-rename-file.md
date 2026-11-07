---
url: 'https://docs.workato.com/en/connectors/google-drive/action-rename-file.md'
description: Renames or moves a file or folder in Google Drive.
---

# Google Drive - Rename or move file/folder action

The **Rename or move file/folder** action renames or moves a file or folder in Google Drive.

- To rename the file/folder, use the **Name** field.
- To move the file/folder, use the **Parent folder** field.
- To rename **and** move the file/folder, use both fields.

> **MOVING FROM MY DRIVE TO A SHARED DRIVE**
> 
> Google Drive does not allow you to move a folder from your My Drive to a shared drive. You can only move files.

![Google Drive Rename or move file/folder action](/assets/google-drive-rename-file.CSocuXKI.png) _Google Drive Rename or move file/folder action_

## Input

| Output field | Description |
| --- | --- |
| File or folder ID | The ID of the file or folder you plan to rename and/or move. **To find the folder ID**: Select the folder and copy the ID at the end of the URL. For example, if the URL is `https://drive.google.com/drive/folders/1ACP9OB-WJQutUk9ABC`, the folder ID is `1ACP9OB-WJQutUk9ABC`.; **To find the file ID**: Right-click the file and select **Share > Copy link**. For example, if the URL is `https://drive.google.com/file/d/123nyR2IjW_Rq84d3qEYRoq1/view`, the file ID is `123nyR2IjW_Rq84d3qEYRoq1`. Alternatively, you can find the file or folder ID in the output of other Google Drive triggers and actions. |
| Name | New name of the file or folder you plan to **rename**. |
| Parent folder | New parent folder of the file or folder you plan to **move**. Select a parent folder from the picklist or enter its folder ID directly. **To find the parent folder ID**: Select the parent folder and copy the ID at the end of the URL. For example, if the URL is `https://drive.google.com/drive/folders/1ACP9OB-WJQutUk9ABC`, the folder ID is `1ACP9OB-WJQutUk9ABC`. Alternatively, you can find the folder ID in the output of other Google Drive triggers and actions. If you are entering the folder ID for a shared drive (formerly Team Drive), this value must be in the form `folder_id/shared_drive_id` (for example, `1fm6iCMYrN7roZZ-ynpVFRTVq9mell1Wp/0AB6ZFCw3XdamUk91AA`). |

## Output

Note that in Google Drive API, the terms `folder` and `file` are used interchangeably. A `folder` is technically a special `file`. As a result, whenever the field name or field description mentions `file`, it also applies to `folder`.

| Output field | Description |
| --- | --- |
| Kind | Identifies what kind of resource this is (for example, file or folder). |
| Name | The name of the file/folder. |
| File ID | The ID of the file/folder. |
| MIME type | The MIME type of the file/folder, as stated in [Google Drive's documentation](https://developers.google.com/drive/api/v3/mime-types). |
| Parents | The list of parent folder IDs that contain the file/folders, including the **List size** and **List index**. |

---
