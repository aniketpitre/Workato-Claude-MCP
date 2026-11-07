---
url: 'https://docs.workato.com/en/connectors/sap-ariba/download-file-action.md'
description: The Download file action downloads files from SAP Ariba.
---

# SAP Ariba - Download file action

The **Download file** action downloads files from SAP Ariba.

## Input

Input fields are dynamically generated based on the object you select. The following field is common to all object types:

| Input field | Description |
| --- | --- |
| Object | Select the object type of the file you plan to download. |

## Output

| Output field | Description |
| --- | --- |
| File content | The contents of the downloaded file. |
| File name | The name of the downloaded file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-ariba/get-record-details-id-action.md
description: >-
  Use the Get record details by ID action to retrieve record details from SAP
  Ariba by specifying a record ID.
---

# SAP Ariba - Get record details by ID action

Use the **Get record details by ID** action to retrieve record details from SAP Ariba by specifying a record ID.

> **COMPATIBLE APIS**
> 
> The SAP Ariba connector supports multiple APIs, and each API provides access to different objects and operations. Refer to the [Available APIs](/en/connectors/sap-ariba#available-apis) section to identify the APIs compatible with this action.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to retrieve, such as a Contract Workspace. Additional fields load dynamically based on the object you select. |
| {Object name} ID | Enter the unique identifier of the object to retrieve. This is typically a numeric or alphanumeric ID from SAP Ariba. You can obtain this ID using the [Search objects action](/en/connectors/sap-ariba/search-objects-action). |

## Output

The output of this action is determined by the object selected in the input. Use the data tree in the recipe editor to see all available output fields for your specific object and map them to subsequent steps.

---
