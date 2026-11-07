---
url: 'https://docs.workato.com/en/workato-api/jobs.md'
description: >-
  Reference for the Workato jobs API to list recipe jobs, retrieve job metadata,
  resume a job, and repeat jobs programmatically.
---

# Developer API - Jobs

Use the following endpoints to manage recipe jobs.

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/recipes/:recipe\_id/jobs](#list-jobs-from-a-recipe) | List jobs from a recipe. |
| GET | [/api/recipes/:recipe\_id/jobs/:job\_handle](#get-a-job) | Returns a single job's metadata. |
| POST | [/api/job/resume](#job-resume) | Resumes a particular job based on the `resume_token` you provide. This endpoint returns HTTP status code `204`, indicating successful request processing without any content included in the response. This endpoint is leveraged by [SDK Wait for resume actions](/en/developing-connectors/sdk/guides/building-actions/wait-for-resume-actions). |
| POST | [/api/recipes/:recipe\_id/repeat\_jobs](#repeat-jobs) | Repeats jobs you specify. |
| POST | [/api/recipes/:recipe\_id/cancel\_jobs](#cancel-jobs) | Cancels ongoing jobs you specify. |

## Rate limits

Job resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Repeat jobs: [/api/recipes/:recipe\_id/repeat\_jobs](/en/workato-api/jobs.html#repeat-jobs) | 1 request per second |
| POST | Cancel jobs: [/api/recipes/:recipe\_id/cancel\_jobs](/en/workato-api/jobs.html#cancel-jobs) | 1 request per second |
| All | All other [Jobs](/en/workato-api/jobs.html) endpoints | 60 requests per minute |

Additionally, [Repeat jobs](#repeat-jobs) and [Cancel jobs](#cancel-jobs) have the following payload quota:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Repeat jobs: [/api/recipes/:recipe\_id/repeat\_jobs](/en/workato-api/jobs.html#repeat-jobs) | 25 jobs per request |
| POST | Cancel jobs: [/api/recipes/:recipe\_id/cancel\_jobs](/en/workato-api/jobs.html#cancel-jobs) | 25 jobs per request |

## List jobs from a recipe

Returns aggregated job information as well as detailed job information for a specified recipe in Workato.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/recipes/:recipe_id/jobs
```

</api-code>

  

> **Run-time data not available**
> 
> Run-time data is the data that flows through the recipe at the time of job execution. This includes the input and output data from individual steps.
> 
> This data is available through the [Get a job](#get-a-job) endpoint or the [job details page](/en/recipes/jobs#viewing-job-reports) on the Workato platform.

> **REPEAT JOBS ARE GROUPED BY CHAIN**
> 
> This endpoint returns one row per repeat chain. Each row represents the most recent repeat in the chain. The list excludes the original job and any intermediate repeats.
> 
> You can use the [Get a job](#get-a-job) endpoint with the corresponding job ID to retrieve the original job or an intermediate repeat.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **integer** _required_ | Recipe ID. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| offset\_job\_id | **string** _optional_ | The ID of the job to paginate from. The endpoint returns up to 1,000 jobs before or after this point, depending on the `prev` parameter. You can obtain a job ID from the response of this endpoint or the [Jobs](/en/recipes/jobs#job-metadata-and-statuses) page in Workato. |
| prev | **boolean** _optional_ | Defaults to `false`. When `prev=false`, this call returns jobs completed prior to the `offset_job_id`. If `prev=true`, jobs newer than the `offset_job_id` are returned. |
| status | **string** _optional_ | Filter by status - `succeeded`, `failed` or `pending`. |
| rerun\_only | **boolean** _optional_ | If `true`, returns jobs that were rerun only. |
| offset\_run\_id | **integer** _(deprecated)_ | Offset run ID. This parameter has been deprecated. |
| failed | **boolean** _(deprecated)_ | If `true`, returns failed jobs only. This parameter has been deprecated. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/jobs' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "job_succeeded_count": 1,
  "job_failed_count": 1,
  "job_count": 1,
  "job_scope_count": 1,
  "items": [
    {
      "id": "j-KGAKfhsz-GYoLe",
      "completed_at": "2015-01-02T01:02:03.000Z",
      "started_at": "2015-01-02T01:02:03.000Z",
      "title": "Callable recipes by Workato: new call for recipe: Calling IP address=129.1.1.1, Access profile ID=123456, and Access profile name=recipe_test",
      "is_poll_error": false,
      "error": null,
      "is_error": false,
      "status": "succeeded",
      "calling_recipe_id": null,
      "calling_job_id": null,
      "recipe_id": 28904,
      "root_recipe_id": null,
      "root_job_id": null,
      "master_job_id": "j-UIL3NQ8L-ekbIaw-B1",
      "job_correlation_id": null
    },
    {
      "id": "j-AD9bJn99-hsCXcs",
      "completed_at": "2015-01-02T01:02:03.000Z",
      "started_at": "2015-01-02T01:02:03.000Z",
      "title": "Callable recipes by Workato: new call for recipe: Calling IP address=129.1.1.1, Access profile ID=123456, and Access profile name=recipe_test",
      "is_poll_error": false,
      "error": "Callable recipes by Workato: new call for recipe: Calling IP address=129.1.1.1, Access profile ID=123456, and Access profile name=recipe_test",
      "error_parts": {
        "adapter": "marketo",
        "error_type": "Missing required field",
        "message": "'Filter values' must be present",
        "error_id": "603260f5-a309-45b3-a20e-111d90a28917",
        "error_at": "2020-01-22T01:17:18.021-08:00",
        "input": "<redacted>",
        "inner_message": null
      },
      "is_error": true,
      "status": "failed",
      "calling_recipe_id": null,
      "calling_job_id": null,
      "recipe_id": 28904,
      "root_recipe_id": null,
      "root_job_id": null,
      "master_job_id": "j-USN6YQ8L-ekbNmw-B6",
      "job_correlation_id": null
    }
  ]
}
```

> **RESPONSE SIZE**
> 
> This endpoint returns up to 1,000 jobs in each response. Use the `offset_job_id` and `prev` parameters for pagination.

> **JOB CORRELATION ID**
> 
> `job_correlation_id` returns the `x-correlation-id` header from the originating webhook request. It's populated for jobs triggered by static webhooks, where the webhook carries the payload directly into the job. This field is `null` for hybrid triggers, where the webhook only signals a time-based poller to run and header metadata isn't retained.

## Get a job

Returns a single job's metadata by its job ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/recipes/:recipe_id/jobs/:job_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **integer** _required_ | Recipe ID. |
| job\_id | **string** _required_ | The job's unique identifier. You can retrieve a Job ID using the [List jobs from a recipe](#list-jobs-from-a-recipe) endpoint or the [Jobs](/en/recipes/jobs#job-metadata-and-statuses) page in Workato. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/jobs/:job_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "id": "j-AJTAt8w6-wdAgWM",
  "handle": "j-AJTAt8w6-wdAgWM",
  "recipe_id": 32723676,
  "completed_at": "2023-09-08T13:55:24.731-07:00",
  "started_at": "2023-09-08T13:55:24.606-07:00",
  "title": "Scheduler by Workato: new recurring event: Scheduled time=2023-09-08T13:55:24.177301-07:00, Scheduled day=Friday, and Scheduled week=36",
  "is_poll_error": false,
  "lines": [
    {
      "recipe_line_number": 0,
      "adapter_name": "clock",
      "adapter_operation": "scheduled_event",
      "input": {
        "time_unit": "minutes",
        "trigger_every": "5"
      },
      "output": {
        "scheduled_time": "2023-09-08T13:55:24.177301-07:00",
        "scheduled_day": "Friday",
        "scheduled_week": 36,
        "scheduled_month": "September",
        "last_job_time": "2023-09-08T12:05:31.000000-07:00"
      },
      "mask_data": false,
      "line_stat": {
        "total": 0.0034586129913805053,
        "details": [
          {
            "name": "map_input",
            "count": 1,
            "average": 0.0032869009883143008,
            "total": 0.0032869009883143008,
            "min": 0.0032869009883143008,
            "max": 0.0032869009883143008
          },
          {
            "name": "summarize_output_report",
            "count": 1,
            "average": 0.000025447006919421256,
            "total": 0.000025447006919421256,
            "min": 0.000025447006919421256,
            "max": 0.000025447006919421256
          },
          {
            "name": "event_title",
            "count": 1,
            "average": 0.00013735999527852982,
            "total": 0.00013735999527852982,
            "min": 0.00013735999527852982,
            "max": 0.00013735999527852982
          },
          {
            "name": "summarize_input_report",
            "count": 1,
            "average": 0.00000890500086825341,
            "total": 0.00000890500086825341,
            "min": 0.00000890500086825341,
            "max": 0.00000890500086825341
          }
        ]
      }
    }
  ],
  "error": null,
  "is_error": false,
  "is_repeat": false,
  "is_test": false,
  "is_test_case_job": false,
  "master_job_id": "j-AJTAt8w6-wdAgWM",
  "master_job_handle": "j-AJTAt8w6-wdAgWM",
  "status": "succeeded",
  "calling_recipe_id": null,
  "calling_job_id": null,
  "calling_job_handle": null,
  "root_recipe_id": null,
  "root_job_id": null,
  "job_correlation_id": null
}
```

> **IS REPEAT**
> 
> `is_repeat` is `true` for jobs created by repeating another job, and `false` for original jobs. `master_job_id` identifies the original job in the repeat chain when `is_repeat` is `true`.

> **JOB CORRELATION ID**
> 
> `job_correlation_id` returns the `x-correlation-id` header from the originating webhook request. It's populated for jobs triggered by static webhooks, where the webhook carries the payload directly into the job. This field is `null` for hybrid triggers, where the webhook only signals a time-based poller to run and header metadata isn't retained.

## Resume a job

Resumes a particular job based on the `resume_token` you provide. This endpoint returns HTTP status code `204`, indicating successful request processing without any content included in the response.

This endpoint is invoked by third-party apps when using [SDK Wait for resume actions](/en/developing-connectors/sdk/guides/building-actions/wait-for-resume-actions).

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/job/resume
```

</api-code>

### Request body

| Name | Type | Description |
| --- | --- | --- |
| token | **string** _required_ | The `resume_token` that matches the particular job you plan to resume. |
| data | **hash** _optional_ | Any contextual data you plan to pass back to the job. This data is accessible by the action in the `before_resume` lambda. The payload's quota is 50MB. For payloads larger than the quota, you can send a reference and allow the action’s `execute` lambda to make a secondary request to retrieve the data. |

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/job/resume \
     -H "Authorization: Bearer <api_token>" \
     -H "Content-Type: application/json" \
     -d '{
       "token": ":token",
       "data": :data
     }'
```

</api-code>

## Repeat jobs

Repeats jobs you specify by their master job ID. Repeats use the latest recipe version.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/recipes/:recipe_id/repeat_jobs
```

</api-code>

  

> **LIMITATIONS**
> 
> The **Repeat jobs** endpoint has the following limitations:
> 
> - You can only repeat jobs that are within the retention period. You can't repeat jobs in recipes that don't retain trigger event data. Refer to [Data retention policies](/en/security/data-protection/data-retention/#basics) for more information.
> - You can repeat a maximum of 25 jobs in each request.
> - You can repeat each job a maximum of 100 times.
> - You can only repeat jobs using the master job ID, not the ID of a previous repeat.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **string** _required_ | The ID of the recipe to repeat jobs in. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| job\_ids | **array** _required_ | Contains the IDs of master jobs to repeat. You can retrieve a `master_job_id` using the [List jobs from a recipe](#list-jobs-from-a-recipe) endpoint or the [Jobs](/en/recipes/jobs#job-metadata-and-statuses) page in Workato. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/repeat_jobs' \
     -H "Authorization: Bearer <api_token>" \
     -H "Content-Type: application/json" \
     -d '{
          "job_ids": [
            ":job_id_1",
            ":job_id_2"
            ]
          }'
```

</api-code>

### Response

200 OK

A `200 OK` status indicates the request was processed successfully. Check the `results` array for the status of each job and the `summary` for totals.

```json
{
  "results": [
    {
      "requested_job_id": "j-AJTAt8w6-wdAgWM",
      "status": "enqueued",
      "job": {
        "id": "j-DN1pT7hv-zgFLZP"
      }
    },
    {
      "requested_job_id": "j-BK9nR5ft-xeAEXN",
      "status": "failed",
      "error": {
        "type_id": "err.item.not_found",
        "message": "Job not found"
      }
    },
    {
      "requested_job_id": "j-AY4oD6g8-hdINaS",
      "status": "failed",
      "error": {
        "type_id": "err.job.repeat.invalid_id",
        "message": "Non-master job handle specified: j-AY4oD6g8-hdINaS"
      }
    },
    {
      "requested_job_id": "j-AOidEfa9-4MdaTF",
      "status": "failed",
      "error": {
        "type_id": "err.job.repeat.trigger_data_unavailable.expired",
        "message": "Can not repeat job j-AOidEfa9-4MdaTF. It has been erased due to retention policy."
      }
    }
  ],
  "summary": {
    "total_requested": 4,
    "total_enqueued": 1,
    "total_failed": 3
  }
}
```

400 Bad Request

You may receive a `400 Bad Request` error for several reasons. For example, the request contains more than 25 jobs, an empty `job_ids` array, duplicate `job_ids`, or a malformed array. Refer to the [400 Bad Request](/en/troubleshooting/400-bad-request-error) troubleshooting guide for more information.

```json
{ "message": "Maximum 25 jobs can be repeated in a single request. Received 75." }
```

```json
{ "message": "param is missing or the value is empty or invalid: job_ids" }
```

## Cancel jobs

Cancels one or more ongoing jobs you specify by their job ID. You can only cancel jobs that are in a `running` state.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/recipes/:recipe_id/cancel_jobs
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **string** _required_ | The ID of the recipe the jobs belong to. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| job\_ids | **array** _required_ | Contains the job IDs of ongoing jobs to cancel. Maximum 25 per request. You can retrieve a job ID using the [List jobs from a recipe](#list-jobs-from-a-recipe) endpoint or the [Jobs](/en/recipes/jobs#job-metadata-and-statuses) page in Workato. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/recipes/:recipe_id/cancel_jobs' \
     -H "Authorization: Bearer <api_token>" \
     -H "Content-Type: application/json" \
     -d '{
          "job_ids": [
            ":job_id_1",
            ":job_id_2"
            ]
          }'
```

</api-code>

### Response

```json
{
  "results": [
    {
      "requested_job_id": "j-AYBHXEFo-PQQBDT-B6",
      "status": "cancel_requested"
    },
    {
      "requested_job_id": "j-AYBHQNCp-oEpBXN-B6",
      "status": "failed",
      "error": {
        "type_id": "err.item.not_found",
        "message": "Job not found"
      }
    },
    {
      "requested_job_id": "j-AYBGmRND-bB6TH3-B6",
      "status": "failed",
      "error": {
        "type_id": "err.job.cancel.noncancellable",
        "message": "Job j-AYBGmRND-bB6TH3-B6 is not ongoing (status: succeeded) and cannot be cancelled."
      }
    }
  ],
  "summary": {
    "total_requested": 3,
    "total_succeeded": 1,
    "total_failed": 2
  }
}
```

400 Bad Request

You may receive a `400 Bad Request` error for several reasons. For example, the request contains more than 25 jobs, an empty or missing `job_ids` array, duplicate `job_ids`, or a malformed body. Refer to the [400 Bad Request](/en/troubleshooting/400-bad-request-error) troubleshooting guide for more information.

```json
{ "message": "Maximum 25 jobs can be cancelled in a single request. Received 26" }
```

```json
{ "message": "param is missing or the value is empty or invalid: job_ids" }
```

```json
{ "message": "Duplicate job IDs are not allowed in a single request" }
```

---
