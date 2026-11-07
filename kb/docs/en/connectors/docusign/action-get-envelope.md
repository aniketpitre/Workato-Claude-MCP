---
url: 'https://docs.workato.com/en/connectors/docusign/action-get-envelope.md'
description: >-
  The Get envelope action in the Docusign connector lets you retrieve the
  details of a single envelope by its ID.
---

# Docusign - Get envelope action

The **Get envelope** action retrieves the details of a single envelope in Docusign. Refer to the Docusign [Envelopes: get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/) API reference for the full field reference.

## Input

| Input field | Description |
| --- | --- |
| Envelope ID | Enter the ID of the envelope to retrieve. |
| Include | Select the additional information to return for the envelope. Refer to [Include options](#include-options) for available options. Recipients are included automatically. Use a comma-separated list to enter values manually. For example, `tabs,powerform`. |
| Advanced update | Select to allow envelope information to be added or modified. This input doesn't change the fields the action returns. |

### Include options

The **Include** input field controls which additional information the action returns for the envelope.

| Include option | Description |
| --- | --- |
| Custom fields | Returns the **Custom fields** field. |
| Documents | Returns the **Envelope documents** field. |
| Document fields | Adds no output field of its own. Select **Documents** to return the **Envelope documents** field. |
| Attachments | Returns the **Envelope attachments** field. |
| Extensions | Returns the **Notification** field. |
| Folders | Returns the **Folders** field. |
| Recipients | Returns the **Recipients** field. This option is automatically applied. |
| PowerForm | Returns the **Power forms** field. |
| Prefill tabs | Returns the **Envelope documents** field, with the prefill tabs of each document in its **Tabs** field. |
| Tabs | Returns the **Tabs** field for each recipient in the **Recipients** field. Refer to [Tab fields](#tab-fields) for the fields each tab contains. |
| Payment tabs | Returns the **Payment tabs** field. |
| Workflow | Returns the **Workflow** field. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |
| Status | The current status of the envelope. |
| Email subject | The subject line of the email sent to all recipients. |
| Signing location | The physical location where signing takes place. Valid values are `InPerson` and `Online`. The default value is `Online`. |
| Purge state | The current purge state of the envelope's documents. |
| Envelope location | Reserved for Docusign. |
| Any signer | Deprecated. This feature has been replaced by signing groups. |
| Voided reason | The reason the envelope was voided. |
| Expire enabled | Indicates whether the envelope is set to expire after a set number of days. |
| Expire after | The number of days before the envelope expires. |
| Allow markup | Indicates whether the Document Markup feature is enabled. |
| Envelope ID stamping | Indicates whether the envelope ID is stamped on the documents. |
| Auto navigation | Indicates whether auto-navigation is set for the recipient. |
| Is signature provider envelope | Indicates whether the envelope uses a third-party signature provider. |
| Is ticket related envelope | Indicates whether the envelope is associated with a support ticket. |
| Created date time | The date and time the envelope was created. |
| Sent date time | The date and time the envelope was sent. |
| Delivered date time | The date and time the envelope was delivered to recipients. |
| Completed date time | The date and time the envelope was completed. |
| Last modified date time | The date and time the envelope was last modified. |
| Status changed date time | The date and time the envelope's status last changed. |
| Envelope URI | The URI for retrieving the envelope. |
| Documents URI | The URI for retrieving the envelope's documents. |
| Recipients URI | The URI for retrieving the envelope's recipients. |
| Attachments URI | The URI for retrieving the envelope's attachments. |
| Custom fields URI | The URI for retrieving the envelope's custom fields. |
| Notification URI | The URI for retrieving the envelope's notification settings. |
| Templates URI | The URI for retrieving the envelope's templates. |
| Certificate URI | The URI for retrieving the envelope's certificate of completion. |
| Documents combined URI | The URI for retrieving all documents combined into a single PDF. |
| Sender | Information about the user who sent the envelope. |
| User ID (Sender) | The ID of the user who sent the envelope. |
| User name (Sender) | The name of the user who sent the envelope. |
| Email (Sender) | The email address of the user who sent the envelope. |
| Account ID (Sender) | The ID of the account that sent the envelope. |
| IP address (Sender) | The IP address of the user who sent the envelope. |
| Email blurb | The email message body sent to all recipients. |
| Initial sent date time | The date and time the envelope was first sent. |
| Expire date time | The date and time the envelope expires. |
| Voided date time | The date and time the envelope was voided. |
| Envelope metadata | Metadata describing the correction and notary options for the envelope. |
| Allow advanced correct (Envelope metadata) | Indicates whether advanced correction is allowed. |
| Allow correct (Envelope metadata) | Indicates whether correction is allowed. |
| Enable sign with notary (Envelope metadata) | Indicates whether signing with a notary is enabled. |
| Enable wet sign | Indicates whether the signer can print the document and sign it on paper. |
| Allow reassign | Indicates whether the recipient can redirect the envelope to a more appropriate recipient. |
| Is 21 CFR Part 11 | Indicates whether the envelope complies with 21 CFR Part 11 (FDA electronic records). |
| Signer can sign on mobile | Indicates whether signers can sign on a mobile device. |
| U sig state | Reserved for Docusign. |
| Has form data changed | Indicates whether the form data in the envelope has changed. |
| Allow view history | Indicates whether recipients can view the history of the envelope. |
| Is dynamic envelope | Indicates whether the envelope is a dynamic envelope. |
| Burn default tab data | Indicates whether default tab data is burned into the documents. |
| Recipients | Information about the envelope's recipients. |
| Current routing order (Recipients) | The routing order currently being processed. |
| Recipient count (Recipients) | The total number of recipients on the envelope. |
| Signers (Recipients) | Recipients who must sign the documents. |
| In person signers (Recipients) | Recipients who sign in person, hosted by another user. |
| Witnesses (Recipients) | Recipients who witness the signing. |
| Carbon copies (Recipients) | Recipients who receive a copy of the completed documents but do not sign. |
| Certified deliveries (Recipients) | Recipients who must receive the documents but do not sign. |
| Agents (Recipients) | Recipients who can add name and email information for other recipients. |
| Editors (Recipients) | Recipients who can edit the envelope's recipients and documents. |
| Intermediaries (Recipients) | Recipients who can add recipients after themselves in the routing order. |
| Seals (Recipients) | Electronic seal recipients applied to the documents. |
| Notaries (Recipients) | Recipients who act as a notary. |
| Custom fields | The custom fields defined on the envelope. The **Custom fields** field is only available when you select **Custom fields** in the **Include** input field. Refer to [Custom fields](#custom-fields) for more information. |
| Envelope documents | The documents in the envelope. The **Envelope documents** field is only available when you select **Documents** or **Prefill tabs** in the **Include** input field. Refer to [Envelope documents](#envelope-documents) for more information. |
| Envelope attachments | The attachments in the envelope. The **Envelope attachments** field is only available when you select **Attachments** in the **Include** input field. |
| Folders | The folders that contain the envelope. The **Folders** field is only available when you select **Folders** in the **Include** input field. Refer to [Folders](#folders) for more information. |
| Power forms | The PowerForms associated with the envelope. The **Power forms** field is only available when you select **PowerForm** in the **Include** input field. |
| Payment tabs | The payment tabs in the envelope. The **Payment tabs** field is only available when you select **Payment tabs** in the **Include** input field. |
| Notification | The reminder and expiration settings for the envelope. The **Notification** field is only available when you select **Extensions** in the **Include** input field. Refer to [Notification](#notification) for more information. |
| Workflow | The workflow steps defined on the envelope. The **Workflow** field is only available when you select **Workflow** in the **Include** input field. Refer to [Workflow](#workflow) for more information. |

The **Recipients** field groups recipients by type. Each type listed above contains the fields described in [Recipient fields](#recipient-fields).

### Custom fields

The **Custom fields** field contains the custom fields defined on the envelope. Text custom fields and list custom fields share the following fields. List custom fields also include **List items**.

| Output field | Description |
| --- | --- |
| Field ID | The ID of the custom field. |
| Name | The name of the custom field. |
| Show | Indicates whether the custom field is displayed in the Docusign UI. |
| Required | Indicates whether the custom field is required. |
| Value | The value of the custom field. |
| List items (List custom fields) | The available values for a list custom field. |

### Envelope documents

The **Envelope documents** field lists the documents in the envelope. Each document contains the following fields.

| Output field | Description |
| --- | --- |
| Document ID | The ID of the document. |
| Document ID GUID | The globally unique identifier (GUID) of the document. |
| URI | The URI for retrieving the document. |
| Name | The name of the document. |
| Type | The type of the document. |
| Order | The order in which the document appears in the envelope. |
| Pages | The pages in the document. |
| Display | How the document is displayed to recipients. |
| Include in download | Indicates whether the document is included when documents are downloaded. |
| Signer must acknowledge | Specifies how the recipient must acknowledge the document. |
| Authoritative copy | Indicates whether the document is marked as an authoritative copy. |
| Template required | Indicates whether the document is required when the envelope is created from a template. |
| Tabs | The prefill tabs defined on the document. The **Tabs** field is only available when you select **Prefill tabs** in the **Include** input field. |

### Folders

The **Folders** field lists the folders that contain the envelope. Each folder contains the following fields.

| Output field | Description |
| --- | --- |
| Folder ID | The ID of the folder. |
| Name | The name of the folder. |
| Type | The type of the folder. |
| URI | The URI for retrieving the folder. |
| Owner | Information about the user who owns the folder. |

### Notification

The **Notification** field contains the reminder and expiration settings for the envelope. Docusign returns these fields only when the envelope has the settings.

| Output field | Description |
| --- | --- |
| Use account defaults | Indicates whether the envelope uses the account's default notification settings. |
| Reminders | The reminder settings. |
| Reminder enabled (Reminders) | Indicates whether reminders are enabled. |
| Reminder delay (Reminders) | The number of days before the first reminder is sent. |
| Reminder frequency (Reminders) | The number of days between reminders. |
| Expirations | The expiration settings. |
| Expire enabled (Expirations) | Indicates whether the envelope expires. |
| Expire after (Expirations) | The number of days before the envelope expires. |
| Expire warn (Expirations) | The number of days before expiration that a warning is sent. |

### Workflow

The **Workflow** field contains the envelope-level workflow. Docusign returns this field only when the envelope has a workflow. Recipient identity verification workflows are separate.

| Output field | Description |
| --- | --- |
| Workflow status | The status of the workflow. |
| Workflow steps | The steps in the workflow. |
| Action (Workflow steps) | The action the step performs. |
| Status (Workflow steps) | The status of the step. |
| Trigger on item (Workflow steps) | The item that triggers the step. |
| Item ID (Workflow steps) | The ID of the item the step applies to. |
| Scheduled date (Workflow steps) | The date and time the step is scheduled to run. |
| Completed date (Workflow steps) | The date and time the step completed. |

### Recipient fields

Each recipient type (such as **Signers** and **Witnesses**) contains the following fields.

| Output field | Description |
| --- | --- |
| Recipient ID | The ID of the recipient within the envelope. |
| Recipient ID GUID | The globally unique identifier (GUID) for the recipient. |
| Recipient type | The type of recipient (for example, signer or carbon copy). |
| Email | The recipient's email address. |
| Name | The recipient's name. |
| Status | The recipient's current status. |
| Role name | The role assigned to the recipient. |
| Routing order | The order in which the recipient receives and acts on the envelope. |
| User ID | The ID of the Docusign user associated with the recipient. |
| Client user ID | The identifier used for an embedded (captive) recipient. |
| Delivery method | The method used to deliver the envelope to the recipient. |
| Note | A private note displayed to the recipient. |
| Sent date time | The date and time the envelope was sent to the recipient. |
| Delivered date time | The date and time the recipient viewed the envelope. |
| Signed date time | The date and time the recipient signed. |
| Completed date time | The date and time the recipient completed their action. |
| Require ID lookup | Indicates whether the recipient must be verified through ID lookup. |
| Is bulk recipient | Indicates whether the recipient is part of a bulk send. Applies to signers only. |
| Recipient supplies tabs | Indicates whether the recipient supplies their own tabs. Applies to signers only. |
| Require upload signature | Indicates whether the recipient must upload a signature. Applies to signers only. |
| Completed count | The number of times the recipient has completed signing. |
| Total tab count | The total number of tabs assigned to the recipient. |
| Creation reason | The reason the recipient was added to the envelope. |
| Tabs | The tabs assigned to the recipient, grouped by type. The **Tabs** field is only available when you select **Tabs** in the **Include** input field. Refer to [Tab fields](#tab-fields) for more information. |

#### Tab fields

The **Tabs** field groups a recipient's tabs by type. Each tab contains the following fields, regardless of its type.

Tab types include:

- Sign here tabs
- Initial here tabs
- Date signed tabs
- Full name tabs
- First name tabs
- Last name tabs
- Email address tabs
- Title tabs
- Company tabs
- Email tabs
- SSN tabs
- ZIP tabs
- Text tabs
- Number tabs
- Date tabs
- Checkbox tabs
- List tabs
- Radio group tabs
- Note tabs

| Output field | Description |
| --- | --- |
| Tab ID | The unique identifier for the tab. |
| Tab label | The label assigned to the tab. |
| Name | The name of the tab. |
| Tab type | The type of tab. |
| Document ID | The ID of the document the tab appears on. |
| Recipient ID | The ID of the recipient the tab is assigned to. |
| Page number | The page number where the tab appears. |
| X position | The horizontal position of the tab on the page, in pixels. |
| Y position | The vertical position of the tab on the page, in pixels. |
| Status | The tab's current status. |
| Locked | Indicates whether the tab is locked from editing. |
| Anchor string | The text string the tab is anchored to. |
| Anchor X offset | The horizontal offset from the anchor string, in pixels. |
| Anchor Y offset | The vertical offset from the anchor string, in pixels. |
| Value | The value entered in or selected for the tab. |
| Required | Indicates whether the recipient must complete the tab. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-get-envelope-recipients.md
description: >-
  The Get envelope recipients action in the Docusign connector lets you retrieve
  the list of recipients for a given envelope.
---

# Docusign - Get envelope recipients action

The **Get envelope recipients** action retrieves the list of recipients in Docusign for a given envelope, including signers, carbon copy recipients, and more. Refer to the Docusign [EnvelopeRecipients: list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/list/) API reference for more information.

## Input

| Input field | Description |
| --- | --- |
| Envelope ID | Enter the ID of the Docusign [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/). |
| Include tabs | Enable to include tab data for each recipient in the response. Refer to [Tab fields](/en/connectors/docusign/action-get-envelope#tab-fields) for the fields each tab contains. |
| Include extended | Enable to include extended recipient properties in the response. Refer to [Additional recipient output](#additional-recipient-output) for more information. |
| Include metadata | Enable to include metadata for each recipient in the response. Refer to [Additional recipient output](#additional-recipient-output) for more information. |

## Output

Docusign groups recipients by [recipient type](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/), and each type shares a common set of fields plus its own type-specific fields. Refer to the Docusign [EnvelopeRecipients resource](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/) documentation for the full field reference of each recipient type.

| Output field | Description |
| --- | --- |
| Current routing order | The routing order value of the current recipient, indicating the envelope was sent to this recipient but they haven't yet completed their action. |
| Recipient count | The number of recipients on the envelope. |
| Signers | The list of recipients who must sign, initial, date, or add information to the documents. |
| In person signers | The list of recipients who sign in person, with a Docusign user acting as a signing host in the same physical location as the signer. |
| Witnesses | The list of recipients who witness another recipient's signature. |
| Carbon copies | The list of recipients who receive a copy of the envelope but don't need to sign, initial, date, or add information to the documents. |
| Certified deliveries | The list of recipients who must receive the completed documents for the envelope to be completed, but don't need to sign, initial, date, or add information to the documents. |
| Agents | The list of recipients who can add name and email information for recipients that appear later in the routing order. |
| Editors | The list of recipients with the same management and access rights as the sender, who can edit the envelope, recipients, and tabs for the remaining recipients. |
| Intermediaries | The list of recipients who can optionally add name and email information for recipients at the same or a later point in the routing order. |
| Seals | The list of electronic seal recipients. An electronic seal represents an organization or government entity rather than an individual. |
| Notaries | The list of recipients who notarize another recipient's signature using Docusign eNotary. |
| Notary witnesses | The list of notary witness recipients on the envelope. Each recipient has the same fields as **Witnesses**, including **Witness for**. |
| Verification signers | The list of verification signer recipients on the envelope. Each recipient has the same fields as **Signers**. |
| Verifiers | The list of verifier recipients on the envelope. Each recipient has the same fields as **Signers**. |

### Recipient fields

Each recipient in the preceding arrays is an object that shares a common set of fields, such as **Recipient ID**, **Recipient type**, **Status**, and **Routing order**. These are the same fields documented in [Recipient fields](/en/connectors/docusign/action-get-envelope#recipient-fields) on the **Get envelope** action. The **Tabs** and **Total tab count** fields are only available when you enable **Include tabs**. Each recipient's tabs use the same structure as [Tab fields](/en/connectors/docusign/action-get-envelope#tab-fields). Informational recipient types (**Carbon copies**, **Certified deliveries**, **Agents**, **Editors**, **Intermediaries**, **Seals**, and **Notaries**) return a subset of these fields.

### Type-specific fields

Some recipient types include fields beyond the common set. **In person signers** use the host and signer fields below instead of the common **Email** and **Name** fields.

| Output field | Description |
| --- | --- |
| Is bulk recipient (Signers) | Indicates whether the recipient is part of a bulk send. |
| Recipient supplies tabs (Signers) | Indicates whether the recipient supplies their own tabs. |
| Require upload signature (Signers) | Indicates whether the recipient must upload a signature. |
| Host email (In person signers) | The email address of the Docusign user hosting the in-person signing session. |
| Host name (In person signers) | The name of the Docusign user hosting the in-person signing session. |
| Signer email (In person signers) | The email address of the in-person signer. |
| Signer name (In person signers) | The name of the in-person signer. |
| Witness for (Witnesses, Notary witnesses) | The recipient ID of the recipient the witness is witnessing for. |
| Witness for GUID (Witnesses, Notary witnesses) | The globally unique identifier (GUID) of the recipient the witness is witnessing for. |

### Additional recipient output

Each option you enable adds fields to each recipient. The output includes only the fields for the options you enable.

| Input field | Output field added | Description |
| --- | --- | --- |
| Include tabs | Tabs, Total tab count | The tabs assigned to the recipient and the number of tabs. |
| Include extended | Email notification | The custom email settings for the recipient. Contains **Email subject**, **Email body**, and **Supported language**. |
| Include extended | Identity verification | The identity verification workflow applied to the recipient. Contains **Workflow ID** and **Workflow label**. |
| Include extended | Phone authentication | The phone authentication settings for the recipient. Contains **Recip may provide number** and **Sender provided numbers**. |
| Include extended | Sms authentication | The phone numbers the recipient can use for SMS authentication. Contains **Sender provided numbers**. |
| Include extended | Other recipient properties | The **Access code**, **Declined reason**, **Declined date time**, **Fax number**, **ID check configuration name**, **Suppress emails**, **Sign in each location**, **Agent can edit email**, **Agent can edit name**, and **Signing group ID** fields. |
| Include metadata | Metadata for each recipient field | Indicates whether the field can be edited. Each metadata object contains **Rights**, and appears next to the field it describes. For example, **Email metadata** appears next to **Email**. Applies to the fields in the preceding rows, such as **Workflow ID metadata** and **Sender provided numbers metadata**. |

Each field appears only when the recipient has a value for it.

---
