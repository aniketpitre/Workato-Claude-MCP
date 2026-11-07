---
url: 'https://docs.workato.com/en/connectors/percolate/custom-action.md'
description: >-
  The Custom action in the Percolate connector lets you build and send a custom
  HTTP request to the Percolate API and parse the JSON response.
---

# Percolate - Custom action

The **Custom action** allows you to build and execute an HTTP request with your Percolate connection.

![Custom action in Percolate](/assets/custom-action.BtgdwoMT.png)_Percolate - Custom action_

## Input

| Input field | Description |
| --- | --- |
| Request type | Select the HTTP method of the request, such as `POST`, `GET`, `PUT`, or `DELETE`. |
| Path | Define the API endpoint path to append to the base URI. Use an absolute URI to override the base URI if necessary. |
| URL parameters | Add any required URL parameters to refine the API call. |
| Request body parameters | For actions like `POST` or `PATCH` that modify data, define the JSON structure of the data payload. |

## Output

The output for this object depends on how you define the output structure to correctly parse the JSON response from the Percolate API.

---
