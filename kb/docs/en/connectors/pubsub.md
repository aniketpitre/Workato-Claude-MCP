---
url: 'https://docs.workato.com/en/connectors/pubsub.md'
description: >-
  Workato Event Streams lets you build event-driven workflows: publish single or
  batched messages and trigger recipes on new messages or batches.
---

# Workato Event streams

Workato Event streams enables you to implement integration solutions that require an event-driven, message-oriented architecture that decouples publishers and consumers. The connector implements a messaging system with support for guaranteed and persistent delivery. This allows us to chain recipes sequentially, as a recipe can publish a message that multiple other recipes consume as a trigger to kickstart their workflow.

This connector allows us to add or modify recipes which are consumers without affecting recipes which are publishers. This enables zero downtime for the publisher recipe as we can add new consumers without impacting or requiring changes in the publisher recipe. This decoupling results in simpler recipes and reduces the time required to create, test, and maintain recipes.

> **EVENT STREAMS ARE PROJECT ASSETS**
> 
> Each event stream is a project asset that belongs to a folder or project and appears in the **Assets** view. Refer to [Event streams as project assets](/en/event-streams#event-streams-as-project-assets) for more information.

## Large message support

Event streams handles large JSON payloads natively, without routing them through external file storage. You can publish single messages up to 10 MB. When a recipe or the API consumes messages in batches, Workato caps each batch at 50 MB of total payload and returns fewer messages per batch when individual payloads are large. No messages are lost, because Workato returns the remaining messages in later batches. Refer to [Event streams quotas](/en/connectors/pubsub/limits) for the full list of quotas.

> **FEATURE AVAILABILITY**
> 
> Event streams is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

---
