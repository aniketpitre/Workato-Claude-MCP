---
url: 'https://docs.workato.com/en/connectors/textract/start-document-action.md'
description: >-
  The Start document analysis action initiates an asynchronous job to analyze a
  document stored in an S3 bucket using Amazon Textract.
---

# Amazon Textract – Start document analysis action

The **Start document analysis** action initiates an asynchronous analysis of a document stored in an Amazon S3 bucket using Textract. This action supports the extraction of structured data such as forms, tables, queries, and signatures.

## Input

| Input field | Description |
| --- | --- |
| S3 bucket | Enter the name of the S3 bucket containing the document to analyze. |
| S3 object key | Provide the path/key to the document in the specified S3 bucket. |
| Feature types | Select one or more feature types to analyze, such as `FORMS`, `TABLES`, `QUERIES`, or `SIGNATURES`. |

Additional input fields may appear based on the selected **Feature types**.

## Output

| Output field | Description |
| --- | --- |
| Job ID | Unique identifier for the document analysis job. Use this ID with the [Get document analysis](/en/connectors/textract/get-document-action) action to retrieve results. |

---
