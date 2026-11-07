---
url: 'https://docs.workato.com/en/connectors/docusign/action-resend-envelope.md'
description: >-
  The Resend envelope action in the Docusign connector lets you resend an
  envelope to recipients who have not yet completed their action.
---

# Docusign - Resend envelope action

The **Resend envelope** action resends an envelope to recipients who have not yet completed their action in Docusign. Refer to the Docusign [EnvelopeRecipients: update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/update/) API reference for more information.

## Input

| Input field | Description |
| --- | --- |
| Envelope ID | Enter the ID of the envelope to resend. |

## Output

| Output field | Description |
| --- | --- |
| Recipient update results | The results of updating each recipient in the envelope. |
| Recipient ID (Recipient update results) | The ID of the recipient that was updated. |
| Recipient ID GUID (Recipient update results) | The globally unique identifier (GUID) for the recipient. |
| Error details (Recipient update results) | Information about any error that occurred while updating the recipient. |
| Error code (Error details) | The code that identifies the error. |
| Error message (Error details) | A description of the error. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-send-document-using-template.md
description: >-
  The Send document using a template action in the Docusign connector lets you
  send a document based on a template you configure.
---

# Docusign - Send document using a template action

The **Send document using a template** action sends a document based on a template that you configure in Docusign. Refer to the Docusign [Envelopes: create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) API reference for more information.

## Input

| Input field | Description |
| --- | --- |
| Template | Select the template to use for the envelopes. |
| Email subject | Enter the subject line of the email message sent to all recipients. The line is limited to 100 characters, including any merged fields. It is not truncated and causes an error if it's longer than 100 characters. |
| Message | Enter the body of the email message sent to all envelope recipients. Maximum length is 10,000 characters. |
| Documents | Provide the URL of the document source files, including the file extension. Supported file formats are .csv, .doc, .jpg, .pdf, .png, .txt, and .xls. |
| Document status | Select the document status. Valid values are **Send** and **Draft**. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |
| URI | The URI of the envelope. |
| Status date time | The date and time the status was generated. |
| Status | The current status of the envelope, including the recipient's progress within that envelope. For example, **Created**, **Sent**, **Delivered**, **Signed**, **Completed**, **Declined**, **Voided**, **Deleted**, or **All**. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> This trigger provides a data tree with attributes and values for the specified object. Additional fields depend on the properties you select.

---

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

---
