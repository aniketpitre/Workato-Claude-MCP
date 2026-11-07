---
url: 'https://docs.workato.com/en/connectors/slack/actions.md'
description: >-
  Learn how Slack actions in Workato use the Slack Web API, the permission
  scopes they require, and actions such as Post message and Respond to button
  click.
---

# Slack - Actions

## Requirements

All Slack actions use the [Slack Web API](https://api.slack.com/web) to perform recipe actions.

You must create a Slack app before you can use Slack actions. Refer to our [Slack triggers documentation](/en/connectors/slack/triggers#requirements) to learn how to create a Slack app.

## Permission scopes

The connected Slack app performs Slack actions on behalf of the user. To perform each action, the app must have the associated permission scope. For example, the **Create conversation** action uses the [`conversations.create`](https://api.slack.com/methods/conversations.create) method, which requires the connected Slack app to have the `channels:write` scope.

The following table describes the minimum permissions required for optimal use.

| Token type | Scope | Reason |
| --- | --- | --- |
| Bot | None | No bot scopes required. |
| User | `channels:read` | Retrieves a list of public conversations. |
| `channels:write` | Create/update public conversations. |
| `groups:read` | Retrieves a list of private conversations. |
| `groups:write` | Create/update private conversations. |
| `im:read` | Retrieves a list of direct message conversations. |
| `im:write` | Create/update direct message conversations. |
| `mpim:write` | Create/update multi-party group conversations. |
| `mpim:read` | Retrieves a list of multi-party group conversations. |
| `chat:write` | Post messages as a user. |
| `users:read` | Get user information. |
| `users:read.email` | Get user information by email. |

### Add or remove permission scopes

To add or remove permission scopes for your app:

1. Go to your Slack app's page. The URL for this page uses the following format:
   
   ```html
   https://api.slack.com/apps/{app_id}
   ```
   
   The `app_id` is unique to your app.
   
2. Go to **OAuth & Permissions > Scopes** to select your app's permission scopes.
   
   ![Add permission scopes](/assets/add-permission-scopes.CsSDYlvY.gif)_Add permission scopes_
   
3. Click **Save changes** to save your permission scopes.
   

### Event subscriptions and permission scopes

When you subscribe to events, Slack automatically adds the scopes that your app does not already have. This can result in your app having unintended permissions from the additional scopes. After you subscribe to events, we recommend going to **OAuth & Permissions > Scopes** to confirm your app's permission scopes.

## Post message action

The post message action posts a message to your specified channel or user. By default, messages are posted as the authenticated user.

![Workato post message](/assets/workato-post-message.DRKYdqFv.png)_Message posted as the authenticated user_

Refer to our [Custom OAuth profiles documentation](/en/connectors/slack/custom-oauth) for more information.

### How it works

The messages you post can range from simple to complex. For example, you can configure this connector to post a message that contains one line of text, or configure it to include a combination of text, buttons, menus, icons and images.

### Input

#### Channel

You can post messages to channels (public and private), or to a specific user.

If you're using channel names to post messages to a channel, prefix them with `#`, for example, `#support-ticket-101`. Otherwise, use the channel IDs and channel datapills as-is, for example, `CANUXC4MU` or Channel respectively.

![Channel datapill](/assets/channel-datapill.CTNzmB-2.png)_Channel datapill_

Similarly, if you're using user names to post a direct message (DM) to a user, prefix them with `@`, for example, `@johndoe`. Otherwise, use user IDs and user datapills without modifying them. For example, `UA12345` or User ID respectively.

![User datapill](/assets/user-datapill.Blo_lvGC.png)_User datapill_

#### Basic text

This is the most basic text field for a post message.

![Basic text](data:image/png;base64,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)_Basic text in Slack_

If [Allow Slack formatting](#allow-slack-formatting) is enabled, you can tag users in the message by enclosing their user ID or user name with `<@` `>`, for example, `<@UA12345>` or `<@johndoe>` for user ID and user name respectively.

#### Attachment title

This input adds an attachment title to the post message.

![Attachment title](data:image/png;base64,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)_Attachment title text in Slack_

#### Attachment title link

When you provide a valid URL, this field is hyperlinked to the [attachment title](#attachment-title), redirecting users there if clicked.

![Attachment title link](data:image/png;base64,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)_Attachment title link in Slack_

> **USE CASE EXAMPLE**
> 
> To learn how to create a recipe that shares image attachments in Slack using a downloadable link, refer to the [Share image attachments from email in Slack using a public link](/en/getting-started/use-cases/gmail-filestorage-slack) use case.

#### Attachment text

This field adds attachment text to the post message, below the attachment title.

![Attachment text](/assets/attachment-text.BSFQnPTq.png)_Attachment text in Slack_

#### Attachment message fields

This field creates a two-column layout below the message text. Enter one name-value pair per line, for example, `Name: John`.

![Attachment message fields](/assets/attachment-message-fields.Vik1-Doe.png)_Attachment message fields in Slack_

#### Buttons

This field adds a button to the post message. When this button is clicked, it triggers a button click event. Another recipe is required to handle this event. Refer to our Slack triggers documentation to learn more about [button click triggers](/en/connectors/slack/triggers#button-click-real-time).

##### Button action handler recipes

This field lists any Slack recipes with a button click trigger. Choosing a recipe ensures that button clicks from this button trigger it.

##### Button actions

This field specifies certain characteristics of the button. Enter one button action on each line in this format:

```
action name, action ID, style, confirmation title, confirmation text, ok button title, dismiss button title
```

Only the first two parameters must be filled in for non-danger-styled actions, as no popup prompt is generated. For example:

```
Notify BizDev, bd, , , , ,
```

For danger-styled actions, all seven parameters must be filled in. For example:

```
Notify Sales, sales, danger, Confirm, Are you sure?, Yes, Cancel
```

The following table provides a detailed description of each button parameter.

| Button definition input fields | Description |
| --- | --- |
| Action name | The button label visible to the Slack user interacting with the buttons. |
| Action ID | The internal value of the button. This must be unique. This value is not visible on Slack to anyone. |
| Style | Leave this field as well as the remaining four fields blank for non-danger styled actions since no pop-up is generated. Otherwise, put **danger** to generate a red button with a pop-up prompt, requiring the user to confirm the button click. When configuring a **danger** button, you must provide input for the remaining four fields. |
| Confirmation title | This value displays in the pop-up prompt as the header. |
| Confirmation text | This value displays in the pop-up prompt as the body text. |
| Ok button title | The Button label in the pop-up prompt to confirm the button click. |
| Dismiss button title | The button label in the pop-up prompt to cancel the button click. |

![Buttons](/assets/buttons.DkL_LBZa.png)_Buttons in Slack_

#### Attachment color

This field allows you to choose the color of the vertical line to the left of the message.

![Attachment color](/assets/attachment-color.BDYCCv2z.png)_Attachment color in Slack_

#### Thumb URL

When a valid image URL is provided, this field displays a thumb image to the right of the message.

#### Image URL

When a valid image URL is provided, this field will display the image at the bottom of the message. Image will be resized to max width of 400px or a max height of 500px.

![Image URL](/assets/attachment-image.BCpOAgXe.png)_Image URL in Slack_

#### Allow Slack formatting

When enabled, this field allows you to tag users in the message by enclosing their user ID or user name with `<` `>`, for example, `<UA12345>` or `<@johndoe>` for user ID and user name respectively.

![Tag users](/assets/tagging-users.BfLjAdtj.png)_Tag users by allowing Slack formatting_

#### Thread ID

[Slack threads](https://api.slack.com/docs/message-threading) allow you to group related messages together, making it easier to follow conversations in Slack channels or groups.

To post a message in an existing thread, enter the Thread ID datapill in this field. Alternatively, you can pass the Message ID of the parent message.

##### Passing a parent message ID to continue a thread

Refer to this [Button action example recipe](https://www.workato.com/recipes/602058) to learn how to configure actions using the thread ID.

If a thread does not exist yet, but you plan to post a message threaded under a parent message, supply the `Message ID` of the parent message.

### Post message as (deprecated)

This field allows you to change the name of the user who posts the message. By default, messages are posted as the authenticated user. This field only works for Classic Slack apps. [Classic Slack apps](https://api.slack.com/authentication/quickstart) are apps that were created before June 10, 2020, utilizing the old umbrella `bot` scope.

![Post message as](/assets/post-message-as.DnmEacf6.png)_How it will look like in Slack_

### Icon image URL (deprecated)

This field allows you to change the icon of the user by who posts the message. By default, messages are posted as the authenticated user. This field only works for Classic Slack apps. [Classic Slack apps](https://api.slack.com/authentication/quickstart) are apps created before June 10, 2020, utilizing the old umbrella `bot` scope.

![Post message as icon](/assets/post-message-as-icon.COUbFrlU.png)_How it will look like in Slack_

### Respond to button click actions

The **Respond to button click** action works together with the [button click (real-time) trigger](/en/connectors/slack/triggers#button-click-real-time) to post messages in response to the button click.

### How it works

By passing the Response URL pill from the output of a [button click (real-time) trigger](/en/connectors/slack/triggers#button-click-real-time), the recipe will know which button has been clicked at run-time.

Similar to the post message action, this action can post messages that are just a simple line of text or include a combination of text, buttons, menus, icons, and images—depending on your use case.

### Input

The following are the additional input fields that the Slack action **Respond to button** has on top of the usual input fields in the **Post message** action.

| Input field | Description |
| --- | --- |
| Button response URL | You can obtain this value from the output datatree of the Slack trigger **New button action**. This tells the action what button click to respond to. |
| Response type | **In channel:** Posts the message like a normal chat message. **Ephemeral:** Posts the message so that it is visible only to the user who clicked the button. |
| Replace original | If **yes**, the new message overwrites the original message with buttons and is posted in the same position in the channel. If **no**, the original message with buttons remains in the same position in the channel. The new message is added to the end of the channel conversation. |
| Delete original | If **yes**, the original message with buttons is removed from the channel. The new message is added to the end of the channel conversation. If **no**, the original message with buttons remains in the same position in the channel. The new message is added to the end of the channel conversation. |

## Invite user to conversation action

The **Invite user to conversation** action invites a user to a conversation.

![Invite user to conversation](/assets/invite-user-to-conversation.WoU0znai.png)

### Input

#### User

You can use either the user ID/name or user ID datapill. Prefix user names with ‘@’, for example, **@johndoe**. However, use user IDs and user ID datapills as-is, for example, **UA12345** or ID, without prefixing them with '@'.

To select available users, switch to **Select user**. ![select-user](/assets/select-user-channel-invite.Dc_dshqY.png)

#### Conversation

Select the conversation to invite the user to. Alternatively, you can use a conversation ID or dynamically set one with a Channel datapill.

To select available conversations, switch to **Select conversation**. ![select-channel](/assets/select-channel-channel-invite.FKcBEi4E.png)

## Archive conversation action

The **Archive conversation** action allows you to archive public, private channels, and multi-party groups to which your app has been added. Note that the **#general** channel of a Slack workspace cannot be archived.

![Archive conversation](/assets/archive-conversation.GZepJh01.png)

### Input

#### Conversation

Select the conversation to archive. Alternatively, you can use a conversation ID or dynamically set one with a Channel datapill.

To select available conversations, switch to **Select conversation**. ![select-channel](/assets/select-channel-archive-channel.7F1hkvqq.png)_Switching to Select channel_

## Unarchive conversation action

The **Unarchive conversation** action allows you to unarchive public and private channels.

![Unarchive conversation](/assets/unarchive-conversation.CZxaD0M2.png)

### Input

#### Conversation

Select the conversation to unarchive. Alternatively, you can use a conversation ID or dynamically set one with a Channel datapill.

To select available conversations, switch to **Select conversation**. ![select-channel](/assets/select-channel-unarchive-channel.C84M05UN.png)_Switching to 'Select conversation'_

## Create conversation action

The **Create conversation** action creates a channel with a specified channel name. You can also create private channels. Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 80 characters or less.

![Create conversation](/assets/create-conversation.DKrKpBLz.png)_Create conversation action_

### Input

#### Private channel?

Set to **Yes** to create a private channel. Defaults to **No**.

#### Return channel details if already exists?

By default, if the channel already exists, this action returns an error. Set this input to **Yes** to prevent an error and direct Workato to return the existing channel's details instead. In workspaces with a large number of conversations, Workato only retrieves and searches through the first 1000 records. This is due to limitations imposed by the Slack API which doesn't facilitate filtering conversations by channel name. If no matching entry is found within the first 1000 records, Workato returns an error.

## Set conversation purpose action

The **Set conversation purpose** action allows you to set the purpose of a conversation.

![Set conversation purpose](/assets/set-conversation-purpose.2dw42j6A.png)_Set conversation purpose action_

### Input

#### Conversation

Select the conversation for which you plan to set the purpose. Alternatively, you can use a conversation ID or dynamically set the conversation purpose using a Channel datapill.

To select available conversations, switch to **Select conversation**.

![select-channel](/assets/select-channel-channel-purpose.4eeUW9_R.png)_Switching to Select conversation_

#### Conversation purpose

Set the conversation's purpose. Slack formatting works in this field, including tagging users.

For example:

##### Input

```
"Hi <@johndoe>, how are _you_ *doing*?"
```

##### Output

Hi @johndoe, how are _you_ **doing**?

Refer to Slack's [documentation](https://api.slack.com/docs/message-formatting) to learn more about formatting messages in Slack.

## Set conversation topic action

The **Set conversation topic** action allows you to set the topic of a conversation.

![Set conversation topic](/assets/set-conversation-topic.DjVgWKI4.png)_Set conversation topic action_

Slack formatting works in this field, including tagging users. For example:

##### Input

```
"Hi <@johndoe>, how are _you_ *doing*?"
```

##### Output

Hi @johndoe, how are _you_ **doing**?

Refer to Slack's [documentation](https://api.slack.com/docs/message-formatting) to learn more about formatting messages in Slack.

### Input

#### Conversation

Select the conversation for which you plan to set the topic. Alternatively, you can use a conversation ID or dynamically set one using a Channel datapill.

To select available conversations, switch to **Select conversations**. ![select-channel](/assets/select-channel-channel-topic.cd9vPOW4.png)_Switching to Select conversations_

#### Conversations topic

Set the conversation's purpose. The topic must be 250 characters or less. Slack formatting works in this field, including tagging users.

For example:

##### Input

```
"Hi <@johndoe>, how are _you_ *doing*?"
```

##### Output

Hi @johndoe, how are _you_ **doing**?

Refer to Slack's [documentation](https://api.slack.com/docs/message-formatting) to learn more about formatting messages in Slack.

---
