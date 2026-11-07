---
url: 'https://docs.workato.com/en/connectors/greenhouse/update-object-action.md'
description: >-
  The Update object action in the Greenhouse connector lets you update a
  candidate, application, or job identified by its unique Greenhouse ID.
---

# Greenhouse - Update object action

This action updates a Greenhouse object identified by the unique Greenhouse ID.

> **Updating Greenhouse jobs**
> 
> Updating Greenhouse jobs may reset approvals and trigger re-approval processes.

![Update objects action](/assets/update-object-action.Dk33g4kd.png)_Update objects action_

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [Update object (v3)](/en/connectors/greenhouse/update-object-v3) action before this date.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

## Input

| Input field | Description |
| --- | --- |
| Object | The object type. The available objects are:- Candidate
- Application
- Job |
| Object ID | The ID of the object you want to update. |
| Object fields | Fields available for the given object. |

## Output

The output of this action will be a datatree that contains information about the updated Greenhouse object.

Find out more about [Greenhouse object datapills](/en/connectors/greenhouse/object-types).

---
