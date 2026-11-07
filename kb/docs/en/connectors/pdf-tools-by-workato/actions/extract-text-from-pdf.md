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
