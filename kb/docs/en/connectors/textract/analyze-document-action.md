---
url: 'https://docs.workato.com/en/connectors/textract/analyze-document-action.md'
description: >-
  The Analyze document action extracts data from documents stored in S3 using
  advanced analysis features.
---

# Amazon Textract – Analyze document action

The **Analyze document** action uses Amazon Textract to extract structured data, such as tables, forms, queries, and signatures, from documents stored in an Amazon S3 bucket.

## Input

| Input field | Description |
| --- | --- |
| S3 bucket | Enter the name of the S3 bucket containing the document. |
| S3 object key | Enter the path or key to the object within the S3 bucket. |
| Feature types | Select one or more feature types to detect. You can choose from `FORMS`, `TABLES`, `QUERIES`, or `SIGNATURES`. |

## Output

| Output field | Description |
| --- | --- |
| Document metadata | Metadata about the input document. |
| Blocks | Array of recognized content blocks including key-value pairs, text, and page. |
| Warnings | Any warnings returned during document analysis. |
| Analyze document model version | The version of the Textract model used for the analysis. |
| Human loop activation output | Information about whether a human review was triggered. |

---
