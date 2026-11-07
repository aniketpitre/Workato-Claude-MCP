---
url: 'https://docs.workato.com/en/workato-api/pubsub.md'
description: >-
  Reference for the Workato Event streams public API to publish single messages,
  publish batches, and consume messages from event topics.
---

# Event streams public API

The Event streams public API provides endpoints to **publish and consume messages** from [event topics](/en/connectors/pubsub). This API is separate from the [Event streams Developer API](/en/workato-api/event-streams), which lets you manage event topics.

Each message in a topic includes an ID you can use as an offset. You must store either the **Message ID** or **Last message timestamp** to use these endpoints.

For more information, refer to the OpenAPI specification at `/api/v1/openapi.json` on the [base URL](#base-url) for your data center.

### Base URL

The base URL for the Event streams public API depends on the [data center](/en/datacenter/datacenter-overview) where your Workato account is hosted. These URLs apply only to endpoints for publishing and consuming messages.

### Workato Enterprise customers

- US Data Center: `https://event-streams.workato.com`
- EU Data Center: `https://event-streams.eu.workato.com`
- JP Data Center: `https://event-streams.jp.workato.com`
- SG Data Center: `https://event-streams.sg.workato.com`
- AU Data Center: `https://event-streams.au.workato.com`
- IL Data Center: `https://event-streams.il.workato.com`
- CN Data Center: `https://event-streams.workatoapp.cn`
- KR Data Center: `https://event-streams.kr.workato.com`
- UK Data Center: `https://event-streams.uk.workato.com`

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service Data Center: `https://event-streams.trial.workato.com`

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This page provides general guidance for all Workato users. If you're a Virtual Private Workato (VPW) customer, refer to your private documentation for detailed configuration guidance specific to your instances.

> **API DOMAIN AND NAMESPACE DIFFERENCES FOR EVENT STREAMS**
> 
> The Event streams APIs are divided into two categories. Each category uses a different domain and namespace.
> 
> #### Public API
> 
> The following endpoints use the [event-streams domain](#base-url):
> 
> - **Consume messages** `POST /api/v1/topics/:topic_id/consume`
> - **Publish a message** `POST /api/v1/topics/:topic_id/publish`
> - **Publish a batch of messages** `POST /api/v1/batch/topics/:topic_id/publish`
> 
> #### Developer API
> 
> The following endpoints use the standard [Developer API base URL](/en/workato-api#base-url):
> 
> - **List topics** `GET /api/event_streams/topics`
> - **Create a topic** `POST /api/event_streams/topics`
> - **Get a topic by ID** `GET /api/event_streams/topics/:topic_id`
> - **Update a topic** `PUT /api/event_streams/topics/:topic_id`
> - **Purge a topic** `PUT /api/event_streams/topics/:topic_id/purge`
> - **Delete a topic** `DELETE /api/event_streams/topics/:topic_id`
> 
> Refer to the [Event streams Developer API](/en/workato-api/event-streams) documentation for more information.

## Rate limits

Event streams developer API resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Event streams public API](/en/workato-api/pubsub.html) endpoints | 60 requests per minute |

Additionally, Event streams public API resources have the following payload quota:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Event streams public API](/en/workato-api/pubsub.html) endpoints | Maximum payload size:​ 10 MB |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v1/topics/:topic\_id/consume](/en/workato-api/pubsub#consume-messages) | Consume messages from a topic. |
| POST | [/api/v1/topics/:topic\_id/publish](/en/workato-api/pubsub#publish-message) | Publish a message to a topic. |
| POST | [/api/v1/batch/topics/:topic\_id/publish](/en/workato-api/pubsub#publish-a-batch-of-messages) | Publish a batch of messages to a topic. |

## Consume messages

Retrieve messages from the topic. This resource provides the option to retrieve all messages within the topic or, by including parameters in the request body, to fetch messages after a specified ID or timestamp. The response is limited to a maximum of 50 messages in each batch.

> **BATCH SIZE IS A MAXIMUM**
> 
> `batch_size` sets the maximum number of messages the response returns. Workato also caps each batch at 50 MB of total payload, so the response can include fewer messages when individual payloads are large. Workato returns the remaining messages in later requests. The request and response formats don't change.

You can enable long polling mode by setting the `timeout_secs` parameter. In this mode, the API returns available messages instantly. If there are no messages, the API waits for a maximum of `timeout_secs` seconds. If a new message appears within this timeframe, it is instantly returned; otherwise, the API provides an empty list after the call times out.

<api-code no-copy-method>

```
POST https://YOUR_EVENT_STREAMS_DC/api/v1/topics/:topic_id/consume
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| topic\_id | **integer** _required_ | Event topic ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| after\_message\_id | **string** _optional_ | Message ID. The service returns all messages after the message with the specified ID. The ID must correspond to a message that exists in the topic. |
| since\_time | **string** _optional_ | Timestamp in RFC 3339 format. The service returns all messages after the timestamp specified. The current time is used if the `since_time` value is a time in the future. |
| batch\_size | **integer** _optional_ | Maximum batch size to return. The maximum value is 50. Returns batch of 50 messages if not specified. Workato may return fewer than `batch_size` messages when individual payloads are large. |
| timeout\_secs | **integer** _optional_ | Maximum timeout for long polling. The maximum value is 60. The default value is 0. When 0, long polling is disabled. |

> **USING SINCE\_TIME PARAMETER**
> 
> We recommend using `after_message_id` to control the topic message cursor. `since_time` should only be used for the first request (to poll messages from a specific timestamp without polling the whole topic), or if you need to re-retrieve messages from the topic. Using `since_time`, especially in combination with batch publish and long polling, doesn't guarantee message order and can lead to skipped messages.

#### Sample request

<api-code>

```shell
curl  -X POST "https://YOUR_EVENT_STREAMS_DC/api/v1/topics/:topic_id/consume" \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      --data '{"after_message_id": ":after_message_id"}'
```

</api-code>

### Response

```json
{
    "messages": [
        {
            "message_id": "A12y",
            "payload": {
                "Name": "Jane",
                "Surname": "Doe"
            },
            "time": "2023-04-14T15:07:14.437+00:00"
        },
        {
            "message_id": "A12z",
            "payload": {
                "Name": "John",
                "Surname": "Doe"
            },
            "time": "2023-04-14T15:43:40.227+00:00"
        }
    ]
}
```

## Publish message

Publish a message to a topic. The message must comply with the topic schema.

<api-code no-copy-method>

```
POST https://YOUR_EVENT_STREAMS_DC/api/v1/topics/:topic_id/publish
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| topic\_id | **integer** _required_ | Event topic ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
|  | **JSON** _required_ | Message to publish to the topic. The message must comply with the [topic schema](/en/connectors/pubsub/pubsub-schema-config). |

#### Sample request

<api-code>

```shell
curl  -X POST "https://YOUR_EVENT_STREAMS_DC/api/v1/topics/:topic_id/publish" \
      -H 'Authorization: Bearer <api_token>' \
      --data '{":field_name_1": ":field_value_1", ":field_name_2": ":field_value_2"}'
```

</api-code>

### Response

```json
{
  "message_id": "A1BRi"
}
```

## Publish a batch of messages

Publish a batch of messages to a topic. The messages must comply with the topic schema.

<api-code no-copy-method>

```
POST https://YOUR_EVENT_STREAMS_DC/api/v1/batch/topics/:topic_id/publish
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| topic\_id | **integer** _required_ | Event topic ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| payloads | **Array of JSON** _required_ | Array of messages to publish to the topic. The messages must comply with the [topic schema](/en/connectors/pubsub/pubsub-schema-config). The maximum array size is 100. |

#### Sample request

<api-code>

```shell
curl  -X POST "https://YOUR_EVENT_STREAMS_DC/api/v1/batch/topics/:topic_id/publish" \
      -H 'Authorization: Bearer <api_token>' \
      --data '{"payloads":[{":field_name_1": ":field_value_1a", ":field_name_2": ":field_value_2a"},
      {":field_name_1": ":field_value_1b", ":field_name_2": ":field_value_2b"}]}'
```

</api-code>

### Response

```json
{
  "is_partial_error": false,
  "message_ids": {
    "0": {
      "message_id": "A1DFi",
      "result": "success"
    },
    "1": {
      "message_id": "A1DL8",
      "result": "success"
    }
  }
}
```

---
