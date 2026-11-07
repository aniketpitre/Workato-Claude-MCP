---
url: 'https://docs.workato.com/en/connectors/docusign/trigger-new-recipient-event.md'
description: >-
  The New recipient event trigger in the Docusign connector fires on Recipient
  Connect events when someone in your organization receives a document.
---

# Docusign - New recipient event trigger

The **New recipient event** trigger is based on the Recipient Connect feature in Docusign that allows you to listen for events where someone in your organization is a receiver of a Docusign email. Use this trigger to relay these events to channels such as business messaging tools to notify the intended recipient further or log this event in your ERP system. To set up this trigger, you must claim the domain in Docusign. Refer to the Docusign [Recipient Connect](https://developers.docusign.com/platform/webhooks/connect/recipient-connect/) guide for more information.

## Input

Select the events that you want to be notified about. If none are selected, the default value is **All**.

| Input field | Description |
| --- | --- |
| Recipient events | Select the recipient events that trigger the recipe. |
| Recipient sent (Recipient events) | Sent when an email notification is sent to the recipient saying that it's their turn to sign an envelope. |
| Recipient auto responded (Recipient events) | Sent when Docusign receives a notification that an email delivery has failed. For example, because the email address is invalid, or the recipient has configured an automatic response. |
| Recipient delivered (Recipient events) | Sent when the recipient has viewed the documents in an envelope on the Docusign website. |
| Recipient completed (Recipient events) | Sent when the recipient has completed the required action, such as signing the envelope. |
| Recipient declined (Recipient events) | Sent when the recipient declines to sign the envelope. |
| Recipient authentication error (Recipient events) | Sent when the recipient fails an authentication check. If the recipient has multiple attempts to pass a check, the event is sent when the final attempt has failed. |
| Recipient resent (Recipient events) | Sent when an envelope is resent to a recipient through the web application or via an API call. |
| Recipient delegate (Recipient events) | Sent when a recipient assigns another user to sign envelopes on their behalf, ensuring document completion even when the original signer is unavailable. |
| Recipient reassign (Recipient events) | Sent when a recipient delegates signing responsibility to another person, provided the sender has enabled this feature. |
| Recipient finish later (Recipient events) | Sent when a recipient exits the signing process, saving their progress and any entered information to complete later using the link in the original email. |
| Set trigger conditions | Define additional rules for trigger events to run a recipe. Refer to [Trigger conditions](/en/recipes/triggers#trigger-conditions) for more information. |

Refer to [Webhook event triggers](https://developers.docusign.com/platform/webhooks/connect/event-triggers/) for more information.

## Output

| Output field | Description |
| --- | --- |
| Event | The event. For example, **Recipient sent**, **Recipient auto responded**, **Recipient delivered**, **Recipient completed**, and more. For a complete list, see the input fields described earlier. |
| Api version | The specific version of the eSignature REST API that your application is using. |
| URI | The URI of the recipient. |
| Retry count | Indicates how many times Docusign has attempted to deliver a connect event to the listener after an initial failure, combining instances of failure into a single count. |
| Configuration ID | A unique identifier assigned to a specific identity verification configuration. This ID helps administrators define and manage different methods for verifying signers' identities. |
| Generated date time | The date and time the event was generated. |
| Data | The IDs of the account, user, envelope, and recipient. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> This trigger provides a data tree with attributes and values for the specified object. Additional fields depend on the properties you select.

---

---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-create-draft-envelope-from-template.md
description: >-
  The Create draft envelope from template action in the Docusign connector lets
  you create a draft envelope based on a template you configure.
---

# Docusign - Create draft envelope from template action

The **Create draft envelope from template** action creates a draft envelope in Docusign based on a template that you configure. The envelope is saved with **created** status and not sent to recipients. Refer to the Docusign [Envelopes: create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) API reference for more information.

## Input

| Input field | Description |
| --- | --- |
| Template | Select the template to use for the envelope. |
| Email subject | Enter the subject line of the email message sent to all recipients. |
| Email blurb | Enter the body text of the email sent to recipients. |
| Template roles | Assign signers to template roles. |
| Template roles source list | Input a list datapill representing the template roles to assign. Refer to [Actions that accept list inputs](/en/features/list-management#list-batch-action) for more information. |
| Role name (Template roles) | Specify the role name defined in the template. |
| Name (Template roles) | Enter the full name of the recipient. |
| Email (Template roles) | Enter the email address of the recipient. |
| In person signer name (Template roles) | Enter the full name of the in-person signer. Required when the role is configured for in-person signing. |
| Custom fields | Set values for envelope custom fields defined in the template. |
| Custom fields source list | Input a list datapill representing the custom field values to set. Refer to [Actions that accept list inputs](/en/features/list-management#list-batch-action) for more information. |
| Field ID (Custom fields) | Specify the custom field ID defined in the template. |
| Value (Custom fields) | Enter the value to set for the custom field. |
| Prefill tabs | Set values for prefill tabs defined in the template. |
| Prefill tabs source list | Input a list datapill representing the prefill tab values to set. Refer to [Actions that accept list inputs](/en/features/list-management#list-batch-action) for more information. |
| Tab label (Prefill tabs) | Enter the tab label for text, date, and checkbox tabs. |
| Group name (Prefill tabs) | Enter the radio group name. Use this instead of **Tab label** for radio group tabs. |
| Value (Prefill tabs) | Enter the value to prefill. For radio group tabs, enter the value of the radio button to select. |
| Selected (Prefill tabs) | Enable to mark the tab as selected. Applicable for checkbox tabs. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |
| URI | The URI of the envelope. |
| Status date time | The date and time the status was generated. |
| Status | The current status of the envelope. |

---

---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-create-recipient-view.md
description: >-
  The Create recipient view action in the Docusign connector generates a URL for
  embedded signing of a Docusign envelope.
---

# Docusign - Create recipient view action

The **Create recipient view** action generates a URL in Docusign for embedded signing. Use it to let signers complete an envelope in your app instead of through an email from Docusign.

The action works with envelopes in the `sent` status and recipients who have a client user ID. Set the **Client user ID (Signers)** field when you create the envelope with the [Create/send document](/en/connectors/docusign/action-create-send-document) action, then enter the same value in the **Client user ID** input of this action.

Refer to the Docusign [EnvelopeViews: createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/) API reference for more information.

## Input

| Input field | Description |
| --- | --- |
| Envelope ID | Enter the ID of the Docusign [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) the recipient signs. |
| User ID | Enter the ID of the Docusign user associated with the recipient. This is the User ID field in the [Recipient fields](/en/connectors/docusign/action-get-envelope#recipient-fields) that the [Get envelope recipients](/en/connectors/docusign/action-get-envelope-recipients) action returns. |
| Client user ID | Enter the client user ID you set for this recipient when you created the envelope. This is the Client user ID field in the same [Recipient fields](/en/connectors/docusign/action-get-envelope#recipient-fields). |
| Return URL | Enter the URL to send the recipient to after the signing session ends. Include `https://` in the URL. Docusign appends an `event` query parameter to this URL with the outcome of the session. Refer to the Docusign [EnvelopeViews: createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/) API reference for the possible values. |
| Authentication method | Select the authentication method your application used to verify the signer's identity. This is recorded in the envelope's Certificate of Completion. |

## Output

| Output field | Description |
| --- | --- |
| URL | The signing URL for the recipient. Redirect the recipient to this URL right away. The URL works once and expires after 5 minutes, so don't store or email it. |

---
