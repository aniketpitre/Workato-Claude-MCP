---
url: 'https://docs.workato.com/en/connectors/docusign/action-void-envelope.md'
description: >-
  The Void envelope action in the Docusign connector lets you void an in-process
  envelope so that it can no longer be acted on.
---

# Docusign - Void envelope action

The **Void envelope** action voids an in-process envelope so that it can no longer be acted on by recipients in Docusign. Only envelopes in **sent** or **delivered** status can be voided. Refer to the Docusign [Envelopes: update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/) API reference for more information.

## Input

| Input field | Description |
| --- | --- |
| Envelope ID | Enter the ID of the envelope to void. |
| Voided reason | Provide the reason the envelope was voided. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |

---
