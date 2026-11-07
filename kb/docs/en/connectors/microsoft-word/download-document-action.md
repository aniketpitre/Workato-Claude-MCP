---
url: >-
  https://docs.workato.com/en/connectors/microsoft-word/download-document-action.md
description: >-
  The Download document action downloads a Word document as XML, binary (.docx),
  or PDF.
---

# Microsoft Word - Download document action

The **Download document** action downloads a Word document in XML, binary (.docx), or PDF format.

## Input

| Input field | Description |
| --- | --- |
| File source | Select where the document is stored. Options are **OneDrive** and **SharePoint**. |
| Document | Select the Word document from a folder-tree list scoped to the file source you selected. |
| Output format | Choose the format the action returns. **Document body XML** returns the WordprocessingML body content. **Raw binary** returns the full `.docx` file. **PDF** converts the document to PDF. |

## Output

| Output field | Description |
| --- | --- |
| Content | The downloaded file content, in the format specified by **Output format**. |
| Content type | The returned file MIME type, which varies based on the selected output format. |
| File name | The downloaded file name. |
