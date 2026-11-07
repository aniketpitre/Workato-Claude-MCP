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
