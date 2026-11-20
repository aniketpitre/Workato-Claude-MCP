---
url: 'https://docs.workato.com/en/connectors/docusign/action-create-envelope.md'
description: >-
  The Create envelope action in the Docusign connector creates and sends an
  envelope from uploaded documents or an existing template.
---

# Docusign - Create envelope action

The **Create envelope** action creates an envelope in Docusign using uploaded documents or an existing template. It supports additional recipient and field configuration options that the [Create/send document](/en/connectors/docusign/action-create-send-document) and [Send document using a template](/en/connectors/docusign/action-send-document-using-template) don't expose.

Refer to the Docusign [Envelopes: create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) API reference for more information.

## Input

| Input field | Description |
| --- | --- |
| Create from | Select whether to create the envelope from uploaded documents or an existing template. Defaults to **Documents**. |
| Documents | Add the documents to include in the envelope. Each document is base64-encoded and sent in a single request. Docusign allows up to 32 MB per document through the API, but base64 encoding adds about 33% overhead. Keep each original file under 25 MB to account for base64 encoding overhead and the overall request size limit. Available when **Create from** is **Documents**. |
| Documents source list (Documents) | Provide a list datapill containing multiple documents. |
| File URL (Documents) | Enter the URL of the file, including the file extension. For example, `https://test.io/wp-content/uploads/2019/02/testIO-logo-rgb-2.png` Click **Use file contents** to provide raw file contents instead of a URL. |
| File name (Documents) | Enter the file name, including its extension (for example, `sample.pdf`). The extension must match the actual file contents, since Docusign uses it to interpret the document. Refer to Docusign's [supported file formats](https://support.docusign.com/s/document-item?language=en_US&bundleId=gbo1643332197980&topicId=xln1578456261162.html) for more information. Required when **File URL** is switched to **Use file contents**. |
| Recipients | Configure the recipients for the envelope. Available when **Create from** is **Documents**. |
| Recipients source list (Recipients) | Provide a list datapill containing multiple recipient records. |
| Email (Recipients) | Enter the recipient's email address. |
| Name (Recipients) | Enter the recipient's full name. |
| Routing order (Recipients) | Enter the signing order (for example, `1` for first recipient, `2` for second). Must be a positive integer that doesn't exceed the number of recipients. Leave blank to send to all recipients at once. |
| Client user ID (Recipients) | Provide a client user ID to enable embedded signing for this recipient. |
| Access code (Recipients) | Set an access code that the recipient must enter before viewing and signing the envelope. |
| Note (Recipients) | Add a note for the recipient that displays before they review the document. |
| Recipient type (Recipients) | Select the recipient type. Defaults to **Signer**. Other options include **Carbon Copy**, **Agent**, **Editor**, **Certified Delivery**, and **Intermediary**. The action doesn't support in-person signers or witnesses. |
| Require ID lookup (Recipients) | Select **Yes** to require ID verification for this recipient. Authentication methods configured in **Authentication settings** override this setting. |
| Authentication settings (Recipients) | Configure authentication settings for this recipient. |
| Authentication type (Authentication settings) | Select the authentication type to apply to this recipient. The option you select determines which setting applies: **Phone authentication**, **Sms authentication**, or **Identity verification**. |
| Phone authentication (Authentication settings) | Configure phone authentication settings. Available when **Authentication type** is set to phone authentication. |
| Can recipient provide number? (Phone authentication) | Select **Yes** to let the recipient provide their own phone number for authentication. |
| Sender provided numbers (Phone authentication) | Enter phone numbers that the sender provides for authentication. Phone numbers must include the country code. For example, `["+919876543210", "+918765432109"]`. |
| Sms authentication (Authentication settings) | Configure SMS-based authentication settings. Available when **Authentication type** is set to SMS authentication. |
| Sender provided numbers (Sms authentication) | Enter phone numbers for SMS authentication. Phone numbers must include the country code. For example, `["+919876543210", "+918765432109"]`. |
| Identity verification (Authentication settings) | Configure identity verification settings. Available when **Authentication type** is set to identity verification. |
| Workflow ID (Identity verification) | Enter the identity verification workflow ID. |
| Email notification (Recipients) | Customize the email notification sent to this recipient. |
| Email subject (Email notification) | Override the default email subject for this recipient. |
| Email body (Email notification) | Enter custom email body content for this recipient. |
| Supported language (Email notification) | Select the language for email notifications sent to this recipient. You must enable **Allow Sender to set email language for recipients** in your Docusign account settings. If the recipient has a Docusign account, their account language preference overrides this setting. |
| Tabs (Recipients) | Configure signature and date fields for this recipient. |
| Sign here tabs (Tabs) | Define signature field placement and properties. |
| Sign here tabs source list (Sign here tabs) | Provide a list datapill containing multiple signature tabs. |
| Positioning type (Sign here tabs) | Select the positioning method. **Anchor** uses text strings in the document. **Absolute** uses X/Y coordinates. |
| Anchor string (Sign here tabs) | Enter text in the document to position the signature tab nearby. Available when **Positioning type** is **Anchor**. |
| Anchor X offset (Sign here tabs) | Set the horizontal offset in pixels from the anchor text. Available when **Positioning type** is **Anchor**. |
| Anchor Y offset (Sign here tabs) | Set the vertical offset in pixels from the anchor text. Available when **Positioning type** is **Anchor**. |
| X position (Sign here tabs) | Set the horizontal pixel coordinate for the tab. Available when **Positioning type** is **Absolute**. |
| Y position (Sign here tabs) | Set the vertical pixel coordinate for the tab. Available when **Positioning type** is **Absolute**. |
| Page number (Sign here tabs) | Enter the page number to place the tab on. Available when **Positioning type** is **Absolute**. |
| Document ID (Sign here tabs) | Enter the document's position in the **Documents** list (for example, `1` for the first document). Defaults to `1` if you leave this field blank. Available when **Positioning type** is **Absolute**. |
| Optional (Sign here tabs) | Select **Yes** to mark the signature tab as optional. |
| Date signed tabs (Tabs) | Configure date fields that populate automatically when the recipient signs. |
| Date signed tabs source list (Date signed tabs) | Provide a list datapill containing multiple date tabs. |
| Positioning type (Date signed tabs) | Select the positioning method. **Anchor** uses text strings in the document. **Absolute** uses X/Y coordinates. |
| Anchor string (Date signed tabs) | Enter text in the document to position the date tab nearby. Available when **Positioning type** is **Anchor**. |
| Anchor X offset (Date signed tabs) | Set the horizontal offset in pixels from the anchor text. Available when **Positioning type** is **Anchor**. |
| Anchor Y offset (Date signed tabs) | Set the vertical offset in pixels from the anchor text. Available when **Positioning type** is **Anchor**. |
| X position (Date signed tabs) | Set the horizontal pixel coordinate for the tab. Available when **Positioning type** is **Absolute**. |
| Y position (Date signed tabs) | Set the vertical pixel coordinate for the tab. Available when **Positioning type** is **Absolute**. |
| Page number (Date signed tabs) | Enter the page number to place the tab on. Available when **Positioning type** is **Absolute**. |
| Document ID (Date signed tabs) | Enter the document's position in the **Documents** list (for example, `1` for the first document). Defaults to `1` if you leave this field blank. Available when **Positioning type** is **Absolute**. |
| Template | Select the template to use for the envelope, or click **Use custom value** to enter the template ID manually. You can find the template ID at the end of the URL on the template's page. Available when **Create from** is **Template**. |
| Template roles | Assign recipients to the template's roles. Available when **Create from** is **Template**. |
| Template roles source list (Template roles) | Provide a list datapill containing multiple template roles. |
| Role name (Template roles) | Enter the role name defined in the template. |
| Name (Template roles) | Enter the full name of the recipient assigned to this role. |
| Email (Template roles) | Enter the email address of the recipient assigned to this role. |
| Routing order (Template roles) | Enter the signing order (for example, `1` for first recipient, `2` for second). |
| Email subject | Enter the subject line of the email sent to recipients. |
| Message | Enter the body text of the email sent to recipients. |
| Envelope status | Select **Draft** to save the envelope without sending it, or **Send** to send it to recipients immediately. Defaults to **Send**. |
| Custom fields | Add custom data to attach to the envelope. |
| Custom fields source list (Custom fields) | Provide a list datapill containing multiple custom fields. |
| Type (Custom fields) | Select the type of custom field. Defaults to **Text**. Select **List** to provide selectable list items. |
| Name (Custom fields) | Enter the name of the custom field. |
| Value (Custom fields) | Enter the value for the custom field. |
| Required (Custom fields) | Select **Yes** to require senders to enter or select a value for the custom field before they send the envelope. |
| Show (Custom fields) | Select **Yes** to display the custom field in the **Envelope Custom Fields** section when a user creates or sends an envelope. |
| List items (Custom fields) | Enter the selectable values for the custom field. Applies only when **Type** is **List**. |
| Expire after (days) | Enter the number of days before the envelope expires. Omitted from the request when left blank. |
| Expiration enabled | Select **Yes** to enable envelope expiration. Defaults to **Yes** when **Expire after (days)** is set. |
| Advanced (JSON) | Enter raw JSON to add fields that this action doesn't otherwise expose as inputs to the envelope request body. For example, `brandId`, `eventNotification`, and `workflow`. If values conflict, the other input fields take precedence over the values in **Advanced (JSON)**. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The unique identifier of the envelope. |
| URI | The URI of the envelope. |
| Status | The current status of the envelope. |
| Status date time | The date and time the status was updated. |

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
