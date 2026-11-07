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
