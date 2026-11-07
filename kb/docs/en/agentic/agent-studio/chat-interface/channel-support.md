---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/chat-interface/channel-support.md
description: >-
  Enable channel support to allow genies to participate in Slack and Microsoft
  Teams channels.
---

# Channel support

Genies support participation in Slack and Microsoft Teams channels. You can use channel support for IT help desks, HR support, and project assistance channels. Workato GO doesn't provide channel support.

## Channel support options

Configure channel behavior in the genie builder when you set up a chat interface. Refer to [Enable channel responses](/en/agentic/agent-studio/chat-interface/chat-interface#enable-channel-responses) for more information.

| Field | Options | Default |
| --- | --- | --- |
| **Genie can chat in** | Specific channels only, Any channel the genie is invited to | Specific channels only |
| **Channels** | Multi-select from available channels | None selected |
| **In channels, genie responds to** | @mentions only, Every message posted | @mentions only |

The **Channels** drop-down menu only displays public channels and private channels the genie has been added to. You must explicitly select each channel where the genie is allowed to respond. The genie displays an error message rather than ignoring messages silently if the channel hasn't been explicitly added to the genie chat interface.

> **DATA EXPOSURE IN CHANNELS**
> 
> Information the genie retrieves from knowledge bases, skills, or external systems may be visible to all channel members when you deploy a genie to a channel. Ensure your genie's knowledge sources and skills are appropriate for the audience in the channels you select.

### Channel modes

You can select **Every message posted** or **@mentions only** channel mode to control when the genie responds before deploying a genie to a channel.

| Mode | Initial trigger (channel) | Within thread |
| --- | --- | --- |
| **Every message posted** | Every new message | Every message |
| **@mentions only** | @mention only | @mention only |

**Every message posted** is intended for support channels where users expect the genie to respond to every message. The genie responds to every new message in the channel and creates a thread. The genie responds to every subsequent message from any user within that thread.

**@mentions only** is intended for channels where the genie should participate only when explicitly invoked through an @mention. The genie responds only when someone @mentions it, either in the channel or in a thread. It ignores all other messages.

### Thread history

Genies receive the full thread history as context when triggered in a channel. Each message includes the sender's name and email address so the genie can identify who sent each message. Previous genie responses are also included in the thread history.

Older messages are summarized automatically and recent messages are included verbatim in threads where the full history exceeds the model's context window.

The genie uses only the messages added since the previous @mention as context for each new response when **@mentions only** is selected. This behavior applies when the genie is mentioned multiple times in the same thread.

### Concurrent requests

If the genie is already processing a request in a thread and another message triggers it before the first request completes, the genie responds to the subsequent trigger with: `I'm still working on something. Please give me a moment.` Users can send another message after the first request completes. All previously queued messages are included in the new context.

## Authentication in channels

Users who haven't authenticated are prompted to log in when they trigger the genie if your genie requires [Workato Identity](/en/workato-identity) authentication.

- **Slack**: The genie sends a login prompt in the thread. Only the triggering user sees the prompt. The user can continue their interaction after authenticating.

### User confirmation in channels

The genie sends a confirmation button to the thread when an action requires confirmation. Clicking the button opens a modal with the confirmation details. The modal validates the identity of the user. Users who aren't requested to confirm an action receive an error message if they click the button.

Confirmation modals support standard input types, including text, boolean, and datetime. Users can update fields before confirming.

### Required scopes

Your chat interface app must have the correct scopes enabled to respond in channels.

#### Slack

Slack requires the following scopes when you create a new genie:

##### Bot scopes

Slack requires the following bot scopes:

- `app_mentions:read`
- `assistant:write`
- `channels:history`
- `channels:read`
- `chat:write`
- `files:read`
- `files:write`
- `groups:history`
- `groups:read`
- `im:history`
- `im:write`
- `users:read`
- `users:read.email`

##### User scopes

Slack requires the following user scopes:

- `users:read`
- `users:read.email`

##### Event subscription scopes

Slack requires the following event subscription scopes if you plan to use **Every message posted**:

- `app_mention`
- `message.im`
- `assistant_thread_started`
- `message.channels`

#### Microsoft Teams

Microsoft Teams requires the following scopes:

- `AppCatalog.Read.All`: For GET `/appCatalogs/teamsApps`. This resolves the Teams catalog app ID from the manifest externalId during connection setup. Required to reach Connected status.
  
- `User.Read.All`: For directory/user read. This maps the message author and the invoking user to the identities or display names shown in conversations. This is the baseline read scope.
  
- `Team.ReadBasic.All`: For GET `/teams`. This lists the teams the bot belongs to enable channel drop-down menus and labeling.
  
- `Channel.ReadBasic.All`: For GET `/teams/{team}/channels` and GET `/teams/{team}/channels/{channel}`. This lists channels and resolves a channel's display name.
  
- `ChannelMessage.Read.All`: For GET `/teams/{team}/channels/{channel}/messages/{id} (+ /replies)`. This reads the channel thread, including the root message and replies, to give the genie conversation context when it's `@mentioned` in a channel.
  
- `Files.Read.All`: For GET `/shares/{url}/driveItem`. This resolves an attachment share URL to a `driveItem` or download URL and size to allow the genie to read files shared in the conversation. Attachments can't be processed without this scope.
