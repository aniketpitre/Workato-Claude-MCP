---
url: >-
  https://docs.workato.com/en/connectors/idp-by-workato/classify-document-action.md
description: >-
  The Classify document action in the IDP by Workato connector analyzes document
  content and assigns it to a predefined category with a confidence score.
---

# IDP by Workato - Classify document using IDP by Workato action

The **Classify document** action analyzes a document’s content and assigns it to a predefined category based on provided guidelines.

## Input

| Input field | Description |
| --- | --- |
| File contents | Provide the file content to classify. |
| File name | Enter the file name with its extension or specify the type in **File type**. |
| File type | Select the file type of the uploaded content. This overrides the inferred type from **File name**. Supported types include `png`, `jpg`, `webp`, `gif`, and `pdf`. PDF files can contain up to 50 pages with IDP model v4. Earlier versions support up to 15 pages. |
| List of categories | Create a list of categories to classify the text. |
| IDP version | Select the IDP version you plan to use. Refer to [IDP model versions](/en/connectors/idp-by-workato/idp-versions) for more information. |

## Output

| Output field | Description |
| --- | --- |
| Remaining calls | Number of IDP API calls left in the current period. |
| Consumed calls | Number of IDP API calls used. |
| Reset time | Timestamp when the call limit resets. |
| Category | Assigned category based on document content. |
| Confidence scores | Confidence level of the classification. |
