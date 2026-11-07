---
url: 'https://docs.workato.com/en/connectors/textract/get-document-action.md'
description: >-
  The Get document analysis action retrieves the results of a previously started
  document analysis job in Amazon Textract.
---

# Amazon Textract – Get document analysis action

The **Get document analysis** action retrieves results from a document analysis job previously started in Amazon Textract.

## Input

| Input field | Description |
| --- | --- |
| Job ID | Enter the job ID returned from the [Start document analysis](/en/connectors/textract/start-document-action) action. This value is valid for 7 days. |
| Max results | Specify the number of results to return per page. Default is 1000. |
| Next token | Provide the token from the previous response to retrieve the next page of results. |

## Output

| Output field | Description |
| --- | --- |
| Job status | Status of the document analysis job. |
| Status message | Additional status message returned from Textract. |
| Analyze document model version | Version of the Textract model used for analysis. |
| Next token | Token for paginating results if more pages exist. |
| Document metadata | Metadata about the document such as page count. |
| Warnings | Any warnings returned by Textract. |
| Blocks | Array of blocks containing extracted content. |

---
