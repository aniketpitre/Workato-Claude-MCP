---
url: 'https://docs.workato.com/en/connectors/openapi/custom-action.md'
description: >-
  The Custom action allows you to build and execute an HTTP request with your
  OpenAPI connection.
---

# OpenAPI - Custom action

The **Custom** action allows you to build and execute an HTTP request with your OpenAPI connection.

![Custom action](/assets/openapi-custom-action.Z43lD8xd.png)_Custom action_

## Input

| Input fields | Description |
| --- | --- |
| Request type | Select the HTTP method of the request, such as POST, GET, PUT, or DELETE. |
| Path | Define the API endpoint path to append to the base URI. Use an absolute URI to override the base URI if necessary. |
| URL parameters | Add any required URL parameters to refine the API call. |
| Request body parameters | Define the JSON structure of the data payload for actions that modify data, such as POST or PATCH. |

## Output

The output for this action depends on how you define the expected schema of the HTTP response. To use them in downstream steps, map the relevant datapill from the data tree.

---
