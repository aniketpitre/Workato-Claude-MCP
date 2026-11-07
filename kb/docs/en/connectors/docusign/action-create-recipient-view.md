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
