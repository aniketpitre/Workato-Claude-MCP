---
url: 'https://docs.workato.com/en/connectors/pdf-tools-by-workato.md'
description: >-
  The PDF tools by Workato connector lets you convert, stamp, split, merge, and
  extract text from PDF documents directly within recipes.
---

# PDF tools by Workato

The PDF tools by Workato connector enables you to process PDF documents directly within recipes. You can use this connector to convert, stamp, split, merge, and extract text from PDF files without external services or custom scripts.

## How PDF tools by Workato works

PDF tools by Workato provides the following actions:

- [Convert to PDF action](/en/connectors/pdf-tools-by-workato/actions/convert-to-pdf): Converts a source document (Word, Excel, CSV, image, or HTML) to a PDF file.
- [Extract text from PDF action](/en/connectors/pdf-tools-by-workato/actions/extract-text-from-pdf): Extracts raw text content from digital PDF documents and returns it page by page.
- [Merge PDF action](/en/connectors/pdf-tools-by-workato/actions/merge-pdf): Combines multiple PDF files into a single PDF document in the order provided.
- [Split PDF action](/en/connectors/pdf-tools-by-workato/actions/split-pdf): Splits a PDF document into multiple smaller files by page range or fixed interval.
- [Stamp PDF action](/en/connectors/pdf-tools-by-workato/actions/stamp-pdf): Adds text or image stamps as overlays on PDF pages while preserving the original content.

## Setup

PDF tools by Workato is a built-in connector. It doesn't require authentication or connection setup.

## Quotas

The PDF tools by Workato connector has the following quotas:

### Rate limits

| Description | Quota |
| --- | --- |
| PDF tools daily operations | 10,000 operations per day per workspace |
| PDF tools large file processing (files larger than 50 MB) | 10 operations per hour per workspace |

### File size quotas

| Description | Quota |
| --- | --- |
| PDF tools maximum file size per source file for all actions | 100 MB |

### Action-specific quotas

| Description | Quota |
| --- | --- |
| Merge PDF action maximum input | 50 files, 100 MB combined |
| Split PDF action maximum output | 50 output files |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/pdf-tools-by-workato/actions/extract-text-from-pdf.md
description: >-
  The Extract text from PDF action extracts raw text content from digital PDF
  documents, returning unstructured text.
---

# PDF tools by Workato - Extract text from PDF action

The **Extract text from PDF** action extracts raw, unstructured text from digital (machine-readable) PDF documents and returns the content page by page. Supported source PDFs include those created from Word, Excel, PowerPoint, web pages, or system-generated reports.

This action is commonly used to ingest PDF content into knowledge bases for AI agents or to prepare text for AI summarization.

> **Scanned PDFs and structured extraction aren't supported**
> 
> This action returns raw text only. It doesn't support scanned or image-based PDFs and doesn't extract data into a defined schema. To extract structured data, or to process scanned documents, use [IDP by Workato](/en/connectors/idp-by-workato) instead.

## Input

| Input field | Description |
| --- | --- |
| Source PDF | Provide the file content of the PDF to extract text from. The maximum size is 100 MB. |
| Page range | Specify the pages to extract text from. For example, `1-3,5-5,7-10`. Defaults to all pages if not specified. |

## Output

| Output field | Description |
| --- | --- |
| Pages | A list of pages with extracted text. Each item in the list contains the following fields. |
| Page number (Pages) | The page number in the source PDF, for example, `1`. |
| Content (Pages) | The extracted text content from the page. |
| List size (Pages) | The total number of pages in the **Pages** list. |
| List index (Pages) | The position of the current page in the **Pages** list. |

---

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

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/pdf-tools-by-workato/actions/stamp-pdf.md
description: >-
  The Stamp PDF action adds text or image stamps to PDF pages as overlays while
  preserving original content.
---

# PDF tools by Workato - Stamp PDF action

The **Stamp PDF** action adds text or image stamps as overlays on PDF pages while preserving the original content. You can use it to add invoice numbers, approval stamps, watermarks, or labels to PDF documents in your workflows.

> **Signed PDFs and PDF/A Compliance**
> 
> Stamping a signed PDF invalidates all signatures in the output file. Apply stamps before signing to keep signatures valid.
> 
> If the source PDF is PDF/A compliant (archival format), the stamped output no longer maintains PDF/A conformance.

## Input

| Input field | Description |
| --- | --- |
| Source PDF | Provide the file content of the PDF to stamp. The maximum size is 100 MB. |
| Stamp type | Select whether to stamp text or an image onto the PDF. |
| Image file | Provide the file content of the image to stamp. Maximum size is 10 MB. Accepted formats include `image/jpeg`, `image/png`, and `image/jpg`. This field is available if you select **Image** as the **Stamp type**. |
| Text content | Enter the text to stamp on the PDF. This field is available if you select **Text** as the **Stamp type**. |
| Page range | Specify the pages to stamp. For example, `1-3,5,7-10`. Defaults to all pages if not specified. |
| Position | Select the position of the stamp on the page. Defaults to `top_right` if not specified. |
| Horizontal margin | Set the horizontal distance in points from the page edge. This value applies to the left edge for left-aligned positions and to the right edge for right-aligned positions. Range is 0-200. Defaults to 20.0 points if not specified. |
| Vertical margin | Set the vertical distance in points from the page edge. This value applies to the top edge for top-aligned positions and to the bottom edge for bottom-aligned positions. Range is 0-200. Defaults to 20.0 points if not specified. |
| Image size | Choose **Large (40.0%)** or **Small (15.0%)**, or toggle to set a custom width between 1 and 100 percent of the page. Height adjusts automatically to preserve aspect ratio. Defaults to **Small** if not set. This field is available if you select **Image** as the **Stamp type**. |
| Text size | Enter the font size in points. The range is 6-72. Defaults to 12.0 if not specified. This field is available if you select **Text** as the **Stamp type**. |
| Text font | Specify the font style for the text stamp. Defaults to **Calibri** if not specified. If text contains Unicode characters outside of the supported font range, the system uses **Noto Sans** automatically. This field is available if you select **Text** as the **Stamp type**. |
| Text color | Specify the color of the text stamp. Defaults to black if not specified. This field is available if you select **Text** as the **Stamp type**. |

## Output

| Output field | Description |
| --- | --- |
| Content | The stamped PDF file as binary content. Use this output with file upload actions or storage connectors to save the modified PDF. |

## Example usage

This example recipe helps Finance teams track paid invoices. When a payment is completed, the recipe downloads the invoice PDF from Google Drive, applies a **PAID** stamp, and saves the stamped version back before archiving.

![Stamp PDF recipe workflow](/assets/stamp-pdf-recipe.Co3-hwQb.png)_Recipe workflow showing invoice stamping process_

The recipe downloads both the invoice PDF and the **PAID** stamp image from Google Drive, uses the **Stamp PDF** action to overlay the stamp in the top-right corner, then uploads the result.

The following tabs show the invoice before and after stamping:

**Before**

![Original invoice](/assets/invoice-example.rhKqDjfs.png)_Original invoice before stamping_

**After**

![Stamped invoice](/assets/invoice-example-paid.MPbsYNeK.png)_Invoice with PAID stamp applied to top-right corner_

---
