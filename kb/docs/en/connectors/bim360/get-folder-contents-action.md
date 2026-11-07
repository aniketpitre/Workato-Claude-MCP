---
url: 'https://docs.workato.com/en/connectors/bim360/get-folder-contents-action.md'
description: >-
  The get folder contents batch action retrieves the contents of a BIM 360
  folder you specify.
---

# BIM 360 - Get folder contents action (batch)

The **Get folder contents** batch action retrieves the contents of a BIM 360 folder you specify.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the folder you plan to retrieve. |
| Project name | Select the project that contains the folder you plan to retrieve. |
| Folder | Select the folder you plan to retrieve. |
| Filters | Specify filters to refine the folder contents. Refer to BIM 360's [Filtering](https://aps.autodesk.com/en/docs/data/v2/developers_guide/filtering/) guide for more information about available filters. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the folder. |
| Project ID | The BIM 360 ID of the project that contains the folder. |
| Folder ID | The BIM 360 ID of the folder. |
| Data | Contains information about the folder contents, such as `Links` and `Attributes`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/bim360/get-folder-info-in-a-project-action.md
description: >-
  The get folder info in a project action retrieves data about a BIM 360 folder
  you specify.
---

# BIM 360 - Get folder info in a project action

The **Get folder info in a project** action retrieves data about a BIM 360 folder you specify.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the folder you plan to retrieve. |
| Project name | Select the project that contains the folder you plan to retrieve. |
| Folder | Select the folder you plan to retrieve. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the folder. |
| Project ID | The BIM 360 ID of the project that contains the folder. |
| Folder ID | The BIM 360 ID of the folder. |
| Item ID | The BIM 360 ID of the item associated with the folder. |
| Item type | The type of item associated with the folder. |
| Attributes | Contains information about the folder's attributes, such as their `Name` an `Created at` date. |
| Links | Contains information about the folder's link, such as its `Href`. |
| Relationships | Contains information about the folder's relationships, such as their `Links` and `Parent`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/bim360/get-issue-in-a-project-v2-action.md
description: >-
  The get issue in a project (V2) action retrieves data about a BIM 360 issue
  you specify.
---

# BIM 360 - Get issue in a project (V2) action

The **Get issue in a project (V2)** action retrieves data about a BIM 360 issue you specify.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the issue you plan to retrieve. |
| Project name | Select the project that contains the issue you plan to retrieve. |
| Container ID | Provide the BIM 360 container ID you plan to retrieve an issue from. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the issue. |
| Project ID | The BIM 360 ID of the project that contains the issue. |
| ID | The BIM 360 ID of the issue. |
| Container ID | The BIM 360 ID of the container that contains the issue. |
| Display ID | A chronological and user-friendly ID for the issue. |
| Title | The issue's title. |
| Description | The issue's description. |
| Snapshot URN | The unique resource name (URN) for the snapshot associated with the issue. |
| Issue type ID | The BIM 360 ID of the issue type. |
| Issue subtype ID | The BIM 360 ID of the issue subtype. |
| Assigned to | The BIM 360 ID of the user, company, or role associated with the issue's current assignee. |
| Due date | The issue's due date. |
| Location ID | The issue's location breakdown structure (LBS) ID. |
| Location details | The issue's location in plain text. |
| Owner ID | The BIM 360 ID of the issue's owner. |
| Root cause ID | The BIM 360 ID of the issue's root cause type. |
| Issue template ID | The BIM 360 ID of the template used to create the issue. |
| Comment count | The number of comments on the issue. |
| Attachment count | The number of attachments on the issue. |
| Opened by | The BIM 360 ID of the user who opened the issue. |
| Opened at | A timestamp indicating when the issue was opened. |
| Closed by | The BIM 360 ID of the user who closed the issue. |
| Closed at | A timestamp indicating when the issue was closed. |
| Created by | The BIM 360 ID of the user who created the issue. |
| Created at | A timestamp indicating when the issue was created. |
| Updated by | The BIM 360 ID of the user who last updated the issue. |
| Updated at | A timestamp indicating when the issue was last updated. |
| Client created at | A timestamp indicating when the issue was created in the client's system. |
| Client updated at | A timestamp indicating when the issue was last updated in the client's system. |
| Status | The issue's current status, such as `draft`, `open`, or `closed`. |
| Assigned to type | Indicates whether `Assigned to` specifies a user, company, or role. |
| Permitted statuses | The statuses permitted for the issue. |
| Permitted attributes | The attributes permitted for the issue. |
| Permitted actions | The actions permitted for the issue. |
| Linked documents | Contains information about documents related to the issue, such as their `Type`, `Details`, and `Created at` date. |
| Official response | Contains information about the response to the issue, such as its `Responded at` date and `Response`. |
| Custom attributes | Contains information about the issue's custom attributes, such as their `Type`, `Title`, and `Attribute definition ID` . |
| Links | Contains information about the issue's associated links, such as their `Type` and `Data`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/bim360/get-object-in-a-project-action.md
description: >-
  The get object in a project action retrieves data about a BIM 360 object you
  specify.
---

# BIM 360 - Get object in a project action

The **Get object in a project** action retrieves data about a BIM 360 object you specify.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the type of object you plan to retrieve. |
| Hub name | Select the hub that contains the object you plan to retrieve. |
| Project name | Select the project that contains the object you plan to retrieve. |

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

> **OUTPUT FIELDS**
> 
> The `Cost attachment` and `Cost document` objects don't generate output fields.
> 
> Other objects may generate additional output fields. Refer to BIM 360’s [API guide](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/) for more information.

---
