---
url: 'https://docs.workato.com/en/connectors/greenhouse/search-objects-action.md'
description: >-
  The Search action in the Greenhouse connector lets you search your Greenhouse
  instance for candidates, applications, jobs, offers, and users by criteria.
---

# Greenhouse - Search action

This action executes a search in your Greenhouse instance by a given search criteria.

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [Search objects (v3)](/en/connectors/greenhouse/search-objects-v3) action before this date. The v3 action uses different query parameters and supports retrieving records by ID using filters.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![Search objects action](/assets/search-objects-action.VqWj_68_.png)_Search objects action_

## Input

| Input field | Description |
| --- | --- |
| Object | The object type. The available objects are:- Candidate
- Application
- Job
- Offer
- User
- Degrees
- Schools
- Disciplines |
| Object fields | Search fields available for the given object. |

## Output

The output of this action will be a datatree that contains information about the Greenhouse object.

Find out more about [Greenhouse object datapills](/en/connectors/greenhouse/object-types).

---
