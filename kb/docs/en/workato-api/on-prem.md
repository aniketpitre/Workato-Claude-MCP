---
url: 'https://docs.workato.com/en/workato-api/on-prem.md'
description: >-
  Reference for the Developer API on-premise endpoints to list, create, update,
  delete, and check the status of on-prem groups and agents.
---

# Developer API - On-prem agents

The Developer API allows you to work with [on-prem groups](/en/on-prem/groups) and [on-prem agents](/en/on-prem/agents) through the API.

## Rate limits

On-prem resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [On-prem](/en/workato-api/on-prem.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/on\_prem\_groups](#list-on-prem-groups) | List on-prem groups. |
| POST | [/api/on\_prem\_groups](#create-on-prem-group) | Create on-prem group. |
| GET | [/api/on\_prem\_groups/:id](#get-on-prem-group-details) | Get on-prem group details. |
| PUT | [/api/on\_prem\_groups/:id](#update-on-prem-group) | Update on-prem group. |
| DELETE | [/api/on\_prem\_groups/:id](#delete-on-prem-group) | Delete an on-prem group. |
| GET | [/api/on\_prem\_groups/:id/status](#get-on-prem-group-status) | Get on-prem group status. |
| GET | [/api/on\_prem\_agents](#list-on-prem-agents) | List on-prem agents. |
| POST | [/api/on\_prem\_agents](#create-on-prem-agent) | Create on-prem agent. |
| GET | [/api/on\_prem\_agents/:id](#get-on-prem-agent-details) | Get on-prem agent details. |
| PUT | [/api/on\_prem\_agents/:id](#update-on-prem-agent) | Update on-prem agent. |
| DELETE | [/api/on\_prem\_agents/:id](#delete-on-prem-agent) | Delete on-prem agents. |
| GET | [/api/on\_prem\_agents/:id/status](#get-on-prem-agent-status) | Get on-prem agent status. |
| GET | [/api/on\_prem\_agents/search](#search-for-on-prem-agent-by-common-name) | Search for on-prem agent. |
| GET | [/api/on\_prem\_agents/:id/activation\_code](#get-on-prem-agent-activation-code) | Get on-prem agent activation code. |

## List on-prem groups

List all [on-prem groups](/en/on-prem/groups) in your workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/on_prem_groups
```

</api-code>

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/on_prem_groups' \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
[
  {
    "id": 16803,
    "name": "CRM server",
    "created_at": "2017-09-21T01:51:45.954-07:00",
    "in_use": true,
    "use_managed_connection": true,
    "config_version": 9,
    "logs_enabled": false,
    "whitelisted_ips": [
      "198.51.100.10",
      "192.0.2.0/24"
    ]
  }
]
```

## Create on-prem group

Create an [on-prem group](/en/on-prem/groups).

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/on_prem_groups
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The on-prem group's name. |
| use\_managed\_connection | **boolean** _optional_ | Set to `true` to configure the on-prem group using a [cloud profile](/en/on-prem/agents/connection/cloud) or `false` to configure each agent manually using a `config.yml` file. Defaults to `false` if not specified. |
| settings\_attributes\[whitelisted\_ips\] | **array of strings** _optional_ | Defines IPs to whitelist for the on-prem group. |

#### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/on_prem_groups' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
          "name": ":name",
          "use_managed_connection": :true_or_false,
          "settings_attributes": {
            "whitelisted_ips": [
              ":whitelisted_ip_1",
              ":whitelisted_ip_2"
            ]
          }
         }'
```

</api-code>

### Response

```json
{
  "id": 16803,
  "name": "CRM server",
  "created_at": "2017-09-21T01:51:45.954-07:00",
  "in_use": false,
  "use_managed_connection": true,
  "config_version": null,
  "logs_enabled": false,
  "whitelisted_ips": [
    "198.51.100.10",
    "192.0.2.0/24"
  ]
}
```

## Get on-prem group details

Get details about an [on-prem group](/en/on-prem/groups).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/on_prem_groups/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The ID of the on-prem group to retrieve. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/on_prem_groups/:id' \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
{
  "id": 16803,
  "name": "CRM server",
  "created_at": "2017-09-21T01:51:45.954-07:00",
  "in_use": false,
  "use_managed_connection": false,
  "config_version": null,
  "logs_enabled": false,
  "whitelisted_ips": [
      "198.51.100.10",
      "192.0.2.0/24"
  ]
}
```

## Update on-prem group

Update an [on-prem group](/en/on-prem/groups).

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/on_prem_groups/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The on-prem group's ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | The on-prem group's name. |
| settings\_attributes\[whitelisted\_ips\] | **array of strings** _optional_ | Defines IPs to whitelist for the on-prem group. |

#### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/on_prem_groups/:id' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
          "name": ":name",
          "settings_attributes": {
            "whitelisted_ips": [
              ":whitelisted_ip_1",
              ":whitelisted_ip_2"
            ]
          }
         }'
```

</api-code>

### Response

```json
{
  "id": 16803,
  "name": "CRM server",
  "created_at": "2017-09-21T01:51:45.954-07:00",
  "in_use": false,
  "use_managed_connection": false,
  "config_version": null,
  "logs_enabled": false,
  "whitelisted_ips": [
    "198.51.100.10",
    "192.0.2.0/24"
  ]
}
```

## Delete on-prem group

Delete an [on-prem group](/en/on-prem/groups) and the [on-prem agents](/en/on-prem/agents) it contains.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/on_prem_groups/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The on-prem group's ID. |

#### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/on_prem_groups/:id' \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
{
  "success": true
}
```

## Get on-prem group status

Get the status of an [on-prem group](/en/on-prem/groups).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/on_prem_groups/:id/status
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The on-prem group's ID. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/on_prem_groups/:id/status' \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
{
  "agent_count": 4,
  "active_agent_count": 3,
  "profiles": [
    {
      "name": "CRM-Oracle",
      "provider": "oracle",
      "type": "Database",
      "connections": [
        {
          "id": 440724,
          "name": "Oracle CRM DB"
        }
      ]
    }
  ]
}
```

## List on-prem agents

List all [on-prem agents](/en/on-prem/agents) in your workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/on_prem_agents
```

</api-code>

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/on_prem_agents' \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
[
  {
    "id": 12233,
    "on_prem_group_id": 16803,
    "name": "primary agent",
    "cn": "134fd7acd89cf5b8b96deea4870d413d:12233",
    "os": "windows",
    "installation_method": null,
    "awaiting_setup": false,
    "enabled": true,
    "last_seen_version": "25.0",
    "created_at": "2024-12-10T13:20:03.330-08:00",
    "updated_at": "2025-05-12T13:03:23.754-07:00",
    "state": "connected",
    "activated": true
  }
]
```

## Create on-prem agent

Create an [on-prem agent](/en/on-prem/agents).

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/on_prem_agents
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The on-prem agent's name. |
| on\_prem\_group\_id | **integer** _required_ | The on-prem group's ID. You can retrieve group IDs from the [List on-prem groups](#list-on-prem-groups) endpoint's response. |
| os | **string** _optional_ | The server's operating system. |
| awaiting\_setup | **boolean** _optional_ | Set to `true` to create the agent in the `awaiting_setup` state. Set to `false` to skip agent setup and get its status right away. Defaults to `true` if not specified. |
| enabled | **boolean** _optional_ | Set to `true` to enable the agent or `false` to disable it. |

#### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/on_prem_agents' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
          "name": ":name",
          "on_prem_group_id": :on_prem_group_id_value,
          "os": ":os",
          "awaiting_setup": :true_or_false
         }'
```

</api-code>

### Response

```json
{
  "id": 12233,
  "on_prem_group_id": 50,
  "name": "US-west-1",
  "cn": "134fd7acd89cf5b8b96deea4870d413d:12233",
  "os": "windows",
  "installation_method": null,
  "awaiting_setup": false,
  "enabled": true,
  "last_seen_version": null,
  "created_at": "2025-06-24T12:37:49.824-07:00",
  "updated_at": "2025-06-24T12:37:49.886-07:00",
  "state": "connected",
  "activated": false
}
```

## Get on-prem agent details

Get the details of an [on-prem agent](/en/on-prem/agents).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/on_prem_agents/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The on-prem agent's ID. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/on_prem_agents/:id' \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
{
  "id": 12233,
  "on_prem_group_id": 16803,
  "name": "primary agent",
  "cn": "134fd7acd89cf5b8b96deea4870d413d:12233",
  "os": "windows",
  "installation_method": null,
  "awaiting_setup": true,
  "enabled": true,
  "last_seen_version": null,
  "created_at": "2025-06-24T12:37:49.824-07:00",
  "updated_at": "2025-06-24T12:37:49.886-07:00",
  "state": "awaiting_setup",
  "activated": false
}
```

## Update on-prem agent

Update an [on-prem agent](/en/on-prem/agents).

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/on_prem_agents/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The on-prem agent's ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | The on-prem agent's name. |
| os | **string** _optional_ | The server's operating system. |
| on\_prem\_group\_id | **integer** _optional_ | The on-prem group's ID. You can retrieve group IDs from the [List on-prem groups](#list-on-prem-groups) endpoint's response. |
| enabled | **boolean** _optional_ | Set to `true` to enable the agent or `false` to disable it. |

#### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/on_prem_agents/:id' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":name"
         }'
```

</api-code>

### Response

```json
{
  "id": 49026,
  "on_prem_group_id": 32109,
  "name": "primary agent",
  "cn": "1ee944db3b24d7c19dfe4685c49b77a4:49026",
  "os": "windows",
  "installation_method": null,
  "awaiting_setup": false,
  "enabled": true,
  "last_seen_version": "27.0",
  "created_at": "2025-03-27T08:18:49.641-07:00",
  "updated_at": "2025-05-12T13:26:36.731-07:00",
  "state": "connected",
  "activated": true
}
```

## Delete on-prem agent

Delete an [on-prem agent](/en/on-prem/agents).

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/on_prem_agents/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The on-prem agent's ID. |

#### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/on_prem_agents/:id' \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
{
  "success": true
}
```

## Get on-prem agent status

Get the status of an [on-prem agent](/en/on-prem/agents).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/on_prem_agents/:id/status
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The on-prem agent's ID. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/on_prem_agents/:id/status' \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
{
  "active": true
}
```

## Search for on-prem agent by common name

Search [on-prem agents](/en/on-prem/agents) by their common name.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/on_prem_agents/search
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| cn | **string** _optional_ | The common name of the on-prem agent to retrieve. Omit this parameter to return all agents. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/on_prem_agents/search' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d  '{
             "cn": "134fd7acd89cf5b8b96deea4870d413d:12233"
          }'
```

</api-code>

### Response

```json
[
  {
    "id": 12233,
    "on_prem_group_id": 16803,
    "name": "primary agent",
    "cn": "134fd7acd89cf5b8b96deea4870d413d:12233",
    "os": "windows",
    "awaiting_setup": false,
    "enabled": true
  }
]
```

## Get on-prem agent activation code

Get an activation code for an [on-prem agent](/en/on-prem/agents).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/on_prem_agents/:id/activation_code
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The on-prem agent's ID. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/on_prem_agents/:id/activation_code' \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
[
  {
    "code": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMjY3MTA4NTU5NDBmMGFjYTVmNDYyMTFhNWYxMmJiNzo2MDg3MCIsImlhdCI6MTc0ODcyNTU5OSwiZXhwIjoxNzQ4NzI5MTk5LCJhZ2VudCI6NjA4NzAsImd3Ijoic2czLndvcmthdG8uY29tfHNnNC53b3JrYXRvLmNvbSJ9.JCcQ0NCetvIjP9xJJ1BIUAxmE9ImuNvtUJLNIazICiQg61RlSz2YJHywhbSXvakjjB77L7ZPydo43Rs_iiWiWRr5atk8iHvZlnfAKL_338-nFxmSkN-Ms7sL-fguNdQaO-DgkkZubAJ-qP8a34VKJ6QYA3c3SaixoNfnukKan0mUySTz7wQsVxU4C0Ff0R42AGO9CjKxYRobeBr_QgLJm6PtSUN5J6JkWGpyg9jTHJEpsFPDLBzJ0u7O7HkDP_onF4wdrraJ7_5BSn04ZllXw6oIwTbMWq1ncqhYHs0ZXNnv3efXF4L0tzgSkekdz-YasqojNSo0wzfpV0W_3vq_Mg"
  }
]
```

---
