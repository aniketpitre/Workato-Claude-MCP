---
url: 'https://docs.workato.com/en/workato-api/recipes.md'
description: >-
  Reference for the Workato recipes API to create, copy, update, start, stop,
  delete, and list recipes and manage recipe versions.
---

# Developer API - Recipes

Use this resource to manage recipes programmatically.

## Rate limits

Recipe resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Force an on-demand run of a recipe: [/api/recipes/:recipe\_id/force\_run](/en/workato-api/recipes.html#force-run-a-recipe) | 1 request per second |
| POST | Create a recipe: [/api/recipes](/en/workato-api/recipes.html#create-a-recipe) | 1 request per second |
| POST | Start analyzing recipe health: [/api/recipes/:recipe\_id/health](/en/workato-api/recipes.html#start-analyzing-recipe-health) | 20 requests per minute |
| All | All other [Recipes](/en/workato-api/recipes.html#get-recipe-details) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/recipes/:id](/en/workato-api/recipes#get-recipe-details) | Get recipe details. |
| GET | [/api/recipes/job\_counts](/en/workato-api/recipes#list-recipe-job-counts) | Retrieve job success and failure counts for one or more recipes. |
| POST | [/api/recipes](/en/workato-api/recipes#create-a-recipe) | Create a recipe. |
| POST | [/api/recipes/:id/copy](/en/workato-api/recipes#copy-a-recipe) | Copy a recipe. |
| PUT | [/api/recipes/:id](/en/workato-api/recipes#update-a-recipe) | Update a recipe. |
| GET | [/api/recipes](/en/workato-api/recipes#list-recipes-belonging-to-user) | List recipes belonging to user. |
| PUT | [/api/recipes/:id/start](/en/workato-api/recipes#start-recipe) | Start recipe. |
| PUT | [/api/recipes/:id/stop](/en/workato-api/recipes#stop-recipe) | Stop recipe. |
| DELETE | [/api/recipes/:id](/en/workato-api/recipes#delete-recipe) | Delete recipe. |
| POST | [/api/recipes/:recipe\_id/reset\_trigger](/en/workato-api/recipes#reset-recipe-trigger) | Reset recipe trigger. |
| PUT | [/api/recipes/:recipe\_id/connect](/en/workato-api/recipes#update-connection-for-recipe) | Update connection for an application in a stopped recipe. |
| POST | [/api/recipes/:recipe\_id/poll\_now](/en/workato-api/recipes#activate-polling-trigger-for-recipe) | Activate a polling trigger for a recipe. |
| POST | [/api/recipes/:recipe\_id/force\_run](/en/workato-api/recipes#force-run-a-recipe) | Force a recipe to run on demand. |
| GET | [/api/recipes/:recipe\_id/versions](/en/workato-api/recipes#get-recipe-versions) | Get recipe versions. |
| GET | [/api/recipes/:recipe\_id/versions/:id](/en/workato-api/recipes#get-a-specific-recipe-version) | Get details of a recipe version. |
| PATCH/PUT | [/api/recipes/:recipe\_id/versions/:id](/en/workato-api/recipes#update-a-recipe-version-comment) | Update a recipe version comment. |
| GET | [/api/recipes/:recipe\_id/health](#get-recipe-health) | Retrieve the most recent optimization report for a recipe. |
| POST | [/api/recipes/:recipe\_id/health](#start-analyzing-recipe-health) | Queue a performance scan using [Performance Copilot](/en/recipes/performance-copilot). |

> **PRIVATE BETA**
> 
> The following endpoints are in private beta:
> 
> - [Get recipe health](#get-recipe-health)
> - [Start analyzing recipe health](#start-analyzing-recipe-health)
> 
> Private beta features are available in production but only to selected customers. Customers must opt in and be accepted into the beta.
> 
> During the private beta, Workato may update its functionality or change its availability without prior notice.

## Get recipe details

Returns details about a recipe object. Lifetime task count has task data starting from March 19, 2021.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/recipes/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | Recipe ID. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| includes\[\] | **array of strings** _optional_ | Specifies additional fields to include in the response. Accepts `tags` as a value. If `tags` is supplied in the request, the response includes a `tags` field for the recipe. This field contains an array of zero or more tag handles (strings). |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id?includes[]=tags' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "id": 12389,
    "user_id": 4848,
    "name": "New webhook call will get JIRA ticket information",
    "created_at": "2016-08-03T11:06:23.950-07:00",
    "updated_at": "2021-11-29T23:31:58.735-08:00",
    "copy_count": 3,
    "trigger_application": "workato_webhooks",
    "action_applications": [
        "jira"
    ],
    "applications": [
        "workato_webhooks",
        "jira"
    ],
    "description": "New webhook call will get JIRA ticket information",
    "project_id": 13595198,
    "parameters_schema": [],
    "parameters": {},
    "folder_id": 4724,
    "running": false,
    "job_succeeded_count": 0,
    "job_failed_count": 0,
    "lifetime_task_count": 0,
    "last_run_at": "2016-08-03T11:06:51.481-07:00",
    "last_job_started_at": "2016-08-03T11:06:45.000-07:00",
    "stopped_at": "2016-08-03T11:22:57.285-07:00",
    "webhook_url": "https://www.workato.com/webhooks/rest/51b6a38f-0102-494d-8290-9d550aeeab3c/webhook_recipe",
    "stop_cause": null,
    "config": [
        {
            "keyword": "application",
            "name": "jira",
            "provider": "jira",
            "skip_validation": false,
            "account_id": null
        },
        {
            "keyword": "application",
            "name": "workato_webhooks",
            "provider": "workato_webhooks",
            "skip_validation": false,
            "account_id": null
        }
    ],
    "trigger_closure": null,
    "code": "...truncated...",
    "version_no": 2,
    "version_author_name": "Jennifer Diaz",
    "version_author_email": "kevin.smith@example.com",
    "version_comment": "Refactored webhook logic to improve error handling and added support for custom JIRA fields",
    "author_name": "Kevin Smith",
    "tags": [
        "tag-Abx8kN3x-Dv9HsJ-CD",
        "tag-Abx8kS4d-Gp2YvB-CD"
    ]
}
```

  

> **RESPONSE FIELDS**
> 
> The `last_run_at` field returns the timestamp when the recipe most recently started. The `last_job_started_at` field returns the timestamp when the most recent job for the recipe started. The `stopped_at` field returns the timestamp when the recipe most recently stopped.
> 
> These fields show when the recipe or its most recent job started or stopped. They don't include timestamps for earlier jobs.
> 
> The `code` field returns a JSON string describing the configuration of each recipe step. You can use `code` as an input for the [Create recipe](#create-a-recipe) and [Update recipe](#update-a-recipe) endpoints.

## List recipe job counts

Returns job success and failure counts for the recipe IDs you specify. Statistics cover the most recent 90 days. Recipes that don't have jobs in the 90-day time period are excluded from the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/recipes/job_counts
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_ids\[\] | **array of integers** _required_ | Recipe IDs to retrieve job counts for. You can specify multiple recipe IDs, but the request URL can't exceed 10,240 characters. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/recipes/job_counts?recipe_ids[]=499977&recipe_ids[]=500012' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "result": {
    "items": [
      {
        "recipe_id": 499977,
        "job_succeeded_count": 8412,
        "job_failed_count": 37
      },
      {
        "recipe_id": 500012,
        "job_succeeded_count": 156,
        "job_failed_count": 2
      }
    ]
  }
}
```

## Create a recipe

Creates a recipe in Workato based on parameters in the request.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/recipes
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| recipe | **object** _required_ | The recipe object. |
| recipe\[name\] | **string** _optional_ | Name of the recipe. |
| recipe\[code\] | **string** _required_ | JSON string representing the recipe lines. You can retrieve the `code` for an existing recipe using the [Get recipe details](#get-recipe-details) or [List recipes belonging to a user](#list-recipes-belonging-to-user) endpoint. |
| recipe\[config\] | **string** _optional_ | JSON string representing the connection lines. |
| recipe\[folder\_id\] | **string** _required_ | Folder for the recipe |
| recipe\[description\] | **string** _optional_ | Description of the recipe. |

> **FOLDER\_ID REQUIRED STARTING MAY 7, 2026**
> 
> Starting **May 7, 2026**, the `folder_id` parameter is required on this endpoint. The value must reference a project or folder other than the **Home assets** folder. Requests that omit `folder_id` or target the **Home assets** folder will return an error.

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/recipes \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
             "recipe": {
               "name": ":name",
               "code": ":code",
               "config": ":config",
               "folder_id": ":folder_id"
            }
          }'
```

</api-code>

### Response

```json
{
  "success": true,
  "id": 116
}
```

## Update a recipe

Updates an existing recipe in Workato specified based on recipe ID. Recipe details are defined based on parameters in the request.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/recipes/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | Recipe ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| recipe | **object** _optional_ | The recipe object. |
| recipe\[name\] | **string** _optional_ | Name of the recipe. |
| recipe\[code\] | **string** _optional_ | JSON string representing the recipe lines. You can retrieve the `code` for an existing recipe using the [Get recipe details](#get-recipe-details) or [List recipes belonging to a user](#list-recipes-belonging-to-user) endpoint. |
| recipe\[config\] | **string** _optional_ | JSON string representing the connection lines. |
| recipe\[folder\_id\] | **string** _optional_ | Folder for the recipe |
| recipe\[description\] | **string** _optional_ | Description of the recipe. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
             "recipe": {
               "name": ":name",
               "code": ":code",
               "config": ":config",
               "folder_id": ":folder_id"
             }
          }'
```

</api-code>

### Response

```json
{
  "success": true
}
```

  

> **UPDATING A RUNNING RECIPE IS PROHIBITED**
> 
> Any update call to a running recipe will return an error.

## Copy a recipe

Copy an existing recipe in Workato specified based on recipe ID.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/recipes/:id/copy
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | Recipe ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| folder\_id | **string** _required_ | Folder id for the copied recipe |

> **FOLDER\_ID REQUIRED STARTING MAY 7, 2026**
> 
> Starting **May 7, 2026**, the `folder_id` parameter is required on this endpoint. The value must reference a project or folder other than the **Home assets** folder. Requests that omit `folder_id` or target the **Home assets** folder will return an error.

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/copy' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{"folder_id": ":folder_id"}'
```

</api-code>

### Response

```json
{
  "success": true,
  "new_flow_id": 39404
}
```

## List recipes belonging to a user

Returns a list of recipes belonging to the authenticated user. Recipes are returned in descending ID order.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/recipes
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| adapter\_names\_all | **string** _optional_ | List of adapters names, separated by commas. Resulting recipes should use all of the given adapters. |
| adapter\_names\_any | **string** _optional_ | List of adapters names, separated by commas. Resulting recipes should use at least one of the given adapters. |
| folder\_id | **string** _optional_ | Return the recipes in the specified folder. |
| with\_subfolders | **boolean** _optional_ | If `true`, includes recipes from subfolders of the folder specified by `folder_id`. The default is `false`. |
| order | **string** _optional_ | Set ordering method. Possible options: activity, default. |
| page | **integer** _optional_ | Page number (defaults to 1). |
| per\_page | **integer** _optional_ | Specifies the number of recipes to include per page. Defaults to 100. The maximum value is 100. |
| running | **boolean** _optional_ | If `true`, returns running recipes. |
| since\_id | **integer** _optional_ | Use this parameter to retrieve recipes with IDs lower than the ID provided in the request. For example, if `since_id=15500`, Workato returns all recipes with IDs lower than `15500` (`0`\-`14999`). |
| stopped\_after | **string** _optional_ | Filter the list of recipes to exclude only those stopped after the date and time you specify. The date and time must be provided in ISO 8601 format according to the following pattern: `YYYY-MM-DDTHH:MM:SSZ`. |
| stop\_cause | **string** _optional_ | Reason that the recipe stopped. Possible reasons include — `trigger_errors_limit`: Recipe was stopped due to consecutive trigger errors `action_quota_limit`: Customer exceeded plan's task quota `trial_expired`: Customer's trial expired `txn_quota_limit`: Customer exceeded plan's job quota |
| updated\_after | **string** _optional_ | Filter the list of recipes to include only those updated after the date and time you specify. The date and time must be provided in ISO 8601 format according to the following pattern: `YYYY-MM-DDTHH:MM:SSZ`. |
| includes\[\] | **array of strings** _optional_ | Specifies additional fields to include in the response. Accepts `tags` as a value. If `tags` is supplied in the request, the response includes a `tags` field for each recipe. This field contains an array of zero or more tag handles (strings). |
| exclude\_code | **boolean** _optional_ | Indicates whether to exclude the recipes' code from the response. This can help avoid timeouts or `500` errors when recipes have complex or lengthy code. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/recipes?folder_id=:folder_id_value&with_subfolders=:with_subfolders_value&includes[]=tags' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "items": [
        {
            "id": 66876978,
            "user_id": 6471278,
            "name": "Sync new contacts from HubSpot to Mailchimp",
            "created_at": "2025-10-15T13:41:05.207-07:00",
            "updated_at": "2025-10-15T13:41:05.207-07:00",
            "copy_count": 1,
            "trigger_application": "hubspot",
            "action_applications": [
                "mailchimp"
            ],
            "applications": [
                "hubspot",
                "mailchimp"
            ],
            "description": "When a new contact is created in HubSpot, add them to the newsletter list in Mailchimp.",
            "project_id": 13595198,
            "parameters_schema": [],
            "parameters": {},
            "webhook_url": null,
            "folder_id": 27180381,
            "running": false,
            "job_succeeded_count": 0,
            "job_failed_count": 0,
            "lifetime_task_count": 0,
            "last_run_at": null,
            "stopped_at": null,
            "version_no": 1,
            "stop_cause": null,
            "config": [
                {
                    "keyword": "application",
                    "name": "hubspot",
                    "provider": "hubspot",
                    "account_id": 18253670,
                    "skip_validation": false
                },
                {
                    "keyword": "application",
                    "name": "mailchimp",
                    "provider": "mailchimp",
                    "account_id": 18253671,
                    "skip_validation": false
                }
            ],
            "trigger_closure": null,
            "code": "...truncated...",
            "author_name": "Sales",
            "version_author_name": "Alex",
            "version_author_email": "alex@workato.com",
            "version_comment": null,
            "tags": [
                "tag-Abx8kS7h-Rq6MtK-CD"
            ]
        },
        {
            "id": 66870000,
            "user_id": 6471278,
            "name": "Post Slack notifications when new leads are created in Salesforce",
            "created_at": "2025-10-15T10:47:45.142-07:00",
            "updated_at": "2025-10-15T10:57:36.857-07:00",
            "copy_count": 1,
            "trigger_application": "salesforce",
            "action_applications": [
                "slack"
            ],
            "applications": [
                "salesforce",
                "slack"
            ],
            "description": "1. New lead is created in Salesforce.\n2. Workato posts a message in Slack with the lead details.",
            "project_id": 13595198,
            "parameters_schema": [],
            "parameters": {},
            "webhook_url": null,
            "folder_id": 27180380,
            "running": false,
            "job_succeeded_count": 1,
            "job_failed_count": 0,
            "lifetime_task_count": 3,
            "last_run_at": "2025-10-15T10:51:29.528-07:00",
            "last_job_started_at": "2025-10-15T10:50:00.000-07:00"
            "stopped_at": "2025-10-15T10:54:29.298-07:00",
            "version_no": 6,
            "stop_cause": null,
            "config": [
                {
                    "keyword": "application",
                    "name": "salesforce",
                    "provider": "salesforce",
                    "account_id": 18253669,
                    "skip_validation": false
                },
                {
                    "keyword": "application",
                    "name": "slack",
                    "provider": "slack",
                    "account_id": 18253665,
                    "skip_validation": false
                }
            ],
            "trigger_closure": null,
            "code": "...truncated...",
            "author_name": "Sales",
            "version_author_name": "Alex",
            "version_author_email": "alex@workato.com",
            "version_comment": null,
            "tags": [
                "tag-Abx8kN3x-Dv9HsJ-CD",
                "tag-Abx8kS4d-Gp2YvB-CD"
            ]
        }
    ],
    "count": 2,
    "page": 1,
    "per_page": 100
}
```

  

> **RESPONSE FIELDS**
> 
> The `last_run_at` field returns the timestamp when the recipe most recently started. The `last_job_started_at` field returns the timestamp when the most recent job for the recipe started. The `stopped_at` field returns the timestamp when the recipe most recently stopped.
> 
> These fields show when the recipe or its most recent job started or stopped. They don't include timestamps for earlier jobs.
> 
> The `code` field returns a JSON string describing the configuration of each recipe step. You can use `code` as an input for the [Create recipe](#create-a-recipe) and [Update recipe](#update-a-recipe) endpoints.

## Start a recipe

Starts a recipe specified by recipe ID.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/recipes/:id/start
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _optional_ | Recipe ID. |

#### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/recipes/:recipe_id/start \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "success": true
}
```

## Stop a recipe

Stops a recipe specified by a recipe ID.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/recipes/:id/stop
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _optional_ | Recipe ID. |

#### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/recipes/:recipe_id/stop \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "success": true
}
```

## Delete a recipe

Delete a recipe specified by ID.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/recipes/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _optional_ | Recipe ID. |

#### Sample request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/recipes/:recipe_id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "success": true
}
```

## Reset recipe trigger

Reset recipe trigger cursor by recipe ID. Use this endpoint to re-sync data from the source application. The recipe should be designed to handle duplicate records because a re-sync processes every record again. Using this endpoint outside data orchestration scenarios may result in unintended behaviors, including data loss or corruption. Resetting a recipe trigger retains job history and records an event in the recipe's Activity audit log.

If you reset the trigger of an active recipe, Workato completes all jobs with a running, deferred, or pending status first. Then, it proceeds to the new jobs created by the reset trigger.

> **TRIGGER COMPATIBILITY**
> 
> This endpoint is only compatible with polling and scheduled triggers. Resetting other triggers may have no effect, or cause unintended behaviors. These triggers include:
> 
> - New CSV file in folder triggers
> - Function triggers
> - API triggers
> - RecipeOps triggers
> - Workbot triggers
> - Deprecated Kafka triggers (compatible with latest triggers)

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/recipes/:recipe_id/reset_trigger
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **integer** _required_ | ID of the recipe to reset. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/reset_trigger' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "success": true
}
```

## Update a connection for a recipe

Updates the chosen connection for a specific connector in a stopped recipe.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/recipes/:recipe_id/connect
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **integer** _required_ | ID of the recipe. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| adapter\_name | **string** _required_ | The internal name of the connector. e.g. `salesforce` |
| connection\_id | **integer** _required_ | The ID of the connection that replaces the existing one. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/connect' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
          "adapter_name": ":adapter_name",
          "connection_id": :connection_id_value
      }'
```

</api-code>

### Response

```json
{
    "success": true
}
```

## Activate a polling trigger for a recipe

Initiate the polling function of a recipe with polling triggers by providing the recipe ID. This action causes the recipe's polling trigger to execute immediately.

Use the [jobs APIs](/en/workato-api/jobs) to check the status of a particular recipe.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/recipes/:recipe_id/poll_now
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **integer** _required_ | The ID of the recipe you plan to start. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/recipes/:recipe_id/poll_now \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

- [Job started](#job-started)
- [Job already in progress](#job-in-progress)
- [Error codes](#error-codes)

#### Job started

```json
{
    "success": true
}
```

#### Job already in progress

```json
{
    "message": "Recipe is currently in trigger back off mode till 2023-06-23T23:02" }
}
```

#### Error codes

| Name | Description | Sample reply |
| --- | --- | --- |
| 404 | Not found | `{"success": false, "message": "Not Found"}` |
| 429 | Too many requests. A [Retry-After header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) specifies how long to wait before making a new request. | `{"message": "Recipe is currently in trigger back off mode till 2023-06-23T11:02"}`, or `{"message": "Not enough transaction credit"},` or `{"message": "Not enough action quota"}` |
| 400 | Bad request | `{"message":"Trial has expired"}` |

## Force an on-demand run of a recipe

Manually triggers an on-demand job for a recipe, independent of its normal schedule. The recipe's schedule isn't affected. This call adds a one-time job without rescheduling the recipe's future runs.

This endpoint only supports recipes that are running and use the [New recurring event trigger](/en/features/scheduler/triggers/new-recurring-event) from the [Scheduler by Workato](/en/features/scheduler) connector. Calling this endpoint on a stopped recipe, or on a recipe using a different trigger, returns a `422` error.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/recipes/:recipe_id/force_run
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **string** _required_ | ID of the recipe to run. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/force_run' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

- [Job enqueued](#force-run-job-enqueued)
- [Error codes](#force-run-error-codes)

#### Job enqueued

```json
{
    "success": true,
    "job_handles": [
        "j-AagAcc43-6otazC-CD"
    ]
}
```

`job_handles` contains the handle of the on-demand job.

#### Error codes

| Code | Description | Sample reply |
| --- | --- | --- |
| 404 | Not found. The recipe doesn't exist. | `{"message": "Not found"}` |
| 422 | Unprocessable entity. The recipe isn't running. | `{"message": "Recipe is not running. Start the recipe before triggering an on-demand run."}` |
| 422 | Unprocessable entity. The recipe's trigger isn't the **New recurring event** trigger. | `{"message": "On-demand runs are only supported for recipes with the Workato Scheduler trigger."}` |
| 429 | Too many requests. The workspace's quota is exceeded, or the [rate limit](#rate-limits) is exceeded. A [Retry-After header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) specifies how long to wait before making a new request. | `{"message": "Too many requests"}` |

## Get recipe versions

Retrieve detailed information about all versions of a specified recipe.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/recipes/:recipe_id/versions
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **string** _required_ | The ID of the recipe for which you plan to retrieve version details. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** _optional_ | Page number. Defaults to 1. |
| per\_page | **integer** _optional_ | Page size. Defaults to 100. The maximum is 100. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/versions' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "id": 397103,
            "comment": "Updated the recipe to include new Slack channels for onboarding new employees based on their roles",
            "version_no": 2,
            "author_name": "Alex",
            "author_email": "alex@example.com",
            "created_at": "2024-08-03T11:06:23.950-07:00",
            "updated_at": "2024-08-04T23:31:58.735-07:00"
        },
        {
            "id": 392814,
            "comment": "Initial setup of Slack channels for onboarding new employees, including creating channels based on department and role",
            "version_no": 1,
            "author_name": "Alex",
            "author_email": "alex@example.com",
            "created_at": "2024-08-03T11:06:23.950-07:00",
            "updated_at": "2024-08-03T11:06:23.950-07:00"
        }
    ]
}
```

## Get a specific recipe version

Retrieve detailed information about a specific recipe version.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/recipes/:recipe_id/versions/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **string** _required_ | The ID of the recipe for which you plan to retrieve version details. |
| id | **string** _required_ | The ID of the recipe version for which you plan to retrieve details. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/versions/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

200 OK

If successful, the API returns a `200 OK` status and a JSON response with the recipe version details:

```json
{
    "data": [
        {
            "id": 397103,
            "comment": "Updated the recipe to include new Slack channels for onboarding new employees based on their roles",
            "version_no": 2,
            "author_name": "Alex",
            "author_email": "alex@example.com",
            "created_at": "2024-08-04T23:31:58.735-07:00",
            "updated_at": "2024-08-04T23:31:58.735-07:00"
        }
    ]
}
```

404 NOT FOUND

The API returns a `404 Not Found` error when you provide a non-existent or mismatched value, such as an incorrect recipe ID or version ID:

```json
{
    "message": "Not found"
}
```

## Update a recipe version comment

Updates the comment on a specific recipe version. This endpoint modifies only the comment associated with the version, not the version itself.

<api-code no-copy-method>

```
PATCH https://YOUR_DATA_CENTER/api/recipes/:recipe_id/versions/:id
```

</api-code>

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/recipes/:recipe_id/versions/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **string** _required_ | The ID of the recipe for which you plan to retrieve version details. |
| id | **string** _required_ | The ID of the recipe version for which you plan to update the comment. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| comment | **string** _required_ | The new comment for the recipe version. Must be 255 characters or fewer. |

### Sample request

<api-code>

```shell
curl  -X PATCH 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/versions/:id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
                "comment": ":comment"
           }'
```

</api-code>

### Responses

200 OK

If successful, the API returns a `200 OK` status and a JSON response with the updated recipe version details:

```json
{
    "data": [
        {
            "id": 397103,
            "comment": "Refined the Slack channel setup for onboarding to ensure channels are created accurately based on employee roles and departments",
            "version_no": 2,
            "author_name": "Alex",
            "author_email": "alex@example.com",
            "created_at": "2024-08-04T23:31:58.735-07:00",
            "updated_at": "2024-08-07T23:31:58.735-07:00"
        }
    ]
}
```

404 NOT FOUND

The API returns a `404 Not Found` error when you provide a non-existent or mismatched value, such as an incorrect recipe ID or version ID:

```json
{
    "message": "Not found"
}
```

422 UNPROCESSABLE ENTITY

The API returns a `422 Unprocessable Entity` error in the following scenarios:

#### Comment exceeds 255 characters

This error occurs when the recipe version comment exceeds 255 characters:

```json
{
  "errors": [
        {
            "code": "validation_error",
            "title": "Comment is too long (maximum is 255 characters)",
            "detail": null
        }
    ]
}
```

#### Missing comment

This error occurs when the recipe version comment is missing from the request payload:

```json
{
  "errors": [
        {
            "code": "validation_error",
            "title": "Missing parameter comment",
            "detail": null
        }
    ]
}
```

## Get recipe health

This endpoint retrieves the most recent optimization report for a recipe. The report includes checks run by [Performance Copilot](/en/recipes/performance-copilot), rule violations, and a total score.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/recipes/:recipe_id/health
```

</api-code>

  

> **NO OPTIMIZATION DATA**
> 
> You must run a scan using the recipe editor or the [API](#start-analyzing-recipe-health) to generate a performance report. If you don't run a scan, this endpoint returns `null`.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **integer** _required_ | The ID of the recipe to retrieve performance data for. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/health' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

This endpoint returns the latest performance report for the recipe. The report includes the following information:

- A list of checks with associated rules
- Rule violations with explanations and suggestions
- A summary report with total score and impact breakdown

In the response, each `rule` includes a `uuid` that uniquely identifies it, and each `violation` has its own `uuid` to identify the specific instance. An empty `violations` array means no issues were found for that rule. A non-empty array indicates one or more violations.

```json
{
    "data": {
        "checks": [
            {
                "rule": {
                    "uuid": "067e2484-fe30-76b3-8000-2434f39f5b38",
                    "title": "Redundant Logging",
                    "category": "cost",
                    "impact": "low",
                    "effort": "low",
                    "level": "single_step",
                    "is_copilot_reparable": false
                },
                "violations": []
            },
            {
                "rule": {
                    "uuid": "01960e61-71ec-77d1-bd0f-6cbe8c830a28",
                    "title": "Using deprecated trigger",
                    "category": "performance",
                    "impact": "high",
                    "effort": "medium",
                    "level": "single_step",
                    "is_copilot_reparable": false
                },
                "violations": []
            },
            {
                "rule": {
                    "uuid": "01963843-d38b-7563-b55e-743ab422f523",
                    "title": "Missing error handling",
                    "category": "quality",
                    "impact": "medium",
                    "effort": "low",
                    "level": "multi_step",
                    "is_copilot_reparable": false
                },
                "violations": []
            },
            {
                "rule": {
                    "uuid": "067e2486-e64b-704a-8000-dc8b1345d458",
                    "title": "Unused Variable Detection",
                    "category": "cost",
                    "impact": "low",
                    "effort": "low",
                    "level": "single_step",
                    "is_copilot_reparable": false
                },
                "violations": []
            },
            {
                "rule": {
                    "uuid": "067e247e-0feb-7e9c-8000-3ebb0e739bcb",
                    "title": "Error handling block with no actions",
                    "category": "quality",
                    "impact": "medium",
                    "effort": "low",
                    "level": "single_step",
                    "is_copilot_reparable": false
                },
                "violations": []
            },
            {
                "rule": {
                    "uuid": "067e2483-75cd-7df8-8000-f5d2b6b8c29c",
                    "title": "Recipe too long",
                    "category": "quality",
                    "impact": "medium",
                    "effort": "medium",
                    "level": "recipe",
                    "is_copilot_reparable": false
                },
                "violations": []
            },
            {
                "rule": {
                    "uuid": "067e2485-f748-7ecd-8000-f11fdbb50534",
                    "title": "Using deprecated action",
                    "category": "performance",
                    "impact": "high",
                    "effort": "medium",
                    "level": "single_step",
                    "is_copilot_reparable": false
                },
                "violations": []
            },
            {
                "rule": {
                    "uuid": "019623c4-ce85-7952-93c2-3236982732a7",
                    "title": "Missing recipe description",
                    "category": "quality",
                    "impact": "low",
                    "effort": "low",
                    "level": "recipe",
                    "is_copilot_reparable": false
                },
                "violations": [
                    {
                        "uuid": "572d474c-e775-488b-b4ac-339642bf6c5f",
                        "explanation": "Recipes without clear descriptions are difficult for team members to understand, maintain, and troubleshoot, creating knowledge silos and increasing support overhead.",
                        "suggestion": "Add a comprehensive description outlining the recipe's purpose, business context, dependencies, and any special considerations for future maintainers.",
                        "level": "recipe",
                        "locations": []
                    }
                ]
            },
            {
                "rule": {
                    "uuid": "067e2482-44d1-7697-8000-d7d3acaf92ab",
                    "title": "Inefficient job filtering",
                    "category": "performance",
                    "impact": "medium",
                    "effort": "low",
                    "level": "multi_step",
                    "is_copilot_reparable": false
                },
                "violations": []
            },
            {
                "rule": {
                    "uuid": "067e2465-6330-75c8-8000-90900aaf09c1",
                    "title": "Consecutive Variable Declaration",
                    "category": "cost",
                    "impact": "medium",
                    "effort": "low",
                    "level": "multi_step",
                    "is_copilot_reparable": false
                },
                "violations": []
            }
        ],
        "report": {
            "total_score": 95,
            "impact": {
                "low": {
                    "total": 3,
                    "broken_rules": 1,
                    "violations": 1,
                    "weight": 2
                },
                "medium": {
                    "total": 5,
                    "broken_rules": 0,
                    "violations": 0,
                    "weight": 5
                },
                "high": {
                    "total": 2,
                    "broken_rules": 0,
                    "violations": 0,
                    "weight": 8
                },
                "critical": {
                    "total": 0,
                    "broken_rules": 0,
                    "violations": 0,
                    "weight": 10
                }
            },
            "completed_at": "2025-04-25T15:42:55.279Z"
        },
        "version": 1
    }
}
```

## Start analyzing recipe health

This endpoint queues a recipe for analysis by [Performance Copilot](/en/recipes/performance-copilot). Use this endpoint to request a new performance scan after making changes to the recipe.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/recipes/:recipe_id/health
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **integer** _required_ | The ID of the recipe to scan for performance issues. |

### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/health' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

The response confirms that the recipe has been successfully queued for analysis.

```json
{
    "status": "enqueued"
}
```

Use the [Get recipe health](#get-recipe-health) endpoint to retrieve the performance report after analysis is complete.

---
