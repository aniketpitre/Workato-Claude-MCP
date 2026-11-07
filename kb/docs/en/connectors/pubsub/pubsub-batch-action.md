---
url: 'https://docs.workato.com/en/connectors/pubsub/pubsub-batch-action.md'
description: >-
  The batch publish action in the Workato Event streams connector lets you
  publish up to 100 messages at a time to a topic other recipes can consume.
---

# Workato Event Streams - Batch publish message action

The batch publish action enables you to publish a batch of messages to a specific topic in Workato. Other recipes can then pick up all messages published to that topic, using Event streams triggers.

One action can publish up to 100 messages at a time. The [topic schema](/en/connectors/pubsub/pubsub-schema-config) defines the action input fields available here.

![Publish message action configuration](/assets/publish-batch-messages-action.PyI3-ke1.png)_Select the topic and fill in the input fields to configure the publish message action_

Note that you need to use a list of messages as a datapill.

> **PAYLOAD SIZE LIMITATIONS**
> 
> Payloads in the [Event streams connector](/en/connectors/pubsub) are subject to the following quotas:
> 
> | Description | Quota |
> | --- | --- |
> | Maximum size of a single published message | 10 MB |

---
