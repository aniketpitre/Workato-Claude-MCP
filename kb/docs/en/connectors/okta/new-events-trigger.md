---
url: 'https://docs.workato.com/en/connectors/okta/new-events-trigger.md'
description: >-
  The New events trigger in the Okta connector fires when new events are created
  in your instance, with both polling and real-time options.
---

# Okta - New events trigger

The **New events** trigger activates when new events are created in your Okta instance. There are two separate triggers available:

- [New events](#new-events): Polls for new events at regular intervals.
- [New events (real-time)](#new-events-real-time): Monitors new events in real-time.

> **PERMISSION REQUIREMENTS**
> 
> The **Super Admin** permission in Okta is required to use this trigger.

## New events

This trigger picks up new events in your Okta instance. It checks for new events once every poll interval and each event is processed as a separate job.

![New event trigger](/assets/new-events-trigger.CGTZj2JN.png)_New event trigger_

### Input

| Field | Description |
| --- | --- |
| Event category | Specify the category of events that you wish to receive from Okta. More than one event category can be selected. |
| Event type | Specify the event types that you wish to receive from Okta. All event types of the chosen event categories are auto populated and more than one event type can be selected. |
| Event result | Specify whether you are observing a positive or negative event. |
| When first started, this recipe should pick up events from | Events created after this time will be processed by the recipe. If left blank, the default will be set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

### Output

The output datatree contains information about the event like the timestamp, the actor, the client used, the authentication and security contents.

Refer to the [Output datatree for events](/en/connectors/okta/events-output-datatree) section for the full list of output fields.

## New events (real-time)

This trigger picks up new events in your Okta instance in real-time. Each event is processed as a separate job.

![New event trigger (real-time)](/assets/new-events-trigger-realtime.DgOVaRub.png)_New event trigger (real-time)_

### Input

| Field | Description |
| --- | --- |
| Event category | Specify the category of events that you wish to receive from Okta. More than one event category can be selected. |
| Event type | Specify the event types that you wish to receive from Okta. All event types of the chosen event categories are auto populated and more than one event type can be selected. |
| Event result | Specify whether you are observing a positive or negative event. |
| When first started, this recipe should pick up events from | Events created after this time will be processed by the recipe. If left blank, the default will be set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

### Output

The output datatree contains information about the event like the timestamp, the actor, the client used, the authentication and security contents.

Refer to the [Output datatree for events](/en/connectors/okta/events-output-datatree) section for the full list of output fields.

---
