---
url: 'https://docs.workato.com/en/connectors/pubsub/pubsub-actions.md'
description: >-
  The publish message action in the Workato Event streams connector lets you
  publish one message at a time to a topic that other recipes can consume.
---

# Using the publish message action

The publish action enables you to publish messages to a specific topic in Workato. Other recipes can then pick up all messages published to that topic, using Event streams triggers.

One action publishes one message at a time. The [topic schema](/en/connectors/pubsub/pubsub-schema-config) defines the action input fields available here.

![Publish message action configuration](/assets/publish-message-action.BEYiRIde.png)_Select the topic and fill in the input fields to configure the publish message action_

> **PAYLOAD SIZE LIMITATIONS**
> 
> Payloads in the [Event streams connector](/en/connectors/pubsub) are subject to the following quotas:
> 
> | Description | Quota |
> | --- | --- |
> | Maximum size of a single published message | 10 MB |

---
