---
url: 'https://docs.workato.com/en/oem/oem-api/event-streams.md'
description: >-
  Reference for the Embedded API event streams resource to list, create, update,
  purge, and delete event topics in customer workspaces.
---

# Event streams

Use the following endpoints to manage [event topics](/en/connectors/pubsub) in customer workspaces.

## Rate limits

Event streams resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Event streams](/en/oem/oem-api/event-streams.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/event\_streams/topics](/en/oem/oem-api/event-streams#list-topics) | List topics in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/event\_streams/topics](/en/oem/oem-api/event-streams#create-a-topic) | Create a topic in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/event\_streams/topics/:topic\_id](/en/oem/oem-api/event-streams#get-topic-by-id) | Get a topic by ID in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/event\_streams/topics/:topic\_id](/en/oem/oem-api/event-streams#update-a-topic) | Update a topic in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/event\_streams/topics/:topic\_id/purge](/en/oem/oem-api/event-streams#purge-a-topic) | Purge a topic in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/event\_streams/topics/:topic\_id](/en/oem/oem-api/event-streams#delete-a-topic) | Delete a topic in a customer workspace. |

> **BEST PRACTICE**
> 
> We recommend that you define parameters in the request body instead of the URL for endpoints that modify ([create](#create-a-topic) and [update](#update-a-topic)) topics.

## List topics

Retrieves a list of event topics in a customer workspace, with optional filtering, sorting, and the ability to include topic schemas in the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Filters event topics by a case-sensitive title. Supports partial matching, which means you can search for fragments of the title. |
| sort | **string** _optional_ | Defines how to sort the results. Options include `activity` with the most recent activity listed first, `name`, and `id`. Set to `id` by default. |
| include\_schema | **boolean** _optional_ | When set to `true`, the schema of each event topic is included in the response payload. Set to `false` by default. |

### Sample request

This request retrieves event topics that contain the keyword `Order` within the name. The results are sorted by event topic ID, and the schema for each event topic is included in the response payload.

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics?name=Order&sort=id&include_schema=true' \
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

Creates a new event topic in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name of the new topic. Topic names must be unique within a folder. |
| folder\_id | **number** _optional_ | The ID of the folder or project to store the topic inside. Workato places the topic in the customer workspace's **Event Streams** project by default, creating that project if it doesn't already exist. |
| schema | **array** _required_ | The schema definition for the new topic. Must adhere to a valid Workato schema format. |
| schema\[control\_type\] | **string** _required_ | The control type for a field in the topic schema. |
| schema\[label\] | **string** _required_ | The label that appears for the field in the topic schema. |
| schema\[name\] | **string** _required_ | The name identifier for the field in the topic schema. |
| schema\[optional\] | **boolean** _required_ | Specifies whether the field is optional. |
| schema\[type\] | **string** _required_ | The data type of the field in the schema. |
| retention | **number** _optional_ | Retention time for the topic in seconds. Defaults to 168 hours (604,800 seconds) if not specified. |
| description | **string** _optional_ | A description of the new topic. |

### Sample request

This request creates a new event topic named `Order delivered`. The topic includes details, such as the order ID, delivery date, and optional information about the person or service delivering the order.

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "folder_id": :folder_id_value,
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

Retrieves an event topic in a customer workspace by its ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics/:topic_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| topic\_id | **number** _required_ | The ID of the event topic to retrieve. You can use the [List topics](#list-topics) endpoint to retrieve topic IDs. |

### Sample request

This request retrieves the `Order delivered` event topic by its unique `:topic_id`.

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics/:topic_id' \
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

Updates an event topic in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics/:topic_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| topic\_id | **number** _required_ | The ID of the event topic to update. You can use the [List topics](#list-topics) endpoint to retrieve topic IDs. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | The name of the updated topic. |
| folder\_id | **number** _optional_ | The ID of the folder or project to move the topic to. Workato places the topic in the customer workspace's **Event Streams** project by default, creating that project if it doesn't already exist. |
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
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics/:topic_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
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

Erases all messages from the event topic's history in a customer workspace and resets topic statistics.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics/:topic_id/purge
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| topic\_id | **number** _required_ | The ID of the event topic to purge. You can use the [List topics](#list-topics) endpoint to retrieve topic IDs. |

### Sample request

This request erases all messages from the `Order delivered` event topic's history and resets topic statistics.

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics/:topic_id/purge' \
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

Deletes an event topic in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics/:topic_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. External IDs must have the prefix `E` and be URL-encoded. For example, `EA2300`. |
| topic\_id | **number** _required_ | The ID of the event topic to delete. You can use the [List topics](#list-topics) endpoint to retrieve topic IDs. |

### Sample request

This request deletes the `Order delivered` event topic.

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/event_streams/topics/:topic_id' \
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
