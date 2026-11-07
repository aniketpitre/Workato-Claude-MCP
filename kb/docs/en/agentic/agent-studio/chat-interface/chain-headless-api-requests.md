---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/chat-interface/chain-headless-api-requests.md
description: >-
  Walk through building a complete genie conversation with the custom interface
  API.
---

# Custom interface API walkthrough

Headless API endpoints are designed to be called in sequence. Each request in a conversation lifecycle depends on identifiers returned by a previous request. This guide demonstrates how to chain requests together to manage a complete conversation, handle interruptions, and respond to skill confirmation and runtime connection events.

## Conversation lifecycle overview

A complete genie conversation follows this sequence:

- Create a conversation to obtain a `conversation_id`.
- Send a message using the `conversation_id` and stream the genie's response.
- Handle Server-Sent Events (SSE) emitted during the stream, including skill confirmations and runtime connection requests.
- Retrieve messages or events if the stream disconnects before it closes.

Every subsequent request in a session depends on the `conversation_id` returned in the initial request. You must retain this value for the duration of the session.

## Complete request chain

The following table summarizes the full sequence of API calls for a conversation session, including the identifier each request produces and where it's used next:

| Step | Request | Produces | Used by |
| --- | --- | --- | --- |
| [Create a conversation](#create-a-conversation) | `POST` `/conversations` | `conversation` `_id` | All subsequent requests |
| [Send a message and stream the response](#send-a-message-and-stream-the-response) | `POST /messages` | `genie_run_id` | Reconnect endpoint |
| [Attach a file (optional)](#attach-a-file-to-a-message) | `POST /upload` | `file_id` | `POST /messages` |
| SSE: [Skill confirmation required](#skill-confirmation-required) | `POST` `/skill_approval` `/:call_id` | Resolution | Genie resumes |
| SSE: [Runtime connection authentication required](#runtime-connection-authentication-required) | `POST` `/runtime_connection` `/:runtime_connection` `_attempt_id/link` | Auth `url` | Presented to user |
| [Reconnect to the stream](#reconnect-to-the-stream) | `GET` `/genie-runs/` `:genie_run_id` | Resumed SSE stream | — |
| [Fetch missed events manually](#fetch-missed-events-manually) | `GET` /`conversations` `/events` | Missed events | — |
| [Retrieve conversation history](#retrieve-conversation-history) | `GET /messages` | Message history | Display or audit |

## How to chain Headless API requests

Complete the following steps to chain Headless API requests:

1. Create a conversation
   
   ### Create a conversation
   
   You must create a conversation before you can send a message. This request returns the `conversation_id` you pass to every subsequent request in the session.
   
   Run the following request to create a conversation and obtain a `conversation_id`:
   
   ```bash
   POST /api/v1/genies/:genie_handle/chat/conversations
   ```
   
2. Send a message and stream the response
   
   ### Send a message and stream the response
   
   Send a message using the `conversation_id` and stream the response. Set stream to `true` to receive a real-time SSE stream as the genie processes the request. The `genie_run_id` returned in the response is required if you need to reconnect after a disconnection.
   
   ```bash
   POST /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/messages
   ```
   
   #### Attach a file to a message
   
   Upload the file before sending the message if you plan to include an attachment. Pass the `file_id` returned by the upload in the `file_id` parameter of the send message request.
   
   ```bash
   POST /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/upload
   ```
   
3. Handle SSE events
   
   ### Handle SSE events
   
   Your application must listen for and respond to events while the stream is open. Some events require immediate action before the genie can continue. Other events are informational.
   
   #### Skill confirmation required
   
   When the genie emits a `skill.confirmation_required` event, it pauses execution and waits for your application to approve or reject the skill call. The event payload includes a `call_id`. Use the `call_id` to approve or reject the skill:
   
   ```bash
   POST /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/skill_approval/:call_id
   ```
   
   #### Runtime connection authentication required
   
   When the genie emits a `runtime_connection.auth_required` event, it requires the user to authenticate a connection before the skill can execute. The event payload includes a `runtime_connection_attempt_id` and an `auth_link`.
   
   Use the `runtime_connection_attempt_id` to request an authentication link to present to the user:
   
   ```bash
   POST /api/v1/genies/:genie_handle/chat/runtime_connection/:runtime_connection_attempt_id/link
   ```
   
   The response returns a `status` field. When `status` is `auth_required`, present the `auth_link.url` to the user to complete authentication. Poll this endpoint until `status` is `authorized`, which indicates the connection is complete and the genie has resumed processing; then read the resumed reply from [message history](/en/agentic/agent-studio/chat-interface/headless-api#get-messages).
   
   Use the following command to cancel the connection request:
   
   ```bash
   POST /api/v1/genies/:genie_handle/chat/runtime_connection/:runtime_connection_attempt_id/reject
   ```
   
4. Recover from a disconnection
   
   ### Recover from a disconnection
   
   Use one of the following recovery methods if the SSE stream disconnects before the genie emits `processing.finished`:
   
   #### Reconnect to the stream
   
   Reopen the SSE stream for the genie run using the `genie_run_id`. Pass the ID of the last successfully received event in the `Last-Event-ID` header to replay only the events you missed:
   
   ```bash
   GET /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/genie-runs/:genie_run_id
   ```
   
   #### Fetch missed events manually
   
   Use the get events endpoint as a fallback if you can't reconnect to the stream. Events are available for 24 hours. Pass the `since_created_at` parameter to retrieve only events that occurred after your last successfully received event.
   
   ```bash
   GET /api/v1/genies/:genie_handle/chat/conversations/events?conversation_id=:conversation_id&since_created_at=:since_created_at
   ```
   
5. Retrieve conversation history
   
   ### Retrieve conversation history
   
   You can retrieve the full message history for the conversation using the `conversation_id` after a conversation closes. Use the following endpoint to display prior messages when a user returns to an existing conversation, or to fetch the genie's final response if your stream closed before the `agent.message` event was received:
   
   ```bash
   GET /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/messages
   ```
