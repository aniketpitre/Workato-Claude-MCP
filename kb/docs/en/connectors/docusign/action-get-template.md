---
url: 'https://docs.workato.com/en/connectors/docusign/action-get-template.md'
description: >-
  The Get template action in the Docusign connector lets you retrieve the
  details of a single template by its ID.
---

# Docusign - Get template action

The **Get template** action retrieves the details of a single template in Docusign. Refer to the Docusign [Templates: get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/get/) API reference for the full field reference.

## Input

| Input field | Description |
| --- | --- |
| Template | Select the template to retrieve. |
| Include | Select the additional information to return for the template. Refer to [Include options](#include-options) for the available options. Documents are included automatically. Use a comma-separated list to enter values manually. For example, `powerforms,favorite_template_status`. |

### Include options

The **Include** input field controls which additional information the action returns for the template.

| Include option | Description |
| --- | --- |
| PowerForms | Returns the **Power forms** field. |
| Tabs | Returns the **Tabs** field for each recipient in the **Recipients** field. Refer to [Tab fields](/en/connectors/docusign/action-get-envelope#tab-fields) for the fields each tab contains. |
| Documents | Returns the **Documents** field. This option is automatically applied. |
| Favorite template status | Returns the **Favorited by me** field. |

## Output

| Output field | Description |
| --- | --- |
| Template ID | The unique identifier of the template. |
| Name | The name of the template. |
| Description | The description of the template. |
| Status | The current status of the template. |
| Email subject | The subject line of the email sent to all recipients. |
| Email blurb | The email message body sent to all recipients. |
| Signing location | The physical location where signing takes place. Valid values are `InPerson` and `Online`. The default value is `Online`. |
| Page count | The number of document pages in the template. |
| Shared | Indicates whether the template is shared with other users. |
| Password protected | Indicates whether the template is password protected. |
| Authoritative copy | Indicates whether the documents are marked as authoritative copies. |
| Enforce signer visibility | Indicates whether document visibility settings are enforced for the envelope. |
| Enable wet sign | Indicates whether the signer can print the document and sign it on paper. |
| Allow markup | Indicates whether the Document Markup feature is enabled. |
| Allow reassign | Indicates whether the recipient can redirect the envelope to a more appropriate recipient. |
| Disable responsive document | Indicates whether responsive documents are disabled. |
| Auto match | Indicates whether the template is included in auto-matching. |
| Auto match specified by user | Indicates whether the template has been explicitly included in or excluded from auto-matching. |
| Any signer | Deprecated. This feature has been replaced by signing groups. |
| Envelope location | Reserved for Docusign. |
| Folder ID | The ID of the folder that contains the template. |
| Folder name | The name of the folder that contains the template. |
| Folder ids | The IDs of the folders where the template exists, either directly or through template sharing. |
| Value (Folder ids) | A folder ID. |
| URI | The URI for retrieving the template. |
| Created | The date and time the template was created. |
| Last modified | The date and time the template was last modified. |
| Last used | The date and time the template was last used. |
| Owner | Information about the user who owns the template. |
| User ID (Owner) | The ID of the user who owns the template. |
| User name (Owner) | The name of the user who owns the template. |
| Email (Owner) | The email address of the user who owns the template. |
| Account ID (Owner) | The ID of the account that owns the template. |
| Last modified by | Information about the user who last modified the template. |
| User name (Last modified by) | The name of the user who last modified the template. |
| User ID (Last modified by) | The ID of the user who last modified the template. |
| Email (Last modified by) | The email address of the user who last modified the template. |
| URI (Last modified by) | The URI for retrieving the user who last modified the template. |
| Documents | The documents in the template. See [Documents](#documents). |
| Notification | The reminder and expiration settings for the template. See [Notification](#notification). |
| Custom fields | The custom fields defined on the template. See [Custom fields](#custom-fields). |
| Envelope ID stamping | Indicates whether the envelope ID is stamped on the documents. |
| Auto navigation | Indicates whether auto-navigation is set for the recipient. |
| U sig state | Reserved for Docusign. |
| Recipients | The recipients defined on the template. See [Recipients](#recipients). |
| Recipient roles | The recipient roles defined on the template. |
| Role name (Recipient roles) | The name of the role. |
| Recipient type (Recipient roles) | The type of recipient for the role. |
| Prefill tabs | The prefill tabs defined on the template. See [Tab fields](#tab-fields). |
| Power forms | The PowerForms created from the template. The **Power forms** field is only available when you select **PowerForms** in the **Include** input field. See [Power forms](#power-forms). |
| Favorited by me | Indicates whether the connected user has marked the template as a favorite. The **Favorited by me** field is only available when you select **Favorite template status** in the **Include** input field. |

### Documents

The **Documents** field lists the documents included in the template. Each document contains the following fields.

| Output field | Description |
| --- | --- |
| Document ID | The ID of the document. |
| URI | The URI for retrieving the document. |
| Name | The name of the document. |
| Order | The order in which the document appears in the template. |
| Pages | The number of pages in the document. |
| Display | How the document is displayed to recipients. |
| Include in download | Indicates whether the document is included when documents are downloaded. |
| Signer must acknowledge | Specifies how the recipient must acknowledge the document. |
| Template locked | Indicates whether the document is locked in the template. |
| Template required | Indicates whether the document is required in the template. |
| Tabs | The tabs defined on the document, grouped by type. Refer to [Tab fields](#tab-fields) for more information. |

### Notification

The **Notification** field contains the reminder and expiration settings applied to envelopes created from the template.

| Output field | Description |
| --- | --- |
| Reminders | The reminder settings. |
| Reminder enabled (Reminders) | Indicates whether reminders are enabled. |
| Reminder delay (Reminders) | The number of days before the first reminder is sent. |
| Reminder frequency (Reminders) | The number of days between reminders. |
| Expirations | The expiration settings. |
| Expire enabled (Expirations) | Indicates whether the envelope expires. |
| Expire after (Expirations) | The number of days before the envelope expires. |
| Expire warn (Expirations) | The number of days before expiration that a warning is sent. |

### Custom fields

The **Custom fields** field contains the custom fields defined on the template. Text custom fields and list custom fields share the following fields. List custom fields also include **List items**.

| Output field | Description |
| --- | --- |
| Field ID | The ID of the custom field. |
| Name | The name of the custom field. |
| Show | Indicates whether the custom field is displayed in the Docusign UI. |
| Required | Indicates whether the custom field is required. |
| Value | The value of the custom field. |
| List items (List custom fields) | The available values for a list custom field. |

### Power forms

The **Power forms** field lists the PowerForms created from the template. Each PowerForm contains the following fields.

| Output field | Description |
| --- | --- |
| Power form ID | The ID of the PowerForm. |
| Name | The name of the PowerForm. |
| URI | The URI for retrieving the PowerForm. |
| PowerForm URL | The URL recipients use to start signing from the PowerForm. |
| Sender name | The name of the sender. |
| Sender user ID | The ID of the sender. |
| Template ID | The ID of the template the PowerForm uses. |
| Template name | The name of the template the PowerForm uses. |
| Email subject | The subject line of the email sent to recipients. |
| Email body | The email message body sent to recipients. |
| Instructions | The instructions shown to recipients. |
| Signing mode | The signing mode of the PowerForm. |
| Is active | Indicates whether the PowerForm is active. |
| Limit use interval enabled | Indicates whether the PowerForm limits how often it can be used within an interval. |
| Limit use interval units | The unit of time for the use interval. |
| Max use enabled | Indicates whether the PowerForm limits the total number of times it can be used. |
| Times used | The number of times the PowerForm has been used. |
| Created date time | The date and time the PowerForm was created. |
| Last used | The date and time the PowerForm was last used. |

### Recipients

The **Recipients** field groups recipients by type (such as **Signers**, **In person signers**, and **Witnesses**), the same structure used by the **Get envelope** action. Refer to [Recipient fields](/en/connectors/docusign/action-get-envelope#recipient-fields) for the fields each recipient contains.

### Tab fields

Prefill tabs let senders add read-only values to a template. They appear at the template level and under each document's **Tabs**, grouped by type: Text tabs, Number tabs, Date tabs, Checkbox tabs, and Radio group tabs. Each prefill tab contains the following fields.

| Output field | Description |
| --- | --- |
| Tab ID | The unique identifier for the tab. |
| Tab label | The label assigned to the tab. |
| Tab type | The type of tab. |
| Document ID | The ID of the document the tab appears on. |
| Page number | The page number where the tab appears. |
| Required | Indicates whether the recipient must complete the tab. |
| Validation pattern | A regular expression used to validate the tab's value. |
| Validation message | The message shown when the tab's value fails validation. |
| Max length | The maximum number of characters allowed in the tab. |
| Selected | Indicates whether the tab is selected. |
| Radios | The radio buttons in a radio group tab. |
| Group name | The name of the group the tab belongs to. |

Document tabs can also be organized into tab groups. Each tab group has a Tab ID, Tab type, Group label, Group rule, Page number, and Status.

---

---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-get-template-document-tabs.md
description: >-
  The Get template document tabs action retrieves the tabs configured on the
  specified document within a Docusign template.
---

# Docusign - Get template document tabs action

The **Get template document tabs** action retrieves the tabs configured on the specified document within a Docusign template.

Refer to the Docusign [TemplateDocumentTabs:get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/get/) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| Template | Select the template that contains the document. |
| Document ID | Enter the unique identifier of the document within the template. This value is available in the Document ID field returned by the [Get template](/en/connectors/docusign/action-get-template) action. |

## Output

The action returns tab collections grouped by tab type. Each tab datapill contains the configuration and placement details for an individual tab. Available nested fields vary by tab type.

| Output field | Description |
| --- | --- |
| Sign here tabs | The signature tabs configured on the document. |
| Initial here tabs | The initials tabs configured on the document. |
| Date signed tabs | The tabs that display the date when a recipient signs. |
| Full name tabs | The tabs that display a recipient's full name. |
| First name tabs | The tabs that display a recipient's first name. |
| Last name tabs | The tabs that display a recipient's last name. |
| Email address tabs | The tabs that display a recipient's email address. |
| Title tabs | The tabs that display a recipient's title. |
| Company tabs | The tabs that display a recipient's company name. |
| Email tabs | The email-entry tabs configured on the document. |
| SSN tabs | The Social Security number-entry tabs configured on the document. |
| ZIP tabs | The ZIP or postal-code entry tabs configured on the document. |
| Text tabs | The text-entry tabs configured on the document. |
| Number tabs | The numeric-entry tabs configured on the document. |
| Date tabs | The date-entry tabs configured on the document. |
| Checkbox tabs | The checkbox tabs configured on the document. |
| List tabs | The drop-down list tabs configured on the document. |
| Radio group tabs | The radio-button group tabs configured on the document. |
| Note tabs | The note tabs configured on the document. |
| Prefill tabs | The sender-prefill tabs grouped by tab type. |

---

---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-list-documents-in-envelope.md
description: >-
  The List documents in envelope (batch) action in the Docusign connector lets
  you retrieve a list of all documents contained within a given envelope.
---

# Docusign - List documents in envelope (batch) action

The **List documents in envelope (batch)** action provides a list of documents contained within the envelope in Docusign.

## Input

| Input field | Description |
| --- | --- |
| Envelope ID | Enter the GUID value that identifies a Docusign [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/). Docusign automatically generates this value when the envelope is created. |

## Output

| Output field | Description |
| --- | --- |
| Envelope ID | The ID assigned to the envelope for tracking and managing the document lifecycle. |
| Envelope documents | The documents contained in the envelope. |
| Document ID (Envelope documents) | The ID of the envelope container for the document. |
| Name (Envelope documents) | The name of the document. |
| Type (Envelope documents) | The type of document. |
| URI (Envelope documents) | The URI of the document. |
| Order (Envelope documents) | The order of the document. |
| Pages (Envelope documents) | The number of pages in the document. |
| Attachment tab ID (Envelope documents) | The ID of the attachment tab. |
| Contains pdf form fields (Envelope documents) | Indicates whether the document contains PDF form fields. |
| Available document types (Envelope documents) | The type of document and whether it is the default. |
| Document fields (Envelope documents) | The document's fields, including name, value, and error details (code and message). |

---
