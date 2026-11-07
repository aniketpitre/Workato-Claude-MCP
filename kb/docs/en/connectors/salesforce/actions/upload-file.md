---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/upload-file.md'
description: This action uploads a file to Salesforce.
---

# Salesforce - Upload file action

This action uploads a file to Salesforce.

## Input

| Input fields | Description |
| --- | --- |
| File contents | Enter the binary contents of the file. You can use the drop-down menu to switch this field to **Use file URL** and input the file's URL. You must specify the **File name** or **Title** if you enter the file's binary contents. |
| File name | Enter the name of the file, including its extension. For example: `New file.csv` |
| Title | Optional. Enter a title for the file, including an extension. For example: `New file.csv` Workato sets the **File name** as the **Title** if this field is left blank. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| Content hub repository | The repository where the file is stored. |
| Moderation flags | Any moderation flags associated with the file in the content hub. |
| Motif | An object containing URLs for small, medium, and large icons that indicate the Salesforce record type. |
| Topics | An object containing the `Current page URL`, `Next page URL`, and `Topics`. |
| Checksum | MD5 checksum for the file. |
| Content modified date | The date the file was last modified. |
| Content size | The size of the file in bytes. |
| Content URL | Returns the URL if the file is a link. |
| Description | A description of the file. |
| Download URL | A URL from which you can download the file. |
| External document URL | The URL to external documents about the file. |
| External file permission information | Permissions information for the external file. |
| File asset | A reference for the file asset object. |
| File extension | The file extension. For example: `.pdf`, `.docx`, `.png` |
| File type | The type of file. |
| Flash rendition status | Specifies if a flash preview version of the file has been rendered. |
| ID | The file's Salesforce ID. |
| Is in my file sync | Indicates whether the file is synced with Salesforce Files Sync. |
| Is major version | Indicates whether the file is a major version. |
| Mime type | The file's MIME type. |
| Modified date | The date the file was last modified. |
| My subscription | The subscription status of the file. |
| Name | The name of the file. |
| Origin | Specifies the file source. Responses include `Chatter` and `Content`. |
| Owner | An object containing information about the file owner, such as their `Company name`, `ID`, and `Is active` status. |
| Page count | The number of pages in the file, if applicable. |
| Parent folder | An object containing information about the parent folder of the file, such as its `ID` and `URL`. |
| Pdf rendition status | Indicates whether a PDF preview version of the file has been rendered. |
| Publish status | Specifies the publish status of the file. `PendingAccess` indicates the file is pending publishing, `PrivateAccess` indicates the file is private, and `PublicAccess` indicates the file is public. |
| Rendition URL | A URL to the rendition for the file. |
| Rendition URL 240 by 180 | A URL to the 240 x 180 rendition resource for the file. |
| Rendition URL 720 by 480 | A URL to the 720 x 480 rendition resource for the file. |
| Repository file ID | The Salesforce ID for the repository file. |
| Repository file URL | A URL to the repository file. |
| Sharing option | Specifies the sharing settings for the file. Responses include `Allowed` and `Restricted`. |
| Sharing role | The sharing role of the file. Responses include `Admin`, `Collaborator`, `Owner`, `Viewer`, and `WorkspaceManaged`. |
| Text preview | A text preview of the file, if one is available. |
| Thumb 120 by 90 rendition status | Specifies the rendering status of the 120 x 90 preview image of the file. |
| Thumb 240 by 180 rendition status | Specifies the rendering status of the 240 x 180 preview image of the file. |
| Thumb 720 by 480 rendition status | Specifies the rendering status of the 720 x 480 preview image of the file. |
| Title | The title of the file. |
| Type | The type of object uploaded. |
| URL | The URL of the file. |
| Version number | The version number of the file. |

---
