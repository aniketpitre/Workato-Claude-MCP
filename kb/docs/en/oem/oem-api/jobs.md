---
url: 'https://docs.workato.com/en/oem/oem-api/jobs.md'
description: >-
  Reference for the Embedded API jobs endpoints to list jobs and retrieve job
  details for recipes in customer workspaces.
---

# Embedded API - Jobs

Use the following endpoints to view jobs for recipes in customer workspaces.

To use this API, you must first [edit the API client's role](/en/workato-api/api-clients#edit-a-client-role) to enable access to jobs in the customer workspace.

1. Navigate to **Workspace admin > API clients > Client roles** and select the role you plan to edit.
   
2. Select **Projects** in the **Customer workspaces** section.
   
3. Check the box for **List** and/or **Get details** to give the API client access to list jobs or get a single job's details.
   
   ![Editing an API client's role](/assets/oem-jobs-edit-api-client-role.yoMeWHo3.png) _Editing an API client's role to allow access to the jobs API_
   

## Rate limits

Job resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Repeat jobs: [/api/managed\_users/:managed\_user\_id/recipes /:recipe\_id/repeat\_jobs](/en/oem/oem-api/jobs.html#repeat-jobs) | 1 request per second |
| All | All other [Jobs](/en/oem/oem-api/jobs.html) endpoints | 1,000 requests per minute |

Additionally, [Repeat jobs](#repeat-jobs) has the following payload quota:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Repeat jobs: [/api/managed\_users/:managed\_user\_id/recipes /:recipe\_id/repeat\_jobs](/en/oem/oem-api/jobs.html#repeat-jobs) | 25 jobs per request |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:id/recipes/:recipe\_id/jobs](#list-jobs) | List jobs for a recipe. |
| GET | [/api/managed\_users/:id/recipes/:recipe\_id/jobs/:job\_id](#get-job-details) | Get job details. |
| POST | [/api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/repeat\_jobs](#repeat-jobs) | Repeats jobs you specify in a customer workspace. |

## List jobs

Returns aggregated job information for a recipe you specify within a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:id/recipes/:recipe_id/jobs
```

</api-code>

> **RUNTIME DATA NOT AVAILABLE**
> 
> Runtime data is the data that flows through the recipe at the time of job execution. This includes the input and output data from individual steps.
> 
> This data is available through the [Get job details](#get-job-details) endpoint or the [job details page](/en/recipes/jobs#viewing-job-reports) on the Workato platform.

  

> **RETRIEVE RECIPE NAME**
> 
> Use the `recipe_id` returned by this endpoint in the [Get recipe in a customer workspace](/en/oem/oem-api/recipes#get-recipe-in-a-customer-account) resource to obtain the corresponding `recipe_name`.

  

> **REPEAT JOBS ARE GROUPED BY CHAIN**
> 
> This endpoint returns one row per repeat chain. Each row represents the most recent repeat in the chain. The list excludes the original job and any intermediate repeats.
> 
> You can use the [Get job details](#get-job-details) endpoint with the corresponding job ID to retrieve the original job or an intermediate repeat.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| recipe\_id | **integer** _required_ | ID of the recipe with the jobs you plan to retrieve. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| offset\_job\_id | **string** _optional_ | The ID of the job to paginate from. The endpoint returns up to 1,000 jobs before or after this point, depending on the `prev` parameter. You can obtain a job ID from the response of this endpoint or the [Jobs](/en/recipes/jobs#job-metadata-and-statuses) page in Workato. |
| prev | **boolean** _optional_ | Defaults to `false`. When `prev=false`, this call returns jobs completed prior to the `offset_job_id`. If `prev=true`, jobs newer than the `offset_job_id` are returned. |
| status | **string** _optional_ | Filter by status - `succeeded`, `failed`, or `pending`. |
| rerun\_only | **boolean** _optional_ | If `true`, returns jobs that were rerun only. |
| offset\_run\_id | **integer** _(deprecated)_ | Offset run ID. This parameter has been deprecated. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/recipes/:recipe_id/jobs' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "job_succeeded_count": 2,
    "job_failed_count": 0,
    "job_count": 2,
    "job_scope_count": 2,
    "items": [
        {
            "id": "j-AJMfQh8c-hsCXcs",
            "completed_at": "2023-08-31T02:25:11.000-07:00",
            "started_at": "2023-08-31T02:25:11.000-07:00",
            "title": "API platform by Workato: new api request: Calling IP address=129.1.1.1, Access profile ID=12345, and Access profile name=Created from API Call after fix",
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
            "id": "j-AJMfNar9-L96nTm",
            "completed_at": "2023-08-31T02:22:09.000-07:00",
            "started_at": "2023-08-31T02:22:09.000-07:00",
            "title": "API platform by Workato: new api request: Calling IP address=129.1.1.1, Access profile ID=12345, and Access profile name=Created from API Call after fix",
            "is_poll_error": false,
            "error": null,
            "is_error": false,
            "status": "succeeded",
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

## Get job details

Returns a single job's metadata by its job ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:id/recipes/:recipe_id/jobs/:job_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| recipe\_id | **integer** _required_ | ID of the recipe with the job you plan to retrieve. |
| job\_id | **string** _required_ | The job's unique identifier. You can retrieve a Job ID using the [List jobs](#list-jobs) endpoint or the [Jobs](/en/recipes/jobs#job-metadata-and-statuses) page in Workato. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/recipes/:recipe_id/jobs/:job_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

View a sample response.

```json
{
    "id": "j-AJMfQh8c-hsCXcs",
    "handle": "j-AJMfQh8c-hsCXcs",
    "recipe_id": 169891,
    "completed_at": "2023-08-31T02:25:11.599-07:00",
    "started_at": "2023-08-31T02:25:11.519-07:00",
    "title": "API platform by Workato: new api request: Calling IP address=129.1.1.1, Access profile ID=12345, and Access profile name=Created from API Call after fix",
    "is_poll_error": false,
    "lines": [
        {
            "recipe_line_number": 0,
            "adapter_name": "workato_api_platform",
            "adapter_operation": "receive_request",
            "input": {
                "request": {
                    "content_type": "json"
                },
                "response": {
                    "content_type": "json",
                    "responses": [
                        {
                            "name": "succ",
                            "http_status_code": "200"
                        }
                    ]
                }
            },
            "output": {
                "context": {
                    "calling_ip": "129.1.1.1",
                    "jwt_payload": null,
                    "headers": {},
                    "access_profile": {
                        "id": 12345,
                        "name": "Created from API Call after fix",
                        "type": "token"
                    },
                    "client": {
                        "id": 4593,
                        "name": "API Client"
                    }
                },
                "request": {}
            },
            "mask_data": false,
            "line_stat": {
                "total": 0.013507305964594707,
                "details": [
                    {
                        "name": "map_input",
                        "count": 1,
                        "average": 0.012967139977263287,
                        "total": 0.012967139977263287,
                        "min": 0.012967139977263287,
                        "max": 0.012967139977263287
                    },
                    {
                        "name": "summarize_output_report",
                        "count": 1,
                        "average": 0.000336808996507898,
                        "total": 0.000336808996507898,
                        "min": 0.000336808996507898,
                        "max": 0.000336808996507898
                    },
                    {
                        "name": "event_title",
                        "count": 1,
                        "average": 0.00018715299665927887,
                        "total": 0.00018715299665927887,
                        "min": 0.00018715299665927887,
                        "max": 0.00018715299665927887
                    },
                    {
                        "name": "summarize_input_report",
                        "count": 1,
                        "average": 1.620399416424334e-05,
                        "total": 1.620399416424334e-05,
                        "min": 1.620399416424334e-05,
                        "max": 1.620399416424334e-05
                    }
                ]
            }
        },
        {
            "recipe_line_number": 1,
            "adapter_name": "workato_api_platform",
            "adapter_operation": "return_response",
            "input": {
                "http_status_code": "200",
                "response": null
            },
            "output": {
                "http_status_code": "200",
                "response": null
            },
            "mask_data": false,
            "line_stat": {
                "total": 0.0006757620139978826,
                "details": [
                    {
                        "name": "map_input",
                        "count": 1,
                        "average": 7.455993909388781e-06,
                        "total": 7.455993909388781e-06,
                        "min": 7.455993909388781e-06,
                        "max": 7.455993909388781e-06
                    },
                    {
                        "name": "normalize_input",
                        "count": 2,
                        "average": 1.2408505426719785e-05,
                        "total": 2.481701085343957e-05,
                        "min": 7.836992153897882e-06,
                        "max": 1.6980018699541688e-05
                    },
                    {
                        "name": "trim_input",
                        "count": 1,
                        "average": 1.774102565832436e-05,
                        "total": 1.774102565832436e-05,
                        "min": 1.774102565832436e-05,
                        "max": 1.774102565832436e-05
                    },
                    {
                        "name": "input_with_indifferent_access",
                        "count": 1,
                        "average": 5.086010787636042e-06,
                        "total": 5.086010787636042e-06,
                        "min": 5.086010787636042e-06,
                        "max": 5.086010787636042e-06
                    },
                    {
                        "name": "render_input",
                        "count": 1,
                        "average": 3.654300235211849e-05,
                        "total": 3.654300235211849e-05,
                        "min": 3.654300235211849e-05,
                        "max": 3.654300235211849e-05
                    },
                    {
                        "name": "input_flattened",
                        "count": 1,
                        "average": 4.6549830585718155e-06,
                        "total": 4.6549830585718155e-06,
                        "min": 4.6549830585718155e-06,
                        "max": 4.6549830585718155e-06
                    },
                    {
                        "name": "execute",
                        "count": 1,
                        "average": 0.0003469760122243315,
                        "total": 0.0003469760122243315,
                        "min": 0.0003469760122243315,
                        "max": 0.0003469760122243315
                    },
                    {
                        "name": "parse_output",
                        "count": 1,
                        "average": 1.7682992620393634e-05,
                        "total": 1.7682992620393634e-05,
                        "min": 1.7682992620393634e-05,
                        "max": 1.7682992620393634e-05
                    },
                    {
                        "name": "normalize_output",
                        "count": 1,
                        "average": 6.82898098602891e-06,
                        "total": 6.82898098602891e-06,
                        "min": 6.82898098602891e-06,
                        "max": 6.82898098602891e-06
                    },
                    {
                        "name": "summarize_input_report",
                        "count": 1,
                        "average": 0.0001418020110577345,
                        "total": 0.0001418020110577345,
                        "min": 0.0001418020110577345,
                        "max": 0.0001418020110577345
                    },
                    {
                        "name": "summarize_output_report",
                        "count": 1,
                        "average": 6.617399048991501e-05,
                        "total": 6.617399048991501e-05,
                        "min": 6.617399048991501e-05,
                        "max": 6.617399048991501e-05
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
    "master_job_id": "j-AJMfQh8c-hsCXcs",
    "master_job_handle": "j-AJMfQh8c-hsCXcs",
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

## Repeat jobs in a customer workspace

Repeats jobs you specify in a customer workspace. Repeats use the latest recipe version.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/recipes/:recipe_id/repeat_jobs
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
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| recipe\_id | **string** _required_ | The ID of the recipe to repeat jobs in. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| job\_ids | **array** _required_ | Contains the IDs of master jobs to repeat. You can retrieve a `master_job_id` using the [List jobs](#list-jobs) endpoint or the [Jobs](/en/recipes/jobs#job-metadata-and-statuses) page in Workato. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/recipes/:recipe_id/repeat_jobs' \
     -H "Authorization: Bearer <api_token>" \
     -H "Content-Type: application/json" \
     -d '{
          "job_ids": [
            ":job_id_1",
            ":job_id_2",
            ":job_id_3",
            ":job_id_4"
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

---
