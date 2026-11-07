---
url: 'https://docs.workato.com/en/agentic/agent-studio/app-events/best-practices.md'
description: Learn best practices for App Events.
---

# App Events best practices

Workato recommends the following best practices to ensure that genie workflows are tuned to meet your goals:

## Use Event streams for high-volume processing

Synchronous App Events are appropriate for most use cases where events arrive at a manageable rate and each event triggers a recipe that runs a **Send business event** action directly.

Synchronous processing can create performance and cost risks for high-volume scenarios. You can decouple event intake from event processing using [Event streams](/en/event-streams) to improve performance.

1. Create an Event intake recipe.
   
   Create an Event intake recipe in your project and name it using the following convention: `Agentic | [Descriptive Name]`. For example, `Agentic | Jira Escalations`. This recipe receives events from the external system rather than calling **Send App Event** directly.
   
2. Replace the Send business event action with a Publish to Event Stream action.
   
   This enables the recipe to receive events from the external system and publish each event to the Event streams topic without waiting for the event to be processed.
   
   The **Event streams topic** stores published events in a persistent queue until consumed. Events queue in the topic rather than being lost if the processing recipe is slow or temporarily unavailable.
   
3. Create an Event processing subscriber recipe.
   
   Create a second recipe in your project. Set the trigger to **New event in Event stream** and select the topic. This recipe subscribes to the Event streams topic in the first recipe, reads each event from the queue, and calls **Send business event** with the appropriate genie and user.

---
