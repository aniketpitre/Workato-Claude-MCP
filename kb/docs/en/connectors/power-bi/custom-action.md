---
url: 'https://docs.workato.com/en/connectors/power-bi/custom-action.md'
description: >-
  The Custom action allows you to build and execute an HTTP request with your
  Power BI connection.
---

# Power BI - Custom action

The **Custom action** allows you to build and execute an HTTP request with your Power BI connection.

## Input

| Input field | Description |
| --- | --- |
| Request type | Select the HTTP method of the request, such as POST, GET, PUT, or DELETE. |
| Path | Define the API endpoint path to append to the base URI. Use an absolute URI to override the base URI if necessary. |
| URL parameters | Add any required URL parameters to refine the API call. |
| Request body parameters | Enter the JSON payload for POST or PATCH requests. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---
