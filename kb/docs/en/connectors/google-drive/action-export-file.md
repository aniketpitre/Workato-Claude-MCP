---
url: 'https://docs.workato.com/en/connectors/google-drive/action-export-file.md'
description: Exports Google files to other MIME types.
---

# Google Drive - Export file action

The **Export file** action exports a Google file to another MIME type, such as Google Sheets to Excel. You can use the exported file in subsequent recipe steps to upload it into another app. This action supports a maximum file size of **10MB** and only exports binary files.

## Input

| Input field | Description |
| --- | --- |
| File | Choose the file you plan to export. Select a file or enter its ID. Right-click the file and select **Share > Copy link** to find the file ID. For example, if the URL is `https://drive.google.com/file/d/123nyR2IjW_Rq84d3qEYRoq1/view`, the file ID is `123nyR2IjW_Rq84d3qEYRoq1`. Alternatively, you can find the file ID from the output of other Google Drive triggers and actions. |
| MIME type | Select the [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types) that you plan to export the file to. Select a type from the picklist or enter the type directly. Refer to the [Upload MIME types for Google Workspace documents](https://developers.google.com/drive/api/guides/manage-uploads#import-docs) guide for a list of supported MIME types. |

> **MIME TYPE CONVERSION LIMITATIONS**
> 
> Google Drive doesn't support all MIME type conversions mentioned in its [API documentation](https://developers.google.com/drive/api/guides/ref-export-formats). Some common limitations include the following:
> 
> - **HTML conversions**: Enter `text/html` as a custom value in the **MIME type** field instead of selecting **HTML** from the picklist.
> - **Conversions from Google Presentations**: You can only export Google Slides to PowerPoint Presentation (PPTX) or Open Document Presentation (ODP) formats.

## Output

| Output field | Description |
| --- | --- |
| File contents | Contents of the newly exported file. You can use this datapill in downstream actions. |
| Size | The size of the exported file in bytes. |

---
