---
url: 'https://docs.workato.com/en/connectors/amazon-ses/send-bulk-email.md'
description: >-
  The Send bulk email action sends emails to multiple destinations by using
  Amazon SES.
---

# Amazon SES - Send bulk email action

The **Send bulk email** action sends emails to multiple destinations by using Amazon SES. Select the template of the email you plan to send, then fill in any relevant input fields related to the email.

## Input

| Input field | Description |
| --- | --- |
| From | Type the email address from which the email is sent. This email address must be verified with SES before you can use it to send an email. Refer to the [verification process](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html) for more information. |
| Bulk email entries | Type a list that contains the bulk destinations, customized tags, and email content for each destination. The recommended approach is to store data in a lookup table or in a CSV and fetch the data by using a list to this action. Each entry must provide the destination address(es), such as **To**, **CC**, and **BCC**, replacement tags, and replacement email content. |
| Template | Select the template name from the list. To create templates use create object action. Refer to [Amazon SES email templates](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html) for more information. |
| Default template data | Add default values for the template data. If replacement data is not provided, these values are used instead. |
| Default email tags | Add default tags to identify a specific email that is being sent. If replacement email tags are not provided, these values are used instead. |
| Feedback forwarding email address | Type an email that any bounce or complaint notifications are forwarded to. Refer to [feedback monitoring](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity-using-notifications.html) for more information. |
| From email address identity arn | Add the ARN of the email that emails are sent from. This adds authorization policies to the emails. Refer to [authorization policies](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html) for more information. |
| Feedback forwarding email address identity arn | Add the ARN of the email where feedback is forwarded to. This adds authorization policies to the emails. |
| List management options | Type an email to associate with a topic, so that contact can unsubscribe. Provide both the contact list name and associated topic name. |
| Reply to addresses | Type the email address to send replies from recipients to. |
| Configuration Set | Add the name of the configuration set to use when sending the email. Configuration sets are groups of rules that you can apply to the emails you send using Amazon SES. Learn how to [set up and use configuration set](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html). |

## Output

The output of this action is an array of bulk email entries for each email that was sent. Each entry contains the following fields.

| Output field | Description |
| --- | --- |
| Error | The description of the error if the email was not sent. |
| Message ID | The message ID of the email that was sent. |
| Status | The status of the message. Learn more about possible values for the [Status field](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_BulkEmailEntryResult.html#API_BulkEmailEntryResult_Contents). |

---
