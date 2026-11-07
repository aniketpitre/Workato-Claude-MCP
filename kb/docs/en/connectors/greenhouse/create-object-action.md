---
url: 'https://docs.workato.com/en/connectors/greenhouse/create-object-action.md'
description: >-
  The Create object action in the Greenhouse connector lets you create new
  candidates, jobs, users, and candidate records in your Greenhouse instance.
---

# Greenhouse - Create object action

This action creates a new object in your Greenhouse instance.

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [Create object (v3)](/en/connectors/greenhouse/create-object-v3) action before this date.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![Update objects action](/assets/create-object-action.z7eI4nKY.png)_Update objects action_

## Input

| Input field | Description |
| --- | --- |
| Object | The object type. The available objects are:- Candidate
- Job
- User
- Candidate records (Candidate ID required) |
| Candidate ID _Only if creating candidate records_ | The candidate ID. You can create the following candidate records:- Candidate note
- Candidate email note
- Candidate education
- Candidate employment
- Candidate application |
| Object fields | Fields available for the given object. |

## Output

The output of this action will be a datatree that contains information about the created Greenhouse object.

Find out more about [Greenhouse object datapills](/en/connectors/greenhouse/object-types).

---
