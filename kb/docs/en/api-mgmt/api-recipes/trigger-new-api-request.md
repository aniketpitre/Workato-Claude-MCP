---
url: 'https://docs.workato.com/en/api-mgmt/api-recipes/trigger-new-api-request.md'
description: >-
  Reference for the New API request trigger in API recipes, covering request and
  response content type, headers, and schema inputs.
---

# API platform by Workato - New API request trigger

The **New API request** trigger defines the request and response structure for a [recipe endpoint](/en/api-mgmt/api-recipes/) and creates a job when it receives an API request.

> **ACCESS REQUIREMENTS**
> 
> API recipes require access to the [API Platform](/en/api-management) feature. Contact your Customer Success Manager if you don't have access to the **Platform > API platform** page in Workato.

## Input

Input fields in the **Request** section define the structure of API requests to the endpoint:

| Input fields | Description |
| --- | --- |
| **Content type** | Defines the data format of the request. Choose `application/json`, `text/plain` or `multipart/form-data`. Use `multipart/form-data` to upload large attachments (up to 5GB). |
| **Request header** | Defines the parameters request headers must have. |
| **Path parameters** | Defines the parameters to accept in the endpoint path for `JSON` and `Text/XML` requests. |
| **Query parameters** | Defines the parameters to accept in the endpoint's query string for `JSON` and `Text/XML` requests. |
| **Request structure** | Defines the outermost structure of the request body: a single `Object`, or a top-level array, such as an `Array of objects`, `Array of strings`, `Array of integers`, `Array of numbers`, `Array of booleans`, `Array of dates`, or `Array of date-times`. Defaults to `Object`. |
| **Request body** | Only appears when Request structure is set to `Object` or `Array of objects`, and when the legacy Request schema is empty. Defines the expected schema request bodies must have. Datapills for these fields appear in the Request body group. |
| **Request schema** | Legacy field that remains fully supported. Appears in recipes that defined a request schema before the Request body field was available. Defines the expected schema request bodies must have. Datapills for these fields appear in the Request parameters group and show as deprecated. Clear this field to define the Request body field instead. |

Input fields in the **Response** section define the structure of responses the endpoint sends:

| Input fields | Description |
| --- | --- |
| **Content type** | Defines the data format of the response. Defaults to JSON if left blank. |
| **Response header** | Defines the parameters response headers will have. |
| **Responses** | Defines the possible responses to a request sent to the endpoint. This field has the following subfields:
| Input fields | Description |
| --- | --- |
| **Name** | The name of the response. For example: Unauthorized or Created |
| **Code** | The HTTP status code to be associated with the response which identifies the type of response. For example: Unauthorized responses are associated with 401 status codes. |
| **Response structure** | Defines the outermost structure of the response body: a single Object, or a top-level array, such as an Array of objects, Array of strings, Array of integers, Array of numbers, Array of booleans, Array of dates, or Array of date-times. Defaults to Object. |
| **Response schema** | Only appears when Response structure is set to Object or Array of objects. Defines the expected schema response bodies will have. |

 |

> **PROCESSING BINARY CONTENT**
> 
> Multipart data may contain binary data, including images and pdf files. You must ensure that these files are in utf-8 encoding format. Workato recipe string processing supports utf-8.

## Output

| Output fields | Description |
| --- | --- |
| **Context** | Metadata about the API request. This field has the following subfields:
| Output fields | Description |
| --- | --- |
| **Calling job ID** | The ID of the job associated with the request. |
| **Calling recipe ID** | If called from a recipe, the ID of the recipe that sent the request. |
| **Calling IP address** | The IP address of the client calling this recipe as an endpoint. |
| **Access profile** | Details about the access profile used to perform the request. |
| **API client** | Contains details about the API client used to perform the request. |
| **JWT claims** | Only available if a JWT token is used. Contains details about the JWT claims used to authenticate the request. | |
| **Request** | Contains details about the request's content type and body. This field has the following subfields:

| Output fields | Description |
| --- | --- |
| **Content type** | Applicable only if the request's Content type is Raw. The `Content-Type` header value from the request. |
| **Request body (raw)** | Applicable only if the request's Content type is `Raw`. The full, raw body of the request. |
| **Request body (JSON)** | Applicable only if the request's Content type is `JSON`. A JSON object containing all the fields defined in the Request body field or the legacy Request schema field. | |
| **Request body** | Contains a datapill for each field defined in the Request body field. This group represents the list of items in the request body when Request structure is set to an array type. |
| **Request parameters** | Legacy group. Contains a datapill for each field defined in the legacy Request schema. When Request structure is set to an array type, this group also includes **List size** and **List index** datapills for use inside a loop over the request body's items. |

## Additional Resources

- [API Platform](/en/api-management)
- [API recipes](/en/api-mgmt/api-recipes/)
- [Create an API recipe](/en/api-mgmt/api-recipes/walkthrough)
- [Response to API request action](/en/api-mgmt/api-recipes/action-response-to-api-request)

---

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

---
