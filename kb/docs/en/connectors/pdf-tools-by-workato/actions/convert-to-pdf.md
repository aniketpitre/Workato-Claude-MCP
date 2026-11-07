---
url: >-
  https://docs.workato.com/en/connectors/pdf-tools-by-workato/actions/convert-to-pdf.md
description: The Convert to PDF action converts a source document to a PDF file.
---

# PDF tools by Workato - Convert to PDF action

The **Convert to PDF** action converts a source document to a PDF file. Supported source formats are Word (`.docx`), Excel (`.xlsx`), CSV, Image (`.png`, `.jpg`), and HTML.

## Input

| Input field | Description |
| --- | --- |
| File format | Select the format of the source document. Options are **Word (.docx)**, **Excel (.xlsx)**, **CSV**, **Image (.png, .jpg)**, and **HTML**. |
| Source file | Provide the file content of the source document. The maximum size is 100 MB. |
| Output file name | Enter a name for the output PDF file, without the extension. Only alphanumeric characters, underscores, and hyphens are allowed. |

## Output

| Output field | Description |
| --- | --- |
| File name | The name of the converted PDF file, for example, `converted_report.pdf`. |
| Converted file content | The converted PDF file as binary content. Use this output with file upload actions or storage connectors to save the file. |
