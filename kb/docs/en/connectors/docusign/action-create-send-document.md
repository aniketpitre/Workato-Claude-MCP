---
url: 'https://docs.workato.com/en/connectors/docusign/action-create-send-document.md'
description: >-
  The Create/send document action in the Docusign connector lets you create and
  send a document for signing, with signers, routing, and signature tabs.
---

# Docusign - Create/send document action

The **Create/send document** action creates and sends a document for signing in Docusign.

You can send documents to multiple signers with configurable routing order, add signature and date fields (tabs), and position tabs using either anchor text or absolute X/Y coordinates. Refer to the Docusign [Tab concepts](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/) documentation for more information.

> **FILE URL**
> 
> Ensure the File URL is in a downloadable format when you configure this action. For example, if you're linking to a Google Drive document, you must follow `https://drive.google.com/uc?export=download&id=FILE_ID` and replace `FILE_ID`.

## Input

| Input field | Description |
| --- | --- |
| Email subject | Enter the subject line for the email that sends the envelope to recipients. |
| Status | Select **Send** to immediately send the envelope or **Create** to save it as a draft. |
| File URL | Provide the URL of the document file, including the file extension. |
| Signers | Configure the list of signers for the document. Use either this field or the legacy **Signer email** and **Signer name** fields. |
| Signers source list (Signers) | Provide a list datapill containing multiple signer records. |
| Email (Signers) | Enter the signer's email address. Note that if both this field and the legacy **Signer email** field are provided, the legacy field takes precedence. |
| Name (Signers) | Enter the signer's full name. Note that if both this field and the legacy **Signer name** field are provided, the legacy field takes precedence. |
| Routing order (Signers) | Specify the signing sequence (1 for first signer, 2 for second). Recipients receive the document in numerical order, with each recipient completing their action before the next receives it. Leave blank to send to all recipients simultaneously. |
| Client user ID (Signers) | Provide a client user ID to enable embedded signing for this recipient. Embedded signers don't receive email notifications and must sign through your app instead. |
| Access code (Signers) | Set an access code that recipients must enter before viewing and signing the envelope. |
| Note (Signers) | Add a note for the signer that displays before they review the document. |
| Require ID lookup (Signers) | Specify whether to enable ID verification for this signer. This setting is overridden if an **ID check configuration name** is provided. |
| ID check configuration name (Signers) | Specify the ID verification configuration to use for this signer. |
| Recipient type (Signers) | Select the recipient type. `Signers` receive the document for action, while `Carbon Copy` recipients only receive a notification copy after signing is complete. Other options include `Agent`, `Editor`, `Certified Delivery`, and `In-Person Signer`. |
| Phone authentication (Signers) | Configure phone authentication settings. |
| Can recipient provide number? (Phone authentication) | Indicate whether the recipient can provide their own phone number for authentication. |
| Sender provided numbers (Phone authentication) | Specify phone numbers that the sender provides for authentication. Phone numbers must include the country code. For example, `["+919876543210", "+918765432109"]`. |
| Sms authentication (Signers) | Configure SMS-based authentication settings. |
| Sender provided numbers (Sms authentication) | Provide phone numbers for SMS authentication. Phone numbers must include the country code. For example, `["+919876543210", "+918765432109"]`. |
| Identity verification (Signers) | Configure identity verification workflow settings. |
| Workflow ID (Identity verification) | Specify the identity verification workflow ID. Use a custom action with the [List identity verifications](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/identityverifications/list/) endpoint to find available workflow IDs for your account. |
| Email notification (Signers) | Customize email notifications sent to this signer. |
| Email subject (Email notification) | Override the default email subject for this specific signer. |
| Email body (Email notification) | Provide custom email body content for this signer. |
| Supported language (Email notification) | Select the language for email notifications sent to this signer. |
| Tabs (Signers) | Configure signature fields, date fields, and other form elements. This section enables you to add **Sign here** and **Date signed** tabs to the document. |
| Sign here tabs (Tabs) | Define signature field placement and properties. |
| Sign here tabs source list (Sign here tabs) | Provide a list datapill for multiple signature tabs. |
| Positioning type (Sign here tabs) | Select the positioning method. **Anchor** uses text strings in the document. **Absolute** uses X/Y coordinates. |
| Optional (Sign here tabs) | Mark the signature tab as optional. |
| Anchor string (Sign here tabs) | Enter text in the document to automatically position the signature tab nearby. Available when **Positioning type** is **Anchor**. |
| Anchor X offset (Sign here tabs) | Set the horizontal distance in pixels from the anchor text to position the signature tab. Available when **Positioning type** is **Anchor**. |
| Anchor Y offset (Sign here tabs) | Set the vertical distance in pixels from the anchor text to position the signature tab. Available when **Positioning type** is **Anchor**. |
| X position (Sign here tabs) | Set the horizontal pixel coordinate for absolute tab positioning. Available when **Positioning type** is **Absolute**. |
| Y position (Sign here tabs) | Set the vertical pixel coordinate for absolute tab positioning. Available when **Positioning type** is **Absolute**. |
| Page number (Sign here tabs) | Enter the page number for absolute positioning. Available when **Positioning type** is **Absolute**. |
| Date signed tabs (Signers) | Configure date fields that automatically populate when the document is signed. |
| Date signed tabs source list (Date signed tabs) | Provide a list datapill for multiple date tabs. |
| Positioning type (Date signed tabs) | Select the positioning method. **Anchor** uses text strings in the document. **Absolute** uses X/Y coordinates. |
| Anchor string (Date signed tabs) | Enter text in the document to automatically position the date tab nearby. Available when **Positioning type** is **Anchor**. |
| Anchor X offset (Date signed tabs) | Set the horizontal distance in pixels from the anchor text to position the date tab. Available when **Positioning type** is **Anchor**. |
| Anchor Y offset (Date signed tabs) | Set the vertical distance in pixels from the anchor text to position the date tab. Available when **Positioning type** is **Anchor**. |
| X position (Date signed tabs) | Set the horizontal pixel coordinate for absolute tab positioning. Available when **Positioning type** is **Absolute**. |
| Y position (Date signed tabs) | Set the vertical pixel coordinate for absolute tab positioning. Available when **Positioning type** is **Absolute**. |
| Page number (Date signed tabs) | Enter the page number for absolute positioning. Available when **Positioning type** is **Absolute**. |
| Signer email | Enter the email address for the document signer. Use this with **Signer name** as an alternative to the **Signers** array. |
| Signer name | Enter the full name of the document signer. Use this with **Signer email** as an alternative to the **Signers** array. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |
| URI | The URI of the envelope to be sent or created. |
| Status date time | The date and time the status was updated. |

---
