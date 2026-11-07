---
url: >-
  https://docs.workato.com/en/connectors/aws-comprehend/classify-document-action.md
description: >-
  The Classify document action analyzes a document in real-time using a custom
  AWS Comprehend's classification model in Workato.
---

# AWS Comprehend - Classify document action

The **Classify document** action analyzes a document in real-time using a custom classification model.

## Input

| Input fields | Description |
| --- | --- |
| Endpoint ARN | Select or enter the Amazon Resource Number (ARN) of the endpoint. |
| File content | Use this parameter to input a text, PDF, Word, or image file. When you classify a document using a custom model, you can use this parameter to input an Amazon Textract, DetectDocumentText, or AnalyzeDocument output file. You can't use this field with the **Text** field. |
| Text | Enter the document text to analyze. You can't use this field with the **File content** field. |
| Document reader configuration | Expand to configure document reading settings. |
| Document read action | Select which Textract API to use: **Textract detect document text** (DetectDocumentText) or **Textract analyze document** (AnalyzeDocument). |
| Document read mode | Select **Service default** to use AWS Comprehend defaults for PDFs or **Force document read action** to use the specified Textract API. |
| Feature types | Select Amazon Textract features to apply. Required when using **Textract analyze document**. |

## Output

| Output fields | Description |
| --- | --- |
| Classes | Includes details about classes including: Name: The name of the class., Page: The page number in the input document., Score: The confidence score that Amazon Comprehend has this class correctly attributed. |
| Document metadata | Includes document metadata including: Extracted characters: List of pages in the document, with the number of characters extracted from each page.; Pages: Number of pages in the document. |
| Document type | Details about the document type including: Page: The page number in a document., Type: The document type. |
| Errors | Error code: The code for the cause of the error., Error message: Text message explaining the reason for the error., Page: Page number where the error occurred. |
| Labels | Name: The name of the label., Page: The page number where the label occurs. This field is present only if you configure the **File content** input field., Score: The confidence score that AWS Comprehend has the label correctly attributed. |
| Warnings | Page: Page number in the input document., Warn code: The type of warning., Warn message: Text message associated with the warning. |
