---
url: 'https://docs.workato.com/en/connectors/docusign/action-create-template.md'
description: The Create template action creates a new template in your Docusign account.
---

# Docusign - Create template action

The **Create template** action creates a new template in your Docusign account.

Refer to the Docusign [Templates:create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/create/) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| Name | Enter the name of the template. |
| Description | Enter a description of the template. |
| Shared | Select **Yes** to share the template with other members of your Docusign account. |
| Email subject | Enter the subject line of the email sent to all recipients. The subject line is limited to 100 characters, including merged fields. |
| Email blurb | Enter the message body of the email sent to all recipients. |
| Folder ID | Enter the ID of the folder to save the template in. |
| Folder name | Enter the name of the folder to save the template in. |
| Documents | Add the documents to include in the template. Each document is base64-encoded and sent in a single request. Docusign allows up to 32 MB per document through the API, but base64 encoding adds about 33% overhead. Keep the original file size well under that limit (around 20-25 MB) to stay within the overall request size limit. |
| Documents source list (Documents) | Provide a list datapill containing multiple documents. |
| File URL (Documents) | Enter the URL of the file, including the file extension. For example, `https://test.io/wp-content/uploads/2019/02/testIO-logo-rgb-2.png`. |
| Roles | Define the recipient roles on the template. Leave the name and email blank to create placeholders that are filled in when the template is used. |
| Roles source list (Roles) | Provide a list datapill containing multiple roles. |
| Role name (Roles) | Enter the role name for this recipient. For example, `Signer 1`. |
| Name (Roles) | Enter the full legal name of the recipient. |
| Email (Roles) | Enter the email address of the recipient. |
| Routing order (Roles) | Enter the signing order of the recipient. For example, `1` for the first signer and `2` for the second signer. |
| Recipient type (Roles) | Select the type of recipient. Defaults to **Signer**. In-person signer and witness aren't supported. |
| Custom fields | Define new custom fields on the template. |
| Custom fields source list (Custom fields) | Provide a list datapill containing multiple custom fields. |
| Type (Custom fields) | Select the type of custom field. Defaults to **Text**. Select **List** to provide selectable list items. |
| Name (Custom fields) | Enter the name of the custom field. |
| Value (Custom fields) | Enter the default value of the custom field. The value can be up to 100 characters. |
| Required (Custom fields) | Select **Yes** to require senders to enter or select a value for the custom field before they send the envelope. |
| Show (Custom fields) | Select **Yes** to display the custom field in the **Envelope Custom Fields** section when a user creates or sends an envelope. |
| List items (Custom fields) | Enter the selectable values for the custom field. Each value can be up to 100 characters. Applies only when **Type** is **List**. |
| Advanced (JSON) | Enter raw JSON to merge into the request body for fields not exposed above. For example, `notarySections` and `envelopeCustomMetadata`. Fields set above take priority over this field on conflict. |

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

---
