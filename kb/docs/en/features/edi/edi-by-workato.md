---
url: 'https://docs.workato.com/en/features/edi/edi-by-workato.md'
description: >-
  EDI tools by Workato let you generate and parse EDI documents in recipes, with
  support for the EDIFACT, HL7, and X12 standards.
---

# EDI tools by Workato

Electronic Data Interchange (EDI) is a broad set of standards and protocols for exchanging commercial documents in B2B space. While outdated compared to modern alternatives like RESTful APIs, it's still widely used in commercial trade and other applications.

EDI tools by Workato enables you to embed Workato in EDI workflows by generating and processing EDI documents.

EDI by Workato supports the following standards:

- EDIFACT
- HL7
- X12

If your use case requires more than generating and processing EDI documents, Workato offers a complete EDI solution in partnership with [Orderful](https://www.workato.com/platform/b2b-edi). This solution offers trade partners management, support for EDI-specific protocols, handling EDI transactions, and more. Contact your Workato Customer Success Representative for more information.

## How to use EDI tools by Workato

You can access EDI tools by Workato from the recipe builder. It is a utility app, so you are not required to set up any connection to use it.

1. Select **EDI tools by Workato** in the actions application selector.
   
2. Select the action you plan to use. Choose **Generate EDI** to create an EDI file or **Parse EDI** to parse an EDI file.
   
3. Configure the corresponding action. Refer to our [Generate EDI action](/en/features/edi/generate-edi-action) or [Parse EDI action](/en/features/edi/parse-edi-action) documentation to learn more.
   

## Quotas

EDI tools by Workato has the following quotas:

| Description | Quota | Notes |
| --- | --- | --- |
| Parse EDI action supported file size | 2.5 MB | Files up to 5 MB may be processed depending on the number of segments and line items they contain. Files larger than 5 MB aren't supported. Contact your Customer Success Manager to learn about a Workato EDI solution for larger files or high-volume workflows. |
| Generate EDI action document size | Varies | Workato may fail to generate very large documents, such as an invoice with tens of thousands of line items or an interchange with thousands of transactions. Split large batches across multiple interchanges, or contact your Customer Success Manager to learn about a Workato EDI solution for high-volume workflows. |

Contact your Customer Success Manager to learn about the complete Workato EDI solution in partnership with [Orderful](https://www.workato.com/platform/b2b-edi) for larger files or high-volume workflows.

---
