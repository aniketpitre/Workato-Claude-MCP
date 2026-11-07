---
url: 'https://docs.workato.com/en/connectors/workfront/triggers.md'
description: >-
  Triggers in the Workfront connector that fire on new events in real time or
  poll for new and updated objects every configured interval.
---

# Workfront - Triggers

The Workfront connector supports the following triggers:

- [New Event trigger](#new-event-trigger) allows you to trigger recipes in real-time.
- [New Object trigger](#new-object-trigger) polls for new objects every configured polling interval.
- [New or updated Object trigger](#new-or-updated-object-trigger) polls for new or updated objects every configured polling interval.

## New event trigger

This trigger picks up new events in Workfront in real time. Each new job represents a single event. The output of the event trigger depends on the event selected in the trigger configuration.

![New event trigger](/assets/new-event-trigger.4Fl3RU3T.png)_New event trigger_

| Input field | Description |
| --- | --- |
| Object | The object you want this recipe to trigger on. When events happen in Workfront on your chosen object type, a job will be created. |
| Event type | Select the types of events you want to this recipe to trigger on. You can select one or more event types to listen on. |
| Custom form | The custom forms to be returned from Workfront. Leave blank to return all custom fields in all custom forms. |

> **Workfront object not found**
> 
> The New event trigger only supports a subset of objects available in Workfront. This is a limitation imposed by Workfront. If the object you are looking for is not present, use the new or new/updated object polling triggers instead.

## New Object trigger

This trigger picks up new object events in Workfront every configured polling interval. Each new object event creates a separate job.

![New Object trigger](/assets/new-object-trigger.C5V6lZyG.png)_New Object trigger_

| Input field | Description |
| --- | --- |
| Object | The object you want this recipe to trigger on. When a new object is created in Workfront, a job will be created. |
| Custom form | The custom forms to be returned from Workfront. Leave blank to return all custom fields in all custom forms. |
| When first started, this recipe should pick up events from | Defaults to 1 hour before the recipe is first started or tested. Use this to retrospectively pull new objects from Workfront. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Defaults to every 5 minutes if no value is given or if the given poll interval is lower. Use this to alter the polling interval. |

## New or updated Object trigger

This trigger picks up new or update object events in Workfront every configured polling interval. Each new or updated object event creates a separate job.

![New or updated Object trigger](/assets/new-updated-object-trigger.BRvS4pr1.png)_New or updated Object trigger_

| Input field | Description |
| --- | --- |
| Object | The object you want this recipe to trigger on. When events happen in Workfront on your chosen object type, a job will be created. |
| Custom form | The custom forms to be returned from Workfront. Leave blank to return all custom fields in all custom forms. |
| When first started, this recipe should pick up events from | Defaults to 1 hour before the recipe is first started or tested. Use this to retrospectively pull new objects from Workfront. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Defaults to every 5 minutes if no value is given or if the given poll interval is lower. Use this to alter the polling interval. |

---
