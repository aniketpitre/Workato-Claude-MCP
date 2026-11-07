---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/chat-interface/headless-api-troubleshooting.md
description: >-
  Find solutions for common Headless API authentication, authorization, and
  streaming errors.
---

# Headless API troubleshooting

Use this page to resolve common [Headless API](/en/agentic/agent-studio/chat-interface/headless-api) failures.

## 401 auth\_failed

**Error**: A runtime call returns `401` with:

```json
{ "error_code": "auth_failed", "error_message": "Authentication failed.", "request_id": "<uuid>" }
```

**Cause and solution**: The gateway rejected the credential before reaching the genie. Check the following items in order:

- **Wrong token type**: Runtime calls use a genie client API key or an OAuth access token rather than the `wrkaus-…` Developer API token, which is only for provisioning.
- **Wrong data center**: Credentials are data-center-scoped. Call the `genie-api` host for the same data center your workspace runs in.
- **Expired or rotated key**: Regenerating an API key invalidates the previous API key. [Regenerate](/en/workato-api/agent-studio#regenerate-a-genie-client-key) and update your backend to use the updated API key.
- **Malformed header**: Send `Authorization: Bearer <token>` exactly.

## 401 user\_nonactive\_or\_missing

**Error**: An API-key call returns `401` with `error_code: "user_nonactive_or_missing"`.

**Cause**: The `X-IDP-User-Id` doesn't resolve to an active, allow-listed user. The runtime returns the same code whether the user doesn't exist, isn't in a user group allow-listed on the genie, or isn't active yet. A user is inactive when they've been invited but haven't accepted the invitation and finished setting up their Workato Identity.

**Solution**: Confirm the user is active. An invited user must accept their email invitation and finish setting up their Workato Identity before you can assert them, so ask the user to check their email if they haven't completed setup. Then make sure the user belongs to a user group allow-listed on the genie, creating the user first if needed. Look the user up with `GET /api/iam/users?query=<email>` server-side before the runtime call. The response includes a `status` field (`active` or `invited`), which also lets you show a different message for an unknown user versus a non-allow-listed one.

## Client creation or attachment fails

**Error**: Most Developer API calls succeed, but creating, regenerating, or attaching a genie client fails with a permission error.

**Cause**: The Developer API client's role is missing the **Custom chat interface** privilege under **Genie building**, which governs client management. This is the most commonly missed privilege for Headless setup.

**Solution**: Grant the role **Custom chat interface** access with privileges to at least **Create**. You don't need to rotate the token after adding a privilege.

**Related**: Attaching a client returns `409` when the genie already has a client. The relationship is [1:1](/en/workato-api/agent-studio#genie-clients). Detach the existing client first.

## Empty stream or repeated blank events

**Error**: The SSE stream stays open but appears idle, or the genie doesn't reply.

**Cause and solution**:

- **Keep-alive events**: During long-running or paused turns, the runtime emits periodic keep-alive events. For example: `system.ping` roughly every 30 seconds. Ignore event types your handler doesn't recognize.
- **Genie not started**: The genie must be active. Start it with `POST /api/agentic/genies/:id/start`.
- **Waiting on you (skill confirmation)**: A `skill.confirmation_required` event pauses the turn until you post your decision with [Approve or reject a skill](/en/agentic/agent-studio/chat-interface/headless-api#approve-or-reject-a-skill). The same stream resumes after you post the resolution. You don't need to reconnect. Each skill that needs confirmation emits its own `skill.confirmation_required` event with a unique `call_id` when the genie runs multiple skills in parallel. Post a resolution for every pending `call_id`.
- **Waiting on the user (runtime connection)**: A `runtime_connection.auth_required` event pauses the turn while the user authenticates an upstream connection out-of-band. There's nothing for your client to post, and the **original stream doesn't resume**. It emits a keep alive, then a `system.stream_interrupted`. Detect completion by polling [Get a runtime connection link](/en/agentic/agent-studio/chat-interface/headless-api#get-a-runtime-connection-link) until `status` is `authorized`, then read the resumed reply from [message history](/en/agentic/agent-studio/chat-interface/headless-api#get-messages).

## Turn hangs when multiple skills need confirmation

**Problem**: A turn stays paused after the genie runs several skills in parallel and more than one skill requires confirmation.

**Cause**: Earlier runtime versions could leave the turn paused in this scenario. This issue is fixed.

**Solution**: Make sure you posted a resolution for every `call_id` from each `skill.confirmation_required` event. Contact support and include the `request_id` if the turn still hangs after you resolve every `call_id`.

## Duplicate events or event IDs

**Problem**: You receive the same event, with the same `event_id`, more than once.

**Cause**: [Reconnecting to a stream](#reconnect-to-a-dropped-stream) and [Get events](/en/agentic/agent-studio/chat-interface/headless-api#get-events) replay events from the point you specify. The replayed events can overlap with events your client already processed, especially if you merge the live stream with recovered events.

**Solution**: Use `event_id` as the unique key and discard events you've already processed. Use `seq_num` to order events within a genie run. Don't repeat side effects for a duplicate, such as showing a second confirmation prompt or posting a second approval for the same `call_id`.

## Reconnect to a dropped stream

**Problem**: The SSE stream closes before you receive `processing.finished`.

**Solution**: Reconnect to the [genie run](/en/agentic/agent-studio/chat-interface/headless-api#reconnect-to-a-stream) and resume from the last event you received. Use one of the following:

- **`Last-Event-ID` header**: Pass the `event_id` of the last event you received.
- **`since_seq_num` query parameter**: Pass the `seq_num` of the last event you received.

```http
GET /api/v1/genies/:genie_handle/chat/conversations/:conversation_id/genie-runs/:genie_run_id?since_seq_num=<last_seq_num>
```

If you receive a `system.stream_interrupted` event, use `last_seq_num` and wait `retry_after_ms` before reconnecting. Don't reconnect after a `processing.finished` event with the reason `business_approval_pending`. Refer to [Processing finished reasons](/en/agentic/agent-studio/chat-interface/headless-api#processing-finished-reasons). Deduplicate replayed events by `event_id`. Refer to [Duplicate events or event IDs](#duplicate-events-or-event-ids) for more information.

## Event recovery returns nothing

**Error**: [Get events](/en/agentic/agent-studio/chat-interface/headless-api#get-events) returns no events after a disconnection.

**Cause**: This error happens when you use the wrong parameter or window. The parameter is `since_created_at` (an RFC3339 timestamp); pass `next_since_created_at` from the previous response to page. Events are retained for 24 hours.

## File upload is rejected

**Error**: A call to the [upload endpoint](/en/agentic/agent-studio/chat-interface/headless-api#upload-a-file) fails, or the genie doesn't receive the attachment.

**Cause and solution**:

- **File too large**: Each upload accepts a single file, with a maximum size of 20 MB. Reduce or split the file.
- **Wrong request format**: Send the file as `multipart/form-data` with a single `file` field. Don't set `Content-Type` manually. Your HTTP client sets the multipart boundary.
- **Attachment not referenced**: Uploading a file doesn't attach it on its own. Pass the returned `file_id` in the `file_id` parameter of [Send a message](/en/agentic/agent-studio/chat-interface/headless-api#send-a-message).

## Conversation topic returns a number instead of text

**Problem**: `GET /conversations/:conversation_id` returns a numeric `topic` such as `5951` instead of a readable title.

**Cause**: The genie auto-generates the conversation `topic` from the user's first message, which takes a few moments. If you call `GET /conversations/:conversation_id` before generation completes, `topic` is still a numeric placeholder. The [list conversations](/en/agentic/agent-studio/chat-interface/headless-api#list-conversations) endpoint returns the generated `topic` once it's ready.

**Solution**: Use the list conversations endpoint for display, or fall back to the conversation's first user message when `topic` is a numeric value.

## Rebuild a conversation timeline after a reload or dropped stream

**Problem**: After a page reload or a dropped SSE stream, you need the full turn, including `skill.*` and `processing.*` events, but you only have what arrived on the live stream.

**Cause**: Every conversation event is persisted, not only the live stream. All event types, including `skill.*` and `processing.*`, are retrievable from [Get events](/en/agentic/agent-studio/chat-interface/headless-api#get-events) for 24 hours after they occur.

**Solution**: Fetch the persisted events with `GET /conversations/events?conversation_id=<conversation_id>&since_created_at=<RFC3339>` and replay them in order to reconstruct the full timeline. Don't treat `skill.*` and `processing.*` events as available only during the live stream.

One exception: a turn **resumed after a `runtime_connection.auth_required` pause** isn't captured in [Get events](/en/agentic/agent-studio/chat-interface/headless-api#get-events) — persisted events stop at the pause. Recover that reply from [message history](/en/agentic/agent-studio/chat-interface/headless-api#get-messages) and merge it in, de-duplicating by `message_id`.

## Get help

Every runtime response includes a `request_id` and an `x-request-id` header. Include these values when you contact Workato support so the request can be traced through the gateway.
