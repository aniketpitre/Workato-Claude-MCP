---
url: 'https://docs.workato.com/en/connectors/azure-ad/custom-action.md'
description: Build your own Microsoft Entra ID action with an HTTP request.
---

# Microsoft Entra ID - Custom action

The **Custom action** enables you to create a Microsoft Entra ID action with an HTTP request. You can authorize the request with your Microsoft Entra ID (Azure Active Directory) connection. Refer to the [Microsoft Entra ID API documentation](https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0) for more information.

## Input

| Input field | Description |
| --- | --- |
| Request type | Select the HTTP method of the request, such as POST, GET, PUT, or DELETE. |
| Path | Define the API endpoint path to append to the base URI. Use an absolute URI to override the base URI if necessary. |
| URL parameters | Add any required URL parameters to refine the API call. |
| Request body parameters | Enter the JSON structure of the data payload for POST or PATCH actions. |

## Output

Define the expected schema of the HTTP response to determine the output. Map the relevant datapill from the datatree to use the output in downstream steps.

---
