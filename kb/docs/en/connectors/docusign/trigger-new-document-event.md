---
url: 'https://docs.workato.com/en/connectors/docusign/trigger-new-document-event.md'
description: >-
  The New document event trigger in the Docusign connector fires when someone in
  your organization sends a document, tracking the full signing lifecycle.
---

# Docusign - New document event trigger

The **New document event** trigger allows you to listen for events where someone in your organization is a sender of a Docusign email. Use this trigger to track the full lifecycle of a contract signing from draft to completion and sync it to systems like your CRM.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This lets your recipe capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Event | Select the event status. For example, **Created**, **Sent**, **Delivered**, **Signed**, **Completed**, **Declined**, **Voided**, or **Deleted**. If a status is not selected, the default value is **All**. |

> **TRIGGER CONDITIONS**
> 
> This trigger supports [Trigger conditions](/en/recipes/triggers#trigger-conditions) that you can use to filter incoming trigger events.

## Output

| Output field | Description |
| --- | --- |
| Status | The current status of the envelope, including the recipient's progress within that envelope. For example, **Created**, **Sent**, **Delivered**, **Signed**, **Completed**, **Declined**, **Voided**, **Deleted**, or **All**. |
| Documents URI | The URI of the document. |
| Recipients URI | The URI for retrieving the envelope's recipients. |
| Envelope URI | The URI of the envelope that contains one or more documents. |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |
| Custom fields URI | The URI of custom fields being reused in the document. |
| Notification URI | The URI used to redirect the browser after users have granted access to their Docusign account. |
| Status changed date time | The last time the status of the envelope changed. For example, when a document was signed or delivered. |
| Documents combined URI | The URI of the single PDF file with combined documents. |
| Certificate URI | The URI of the certificate used to verify the identity of the sender. |
| Templates URI | The URL of the template used for reusing envelopes. |
| Sign info | The data and details associated with a completed electronic signature, including the signer's identity, the timestamp of the signature, and other audit trail information. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> This trigger provides a data tree with attributes and values for the specified object. Additional fields depend on the properties you select.

---

---
url: >-
  https://docs.workato.com/en/connectors/docusign/trigger-new-document-received.md
description: >-
  The New document received trigger in the Docusign connector fires when a new
  document arrives in a single mailbox for the authenticated user.
---

# Docusign - New document received trigger

The **New document received** trigger is similar to the [New recipient event](/en/connectors/docusign/trigger-new-recipient-event) trigger except that it's scoped to a single mailbox for the authenticated user in Docusign. This trigger is useful in scenarios where you want to focus on a specific mailbox.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This lets your recipe capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. Determine how frequently to check for new events. Defaults to five minutes if left blank. Minimum value allowed is five minutes. |

## Output

| Output field | Description |
| --- | --- |
| Status | The current status of the envelope, including the recipient's progress within that envelope. For example, **Created**, **Sent**, **Delivered**, **Signed**, **Completed**, **Declined**, **Voided**, **Deleted**, or **All**. |
| Documents URI | The URI of the document. |
| Recipients URI | The URI for retrieving the envelope's recipients. |
| Attachments URI | The URI of the attachment file in the envelope. |
| Envelope URI | The URI of the envelope that contains one or more documents. |
| Email subject | The subject line of the email sent to recipients for signing. |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |
| Custom fields URI | The URI of custom fields being reused in the document. |
| Notification URI | The URI used to redirect the browser after users have granted access to their Docusign account. |
| Created date time | The date and time the envelope was created. |
| Last modified date time | The date and time the envelope was last modified. |
| Initial sent date time | The date and time the envelope was initially sent to the recipient. |
| Sent date time | The most recent date and time the envelope was sent to the recipient. |
| Delivered date time | The date and time the recipient viewed the document. |
| Completed date time | The date and time the recipient completed signing the document. |
| Documents combined URI | The URI of the single PDF file with combined documents. |
| Certificate URI | The URI of the certificate used to verify the identity of the sender. |
| Templates URI | The URL of the template used for reusing envelopes. |
| Expire enabled | Whether the envelope is configured with an expiration date. |
| Expire date time | The date and time the envelope expires and becomes void. |
| Expire after | The number of days until the envelope expires and becomes void. |
| Sender | The person or organization that initiates the envelope and distributes it to one or more recipients for review and/or signature. |
| Sign info | The data and details associated with a completed electronic signature, including the signer's identity, the timestamp of the signature, and other audit trail information. |
| Tabs | Placeholders in a document where recipients are required to provide input, such as a signature or text, or where calculated values are displayed. |
| Purge state | The status of an envelope and its documents within the purge queue, indicating whether and how they will be permanently deleted after a set retention period. |
| Is signature provider envelope | Indicates whether the envelope uses a third-party signature provider. |
| Any signer | Deprecated. This feature has been replaced by signing groups. |
| Envelope location | Reserved for Docusign. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> This trigger provides a data tree with attributes and values for the specified object. Additional fields depend on the properties you select.

Refer to the Docusign [API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/) for more information.

---
