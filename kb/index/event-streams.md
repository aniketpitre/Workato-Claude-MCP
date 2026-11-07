# Event streams

18 pages. Paths are relative to the repository root.


## Event streams

- **Workato connectors - Workato Event streams** - `kb/docs/en/connectors/pubsub.md` - Workato Event Streams lets you build event-driven workflows: publish single or batched messages and trigger recipes on new messages or batches.
- **Event streams quotas** - `kb/docs/en/connectors/pubsub/limits.md` - Reference for Workato Event streams quotas, including payload size and other constraints that apply when publishing and consuming messages.
- **Event streams** - `kb/docs/en/event-streams.md` - Workato Event streams provides event-driven, message-oriented architecture that decouples publishers and consumers for guaranteed, persistent message delivery.
- **Developer API - Event streams public API** - `kb/docs/en/workato-api/pubsub.md` - Reference for the Workato Event streams public API to publish single messages, publish batches, and consume messages from event topics.

## Workato Event streams

- **Workato Event streams - actions** - `kb/docs/en/connectors/pubsub/pubsub-actions.md` - The publish message action in the Workato Event streams connector lets you publish one message at a time to a topic that other recipes can consume.
- **Workato Event streams - batch publish action** - `kb/docs/en/connectors/pubsub/pubsub-batch-action.md` - The batch publish action in the Workato Event streams connector lets you publish up to 100 messages at a time to a topic other recipes can consume.
- **Workato Event streams - batch trigger** - `kb/docs/en/connectors/pubsub/pubsub-batch-trigger.md` - The new batch of messages trigger in Workato Event streams polls batches of new messages from a topic at a specified time interval.
- **Workato Event streams - Set up** - `kb/docs/en/connectors/pubsub/pubsub-creating-new.md` - Create an event stream asset that defines a schema for publishers and consumers.
- **Workato Event streams - how to use** - `kb/docs/en/connectors/pubsub/pubsub-how-to-use.md` - Learn how to use Workato Event streams by creating a topic and building recipes that publish and consume messages from it.
- **Workato Event streams - messages list** - `kb/docs/en/connectors/pubsub/pubsub-messages-preview.md` - View the list of messages published to a Workato Event streams topic and inspect message details from the Message history tab.
- **Workato Event streams - new message trigger** - `kb/docs/en/connectors/pubsub/pubsub-new-message-trigger.md` - The New message trigger monitors a specific topic in real-time. The trigger picks up all messages published to that topic as a single trigger event.
- **Workato Event streams - permissions** - `kb/docs/en/connectors/pubsub/pubsub-permissions.md` - Set granular Workato Event streams permissions using role-based access control to manage who can view, edit, create, or delete topics.
- **Workato Event streams - resetting the topic** - `kb/docs/en/connectors/pubsub/pubsub-reset.md` - Reset a Workato Event streams topic to clear all of its messages, which is useful after an incompatible schema change or invalid data.
- **Workato Event streams - retention period** - `kb/docs/en/connectors/pubsub/pubsub-retention.md` - Configure the retention period for a Workato Event streams topic to control how long subscribers can access published messages.
- **Workato Event streams - setting up** - `kb/docs/en/connectors/pubsub/pubsub-schema-config.md` - Define the topic schema for Workato Event streams, setting message field names, data types, and hints manually or with a sample JSON.
- **Workato Event streams - setting up** - `kb/docs/en/connectors/pubsub/pubsub-settings.md` - Manage Workato Event streams topics from the control UI, including topic schema, message history, retention, and reset settings.
- **Workato Event streams - example scenarios** - `kb/docs/en/connectors/pubsub/pubsub-use-cases.md` - Example use cases for Workato Event streams, including decoupling recipes and creating batches from real-time events with topics.
- **Cross workspace sharing for Event Streams** - `kb/docs/en/cross-share-streams.md` - Share Event streams topics across Automation HQ workspaces using cross-workspace grants. You can create grants, manage access, and deploy recipes that depend on shared topics
