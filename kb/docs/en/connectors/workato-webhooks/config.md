---
url: 'https://docs.workato.com/en/connectors/workato-webhooks/config.md'
description: >-
  The New event via HTTP webhook trigger in the Webhooks connector runs recipe
  actions when incoming webhook events are received.
---

# Webhooks - New event via HTTP webhook trigger

The **New event via HTTP webhook** trigger executes recipe actions when webhooks are received. This trigger doesn't process webhooks when a recipe is stopped.

## Input

| Input field | Description |
| --- | --- |
| Event name | Enter the name of the event this webhook trigger is listening to. This name is used to create the unique URI for your webhook trigger. |
| Payload configuration | Expand this field to manually configure the payload you expect from the webhook event. |
| Webhook type | Select the [type](#webhook-types) that matches the incoming webhooks. You can select from the following list. |
| Payload schema | Describe the fields that you expect to receive from the webhook event. If you use the webhooks wizard, the schema is automatically generated using the sample webhook event as a template. Otherwise, you must add each field to the schema manually. You must define this field when using the following webhook types: **GET request**, **PUT/POST with JSON payload**, **PUT/POST with XML payload**, **PUT/POST with FORM encoded payload**. |
| Query params | Describe the query parameters you expect from the webhook event. |
| Headers | Describe the headers that you expect from the webhook event. Headers are automatically generated if you use the webhooks wizard, using the sample webhook event as a template. Otherwise, there are two ways to configure this input field. The easier way is to use a sample JSON to generate all the fields at once. Alternatively, you can add each field individually. |

> **ARRAY PAYLOADS**
> 
> If a webhook event's payload is a JSON array, Workato wraps it in an `array` field when you generate the **Payload schema** from a sample JSON array. Reference the `array` field in your recipe to access the payload's list of items.

> **DEDUPLICATION HEADERS**
> 
> The `X-Workato-Dedup` header is an optional webhook header that can be added for any incoming webhook events.
> 
> The `X-Workato-Dedup` header allows you to prevent duplicate webhook events from creating duplicate jobs in Workato. If supplied, Workato verifies that this event's `X-Workato-Dedup` header value hasn't been seen before for this recipe before creating a job. This is useful for custom systems that guarantee an "at least once" delivery of events.

### Webhook types

You can select the following options as the **Webhook type**:

- GET request
- PUT/POST with JSON payload
- PUT/POST with XML payload
- PUT/POST with FORM encoded payload
- PUT/POST with raw binary data
- PUT/POST with unicode text data

## Output

| Output field | Description |
| --- | --- |
| Headers | This output object contains datapills of all the headers that you can expect from the webhook events calling this recipe. To add missing headers, add a field in the **Headers** input field. |
| Payload | This output object contains datapills matching the data that you can expect from the webhook events calling this recipe. To add or edit these fields, update the **Payload schema** input field. |

## Webhook response

Webhook triggers respond to events with a `200` response code and a JSON payload of `{"status":"ok"}` by default. Here is an example:

```shell
$ curl 'https://www.workato.com/webhooks/rest/b48a7c64-a7dd-4185-936b-ada1ca84e9fd/foobar' -i

HTTP/1.1 200 OK
Date: Wed, 28 Jul 2021 10:03:18 GMT
Content-Type: application/json; charset=utf-8
Connection: keep-alive
Server: nginx
Vary: Origin
X-Request-Id: 0b6d7f2ffbfab278c685080aed91d690
X-Correlation-Id: 0b6d7f2ffbfab278c685080aed91d690
Strict-Transport-Security: max-age=31536000; includeSubDomains

{"status":"ok"}
```

  

> **WEBHOOK VALIDATIONS**
> 
> - Workato performs validations on JSON based webhooks - denoted by your defined `Webhook type`, to ensure that the payload is valid JSON. Otherwise, Workato responds with 400 bad request.
> - Workato performs validations on JSON/Form/XML/Unicode text based webhooks - denoted by your defined `Webhook type`, to ensure that the payload is UTF-8 compatible. Otherwise, Workato responds with 400 bad request. If your payload is UTF-8 incompatible, use the `Raw Binary Data` option for `Webhook Type`

## Custom responses

In some situations, the webhook client requires a different structure in one or more parts of the HTTP response. To achieve that, the webhooks connector supports query parameters to change the default response structure.

| Query parameter | Accepted values | Description |
| --- | --- | --- |
| workato\_response\_code | Only 2XX codes. Default is \`200\`. | Returns a different response status code. For example, `201` or `204`.
> 204 NO CONTENT RESPONSE CODE The `204` response code implies that the response body is empty. This takes precedence and overrides `workato_empty_response=false`.

 |
| workato\_empty\_response | `true`/`false` (default) | Returns an empty response body instead of `{"status":"ok"}` |

The following example uses `workato_response_code=201` to return `201 Created` as the HTTP response code:

```shell
$ curl 'https://www.workato.com/webhooks/rest/b48a7c64-a7dd-4185-936b-ada1ca84e9fd/custom-code?workato_response_code=201' -i

HTTP/1.1 201 Created
Date: Wed, 28 Jul 2021 10:05:03 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 15
Connection: keep-alive
Server: nginx
Vary: Origin
X-Request-Id: b23380f48d02c38fa761e8afa4b94862
X-Correlation-Id: b23380f48d02c38fa761e8afa4b94862
Strict-Transport-Security: max-age=31536000; includeSubDomains

{"status":"ok"}
```

## Where can I find a connector's static webhook URI?

Complete the following steps to find a custom connector's static webhook URI:

1. Navigate to **Tools > Connector SDK**.
   
2. Select the connector you plan to use.
   
3. Go to **Source code** and click the **Test code** tab.
   
4. Expand the **Static webhook URI** section and copy the provided URI:
   
   ![Connector webhook URI](/assets/connector-webhook-url.DVweeIka.png)_Connector webhook URI_

---
