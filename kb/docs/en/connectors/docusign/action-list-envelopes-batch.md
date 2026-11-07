---
url: 'https://docs.workato.com/en/connectors/docusign/action-list-envelopes-batch.md'
description: >-
  The List envelopes (batch) action in the Docusign connector lets you retrieve
  a batch of envelopes that match the criteria you specify.
---

# Docusign - List envelopes (batch) action

The **List envelopes (batch)** action retrieves a batch of envelopes that match the criteria you specify in Docusign. Refer to the Docusign [Envelopes: listStatusChanges](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/) API reference for more information.

## Input

| Input field | Description |
| --- | --- |
| From date | Return envelopes with status changes on or after this date. |
| To date | Return envelopes with status changes up to this date. Defaults to now. |
| From/to status | Specify the status type the date range applies to. Defaults to `Changed`. Valid values are `Changed`, `Voided`, `Created`, `Deleted`, `Sent`, `Delivered`, `Signed`, `Completed`, `Declined`, `Timed out`, and `Processing`. |
| Status | Filter envelopes by status. Valid values are `Changed`, `Voided`, `Created`, `Deleted`, `Sent`, `Delivered`, `Signed`, `Completed`, `Declined`, `Timed out`, and `Processing`. |
| Envelope IDs | Enter a comma-separated list of envelope IDs to filter results. |
| Email | Filter envelopes by the email address of a sender or recipient. |
| Order by | Sort envelopes by this field. Valid values are `Action required`, `Created`, `Completed`, `Envelope name`, `Expire`, `Last modified`, `Sent`, `Signer list`, `Status`, `Status changed`, `Subject`, and `User name`. |
| Order | Set the sort order direction. Valid values are `Ascending` and `Descending`. |
| Search text | Filter envelopes by text in the subject line or in recipient names and email addresses. |
| Transaction IDs | Enter a comma-separated list of transaction IDs to filter results. |
| User filter | Filter envelopes based on the user's relationship to them. |
| User ID | Filter envelopes by the ID of the associated user. |
| User name | Filter envelopes by the name of the associated user. |
| Count | Specify the maximum number of envelopes to return per page. |
| Start position | Specify the zero-based index of the result from which to start returning results. |
| Include | Select the additional information to return for each envelope. Refer to [Additional envelope output](#additional-envelope-output) for the available options. Only the summary fields are returned if this field is left blank. Use a comma-separated list to enter values manually. For example, `custom_fields,documents`. |

## Output

| Output field | Description |
| --- | --- |
| Result set size | The number of results returned in the current batch. |
| Total set size | The total number of results available. |
| Start position | The zero-based index of the first result in the batch. |
| End position | The zero-based index of the last result in the batch. |
| Next URI | The URI for retrieving the next batch of results. |
| Previous URI | The URI for retrieving the previous batch of results. |
| Envelopes | The envelopes that match the specified criteria. See [Envelopes](#envelopes). |

### Envelopes

Each envelope in the batch contains the following summary fields. This is a subset of the fields returned by the [Get envelope](/en/connectors/docusign/action-get-envelope) action. You can use the **Include** input field to return more details for each envelope. Refer to [Additional envelope output](#additional-envelope-output) for more information.

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

### Additional envelope output

Each option you select in the **Include** input field adds an object to each envelope in the output. The output includes only the objects for the options you select. This retrieves related envelope data in a single call, replacing separate action calls for each envelope.

| Include option | Output field added | Description |
| --- | --- | --- |
| Custom fields | Custom fields | The custom fields on the envelope. Contains **Text custom fields** and **List custom fields**. |
| Documents | Envelope documents | The documents in the envelope, including each document's pages. |
| Attachments | Envelope attachments | The attachments on the envelope, including each attachment's ID, type, name, label, remote URL, and access control. |
| Extensions | Notification | The envelope's reminder and expiration settings. Contains **Use account defaults**, **Reminders**, and **Expirations**. |
| Folders | Folders | The folders that contain the envelope, including each folder's ID, name, type, URI, and parent folder. |
| Recipients | Recipients | The envelope's recipients, grouped by recipient type. Refer to [Recipient fields](/en/connectors/docusign/action-get-envelope#recipient-fields) in the **Get envelope** action for the fields in each type. |
| Payment tabs | Payment tabs | The payment tabs on the envelope, including each tab's ID, recipient ID, document ID, page number, amount, and currency code. |

---
