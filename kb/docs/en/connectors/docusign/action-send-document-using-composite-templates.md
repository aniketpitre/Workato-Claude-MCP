---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-send-document-using-composite-templates.md
description: >-
  The Send document using composite templates action creates an envelope by
  combining one or more templates and assigning a shared recipient role across
  the templates.
---

# Docusign - Send document using composite templates action

The **Send document using composite templates** action creates an envelope by combining one or more templates and assigning a shared recipient role across the templates.

Refer to the Docusign [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| Template IDs | Select one or more templates to combine into a single envelope. |
| Role name | Enter the template recipient role name shared across all templates. |
| Name | Enter the recipient's full name. |
| Email | Enter the recipient's email address. |
| Email subject | Enter the subject line for the email sent to the recipient. |
| Message | Enter a message to include in the email sent to the recipient. |
| Document status | Select **Draft** to save the envelope as a draft or **Send** to send it. Defaults to **Send**. |
| Expire after (days) | Enter the number of days before the envelope expires. This field is omitted from the request when blank. |
| Expiration enabled | Enable envelope expiration. Defaults to true when **Expire after (days)** is set. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The unique identifier of the envelope. |
| URI | The URI of the envelope. |
| Status date time | The date and time of the most recent envelope status change. |
| Status | The current status of the envelope. |
