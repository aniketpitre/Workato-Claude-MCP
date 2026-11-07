---
url: >-
  https://docs.workato.com/en/connectors/pdf-tools-by-workato/actions/merge-pdf.md
description: The Merge PDF action combines multiple PDF documents into a single PDF file.
---

# PDF tools by Workato - Merge PDF action

The **Merge PDF** action combines multiple PDF files into a single PDF document, in the order provided. You must provide a minimum of 2 files and a maximum of 50. The total size of all input files must be under 100 MB.

## Input

| Input field | Description |
| --- | --- |
| PDF files | A list of PDF files to merge, in the order provided. Click **Add item** to add each file. You must provide at least 2 files and no more than 50. |
| File content (PDF files) | Provide the file content of a PDF to include in the merged output. |
| Output file name | Enter a name for the merged PDF file, without the extension. Only alphanumeric characters, underscores, and hyphens are allowed. For example, `merged_report`. |

## Output

| Output field | Description |
| --- | --- |
| File name | The name of the merged PDF file, for example, `merged_report.pdf`. |
| Merged file content | The merged PDF file as binary content. Use this output with file upload actions or storage connectors to save the file. |
| Total pages | The total number of pages in the merged PDF. |
| Source file count | The number of source PDF files combined into the merged output. |
