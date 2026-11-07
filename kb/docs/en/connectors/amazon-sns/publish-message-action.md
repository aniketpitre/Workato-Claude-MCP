---
url: 'https://docs.workato.com/en/connectors/amazon-sns/publish-message-action.md'
description: The Publish message action publishes a message to a specified topic.
---

# Amazon SNS - Publish message action

The **Publish message** action publishes a message to a specified topic.

## Input

| Input field | Description |
| --- | --- |
| Topic Name | Use the drop-down menu to select a message topic. |
| Subject | Enter a subject tile for the message. |
| Message format | Select the message format. Select **JSON** to send different messages for each transport protocol. Select **Raw** to send the same message to all protocols. Refer to the [Amazon documentation](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) for more information. |
| Message | Provide the message content. For **Raw**, enter a single message for all protocols. For **JSON**, define the message schema and enter the message content. Refer to the [Configure message schema](#configure-message-schema) section for more information. |
| Message attributes schema | Enter values to define your message attribute schema. Enter a **Name**, **Type**, and **Value** for each attribute. Refer to the [message attributes](https://docs.aws.amazon.com/sns/latest/dg/sns-message-attributes.html) section for more information. |

### Configure message schema

Define the message schema to send different messages for each transport protocol.

Refer to the [Amazon documentation](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html#API_Publish_RequestParameters) for more information.

**Define message schema with JSON snippet:**

![Define schema](/assets/define-message-schema.XPo6ksju.png)_Define message schema with JSON snippet_

**Resulting message schema input field:**

![Message schema input field](/assets/message-schema-input-box.DATuJAVi.png)_Message schema input field_

## Output

| Output field | Description |
| --- | --- |
| Message ID | The message ID. |

---
