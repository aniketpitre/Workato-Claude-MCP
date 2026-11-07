---
url: 'https://docs.workato.com/en/connectors/gmail/send-email-action.md'
description: The Send email action sends an email from your Gmail account.
---

# Gmail - Send email action

The **Send email** action sends an email from your Gmail account. Each email is processed as an individual job.

## Input

| Input fields | Description |
| --- | --- |
| To | Enter one or more recipient email addresses, separated by a comma. |
| Subject | Enter a subject for the email. |
| Email type | Select the format of the email message. Available options include `Text` and `HTML`. |
| Message | Enter the message to include in the email. Use plain text if the selected email type is `Text`; otherwise, use HTML formatting. |
| From | Enter an alias email ID or name from which you plan to send the email. Configure your alias email ID in Gmail by navigating to **Settings > Accounts > Send email as**. For example, enter `myname@mycompany.com` or select the From datapill from a previous step. |
| Leave this field blank to send an email from the email address connected to Workato. |  |
| Bcc | Enter one or more email addresses to send a blind carbon copy (bcc), separated by a comma. |
| Cc | Enter one or more email addresses to send a carbon copy (cc), separated by a comma. |
| Attachments | Enter attachments for the email. The total attachments size must be less than 25 MB. |

> **SEND EMAIL TO MULTIPLE ADDRESSES USING A LIST DATAPILL**
> 
> Complete the following steps to send an email to multiple email addresses using a list datapill in Gmail, with the [pluck](/en/formulas/array-list-formulas#pluck) and [join](/en/formulas/array-list-formulas#join) list formulas:
> 
> 1. Set the **To** field to **Formula** mode by clicking the formula icon next to the field.
>    
> 2. Drag the list datapill containing the email addresses into the **To** field.
>    
> 3. Type `.pluck("email_address").join(",")` after the list datapill. Use the field's API name to extract the email addresses instead of the label or name displayed in the datapill.
>    
> 
> The `.pluck("email_address")` function extracts the email addresses from each item in the list, and `.join(",")` combines them into a single string separated by commas.

## Output

The output of this action is a datatree that contains information about the sent email. Refer to the [Gmail API documentation](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) for more information.

| Output field | Description |
| --- | --- |
| ID | The unique identifier for the email. |
| Thread ID | The identifier for the email thread. |
| Label IDs | The identifiers for the labels attached to the email. |

---
