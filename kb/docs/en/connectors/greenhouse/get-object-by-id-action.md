---
url: 'https://docs.workato.com/en/connectors/greenhouse/get-object-by-id-action.md'
description: >-
  The Get object by ID action in the Greenhouse connector lets you retrieve a
  candidate, application, job, offer, or user by its unique Greenhouse ID.
---

# Greenhouse - Get object by ID action

This action retrieves information about a Greenhouse object by its unique Greenhouse ID.

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Greenhouse v3 doesn't provide a direct equivalent for this action. Use the [Search objects (v3)](/en/connectors/greenhouse/search-objects-v3) action and filter by a comma-separated list of IDs to retrieve specific records.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![Reject application action](/assets/get-object-by-id-action.FSDfCpyI.png)_Reject application action_

## Input

| Input field | Description |
| --- | --- |
| Object | The object type. The available objects are:- Candidate
- Application
- Job
- Offer
- User |
| Object ID | The ID of the object you want to retrieve. |

> **Retrieving Offer ID**
> 
> There are two ways to retrieve an offer - by Application ID or by Offer ID.
> 
> When using the **Application ID**, this action will only return the most recent offer. To retrieve the history of offers for an application, use the [Search object](/en/connectors/greenhouse/search-objects-action) action.

## Output

The output of this action will be a datatree that contains information about the Greenhouse object.

Find out more about [Greenhouse object datapills](/en/connectors/greenhouse/object-types).

---

---
url: >-
  https://docs.workato.com/en/connectors/greenhouse/advance-application-action.md
description: >-
  The Advance application action in the Greenhouse connector lets you move an
  active application to the next stage in the hiring pipeline.
---

# Greenhouse - Advance application action

This action moves the application to the next stage. Note that only applications with the [active status](/en/connectors/greenhouse/object-types#application-object) can be advanced.

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [Move application (v3)](/en/connectors/greenhouse/move-application-v3) action before this date. The v3 action supports broader transitions, including moving applications across stages and jobs.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![Advance application action](/assets/advance-application-action.Dq67EXDt.png)_Advance application action_

## Input

| Input field | Description |
| --- | --- |
| Application ID | The unique Greenhouse application ID. |
| From stage ID | The ID of the job stage this application is currently in. |

## Output

The output of this action is the application's information which reflects its new status.

Find out more about the [application object](/en/connectors/greenhouse/object-types#application-object).

---

---
url: >-
  https://docs.workato.com/en/connectors/greenhouse/mark-candidate-as-hired-action.md
description: >-
  The Mark candidate as hired action in the Greenhouse connector lets you set an
  active application's status to hired and set the start date.
---

# Greenhouse - Mark candidate as hired action

This action changes the status of the application to `hired`. Note that only applications with the [active status](/en/connectors/greenhouse/object-types#application-object) can be hired.

> **DEPRECATION NOTICE**
> 
> This action uses the legacy Greenhouse v1 API, which Greenhouse will remove on August 30, 2026.
> 
> Migrate to the [Mark candidate as hired (v3)](/en/connectors/greenhouse/mark-candidate-v3) action before this date.
> 
> Refer to the [Greenhouse v3 migration guide](/en/connectors/greenhouse/migration) to migrate your recipes.

![Mark candidate as hired action](/assets/mark-candidate-as-hired-action.Cmnj3hh_.png)_Mark candidate as hired action_

## Input

| Input field | Description |
| --- | --- |
| Application ID | The unique Greenhouse application ID. |
| Start date | The start date of the newly hired candidate. |

## Output

The output of this action is the application's information which reflects the `hired` status.

Find out more about the [application object](/en/connectors/greenhouse/object-types#application-object).

---
