---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-get-envelope-form-data.md
description: >-
  The Get envelope form data action returns tab values entered by recipients on
  a completed envelope.
---

# Docusign - Get envelope form data action

The **Get envelope form data** action returns tab values entered by recipients on a completed envelope. You must enable the Docusign **Allow sender to download form data** account setting to use this action.

Refer to the Docusign [EnvelopeFormData:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeformdata/get/) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| Envelope ID | Enter the ID of the envelope. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The unique identifier of the envelope. |
| Status | The current status of the envelope. |
| Sent date time | The date and time when Docusign sent the envelope. |
| Form data | The form data associated with the envelope. |
| Name (Form data) | The name of the form field. |
| Value (Form data) | The value entered or selected for the form field. |
| Recipient form data | Form data grouped by recipient. |
| Name (Recipient form data) | The recipient's name. |
| Email (Recipient form data) | The recipient's email address. |
| Recipient ID (Recipient form data) | The unique identifier of the recipient. |
| Signed time (Recipient form data) | The date and time when the recipient completed signing. |
| Delivered time (Recipient form data) | The date and time when Docusign delivered the envelope to the recipient. |
| Form data (Recipient form data) | The form data associated with the recipient. |
| Name (Recipient form data > Form data) | The recipient's form field name. |
| Value (Recipient form data > Form data) | The value entered or selected by the recipient. |
