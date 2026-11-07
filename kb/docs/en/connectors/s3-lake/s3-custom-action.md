---
url: 'https://docs.workato.com/en/connectors/s3-lake/s3-custom-action.md'
description: >-
  The Custom action in the S3 Data Lake connector lets you make authorized HTTP
  requests to AWS Glue or S3 Data Lake APIs for advanced use cases.
---

# S3 Data Lake - Custom action

The **Custom action** enables you to make authorized HTTP requests to AWS Glue or S3 Data Lake APIs. This enables you to implement advanced use cases not directly supported by prebuilt actions.

![S3 Data Lake – Custom action](/assets/s3-custom-action.8O3EVzK8.png)_S3 Data Lake – Custom action_

## Input

| Input field | Description |
| --- | --- |
| Action name | Enter a name that describes the purpose of the custom action, such as `create job` or `delete table`. |
| Method | Select the HTTP method to use for the request (`GET`, `POST`, `PUT`, `PATCH`, `OPTIONS` or `DELETE`). |
| Path | Provide the request path to append to the base URI. Use absolute URI to override the base URI if needed. |
| Request type | Choose the structure for sending data. Use `JSON request body` for most AWS Glue and S3 API requests. |
| Response type | Choose how the response should be parsed. Use `JSON response` to extract output fields. |
| Request body parameters | Define key-value pairs or objects to send in the body of the request (`POST`/`PUT`). |
| Request headers | Add headers such as `Content-Type: application/json` if required by the API. |
| Response body | Describe the expected fields from the response. Use the **Use JSON** button to parse fields automatically. |
| Response headers | Optionally define the structure of headers returned in the response. |

## Output

The output fields depend on your **Response body** configuration. Workato parses the fields you configure for downstream use in your recipe.

---
