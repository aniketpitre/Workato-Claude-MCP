---
url: 'https://docs.workato.com/en/connectors/bim360/get-project-details-action.md'
description: >-
  The get object in a project action retrieves data about a BIM 360 object you
  specify.
---

# BIM 360 - Get project details action

The **Get project details** action retrieves data about a BIM 360 project you specify.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project you plan to retrieve. |
| Project name | Select the project you plan to retrieve. |

## Output

| Output fields | Description |
| --- | --- |
| Project ID | The ID of the project. |
| Type | The project's type. |
| Attributes | Contains information about the project's attributes, such as their `Name` an `Scopes`. |
| Links | Contains information about the project's link, such as its `Href`. |
| Relationships | Contains information about the project's relationships, such as their `Location` and `Root folder`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/bim360/search-issues-in-a-project-v2-action.md
description: >-
  The search issues in a project (V2) batch action retrieves a list of the
  issues in a BIM 360 project you specify.
---

# BIM 360 - Search issues in a project (V2) action (batch)

The **Search issues in a project (V2)** batch action retrieves a list of issues from a BIM 360 project you specify.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project you plan to search. |
| Project name | Select the project that contains the container you plan to search. |
| Container ID | Provide the BIM 360 container ID you plan to retrieve issues from. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the issues. |
| Project ID | The BIM 360 ID of the project that was searched. |
| Pagination | Contains information about pagination of the returned `Results` list, such as `Limit`, `Offset`, and `Total results`. |
| Results | Contains information about the issues retrieved from BIM 360, such as their `ID`, `Title`, and `Description`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/bim360/search-objects-in-a-project-action.md
description: >-
  The search objects in a project action searches a BIM 360 project and returns
  a list of objects matching the type you specify.
---

# BIM 360 - Search objects in a project action

The **Search objects in a project** action searches a BIM 360 project and returns a list of objects matching the type you specify.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the type of object you plan to search for. |
| Hub name | Select the hub that contains the project you plan to search. |
| Project name | Select the project you plan to search. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the object. |
| Project ID | The BIM 360 ID of the project that contains the object. |
| Pagination | Contains information about pagination of the returned `Results` list, such as `Limit`, `Offset`, and `Total results`. |
| Results | Contains information about the objects retrieved from BIM 360, such as their `ID`, `Title`, and `Description` |

> **COST FILE PACKAGE OBJECT OUTPUT FIELDS**
> 
> The `Cost file package` object doesn't generate output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/bim360/update-issue-in-a-project-v2-action.md
description: >-
  The update issue in a project (V2) action updates an existing issue you
  specify in BIM 360.
---

# BIM 360 - Update issue in a project (V2) action

The **Update issue in a project (V2)** action updates an existing issue you specify in BIM 360.

> **REQUIRED PERMISSIONS**
> 
> Users must have one of the following permissions in BIM 360 to update issues:
> 
> - The project admin role. Refer to BIM 360's [Roles](https://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-7E2C374B-DADC-4E13-AEA7-C8DCF6838A31) guide for more information.
> - The `create`, `view and create`, or `full control` field management permissions. Refer to BIM 360's [Permissions: Field Management](https://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-7E2C374B-DADC-4E13-AEA7-C8DCF6838A31) guide for more information.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project you plan to update. |
| Project name | Select the project that contains the issue you plan to update. |
| Container ID | Provide the BIM 360 container ID where you plan to update an issue. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the issue. |
| Project ID | The BIM 360 ID of the project that contains the issue. |
| Pagination | Contains information about pagination of the returned `Results` list, such as `Limit`, `Offset`, and `Total results`. |
| Results | Contains information about the issues retrieved from BIM 360, such as their `ID`, `Title`, and `Description` |

---

---
url: >-
  https://docs.workato.com/en/connectors/bim360/update-object-in-a-project-action.md
description: >-
  The update object in a project action updates an existing object you specify
  in BIM 360.
---

# BIM 360 - Update object in a project action

The **Update object in a project** action updates an existing object you specify in BIM 360.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project you plan to update. |
| Project name | Select the project that contains the object you plan to update. |
| Container ID | Provide the BIM 360 container ID where you plan to update an object. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the object. |
| Project ID | The BIM 360 ID of the project that contains the object. |
| ID | The BIM 360 ID of the object. |
| Name | The name of the object. |
| Description | The object's description. |
| Creator ID | The ID of the user that created the object. |
| Changed by | Indicates the user that changed the object. |
| External ID | The ID of the object in an external system. |
| External system | The name of the external system that manages the object. |
| Created at | A timestamp indicating when the object was created. |
| Updated at | A timestamp indicating when the object was last updated. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> The **Update object in a project** action generates additional output fields based on your selected **Object**. Refer to BIM 360's [API guide](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/) for more information on BIM 360 objects.

---

---
url: >-
  https://docs.workato.com/en/connectors/bim360/upload-document-to-a-project-action.md
description: >-
  The upload document to a project action uploads a file to a project you
  specify in BIM 360.
---

# BIM 360 - Upload document to a project action

The **Upload document to a project** action uploads a file to a project you specify in BIM 360.

> **UPLOAD LOCATION LIMITATIONS**
> 
> The **Upload document to a project** action can't upload documents to BIM 360's root `Docs` folder. It can only upload to project folders and their sub-folders.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project where you plan to upload the document. |
| Project name | Select the project that contains the folder where you plan to upload the document. |
| Folder name | Select the folder where you plan to upload the document. |
| File name | Specify the file name and extension of the document you plan to upload. |
| Contents | Enter the contents of the file. |
| Upload threads | Specify the number of threads to use for processing the document. The default value is `10` and the maximum is `20`. |
| Item ID | Specify the BIM 360 item ID of the document. |
| File extension | Select the document's file extension type. |
| Type of version | Select the document's version type. |
| File size | Enter the file size in bytes. This is required for documents larger than 10 MB. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the document. |
| Project ID | The BIM 360 ID of the project that contains the document. |
| Folder ID | The BIM 360 ID of the folder that contains the document. |
| Item ID | The BIM 360 ID of the document. |
| Item type | The document's type. |
| Attributes | Contains information about the document's attributes, such as their `Name` an `Created at` date. |
| Links | Contains information about the document's link, such as its `Href`. |
| Relationships | Contains information about the document's relationships, such as their `Links` and `Parent`. |

---
