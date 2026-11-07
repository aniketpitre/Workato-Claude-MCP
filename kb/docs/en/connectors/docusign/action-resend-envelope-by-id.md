---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-resend-envelope-by-id.md
description: >-
  The Resend envelope by ID action in the Docusign connector resends a sent
  envelope to pending recipients and returns the envelope ID.
---

# Docusign - Resend envelope by ID action

The **Resend envelope by ID** action resends a previously sent envelope to pending recipients in Docusign. Refer to the Docusign [Envelopes: update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/) API reference for more information.

Alternatively, use the [Resend envelope](/en/connectors/docusign/action-resend-envelope) action to retrieve each recipient’s ID and GUID.

## Input

| Input field | Description |
| --- | --- |
| Envelope ID | Enter the ID of the envelope to resend. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |
| Error details | Information about any error that occurred while resending the envelope. |
| Error code (Error details) | The code that identifies the error. |
| Message (Error details) | A description of the error. |
