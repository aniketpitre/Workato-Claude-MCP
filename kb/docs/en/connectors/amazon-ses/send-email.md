---
url: 'https://docs.workato.com/en/connectors/amazon-ses/send-email.md'
description: The Send email action sends an email by using Amazon SES.
---

# Amazon SES - Send email action

The **Send email** action sends an email through Amazon SES. Fill in any relevant input fields related to the email to use the action.

* * *

## Input

| Input field | Description |
| --- | --- |
| Content type **Required** | Select the content type of the email you plan to send. You can send a [simple email](#simple-email-input) or [template email](#template-email-input) message. |

* * *

### Simple email input

| Input field | Description |
| --- | --- |
| Subject | Type the subject line of the email. |
| From | Type the email address from which the email is sent. This email address must be verified with SES before you can use it. Refer to the [verification process](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html) for more information. |
| To | Add the email addresses to send the email to. |
| Text Data | Type the message body. This content displays if the email client does not support HTML. |
| HTML Data | Type any data with HTML content. This content displays in email clients that support HTML. HTML messages can include formatted text, hyperlinks, and more. |
| BCC | Type BCC email addresses. |
| CC | Type CC email addresses here. |
| Tags | Type tags to identify a specific email. Tags correspond to characteristics of the email that you define, and they can be published to email sending events. |
| Feedback forwarding email address | Type the email address to forward any bounce or complaint notifications to. Refer to [feedback monitoring](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity-using-notifications.html) for more information. |
| From email address identity arn | Type the ARN of the email address the email is sent from. This adds authorization policies to the emails. Refer to [authorization policies](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html) for more information. |
| Feedback forwarding email address identity arn | Add the ARN of the email address to forward feedback to. This adds authorization policies to the emails. Click here to know more about authorization policies. |
| List management options | Associate an email with a topic, so that contact can unsubscribe from the same. Provide both the contact list name and associated topic name |
| Reply to addresses | Type the email address that replies from recipients are sent to. |
| Configuration Set | Add the name of the configuration set to use when sending the email. Configuration sets are groups of rules that you can apply to the emails you send using Amazon SES. Refer to [set up and use configuration set](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html) for more information. |

### Template email input

| Input field | Description |
| --- | --- |
| Subject | Type the subject line of the email. |
| From | Type the email address from which the email is being sent. This email address must be verified with SES before you can use it to send an email. Refer to the [verification process](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html) for more information. |
| To | Add the email addresses to send the emails to. |
| Template | Select the template name from the list. To create templates use the **Create object** action. Refer to [Amazon SES email templates](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html) for more information. |
| Template Data | Type values for template data that needs to be customized. You can enter customized values. |
| BCC | Add BCC email addresses. |
| CC | Add CC email addresses. |
| Tags | Type tags to identify a specific sent email. Tags correspond to characteristics of the email that you define, and they can be published to email sending events. |
| Feedback forwarding email address | Type an email that any bounce or complaint notifications are forwarded to. Refer to [feedback monitoring](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity-using-notifications.html) for more information. |
| From email address identity arn | Type the ARN of the email address that the emails are from. This adds authorization policies to the emails. Refer to the [authorization policies](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html) for more information. |
| Feedback forwarding email address identity arn | Type the ARN of the email address to forward feedback to. This adds authorization policies to the emails. |
| List management options | Type an email to associate with a topic, so that contact can unsubscribe. Provide both the contact list name and associated topic name. |
| Reply to addresses | Type an email address to send recipient replies to. |
| Configuration Set | Type the name of the configuration set to use when sending the email. Configuration sets are groups of rules that you can apply to the emails you send using Amazon SES. Learn how to [set up and use configuration set](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html). |

* * *

## Output

| Output field | Description |
| --- | --- |
| Message ID | The message ID. This field indicates that the email was successfully sent. |

---
