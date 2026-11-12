---
url: 'https://docs.workato.com/en/workato-api/event-streams.md'
description: >-
  Reference for the Workato event streams API to publish and consume messages
  and create, list, update, purge, and delete event topics.
---

# Developer API - Event streams

The following endpoints enable you to manage [event topics](/en/connectors/pubsub).

> **API DOMAIN AND NAMESPACE DIFFERENCES FOR EVENT STREAMS**
> 
> The Event streams APIs are divided into two categories. Each category uses a different domain and namespace.
> 
> #### Public API
> 
> The following endpoints use the [event-streams domain](/en/workato-api/pubsub#base-url):
> 
> - **Consume messages** `POST /api/v1/topics/:topic_id/consume`
> - **Publish a message** `POST /api/v1/topics/:topic_id/publish`
> - **Publish a batch of messages** `POST /api/v1/batch/topics/:topic_id/publish`
> 
> Refer to the [Event streams public API](/en/workato-api/pubsub) documentation for more information.
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

## Rate limits

Event streams developer API resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Event streams](/en/workato-api/event-streams.html) endpoints | 60 requests per minute |

Additionally, Event streams developer API resources have the following payload quota:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Event streams](/en/workato-api/event-streams.html) endpoints | Maximum payload size:​ 1 MB |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/event\_streams/topics](/en/workato-api/event-streams#list-topics) | Retrieve a list of topics. |
| POST | [/api/event\_streams/topics](/en/workato-api/event-streams#create-a-topic) | Create a topic. |
| GET | [/api/event\_streams/topics/:topic\_id](/en/workato-api/event-streams#get-topic-by-id) | Get topic by ID. |
| PUT | [/api/event\_streams/topics/:topic\_id](/en/workato-api/event-streams#update-a-topic) | Update a topic. |
| PUT | [/api/event\_streams/topics/:topic\_id/purge](/en/workato-api/event-streams#purge-a-topic) | Purge a topic. |
| DELETE | [/api/event\_streams/topics/:topic\_id](/en/workato-api/event-streams#delete-a-topic) | Delete a topic. |

> **BEST PRACTICE**
> 
> For endpoints that modify topics ([create](#create-a-topic) and [update](#update-a-topic)), we recommend that you define parameters in the request body instead of the URL.

## List topics

Retrieves a list of event topics, with optional filtering, sorting, and the ability to include topic schemas in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/event_streams/topics
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Filters event topics by a case-sensitive title. Supports partial matching, which means you can search for fragments of the title. |
| sort | **string** _optional_ | Defines how to sort the results. Options include `activity` (most recent activity first), `name`, and `id`. Set to `id` by default. |
| include\_schema | **boolean** _optional_ | When set to `true`, the schema of each event topic is included in the response payload. Set to `false` by default. |

### Sample request

This request retrieves event topics that contain the keyword `Order` within the name. The results are sorted by event topic ID, and the schema for each event topic is included in the response payload.

<api-code>

```shell
curl  -X GET "https://YOUR_DATA_CENTER/api/event_streams/topics?name=:name_value&sort=:sort_value&include_schema=:include_schema_value" \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "count": 2,
    "data": [
        {
            "id": 334525,
            "name": "Order placed",
            "folder_id": 986754,
            "created_at": "2024-09-25T09:47:54.089-07:00",
            "updated_at": "2024-09-25T09:47:54.089-07:00",
            "retention": 604800,
            "schema": [
                {
                    "control_type": "text",
                    "label": "Order ID",
                    "name": "OrderId",
                    "optional": false,
                    "type": "string"
                },
                {
                    "control_type": "text",
                    "label": "Customer ID",
                    "name": "CustomerId",
                    "optional": false,
                    "type": "string"
                },
                {
                    "control_type": "text",
                    "label": "Amount",
                    "name": "Amount",
                    "optional": false,
                    "type": "string"
                },
                {
                    "control_type": "date",
                    "label": "Order date",
                    "name": "OrderDate",
                    "optional": false,
                    "parse_output": "date_conversion",
                    "render_input": "date_conversion",
                    "type": "date_time"
                }
            ],
            "description": "Triggered when a new order is placed."
        },
        {
            "id": 334526,
            "name": "Order shipped",
            "folder_id": 986754,
            "created_at": "2024-09-25T09:51:12.130-07:00",
            "updated_at": "2024-09-25T09:51:12.130-07:00",
            "retention": 604800,
            "schema": [
                {
                    "control_type": "text",
                    "label": "Order ID",
                    "name": "OrderId",
                    "optional": false,
                    "type": "string"
                },
                {
                    "control_type": "text",
                    "label": "Shipping carrier",
                    "name": "ShippingCarrier",
                    "optional": false,
                    "type": "string"
                },
                {
                    "control_type": "text",
                    "label": "Tracking number",
                    "name": "TrackingNumber",
                    "optional": false,
                    "type": "string"
                },
                {
                    "control_type": "date",
                    "label": "Shipped date",
                    "name": "ShippedDate",
                    "optional": false,
                    "parse_output": "date_conversion",
                    "render_input": "date_conversion",
                    "type": "date_time"
                }
            ],
            "description": "Triggered when an order is shipped."
        }
    ]
}
```

## Create a topic

Creates a new event topic.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/event_streams/topics
```

</api-code>

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name of the new topic. Topic names must be unique within a folder. |
| folder\_id | **number** _optional_ | The ID of the folder or project to store the topic inside. By default, Workato places the topic in your workspace's **Event Streams Topics** project, creating that project if it doesn't already exist. |
| schema | **array** _required_ | The schema definition for the new topic. Must adhere to a valid Workato schema format. |
| schema\[control\_type\] | **string** _required_ | The control type for a field in the topic schema. |
| schema\[label\] | **string** _required_ | The label that appears for the field in the topic schema. |
| schema\[name\] | **string** _required_ | The name identifier for the field in the topic schema. |
| schema\[optional\] | **boolean** _required_ | Specifies whether the field is optional. |
| schema\[type\] | **string** _required_ | The data type of the field in the schema. |
| retention | **number** _optional_ | Retention time for the topic in seconds. Defaults to 168 hours (604,800 seconds) if not specified. |
| description | **string** _optional_ | A description of the new topic. |

> **DEFAULT ACCESS FOR API TOPICS**
> 
> Topics that you create through the Developer API are accessible only to the workspace owner by default. The workspace owner grants access to other collaborators by adding them to the [project](/en/projects) that contains the topic and assigning a [project role](/en/connectors/pubsub/pubsub-permissions#project-level-access-for-event-streams-topics) that includes the **Event streams** privilege.

### Sample request

This request creates a new event topic named `Order delivered`. The topic includes details such as the order ID, delivery date, and optional information about the person or service delivering the order.

<api-code>

```shell
curl  -X POST "https://YOUR_DATA_CENTER/api/event_streams/topics" \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "name": ":name",
            "schema": [
                {
                    "control_type": ":control_type",
                    "label": ":label",
                    "name": ":schema_name",
                    "folder_id": 986754,
                    "optional": :true_or_false,
                    "type": ":type"
                }
            ],
            "retention": :retention_value,
            "description": ":description"
         }'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 334527,
        "name": "Order delivered",
        "folder_id": 986754,
        "created_at": "2024-09-25T09:56:32.986-07:00",
        "updated_at": "2024-09-25T09:56:32.986-07:00",
        "retention": 604800,
        "schema": [
            {
                "control_type": "text",
                "label": "Order ID",
                "name": "OrderId",
                "optional": false,
                "type": "string"
            },
            {
                "control_type": "date",
                "label": "Delivery date",
                "name": "DeliveryDate",
                "optional": false,
                "type": "date_time"
            },
            {
                "control_type": "text",
                "label": "Delivered by",
                "name": "DeliveredBy",
                "optional": true,
                "type": "string"
            }
        ],
        "description": "Triggered when an order is delivered."
    }
}
```

#### Folder not found

The request fails and returns the following response if you supply a `folder_id` that doesn't exist:

```json
{
    "message": "Folder not found"
}
```

## Get topic by ID

Retrieves an event topic by its ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/event_streams/topics/:topic_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| topic\_id | **number** _required_ | The ID of the event topic to retrieve. |

### Sample request

This request retrieves the `Order delivered` event topic by its unique `:topic_id`.

<api-code>

```shell
curl  -X GET "https://YOUR_DATA_CENTER/api/event_streams/topics/:topic_id" \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 334527,
        "name": "Order delivered",
        "folder_id": 986754,
        "created_at": "2024-09-25T09:56:32.986-07:00",
        "updated_at": "2024-09-25T09:56:32.986-07:00",
        "retention": 604800,
        "schema": [
            {
                "control_type": "text",
                "label": "Order ID",
                "name": "OrderId",
                "optional": false,
                "type": "string"
            },
            {
                "control_type": "date",
                "label": "Delivery date",
                "name": "DeliveryDate",
                "optional": false,
                "type": "date_time"
            },
            {
                "control_type": "text",
                "label": "Delivered by",
                "name": "DeliveredBy",
                "optional": true,
                "type": "string"
            }
        ],
        "description": "Triggered when an order is delivered."
    }
}
```

## Update a topic

Updates an event topic.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/event_streams/topics/:topic_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| topic\_id | **number** _required_ | The ID of the event topic to update. |

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | The name of the updated topic. |
| folder\_id | **number** _optional_ | The ID of the folder or project to move the topic to. By default, Workato places the topic in your workspace's **Event Streams Topics** project, creating that project if it doesn't already exist. |
| schema | **array** _optional_ | The schema definition for the updated topic. Must adhere to a valid Workato schema format. |
| schema\[control\_type\] | **string** _optional_ | The control type for a field in the topic schema. |
| schema\[label\] | **string** _optional_ | The label that appears for the field in the topic schema. |
| schema\[name\] | **string** _optional_ | The name identifier for the field in the topic schema. |
| schema\[optional\] | **boolean** _optional_ | Specifies whether the field is optional. |
| schema\[type\] | **string** _optional_ | The data type of the field in the schema. |
| retention | **number** _optional_ | Retention time for the topic in seconds. Defaults to 168 hours (604,800 seconds) if not specified. |
| description | **string** _optional_ | A description of the updated topic. |

### Sample request

This request updates the topic schema for the `Order delivered` event topic by adding a new field named `Recipient`.

<api-code>

```shell
curl  -X PUT "https://YOUR_DATA_CENTER/api/event_streams/topics/:topic_id" \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "name": ":name",
            "schema": [
                {
                    "control_type": ":control_type",
                    "label": ":label",
                    "name": ":schema_name",
                    "optional": :true_or_false,
                    "type": ":type"
                }
            ],
            "retention": :retention_value,
            "description": ":description"
         }'
```

</api-code>

### Response

```json
{
    "data": {
        "id": 334527,
        "name": "Order delivered",
        "folder_id": 986754,
        "created_at": "2024-09-25T09:56:32.986-07:00",
        "updated_at": "2024-09-25T09:56:32.986-07:00",
        "retention": 604800,
        "schema": [
            {
                "control_type": "text",
                "label": "Order ID",
                "name": "OrderId",
                "optional": false,
                "type": "string"
            },
            {
                "control_type": "date",
                "label": "Delivery date",
                "name": "DeliveryDate",
                "optional": false,
                "type": "date_time"
            },
            {
                "control_type": "text",
                "label": "Delivered by",
                "name": "DeliveredBy",
                "optional": true,
                "type": "string"
            },
            {
                "control_type": "text",
                "label": "Recipient",
                "name": "Recipient",
                "optional": false,
                "type": "string"
            }
        ],
        "description": "Triggered when an order is delivered."
    }
}
```

#### Folder not found

The request fails and returns the following response if you supply a `folder_id` that doesn't exist:

```json
{
    "message": "Folder not found"
}
```

## Purge a topic

Erases all messages from the event topic's history and resets topic statistics.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/event_streams/topics/:topic_id/purge
```

</api-code>

| Name | Type | Description |
| --- | --- | --- |
| topic\_id | **number** _required_ | The ID of the event topic to purge. |

### Sample request

This request erases all messages from the `Order delivered` event topic's history and resets topic statistics.

<api-code>

```shell
curl  -X PUT "https://YOUR_DATA_CENTER/api/event_streams/topics/:topic_id/purge" \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": {
        "status": "success"
    }
}
```

## Delete a topic

Deletes an event topic.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/event_streams/topics/:topic_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| topic\_id | **number** _required_ | The ID of the event topic to delete. |

### Sample request

This request deletes the `Order delivered` event topic.

<api-code>

```shell
curl  -X DELETE "https://YOUR_DATA_CENTER/api/event_streams/topics/:topic_id" \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": {
        "status": "success"
    }
}
```

---
