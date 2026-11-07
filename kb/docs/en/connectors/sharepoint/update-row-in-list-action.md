---
url: 'https://docs.workato.com/en/connectors/sharepoint/update-row-in-list-action.md'
description: >-
  The update row action in the SharePoint connector lets you update a single row
  in a list you specify by its row ID and field values.
---

# SharePoint - Update row in SharePoint list action

This action updates a row in a specified SharePoint list.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the specific list where you plan to update a row. |
| Row ID | Provide the ID of the row to be updated. |
| **{List fields}** | Provide input for the list fields you plan to update. These fields are dynamic and are determined by the list you select. For example, a list of employees could include fields for the employee name, title, and contact information. |

## Output

The output datatree contains the status of the update operation.

| Field | Description |
| --- | --- |
| Success | The status of the update operation. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/update-rows-in-list-action-batch.md
description: >-
  The update rows action in the SharePoint connector lets you update a batch of
  rows in a list you specify using row IDs and field values.
---

# SharePoint - Update rows in SharePoint list action (batch)

This action updates a batch of rows in a SharePoint list you specify. To update multiple rows, select the list containing the rows you plan to update, provide the row/item IDs and the updated values of the list fields.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the list where you plan to update rows. |
| Batch | Specify the batch of rows you plan to update. Each row should contain the row ID and the fields you plan to update. |
| Batch source list | Input a list datapill to specify which rows to update. [Learn more about list input](/en/features/list-management#list-batch-action). |
| Row ID | Provide the ID of the row or item you plan to update. |
| **{List fields}** | Provide input for the list fields you plan to update. These fields are dynamic and are determined by the list you select. For example, a list of employees could include fields for the employee name, title, and contact information. |

## Output

The output datatree contains the status of the update operation for each row.

| Field | Description |
| --- | --- |
| Record status | The status of the update operation for each row. This object contains the Row ID, whether the operation was successful, and the list size and list index. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/upload-attachment-in-list-action.md
description: >-
  The upload attachment action in the SharePoint connector lets you upload an
  attachment to an item you specify in a list.
---

# SharePoint - Upload attachment in SharePoint list action (file)

This action uploads an attachment to a specified item in a SharePoint list.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the list to which to upload the attachment. |
| Item ID | Provide the ID of the item to which the attachment is uploaded. |
| File name | Provide the name of the file you plan to upload. |
| Content | Provide the content of the file you plan to upload. |

## Output

The output datatree contains the details of the uploaded attachment.

| Field | Description |
| --- | --- |
| File name | The name of the uploaded file. |
| File name as path | The path of the uploaded file. |
| Server relative path | The server relative path of the uploaded file. |
| Server relative URL | The server relative URL of the uploaded file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/upload-file-in-library-action.md
description: >-
  The upload file action in the SharePoint connector lets you upload a file to a
  folder you specify in a library.
---

# SharePoint - Upload file in SharePoint library action (file)

This action uploads a file to a specified folder in SharePoint library.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Folder | The folder where you plan to upload the file. You can either select the folder from the drop-down, or enter the server relative URL, which is available in the output of other SharePoint actions. For example, `/Shared Documents/Test/`. |
| File name | The name of the file you plan to upload. |
| File contents | The content of the file you plan to upload. |

## Output

The output datatree contains the details of the uploaded file.

| Field | Description |
| --- | --- |
| ID | The unique identifier of the uploaded file. |
| Name | The name of the uploaded file. |
| Server relative URL | The URL of the uploaded file relative to the SharePoint server. |
| Exists | Indicates whether the uploaded file exists. |
| Type | The file type or extension of the uploaded file. |
| Edit link | The URL for editing properties of the uploaded file. |
| Check in comment | Comments associated with checking in the uploaded file. |
| Check out type | The type of check-out (e.g., online, offline) for the uploaded file. |
| Content tag | The tag associated with the content of the uploaded file. |
| Customized page status | Indicates if the page of the uploaded file is customized. |
| E tag | The entity tag (ETag) for versioning of the uploaded file. |
| IRM enabled | The Information Rights Management (IRM) status of the uploaded file. |
| Length | The size or length of the uploaded file. |
| Level | The security level of the uploaded file. |
| Major version | The major version number of the uploaded file. |
| Minor version | The minor version number of the uploaded file. |
| Linking URI | The URI linking to the uploaded file. |
| Linking URL | The URL linking to the uploaded file. |
| Time created | The date and time the uploaded file was created. |
| Time last modified | The date and time the uploaded file was last modified. |
| Title | The title or display name of the uploaded file. |
| UI version | The User Interface (UI) version of the uploaded file. |
| UI version label | The label for the UI version of the uploaded file. |
| Unique ID | The unique identifier of the uploaded file. |
| Metadata | The metadata associated with the uploaded file. |
| Author | The author who uploaded the file. |
| Checked out by user | The user who has checked out the uploaded file. |
| Effective information management settings | The settings for effective information management related to the uploaded file. |
| Information rights management settings | The settings for information rights management related to the uploaded file. |
| List item all fields | All fields related to the uploaded file in the SharePoint list. |
| Locked by user | The user who has locked the uploaded file. |
| Modified by | The user who last modified the uploaded file. |
| Properties | Additional properties of the uploaded file. |
| Version events | The events related to the versioning of the uploaded file. |
| Versions | The versions available for the uploaded file. |

---
