---
url: >-
  https://docs.workato.com/en/connectors/pdf-tools-by-workato/actions/split-pdf.md
description: The Split PDF action splits a PDF document into multiple PDF files.
---

# PDF tools by Workato - Split PDF action

The **Split PDF** action splits a PDF document into multiple smaller files. You can split by specifying exact page ranges or by setting a fixed interval. The maximum number of output files is 50.

## Input

| Input field | Description |
| --- | --- |
| Source PDF | Provide the file content of the PDF to split. The maximum size is 100 MB. |
| Split mode | Select whether to split by specifying exact page ranges (for example, `1-5,6-10`) or by setting a fixed interval (for example, every `10` pages). Options are **Fixed interval** and **Page ranges**. |
| Output file naming | Enter a prefix for output file names (for example, `invoice` or `section`). Files are named as `[prefix]_1.pdf`, `[prefix]_2.pdf`, and so on. |
| Pages per file | Enter the number of pages to include in each output file (for example, `5`, `10`, or `20`). The last file may contain fewer pages if the total page count is not evenly divisible. This field is available if you select **Fixed interval** as the **Split mode**. |
| Page ranges | Define page ranges for each output file, separated by commas. Each range must be in the format `x-y`. For a single page, use `x-x` (for example, `1-1`). For example, `1-5,6-10,11-15` creates three files. This field is available if you select **Page ranges** as the **Split mode**. |

## Output

| Output field | Description |
| --- | --- |
| Files | A list of the split PDF files. Each item in the list contains the following fields. |
| File name (Files) | The name of the output file, for example, `document_1.pdf`. |
| Page count (Files) | The number of pages in the output file. |
| File content (Files) | The output PDF file as binary content. Use this output with file upload actions or storage connectors to save the file. |
| List size (Files) | The total number of files in the **Files** list. |
| List index (Files) | The position of the current file in the **Files** list. |
