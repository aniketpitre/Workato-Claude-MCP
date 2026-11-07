---
url: 'https://docs.workato.com/en/connectors/textract/get-lending-action.md'
description: >-
  The Get lending analysis action retrieves the results of a lending document
  analysis job previously started in Amazon Textract.
---

# Amazon Textract – Get lending analysis action

The **Get lending analysis** action retrieves results from a lending document analysis job previously started in Amazon Textract.

## Input

| Input field | Description |
| --- | --- |
| Job ID | Enter the job ID returned from the [Start lending analysis](/en/connectors/textract/start-lending-action) action. This is valid for 7 days. |
| Max results | Specify the number of results to return per page. |
| Next token | Provide the token from the previous response to retrieve the next page of results. |

## Output

| Output field | Description |
| --- | --- |
| Job status | Status of the lending analysis job. |
| Status message | Additional status message returned from Textract. |
| Next token | Token for paginating results if more pages exist. |
| Analyze lending model version | Version of the Textract model used for lending analysis. |
| Document metadata | Metadata about the document such as page count. |
| Results | Lending-specific analysis results. |
| Warnings | Any warnings returned by Textract. |

---
