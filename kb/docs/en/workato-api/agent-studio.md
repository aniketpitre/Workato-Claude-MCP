---
url: 'https://docs.workato.com/en/workato-api/agent-studio.md'
description: >-
  Reference for the Agent Studio API to create and manage genies, knowledge
  bases, skills, and guardrail policies programmatically.
---

# Developer API - Agent Studio

The [Agent Studio](/en/agentic/agent-studio) APIs allow you to programmatically create and manage Agent Studio assets, such as genies, knowledge bases, and skills.

## Rate limits

Agent Studio resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| GET | List genies: [/api/agentic/genies](https://docs.workato.com/workato-api/agent-studio.html#list-genies) | 1,000 requests per minute |
| GET | Get a genie by ID: [/api/agentic/genies/:id](https://docs.workato.com/workato-api/agent-studio.html#get-a-genie-by-id) | 1,000 requests per minute |
| GET | All [genie conversation](https://docs.workato.com/workato-api/agent-studio.html#conversations) endpoints | 10 requests per second |
| All | All other [genie](https://docs.workato.com/workato-api/agent-studio.html#genies) endpoints | 60 requests per minute |
| GET | List Knowledge bases: [/api/agentic/knowledge\_bases](https://docs.workato.com/workato-api/agent-studio.html#list-knowledge-bases) | 1,000 requests per minute |
| GET | Get a Knowledge base by ID: [/api/agentic/knowledge\_bases/:id](https://docs.workato.com/workato-api/agent-studio.html#get-a-knowledge-base-by-id) | 1,000 requests per minute |
| All | All other [Knowledge bases](https://docs.workato.com/workato-api/agent-studio.html#knowledge-bases) endpoints | 60 requests per minute |
| GET | List Skills: [/api/agentic/skills](https://docs.workato.com/workato-api/agent-studio.html#list-skills) | 1,000 requests per minute |
| GET | Get a skill by ID: [api/agentic/skills/:id](https://docs.workato.com/workato-api/agent-studio.html#get-a-skill-by-id) | 1,000 requests per minute |
| All | All other [Skills](https://docs.workato.com/workato-api/agent-studio.html#skills) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/agentic/genies](#genies) | Returns a list of genies. |
| POST | [/api/agentic/genies](#create-a-genie) | Creates a new genie. |
| PUT | [/api/agentic/genies/:id](#update-a-genie) | Updates an existing genie. |
| GET | [/api/agentic/genies/:id](#get-a-genie-by-id) | Returns the genie associated with the ID you specify. |
| DELETE | [/api/agentic/genies/:id](#delete-a-genie) | Deletes a genie. |
| POST | [/api/agentic/genies/:id/start](#start-a-genie) | Starts the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/stop](#stop-a-genie) | Stops the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/assign\_skills](#assign-a-skill-to-a-genie) | Assigns skills and MCP servers to the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/remove\_skills](#remove-a-skill-from-a-genie) | Removes skills from the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/assign\_knowledge\_bases](#assign-a-knowledge-base-to-a-genie) | Assigns knowledge bases to the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/remove\_knowledge\_bases](#remove-a-knowledge-base-from-a-genie) | Removes knowledge bases from the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/assign\_user\_groups](#assign-a-user-group-to-a-genie) | Assigns user group access to the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/remove\_user\_groups](#remove-a-user-group-from-a-genie) | Removes user group access from the genie associated with the ID you specify. |
| GET | [/api/agentic/genies/clients](#list-genie-clients) | Returns a list of genie clients. |
| POST | [/api/agentic/genies/clients](#create-a-genie-client) | Creates a new genie client (API key or OAuth). |
| GET | [/api/agentic/genies/clients/:client\_id](#get-a-genie-client) | Returns the genie client associated with the ID you specify. |
| PUT | [/api/agentic/genies/clients/:client\_id](#update-a-genie-client) | Updates a genie client's name and OAuth redirect URLs. |
| DELETE | [/api/agentic/genies/clients/:client\_id](#delete-a-genie-client) | Deletes a genie client. |
| POST | [/api/agentic/genies/clients/:client\_id/regenerate](#regenerate-a-genie-client-key) | Regenerates the API key for a genie client. |
| POST | [/api/agentic/genies/clients/:client\_id/pause](#pause-a-genie-client) | Pauses a genie client. |
| POST | [/api/agentic/genies/clients/:client\_id/start](#start-a-genie-client) | Starts a paused genie client. |
| POST | [/api/agentic/genies/:id/clients](#attach-a-client-to-a-genie) | Attaches a client to a genie. |
| DELETE | [/api/agentic/genies/:id/clients/:client\_id](#detach-a-client-from-a-genie) | Detaches a client from a genie. |
| GET | [/api/agentic/genies/:genie\_id/interfaces](#list-chat-interface-triggers) | Returns all chat interface triggers of a genie in a single list. |
| GET | [/api/agentic/genies/:genie\_id/conversations](#list-conversations) | Returns a list of a genie's conversations. Doesn't include event-level detail. |
| GET | [/api/agentic/genies/:genie\_id/conversations/:conversation\_id](#get-a-conversation) | Returns a genie conversation you specify. Doesn't include event-level detail. |
| GET | [/api/agentic/genies/:genie\_id/conversations/:conversation\_id/events](#list-conversation-events) | Returns the full events of a single conversation. |
| GET | [/api/agentic/genies/:genie\_id/guardrails](#get-a-genies-guardrail) | Returns the guardrail and its policies for the genie associated with the ID you specify. |
| PUT | [/api/agentic/genies/:genie\_id/guardrails/policies/:policy\_type](#create-or-update-a-policy) | Creates or updates a single guardrail policy on the genie associated with the ID you specify. |
| GET | [/api/agentic/genies/guardrails/policies/pii\_entities](#list-pii-entity-types) | Returns the list of PII entity type strings you can use in a `pii_detection` policy. |
| GET | [/api/agentic/knowledge\_bases](#list-knowledge-bases) | Returns a list of knowledge bases. |
| POST | [/api/agentic/knowledge\_bases](#create-a-knowledge-base) | Creates a new knowledge base. |
| GET | [/api/agentic/knowledge\_bases/:id](#get-a-knowledge-base-by-id) | Returns the knowledge base associated with the ID you specify. |
| PUT | [/api/agentic/knowledge\_bases/:id](#update-a-knowledge-base) | Updates an existing knowledge base. |
| DELETE | [/api/agentic/knowledge\_bases/:id](#delete-a-knowledge-base) | Deletes a knowledge base. |
| GET | [/api/agentic/knowledge\_bases/:id/data\_sources](#get-knowledge-base-data-sources) | Returns the data sources associated with the knowledge base ID you specify. |
| GET | [/api/agentic/knowledge\_bases/:id/recipes](#get-knowledge-base-recipes) | Returns the recipes associated with the knowledge base ID you specify. |
| GET | [/api/agentic/skills](#list-skills) | Returns a list of skills. |
| POST | [/api/agentic/skills](#create-a-skill) | Creates a new skill. |
| GET | [/api/agentic/skills/:id](#get-a-skill-by-id) | Returns the skill associated with the ID you specify. |

## Genies

Agent Studio genies support the following endpoints and configurations:

### List genies

Returns a list of genies. Each genie includes a `triggers[]` array. Refer to [Genie triggers](#genie-triggers) for more information.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/genies
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| folder\_id | **string** _optional_ | The ID of the folder where the genie resides. |
| project\_id | **string** _optional_ | The ID of the project where the genie resides. |
| state | **string** _optional_ | The state of the genie. For example: `active` or `inactive`. |
| page | **integer** _optional_ | Page number of the genies to fetch. Minimum value is `1`. |
| per\_page | **integer** _optional_ | Number of genies to return in a single page. Minimum value is `1`. Maximum value is `50`. |

##### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/agentic/genies?per_page=:per_page_value&page=:page_value \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

Channel configuration fields are returned using the default values when no explicit configuration is set.

The response includes a `Deprecation: true` header. The top-level `connection_id`, `custom_oauth_key_id`, and channel fields are deprecated. Use `triggers[]` instead.

```json
[
  {
      "id": "gin-BWLSPX4z-BaT3D9",
      "name": "Customer Support Genie",
      "description": "Handles customer support inquiries and provides quick responses.",
      "state": "stopped",
      "folder_id": 22991030,
      "instructions": "You are a helpful, friendly support agent who answers customer questions clearly and politely.",
      "ai_provider": "open_ai",
      "chat_interface": "slack",
      "channel_mode": "dms_only",
      "channel_scope": "specific",
      "response_mode": "on_mention",
      "channel_whitelist": [],
      "triggers": [
        {
          "id": "ginct-abc123",
          "platform": "slack",
          "name": "Slack - Acme",
          "status": "active",
          "shared_account_id": 1234,
          "custom_oauth_key_id": 5678,
          "channel_mode": "dms_only",
          "channel_scope": "specific",
          "response_mode": "on_mention",
          "channel_whitelist": []
        }
      ],
      "skills_count": 5,
      "knowledge_bases_count": 3,
      "user_groups_count": 0,
      "active_recipes_count": 0,
      "inactive_skills_count": 5,
      "logo_url": "https://example.com/logo.png",
      "created_at": "2025-07-15T11:07:34.060-07:00",
      "updated_at": "2026-02-24T08:38:29.099-08:00"
  },
  {
      "id": "gin-ZWSMPR4a-TaG7S9",
      "name": "Customer Support Genie v2",
      "description": "Updated to handle billing inquiries in addition to general support.",
      "state": "stopped",
      "folder_id": 21285720,
      "instructions": "You are a knowledgeable, polite support assistant. Prioritize clear, concise answers.",
      "ai_provider": "open_ai",
      "chat_interface": "slack",
      "channel_mode": "everywhere",
      "channel_scope": "all_invited",
      "response_mode": "helpdesk",
      "channel_whitelist": [],
      "triggers": [
        {
          "id": "ginct-def456",
          "platform": "slack",
          "name": "Slack - Acme",
          "status": "active",
          "shared_account_id": 1234,
          "custom_oauth_key_id": 5678,
          "channel_mode": "everywhere",
          "channel_scope": "all_invited",
          "response_mode": "helpdesk",
          "channel_whitelist": []
        }
      ],
      "skills_count": 5,
      "knowledge_bases_count": 3,
      "user_groups_count": 0,
      "active_recipes_count": 0,
      "inactive_skills_count": 5,
      "logo_url": "https://example.com/logo.png",
      "created_at": "2026-02-24T08:54:34.585-08:00",
      "updated_at": "2026-02-25T09:34:14.013-08:00"
  }
]
```

### Create a genie

Creates a new genie.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name of the genie. |
| description | **string** _required_ | A description of the genie's purpose. |
| folder\_id | **string** _required_ | The ID of the folder where the genie resides. |
| instructions | **string** _required_ | The instructions your genie uses to identify its purpose, personality, and job description. |
| ai\_model | **string** _optional_ | The model the genie uses. For example: `gpt-4o`. Use with `ai_provider`. Returns `null` for custom providers. |
| ai\_provider | **string** _optional_ | The internal provider engine that powers your genie. Accepted values are `open_ai`, `anthropic`, or `byollm`. Use with `ai_model`. |
| ai\_provider\_type | **string** _optional_ | The type of AI provider that powers your genie. Use with `ai_provider_id`. |
| ai\_provider\_id | **string** _optional_ | The ID of the AI provider that powers your genie. Use with `ai_provider_type`. |
| shared\_account\_id | **integer** _required_ | The Connection ID of your genie. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| custom\_oauth\_key\_id | **integer** _required_ | Custom OAuth key ID. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| matrix | **boolean** _required_ | Determines whether Workato GO is enabled as your chat interface or not. Accepted values are `true` or `false`. |
| channel\_mode | **string** _optional_ | Controls where the genie responds. Accepted values are `dms_only` or `everywhere`. Defaults to `dms_only`. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| channel\_scope | **string** _optional_ | Determines which channels the genie responds in. Accepted values are `specific` or `all_invited`. Defaults to `specific`. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| response\_mode | **string** _optional_ | Controls how the genie is triggered in a channel. Accepted values are `on_mention` or `helpdesk`. Defaults to `on_mention`. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| channel\_whitelist | **string\[\]** _optional_ | An array of Slack channel IDs the genie is permitted to respond in. Only applies when `channel_scope` is `specific`. Defaults to `[]`. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| triggers | **array of object** _optional_ | The chat triggers of the genie. The server generates an `id` for each entry. Refer to [Genie triggers](#genie-triggers) for the schema, validation rules, and legacy field behavior. |

##### Sample request

<api-code>

```shell

curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":genie_name",
           "description": ":description",
           "folder_id": ":folder_id",
           "instructions": ":instructions",
           "ai_provider": ":ai_provider",
           "shared_account_id": :shared_account_id,
           "custom_oauth_key_id": :custom_oauth_key_id,
           "matrix": :true_or_false,
           "channel_mode": ":channel_mode",
           "channel_scope": ":channel_scope",
           "response_mode": ":response_mode",
           "channel_whitelist": [":channel_id", ":channel_id"]
         }'
```

</api-code>

Create a genie with `triggers[]`:

<api-code>

```shell

curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":genie_name",
           "description": ":description",
           "folder_id": ":folder_id",
           "instructions": ":instructions",
           "ai_provider": ":anthropic",
           "triggers": [
             {
               "platform": "slack",
               "name": ":trigger_name",
               "shared_account_id": :shared_account_id,
               "custom_oauth_key_id": :custom_oauth_key_id,
               "channel_mode": ":channel_mode",
               "channel_scope": ":channel_scope",
               "response_mode": ":response_mode",
               "channel_whitelist": [":channel_id"]
             }
           ]
         }'
```

</api-code>

##### Sample response

```json
{
  "id": "gin-BWLSPX4z-BaT3D9"
}
```

### Update a genie

Updates an existing genie.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/agentic/genies/:id
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you plan to update. |
| name | **string** _optional_ | The name of the genie. |
| description | **string** _optional_ | A description of the genie's purpose. |
| folder\_id | **string** _optional_ | The ID of the folder where the genie resides. |
| instructions | **string** _optional_ | The instructions your genie uses to identify its purpose, personality, and job description. |
| ai\_provider | **string** _optional_ | The internal provider engine that powers your genie. Accepted values are `open_ai`, `anthropic`, or `byollm`. Use with `ai_model`. |
| ai\_model | **string** _optional_ | The model the genie uses. For example: `gpt-4o`. Use with `ai_provider`. Returns `null` for custom providers. |
| ai\_provider\_type | **string** _optional_ | The type of AI provider that powers your genie. Use with `ai_provider_id`. |
| ai\_provider\_id | **string** _optional_ | The ID of the AI provider that powers your genie. Use with `ai_provider_type`. |
| shared\_account\_id | **integer** _optional_ | The Connection ID of your genie. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| custom\_oauth\_key\_id | **integer** _optional_ | Custom OAuth key ID. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| matrix | **boolean** _optional_ | Determines whether Workato GO is enabled as your chat interface or not. Accepted values are `true` or `false`. |
| channel\_mode | **string** _optional_ | Controls where the genie responds. Accepted values are `dms_only` or `everywhere`. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| channel\_scope | **string** _optional_ | Determines which channels the genie responds in. Accepted values are `specific` or `all_invited`. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| response\_mode | **string** _optional_ | Controls how the genie is triggered in a channel. Accepted values are `on_mention` or `helpdesk`. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| channel\_whitelist | **string\[\]** _optional_ | An array of Slack channel IDs the genie is permitted to respond in. Only applies when `channel_scope` is `specific`. Pass an empty array to clear the list. Deprecated in favor of `triggers[]`. Ignored when you send `triggers[]`. |
| triggers | **array of object** _optional_ | The complete list of chat triggers for the genie. This replaces all existing triggers atomically. Refer to [Genie triggers](#genie-triggers) for the replacement semantics, validation rules, and legacy field behavior. |

##### Sample request

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/agentic/genies/:id \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":genie_name",
           "description": ":description",
           "instructions": ":instructions",
           "matrix": :true_or_false,
           "channel_mode": ":channel_mode_setting",
           "channel_scope": ":channel_scope",
           "response_mode": ":response_mode",
           "channel_whitelist": [":channel_id"]
         }'
```

</api-code>

Update a genie's triggers. This example updates an existing trigger and creates a new one. Any existing trigger missing from the array is removed:

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/agentic/genies/:id \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "triggers": [
             {
               "id": ":trigger_id",
               "status": "inactive",
               "channel_mode": ":channel_mode",
               "channel_scope": ":channel_scope",
               "channel_whitelist": [":channel_id"]
             },
             {
               "platform": "ms_teams",
               "shared_account_id": :shared_account_id,
               "custom_oauth_key_id": :custom_oauth_key_id
             }
           ]
         }'
```

</api-code>

##### Sample response

```json
{
  "id": "gin-ZWSMPR4a-TaG7S9",
  "name": "Customer Support Genie v2",
  "description": "Updated to handle billing inquiries in addition to general support.",
  "folder_id": "7498",
  "project_id": "4567",
  "instructions": "You are a knowledgeable, polite support assistant. Always prioritize clear, concise answers.",
  "ai_provider": "open_ai",
  "ai_provider_type": "<ai_provider_type>",
  "ai_provider_id": "<ai_provider_id>",
  "shared_account_id": 1234,
  "custom_oauth_key_id": 5678,
  "matrix": false,
  "channel_mode": "everywhere",
  "channel_scope": "specific",
  "response_mode": "on_mention",
  "channel_whitelist": ["C0A9H9EN7J6"]
}
```

### Get a genie by ID

Returns the genie associated with the ID you specify. The genie includes a `triggers[]` array and the LLM configuration, `ai_provider_type` and `ai_provider_id`. Refer to [Genie triggers](#genie-triggers) for more information.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/genies/:id
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you plan to retrieve. |

##### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/genies/:id \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

Channel configuration fields are returned with the default values when no explicit configuration is set.

The response includes a `Deprecation: true` header. The top-level `connection_id`, `custom_oauth_key_id`, and channel fields are deprecated. Use `triggers[]` instead.

```json
{
  "data": {
    "id": "gin-ZWSMPR4a-TaG7S9",
    "name": "Customer Support Genie v2",
    "description": "Updated to handle billing inquiries in addition to general support.",
    "state": "inactive",
    "folder_id": 21285720,
    "project_id": 93761783,
    "instructions": "You are a knowledgeable, polite support assistant. Always prioritize clear, concise answers.",
    "ai_provider": "anthropic",
    "chat_interface": "slack",
    "skills_count": 5,
    "knowledge_bases_count": 3,
    "user_groups_count": 0,
    "active_recipes_count": 0,
    "inactive_skills_count": 5,
    "custom_oauth_key_id": 5678,
    "connection_id": null,
    "folders": [
      {
        "id": 21285720,
        "name": "Customer Assistants"
      }
    ],
    "logo_url": "https://example.com/logo.png",
    "channel_mode": "dms_only",
    "channel_scope": "specific",
    "response_mode": "on_mention",
    "channel_whitelist": [],
    "triggers": [
      {
        "id": "ginct-abc123",
        "platform": "slack",
        "name": "Slack - Acme",
        "status": "active",
        "shared_account_id": null,
        "custom_oauth_key_id": 5678,
        "channel_mode": "dms_only",
        "channel_scope": "specific",
        "response_mode": "on_mention",
        "channel_whitelist": []
      }
    ],
    "user_groups": [],
    "created_at": "2026-02-24T08:54:34.170-08:00",
    "updated_at": "2026-02-25T09:34:14.300-08:00",
    "ai_model": "claude-sonnet-4-6",
    "ai_provider_type": "default",
    "ai_provider_id": "claude-sonnet-4-6",
    "ai_model_label": "Claude Sonnet 4.6",
    "guardrails": {
      "id": "aigrl-Abw694Q4-YsapGf-B6",
      "policies": [
        {
          "id": "aigrlp-Abw696Cf-GtErhP-B6",
          "policy_type": "harmful_content",
          "configuration": {
            "filters": [
              { "type": "HATE", "strength": "NONE" },
              { "type": "INSULTS", "strength": "NONE" },
              { "type": "SEXUAL", "strength": "NONE" },
              { "type": "VIOLENCE", "strength": "NONE" },
              { "type": "MISCONDUCT", "strength": "NONE" }
            ]
          }
        },
        {
          "id": "aigrlp-Abw696Ca-CKs8Cr-B6",
          "policy_type": "prompt_attack",
          "configuration": {
            "strength": "NONE"
          }
        }
      ]
    }
  }
}
```

### Delete a genie

Deletes a genie.

<api-code no-copy-method>


```
DELETE https://YOUR_DATA_CENTER/api/agentic/genies/:id
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you plan to delete. |

##### Sample request

<api-code>

```shell
curl -X DELETE https://YOUR_DATA_CENTER/api/agentic/genies/:id \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
    "success": "true"
}
```

### Start a genie

Starts the genie associated with the ID you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/start
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you plan to start. |

##### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/start \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
  "success": true
}
```

### Stop a genie

Stops the genie associated with the ID you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/stop
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you plan to stop. |

##### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/stop \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
  "success": true
}
```

### Assign a skill to a genie

Assigns skills and MCP servers to the genie associated with the ID you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/assign_skills
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you to which you plan to assign skills. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| skill\_ids | **array of string** _optional_ | An array of skill IDs to assign to a genie. |
| mcp\_server\_ids | **array of string** _optional_ | An array of MCP server IDs to assign to a genie. |

You must send at least one of `skill_ids` or `mcp_server_ids`.

###### Sample request

Assign a skill:

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/assign_skills \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "skill_ids": [":skill_id", ":skill_id", ":skill_id"]
         }'
```

</api-code>

###### Sample response

```json
{
    "skills": [
    {
      "id": "65001201",
      "name": "Sales Lead"
    },
    {
      "id": "65704499",
      "name": "Ticket Escalation"
    },
    {
      "id": "65039789",
      "name": "Order Tracking"
    }
  ],
}
```

###### Assign an MCP server sample request

Assign an MCP server:

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/assign_skills \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "mcp_server_ids": [":mcp_server_id"]
         }'
```

</api-code>

### Remove a skill from a genie

Removes a skill from the genie associated with the ID you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/remove_skills
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you from which you plan to remove skills. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| skill\_ids | **array of string** _required_ | An array of skill IDs to remove from a genie. |

###### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/remove_skills \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "skill_ids": [":skill_id", ":skill_id"]
         }'
```

</api-code>

###### Sample response

```json
{
    "skills": [
    {
      "id": "65001201",
      "name": "Sales Lead"
    },
    {
      "id": "65704499",
      "name": "Ticket Escalation"
    }
  ],
}
```

### Assign a knowledge base to a genie

Assigns knowledge bases to the genie associated with the ID you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/assign_knowledge_bases
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you to which you plan to assign knowledge bases. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| knowledge\_base\_ids | **array of string** _required_ | An array of knowledge base IDs to assign to a genie. |

###### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/assign_knowledge_bases \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "knowledge_base_ids": [":knowledge_base_id", ":knowledge_base_id"]
         }'
```

</api-code>

###### Sample response

```json
{
    "knowledge_bases": [
    {
      "id": "kb-WSm8kore-blMxrh",
      "name": "Sync Jira"
    },
    {
      "id": "kb-ATx0crok-saMvba",
      "name": "PRD sync"
    }
  ],
}
```

### Remove a knowledge base from a genie

Removes a knowledge base from the genie associated with the ID you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/remove_knowledge_bases
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you from which you plan to remove knowledge bases. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| knowledge\_base\_ids | **array of string** _required_ | An array of knowledge base IDs to remove from a genie. |

###### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/remove_knowledge_bases \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "knowledge_base_ids": [":knowledge_base_id"]
         }'
```

</api-code>

###### Sample response

```json
{
    "knowledge_bases": [
    {
      "id": "kb-WSm8kore-blMxrh",
      "name": "Sync Jira"
    }
  ],
}
```

### Assign a user group to a genie

Assigns user group access to the genie associated with the ID you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/assign_user_groups
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you to which you plan to assign user group access. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| user\_group\_ids | **array of string** _required_ | An array of user group IDs to add to a genie. |

###### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/assign_user_groups \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "user_group_ids": [":user_group_id", ":user_group_id"]
         }'
```

</api-code>

###### Sample response

```json
{
    "user_groups": [
    {
      "id": "ertXU2Z3sQaL47T8PssX2V",
      "name": "Sales"
    },
    {
      "id": "gpzHU1Y3mJaG77W1JbbZ2B",
      "name": "Finance"
    },
  ],
}
```

### Remove a user group from a genie

Removes user group access from the genie associated with the ID you specify.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/remove_user_groups
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the genie you from which you plan to remove user group access. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| user\_group\_ids | **array of string** _required_ | An array of user group IDs to remove from a genie. |

###### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/remove_user_groups \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "user_group_ids": [":user_group_id"]
         }'
```

</api-code>

###### Sample response

```json
{
    "user_groups": [
    {
      "id": "ertXU2Z3sQaL47T8PssX2V",
      "name": "Sales"
    }
  ],
}
```

## Genie triggers

A trigger is a chat interface a genie responds through, such as Slack, Microsoft Teams, or Workato GO. The `triggers[]` array is available on [List genies](#list-genies), [Get a genie by ID](#get-a-genie-by-id), [Create a genie](#create-a-genie), and [Update a genie](#update-a-genie). Custom clients are a separate resource and aren't part of `triggers[]`. Refer to [Genie clients](#genie-clients) for more information.

Add the following privilege to your API client to use this endpoint:

| Privilege | Required for |
| --- | --- |
| `genie_interfaces.index` | List genie chat interface triggers |

### Trigger fields

| Name | Type | Description |
| --- | --- | --- |
| id | **string** | The trigger handle, for example `ginct-abc123`. The server generates this value. Omit it on create and include it on update to modify an existing trigger. |
| platform | **string** | The chat platform. Accepted values are `slack`, `ms_teams`, or `matrix`. `matrix` is Workato GO. |
| name | **string** _optional_ | A name for the trigger. |
| status | **string** _optional_ | The desired state of the trigger. Accepted values in requests are `active` or `inactive`. Use `inactive` to pause a trigger and `active` to start it. New triggers start as `active`. Responses return `active`, `inactive`, or `warning`. Any other value in a request returns `422`. |
| shared\_account\_id | **integer** _optional_ | The Connection ID of the trigger. Returned as `null` for `matrix` triggers. |
| custom\_oauth\_key\_id | **integer** _optional_ | Custom OAuth key ID. Returned as `null` for `matrix` triggers. |
| channel\_mode | **string** _optional_ | Controls where the genie responds. Accepted values are `dms_only` or `everywhere`. |
| channel\_scope | **string** _optional_ | Determines which channels the genie responds in. Accepted values are `specific` or `all_invited`. |
| response\_mode | **string** _optional_ | Controls how the genie is triggered in a channel. Accepted values are `on_mention` or `helpdesk`. |
| channel\_whitelist | **string\[\]** _optional_ | An array of Slack channel IDs the genie is permitted to respond in. Only applies when `channel_scope` is `specific`. |

#### Sample trigger response

```json
{
  "data": {
    "id": 123,
    "name": "My Genie",
    "triggers": [
      {
        "id": "ginct-abc123",
        "platform": "slack",
        "name": "Slack - Acme",
        "status": "active",
        "shared_account_id": 1234,
        "custom_oauth_key_id": 5678,
        "channel_mode": "everywhere",
        "channel_scope": "specific",
        "response_mode": "on_mention",
        "channel_whitelist": ["C1H9RESGL"]
      },
      {
        "id": "ginct-def456",
        "platform": "matrix",
        "name": "Workato Go",
        "status": "active",
        "shared_account_id": null,
        "custom_oauth_key_id": null,
        "channel_mode": "dms_only",
        "channel_scope": "specific",
        "response_mode": "on_mention",
        "channel_whitelist": []
      }
    ],
    "connection_id": 1234,
    "custom_oauth_key_id": 5678,
    "channel_mode": "everywhere"
  }
}
```

### Replacement semantics on update

`triggers[]` on [Update a genie](#update-a-genie) is an atomic full replacement:

- An entry without an `id` creates a new trigger.
- An entry with an `id` updates the existing trigger.
- An existing trigger missing from the array is removed.
- `"triggers": []` removes all triggers.
- An unknown `id` returns `422` and nothing is applied.

You can swap connections between two triggers in a single request.

#### Validation

Validation is atomic. No entries are applied if an entry fails. Errors include the entry index in the format `triggers[2].field: message`.

| Case | Error |
| --- | --- |
| `channel_scope` is `specific` without a non-empty `channel_whitelist` | `422` on `triggers[i].channel_whitelist` |
| Non-empty `channel_whitelist` with `channel_mode` set to `dms_only` or `channel_scope` set to `all_invited` | `422` on `triggers[i].channel_whitelist` |
| Two entries with the same `shared_account_id` in one request | `422` connection exclusivity |
| Connection already used by another trigger or genie | `422` connection exclusivity |
| More than 50 entries | `422` cap |
| Unknown `id` on update | `422` unknown trigger id |
| `status` isn't `active` or `inactive` | `422` on `triggers[i].status` |
| More than one `matrix` entry for a genie. A genie supports one Workato GO trigger. | `422` |
| `triggers` isn't an array | `400` |

The connection fields, `shared_account_id` and `custom_oauth_key_id`, and channel fields, `channel_mode`, `channel_scope`, `response_mode` and `channel_whitelist`, are ignored for `matrix` triggers. A `matrix` trigger retains default values.

#### Legacy field compatibility

The top-level `connection_id`, `custom_oauth_key_id`, `channel_mode`, `channel_scope`, `response_mode`, and `channel_whitelist` fields remain available but are deprecated. Responses from [List genies](#list-genies) and [Get a genie by ID](#get-a-genie-by-id) include a `Deprecation: true` header.

- **Responses**: Legacy fields mirror the oldest active trigger, `triggers[0]`.
- **Requests**: Legacy flat fields, such as `connection_id` or `shared_account_id`, `custom_oauth_key_id`, and `channel_*`, apply only when you don't send `triggers[]`. These fields apply to the oldest active trigger, `triggers[0]`. Other triggers are untouched.
- The flat fields are ignored and only `triggers[]` applies when you send both.

## Genie clients

Genie clients use the runtime credentials applications use to call a genie through the [Headless API](/en/agentic/agent-studio/chat-interface/headless-api). You must create a client and attach it to a genie. A client authenticates at runtime with either an API key or OAuth 2.0 (PKCE).

> **MULTIPLE CLIENTS PER GENIE, ONE GENIE PER CLIENT**
> 
> A genie supports multiple attached clients. A client belongs to only one genie at a time. Attaching a client that's already attached to another genie returns a `409` conflict with the message `Client is already assigned to another genie`. [Detach](#detach-a-client-from-a-genie) the existing pairing first to re-point a client.
> 
> A genie supports a single client if multiple clients per genie isn't enabled for your workspace. Attempting to attach a second client returns a `409` conflict.
> 
> A genie can have a custom client and a Slack or Microsoft Teams interface at the same time.

> **AVAILABILITY AND PRIVILEGES**
> 
> The following require multiple clients per genie to be enabled for your workspace. Contact your customer manager to enable it.
> 
> - `triggers[]` in genie requests and responses
> - `status`, `type`, `base_host`, `activated_at`, and `genie_ids` in genie client responses
> - The get, pause, and start genie client endpoints
> - The list genie interfaces endpoint
> - `trigger_id` and `trigger_name` in conversation responses, and the `trigger_id` conversation filter
> - [List genie interfaces](#list-genie-interfaces)
> 
> These endpoints return a `403` error if multiple clients per genie isn't enabled.

Add the following privileges to your API client to use the endpoints:

| Privilege | Required for |
| --- | --- |
| `genie_clients.show` | [Get a genie client](#get-a-genie-client) |
| `genie_clients.start` | [Start a genie client](#start-a-genie-client) |
| `genie_clients.pause` | [Pause a genie client](#pause-a-genie-client) |

### List genie clients

Returns the genie clients in the workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/genies/clients
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_id | **string** _optional_ | The handle of a genie to filter results by. Returns only the clients assigned to that genie. For example, `gin-abc`. |

##### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/genies/clients \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

Filter by genie:

<api-code>

```shell
curl -X GET "https://YOUR_DATA_CENTER/api/agentic/genies/clients?genie_id=:genie_handle" \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

Each client also returns `status`, `type`, `base_host`, `activated_at`, `ip_allow_list`, and `genie_ids` when multiple clients per genie is enabled for your workspace. Refer to [Client response fields](#genie-client-response-fields).

```json
{
  "data": [
    {
      "client_id": "gincl-AaBGpLGx-HLdsJL",
      "client_name": "HR Concierge Web",
      "status": "active",
      "type": "api_key",
      "base_host": "genie-api.workato.com",
      "activated_at": null,
      "ip_allow_list": [],
      "genie_ids": ["gin-abc"]
    }
  ],
  "total": 1,
  "page": 1,
  "per_page": 10
}
```

#### Client response fields

| Name | Type | Description |
| --- | --- | --- |
| client\_id | **string** | The ID of the client. |
| client\_name | **string** | The name of the client. |
| status | **string** | The state of the client. Returns `active`, `inactive`, or `warning`. |
| type | **string** | The authentication type of the client. Returns `api_key` or `oauth`. |
| base\_host | **string** | The host the client uses to call the genie. |
| activated\_at | **string** | The time the client was first activated. Returns `null` if it hasn't been activated. |
| ip\_allow\_list | **array** | The IP addresses allowed to use the client. |
| genie\_ids | **array of string** | The handles of the genies the client is assigned to. |

### Create a genie client

Creates a genie client. Set `auth.type` to `api_key` for a server-to-server credential, or `oauth` for a browser-based OAuth 2.0 (PKCE) client.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/clients
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| client\_name | **string** _required_ | A name for the client. |
| auth | **object** _required_ | The authentication configuration. |
| auth.type | **string** _required_ | The authentication type. Accepted values are `api_key` and `oauth`. |
| auth.oauth\_redirect\_url | **string or array of string** _optional_ | The redirect URL or URLs registered for the OAuth flow. Pass an array to register multiple redirect URLs. Required when `auth.type` is `oauth`. |

##### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/clients \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{ "client_name": ":client_name", "auth": { "type": ":auth_type" } }'
```

</api-code>

Create an OAuth client with multiple redirect URLs:

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/clients \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "client_name": ":client_name",
           "auth": {
             "type": "oauth",
             "oauth_redirect_url": [":redirect_url", ":redirect_url"]
           }
         }'
```

</api-code>

##### Sample response

API-key clients use the `api_key` with the 64-character hex string returned only once, at creation. Every client also returns a public `oauth_client_id`. OAuth clients don't return secrets.

When multiple clients per genie is enabled for your workspace, the response also includes `status`, `type`, `base_host`, `activated_at`, `ip_allow_list`, and `genie_ids`.

```json
{
  "data": {
    "client_id": "gincl-AaBGpLGx-HLdsJL",
    "client_name": "HR Concierge Web",
    "oauth_client_id": "MtaJ4c5oIc3_c0TASWnCW0rfmCr6R4UTO7",
    "api_key": "<64-character hex string>",
    "status": "active",
    "type": "api_key",
    "base_host": "genie-api.workato.com",
    "activated_at": null,
    "ip_allow_list": [],
    "genie_ids": []
  }
}
```

### Get a genie client

Returns the genie client associated with the ID you specify. OAuth clients also return `oauth_client_id` and `oauth_redirect_url`. Requires the `genie_clients.show` privilege.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id
```

</api-code>

#### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| client\_id | **string** _required_ | The ID of the client you plan to retrieve. |

##### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
  "data": {
    "client_id": "gincl-xyz789",
    "client_name": "Custom API Client 1",
    "status": "active",
    "type": "api_key",
    "base_host": "genie-api.workato.com",
    "activated_at": null,
    "ip_allow_list": [],
    "genie_ids": ["gin-abc"]
  }
}
```

OAuth clients also return the following fields:

```json
{
  "data": {
    "client_id": "gincl-AaBGpLGx-HLdsJL",
    "client_name": "HR Concierge Web",
    "status": "active",
    "type": "oauth",
    "base_host": "genie-api.workato.com",
    "activated_at": null,
    "ip_allow_list": [],
    "genie_ids": ["gin-abc"],
    "oauth_client_id": "MtaJ4c5oIc3_c0TASWnCW0rfmCr6R4UTO7",
    "oauth_redirect_url": ["https://example.com/callback"]
  }
}
```

#### Error responses

| Status | When |
| --- | --- |
| `403 Forbidden` | Multiple clients per genie isn't enabled for your workspace, or your API client lacks the `genie_clients.show` privilege. |
| `404 Not Found` | The client doesn't exist or was deleted. |

### Update a genie client

Updates a genie client's name and OAuth redirect URLs.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| client\_name | **string** _required_ | The new name for the client. |
| auth.oauth\_redirect\_url | **string or array of string** _optional_ | The redirect URL or URLs for an OAuth client. Replaces the existing redirect URLs. Pass an array to register multiple redirect URLs. An empty array for an OAuth client returns `422`. |

##### Sample request

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{ "client_name": ":client_name" }'
```

</api-code>

Update the redirect URLs of an OAuth client:

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "client_name": ":client_name",
           "auth": { "oauth_redirect_url": [":redirect_url", ":redirect_url"] }
         }'
```

</api-code>

### Delete a genie client

Deletes a genie client and invalidates its credentials. [Detach](#detach-a-client-from-a-genie) a genie client to remove it from a genie without deleting it.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id
```

</api-code>

##### Sample request

<api-code>

```shell
curl -X DELETE https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Regenerate a genie client key

Regenerates the API key for an API-key client. The previous key is invalidated immediately, and the new key is returned only once.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id/regenerate
```

</api-code>

##### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id/regenerate \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
  "data": {
    "api_key": "<64-character hex string>",
    "updated_at": "2026-06-15T06:44:40-07:00"
  }
}
```

### Pause a genie client

Pauses a genie client. The client's `status` changes to `inactive`. Pausing a client that's already paused has no effect and returns `200`. Requires the `genie_clients.pause` privilege.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id/pause
```

</api-code>

##### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id/pause \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
  "data": {
    "status": "inactive"
  }
}
```

#### Error responses

| Status | When |
| --- | --- |
| `403 Forbidden` | Multiple clients per genie isn't enabled for your workspace, or your API client lacks the `genie_clients.pause` privilege. |
| `404 Not Found` | The client doesn't exist or was deleted. |

### Start a genie client

Starts a paused genie client. The client's `status` changes to `active`. Starting a client that's already active has no effect and returns `200`. Requires the `genie_clients.start` privilege.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id/start
```

</api-code>

##### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/clients/:client_id/start \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
  "data": {
    "status": "active"
  }
}
```

#### Error responses

| Status | When |
| --- | --- |
| `403 Forbidden` | Multiple clients per genie isn't enabled for your workspace, or your API client lacks the `genie_clients.start` privilege. |
| `404 Not Found` | The client doesn't exist or was deleted. |

### Attach a client to a genie

Attaches a client to the genie you specify. A genie can have multiple clients. The client can only be attached to one genie at a time. Attaching a client that's already attached to another genie returns `409` with the message `Client is already assigned to another genie`. The response includes the client's `status`.

When multiple clients per genie isn't enabled for your workspace, the genie can't have an existing client.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/clients
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| genie\_client\_id | **string** _required_ | The ID of the client to attach. |

##### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/genies/:id/clients \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{ "genie_client_id": ":genie_client_id" }'
```

</api-code>

### Detach a client from a genie

Detaches a client from the genie you specify. The client isn't deleted and can be attached to another genie.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/agentic/genies/:id/clients/:client_id
```

</api-code>

##### Sample request

<api-code>

```shell
curl -X DELETE https://YOUR_DATA_CENTER/api/agentic/genies/:id/clients/:client_id \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

## Chat interface triggers

Ensure that you meet the following requirements to use chat interface triggers programmatically:

- Multiple clients per genie is enabled for your workspace
- The `genie_interfaces.index` privilege

### List chat interface triggers

Returns a genie's chat interface triggers in a single list. Use the `type` field to determine the chat interface triggers, including `slack`, `ms_teams`, or `matrix`, `api` for custom clients, and `recipe` for recipes. Results are sorted by name. This endpoint is read-only. You must have the `genie_interfaces.index` privilege to use this endpoint.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/genies/:genie_id/interfaces
```

</api-code>

#### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_id | **string** _required_ | The ID of the genie whose interfaces to retrieve. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| query | **string** _optional_ | A case-insensitive substring to match against the chat interface trigger name. Applies to all interface types. |
| page | **integer** _optional_ | Page number to fetch. Starts at `1`. |
| per\_page | **integer** _optional_ | Number of interfaces to return in a single page. Defaults to `20`. Maximum value is `50`. Higher values are reduced to `50`. |

##### Sample request

<api-code>

```shell
curl -X GET "https://YOUR_DATA_CENTER/api/agentic/genies/:genie_id/interfaces?query=:query&page=:page_value&per_page=:per_page_value" \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

`total` is the number of matching chat interface triggers after applying `query` and before paging. Chat interface triggers return `connection_id`, which is the same value as `shared_account_id` in the `triggers[]` array of a genie.

```json
{
  "data": [
    {
      "id": "ginct-abc",
      "name": "Slack - Acme",
      "type": "slack",
      "status": "active",
      "connection_id": 42,
      "channel_mode": "everywhere"
    },
    {
      "id": "gincl-xyz",
      "name": "API Client 1",
      "type": "api",
      "status": "active",
      "auth_type": "api_key",
      "base_host": "genie-api.workato.com",
      "ip_allow_list": [],
      "activated_at": null
    },
    {
      "id": "1842",
      "name": "Handle ticket",
      "type": "recipe",
      "status": "inactive",
      "running": false,
      "trigger_application": "salesforce",
      "latest_activity": {}
    }
  ],
  "total": 3,
  "page": 1,
  "per_page": 20
}
```

#### Error responses

A `403 Forbidden` error response is returned when multiple clients per genie isn't enabled for your workspace, or your API client lacks the `genie_interfaces.index` privilege.

## Conversations

Conversation endpoints expose genie conversation data for use cases that don't require real-time streaming, such as attaching transcripts to support tickets, ad-hoc investigation, or recipe-based automation. Use [Audit log streaming](/en/features/activity-audit-log-streaming) for cases that require real-time streaming.

> **ENVIRONMENT-SCOPED ENDPOINTS**
> 
> All conversation endpoints return data scoped to the environment of the API client used. The `environment_type` and `environment_id` fields in the response identify which environment the data belongs to. Create separate API clients and combine the results to retrieve conversation data across environments.

### List conversations

Returns a list of conversations a genie has had. The most recently active conversations return first.

<api-code no-copy-method>

```
GET /api/agentic/genies/:genie_id/conversations
```

</api-code>

#### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_id | **string** _required_ | The ID of the genie whose conversations to retrieve. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page\[after\] | **string** _optional_ | The starting point for the next set of results based on the last result of the current page. |
| page\[size\] | **integer** _optional_ | The number of items to retrieve per page. The default value is `50` and maximum value is `100`. |
| from | **string** _optional_ | The lower bound on `created_at`, in ISO 8601 format (`YYYY-MM-DDTHH:mm:ss.SSSZ`). Defaults to the start of the retention window. |
| to | **string** _optional_ | The upper bound on `created_at`, in ISO 8601 format (`YYYY-MM-DDTHH:mm:ss.SSSZ`). Defaults to the current time. |
| app\_type | **string** _optional_ | The trigger source to filter results by. Accepted values are `slack`, `teams`, `go`, `headless_api`, `test_mode`, `genie_task`, or `app_event`. Defaults to all sources. |
| trigger\_id | **string** _optional_ | The ID of a chat trigger (`ginct-…`) or custom client (`gincl-…`) to filter conversations by. Returns only conversations that client originated. Ignored when multiple clients per genie isn't enabled for your workspace. |
| identity\_user\_id | **string** _optional_ | The ID of a Workato Identity user to filter conversations by. Defaults to all users. |
| feedback\[\] | **array of string** _optional_ | The feedback state to filter conversations by. Accepted values are `has_positive`, `has_negative`, `has_comments`, or `no_feedback`. You can pass `has_positive`, `has_negative`, and `has_comments` together with `OR`. `no_feedback` is exclusive and can't be combined with any other `feedback[]` values. Requests that combine it with other values return `400 Invalid request`. Requires the feedback filtering feature flag to be enabled for your workspace. |

##### Sample request

<api-code>

```shell
curl -X GET "https://YOUR_DATA_CENTER/api/agentic/genies/gin-AaDdXzLX-dAFvWn-B6/conversations" \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

Filter by conversations that received positive or negative feedback:

<api-code>

```shell
curl -X GET "https://YOUR_DATA_CENTER/api/agentic/genies/gin-AaDdXzLX-dAFvWn-B6/conversations?feedback[]=has_positive&feedback[]=has_negative" \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

Filter by the trigger or client that originated the conversation:

<api-code>

```shell
curl -X GET "https://YOUR_DATA_CENTER/api/agentic/genies/gin-AaDdXzLX-dAFvWn-B6/conversations?trigger_id=ginct-abc123" \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

When multiple clients per genie is enabled for your workspace, each conversation includes `trigger_id` and `trigger_name`, which identify the chat trigger (`ginct-…`) or custom client (`gincl-…`) that originated the conversation. These fields are omitted, not returned as `null`, for legacy conversations without a handle and when the trigger was deleted.

```json
{
    "data": [
        {
            "id": "conversation-01KSR1JDQMT001AWVTPMTRJ3K8",
            "topic": "IT support request classification",
            "created_at": 1779997161292,
            "last_message_at": 1779997161292,
            "started_by": {
                "user_id": "5XwAGRPmbmjAwRgRrt7X2D"
            },
            "started_via": "Recipe",
            "app_type": "genie_task",
            "chat_type": "GENIE",
            "genie_version": 0,
            "test_conversation": false,
            "conversation_origin": "genie_task",
            "trigger_id": "ginct-abc123",
            "trigger_name": "Slack - Acme",
            "genie_id": "6055",
            "genie_handle": "gin-AaDdXzLX-dAFvWn-B6",
            "genie_name": "IT Support genie",
            "workspace_id": 40291,
            "environment_id": 40291,
            "environment_type": "dev"
        }
    ],
    "next_cursor": null
}
```

### Get a conversation

Returns a genie conversation you specify.

<api-code no-copy-method>

```
GET /api/agentic/genies/:genie_id/conversations/:conversation_id
```

</api-code>

#### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_id | **string** _required_ | The ID of the genie to retrieve a conversation from. |
| conversation\_id | **string** _required_ | The ID of the conversation to retrieve. |

##### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/genies/gin-AaDdXzLX-dAFvWn-B6/conversations/conversation-01KSR1JDQMT001AWVTPMTRJ3K8 \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

The Get conversation endpoint doesn't return the underlying event payload, such as LLM calls, tool executions, and guardrail evaluations. Use [List conversation events](#list-conversation-events) to retrieve event-level detail.

When the feedback filtering feature flag is enabled for your workspace, `totals` includes a `feedback` block with counts of positive and negative reactions and the number of those reactions that carried a comment. Both `count` and `comments` are `0` when the conversation has received no feedback.

When multiple clients per genie is enabled for your workspace, the response includes `trigger_id` and `trigger_name`. These fields are omitted, not returned as `null`, for legacy conversations without a handle and when the trigger was deleted.

```json
{
    "data": {
        "id": "conversation-01KSR1JDQMT001AWVTPMTRJ3K8",
        "topic": "IT support request classification",
        "created_at": 1779997161292,
        "last_message_at": 1779997176899,
        "started_by": {
            "user_id": "5XwAGRPmbmjAwRgRrt7X2D"
        },
        "started_via": "Recipe",
        "app_type": "genie_task",
        "chat_type": "GENIE",
        "genie_version": 0,
        "totals": {
            "errors": {
                "count": 0
            },
            "skill_calls": {
                "count": 0
            },
            "kb_calls": {
                "count": 1
            },
            "feedback": {
                "positive": {
                    "count": 6,
                    "comments": 2
                },
                "negative": {
                    "count": 2,
                    "comments": 1
                }
            }
        },
        "test_conversation": false,
        "conversation_origin": "genie_task",
        "trigger_id": "ginct-abc123",
        "trigger_name": "Slack - Acme",
        "genie_id": "6055",
        "genie_handle": "gin-AaDdXzLX-dAFvWn-B6",
        "genie_name": "IT Support genie",
        "workspace_id": 40291,
        "environment_id": 40291,
        "environment_type": "dev"
    }
}
```

### List conversation events

Returns the full events of a single conversation. Refer to [Genie conversation events](/en/features/activity-audit-log-streaming-sample#genie-conversations) for information about each event type.

<api-code no-copy-method>

```
GET /api/agentic/genies/:genie_id/conversations/:conversation_id/events
```

</api-code>

#### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_id | **string** _required_ | The ID of the genie to retrieve conversation events from. |
| conversation\_id | **string** _required_ | The ID of the conversation to retrieve conversation events from. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page\[after\] | **string** _optional_ | The starting point for the next set of results based on the last result of the current page. |
| page\[size\] | **integer** _optional_ | The number of items to retrieve per page. The default value is `20` and maximum value is `100`. We recommend smaller values when events carry large LLM payloads. |
| order | **string** _optional_ | Specifies whether to return newest results first (`desc`) or oldest results first (`asc`). Defaults to `asc`. |
| include\_event\_types\[\] | **array of string** _optional_ | Specifies the event types to filter results by. Defaults to all event types. |
| genie\_run\_id | **string** _optional_ | The ID of a run to filter results by. Defaults to all runs. |

##### Sample request

<api-code>

```shell
curl -X GET "https://YOUR_DATA_CENTER/api/agentic/genies/gin-AaDdXzLX-dAFvWn-B6/conversations/conversation-01KSR1JDQMT001AWVTPMTRJ3K8/events?include_event_types[]=structured_output_formatting_completed" \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json'
```

</api-code>

##### Sample response

```json
{
    "data": [
        {
            "event_id": "191140b7-9735-4b35-acd5-26d91333d391",
            "event_type": "structured_output_formatting_completed",
            "date_time": "2026-05-28T19:39:38.427751Z",
            "workspace_id": 40291,
            "environment_id": 40291,
            "conversation_id": "conversation-01KSR1JDQMT001AWVTPMTRJ3K8",
            "genie_run_id": "1a11ce5f-f04f-44a3-8dd7-818d24fc3ce1",
            "identity_user_id": "5XwAGRPmbmjAwRgRrt7X2D",
            "genie_handle": "gin-AaDdXzLX-dAFvWn-B6",
            "chat_type": "GENIE",
            "request_id": "00-10f680ac3928f4324a8ce8fc602eb58b-d5e7379818cd3c89-01",
            "app_type": "genie_task",
            "data": "{\"message\":\"{\\\"Category\\\": \\\"Hardware / Performance\\\", \\\"Priority\\\": \\\"Medium\\\", \\\"Summary\\\": \\\"The user is experiencing significant performance degradation on their laptop, including a very slow boot time of approximately 5 minutes, possibly caused by several common endpoint issues.\\\"}\",\"error_message\":null}"
        }
    ],
    "next_cursor": null
}
```

## Guardrails

[Guardrails](/en/agentic/agent-studio/guardrails/guardrails) let you attach content safety policies to a genie. Every chat turn is evaluated against its policies before the model responds when a guardrail is present. Each guardrail has two default policies when first attached: `prompt_attack` and `harmful_content`.

> **BETA FEATURE**
> 
> Guardrails API endpoints are in beta. Contact your customer manager for more information.

### Disable or remove a policy

There isn't a `DELETE` guardrail endpoint to enable you to remove a policy from a guardrail through the API. You must reconfigure the guardrail with the [Create or update a policy](#create-or-update-a-policy) endpoint. Use the following table to determine how to turn a policy off based on its type:

| Policy type | How to turn off the policy |
| --- | --- |
| `pii_detection`, `profanity_filter` | Set `enabled: false`. The policy stays attached but takes no action. |
| `harmful_content` | Set each category's filter to `strength: "NONE"` to disable it. `filters` must stay non-empty (an empty array returns `422`), so a fully disabled policy keeps all five entries at `strength: "NONE"`. Sending `enabled` returns `422`. |
| `prompt_attack` | Set `strength: "NONE"`. Sending `enabled` returns `422`. |
| `custom_word_filter` | Send `custom_words: []` to clear the list. |
| `topic_boundary` | `topics` must be non-empty. Reconfigure the topics rather than emptying the array. |

`NONE` is a valid `strength` value and is used by the genie builder UI to turn `prompt_attack` and `harmful_content` off. The two default policies, `prompt_attack` and `harmful_content`, are present after a guardrail is attached. You can turn off these policies with `strength: "NONE"`, but you can't remove the policies.

### Get a genie guardrail

Returns the guardrail and its policies for the genie associated with the ID you specify.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/genies/:genie_id/guardrails
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_id | **string** _required_ | The ID of the genie whose guardrail you plan to retrieve. Genie handles begin with `gin-`. For example `gin-aBC123-xYz789-prod1`. |

##### Sample request

<api-code>

```shell
curl -sS https://YOUR_DATA_CENTER/api/agentic/genies/:id/guardrails \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
  "data": {
    "id": "aigrl-aBC123-xYz789-prod1",
    "policies": [
      {
        "id": "aigrlp-aBC123-pQr456-prod1",
        "policy_type": "harmful_content",
        "configuration": {
          "filters": [
            { "type": "HATE",        "strength": "LOW" },
            { "type": "INSULTS",     "strength": "LOW" },
            { "type": "SEXUAL",      "strength": "LOW" },
            { "type": "VIOLENCE",    "strength": "LOW" },
            { "type": "MISCONDUCT",  "strength": "LOW" }
          ]
        }
      },
      {
        "id": "aigrlp-aBC123-sTu789-prod1",
        "policy_type": "prompt_attack",
        "configuration": { "strength": "LOW" }
      }
    ]
  }
}
```

##### Sample response

```json
{ "data": { "id": null, "policies": [] } }
```

#### Error responses

| Status | When |
| --- | --- |
| `401 Unauthorized` | Missing or invalid API token. |
| `404 Not Found` | Genie handle unknown, outside your folder scope, or the `genie_guardrails_enabled` flag is off. |

* * *

### Create or update a policy

Creates or updates a single guardrail policy on the genie associated with the ID you specify. A new policy is created if no policy exists for the `policy_type` you provide. Otherwise the existing policy's configuration is replaced in full. You must send the complete configuration you plan to use. Partial updates aren't supported.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/agentic/genies/:id/guardrails/policies/:policy_type
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_id | **string** _required_ | The ID of the genie whose policy you plan to create or update. |
| policy\_type | **string** _required_ | The type of policy to create or update. Accepted values: `harmful_content`, `prompt_attack`, `pii_detection`, `topic_boundary`, `profanity_filter`, `custom_word_filter`. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| configuration | **object** _required_ | The policy configuration. Shape varies by `policy_type`. Refer to [Policy types](#policy-types) for more information. |

##### Sample request

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/agentic/genies/:id/guardrails/policies/:policy_type \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "configuration": {
             "filters": [
               { "type": ":policy_type","strength": ":strength-level" },
               { "type": ":policy_type","strength": ":strength-level" },
               { "type": ":policy_type","strength": ":strength-level" },
               { "type": ":policy_type","strength": ":strength-level" },
               { "type": ":policy_type","strength": ":strength-level" }
             ]
           }
         }'
```

</api-code>

##### Sample response

```json
{
  "data": {
    "id": "aigrlp-aBC123-pQr456-prod1",
    "policy_type": "harmful_content",
    "configuration": {
      "filters": [
        { "type": "HATE",       "strength": "HIGH" },
        { "type": "INSULTS",    "strength": "HIGH" },
        { "type": "SEXUAL",     "strength": "HIGH" },
        { "type": "VIOLENCE",   "strength": "MEDIUM" },
        { "type": "MISCONDUCT", "strength": "MEDIUM" }
      ]
    }
  }
}
```

#### Error responses

| Status | When |
| --- | --- |
| `400 Bad Request` | `policy_type` isn't one of the six valid values. |
| `401 Unauthorized` | Missing or invalid API token. |
| `404 Not Found` | Genie not found, no guardrail attached to the genie, or the feature flag is off. |
| `422 Unprocessable Entity` | `configuration` failed validation. This can be caused by missing a required field, an unknown key, an invalid enum value, or if the request exceeds quotas. |

##### Sample 422 response

```json
{
  "errors": [
    {
      "code": 422,
      "title": "Failed to update policy",
      "detail": "Configuration contains unknown keys: junk"
    }
  ]
}
```

* * *

### List available PII entity types

Returns the list of PII entity type strings you can use in a `pii_detection` policy's `pii_entities[].type` field. This list isn't specific to your current environment.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/genies/guardrails/policies/pii_entities
```

</api-code>

##### Sample request

<api-code>

```shell
curl -sS https://YOUR_DATA_CENTER/api/agentic/genies/guardrails/policies/pii_entities \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
  "data": [
    "ADDRESS", "AGE", "AWS_ACCESS_KEY", "AWS_SECRET_KEY",
    "CA_HEALTH_NUMBER", "CA_SOCIAL_INSURANCE_NUMBER",
    "CREDIT_DEBIT_CARD_CVV", "CREDIT_DEBIT_CARD_EXPIRY", "CREDIT_DEBIT_CARD_NUMBER",
    "DRIVER_ID", "EMAIL", "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
    "IP_ADDRESS", "LICENSE_PLATE", "MAC_ADDRESS", "NAME",
    "PASSWORD", "PHONE", "PIN", "SWIFT_CODE",
    "UK_NATIONAL_HEALTH_SERVICE_NUMBER", "UK_NATIONAL_INSURANCE_NUMBER", "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
    "URL", "USERNAME",
    "US_BANK_ACCOUNT_NUMBER", "US_BANK_ROUTING_NUMBER",
    "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER", "US_PASSPORT_NUMBER", "US_SOCIAL_SECURITY_NUMBER",
    "VEHICLE_IDENTIFICATION_NUMBER"
  ]
}
```

* * *

### Policy types

Each `policy_type` accepts a specific `configuration` shape. Sending unknown top-level keys fails with `422`.

#### harmful\_content

Filters user input and model output for categories of harmful content.

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `filters` | array | yes | Non-empty. Each element is `{ "type": <category>, "strength": <strength> }`. |
| `filters[].type` | string | yes | One of `HATE`, `INSULTS`, `SEXUAL`, `VIOLENCE`, `MISCONDUCT`, `PROMPT_ATTACK`. |
| `filters[].strength` | string | yes | One of `NONE`, `LOW`, `MEDIUM`, `HIGH`. Use `NONE` or omit the entry to disable the category. |

```json
{
  "configuration": {
    "filters": [
      { "type": "HATE",       "strength": "HIGH" },
      { "type": "INSULTS",    "strength": "HIGH" },
      { "type": "SEXUAL",     "strength": "HIGH" },
      { "type": "VIOLENCE",   "strength": "MEDIUM" },
      { "type": "MISCONDUCT", "strength": "MEDIUM" }
    ]
  }
}
```

#### prompt\_attack

Detects attempts to override system instructions, jailbreak, or otherwise manipulate the genie within the user's prompt.

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `strength` | string | yes | One of `NONE`, `LOW`, `MEDIUM`, `HIGH`. Use `NONE` to turn off the policy. |

```json
{ "configuration": { "strength": "HIGH" } }
```

#### pii\_detection

Detects PII in chat content and blocks, anonymizes, or tokenizes it. You can match by built-in entity type, custom regex, or both.

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `enabled` | boolean | yes | Enables the feature. Other fields are accepted but ignored when set to `false`. |
| `action` | string | yes | One of `BLOCK`, `ANONYMIZE`, `TOKENIZE`. Required even when `enabled` is `false`. |
| `pii_entities` | array | conditional | Required (non-empty) if `enabled` is `true` and `pii_custom_regexes` is empty or absent. Each element is `{ "type": <entity> }`. Use [List available PII entity types](#list-pii-entity-types) to view valid values. |
| `pii_custom_regexes` | array | conditional | Required (non-empty) if `enabled` is `true` and `pii_entities` is empty or absent. Up to 10 entries. Each is `{ "name": <label>, "pattern": <regex> }`. |
| `pii_custom_regexes[].name` | string | yes | Non-blank label shown in audit logs. |
| `pii_custom_regexes[].pattern` | string | yes | Valid regular expression. Must be less than 500 characters. |

```json
{
  "configuration": {
    "enabled": true,
    "action": "ANONYMIZE",
    "pii_entities": [
      { "type": "EMAIL" },
      { "type": "PHONE" },
      { "type": "CREDIT_DEBIT_CARD_NUMBER" },
      { "type": "US_SOCIAL_SECURITY_NUMBER" }
    ],
    "pii_custom_regexes": []
  }
}
```

#### topic\_boundary

Restricts the conversation to specific topics. Optional example utterances help the model classify borderline cases.

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `topics` | array | yes | Non-empty. Up to 30 topics. |
| `topics[].name` | string | yes | Must be less than 50 characters. Non-blank. |
| `topics[].description` | string | no | Must be less than 300 characters. |
| `topics[].examples` | array of strings | no | Up to 5 examples, each must be less than 300 characters. |

```json
{
  "configuration": {
    "topics": [
      {
        "name": "Investment advice",
        "description": "Refuse to provide personalized financial or investment advice; suggest the user contact a licensed advisor.",
        "examples": [
          "Should I buy NVDA stock?",
          "How should I allocate my 401(k)?",
          "Is now a good time to invest in crypto?"
        ]
      }
    ]
  }
}
```

#### profanity\_filter

The profanity filter can be enabled or disabled.

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `enabled` | boolean | yes | `true` to enable, `false` to disable. |

```json
{ "configuration": { "enabled": true } }
```

#### custom\_word\_filter

Blocks messages containing any of an explicit list of words or short phrases.

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `custom_words` | array of strings | yes | Up to 100 entries. Each entry must be less than 50 characters. Send an empty array to clear the list. |

```json
{
  "configuration": {
    "custom_words": ["Project Atlas", "Operation Falcon", "internal-only"]
  }
}
```

## Knowledge bases

### List knowledge bases

Returns a list of knowledge bases.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/knowledge_bases
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| folder\_id | **string** _optional_ | The ID of the folder where the knowledge base resides. |
| project\_id | **string** _optional_ | The ID of the project where the knowledge base resides. |
| query | **string** _optional_ | Search query. |
| page | **integer** _optional_ | Page number of the knowledge base to fetch. Minimum value is `1`. |
| per\_page | **integer** _optional_ | Number of knowledge bases to return in a single page. Minimum value is `1`. Maximum value is `50`. |
| sort\_term | **string** _optional_ | The field or term to sort results by. For example: `name` or `latest_activity`. |
| genie\_ids\[\] | **array of string** _optional_ | An array of genie IDs to filter results by. Returns only knowledge bases assigned to at least one of the genies you specify. |

###### Sample request

<api-code>

``` shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/knowledge_bases \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "per_page": :per_page_value,
           "page": :page_value,
           "sort_term": ":sort_term"
         }'

```

</api-code>

###### Sample response

Each knowledge base includes a `genies[]` array of the genies it's assigned to.

```json
[
  {
    "id": "kb-WSm8kore-blMxrh",
    "name": "Support FAQs",
    "description": "Knowledge base with frequently asked customer support questions.",
    "folder_id": "7498",
    "project_id": "4567",
    "genies": [
      {
        "id": "gin-BWLSPX4z-BaT3D9",
        "name": "Customer Support Genie"
      }
    ]
  },
  {
    "id": "kb-BLm8cove-brMxrh",
    "name": "Sales Playbook",
    "description": "Guidelines and resources for the sales team.",
    "folder_id": "7302",
    "project_id": "9876",
    "genies": []
  }
]
```

### Create a knowledge base

Creates a new knowledge base.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/knowledge_bases
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name of the knowledge base. |
| description | **string** _required_ | A description of the knowledge base. |
| folder\_id | **string** _required_ | The ID of the folder where the knowledge base resides. |
| source\_type | **string** _required_ | The source of the knowledge base, such as a recipe. |
| data\_sources | **string** _required_ | Configure data sources for the knowledge base. |

###### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/knowledge_bases \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":name",
           "description": ":description",
           "folder_id": ":folder_id",
           "source_type": ":source_type",
           "data_sources": ":data_sources"
         }'
```

</api-code>

###### Sample response

```json
{
  "id": "kb-BRm8coke-rhMxsa",
  "name": "Support FAQs",
  "description": "Knowledge base with frequently asked customer support questions.",
  "folder_id": "7498",
  "source_type": "recipe",
  "data_sources": "zendesk_articles"
```

### Get a knowledge base by ID

Returns the knowledge base associated with the ID you specify.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the knowledge base you plan to retrieve. |

###### Sample request

<api-code>

``` shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

###### Sample response

```json
[
  {
    "id": "kb-WSm8kore-blMxrh",
    "name": "Support FAQs",
    "description": "Knowledge base with frequently asked customer support questions.",
    "folder_id": "7498",
    "project_id": "4567"
  }
]
```

### Update a knowledge base

Updates an existing knowledge base.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the knowledge base you plan to update. |
| name | **string** _optional_ | The name of the knowledge base. |
| description | **string** _optional_ | The description of the knowledge base. |
| folder\_id | **string** _optional_ | The ID of the folder where the knowledge base resides. |
| data\_sources | **object** _optional_ | The configured data sources for the knowledge base. |

##### Sample request

<api-code>

```shell
curl -X PUT https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "name": ":name",
           "description": ":description",
           "data_sources": {
             ":data-source-name": :true_or_false,
             ":data-source-name": :true_or_false
           }
         }'
```

</api-code>

##### Sample response

```json
{
  "id": "kb-WSm8kore-blMxrh",
  "name": "Support FAQs v2",
  "description": "Updated to include billing FAQs in addition to support.",
  "folder_id": "7498",
  "source_type": "recipe",
  "data_sources": {
    "zendesk_articles": true,
    "internal_docs": true
  }
}
```

### Delete a knowledge base

Deletes a knowledge base.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the knowledge base you plan to delete. |

##### Sample request

<api-code>

```shell
curl -X DELETE https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

##### Sample response

```json
{
    "success": "true"
}
```

### Get knowledge base data sources

Returns the data sources associated with the knowledge base ID you specify.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id/data_sources
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the knowledge base for which you plan to retrieve data sources. |

##### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id/data_sources \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Sample response

```json
{
  "knowledge_base_id": "kb-WSm8kore-blMxrh",
  "data_sources": {
    "zendesk_articles": true,
    "internal_docs": true,
    "slack_channels": false
  }
}
```

### Get knowledge base recipes

Returns the recipes associated with the knowledge base ID you specify.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id/recipes
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the knowledge base for which you plan to retrieve associated recipes. |
| query | **string** _optional_ | Search query. |
| page | **integer** _optional_ | Page number of the genies to fetch. Minimum value is `1`. |
| per\_page | **integer** _optional_ | Number of genies to return in a single page. Minimum value is `1`. Maximum value is `50`. |
| sort\_term | **string** _optional_ | The field or term to sort results by. For example: `name` or `latest_activity`. |

##### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/knowledge_bases/:id/recipes \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "per_page": :per_page_value,
           "page": :page_value,
           "sort_term": ":sort_term"
         }'
```

</api-code>

##### Sample response

```json
[
  {
    "id": 45246391,
    "name": "Customer Support Escalation",
    "description": "Routes high-priority Zendesk tickets to Slack.",
    "knowledge_base_id": "kb-WSm8kore-blMxr/recipes"
  },
  {
    "id": 87654321,
    "name": "Billing Notifications",
    "description": "Sends alerts for overdue invoices to the finance team.",
    "knowledge_base_id": "kb-WSm8kore-blMxr/recipes"
  }
]
```

## Skills

Use the following endpoints to work with skills programmatically:

### List skills

Returns a list of skills.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/skills
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| folder\_id | **string** _optional_ | The ID of the folder where the genie resides. |
| project\_id | **string** _optional_ | The ID of the project where the genie resides. |
| query | **string** _optional_ | Search query. |
| page | **integer** _optional_ | Page number of the genies to fetch. Minimum value is `1`. |
| per\_page | **integer** _optional_ | Number of genies to return in a single page. Minimum value is `1`. Maximum value is `50`. |
| sort\_term | **string** _optional_ | The field or term to sort results by. For example: `name` or `latest_activity`. |
| genie\_ids\[\] | **array of string** _optional_ | An array of genie IDs to filter results by. Returns only skills and MCP servers assigned to at least one of the genies you specify. |

##### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/skills \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "per_page": :per_page_value,
           "page": :page_value,
           "sort_term": ":sort_term"
         }'
```

</api-code>

##### Sample response

The response includes both recipe-based skills and MCP servers. Use `type` to tell recipe-based skills and MCP servers apart. Each entry includes a `genies[]` array of the genies it's assigned to.

```json
[
  {
    "id": 65001201,
    "name": "Zendesk Ticket Management",
    "description": "Skill for handling customer support tickets from Zendesk.",
    "type": "recipe",
    "folder_id": "7498",
    "project_id": "4567",
    "genies": [
      {
        "id": "gin-BWLSPX4z-BaT3D9",
        "name": "Customer Support Genie"
      }
    ]
  },
  {
    "id": 65039789,
    "name": "Slack Notifications",
    "description": "Skill for sending targeted Slack alerts.",
    "type": "recipe",
    "folder_id": "7302",
    "project_id": "4567",
    "genies": []
  },
  {
    "id": "<mcp_server_id>",
    "name": "Salesforce MCP server",
    "description": "MCP server that exposes Salesforce tools.",
    "type": "<mcp_server_type_value>",
    "folder_id": "7302",
    "project_id": "4567",
    "genies": []
  }
]
```

### Create a skill from an existing recipe

Converts an existing recipe into a skill. The recipe must use a [Start workflow](/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow) trigger with defined inputs and actions. Call this endpoint with the `recipe_id` to register the recipe as a skill in Agent Studio.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/agentic/skills
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| recipe\_id | **integer** _required_ | The ID of the recipe to convert into a skill. |

##### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/agentic/skills \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "recipe_id": :recipe_id
         }'
```

</api-code>

##### Sample response

```json
{
  "name": "Customer Escalation Skill",
  "description": "Skill automatically routes high-priority Zendesk tickets to Slack.",
  "recipe_id": 65039789,
  "folder_id": "7498",
  "project_id": "4567"
}
```

### Get a skill by ID

Returns the skill associated with the ID you specify.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/agentic/skills/:id
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the skill for you plan to retrieve. |

##### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/agentic/skills/:id \
     -H 'Authorization: Bearer <api_token>' \
```

</api-code>

##### Sample response

```json
{
  "name": "Customer Escalation Skill",
  "description": "Skill automatically routes high-priority Zendesk tickets to Slack.",
  "recipe_id": 65039789,
  "folder_id": "7498",
  "project_id": "4567"
}
```

---
