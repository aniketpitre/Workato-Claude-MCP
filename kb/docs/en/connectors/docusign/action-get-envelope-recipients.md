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
