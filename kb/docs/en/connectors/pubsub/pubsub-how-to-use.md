---
url: 'https://docs.workato.com/en/connectors/pubsub/pubsub-how-to-use.md'
description: >-
  Learn how to use Workato Event streams by creating a topic and building
  recipes that publish and consume messages from it.
---

# How to use Workato Event streams

There is no connection required to use Workato Event streams, as schemas are stored in the Workato account for recipes to interact with.

Refer to [Event streams permissions](/en/connectors/pubsub/pubsub-permissions) to ensure you have the required permissions to work with event streams.

> **FEATURE AVAILABILITY**
> 
> is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

In order to use Event streams you must complete the following steps:

1. [Create and configure](/en/connectors/pubsub/pubsub-creating-new) an event stream.
   
2. Create at least one recipe that uses a [publish message action](/en/connectors/pubsub/pubsub-actions) or [batch publish action](/en/connectors/pubsub/pubsub-batch-action) to publish to that event stream. Several recipes can publish to one event stream. Workato orders event stream messages by publish time.
   
3. Create at least one recipe that uses a [new message trigger](/en/connectors/pubsub/pubsub-new-message-trigger) or [new batch of messages trigger](/en/connectors/pubsub/pubsub-batch-trigger) to consume messages from that event stream. Several recipes can consume from one event stream, and each recipe receives all messages.
   
4. As an alternative to, or in addition to, publishing and consuming recipes, you can use the [Workato API](/en/workato-api/pubsub) to publish or consume messages directly.
   
5. Manage event stream properties in the [control UI](/en/connectors/pubsub/pubsub-settings).

---
