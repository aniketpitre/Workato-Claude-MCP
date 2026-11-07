---
url: 'https://docs.workato.com/en/connectors/hibob/upload-document-action.md'
description: >-
  The **Upload document** action uploads a document to the specific folder in
  HiBob. The maximum file size allowed to upload is 1 MB.
---

# HiBob - Upload document action

The **Upload document** action uploads a document to a folder you specify in HiBob. The maximum file size you can upload is 1 MB.

## Input

| Input field | Description |
| --- | --- |
| Document location | Select the location from the drop-down menu. |

Input fields are dynamically loaded based on the selected location. The following example displays the input schema for a **Shared** location:

| Input fields | Description |
| --- | --- |
| Employee ID | Provide the ID of the employee. |
| File content | Provide the file content to upload. |
| File name | Provide the file name with extension. |

## Output

| Output fields | Description |
| --- | --- |
| ID | Returns the ID of the uploaded document. |

---
