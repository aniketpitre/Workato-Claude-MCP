---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-recruiting/upload-record-action.md
description: The Upload record action uploads a document to UKG Pro (Recruiting).
---

# UKG Pro (Recruiting) - Upload record action

The **Upload record** action uploads a document to UKG Pro (Recruiting).

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve a list of records. Fields load dynamically based on the object you select. |

Workato dynamically populates additional fields depending on the object you select. For example, the **Application document** object has the following input fields:

| Input fields | Description |
| --- | --- |
| Application ID | Provide the unique ID of an application. |
| File | Provide the file name and content. The file name must not be empty, contain only spaces, or include these characters: `/ \\? : \* " \< \> |`. The file extension must be: `.jpg`, `.jpeg`, `.png`, `.pdf`, `.doc`, or `.docx`. |
| Metadata | Provide the metadata associated with an uploaded file. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the **Application document** object has the following output schema:

| Output field | Description |
| --- | --- |
| ID | The Application ID (GUID). |
| File name | The name of the uploaded file. |
| Document type | The type or category of the uploaded document. |
| Description | The description for the document. |
| Creator | The ID of the user who uploaded the document. |
| Links | URLs associated with the uploaded document. |
