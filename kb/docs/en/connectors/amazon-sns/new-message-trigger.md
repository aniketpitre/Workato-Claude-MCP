---
url: 'https://docs.workato.com/en/connectors/amazon-sns/new-message-trigger.md'
description: >-
  The New message trigger monitors a message topic and picks up newly published
  messages.
---

# Amazon SNS - New message trigger

The **New message** trigger monitors a message topic and fetches new messages. Workato processes each message as a new job.

> **429 RESPONSES**
> 
> Amazon SNS treats a `429` (Too Many Requests) response as a successful delivery when using the **New message** trigger. Events that receive a `429` response aren't retried or sent to a Dead Letter Queue (DLQ).
> 
> Throttle message delivery using the SNS topic's delivery policy to align with Workato's [rate limits](/en/troubleshooting/webhook-gateway-limits#webhook-gateway-limits) and prevent event loss. AWS SNS doesn't treat a `429` as a failure and doesn't trigger retries. You can set the `throttlePolicy` to `maxReceivesPerSecond` to control delivery rate. Refer to the [AWS SNS documentation](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html#delivery-policy-maximum-receive-rate) for more information.

## Input

| Input field | Description |
| --- | --- |
| Topic name | Use the drop-down menu to select a message topic. |
| Message format | Choose a message format. The message format determines the trigger output. Refer to the [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) documentation for more information. |
| Message schema | Provide the message schema. This field applies only when you select the JSON message format. |
| Message attributes schema | Enter the message attribute schema, if available. |

## Output

| Output field | Description |
| --- | --- |
| Type | The type of message. |
| Message ID | A unique message ID. |
| Topic ARN | The Amazon Resource Name (ARN) for the topic. |
| Topic name | The topic name. |
| Subject | The subject parameter specified when the notification was published to the topic. |
| Timestamp | The time (GMT) when the subscription confirmation was sent. |
| Signature version | The version of the Amazon SNS signature used. |
| Signature | The encoded signature. |
| Signing cert URL | The URL to the certificate used to sign the message. |
| Message | The message content. The data type varies based on the selected message format. |
| Message attribute | The message attributes. These vary based on the selected message format. |

---
