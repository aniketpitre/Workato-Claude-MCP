---
url: 'https://docs.workato.com/en/features/activity-audit-log-streaming-sample.md'
description: >-
  Reference for the Workato activity audit log JSON file, including the file
  path and name format plus sample job history data.
---

# Activity audit log file details and sample data

This article contains sample data on what is included in a typical activity audit log JSON file.

## JSON file details

Workato creates a JSON file for each event. The file path and name format are as follows:

| Item | Description |
| --- | --- |
| path | user\_id/jobs/recipe\_id/YYYYMMDD/job\_id/ Example: `1234/jobs/456/20220614/j-KGAKfhsz-GYoLeD/` |
| name | user\_id-recipe\_id-job\_id-YYYYMMDDHHMMSS-status.json Example: `1234-456-j-KGAKfhsz-GYoLeD-20220614-succeeded.json` |

Example file name: `1234/jobs/456/20220614/j-KGAKfhsz-GYoLeD/1234-456-j-KGAKfhsz-GYoLeD-20220614-succeeded.json`

> **LOG FILE SIZE QUOTA**
> 
> The file size quota for logs is 40 MB.
> 
> When streaming full job details, the system does not send step-specific log lines if the overall file size exceeds 40 MB. If a file exceeds 40 MB, the system still sends contextual job information, such as `user_id`, `recipe_id`, and `time_executed`. However, the “lines” column displays the default text, `Log lines exceed size limit`.

### JSON file content - sample data

Job history - Success

```json
{
  "id": "j-AEcaNzd9-dGQ4Bf",
  "master_job_id": "j-AEcaNXb8-KWAmEL",
  "recipe_id": 3026581,
  "calling_job_id": "j-AEcaNXWz-Yhzrct",
  "calling_recipe_id": 3026585,
  "root_job_handle": "j-AEcaNXWz-Yhzrct",
  "root_recipe_id": 3026585,
  "title": "Recipe function by Workato: new call for function: Calling job ID=j-AEcaNXWz-Yhzrct, Calling recipe ID=3026585, and ID=2d02d10dj28",
  "status": "succeeded",
  "is_repeat": true,
  "is_test": false,
  "started_at": "2022-10-19T22:30:46-07:00",
  "completed_at": "2022-10-19T22:30:46-07:00",
  "repeat_count": 1,
  "action_count": 2,
  "parent_id": "j-AEcaNXb8-KWAmEL",
  "flow_id": 3026581,
  "error_type": null,
  "is_poll_error": false,
  "account_id": 33359,
  "account_name": "Gabriel Sim",
  "environment_type": "dev",
  "environment_id": 33359,
  "error": null,
  "context": {
    "user_id": 33359,
    "user_name": "Gabriel Sim",
    "user_email": "gabriel.sim@workato.com",
    "recipe_id": 3026581,
    "recipe_url": "https://app.workato.com/recipes/3026581",
    "recipe_name": "Update customer contact details",
    "recipe_path": "Home/Functions",
    "job_id": "j-AEcaNzd9-dGQ4Bf",
    "master_job_id": "j-AEcaNXb8-KWAmEL",
    "calling_recipe_id": 3026585,
    "calling_job_id": "j-AEcaNXWz-Yhzrct",
    "is_repeat": true,
    "is_test": false,
    "repeat_count": 1,
    "job_url": "https://app.workato.com/recipes/3026581/job/j-AEcaNXb8-KWAmEL?child_job_id=j-AEcaNzd9-dGQ4Bf",
    "job_created_at": "2022-10-19T22:30:46.084655-07:00",
    "repeated_job": true,
    "parent_job_id": "j-AEcaNXb8-KWAmEL",
    "user_external_id": null
  },
  "report": {},
  "lines": [{
    "recipe_line_number": 0,
    "adapter_name": "workato_recipe_function",
    "adapter_operation": "execute",
    "input": {
      "parameters_schema_json": "[{\"name\":\"id\",\"type\":\"string\",\"optional\":false,\"control_type\":\"text\",\"label\":\"ID\"},{\"name\":\"name\",\"type\":\"string\",\"optional\":false,\"control_type\":\"text\",\"label\":\"Name\"}]"
    },
    "output": {
      "context": {
        "calling_job_id": "j-AEcaNXWz-Yhzrct",
        "calling_recipe_id": 3026585
      },
      "parameters": {
        "id": "2d02d10dj28",
        "name": "John Doe"
      }
    },
    "mask_data": false,
    "line_stat": {
      "total": 0.00043684104457497597,
      "details": [{
        "name": "map_input",
        "count": 1,
        "average": 3.4561380743980408e-06,
        "total": 3.4561380743980408e-06,
        "min": 3.4561380743980408e-06,
        "max": 3.4561380743980408e-06
      }, {
        "name": "normalize_input",
        "count": 1,
        "average": 2.6102876290678978e-05,
        "total": 2.6102876290678978e-05,
        "min": 2.6102876290678978e-05,
        "max": 2.6102876290678978e-05
      }, {
        "name": "summarize_output_report",
        "count": 1,
        "average": 0.00013904995284974575,
        "total": 0.00013904995284974575,
        "min": 0.00013904995284974575,
        "max": 0.00013904995284974575
      }, {
        "name": "event_title",
        "count": 1,
        "average": 0.00023522903211414814,
        "total": 0.00023522903211414814,
        "min": 0.00023522903211414814,
        "max": 0.00023522903211414814
      }, {
        "name": "summarize_input_report",
        "count": 1,
        "average": 3.300304524600506e-05,
        "total": 3.300304524600506e-05,
        "min": 3.300304524600506e-05,
        "max": 3.300304524600506e-05
      }]
    }
  }, {
    "recipe_line_number": 1,
    "adapter_name": "logger",
    "adapter_operation": "log_message",
    "input": {
      "user_logs_enabled": "false",
      "message": "2d02d10dj28\nJohn Doe"
    },
    "output": {
      "message": "2d02d10dj28\nJohn Doe"
    },
    "mask_data": false,
    "line_stat": {
      "total": 0.0006231747101992369,
      "details": [{
        "name": "map_input",
        "count": 1,
        "average": 6.73769973218441e-05,
        "total": 6.73769973218441e-05,
        "min": 6.73769973218441e-05,
        "max": 6.73769973218441e-05
      }, {
        "name": "normalize_input",
        "count": 2,
        "average": 2.1075480617582798e-05,
        "total": 4.2150961235165596e-05,
        "min": 1.0683899745345116e-05,
        "max": 3.146706148982048e-05
      }, {
        "name": "trim_input",
        "count": 1,
        "average": 2.4744775146245956e-05,
        "total": 2.4744775146245956e-05,
        "min": 2.4744775146245956e-05,
        "max": 2.4744775146245956e-05
      }, {
        "name": "input_with_indifferent_access",
        "count": 1,
        "average": 8.066883310675621e-06,
        "total": 8.066883310675621e-06,
        "min": 8.066883310675621e-06,
        "max": 8.066883310675621e-06
      }, {
        "name": "render_input",
        "count": 1,
        "average": 5.113217048346996e-05,
        "total": 5.113217048346996e-05,
        "min": 5.113217048346996e-05,
        "max": 5.113217048346996e-05
      }, {
        "name": "input_flattened",
        "count": 1,
        "average": 2.0849984139204025e-06,
        "total": 2.0849984139204025e-06,
        "min": 2.0849984139204025e-06,
        "max": 2.0849984139204025e-06
      }, {
        "name": "execute",
        "count": 1,
        "average": 0.00036507495678961277,
        "total": 0.00036507495678961277,
        "min": 0.00036507495678961277,
        "max": 0.00036507495678961277
      }, {
        "name": "parse_output",
        "count": 1,
        "average": 2.2870954126119614e-05,
        "total": 2.2870954126119614e-05,
        "min": 2.2870954126119614e-05,
        "max": 2.2870954126119614e-05
      }, {
        "name": "normalize_output",
        "count": 1,
        "average": 8.760020136833191e-06,
        "total": 8.760020136833191e-06,
        "min": 8.760020136833191e-06,
        "max": 8.760020136833191e-06
      }, {
        "name": "summarize_input_report",
        "count": 1,
        "average": 1.499708741903305e-05,
        "total": 1.499708741903305e-05,
        "min": 1.499708741903305e-05,
        "max": 1.499708741903305e-05
      }, {
        "name": "summarize_output_report",
        "count": 1,
        "average": 1.5914905816316605e-05,
        "total": 1.5914905816316605e-05,
        "min": 1.5914905816316605e-05,
        "max": 1.5914905816316605e-05
      }]
    }
  }, {
    "recipe_line_number": 2,
    "adapter_name": "workato_recipe_function",
    "adapter_operation": "return_result",
    "input": {
      "result": null
    },
    "output": {},
    "mask_data": false,
    "line_stat": {
      "total": 0.00041800527833402157,
      "details": [{
        "name": "map_input",
        "count": 1,
        "average": 1.4118850231170654e-06,
        "total": 1.4118850231170654e-06,
        "min": 1.4118850231170654e-06,
        "max": 1.4118850231170654e-06
      }, {
        "name": "normalize_input",
        "count": 2,
        "average": 1.2210803106427193e-06,
        "total": 2.4421606212854385e-06,
        "min": 7.431954145431519e-07,
        "max": 1.6989652067422867e-06
      }, {
        "name": "trim_input",
        "count": 1,
        "average": 3.2829120755195618e-06,
        "total": 3.2829120755195618e-06,
        "min": 3.2829120755195618e-06,
        "max": 3.2829120755195618e-06
      }, {
        "name": "input_with_indifferent_access",
        "count": 1,
        "average": 3.4710392355918884e-06,
        "total": 3.4710392355918884e-06,
        "min": 3.4710392355918884e-06,
        "max": 3.4710392355918884e-06
      }, {
        "name": "render_input",
        "count": 1,
        "average": 5.241017788648605e-06,
        "total": 5.241017788648605e-06,
        "min": 5.241017788648605e-06,
        "max": 5.241017788648605e-06
      }, {
        "name": "input_flattened",
        "count": 1,
        "average": 1.1560041457414627e-06,
        "total": 1.1560041457414627e-06,
        "min": 1.1560041457414627e-06,
        "max": 1.1560041457414627e-06
      }, {
        "name": "execute",
        "count": 1,
        "average": 0.0003324940335005522,
        "total": 0.0003324940335005522,
        "min": 0.0003324940335005522,
        "max": 0.0003324940335005522
      }, {
        "name": "parse_output",
        "count": 1,
        "average": 5.090143531560898e-06,
        "total": 5.090143531560898e-06,
        "min": 5.090143531560898e-06,
        "max": 5.090143531560898e-06
      }, {
        "name": "normalize_output",
        "count": 1,
        "average": 8.961651474237442e-07,
        "total": 8.961651474237442e-07,
        "min": 8.961651474237442e-07,
        "max": 8.961651474237442e-07
      }, {
        "name": "summarize_input_report",
        "count": 1,
        "average": 6.251991726458073e-05,
        "total": 6.251991726458073e-05,
        "min": 6.251991726458073e-05,
        "max": 6.251991726458073e-05
      }]
    }
  }]
}
```

Job history - Summary

```json
{
    "log_message": {
        "id": "job-123456789",
        "master_job_id": "job-123456789",
        "recipe_id": 35428227,
        "calling_job_id": "job-987654321",
        "calling_recipe_id": 32587368,
        "root_job_handle": "j-AEcaNXWz-Yhzrct",
        "root_recipe_id": 3026585,
        "title": "Recipe function by Workato: new call for function: Calling job ID=job-987654321, Calling recipe ID=32587368, and Project name=Test CICD",
        "status": "succeeded",
        "is_repeat": false,
        "is_test": false,
        "is_test_case_job": false,
        "started_at": "2023-12-22T12:08:58-08:00",
        "completed_at": "2023-12-22T12:08:59-08:00",
        "repeat_count": 0,
        "action_count": 5,
        "parent_id": null,
        "flow_id": 35428227,
        "error_type": null,
        "is_poll_error": false,
        "account_id": 0000000,
        "account_name": "John Doe",
        "environment_type": "dev",
        "environment_id": 0000000,
        "hq_account_id": 0,
        "hq_account_name": "",
        "error": null,
        "report": {},
        "context": {
            "user_id": 0000000,
            "user_name": "John Doe",
            "user_email": "john.doe@example.com",
            "recipe_id": 35428227,
            "recipe_url": "https://app.workato.com/recipes/35428227",
            "recipe_name": "[CICD] | FUN-003 | Deploy via Projects",
            "recipe_path": "Home/CICD AWS/Functions",
            "job_id": "job-123456789",
            "master_job_id": "job-123456789",
            "calling_recipe_id": 32587368,
            "calling_job_id": "job-987654321",
            "root_job_handle": "j-AEcaNXWz-Yhzrct",
            "root_recipe_id": 3026585,
            "is_repeat": false,
            "is_test": false,
            "repeat_count": 0,
            "job_url": "https://app.workato.com/recipes/35428227/job/job-123456789",
            "job_created_at": "2023-12-22T12:08:58-08:00",
            "repeated_job": false,
            "parent_job_id": null,
            "user_external_id": null
        }
    },
    "now_utc_micro": 1703275739238000
}
```

Job history - Failure

```json
{
  "id": "j-AEcaQsxm-Ec4PRe",
  "master_job_id": "j-AEcaNXb8-KWAmEL",
  "recipe_id": 3026581,
  "calling_job_id": "j-AEcaNXWz-Yhzrct",
  "calling_recipe_id": 3026585,
  "root_job_handle": "j-AEcaNXWz-Yhzrct",
  "root_recipe_id": 3026585,
  "title": "Recipe function by Workato: new call for function: Calling job ID=j-AEcaNXWz-Yhzrct, Calling recipe ID=3026585, and ID=2d02d10dj28",
  "status": "failed",
  "is_repeat": true,
  "is_test": false,
  "started_at": "2022-10-19T22:33:29-07:00",
  "completed_at": "2022-10-19T22:33:29-07:00",
  "repeat_count": 2,
  "action_count": 0,
  "parent_id": "j-AEcaNzd9-dGQ4Bf",
  "flow_id": 3026581,
  "error_type": "Bad data sent to API server",
  "is_poll_error": false,
  "account_id": 33359,
  "account_name": "Gabriel Sim",
  "environment_type": "dev",
  "environment_id": 33359,
  "error": "{\"error_id\":\"7859dd09-bf6d-4d47-a55b-e84049cdafe2\",\"error_type\":\"Bad data sent to API server\",\"error_at\":\"2022-10-19T22:33:29.643-07:00\",\"adapter\":\"salesforce\",\"action\":\"create_custom_object\",\"line_number\":2,\"message\":\"Invalid Salesforce ID value(s) for: AccountId\",\"inner_message\":null, \"http_response\":{\"protocol\":\"HTTP/1.1\",\"code\":400,\"raw_status_text\":\"Bad Request\",\"normalized_status_text\":\"Bad Request\",\"normalized_headers\":[{\"name\":\"Content-Length\",\"value\":\"2\"},{\"name\":\"Content-Type\",\"value\":\"application/json\"},{\"name\":\"Date\",\"value\":\"Wed, 19 Oct 2022 07:00:21 GMT\"}],\"body\":\"{}\",\"headers\":{\"content_length\":\"2\",\"content_type\":\"application/json\",\"date\":\"Wed, 19 Oct 2022 07:00:21 GMT\"}}}",
  "context": {
    "user_id": 33359,
    "user_name": "Gabriel Sim",
    "user_email": "gabriel.sim@workato.com",
    "recipe_id": 3026581,
    "recipe_url": "https://app.workato.com/recipes/3026581",
    "recipe_name": "Update customer contact details",
    "recipe_path": "Home/Functions",
    "job_id": "j-AEcaQsxm-Ec4PRe",
    "master_job_id": "j-AEcaNXb8-KWAmEL",
    "calling_recipe_id": 3026585,
    "calling_job_id": "j-AEcaNXWz-Yhzrct",
    "root_job_handle": "j-AEcaNXWz-Yhzrct",
    "root_recipe_id": 3026585,
    "is_repeat": true,
    "is_test": false,
    "repeat_count": 2,
    "job_url": "https://app.workato.com/recipes/3026581/job/j-AEcaNzd9-dGQ4Bf?child_job_id=j-AEcaQsxm-Ec4PRe",
    "job_created_at": "2022-10-19T22:33:29.354481-07:00",
    "repeated_job": true,
    "parent_job_id": "j-AEcaNzd9-dGQ4Bf",
    "user_external_id": null
  },
  "report": {},
  "lines": [{
    "recipe_line_number": 0,
    "adapter_name": "workato_recipe_function",
    "adapter_operation": "execute",
    "input": {
      "parameters_schema_json": "[{\"name\":\"id\",\"type\":\"string\",\"optional\":false,\"control_type\":\"text\",\"label\":\"ID\"},{\"name\":\"name\",\"type\":\"string\",\"optional\":false,\"control_type\":\"text\",\"label\":\"Name\"}]"
    },
    "output": {
      "context": {
        "calling_job_id": "j-AEcaNXWz-Yhzrct",
        "calling_recipe_id": 3026585,
        "root_job_handle": "j-AEcaNXWz-Yhzrct",
        "root_recipe_id": 3026585
      },
      "parameters": {
        "id": "2d02d10dj28",
        "name": "John Doe"
      }
    },
    "mask_data": false,
    "line_stat": {
      "total": 0.00029799481853842735,
      "details": [{
        "name": "map_input",
        "count": 1,
        "average": 3.3209798857569695e-06,
        "total": 3.3209798857569695e-06,
        "min": 3.3209798857569695e-06,
        "max": 3.3209798857569695e-06
      }, {
        "name": "normalize_input",
        "count": 1,
        "average": 1.7269980162382126e-05,
        "total": 1.7269980162382126e-05,
        "min": 1.7269980162382126e-05,
        "max": 1.7269980162382126e-05
      }, {
        "name": "summarize_output_report",
        "count": 1,
        "average": 0.00010947103146463633,
        "total": 0.00010947103146463633,
        "min": 0.00010947103146463633,
        "max": 0.00010947103146463633
      }, {
        "name": "event_title",
        "count": 1,
        "average": 0.00014947890304028988,
        "total": 0.00014947890304028988,
        "min": 0.00014947890304028988,
        "max": 0.00014947890304028988
      }, {
        "name": "summarize_input_report",
        "count": 1,
        "average": 1.8453923985362053e-05,
        "total": 1.8453923985362053e-05,
        "min": 1.8453923985362053e-05,
        "max": 1.8453923985362053e-05
      }]
    }
  }, {
    "recipe_line_number": 1,
    "adapter_name": "salesforce",
    "adapter_operation": "create_custom_object",
    "input": {
      "sobject_name": "Contact",
      "LastName": "John Doe",
      "AccountId": "2d02d10dj28",
      "FirstName": "John Doe"
    },
    "output": {},
    "error": "Invalid Salesforce ID value(s) for: AccountId",
    "mask_data": false,
    "line_stat": {
      "total": 0.07894168607890606,
      "details": [{
        "name": "map_input",
        "count": 1,
        "average": 8.689402602612972e-05,
        "total": 8.689402602612972e-05,
        "min": 8.689402602612972e-05,
        "max": 8.689402602612972e-05
      }, {
        "name": "normalize_input",
        "count": 2,
        "average": 1.2068485375493765e-05,
        "total": 2.413697075098753e-05,
        "min": 7.361988537013531e-06,
        "max": 1.6774982213974e-05
      }, {
        "name": "trim_input",
        "count": 1,
        "average": 7.869710680097342e-05,
        "total": 7.869710680097342e-05,
        "min": 7.869710680097342e-05,
        "max": 7.869710680097342e-05
      }, {
        "name": "input_with_indifferent_access",
        "count": 1,
        "average": 5.826936103403568e-06,
        "total": 5.826936103403568e-06,
        "min": 5.826936103403568e-06,
        "max": 5.826936103403568e-06
      }, {
        "name": "render_input",
        "count": 1,
        "average": 0.00010894099250435829,
        "total": 0.00010894099250435829,
        "min": 0.00010894099250435829,
        "max": 0.00010894099250435829
      }, {
        "name": "input_flattened",
        "count": 1,
        "average": 1.3289973139762878e-06,
        "total": 1.3289973139762878e-06,
        "min": 1.3289973139762878e-06,
        "max": 1.3289973139762878e-06
      }, {
        "name": "execute",
        "count": 1,
        "average": 0.07858130801469088,
        "total": 0.07858130801469088,
        "min": 0.07858130801469088,
        "max": 0.07858130801469088
      }, {
        "name": "summarize_input_report",
        "count": 1,
        "average": 5.455303471535444e-05,
        "total": 5.455303471535444e-05,
        "min": 5.455303471535444e-05,
        "max": 5.455303471535444e-05
      }]
    }
  }]
}
```

User login

```json
{
  "resource": {
    "email_confirmed_at": "2019-11-24 14:29:30 -0800",
    "name": "John Smith",
    "id": 4848,
    "type": "User",
    "email": "john.smith@workato.com"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    },
    "activity": "sso_login",
    "sso_provider": "google"
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "user_login",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-02 02:39:22 UTC"
}
```

User logout

```json
{
  "resource": {
    "email_confirmed_at": "2019-11-24 14:29:30 -0800",
    "name": "John Smith",
    "id": 4848,
    "type": "User",
    "email": "john.smith@workato.com"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    },
    "activity": "user_logout"
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "user_logout",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-02 02:39:10 UTC"
}
```

Manifest updated

```json
{
  "resource": {
    "name": "Document reading",
    "id": 911,
    "type": "ExportManifest"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato eam",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "manifest_updated",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-02 02:51:46 UTC"
}
```

Package exported

```json
{
  "resource": {
    "file_name": "vision-ai-license-and-registration_john-smith.zip",
    "id": 1076,
    "type": "Package",
    "folder_id": 5223,
    "folder_path": "Home/Vision AI - License and Registration"
  },
  "team": {
    "name": "Workato Team",
    "id": 4805,
    "email": "john.smith@workato.com"
  },
  "event": "package_exported",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-02 02:52:17 UTC"
}
```

Package imported

```json
{
  "resource": {
    "file_name": "griddynamics_demo.zip",
    "id": 1077,
    "type": "Package",
    "folder_id": 6593,
    "folder_path": "Home/HR"
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "package_imported",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-02 02:53:33 UTC"
}
```

Recipe created

```json
{
  "resource": {
    "name": "Candidate in Progress on JIRA will advance on GreenHouse",
    "id": 33167,
    "type": "Flow"
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "recipe_created",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-02 02:53:32 UTC"
}
```

Recipe updated

```json
{
  "resource": {
    "name": "Trigger on a specified interval will send request via HTTP",
    "id": 32896,
    "type": "Flow"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "recipe_updated",
  "user": {
    "name": "john.smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:26:28 UTC"
}
```

Recipe deleted

```json
{
  "resource": {
    "parent_id": 32896,
    "name": "Send opportunity sync request via HTTP",
    "id": 33179,
    "type": "Flow"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "recipe_deleted",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:39:15 UTC"
}
```

Recipe cloned

```json
{
  "resource": {
    "name": "Trigger on a specified interval will send request via HTTP",
    "id": 32896,
    "type": "Flow"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "recipe_copied",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:32:43 UTC"
}
```

Recipe renamed

```json
{
  "resource_changes": {
    "name": {
      "old_value": "Send request via HTTP"
    }
  },
  "resource": {
    "parent_id": 32896,
    "name": "Send opportunity sync request via HTTP",
    "id": 33179,
    "type": "Flow"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "recipe_renamed",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:33:23 UTC"
}
```

Recipe started

```json
{
  "resource": {
    "parent_id": 32896,
    "name": "Send opportunity sync request via HTTP",
    "id": 33179,
    "type": "Flow"
  },
  "details": {
    "request": {
      "ip_address": "67.164.97.88",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    },
    "run_once": false
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "recipe_started",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:38:46 UTC"
}
```

Recipe stopped

```json
{
  "resource": {
    "parent_id": 32896,
    "name": "Send opportunity sync request via HTTP",
    "id": 33179,
    "type": "Flow"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    },
    "stop_reason": "user",
    "force": false,
    "error": false
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "recipe_stopped",
  "user": {
    "name": "Johm Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:39:06 UTC"
}
```

Folder created

```json
{
  "resource": {
    "path": "Home/RevOps Salesforce <> Netsuite",
    "name": "RevOps Salesforce <> Netsuite",
    "id": 6847,
    "type": "Folder"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "folder_created",
  "user": {
    "name": "Johm Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:48:08 UTC"
}
```

Folder deleted

```json
{
  "resource": {
    "path": "RevOps Salesforce <> Netsuite",
    "name": "RevOps Salesforce <> Netsuite",
    "id": 6847,
    "type": "Folder"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "folder_deleted",
  "user": {
    "name": "Johm Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:50:20 UTC"
}
```

Team - Invited a team member

```json
{
  "resource": {
    "role": "Admin",
    "name": "Alice Jackson",
    "id": 847,
    "type": "MemberInvitation",
    "email": "alice.jackson@workato.com"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "team_invitation_created",
  "user": {
    "name": "Johm Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:53:59 UTC"
}
```

Team - Member accepted invite

```json
{
  "resource": {
    "role": "Admin",
    "name": "Alice Jackson",
    "id": 847,
    "type": "MemberInvitation",
    "email": "alice.jackson@workato.com"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "team_invitation_accept",
  "user": {
    "name": "Alice Jackson",
    "id": 6464,
    "email": "alice.jackson@workato.com"
  },
  "timestamp": "2020-05-04 20:05:02 UTC"
}
```

Team - Member deleted

```json
{
  "resource": {
    "role": "Admin",
    "grant_type": "team",
    "member": {
      "email_confirmed_at": "2019-09-11 14:38:19 -0700",
      "name": "Nick Jefferies",
      "id": 4941,
      "type": "User",
      "email": "nick.jefferies@workato.com"
    },
    "id": 1483,
    "type": "ManagedUserGrant"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "team_membership_deleted",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 18:53:16 UTC"
}
```

Team - Switched teams

```json
{
  "resource": {
    "email_confirmed_at": "2019-11-24 14:29:30 -0800",
    "name": "John Smith",
    "id": 4848,
    "type": "User",
    "email": "johm.smith@workato.com"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0"
    },
    "activity": "switch_team"
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "user_login",
  "user": {
    "name": "Alice Jackson",
    "id": 6464,
    "email": "alice.jackson@workato.com"
  },
  "timestamp": "2020-05-04 20:27:33 UTC"
}
```

Team - Switched out of a team

```json
{
  "resource": {
    "email_confirmed_at": "2019-11-24 14:29:30 -0800",
    "name": "John Smith",
    "id": 4848,
    "type": "User",
    "email": "john.smith@workato.com"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0"
    },
    "activity": "switch_team"
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "user_logout",
  "user": {
    "name": "Alice Jackson",
    "id": 6464,
    "email": "alice.jackson@workato.com"
  },
  "timestamp": "2020-05-04 20:28:01 UTC"
}
```

Connection - Connected

```json
{
  "resource": {
    "provider": "postgresql",
    "authorized": true,
    "name": "My PostgreSQL account",
    "id": 7145,
    "type": "SharedAccount"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "connection_connected",
  "user": {
    "name": "Johm Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 20:56:35 UTC"
}
```

Connection - Disconnected

```json
{
  "resource": {
    "provider": "postgresql",
    "authorized": false,
    "name": "My PostgreSQL account",
    "id": 7145,
    "type": "SharedAccount"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "connection_disconnected",
  "user": {
    "name": "Johm Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 20:56:24 UTC"
}
```

Connection - Created

```json
{
  "resource": {
    "provider": "asana",
    "authorized": false,
    "name": "My second Asana account",
    "id": 7174,
    "type": "SharedAccount"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "connection_created",
  "user": {
    "name": "Johm Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 21:59:58 UTC"
}
```

Connection - Updated

```json
{
  "resource": {
    "provider": "postgresql",
    "authorized": false,
    "name": "My PostgreSQL account",
    "id": 7145,
    "type": "SharedAccount"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "connection_updated",
  "user": {
    "name": "Johm Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 20:56:32 UTC"
}
```

Connection - Deleted

```json
{
  "resource": {
    "provider": "greenhouse_connector_4805_1566279565",
    "authorized": false,
    "name": "Carly's Greenhouse Account",
    "id": 6588,
    "type": "SharedAccount"
  },
  "details": {
    "request": {
      "ip_address": "60.160.90.91",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "event": "connection_deleted",
  "user": {
    "name": "Johm Smith",
    "id": 4848,
    "email": "johm.smith@workato.com"
  },
  "timestamp": "2020-05-04 20:57:21 UTC"
}
```

Connector - Updated

```json
{
  "resource": {
    "name": "Greenhouse",
    "id": 1884,
    "type": "Adapter"
  },
  "team": {
    "name": "Workato Team",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "event": "connector_updated",
  "user": {
    "name": "John Smith",
    "id": 4848,
    "email": "john.smith@workato.com"
  },
  "timestamp": "2020-05-02 02:53:28 UTC"
}
```

Project - Deployments

```json
{
  "user_name": "Workato Root",
  "user_environment_id": 123456,
  "user_environment_type": "dev",
  "user_account_id": 123456,
  "user_account_name": "Workato Root",
  "team_id_d": 123456,
  "team_email": "acme@example.com",
  "team_name": "ACME",
  "team_environment_id": 123456,
  "team_environment_type": "dev",
  "team_account_id": 123456,
  "team_account_name": "Workato Root",
  "resource_type": "Deployment",
  "resource_id_d": 123456,
  "resource_project_name": "HR projects",
  "resource_target_environment": "Production",
  "resource_performed_by": "Workato Root",
  "timestamp": "2023-01-21 23:31:38 UTC"
}
```

On-prem group - Created

```json
{
  "log_id": "9002101:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_group_created",
  "details": {
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "curl/8.4.0"
    }
  },
  "resource": {
    "id": 41230,
    "name": "West Coast Prod Servers",
    "type": "SecureGatewayTunnel"
  },
  "timestamp": "2026-07-20 20:56:32 UTC",
  "api_client": {
    "id": 501234,
    "name": "On-prem management",
    "privilege_group": "On-prem admin"
  }
}
```

On-prem group - Renamed

```json
{
  "log_id": "9002115:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_group_renamed",
  "details": {
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "curl/8.4.0"
    }
  },
  "resource": {
    "id": 41230,
    "name": "West Coast Prod Servers",
    "type": "SecureGatewayTunnel"
  },
  "timestamp": "2026-07-21 09:14:02 UTC",
  "api_client": {
    "id": 501234,
    "name": "On-prem management",
    "privilege_group": "On-prem admin"
  },
  "resource_changes": {
    "name": {
      "new_value": "West Coast Prod Servers",
      "old_value": "West Coast Servers"
    }
  }
}
```

On-prem group - Setting updated

```json
{
  "log_id": "9002175:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_group_setting_updated",
  "details": {
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
  },
  "resource": {
    "id": 41230,
    "name": "West Coast Prod Servers",
    "type": "SecureGatewayTunnel"
  },
  "timestamp": "2026-07-22 11:02:47 UTC",
  "resource_changes": {
    "graceful_email_notifications": {
      "new_value": true,
      "old_value": false
    },
    "non_graceful_email_notifications": {
      "new_value": true,
      "old_value": false
    },
    "expired_certificate_email_notifications": {
      "new_value": true,
      "old_value": false
    }
  }
}
```

On-prem group - Deleted

```json
{
  "log_id": "9002140:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_group_deleted",
  "details": {
    "internal_details": {
      "agent_count": 3
    },
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "curl/8.4.0"
    }
  },
  "resource": {
    "id": 41230,
    "name": "West Coast Prod Servers",
    "type": "SecureGatewayTunnel"
  },
  "timestamp": "2026-08-01 16:40:19 UTC",
  "api_client": {
    "id": 501234,
    "name": "On-prem management",
    "privilege_group": "On-prem admin"
  }
}
```

`agent_count` contains the number of on-prem agents in the group at the time of deletion. Deleting a group also deletes all agents it contains. Each deleted agent emits its own `on_prem_agent_deleted` event.

On-prem agent - Created

```json
{
  "log_id": "9002108:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_agent_created",
  "details": {
    "group_name": "West Coast Prod Servers",
    "internal_details": {
      "group_id": 41230
    },
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "curl/8.4.0"
    }
  },
  "resource": {
    "id": 60870,
    "name": "us-west-agent-01",
    "type": "OnPremAgent"
  },
  "timestamp": "2026-07-20 21:03:11 UTC",
  "api_client": {
    "id": 501234,
    "name": "On-prem management",
    "privilege_group": "On-prem admin"
  }
}
```

On-prem agent - Activated

```json
{
  "log_id": "9002112:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_agent_activated",
  "details": {
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "GatewayHttpClient:1a2b3c4d5e6f7890abcd1234ef567890:60870:api"
    },
    "group_name": "West Coast Prod Servers",
    "internal_details": {
      "group_id": 41230,
      "system_action": true
    }
  },
  "resource": {
    "id": 60870,
    "name": "us-west-agent-01",
    "type": "OnPremAgent"
  },
  "timestamp": "2026-07-20 21:05:47 UTC",
  "resource_changes": {
    "state": {
      "new_value": "disconnected",
      "old_value": "awaiting_setup"
    }
  }
}
```

This event fires when an agent registers using an activation code. The `state` updates to `disconnected` rather than `connected` because the agent doesn't start automatically. Refer to [Run an on-prem agent](/en/on-prem/agents/run) to start an agent after activation.

Logs capture `state` transitions regardless of whether they're user-initiated or system-triggered.

On-prem agent - Renamed

```json
{
  "log_id": "9002151:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_agent_renamed",
  "details": {
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "curl/8.4.0"
    },
    "group_name": "West Coast Prod Servers",
    "internal_details": {
      "group_id": 41230
    }
  },
  "resource": {
    "id": 60870,
    "name": "us-west-agent-primary",
    "type": "OnPremAgent"
  },
  "timestamp": "2026-07-25 14:22:09 UTC",
  "api_client": {
    "id": 501234,
    "name": "On-prem management",
    "privilege_group": "On-prem admin"
  },
  "resource_changes": {
    "name": {
      "new_value": "us-west-agent-primary",
      "old_value": "us-west-agent-01"
    }
  }
}
```

On-prem agent - Disabled

```json
{
  "log_id": "9002181:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_agent_disabled",
  "details": {
    "group_name": "West Coast Prod Servers",
    "internal_details": {
      "group_id": 41230
    },
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
  },
  "resource": {
    "id": 60870,
    "name": "us-west-agent-primary",
    "type": "OnPremAgent"
  },
  "timestamp": "2026-07-30 08:17:53 UTC",
  "resource_changes": {
    "state": {
      "new_value": "disabled",
      "old_value": "connected"
    }
  }
}
```

Logs capture `state` transitions regardless of whether they're user-initiated or system-triggered.

On-prem agent - Enabled

```json
{
  "log_id": "9002188:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_agent_enabled",
  "details": {
    "group_name": "West Coast Prod Servers",
    "internal_details": {
      "group_id": 41230
    },
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
  },
  "resource": {
    "id": 60870,
    "name": "us-west-agent-primary",
    "type": "OnPremAgent"
  },
  "timestamp": "2026-07-30 09:02:41 UTC",
  "resource_changes": {
    "state": {
      "new_value": "syncing",
      "old_value": "disabled"
    }
  }
}
```

Logs capture `state` transitions regardless of whether they're user-initiated or system-triggered.

On-prem agent - Deleted

```json
{
  "log_id": "9002163:workato",
  "team": {
    "id": 512345,
    "name": "Kiran Patel's workspace",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "user": {
    "id": 512345,
    "name": "Kiran Patel",
    "email": "kiran.patel@example.com",
    "account_id": 512345,
    "external_id": null,
    "account_name": "Kiran Patel's workspace",
    "hq_account_id": 512345,
    "environment_id": 512345,
    "hq_account_name": "Kiran Patel's workspace",
    "environment_type": "dev"
  },
  "event": "on_prem_agent_deleted",
  "details": {
    "group_name": "West Coast Prod Servers",
    "internal_details": {
      "group_id": 41230
    },
    "request": {
      "ip_address": "203.0.113.10",
      "user_agent": "curl/8.4.0"
    }
  },
  "resource": {
    "id": 60870,
    "name": "us-west-agent-primary",
    "type": "OnPremAgent"
  },
  "timestamp": "2026-08-01 16:40:19 UTC",
  "api_client": {
    "id": 501234,
    "name": "On-prem management",
    "privilege_group": "On-prem admin"
  }
}
```

`group_name` and `group_id` describe the on-prem group the agent belonged to. Deleting a group also deletes all agents it contains. Each deleted agent emits its own `on_prem_agent_deleted` event.

### Example `log_message_str`

The following string is an example of `{{{log_message_str}}}` output, showing a `recipe_started` event:

```
"{\"event\":\"recipe_started\",\"details\":{\"run_once\":false,\"request\":{\"ip_address\":\"76.100.203.123\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36\"}},\"user\":{\"id\":1234567,\"external_id\":null,\"email\":\"example.user@workato.com\",\"name\":\"Example User\",\"environment_id\":1234567,\"environment_type\":\"dev\",\"account_id\":1234567,\"account_name\":\"Example User\"},\"team\":{\"id\":1234567,\"external_id\":null,\"email\":\"example.user@workato.com\",\"name\":\"Example User's team\",\"environment_id\":1234567,\"environment_type\":\"dev\",\"account_id\":1234567,\"account_name\":\"Example User\"},\"resource\":{\"type\":\"Flow\",\"id\":16983123,\"name\":\"Cat Fact Generator\",\"path\":\"Home/AI Testing\",\"folder_id\":9020123},\"timestamp\":\"2023-06-02 06:30:53 UTC\"}"
```

## Audit log streaming types

Workato enables you to stream various log types. The following examples display the JSON structures for different log types that you can [stream to external destinations](/en/features/activity-audit-log-streaming-destinations):

- [Job status only](#job-status-only)
- [Full job details](#full-job-details)
- [User activity](#user-activity)
- [Workato Log events](#log-events)
- [Genie conversation events](#genie-conversations)

### Job status only

This log type captures whether each job has succeeded or failed, excluding log lines.

```json
{
    "source": "Workato Dev Environment",
    "UserID": "12345",
    "log": {
        "id": "job-000001",
        "master_job_id": "master-job-000001",
        "recipe_id": "98765",
        "calling_job_id": null,
        "calling_recipe_id": null,
        "root_job_handle": "",
        "root_recipe_id": 0,
        "title": "Scheduler by Workato: new recurring event: Scheduled time=2024-03-11T21:01:44.621606-03:00, Scheduled day=Monday, and Scheduled week=10",
        "status": "succeeded",
        "is_repeat": true,
        "is_test": false,
        "is_test_case_job": false,
        "started_at": "2024-03-11T17:02:31-07:00",
        "completed_at": "2024-03-11T17:02:32-07:00",
        "repeat_count": 1,
        "action_count": 1,
        "parent_id": null,
        "flow_id": "12345-flow",
        "error_type": null,
        "is_poll_error": false,
        "account_id": "67890",
        "account_name": "HR account",
        "environment_type": "dev",
        "environment_id": "12345-env",
        "hq_account_id": null,
        "hq_account_name": "HR Workspace",
        "error": null,
        "report": {
            "custom_column_0": "2024-03-11T20:56:44.000Z",
            "custom_column_1": "Some Text",
            "custom_column_2": "2024-03-13T17:02:32.631Z",
            "custom_column_3": "test:2024-03-11T21:01:44.621606-03:00"
        },
        "context": {
            "user_id": "54321",
            "user_name": "Alex Nur",
            "user_email": "alex@example.com",
            "recipe_id": "98765",
            "recipe_url": "https://workato.com/recipes/98765",
            "recipe_name": "Employee onboarding",
            "recipe_path": "Home/Collaborator Test",
            "job_id": "job-000001",
            "master_job_id": "master-job-000001",
            "calling_recipe_id": null,
            "calling_job_id": null,
            "root_job_handle": "",
            "root_recipe_id": 0,
            "is_repeat": true,
            "is_test": false,
            "repeat_count": 1,
            "job_url": "https://workato.com/recipes/98765/job/job-000001",
            "job_created_at": "2024-03-11T17:02:31-07:00",
            "repeated_job": true,
            "parent_job_id": "master-job-000001",
            "user_external_id": "external-12345"
        }
    },
    "log_message": "Log message content anonymized for example purposes."
}
```

### Full job details

This log includes comprehensive details for all job executions, including complete log lines such as statuses, individual actions, and line statistics.

```json
{
  "source": "Workato Dev Environment",
  "Env": "ACME_OEM",
  "Time": "2023-09-07 02:07:15.979 -0800 AKDT",
  "Time_utc": 1694081235979,
  "Time_micro": 1694081235979000,
  "Time_nano": 1694081235979000000,
  "Log": {
    "id": "j-1234ABC",
    "master_job_id": "j-5678DEF",
    "recipe_id": 654321,
    "calling_job_id": null,
    "calling_recipe_id": null,
    "root_job_handle": "",
    "root_recipe_id": 0,
    "job_url": "https://workato.example.com/recipes/654321/job/j-1234ABC",
    "title": "Scheduler by Workato: new recurring event: Scheduled time=2023-09-07T02:07:13.217909-08:00, Scheduled day=Thursday, and Scheduled week=36",
    "status": "succeeded",
    "is_repeat": false,
    "is_test": false,
    "is_test_case_job": false,
    "started_at": "2023-09-07T03:07:15-07:00",
    "completed_at": "2023-09-07T03:07:15-07:00",
    "repeat_count": 0,
    "action_count": 1,
    "parent_id": null,
    "flow_id": 123456,
    "error_type": null,
    "account_id": 1111,
    "account_name": "ACME Admin (OEM)",
    "environment_type": "dev",
    "environment_id": 5432,
    "hq_account_id": 0,
    "hq_account_name": "",
    "error": null,
    "report": {},
    "lines": [
      {
        "input": { "time_unit": "minutes", "trigger_every": "5" },
        "output": {
          "last_job_time": "2023-09-07T02:02:13.000000-08:00",
          "scheduled_day": "Thursday",
          "scheduled_month": "September",
          "scheduled_time": "2023-09-07T02:07:13.217909-08:00",
          "scheduled_week": 36
        },
        "adapter_name": "clock",
        "adapter_operation": "scheduled_event",
        "recipe_line_number": 0,
        "mask_data": false
      },
      {
        "input": {
          "message": "Test:2023-09-07T02:02:13.000000-08:00",
          "user_logs_enabled": "false"
        },
        "output": { "message": "Test:2023-09-07T02:02:13.000000-08:00" },
        "adapter_name": "logger",
        "adapter_operation": "log_message",
        "recipe_line_number": 1,
        "mask_data": false
      }
    ],
    "context": {
      "user_id": 12345,
      "user_name": "Ariel Quinn",
      "user_email": "ariel@example.com",
      "recipe_id": 654321,
      "recipe_url": "https://workato.example.com/recipes/654321",
      "recipe_name": "Data processing task",
      "recipe_path": "Home",
      "user_external_id": null
    }
  },
  "Log_Str": "{\"id\":\"j-1234ABC\",\"master_job_id\":\"j-5678DEF\",\"recipe_id\":654321,\"calling_job_id\":null,\"calling_recipe_id\":null,\"title\":\"Scheduler by Workato: new recurring event: Scheduled time=2023-09-07T02:07:13.217909-08:00, Scheduled day=Thursday, and Scheduled week=36\",\"status\":\"succeeded\",\"is_repeat\":false,\"is_test\":false,\"is_test_case_job\":false,\"started_at\":\"2023-09-07T03:07:15-07:00\",\"completed_at\":\"2023-09-07T03:07:15-07:00\",\"repeat_count\":0,\"action_count\":1,\"parent_id\":null,\"flow_id\":123456,\"error_type\":null,\"is_poll_error\":false,\"account_id\":1111,\"account_name\":\"ACME Admin (OEM)\",\"environment_type\":\"dev\",\"environment_id\":5432,\"hq_account_id\":0,\"hq_account_name\":\"\",\"error\":null,\"report\":{},\"lines\":[{\"input\":{\"time_unit\":\"minutes\",\"trigger_every\":\"5\"},\"output\":{\"last_job_time\":\"2023-09-07T02:02:13.000000-08:00\",\"scheduled_day\":\"Thursday\",\"scheduled_month\":\"September\",\"scheduled_time\":\"2023-09-07T02:07:13.217909-08:00\",\"scheduled_week\":36},\"adapter_name\":\"clock\",\"adapter_operation\":\"scheduled_event\",\"context\":{\"user_id\":12345,\"user_name\":\"Ariel Quinn\",\"user_email\":\"ariel@example.com\",\"recipe_id\":654321,\"recipe_url\":\"https://workato.example.com/recipes/654321\",\"recipe_name\":\"Data processing task\",\"recipe_path\":\"Home\",\"job_id\":\"j-1234ABC\",\"master_job_id\":\"j-5678DEF\",\"calling_recipe_id\":null,\"calling_job_id\":null,\"is_repeat\":false,\"is_test\":false,\"repeat_count\":0,\"job_url\":\"https://workato.example.com/recipes/654321/job/j-1234ABC\",\"job_created_at\":\"2023-09-07T03:07:15-07:00\",\"repeated_job\":false,\"parent_job_id\":null,\"user_external_id\":null}}"
}
```

#### Duplicate entries removed from full job details

Effective September 2024, the format of full job details will change to eliminate duplicate entries.

These entries include:

- `line_stat`
- `context.repeated_job`
- `context.job_created_at`
- `context.job_id`
- `context.master_job_id`
- `context.calling_recipe_id`
- `context.calling_job_id`
- `context.is_repeat`
- `context.repeated_count`
- `parent_id`
- `context.parent_job_id`

### User activity

This log type records all user activities within your Workato workspace, providing insights into user interactions and any changes made within this particular environment.

```json
{
    "source": "Workato Dev Environment",
    "UserID": "99999",
    "log": {
        "event": "recipe_stopped",
        "details": {
            "error": false,
            "stop_reason": "user"
        },
        "user": {
            "id": 99999,
            "external_id": "ext-98765",
            "email": "taylor@example.com",
            "name": "Taylor Cruz",
            "environment_id": 88888,
            "environment_type": "dev",
            "account_id": 77777,
            "account_name": "HR workspace"
        },
        "team": {
            "id": 55555,
            "external_id": "team-ext-12345",
            "email": "team-operations@example.com",
            "name": "Operations team",
            "environment_id": 88888,
            "environment_type": "dev",
            "account_id": 77777,
            "account_name": "Global operations division"
        },
        "resource": {
            "type": "Flow",
            "id": 123456,
            "name": "Sample Logger",
            "path": "Home/Example Path",
            "folder_id": 654321
        },
        "timestamp": "2024-03-12 00:06:33 UTC"
    },
    "log_message": "{\"event\":\"recipe_stopped\",\"details\":{\"error\":false,\"stop_reason\":\"user\"},\"user\":{\"id\":99999,\"external_id\":\"ext-98765\",\"email\":\"user@example.com\",\"name\":\"Random User\",\"environment_id\":88888,\"environment_type\":\"dev\",\"account_id\":77777,\"account_name\":\"Random Account\"},\"team\":{\"id\":55555,\"external_id\":\"team-ext-12345\",\"email\":\"team@example.com\",\"name\":\"Random Team\",\"environment_id\":88888,\"environment_type\":\"dev\",\"account_id\":77777,\"account_name\":\"Team Account\"},\"resource\":{\"type\":\"Flow\",\"id\":123456,\"name\":\"Sample Logger\",\"path\":\"Home/Example Path\",\"folder_id\":654321},\"timestamp\":\"2024-03-12 00:06:33 UTC\"}"
}
```

### Workato Log events

This log type contains information from the [Workato logging service](/en/features/logging-service#workato-logging-service). For example:

- User-defined messages
- Polling and webhook trigger errors
- OPA, Workflow app, MCP Server, and Data pipeline events

User-defined messages

```json
{
  "adapter": "logger",
  "source": "job",
  "log_level": "INFO",
  "job_handle": "j-AYGYrdPt-CoQaFe-B6",
  "date_time": "2026-03-02T10:38:45.968Z",
  "user_id": 32443,
  "flow_id": 507206,
  "project_id": 37163,
  "line_number": 3,
  "log_entry_sequence": 1,
  "operation": "Log message",
  "data": "{\"input\":{},\"output\":{\"message\":\"This is an example log using Logger by Workato\"}}"
}
```

Trigger errors

```json
{
  "source": "webhook",
  "log_level": "ERROR",
  "date_time": "2026-03-02T08:45:15.379Z",
  "user_id": 32443,
  "data": "{\"message\":\"Error accepting webhook event\",\"http_code\":404,\"url\":\"/webhooks/rest/c4034159-c62e-49d7-ab79-7d5192293a2c/event\",\"method\":\"POST\",\"count\":1,\"last_error_seen_at\":\"2026-03-02T08:40:15.219Z\",\"aggregation_window_start\":\"2026-03-02T08:40:15.219Z\",\"aggregation_window_end\":\"2026-03-02T08:45:15.219Z\"}"
}
```

OPA events

```json
{
  "agent": "logging4",
  "agent_id": 31237,
  "source": "opa",
  "log_level": "INFO",
  "on_prem_group": "kafka",
  "on_prem_group_id": 3821,
  "date_time": "2026-03-19T06:41:16.025Z",
  "user_id": 16468,
  "log_entry_sequence": 11784,
  "data": "{\"message\":\"SAP subscriptions monitor started.\",\"logger\":\"com.workato.agent.sap.SapReceiverHub\"}"
}
```

Workflow app events

```json
{
  "source": "lcap",
  "log_level": "ERROR",
  "date_time": "2026-03-02T17:15:03.140Z",
  "user_id": 32443,
  "lcap_app_uid": "zTthn6xz1qgyteks7Row",
  "lcap_user_uid": "945hPemr4MMYCrJ7YNUusD",
  "data": "{\"message\":\"An error has occurred on the page: \\\"Widget configuration error\\\"\",\"debug_info\":[\"\\\"Button\\\" widget\",\"Handler for click event\"],\"events_count\":1,\"is_public_page\":false,\"page_path\":\"blank-page\"}"
}
```

MCP Server events

```json
{
  "source": "apim-mcp-gateway",
  "log_level": "INFO",
  "job_handle": "j-AYETNJfP-xYGrB6-B6",
  "date_time": "2026-02-26T11:23:29.694Z",
  "user_id": 32443,
  "flow_id": 477766,
  "log_entry_sequence": 1,
  "data": "{\"message_type\":\"tool_call\",\"environment_id\":32443,\"auth_method\":\"token\",\"ip_address\":\"192.0.2.255\",\"user_agent\":\"Ruby\",\"request_id\":\"ad29825db1224a53b77d4b6c71159abc\",\"server_name\":\"CarData - MCP Server Auto Test\",\"duration_seconds\":2.734584499,\"details\":{\"input\":\"{\\\"make\\\":\\\"Subaru\\\",\\\"model\\\":\\\"Impreza\\\"}\",\"method\":\"tools/call\",\"name\":\"Search_CarData_by_make_and_model\",\"output\":\"{\\\"car_data\\\":{\\\"make\\\":\\\"Subaru\\\",\\\"model\\\":\\\"Impreza\\\",\\\"year\\\":1999,\\\"price\\\":70000.0,\\\"is_sold\\\":false}}\",\"succeeded\":true}}"
}
```

Data pipeline events

```json
{
  "source": "data-pipeline-conductor",
  "log_level": "INFO",
  "job_handle": "dpr-AYEXsoer-BARdJk-B6#019c9a41-ceff-7889-9dcc-5db023c97dea",
  "date_time": "2026-02-26T14:02:16.000Z",
  "user_id": 32443,
  "project_id": 35489,
  "log_entry_sequence": 4,
  "pipeline_event_type": "OBJECT_RUN_CANCEL",
  "pipeline_id": "dpr-AYEXsoer-BARdJk-B6",
  "pipeline_workato_id": 0,
  "pipeline_sync_id": "019c9a41-9cb9-74e1-8310-f3d554f32006",
  "pipeline_object_name": "test",
  "pipeline_object_run_id": "019c9a41-ceff-7889-9dcc-5db023c97dea",
  "operation": "test#OBJECT_RUN_CANCEL",
  "data": "{\"context\":{\"event\":\"OBJECT_RUN_CANCEL\",\"start_time\":\"2026-02-26T14:02:08.303Z\",\"end_time\":\"2026-02-26T14:02:16.366Z\",\"pipeline_id\":\"dpr-AYEXsoer-BARdJk-B6\",\"workato_pipeline_id\":0,\"pipeline_sync_id\":\"019c9a41-9cb9-74e1-8310-f3d554f32006\",\"object_run_id\":\"019c9a41-ceff-7889-9dcc-5db023c97dea\",\"source\":\"GOOGLE_DRIVE-68412\",\"destination\":\"SNOWFLAKE-83875\",\"duration\":\"8 seconds\",\"object_name\":\"test\"},\"error_message\":\"Running pipeline was stopped by user\",\"sync_mode\":\"INCREMENTAL_MERGE\"}"
}
```

### Genie conversation events

This log type records user interactions with an Agent Studio [genie](/en/agentic/agent-studio). The logger captures each step in a conversation as a separate entry with a shared `genie_run_id` and `conversation_id`. You can use these shared properties to stitch steps into runs and conversations.

LLM call started

The `llm_call_started` event logs when the genie sends a prompt to the LLM.

The `stage` field indicates the position in the run:

- `USER_QUERY` is the first call.
- `MID_EXECUTION` is a subsequent call after a tool result is returned.
- `AGENT_RESPONSE` is the final call that produces the user-facing reply.

```json
{
  "event_id": "15a0bcec-afaf-421a-8a8c-877679e6f86c",
  "event_type": "llm_call_started",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "conversation_id": "conversation-01KS34RAWWDJ00EQBA6M5FNYGY",
  "genie_run_id": "95ce2c49-de8f-418e-9818-2f648e15aff2",
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "request_id": "00-e999dfff564597e0e7d45e19d5857ba6-08ab45fa94da0d05-01",
  "date_time": "2026-05-20T16:51:03.14646Z",
  "data": {
    "message": "How do I back up my data?",
    "conversation_history": [
      {
        "type": "system",
        "content": "You are an AI Agent System with the sole purpose of following user instructions.\nYour Instructions:\n\n**What's my job?**\nYou are an IT support assistant. You help users resolve common IT issues and answer questions about internal systems and policies. Your goal is to provide efficient and accurate support to ensure smooth IT operations.\n\n**Who will need my help?**\nEmployees and staff members who encounter IT issues or have questions about internal systems and policies will need your assistance. IT managers may also rely on you to log and track support tickets.\n\n**How do I get things done?**\nWhen a user asks an IT support question, search the knowledge base for relevant answers and respond with clear, step-by-step guidance. When a user asks to log, submit, or create a support ticket, use the \"Log support ticket\" skill to record their issue. Ask for their name if they haven't provided it. When a user shares a file or attachment, read and analyze its contents and summarize or describe what you find.\n\n**What should I avoid?**\nAvoid providing technical solutions that are not verified or beyond your scope. Do not share sensitive information or access unauthorized systems. Avoid making promises about resolution times that you cannot guarantee.\n\n**What results do you want me to track?**\nTrack the number of resolved issues, the average response time, and user satisfaction scores. Monitor the number of support tickets logged and ensure they are addressed promptly.\n\n**How should I talk to people?**\nCommunicate clearly and professionally. Use simple language for non-technical users and provide detailed explanations when necessary. Be patient and empathetic, especially when users are frustrated.\n\n**Any extra tips?**\nKeep the knowledge base updated with new solutions and common issues. Regularly review and refine your responses to improve clarity and effectiveness. Stay informed about updates to internal systems and policies.\n1. DO NOT attempt to aggregate data (count, sum, average, etc.) across large datasets. This includes:\n   - Knowledge base documents\n   - Database query results with more than 5-10 items\n   - Any dataset where you cannot see all relevant entries in your context window\n\n2. When a user requests data aggregation:\n   - If the data is small (10 or fewer distinct items) and fully visible in your context, you may perform the aggregation\n   - If the data exceeds this limit, DO NOT attempt the aggregation\n\n3. When declining to perform aggregation on large datasets:\n   - Clearly explain: \"I cannot reliably aggregate this data as I may have incomplete information\"\n   - Suggest alternatives: \"Instead, I can help you analyze specific examples or provide information about individual items\"\n   - Offer to assist with a more targeted query\n\n4. Be transparent about your limitations:\n   - Acknowledge that attempting to aggregate incomplete data could lead to incorrect conclusions\n   - Explain that you can only work with what's visible in your current context\n<full message sent to LLM but truncated to 3K characters in logs>",
        "truncated": true,
        "tool_calls": null
      },
      {
        "type": "human",
        "content": "How do I back up my data?\n\n# Attached context\n\nCurrent time: Wednesday, May 20, 2026 at 04:51:01 PM UTC",
        "truncated": false,
        "tool_calls": null
      }
    ]
  },
  "app_type": "slack",
  "stage": "USER_QUERY",
  "llm_call_id": "e66e3132-241f-4ccb-b2ec-fe1418a0fbc5",
  "call_result": "SUCCESS"
}
```

LLM call completed

The `llm_call_completed` event logs when the genie receives a response from the LLM:

```json
{
  "event_id": "3d62f9ed-586b-4f1d-9eca-eb728f429341",
  "event_type": "llm_call_completed",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "conversation_id": "conversation-01KS34RAWWDJ00EQBA6M5FNYGY",
  "genie_run_id": "95ce2c49-de8f-418e-9818-2f648e15aff2",
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "request_id": "00-e999dfff564597e0e7d45e19d5857ba6-08ab45fa94da0d05-01",
  "date_time": "2026-05-20T16:51:05.935356Z",
  "data": {
    "message": "",
    "tool_calls": [
      {
        "name": "enterprise_search",
        "args": {
          "query": "How do I back up my data?",
          "knowledge_base_names": [
            "IT FAQ"
          ]
        }
      }
    ]
  },
  "app_type": "slack",
  "stage": "MID_EXECUTION",
  "llm_call_id": "e66e3132-241f-4ccb-b2ec-fe1418a0fbc5",
  "model_name": "bedrock/claude-sonnet-4-6",
  "input_tokens": 3412,
  "output_tokens": 113,
  "call_result": "SUCCESS"
}
```

Genie run start

The `genie_run_start` event logs when a genie run begins. The fields present depend on how the run was triggered.

**User-initiated run** (`genie_run_trigger: "user"`)

```json
{
  "event_id": "1da5cd9e-ffdd-435b-a4dd-0faee02c4c38",
  "event_type": "genie_run_start",
  "workspace_id": 52718,
  "environment_id": 52718,
  "genie_id": "2341",
  "date_time": "2026-05-20T16:51:02.55Z",
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "conversation_id": "conversation-01KS34RAWWDJ00EQBA6M5FNYGY",
  "genie_run_id": "95ce2c49-de8f-418e-9818-2f648e15aff2",
  "app_type": "slack",
  "genie_run_trigger": "user",
  "first_run_in_conversation": true,
  "test_run": false
}
```

**Recipe-triggered run** (`genie_run_trigger: "genie_task"`)

Four additional fields appear when the **Assign task to Genie** recipe action triggers a genie run:

- `genie_executor`
- `genie_executor_id`
- `genie_executor_related_id`
- `call_stack`

```json
{
  "event_id": "94dd2c8f-5c19-4eae-a604-1ef86a07cb52",
  "event_type": "genie_run_start",
  "workspace_id": 52718,
  "environment_id": 52718,
  "genie_id": "2341",
  "date_time": "2026-05-28T19:39:21.403Z",
  "identity_user_id": "5XwUVCPmbmjWxBbRrt7X2D",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "conversation_id": "conversation-01KSR1JDQMT001AWVTPMTRJ3K8",
  "genie_run_id": "1a11ce5f-f04f-44a3-8dd7-818d24fc3ce1",
  "app_type": "genie_task",
  "genie_run_trigger": "genie_task",
  "first_run_in_conversation": true,
  "test_run": false,
  "genie_executor": "genie_task_source_recipe",
  "genie_executor_id": "j-AaJL4YeN-FNdEnW-B6",
  "genie_executor_related_id": "1658592",
  "call_stack": [
    "2341:1a11ce5f-f04f-44a3-8dd7-818d24fc3ce1"
  ]
}
```

Genie run finish

The `genie_run_finish` event logs when a genie run ends:

```json
{
  "event_id": "ea984e0f-77cf-4a1d-bfdc-322c235e5acc",
  "event_type": "genie_run_finish",
  "workspace_id": 52718,
  "environment_id": 52718,
  "genie_id": "2341",
  "date_time": "2026-05-20T16:51:20.116Z",
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "conversation_id": "conversation-01KS34RAWWDJ00EQBA6M5FNYGY",
  "genie_run_id": "95ce2c49-de8f-418e-9818-2f648e15aff2",
  "first_run_in_conversation": true,
  "test_run": false
}
```

Topic assigned

The `topic_assigned` event logs when the genie classifies the user's message and assigns it to a relevant topic.

`genie_run_id` returns `"unknown"` for this event, because topic assignment occurs before the run ID is established in the event pipeline. Use `conversation_id` and `request_id` to correlate it with other events in the same run.

```json
{
  "event_id": "04b12c52-ec5b-4651-b54f-e4cf0b335905",
  "event_type": "topic_assigned",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "conversation_id": "conversation-01KS34RAWWDJ00EQBA6M5FNYGY",
  "genie_run_id": "unknown",
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "request_id": "00-e999dfff564597e0e7d45e19d5857ba6-08ab45fa94da0d05-01",
  "date_time": "2026-05-20T16:51:14.369385Z",
  "data": "Data backup using OneDrive",
  "app_type": "slack"
}
```

User message

The `user_message` event logs when a user sends a message:

```json
{
  "event_id": "fbc9ee11-70b6-4092-b7f5-21309a84e221",
  "event_type": "user_message",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "conversation_id": "conversation-01KS34RAWWDJ00EQBA6M5FNYGY",
  "genie_run_id": "95ce2c49-de8f-418e-9818-2f648e15aff2",
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "request_id": "00-e999dfff564597e0e7d45e19d5857ba6-08ab45fa94da0d05-01",
  "date_time": "2026-05-20T16:51:03.117732Z",
  "data": {
    "message": "How do I back up my data?",
    "context": {
      "file_paths": [],
      "files": null,
      "location": null,
      "workato_context": null,
      "timestamp": "Wednesday, May 20, 2026 at 04:51:01 PM UTC",
      "author": null
    },
    "metadata": {}
  },
  "app_type": "slack"
}
```

Guardrail evaluation

The `guardrail_evaluated` event logs when input or output guardrails are checked:

```json
{
  "event_id": "667f689a-0cf2-422f-92d4-0f556edae59c",
  "event_type": "guardrail_evaluated",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "conversation_id": "conversation-01KS34RAWWDJ00EQBA6M5FNYGY",
  "genie_run_id": "95ce2c49-de8f-418e-9818-2f648e15aff2",
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "request_id": "00-e999dfff564597e0e7d45e19d5857ba6-08ab45fa94da0d05-01",
  "date_time": "2026-05-20T16:51:03.128767Z",
  "data": {
    "results": [
      {
        "policy_type": "harmful_content",
        "action": "passed",
        "direction": "input",
        "execution_time_ms": 397.645614000794,
        "findings": [],
        "severity": null,
        "evaluated_step_id": "e66e3132-241f-4ccb-b2ec-fe1418a0fbc5"
      },
      {
        "policy_type": "prompt_attack",
        "action": "passed",
        "direction": "input",
        "execution_time_ms": 312.3382350004249,
        "findings": [],
        "severity": null,
        "evaluated_step_id": "e66e3132-241f-4ccb-b2ec-fe1418a0fbc5"
      }
    ],
    "response_message": null
  },
  "app_type": "slack"
}
```

System message

The `system_message` event logs when the genie responds to the user and invokes a tool at the same time. The event is absent when the LLM invokes a tool without a user-facing message.

```json
{
  "event_id": "c98b17e1-7fe3-45b4-91a6-0770b0613061",
  "event_type": "system_message",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "conversation_id": "conversation-01KSQXJBK9RGRBPTWWSFQEMQFQ",
  "genie_run_id": "e8963ba1-7310-4c92-8941-c0d53a6213bb",
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "request_id": "00-3d21f3b0d836c95b9e8ec595c747202f-4a971e3fdc8871eb-01",
  "date_time": "2026-05-28T18:29:32.203154Z",
  "data": "I'll log that support ticket for you right away!",
  "app_type": "slack",
  "tool_call_id": "tooluse_A2RpFpCllAFFF2ivljZi1X",
  "tool_name": "Log support ticket",
  "tool_description": "Use this skill when the user wants to log, submit, or create a support ticket. Extract the user's name and a brief description of their issue from the conversation.",
  "tool_type": "EXTERNAL",
  "call_result": "SUCCESS"
}
```

Tool execution started

The `tool_execution_started` event logs when the genie begins executing a tool.

The shape of `data`, which contains the arguments passed to the tool, varies based on the tool used.

`external_tool_ids` appears on both `BUILTIN` and `EXTERNAL` events:

- In `BUILTIN` events it contains a UUID.
- In `EXTERNAL` events it contains the recipe identifier in `recipe:<id>` format.

```json
{
  "event_id": "32665b99-3a5f-4bb0-a883-40aac15aad0d",
  "event_type": "tool_execution_started",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "conversation_id": "conversation-01KS34RAWWDJ00EQBA6M5FNYGY",
  "genie_run_id": "95ce2c49-de8f-418e-9818-2f648e15aff2",
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "request_id": "00-e999dfff564597e0e7d45e19d5857ba6-08ab45fa94da0d05-01",
  "date_time": "2026-05-20T16:51:05.968881Z",
  "data": {
    "query": "How do I back up my data?",
    "knowledge_base_names": [
      "IT FAQ"
    ]
  },
  "app_type": "slack",
  "tool_call_id": "tooluse_sdDMAh6qWShfw7XIOcbjUi",
  "tool_name": "enterprise_search",
  "tool_description": "\n## Enterprise Search Tool\nYou have access to a tool named `enterprise_search`. This tool allows you to search for information across various knowledge bases within the organization.\n\nUse this tool to search for information across the organization's knowledge bases before answering questions.\n\nThis tool is useful when you need to:\n- Find specific information in documents, wikis, or other enterprise content\n- Research company-specific topics\n- Look up policies, procedures, or documentation\n\n## Parameters:\n- `query`: The search query (required) - question the user asks to find relevant information. Always use a well formed short question for query.\n- `knowledge_base_names`: A list of knowledge base names to filter the search (optional). Use the exact names from the available knowledge bases list. If not possible to determine, use empty array []\n\n## Usage Guidelines:\n- Always use a well formed short question for query.\n- Be very specific and use only specific context from the conversation when query is formulated.\n- Use knowledge base names (not IDs) when filtering. Match names exactly as shown in the available knowledge bases list.\n\n## Tool response format (knowledge_fragments):\nThe tool returns a list of results in `knowledge_fragments`. Each fragment has:\n- `document_id`, `title`, `url`, `content`\nUse `title` and `url` for citations; use `content` for the passage text.\nWhen `content` contains multiple passages from the same document, they are labeled with `[Passage 1]`, `[Passage 2]`, etc. These labels are not part of the source document—only the text after each label is the actual excerpt. Do not quote or treat the labels as document content; use the text that follows each label when answering.\n\n## Handling User Queries:\nWhen a user asks a question:\n- Formulate well formed short question based on the user's question.\n- Determine if knowledge base names are applicable based on descriptions or names of available knowledge bases.\n- Call the `enterprise_search` tool with your formulated query.\n- Analyze the search results and compose a response to the user's question.\n- If the search doesn't yield relevant results, explain this to the user and suggest a refined query.\n\n## Example:\n```json\n{\n    \"query\": \"What are the incentive fees?\",\n    \"knowledge_base_names\": [\"Internal Policies\", \"kb_fees\", \"General Information\"]\n}\n```\n",
  "tool_type": "BUILTIN",
  "external_tool_ids": [
    "e7b294b7-be96-4361-b2af-043d4b251540"
  ],
  "call_result": "SUCCESS"
}
```

Tool execution completed

The `tool_execution_completed` event logs when the genie finishes executing a tool.

The `data` field shape varies by `tool_type`:

- `BUILTIN` tools return results in `artifact.knowledge_fragments`.
- `EXTERNAL` skill calls return a JSON-encoded string in `message`.

**Knowledge base search (BUILTIN)**

The `[Passage 1]` label in `content` is an internal passage marker, not part of the source document. Excerpts from the same document are labeled `[Passage 1]`, `[Passage 2]`, and so on.

```json
{
  "event_id": "fc979af5-6c44-4838-bc95-f9a0d99829c5",
  "event_type": "tool_execution_completed",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "conversation_id": "conversation-01KS34RAWWDJ00EQBA6M5FNYGY",
  "genie_run_id": "95ce2c49-de8f-418e-9818-2f648e15aff2",
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "request_id": "00-e999dfff564597e0e7d45e19d5857ba6-08ab45fa94da0d05-01",
  "date_time": "2026-05-20T16:51:06.792985Z",
  "data": {
    "message": null,
    "artifact": {
      "knowledge_fragments": [
        {
          "document_id": "1lrNyRTpddxSc2t_QCimKYoVxKyAJDwqRo30cwZqXfX4",
          "title": "IT FAQ",
          "url": null,
          "content": "[Passage 1]\nTitle: IT FAQ\n\nHow do I back up my files? All files saved to your OneDrive folder are automatically backed up. Avoid saving important files to the desktop or local Downloads folder."
        }
      ]
    }
  },
  "app_type": "slack",
  "tool_call_id": "tooluse_sdDMAh6qWShfw7XIOcbjUi",
  "tool_name": "enterprise_search",
  "tool_type": "BUILTIN",
  "call_result": "SUCCESS"
}
```

**Recipe skill (EXTERNAL)**

For `EXTERNAL` skill calls, `message` is a JSON-encoded string. Parse it to access the structured output from the skill.

```json
{
  "event_id": "c6e63073-2584-4527-b4ed-746696dc342b",
  "event_type": "tool_execution_completed",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "conversation_id": "conversation-01KSJPZNN9ZCJ4CKP4R53223HX",
  "genie_run_id": "e5929bae-750c-4ef6-8f26-888dddd5bc2c",
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "request_id": "00-59adf691336c3fb3e4f0fc0db1f9a46f-21ca607eb3911b5b-01",
  "date_time": "2026-05-26T17:58:24.892012Z",
  "data": {
    "message": "{\"Confirmation\":\"Ticket successfully created for Alex\"}",
    "artifact": null
  },
  "app_type": "slack",
  "tool_call_id": "tooluse_l525qY8mmydN1vJurIWpb1",
  "tool_name": "Log support ticket",
  "tool_type": "EXTERNAL",
  "call_result": "SUCCESS"
}
```

Skill run

The `genie_skill_run` event logs when a genie uses a skill.

`job_id` contains the recipe job ID you can use to look up the corresponding recipe job log for end-to-end traceability. This event pairs with the `tool_execution_started` and `tool_execution_completed` events that share the same `tool_call_id`.

```json
{
  "event_id": "e88a1dc7-28e9-4534-8a14-5969fa312e88",
  "event_type": "genie_skill_run",
  "workspace_id": 52718,
  "environment_id": 52718,
  "genie_id": "2341",
  "date_time": "2026-05-26T17:58:21.535Z",
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "conversation_id": "conversation-01KSJPZNN9ZCJ4CKP4R53223HX",
  "genie_run_id": "e5929bae-750c-4ef6-8f26-888dddd5bc2c",
  "app_type": "slack",
  "first_run_in_conversation": false,
  "test_run": false,
  "tool_call_id": "tooluse_l525qY8mmydN1vJurIWpb1",
  "job_id": "j-AaHGJpoK-n3dWo9-B6",
  "event_ts": "2026-05-26T17:58:21.465Z"
}
```

Structured output formatting started

The `structured_output_formatting_started` event logs when the genie begins formatting its LLM response to conform to a JSON schema. This occurs when an **Assign task to Genie** recipe action has custom output fields.

```json
{
  "event_id": "d055f354-882b-4350-b6f4-4c333ae1ae37",
  "event_type": "structured_output_formatting_started",
  "date_time": "2026-05-13T13:34:35.653011Z",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "genie_run_id": "dcda0a4d-decc-4092-a6f8-fba4d4b1c36b",
  "conversation_id": "conversation-01KRGRQN8DP5MR8Y4D33K5CPCJ",
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "app_type": "genie_task",
  "request_id": "00-6e6d1dfc66633621c2c807d43a344cd3-f6e1213b0a8c6a1a-01",
  "data": {
    "message": "Based on the details provided, this appears to be a hardware or performance-related issue. The laptop takes approximately 5 minutes to boot, which suggests possible causes such as too many startup applications, a near-capacity hard drive, insufficient RAM, or malware activity. I would classify this as a Medium priority issue — the user can still work but is experiencing significant disruption to productivity. Category: Hardware / Performance, Priority: Medium.",
    "output_schema": "{\"type\":\"object\",\"properties\":{\"Category\":{\"type\":\"string\"},\"Priority\":{\"type\":\"string\"},\"Summary\":{\"type\":\"string\"}},\"required\":[\"Category\",\"Priority\",\"Summary\"]}"
  }
}
```

Structured output formatting completed

The `structured_output_formatting_completed` event logs when the genie finishes formatting its LLM response to conform to a JSON schema. This occurs when an **Assign task to Genie** recipe action has custom output fields.

```json
{
  "event_id": "ff4dde2b-53c2-43fd-9ef3-5679f5f4f27d",
  "event_type": "structured_output_formatting_completed",
  "date_time": "2026-05-13T13:34:36.147033Z",
  "chat_type": "GENIE",
  "workspace_id": 52718,
  "environment_id": 52718,
  "genie_id": "2341",
  "genie_handle": "gin-GgDdAaLX-sYHkWn-B2",
  "genie_run_id": "dcda0a4d-decc-4092-a6f8-fba4d4b1c36b",
  "conversation_id": "conversation-01KRGRQN8DP5MR8Y4D33K5CPCJ",
  "identity_user_id": "9Af5GRAXR4wB1u4ZFSqZ8E",
  "app_type": "genie_task",
  "request_id": "00-6e6d1dfc66633621c2c807d43a344cd3-f6e1213b0a8c6a1a-01",
  "data": {
    "message": "{\"Category\":\"Hardware / Performance\",\"Priority\":\"Medium\",\"Summary\":\"The user is experiencing significant performance degradation on their laptop, including a very slow boot time of approximately 5 minutes, possibly caused by several common endpoint issues.\"}"
  }
}
```

Genie user feedback

The `user_feedback` event logs when the user provides feedback. `user_feedback_reaction` can be `positive` or `negative`. `user_feedback_reaction_comment` only contains a value when the user chooses to provide a comment.

```json
{
	"event_id": "e7ef29f4-af1e-4724-b6f8-3eca66ad0a00",
	"event_type": "user_feedback",
	"workspace_id": 51395,
	"environment_id": 51395,
	"genie_id": "7438",
	"date_time": "2026-07-21T08:00:39.264Z",
	"identity_user_id": "nLvaG8PdzirjTS662KzmW3",
	"genie_handle": "gin-AagWJwHm-QLTYDT-B6",
	"conversation_id": "conversation-01KXZY461EA1GH37CJ4T8CPVAD",
	"genie_run_id": "a99329ad-a99d-4b90-92f0-f634ab1556f8",
	"app_type": "slack",
	"first_run_in_conversation": false,
	"test_run": false,
	"event_ts": "2026-07-21T08:00:35.882Z",
	"user_feedback_reaction": "positive",
	"user_feedback_reaction_comment": "A thoughtful answer",
	"client_id": "ginct-AagXsbbH-W6aWkH-B6"
}
```

---
