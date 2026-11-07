---
url: 'https://docs.workato.com/en/connectors/creatio/custom-action.md'
description: >-
  The Custom action allows you to build and execute an HTTP request with your
  Creatio connection.
---

# Creatio - Custom action

The **Custom action** allows you to build and execute an HTTP request with your Creatio connection.

![Creatio Custom action](/assets/creatio-custom-action.kt_UwBcf.png)_Creatio custom action_

## Input

| Input fields | Description |
| --- | --- |
| Request type | Select the HTTP method of the request, such as POST, GET, PUT, or DELETE. |
| Path | Define the API endpoint path to append to the base URI. Use an absolute URI to override the base URI if necessary. |
| URL parameters | Add any required URL parameters to refine the API call. |
| Request body parameters | For actions like POST or PATCH that modify data, define the JSON structure of the data payload. |

## Output

The output for this action depends on how you define the expected schema of the HTTP response. To use them in downstream steps, map the relevant datapill from the data tree.

---
