---
url: >-
  https://docs.workato.com/en/api-mgmt/api-recipes/action-response-to-api-request.md
description: >-
  Reference for the Respond to API request action in Workato API recipes, which
  ends the job and sends the HTTP response defined by the New API request
  trigger.
---

# API platform by Workato - Respond to API request action

The **Respond to API request** action ends the current job and sends an HTTP response defined by the [New API request](/en/api-mgmt/api-recipes/trigger-new-api-request) trigger.

> **ACCESS REQUIREMENTS**
> 
> API recipes require access to the [API Platform](/en/api-management) feature. Contact your Customer Success Manager if you don't have access to the **Platform > API platform** page in Workato.

## Input

The fields for this action define how the endpoint responds to API requests:

| Input fields | Description |
| --- | --- |
| **Response** | Defines the type of the response. The options in this menu are determined by the responses defined in the recipe's New API request trigger. |
| **Response headers** | Defines the header used by the response. Only present if defined in the recipe's New API request trigger. |
| **Response body** | Defines the schema of the body used by the response. Only present if defined in the recipe's New API request trigger. |

## Output

| Output fields | Description |
| --- | --- |
| **Context** | Metadata about the API request. This field has the following subfields:
| Output fields | Description |
| --- | --- |
| **Calling IP address** | The IP address of the client calling this recipe as a REST endpoint. |
| **Access profile** | Details about the access profile used to perform the request. |
| **API client** | Contains details about the API client used to perform the request. |
| **JWT claims** | Only available if a JWT token is used. Contains details about the JWT claims used to authenticate the request. |
| **Request headers** | Details about the request headers defined for the endpoint. For each request header defined for the endpoint, a datapill will be created. | |
| **Request body** | Details about the properties defined for the endpoint's **Request body**. For each property, a datapill will be created. |
| **Request parameters** | Legacy group. Details about the properties defined for the endpoint's legacy **Request schema**. For each property, a datapill will be created. |

## Additional Resources

- [API Platform](/en/api-management)
- [API recipes](/en/api-mgmt/api-recipes/)
- [Create an API recipe](/en/api-mgmt/api-recipes/walkthrough)
- [New API request trigger](/en/api-mgmt/api-recipes/trigger-new-api-request)
