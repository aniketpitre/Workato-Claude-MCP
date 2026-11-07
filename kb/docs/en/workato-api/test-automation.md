---
url: 'https://docs.workato.com/en/workato-api/test-automation.md'
description: >-
  Reference for the Workato Test Automation API to run recipe test cases and
  poll run requests by manifest, project, folder, or recipe.
---

# Developer API - Test Automation

The following endpoints enable you to use the [Test Automation](/en/test-automation) feature programmatically.

## Rate limits

Test Automation resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Test Automation](/en/workato-api/test-automation.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/test\_cases/run\_requests](#request-run) | Run test cases. |
| GET | [/api/test\_cases/run\_requests/:id](#run-result-get) | Get the current state of a test case run request. |
| GET | [/api/recipes/:recipe\_id/test\_cases](#test-cases-get) | Get test cases. |

## Run test cases

Use this endpoint to run test cases. You can specify the test cases to run in the following ways:

- All test cases of all recipes in a manifest
- All test cases of all recipes in a project
- All test cases of all recipes in a folder
- All test cases belonging to a particular recipe
- Test cases you specify

This endpoint is asynchronous. You can use the run request `id` to poll the current state of the request using the [/api/test\_cases/run\_requests/:id](#run-result-get) endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/test_cases/run_requests
```

</api-code>

### Request body

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| manifest\_id | **integer** _optional_ | Run test cases for all recipes in the export manifest you specify. |
| project\_id | **integer** _optional_ | Run test cases for all recipes in the project you specify. Use the [list projects](/en/workato-api/folders#list-projects) endpoint to retrieve the IDs of all projects in your workspace. |
| folder\_id | **integer** _optional_ | Run test cases for all recipes in the folder you specify. |
| recipe\_id | **integer** _optional_ | Run all test cases for the recipe you specify. |
| test\_case\_ids | **array of strings** _optional_ | Run specific test cases by ID. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/test_cases/run_requests \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "manifest_id": :manifest_id
          }'
```

</api-code>

### Sample response

```json
{
  "data": {
    "id": "cirr-AHNFkza6-dwMArc",
    "status": "running",
    "user": {
      "id": 0
    },
    "created_at": "2023-06-01T01:40:00.000-07:00",
    "updated_at": "2023-06-01T01:40:00.000-07:00",
    "results": [
      {
        "recipe": {
          "id": 0,
          "name": "string"
        },
        "test_case": {
          "id": "citc-AG48N4xo-g6ccgP",
          "name": "string"
        },
        "job": {
          "id": "j-AHNFpnRa-sMWLYJ"
        },
        "status": "pending"
      }
    ]
  }
}
```

## Get the current state of a test case run request

Get the current state of a test case run request. For completed requests, Workato also returns the test coverage data along with the results.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/test_cases/run_requests/:id
```

</api-code>

### URL parameters

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| id | **string** _required_ | The run request's ID. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/test_cases/run_requests/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

```json
{
  "data": {
    "id": "cirr-AHNFkza6-dwMArc",
    "status": "completed",
    "user": {
      "id": 0
    },
    "created_at": "2023-06-01T01:40:00.000-07:00",
    "updated_at": "2023-06-01T01:40:00.000-07:00",
    "coverage": {
      "value": 87.5,
      "total_actions_count": 8,
      "total_visited_actions_count": 7,
      "recipes": [
        {
          "id": 0,
          "version_no": 0,
          "coverage": {
            "value": 87.5,
            "not_visited_actions": [
              {
                "step_number": 4
              }
            ]
          }
        }
      ]
    },
    "results": [
      {
        "recipe": {
          "id": 0,
          "name": "string"
        },
        "test_case": {
          "id": "citc-AG48N4xo-g6ccgP",
          "name": "string"
        },
        "job": {
          "id": "j-AHNFpnRa-sMWLYJ"
        },
        "status": "succeeded"
      }
    ]
  }
}
```

## Get test cases

Returns a collection of test cases belonging to the recipe you specify.

<api-code no-copy-method>

```
GET  https://YOUR_DATA_CENTER/api/recipes/:recipe_id/test_cases
```

</api-code>

### URL Parameters

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| recipe\_id | **integer** _required_ | The ID of the recipe you plan to retrieve test case details from. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/recipes/:recipe_id/test_cases \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

```json
{
  "data": [
    {
      "id": "citc-AG48N4xo-g6ccgP",
      "created_at": "2023-06-01T01:40:00.000-07:00",
      "updated_at": "2023-06-01T01:40:00.000-07:00",
      "description": "string",
      "name": "string"
    }
  ]
}
```

---
