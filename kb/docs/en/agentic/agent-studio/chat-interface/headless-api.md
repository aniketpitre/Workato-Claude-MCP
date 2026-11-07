---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/chat-interface/headless-api.md
description: Enable your application to talk to your genie directly over a REST API.
---

# Headless API

The [custom chat interface](/en/agentic/agent-studio/chat-interface/chat-interface#configure-a-custom-chat-interface) lets you connect your genie to any application you build and control. Your application talks to your genie directly over a REST API, called a Headless API, instead of routing users through Slack, Microsoft Teams, or Workato GO.

> **HEADLESS API ENDPOINTS REQUIRE A CUSTOM CHAT INTERFACE**
> 
> Headless API endpoints are only compatible with the [custom chat interface](/en/agentic/agent-studio/chat-interface/chat-interface#configure-a-custom-chat-interface) option.

The custom chat interface includes API endpoints to manage conversations and send and receive genie messages. This API is separate from the [Agent Studio Developer API](/en/workato-api/agent-studio#agent-studio), which lets you create, configure, and maintain genies.

## Headless API prerequisites

Confirm you have the following requirements to use Headless API:

- You have a genie in Agent Studio.
- You've set up the genie's [custom chat interface](/en/agentic/agent-studio/chat-interface/chat-interface#configure-a-custom-chat-interface) from the Agent Studio UI, including creating and attaching a genie client with either API key or OAuth 2.0 (PKCE) credentials. Refer to [Genie clients](/en/workato-api/agent-studio#genie-clients) in the Developer API if you provision the client programmatically instead of through the UI.
- Your builder role has the **Custom chat interface** privilege under **Genie building**. Refer to [collaborator privileges](/en/privileges#custom-chat-interface) for more information on configuring builder roles.

## Headless API base URLs

Headless API is available in all data centers where Agentic is supported. The base URLs follow the same per-data-center scheme as the app host. For example:

| Data center | Dev API base URL | Headless API base URL |
| --- | --- | --- |
| US | `https://app.workato.com` | `https://genie-api.workato.com` |

Refer to the [data center overview](/en/datacenter/datacenter-overview) for more information.

## Authentication

Headless API supports the following access methods:

**API key:**

```http
Authorization: Bearer <api_key>
X-IDP-User-Id: <idp_user_id>
```

**OAuth 2.0 (PKCE):**

```http
Authorization: Bearer <access_token>
```

### Authorization methods comparison

Refer to the following authorization method comparison and use case recommendation tables to determine which authorization method to use:

| Comparison point | API key (token-based) | OAuth 2.0 (PKCE) |
| --- | --- | --- |
| **How it works** | The builder's backend holds a static API key and asserts user identity through the `X-IDP-User-Id` header. | End users authenticate directly through Workato Identity and delegate to the customer's IdP through SAML SSO. |
| **End user visibility** | Workato is invisible to end users. | End users see an IdP login step. |
| **Required headers** | `Authorization: Bearer <api_key>` and `X-IDP-User-Id: <idp_user_id>` | `Authorization: Bearer <access_token>` |
| **Client credentials** | The API key is static and is shown only once. | `client_id` only — PKCE replaces the client secret. |
| **User identity managed by** | The builder maps user IDs to Workato IdP user IDs. | IdP directly, such as Okta, Microsoft Entra ID, OneLogin, and more. |
| **Prerequisites** | End users provisioned in Workato Identity through IAM API or the Workato UI. | One-time SAML federation between Workato Identity and the customer's existing IdP. Workato Identity acts as a broker. It doesn't replace the customer's IdP. |
| **Recommended for** | Server-side integrations, QA, automated testing, internal tools. | User-facing apps requiring SSO, centralized access governance, and per-user permissions. |

### Recommended authorization method by scenario

| Scenario | Recommended |
| --- | --- |
| QA / automated testing | API key |
| Security red-teaming through CI/CD | API key |
| Internal tool with builder-controlled authorization | API key |
| Custom chat UI where Workato should be invisible | API key |
| Employee portal with company SSO | OAuth 2.0 |
| Multi-tenant app serving multiple organizations | OAuth 2.0 |
| Deployment requiring IdP-governed access control | OAuth 2.0 |
| Mobile or single-page app or public client | OAuth 2.0 |

### OAuth 2.0 PKCE authorization flow

OAuth clients authenticate end users through Workato Identity (`id.workato.com`) using the authorization code flow with PKCE. No client secret is required. Use the `oauth_client_id` returned when you [create an OAuth genie client](/en/workato-api/agent-studio#create-a-genie-client).

You must complete the following steps to use this authorization flow:

1. Generate a `code_verifier` to create a random, URL-safe string of 43–128 characters and derive the `code_challenge` as `base64url(sha256(code_verifier))`.
   
2. Redirect the user to the authorization endpoint:
   
   ```plaintext
   https://id.workato.com/oauth/authorize?response_type=code
     &client_id=<oauth_client_id>
     &redirect_uri=<your_redirect_url>
     &scope=openid profile email
     &state=<random_state>
     &code_challenge=<code_challenge>
     &code_challenge_method=S256
   ```
   
3. Verify `state` matches when Workato Identity redirects to your `redirect_uri` with a `code` and the original `state`.
   
4. Exchange the code for tokens at `https://id.workato.com/oauth/token` with a form-encoded body. Don't send the client secret:
   
   <api-code>

   ```
   curl -X POST https://id.workato.com/oauth/token \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=authorization_code" \
     -d "client_id=<oauth_client_id>" \
     -d "redirect_uri=<your_redirect_url>" \
     -d "code=<authorization_code>" \
     -d "code_verifier=<code_verifier>"
   ```

   </api-code>
   
5. Use the returned `access_token` as `Authorization: Bearer <access_token>` on Headless API calls. The token response also includes a `refresh_token` and an `id_token`.
   
6. Refresh the access token before it expires (`expires_in` is `3600` seconds) to avoid forcing the user through an interactive login again. Exchange the `refresh_token` at `https://id.workato.com/oauth/token` to obtain a new access token silently:
   
   <api-code>

   ```
   curl -X POST https://id.workato.com/oauth/token \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=refresh_token" \
     -d "client_id=<oauth_client_id>" \
     -d "refresh_token=<refresh_token>"
   ```

   </api-code>
   
   Refresh tokens are single-use and rotating: each refresh returns a new `refresh_token`. Persist the new value for the next refresh. Request the default `openid profile email` scope and don't add `offline_access`, which Workato Identity rejects.
   

The redirect URL must match the `oauth_redirect_url` registered on the client. Perform the code exchange in the preceding steps from a same-origin backend rather than directly in the browser. This ensures the flow is free of cross-origin (CORS) concerns and keeps token handling server-side.

* * *

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v1/genies/:genie\_handle/chat/conversations](#list-conversations) | List a user's conversations. |
| POST | [/api/v1/genies/:genie\_handle/chat/conversations](#create-a-conversation) | Create a new conversation. |
| GET | [/api/v1/genies/:genie\_handle/chat/conversations/ :conversation\_id](#get-a-conversation) | Get conversation details and state. |
| GET | [/api/v1/genies/:genie\_handle/chat/conversations/ :conversation\_id/messages](#get-messages) | Get message history for a conversation. |
| POST | [/api/v1/genies/:genie\_handle/chat/conversations/ :conversation\_id/messages](#send-a-message) | Send a message and receive a streaming response. |
| GET | [/api/v1/genies/:genie\_handle/chat/conversations/ :conversation\_id/genie-runs/:genie\_run\_id](#reconnect-to-a-stream) | Reconnect to a message stream. |
| GET | [/api/v1/genies/:genie\_handle/chat/ conversations/events](#get-events) | Get recent events. |
| POST | [/api/v1/genies/:genie\_handle/chat/conversations/ :conversation\_id/skill\_approval/:call\_id](#approve-or-reject-a-skill) | Approve or reject a skill confirmation. |
| POST | [/api/v1/genies/:genie\_handle/chat/conversations/ :conversation\_id/business\_approval/:call\_id](#approve-or-reject-a-business-approval) | Approve or reject a business approval request. |
| POST | [/api/v1/genies/:genie\_handle/chat/ runtime\_connection/:runtime\_connection\_attempt\_id/link](#get-a-runtime-connection-link) | Get an authentication link for a runtime connection. |
| POST | [/api/v1/genies/:genie\_handle/chat/ runtime\_connection/:runtime\_connection\_attempt\_id/reject](#reject-a-runtime-connection) | Reject a runtime connection request. |
| POST | [/api/v1/genies/:genie\_handle/chat/conversations/ :conversation\_id/upload](#upload-a-file) | Upload a file for attachment to a message. |
| POST | [/api/v1/genies/:genie\_handle/chat/conversations/ :conversation\_id/genie-runs/:genie\_run\_id/feedback](#submit-feedback) | Submit user feedback for a genie run. |
| POST | [/api/v1/genies/:genie\_handle/task](#send-a-genie-task) | Send a task to a genie. |

* * *

## List conversations

Retrieve a list of the authenticated user's conversations. Results are listed by the `created_at` timestamp in descending order.

<api-code no-copy-method>

```
GET /api/v1/genies/:genie_handle/chat/conversations
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| limit | **integer** _optional_ | Number of conversations to return. Defaults to `50`. |
| cursor | **string** _optional_ | Pagination cursor from a previous response. |

### Response

| Name | Type | Description |
| --- | --- | --- |
| list\[\] | **array** | List of conversations. |
| list\[\].conversation\_id | **string** | Conversation ID. |
| list\[\].topic | **string** | Conversation topic. |
| list\[\].last\_updated\_at | **string** | Timestamp of the last update. |
| list\[\].created\_at | **string** | Timestamp when the conversation was created. |
| total\_count | **integer** | Total number of conversations. |
| cursor | **string** | Cursor for the next page of results. |

* * *

## Create a conversation

Create a new conversation with the genie.

<api-code no-copy-method>

```
POST /api/v1/genies/:genie_handle/chat/conversations
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |

### Response

| Name | Type | Description |
| --- | --- | --- |
| conversation\_id | **string** | ID of the new conversation. |

* * *

## Get a conversation

Retrieve the details and current state of a conversation.

<api-code no-copy-method>

```
GET /api/v1/genies/:genie_handle/chat/conversations/:conversation_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| conversation\_id | **string** _required_ | Conversation ID. |

### Response

| Name | Type | Description |
| --- | --- | --- |
| updated\_at | **string** | Timestamp of the last update. |
| state | **string** | Current state of the conversation. One of `idle` (no active turn), `ai_running` (the model is generating), `skill_processing` (a skill is executing — including while the turn is paused on a runtime-connection authorization), or `awaiting_approval` (paused on a `skill.confirmation_required`). |
| last\_event | **object** | The most recent event in the conversation. |

* * *

## Get messages

Retrieve message history for a conversation. Results are listed by the `created_at` timestamp in descending order.

<api-code no-copy-method>

```
GET /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/messages
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| conversation\_id | **string** _required_ | Conversation ID. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| cursor | **string** _optional_ | Pagination cursor from a previous response. |
| limit | **integer** _optional_ | Number of messages to return. Defaults to `100`. |

### Response

| Name | Type | Description |
| --- | --- | --- |
| conversation\_id | **string** | Conversation ID. |
| messages\[\] | **array** | List of messages. |
| messages\[\].message\_id | **string** | Message ID. |
| messages\[\].source | **string** | Message origin. One of `user` or `genie`. |
| messages\[\].content | **string** | Text content of the message. |
| messages\[\].genie\_run\_id | **string** | ID of the request/response cycle the message belongs to. |
| messages\[\].created\_at | **string** | Timestamp of the message in RFC3339 format. |
| total\_count | **integer** | Total number of messages in the conversation. |
| cursor | **string** | Cursor for the next page of results. |

* * *

## Send a message

Send a user message and receive a real-time stream of events as the genie processes and responds.

<api-code no-copy-method>

```
POST /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/messages
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| conversation\_id | **string** _required_ | Conversation ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| message | **string** _required_ | The user's message. Maximum 12 KB. |
| file\_id | **string** _optional_ | ID of a previously uploaded file to attach to this message. |
| stream | **boolean** _optional_ | Set to `true` to receive an SSE stream in the response. Defaults to `false`. |

### Response

When `stream` is `false`, returns HTTP 202 with the following body:

| Name | Type | Description |
| --- | --- | --- |
| conversation\_id | **string** | Conversation ID. |
| genie\_run\_id | **string** | ID of the genie run. Use this to reconnect to the stream. |

When `stream` is `true`, the response is a stream of [Server-Sent Events](#sse-events). The stream closes when the genie finishes processing, and indicates the finished process with the `processing.finished` event. Check the `reason` field. A new genie run starts after the approval is decided if the reason is `business_approval_pending`.

* * *

## Reconnect to a stream

Reopen the SSE stream for a specific genie run. Use this to recover events after a disconnection. Pass the ID of the last successfully received event in the `Last-Event-ID` header. Don't reconnect after a `processing.finished` event with a `business_approval_pending` reason. The stream closes intentionally, and the next events arrive in a new genie run.

<api-code no-copy-method>

```
GET /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/genie-runs/:genie_run_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| conversation\_id | **string** _required_ | Conversation ID. |
| genie\_run\_id | **string** _required_ | Genie run ID, as returned by [Send a message](#send-a-message). |

### Headers

| Name | Type | Description |
| --- | --- | --- |
| Last-Event-ID | **string** _optional_ | ID of the last successfully received event. The stream replays events from this point. |

### Response

The response is a stream of [Server-Sent Events](#sse-events).

* * *

## Get events

Retrieve recent events. Use this as a fallback to manually fetch missed events after a disconnection. Events are returned oldest first and are available for 24 hours.

<api-code no-copy-method>

```
GET /api/v1/genies/:genie_handle/chat/conversations/events
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| since\_created\_at | **string** _optional_ | Lower bound (inclusive) on event creation time, as an RFC3339 timestamp (for example, `2026-05-26T12:00:00.123456Z`). Pass `next_since_created_at` from the previous response to fetch the next page. |
| conversation\_id | **string** _optional_ | Filter events by conversation ID. |
| limit | **integer** _optional_ | Page size. Defaults to `100`. |

### Response

| Name | Type | Description |
| --- | --- | --- |
| events\[\] | **array** | Array of events, ordered oldest first. |
| events\[\].conversation\_id | **string** | Conversation ID. |
| events\[\].genie\_handle | **string** | Genie handle (string identifier, for example `gin-AaDX9axF-CNtgQn-B6`). |
| events\[\].genie\_run\_id | **string** | ID of the genie run this event belongs to. |
| events\[\].type | **string** | Event type. |
| events\[\].event\_id | **string** | UUIDv7 identifying this event. |
| events\[\].seq\_num | **integer** | Per-genie-run monotonic sequence number. |
| events\[\].created\_at | **string** | Gateway-side timestamp when the event was persisted, in RFC3339 format. |
| next\_since\_created\_at | **string** | Continuation cursor. When present, pass this value as `since_created_at` on the next request to fetch the next page. |

* * *

## Approve or reject a skill

Approve or reject a skill confirmation request. Use this when the genie emits a `skill.confirmation_required` event.

<api-code no-copy-method>

```
POST /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/skill_approval/:call_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| conversation\_id | **string** _required_ | Conversation ID. |
| call\_id | **string** _required_ | Call ID from the `skill.confirmation_required` event. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| resolution | **string** _required_ | One of `approved` or `rejected`. |
| rejection\_reason | **string** _optional_ | Reason for rejection. Only used when `resolution` is `rejected`. |

* * *

## Approve or reject a business approval

Submit an approver's decision for a business approval identified by `call_id`.

<api-code no-copy-method>

```
POST /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/business_approval/:call_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| conversation\_id | **string** _required_ | Conversation ID. |
| call\_id | **string** _required_ | Call ID of the business approval to resolve. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| resolution | **string** _required_ | One of `approved` or `rejected`. |
| rejection\_reason | **string** _optional_ | Reason for rejection. Only used when `resolution` is `rejected`. |

* * *

## Get a runtime connection link

Get an authentication link for a runtime connection. Use this when the genie emits a `runtime_connection.auth_required` event.

<api-code no-copy-method>

```
POST /api/v1/genies/:genie_handle/chat/runtime_connection/:runtime_connection_attempt_id/link
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| runtime\_connection\_attempt\_id | **string** _required_ | Server-generated ID for the pending runtime-connection authorization attempt, as delivered in the `runtime_connection.auth_required` SSE event. |

### Response

| Name | Type | Description |
| --- | --- | --- |
| status | **string** | One of `auth_required` or `authorized`. When `authorized`, the connection is already complete and no user action is needed. |
| auth\_link.url | **string** | Authentication URL to present to the user. Only present when `status` is `auth_required`. |
| auth\_link.expires\_at | **string** | Expiration time of the authentication URL in RFC3339 format. Only present when `status` is `auth_required`. |
| auth\_link.connector\_name | **string** | Human-readable connector label (for example, `Salesforce`, `Google Drive`). Only present when `status` is `auth_required`. |

* * *

## Reject a runtime connection

Reject a runtime connection request. The genie emits a `runtime_connection.auth_failed` event with the reason `rejected_by_user`, and the skill doesn't run with that connection.

<api-code no-copy-method>

```
POST /api/v1/genies/:genie_handle/chat/runtime_connection/:runtime_connection_attempt_id/reject
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| runtime\_connection\_attempt\_id | **string** _required_ | Server-generated ID for the pending runtime-connection authorization attempt, as delivered in the `runtime_connection.auth_required` SSE event. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| reason | **string** _optional_ | Reason for rejection. |

* * *

## Upload a file

Upload a file to attach to a subsequent message. Returns a `file_id` to pass in the `file_id` parameter of [Send a message](#send-a-message). The maximum file size is 20 MB.

<api-code no-copy-method>

```
POST /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/upload
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| conversation\_id | **string** _required_ | Conversation ID. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| file | **file** _required_ | File data (multipart/form-data). Maximum size is 20 MB. |

### Response

| Name | Type | Description |
| --- | --- | --- |
| file\_id | **string** | ID of the uploaded file. |

* * *

## Submit feedback

Submit user feedback through a positive or negative reaction and an optional comment for the AI response produced by a genie run.

<api-code no-copy-method>

```
POST /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/genie-runs/:genie_run_id/feedback
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |
| conversation\_id | **string** _required_ | Conversation ID. |
| genie\_run\_id | **string** _required_ | Genie run ID whose response the feedback is about. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| reaction | **string** _required_ | The user's reaction to the AI response. One of `positive` or `negative`. |
| comment | **string** _optional_ | Free-form comment accompanying the reaction. Maximum 10,000 characters. |

* * *

## Send a genie task

Send a task to a genie and get a result synchronously or asynchronously. Use this endpoint for programmatic, system-to-system work, such as running multiple related tasks or triggering a genie from a backend process. Use the [conversation endpoints](#create-a-conversation) for chat interfaces.

> **SEND A GENIE TASK ONLY FOR HEADLESS API**
> 
> This endpoint uses the Headless API gateway, not the Developer API. It supports API key authentication only. OAuth 2.0 isn't supported. Send only `Authorization: Bearer <api_key>`. Don't send the `X-IDP-User-Id` header. No user ID is required.

<api-code no-copy-method>

```
POST /api/v1/genies/:genie_handle/task
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| genie\_handle | **string** _required_ | Genie handle. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| request\_text | **string** _required_ | The task for the genie to perform. |
| context\_id | **string** _optional_ | An ID that connects multiple genie tasks. Pass the same `context_id` on related tasks to link the executions. |
| callback\_url | **string** _optional_ | A URL Workato sends a notification to when the task completes. |

### Response

Returns HTTP 200 with the following body:

| Name | Type | Description |
| --- | --- | --- |
| task\_id | **string** | ID of the task. |
| conversation\_id | **string** | ID of the conversation the task runs in. |
| response\_url | **string** | URL to retrieve the task response. |
| status | **string** | Whether the genie accepted the task. One of `accepted` or `rejected`. |

## SSE events

You can send a message with `stream: true` to get a response with a stream of SSE covering the full lifecycle of the genie's response.

Events are persisted for 24 hours and are retrievable through the [Get events](#get-events) endpoint.

### Base event shape

Every event shares the following base fields:

| Field | Type | Description |
| --- | --- | --- |
| `conversation_id` | **string** | Conversation ID. |
| `genie_handle` | **string** | Genie handle (string identifier, for example `gin-AaDX9axF-CNtgQn-B6`). |
| `genie_run_id` | **string** | ID of the genie run this event belongs to. |
| `type` | **string** | Event type. |
| `event_id` | **string** | UUIDv7 identifying this event. |
| `seq_num` | **integer** | Per-genie-run monotonic sequence number. |
| `created_at` | **string** | Gateway-side timestamp when the event was persisted, in RFC3339 format. |

### Event types

| Event | Additional fields | Description |
| --- | --- | --- |
| `processing` `.started` |  | Genie has begun processing the request. |
| `processing` `.finished` | `reason` | Genie has completed processing. The `reason` field indicates why the run ended. Refer to [Processing finished reasons](#processing-finished-reasons). |
| `agent` `.message` | `message` | The genie's response message. |
| `skill` `.running` | `skill_name`, `skill_id`, `call_id`, `skill_parameters`, `skill_` `parameter_schema`, `requires_user_` `confirmation` | A skill has started executing. When the genie runs skills in parallel, each skill emits its own `skill.running` event. Match events to skills by `call_id`. |
| `skill` `.completed` | `skill_name`, `skill_id`, `call_id`, `skill_result`, `skill_result_schema`, `requires_user_` `confirmation`, `job_id` | A skill completed successfully. Match to the corresponding `skill.running` event by `call_id`. `job_id` is absent for MCP skills. |
| `skill` `.failed` | `skill_name`, `skill_id`, `error`, `job_id` | A skill execution failed. |
| `skill` `.stopped` | `skill_name`, `skill_id` | Terminal variant emitted by some runtime versions in place of `skill.completed`. Treat it as a successful completion. |
| `skill` `.confirmation` `_required` | `call_id`, `skill_name`, `skill_id`, `skill_parameters`, `skill_` `parameter_schema` | A skill requires user confirmation before executing. Use `call_id` with [Approve or reject a skill](#approve-or-reject-a-skill). |
| `runtime_connection` `.auth_required` | `runtime_connection` `_attempt_id`, `auth_link` | A skill requires the user to authenticate a connection. Use `runtime_connection` `_attempt_id` with [Get a runtime connection link](#get-a-runtime-connection-link). |
| `runtime_connection` `.auth_success` | `runtime_connection` `_attempt_id` | The user completed authentication and the connection is established. The skill resumes. |
| `runtime_connection` `.auth_failed` | `runtime_connection` `_attempt_id`, `reason` | The runtime connection authorization didn't complete. `reason` explains why, for example `rejected_by_user`. |
| `system.ping` |  | Keep-alive heartbeat, sent roughly every 30 seconds during long-running or paused turns. Ignore it. |
| `system` `.stream_interrupted` | `genie_run_id`, `last_seq_num`, `reason`, `retry_after_ms` | The server closed the stream before the turn finished (for example, during a long pause). Recover from persisted state rather than assuming the turn failed; see [Rebuild a conversation timeline](/en/agentic/agent-studio/chat-interface/headless-api-troubleshooting#rebuild-a-conversation-timeline). |

### Processing finished reasons

The `processing.finished` event includes a `reason` field:

| Reason | Description | Client action |
| --- | --- | --- |
| `internal_error` | The genie run ended because of an internal error. | Show an error state. You can send the message again. |
| `business_approval_pending` | The genie is waiting on a business approval. The stream closes. A new genie run starts after the approval is decided. | Don't reconnect to the stream. Listen for the new run's events after the approval is resolved. |

### Runtime connection flow

The stream runs the following sequence when a skill requires a connection the user hasn't authorized:

- The genie emits `runtime_connection.auth_required` with a `runtime_connection_attempt_id`.
- Calls [Get a runtime connection link](#get-a-runtime-connection-link) and shows `auth_link.url` to the user. No user action is needed if the `status` is `authorized`.
- Authentication flow either:
  - The user authenticates, and the genie emits `runtime_connection.auth_success`. The skill resumes.
  - The user declines, and [Reject a runtime connection](#reject-a-runtime-connection) is called. The genie emits `runtime_connection.auth_failed` with `reason` set to `rejected_by_user`.

## Limitations

Headless API endpoints have the following limitations:

- [Action Board](/en/agentic/agent-studio/action-board) isn't supported
- [App Events](/en/agentic/agent-studio/app-events) aren't supported
- A genie supports a single attached client. The client-to-genie relationship is **1:1**: attaching a second client returns a `409` conflict. [Detach](/en/workato-api/agent-studio#detach-a-client-from-a-genie) the existing client first to re-point it.

## Quotas

| Description | Quota | Notes |
| --- | --- | --- |
| Rate quota for unauthenticated Headless API requests | 200 requests per second globally | 50 requests per second per genie and 50 requests per second per source IP also apply. |
| Rate quota for authenticated Headless API requests | 50 requests per second globally | 20 requests per second per workspace apply to all endpoints except **Send a message**. 5 requests per second per workspace apply to the **Send a message** endpoint. |
| Concurrent server-sent event (SSE) streams for authenticated Headless API requests | 1,000 concurrent streams globally | 100 concurrent SSE streams per workspace also apply. |
