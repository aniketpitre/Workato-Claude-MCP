---
url: 'https://docs.workato.com/en/oem/oem-api/test-automation.md'
description: >-
  Reference for Embedded API endpoints to run test cases, list a recipe's test
  cases, and check test run status in customer workspaces.
---

# Embedded API - Test Automation

The following endpoint enables you to use the [Test Automation](/en/test-automation) feature programmatically.

## Rate limits

Test automation resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Test Automation](/en/oem/oem-api/test-automation.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users/:managed\_user\_id/ test\_cases/run\_requests](#run-test-cases) | Run test cases in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/recipes/ :recipe\_id/test\_cases](#list-test-cases) | Get test cases for a specific recipe in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/ test\_cases/run\_requests/:test\_id](#run-a-test-case) | Get the current state of a test case run request in a customer workspace. |

## Run test cases

Use this endpoint to run test cases in a customer workspace.

You can specify the test cases to run in the following ways:

- All test cases of all recipes in a manifest
- All test cases of all recipes in a project
- All test cases of all recipes in a folder
- All test cases belonging to a particular recipe
- Test cases you specify

This endpoint is asynchronous.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/test_cases/run_requests
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The external ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| manifest\_id | **integer** _optional_ | Run test cases for all recipes in the export manifest you specify. |
| project\_id | **integer** _optional_ | Run test cases for all recipes in the project you specify. Use the [list projects](/en/oem/oem-api/project-properties#list-projects) endpoint to retrieve the IDs of all projects in a customer workspace. |
| folder\_id | **integer** _optional_ | Run test cases for all recipes in the folder you specify. Use the [list folders](/en/oem/oem-api/folders#list-folders) endpoint to retrieve the IDs of all folders in a customer workspace. |
| recipe\_id | **integer** _optional_ | Run all test cases for the recipe you specify. Use the [list recipes](/en/oem/oem-api/recipes#list-recipes-in-a-customer-account) endpoint to retrieve the IDs of all recipes in a customer workspace. |
| test\_case\_ids | **array of strings** _optional_ | Run specific test cases by ID. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/test_cases/run_requests \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "recipe_id": :recipe_id
          }'
```

</api-code>

### Sample response

```json
{
    "data": {
        "id": "cirr-ALAGo123-Em8ewZ",
        "status": "running",
        "created_at": "2024-01-24T04:24:11.601-09:00",
        "updated_at": "2024-01-24T04:24:11.601-09:00",
        "user": {
            "id": 12345
        },
        "results": [
            {
                "job": {
                    "id": "j-ALAGo234-tXMPxZ"
                },
                "status": "pending",
                "recipe": {
                    "id": 987654,
                    "name": "Example Recipe"
                },
                "test_case": {
                    "id": "citc-ALAGd789-wcotNZ",
                    "name": "Example Test Case"
                }
            }
        ]
    }
}
```

## Get test cases

Returns a collection of test cases belonging to the recipe you specify in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/recipes/:recipe_id/test_cases
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer workspace ID/external ID. The external ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| recipe\_id | **integer** _required_ | The ID of the recipe for which to list the test cases. |

### Sample response

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/recipes/:recipe_id/test_cases' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

```json
{
  "data": [
    {
      "id": "citc-AG48N4xo-g6ccgP",
      "created_at": "2023-06-01T01:40:00.000-07:00",
      "updated_at": "2023-06-01T01:40:00.000-07:00",
      "description": "Validate API connections and data mappings",
      "name": "API connection Test"
    }
  ]
}
```

## Get the current state of a test case run request

Retrieve the current status and detailed information of a test case run request within a customer workspace. This endpoint provides insights into the test's progress and, for completed tests, includes data on test coverage and other relevant outcomes.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/test_cases/run_requests/:test_id
```

</api-code>

### URL parameters

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer workspace ID/external ID. |
| test\_id | **string** _required_ | The ID of the test run request. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/test_cases/run_requests/:test_id' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

```json
{
  "data": {
    "id": "cirr-AHNFkza6-dwMArc",
    "status": "completed",
    "created_at": "2024-01-24T04:24:11.601-09:00",
    "updated_at": "2024-01-24T04:24:12.602-09:00",
    "coverage": {
      "value": 87.5,
      "total_actions_count": 8,
      "total_visited_actions_count": 7,
      "recipes": [
        {
          "id": 67890,
          "name": "Employee Data Sync",
          "coverage": {
            "value": 87.5,
            "not_visited_actions": [
              {
                "step_number": 4,
                "description": "Check database trigger execution"
              }
            ]
          }
        }
      ]
    },
    "results": [
      {
        "recipe": {
          "id": 67890,
          "name": "Employee Data Sync"
        },
        "test_case": {
          "id": "citc-AG48N4xo-g6ccgP",
          "name": "Full Sync Test"
        },
        "job": {
          "id": "j-AHNFpnRa-sMWLYJ",
          "status": "succeeded"
        }
      }
    ]
  }
}
```

---
