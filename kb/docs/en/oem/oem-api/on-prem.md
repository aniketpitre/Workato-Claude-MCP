---
url: 'https://docs.workato.com/en/oem/oem-api/on-prem.md'
description: >-
  Reference for Embedded API endpoints to list, create, update, delete, and
  check the status of on-prem groups and agents in customer workspaces.
---

# Embedded API - On-prem

Use the following endpoints to manage [on-prem groups](/en/on-prem/groups) and [on-prem agents](/en/on-prem/agents) programmatically.

## Rate limits

On-prem resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [On-prem](/en/oem/oem-api/on-prem.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_groups](#list-on-prem-groups) | List on-prem groups in a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_groups](#create-on-prem-group) | Create an on-prem group in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_groups/:group\_id](#get-on-prem-group-details) | Retrieve details about an on-prem group in a customer workspace. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_groups/:group\_id](#update-on-prem-group) | Updates an on-prem group in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_groups/:group\_id](#delete-on-prem-group) | Deletes an on-prem group in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_groups/:group\_id/status](#get-on-prem-group-status) | Retrieves status of an on-prem group in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_agents](#list-on-prem-agents) | List on-prem agents in a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_agents](#create-on-prem-agent) | Create an on-prem agent in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_agents/:agent\_id](#get-details-about-an-on-prem-agent) | Retrieve the details of a specific on-prem agent in a customer workspace using its ID. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_agents/:agent\_id](#update-on-prem-agent) | Update an on-prem agent in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_agents/:agent\_id](#delete-on-prem-agent) | Delete an on-prem agent in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_agents/:agent\_id/status](#get-on-prem-agent-status) | Retrieve the status of an on-prem agent in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/on\_prem\_agents/search](#search-on-prem-agents) | Finds on-prem agents in a customer workspace by common name. |

## List on-prem groups

Retrieves a list of all [on-prem groups](/en/on-prem/groups) in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "id": 2159,
            "name": "DevOps Network",
            "created_at": "2024-09-25T13:09:31.292-07:00",
            "use_managed_connection": true,
            "config_version": null,
            "in_use": false,
            "logs_enabled": false,
            "whitelisted_ips": [
              "198.51.100.10",
              "192.0.2.0/24"
            ]
        }
    ]
}
```

## Create on-prem group

Creates an [on-prem group](/en/on-prem/groups) in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The on-prem group's name. |
| use\_managed\_connection | **boolean** _optional_ | Set to `true` to configure the on-prem group using a [cloud profile](/en/on-prem/agents/connection/cloud) or `false` to configure each agent manually using a `config.yml` file. Defaults to `false` if not specified. |
| settings\_attributes\[whitelisted\_ips\] | **array of strings** _optional_ | Defines IPs to whitelist for the on-prem group. |

#### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
          "name": ":name",
          "use_managed_connection": :true_or_false,
          "settings_attributes": {
            "whitelisted_ips": [
              ":whitelisted_ips_1",
              ":whitelisted_ips_2"
            ]
          }
         }'
```

</api-code>

#### Sample response

```json
{
  "data": {
    "id": 16803,
    "name": "CRM server",
    "created_at": "2025-07-24T12:53:23.255-07:00",
    "use_managed_connection": true,
    "config_version": null,
    "in_use": false,
    "logs_enabled": false,
    "whitelisted_ips": [
        "198.51.100.10",
        "192.0.2.0/24"
    ]
  }
}
```

## Get on-prem group details

Retrieves details about an [on-prem group](/en/on-prem/groups) in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups/:group_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| group\_id | **integer** _required_ | The ID of the on-prem group to retrieve. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups/:group_id' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
[
  {
    "id": 16803,
    "name": "CRM server",
    "created_at": "2017-09-21T01:51:45.954-07:00",
    "use_managed_connection": false,
    "config_version": null,
    "in_use": false,
    "logs_enabled": false,
    "whitelisted_ips": [
      "198.51.100.10",
      "192.0.2.0/24"
    ]
  }
]
```

## Update on-prem group

Updates an [on-prem group](/en/on-prem/groups) in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups/:group_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| group\_id | **integer** _required_ | The on-prem group's ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | The on-prem group's name. |
| settings\_attributes\[whitelisted\_ips\] | **array of strings** _optional_ | Defines IPs to whitelist for the on-prem group. |

#### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups/:group_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
             "name": ":name",
             "settings_attributes": {
                "whitelisted_ips": [
                  ":whitelisted_ips_1",
                  ":whitelisted_ips_2"
                ]
              }
            }'
```

</api-code>

#### Sample response

```json
[
  {
    "id": 16803,
    "name": "CRM server",
    "created_at": "2017-09-21T01:51:45.954-07:00",
    "use_managed_connection": false,
    "config_version": null,
    "in_use": false,
    "logs_enabled": false,
    "whitelisted_ips": [
      "198.51.100.55",
      "192.0.2.0/5"
    ]
  }
]
```

## Delete on-prem group

Deletes an [on-prem group](/en/on-prem/groups) in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups/:group_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| group\_id | **integer** _required_ | The on-prem group's ID. |

#### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups/:group_id' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
{
  "success": true
}
```

## Get on-prem group status

Retrieves status of an [on-prem group](/en/on-prem/groups) in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups/:group_id/status
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| group\_id | **integer** _required_ | The on-prem group's ID. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_groups/:group_id/status' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

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

Retrieves a list of all [on-prem agents](/en/on-prem/agents) in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "id": 29104,
            "name": "Marketing(Cupertino)",
            "os": "mac",
            "installation_method": null,
            "awaiting_setup": true,
            "enabled": true,
            "last_seen_version": null,
            "created_at": "2024-09-25T13:21:43.292-07:00",
            "updated_at": "2024-09-25T13:21:43.292-07:00",
            "state": "awaiting_setup",
            "activated": true,
            "cn": "134fd7acd89cf5b8b96deea4870d413d:29104",
            "on_prem_group_id": 12345
        },
        {
            "id": 29105,
            "name": "Sales(Cupertino)",
            "os": "mac",
            "installation_method": null,
            "awaiting_setup": true,
            "enabled": true,
            "last_seen_version": null,
            "created_at": "2024-09-26T09:15:30.123-07:00",
            "updated_at": "2024-09-26T09:15:30.123-07:00",
            "state": "awaiting_setup",
            "activated": true,
            "cn": "e29f4b6d8e1845e299e5c8cfb7f72d4a:29105",
            "on_prem_group_id": 12345
        }
    ]
}
```

## Create on-prem agent

Creates an [on-prem agent](/en/on-prem/agents) in a customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The on-prem agent's name. |
| os | **string** _optional_ | The server's operating system. |
| on\_prem\_group\_id | **integer** _required_ | The on-prem group's ID. You can retrieve group IDs from the [List on-prem groups](#list-on-prem-groups) endpoint's response. |
| awaiting\_setup | **boolean** _optional_ | Set to `true` to create the agent in the `awaiting_setup` state. Set to `false` to skip agent setup and get its status right away. Defaults to `true` if not specified. |

#### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents' \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":name",
           "os": ":os",
           "on_prem_group_id": :on_prem_group_id,
           "awaiting_setup": :true_or_false
         }'
```

</api-code>

#### Sample response

```json
[
  {
    "id": 71144,
    "name": "US-west-1",
    "os": "windows",
    "installation_method": null,
    "awaiting_setup": false,
    "enabled": true,
    "last_seen_version": null,
    "created_at": "2025-07-16T07:10:32.231-07:00",
    "updated_at": "2025-07-16T07:10:32.487-07:00",
    "state": "connected",
    "activated": false,
    "cn": "30a600473728b596e63ee8b30e3dd648:71144",
    "on_prem_group_id": 33830
  }
]
```

## Get details about an on-prem agent

Retrieves details about an [on-prem agent](/en/on-prem/agents) within a customer workspace using its unique ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents/:agent_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| agent\_id | **number** _required_ | The ID of the on-prem agent to retrieve details about. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents/:agent_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "id": 29104,
            "name": "Marketing(Cupertino)",
            "os": "mac",
            "installation_method": null,
            "awaiting_setup": true,
            "enabled": true,
            "last_seen_version": null,
            "created_at": "2024-09-25T13:21:43.292-07:00",
            "updated_at": "2024-09-25T13:21:43.292-07:00",
            "state": "awaiting_setup",
            "activated": true,
            "cn": "134fd7acd89cf5b8b96deea4870d413d:12233",
            "on_prem_group_id": 12345
        }
    ]
}
```

## Update on-prem agent

Updates an [on-prem agent](/en/on-prem/agents) in a customer workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents/:agent_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| agent\_id | **string** _required_ | The on-prem agent's ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | The on-prem agent's name. |
| os | **string** _optional_ | The server's operating system. |
| on\_prem\_group\_id | **integer**_optional_ | The on-prem group's ID. You can retrieve group IDs from the [List on-prem groups](#list-on-prem-groups) endpoint's response. |

#### Sample request

<api-code>

```shell
curl -X PUT 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents/:agent_id' \
      -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":name",
           "os": ":os",
           "on_prem_group_id": :on_prem_group_id
         }'
```

</api-code>

#### Sample response

```json
[
  {
    "id": 12233,
    "name": "US-west-1",
    "os": "windows",
    "installation_method": null,
    "awaiting_setup": false,
    "enabled": true,
    "last_seen_version": null,
    "created_at": "2025-07-16T07:10:32.231-07:00",
    "updated_at": "2025-07-16T07:10:32.487-07:00",
    "state": "connected",
    "activated": false,
    "cn": "30a600473728b596e63ee8b30e3dd648:12233",
    "on_prem_group_id": 16803
  }
]
```

## Delete on-prem agent

Deletes an [on-prem agent](/en/on-prem/agents) in a customer workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents/:agent_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| agent\_id | **string** _required_ | The on-prem agent's ID. |

### Sample response

```json
{
  "success": true
}
```

## Get on-prem agent status

Retrieves the status of an [on-prem agent](/en/on-prem/agents) in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents/:agent_id/status
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| agent\_id | **string** _required_ | The on-prem agent's ID. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents/:agent_id/status' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

```json
{
  "active": true
}
```

## Search on-prem agents

Finds [on-prem agents](/en/on-prem/agents) in a customer workspace by common name.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents/search
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| cn | **string** _optional_ | The common name of the on-prem agent to retrieve. Omit this parameter to return all agents. |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/on_prem_agents/search?cn=:cn' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Sample response

```json
[
  {
    "id": 12233,
    "on_prem_group_id": 16803,
    "name": "example_cn",
    "cn": "134fd7acd89cf5b8b96deea4870d413d:12233",
    "os": "windows",
    "awaiting_setup": false,
    "enabled": true
  }
]
```

---
