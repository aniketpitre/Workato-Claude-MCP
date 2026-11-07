---
url: 'https://docs.workato.com/en/connectors/docusign/action-list-templates-batch.md'
description: >-
  The List templates (batch) action in the Docusign connector lets you retrieve
  a batch of templates that match the criteria you specify.
---

# Docusign - List templates (batch) action

The **List templates (batch)** action retrieves a batch of templates that match the criteria you specify in Docusign. Refer to the Docusign [Templates: list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/list/) API reference for more information.

## Input

| Input field | Description |
| --- | --- |
| Search text | Filter templates by name. Maximum 48 characters. |
| Order by | Sort templates by this field. Valid values are `Name`, `Modified`, and `Last used`. |
| Order | Sort order direction. Valid values are `Ascending` and `Descending`. |
| From date | Return templates modified on or after this date. |
| To date | Return templates modified up to this date. |
| Shared by me | Enable to return only templates shared by the current user. |
| User filter | Filter templates based on the current user's relationship to them. |
| Count | Specify the maximum number of templates to return per page. |
| Start position | Specify the zero-based index of the result from which to start returning results. |

## Output

| Output field | Description |
| --- | --- |
| Result set size | The number of results returned in the current batch. |
| Total set size | The total number of results available. |
| Start position | The zero-based index of the first result in the batch. |
| End position | The zero-based index of the last result in the batch. |
| Next URI | The URI for retrieving the next batch of results. |
| Previous URI | The URI for retrieving the previous batch of results. |
| Envelope templates | The templates that match the specified criteria. See [Envelope templates](#envelope-templates). |

### Envelope templates

Each template in the batch contains the following summary fields. This is a subset of the fields returned by the [Get template](/en/connectors/docusign/action-get-template) action.

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
