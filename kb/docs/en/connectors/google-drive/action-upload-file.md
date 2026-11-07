---
url: 'https://docs.workato.com/en/connectors/google-drive/action-upload-file.md'
description: Uploads a file to Google Drive using multipart streaming uploads.
---

# Google Drive - Upload file action

The **Upload file** action uploads a file to Google Drive with [multipart streaming uploads](/en/features/file-streaming). There is no fixed file size limit.

## Input

| Input field | Description |
| --- | --- |
| File contents | Enter the contents of the file to upload. Accepts a datapill such as File contents from other Workato triggers and actions. |
| File name | Define the name of the uploaded file. Defaults to **Untitled** if not provided. |
| Parent folder | Choose the folder where the file is stored. Select from the picklist or enter the folder ID directly. Enter the folder ID in `folder_id/shared_drive_id` format for shared drives. For example, `1fm6iCMYrN7roZZ-ynpVFRTVq9mellrWp/0AB6ZFCw3XdamUk9PAA`. Google Drive saves the file in My Drive if a value isn't provided. |
| Upload MIME type | Define the [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types) of the file. For example, `image/jpeg`. Google Drive automatically detects the MIME type if not provided. |
| Target MIME type | Specify the [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types) for conversion after upload. For example, `application/pdf`. Refer to the [Upload MIME types for Google Workspace documents](https://developers.google.com/drive/api/guides/manage-uploads#import-docs) guide for supported MIME types. |
| Description | Enter a description for the uploaded file. |
| Starred | Specify whether the file should be starred in Google Drive. Defaults to **No**. |
| Viewers can copy content | Enable or disable content copying for users with **View** access. Defaults to **Yes**. |
| Writers can share | Enable or disable file sharing for users with **Edit** access. Defaults to **Yes**. This setting applies to My Drive but not shared drives. |
| Chunk size (KB) | Adjust the chunk size for optimized throughput. Larger values increase speed but may hit API quotas. Defaults to **1024 KB**. Refer to [File streaming](/en/features/file-streaming) for more information. |
| Copy requires writer permission | Specify whether to disable these actions for readers and commenters. Defaults to **No**. |
| Properties | Provide key-value pairs visible to all users. |

> **MIME TYPE CONVERSION LIMITATIONS**
> 
> Google Drive doesn't support all MIME type conversions mentioned in its [API documentation](https://developers.google.com/drive/api/guides/manage-uploads#import-docs). Some common limitations include the following:
> 
> - **GIF/BMP conversion**: This conversion isn't supported.
>   
> - **Plain text to Google Sheets**: Set **Upload MIME type** to **CSV**. The file converts to a Google Docs document if you set the field to **Plain Text**.
>   
> - **HTML to Google Docs**: Google Drive only accepts specific HTML formats. You may need to manually adjust formatting. We recommend that you use `text/html` as a custom value instead of selecting **HTML** from the picklist. Contact Google Support if you need assistance with supported HTML formats.
>   
> - **JSON/Plain text to Google Apps Script**: Only specific formats are accepted, which are not well documented in the Google Drive API. Contact Google Support if you need assistance with supported formats.
>   

## Output

| Output field | Description |
| --- | --- |
| Kind | Displays whether the uploaded file is a file or folder. |
| ID | Returns the unique ID of the uploaded file. |
| Name | Name of the uploaded file. |
| Mime type | The [MIME type](https://developers.google.com/drive/api/guides/mime-types) of the uploaded file. |
| Parents | The list of parent folder IDs that contain the file/folder, such as the **List size** and **List index**. |
| Description | A short description of the file. |
| Starred | Indicates whether you have starred the file. |
| Viewers can copy content | Indicates whether users with **View** access can copy content. |
| Writers can share | Indicates whether users with **Edit** access can share the file. This field is not populated for shared drive files. |
| Properties | Returns custom key-value pairs assigned to the file. |

---
