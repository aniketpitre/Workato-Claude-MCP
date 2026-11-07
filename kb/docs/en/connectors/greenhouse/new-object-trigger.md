---
url: 'https://docs.workato.com/en/connectors/greenhouse/new-object-trigger.md'
description: >-
  The New object trigger in the Greenhouse connector picks up newly created
  candidates, applications, and scheduled interviews, processing each as a job.
---

# Greenhouse - New object trigger

This trigger picks up new objects that are created in your Greenhouse instance. Each new object is processed as an individual job.

> **DEPRECATION NOTICE**
> 
> This trigger uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [New object (v3) trigger](/en/connectors/greenhouse/new-object-v3) before this date.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![New objects trigger](/assets/new-object-trigger.Cj5ZjsQ8.png)_New objects trigger_

## Input

| Input field | Description |
| --- | --- |
| Object | The object type. The available objects are:- Candidate
- Application
- Scheduled interview |
| When first started, this recipe should pick up events from | Greenhouse objects that are created after this date and time will be processed in the trigger. If left blank, the trigger will pick up entries created 1 hour before the first time this recipe is started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output of this trigger will be a datatree that contains information about the new Greenhouse object.

Find out more about [Greenhouse object datapills](/en/connectors/greenhouse/object-types).

---
