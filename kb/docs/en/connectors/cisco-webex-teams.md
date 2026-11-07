---
url: 'https://docs.workato.com/en/connectors/cisco-webex-teams.md'
description: >-
  The Cisco Webex Teams connector lets you automate messaging workflows: post
  messages, create and manage rooms, add people, and trigger on new messages.
---

# Cisco Webex Teams

[Cisco Webex Teams](https://www.webex.com/) is a collaboration platform that provides messaging, video meetings, and file sharing capabilities.

## API version

The Cisco Webex Teams connector uses [Cisco Webex Teams API v1](https://developer.webex.com/docs/api/getting-started).

## How to connect to Cisco Webex Teams

Workato supports the following authentication methods for connecting to Cisco Webex Teams:

- [OAuth 2.0](#oauth-2-0)
- [Bot access token](#bot-access-token)

### OAuth 2.0

Complete the following steps to connect to Cisco Webex Teams using OAuth 2.0 authentication:

1. Sign in to your Workato account.
   
2. Click **Create > Connection** or press C+C.
   
3. Search for and select `Cisco Webex Teams` in the **New connection** page.
   
4. Enter a name for the connection in the **Connection name** field.
   
   ![Connect to Cisco Webex Teams](/assets/oauth.BnIRe4PW.png)_Connect to Cisco Webex Teams_
   
5. Use the **Location** drop-down menu to select the project where you plan to store this connection.
   
6. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   
9. Enter the email address associated with your Cisco Webex Teams account and click **Sign in**.
   
10. Click **Accept**. Workato requests the following permissions:
    
    - List the people in rooms that you're in
    - Read your company directory
    - List the titles of spaces that you are in
    - Post and delete messages on your behalf
    - Invite people to rooms on your behalf
    - Manage spaces on your behalf
    - Read the content of rooms that you're in

### Bot access token

You can use bot access token authentication to connect Workato to Cisco Webex Teams. This method requires two main steps:

1. [Create a bot in the Webex Developer Portal](#create-the-bot)
2. [Complete the connection setup in Workato](#complete-setup-in-workato)

#### Create a bot in the Webex Developer Portal

Complete the following steps to create a bot in the Webex Developer Portal:

1. Sign in to the [Webex Developer Portal](https://developer.webex.com/) and click **Start Building Apps**.
   
2. Click **Create a Bot** to open the [New Bot](https://developer.webex.com/my-apps/new/bot) page.
   
   ![New bot page](/assets/new-bot.dgKVoxbE.png)_New bot page_
   
3. Enter a name for your bot in the **Bot name** field. This is the bot name that appears in Webex and the Webex App Hub.
   
4. Enter a username for your bot in the **Bot username** field. Users use this username to add your bot to a space. This value cannot be changed later.
   
5. Upload a 512x512px JPEG or PNG file in the **Icon** field, or select a default option from Webex.
   
6. Provide an app description in 1024 characters or less in the **App Hub Description** field.
   
7. Click **Add Bot** to create your bot.
   
8. Click **Copy Token** to retrieve your bot access token. Store this value securely, as it is required to create your connection in Workato.
   
   ![Copy the bot access token](/assets/copy-token.mX1Zu-Cn.png)_Copy the bot access token_
   

#### Complete the connection setup in Workato

Complete the following steps to configure the Cisco Webex Teams connection in Workato:

1. Sign in to your Workato account.
   
2. Click **Create > Connection** or press C+C.
   
3. Search for and select `Cisco Webex Teams` in the **New connection** page.
   
4. Enter a name for the connection in the **Connection name** field.
   
   ![Connect to Cisco Webex Teams](/assets/bot-access-token.C1ceuNFW.png)_Connect to Cisco Webex Teams_
   
5. Use the **Location** drop-down menu to select the project where you plan to store this connection.
   
6. Use the **Authentication type** drop-down menu to select **Bot access token**.
   
7. Enter the bot access token in the **Bot access token** field. For detailed steps on how to obtain this value, see [Create a bot in the Webex Developer Portal](#create-the-bot).
   
8. Click **Connect**.
   

Refer to the Webex documentation for more information on [Bots](https://developer.webex.com/docs/bots).

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/triggers/new-message.md
description: >-
  The New message trigger in the Cisco Webex Teams connector fires in real time
  when a new message is posted in a selected room.
---

# Cisco Webex Teams - New message trigger (real-time)

This trigger monitors new messages in your Cisco Webex Teams instance in real-time. Workato processes each message as a separate job.

> **USING THIS TRIGGER WITH BOT ACCESS TOKEN AUTHENTICATION**
> 
> To ensure new messages sent to the bot are processed, tag the bot in the message. For example, `@bot_name new message`.
> 
> Additionally, due to API response times, this trigger may experience delays. To minimize delays, bot users should avoid sending messages less than three seconds apart. If a message doesn’t trigger a job, try sending another message to process the previous job.

## Input

| Field | Description |
| --- | --- |
| Room name | Select the room from which to receive messages. You can choose from a list of rooms or use a specific room ID. |
| Max | Specify the number of existing messages to retrieve starting from the latest. Defaults to 1. |

## Output

| Field | Description |
| --- | --- |
| Room type | The type of room where the message was posted. |
| Message | The content of the message. |
| Message ID | The unique identifier of the message. |
| Room ID | The unique identifier of the room. |
| Person ID | The unique identifier of the person who sent the message. |
| Person email | The email address of the person who sent the message. |
| Created | The timestamp when the message was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/triggers/new-button-submission.md
description: >-
  The New button submission trigger in the Cisco Webex Teams connector fires in
  real time when a button is submitted, processing each as a job.
---

# Cisco Webex Teams - New button submission trigger (real-time)

This trigger monitors new button submissions in your Cisco Webex Teams instance in real-time. Workato processes each submission as a separate job.

## Input

This trigger doesn't require user input.

## Output

| Field | Description |
| --- | --- |
| Attachment action ID | The unique identifier of the attachment action. |
| Message ID | The unique identifier of the message associated with the button submission. |
| Actor ID | The unique identifier of the actor who performed the button submission. |
| Room ID | The unique identifier of the room where the button was submitted. |
| Created | The timestamp when the button submission was created. |
| Org ID | The unique identifier of the organization. |
| App ID | The unique identifier of the application. |
| Advanced | An object that contains additional information about the button submission. |
| Created by (advanced) | The unique identifier of the user who created the button submission. |
| Webhook ID (advanced) | The unique identifier of the webhook associated with the button submission. |
| Name of the webhook (advanced) | The name of the webhook associated with the button submission. |
| Type of received webhook (advanced) | The type of webhook that was received. For example, `submit`. |
| Type of event (advanced) | The type of event associated with the button submission. For example, `create`. |
| Owned by (advanced) | The owner of the button submission. |
| Status (advanced) | The status of the button submission. For example, `active`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/add-person-to-room.md
description: >-
  The Add person to room action in the Cisco Webex Teams connector lets you add
  a person to a room by email, optionally as a moderator.
---

# Cisco Webex Teams - Add person to room action

This action adds a person to a specific room in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Room | Select the room you plan to add the person to, or provide the room ID. |
| Person email | Enter the email address of the person to add to the room. |
| Is moderator | Indicate whether the person should be added as a moderator. |

## Output

| Field | Description |
| --- | --- |
| ID | The unique ID of the membership. |
| Room | The room to which the person was added. |
| Person ID | The ID of the person added to the room. |
| Person organization ID | The organization ID of the person added to the room. |
| Person email | The email of the person added to the room. |
| Person display name | The display name of the person added to the room. |
| Is moderator | Indicates whether the person is a moderator in the room. |
| Is monitor | Indicates whether the person is a monitor in the room. |
| Created | The timestamp when the person was added to the room. |

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/create-room.md
description: >-
  The Create room action in the Cisco Webex Teams connector lets you create a
  new room with a specified topic and return its details.
---

# Cisco Webex Teams - Create room action

This action creates a new room in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Room topic | Specify the topic of the room you plan to create. |

## Output

| Field | Description |
| --- | --- |
| Creator ID | The ID of the person who created the room. |
| Room ID | The unique ID of the room. |
| Topic | The topic of the room. |
| Type | The type of the room. |
| Is locked | Indicates whether the room is locked. |
| Last activity | The timestamp of the last activity in the room. |
| Created | The timestamp when the room was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/get-attachment-details.md
description: >-
  The Get attachment details action in the Cisco Webex Teams connector lets you
  retrieve details of a specific attachment action by its ID.
---

# Cisco Webex Teams - Get attachment details action

This action retrieves the details of a specific attachment in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Attachment action ID | Enter the unique ID of the attachment to retrieve. You can obtain this value from the output of the [New button submission trigger](/en/connectors/cisco-webex-teams/triggers/new-button-submission). |
| Input schema | Specify the input schema. Ensure it matches the schema defined in the upstream button triggering this recipe. |

## Output

| Field | Description |
| --- | --- |
| Attachment action ID | The unique ID of the attachment action. |
| Message ID | The ID of the message associated with the attachment action. |
| Room ID | The ID of the room where the attachment action occurred. |
| Type | The type of the attachment action. |
| Person ID | The ID of the person who performed the attachment action. |
| Inputs | The inputs provided during the attachment action. |
| Created | The timestamp when the attachment action was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/get-message-details.md
description: >-
  The Get message details action in the Cisco Webex Teams connector lets you
  retrieve the details of a specific message by its ID.
---

# Cisco Webex Teams - Get message details action

This action retrieves the details of a specific message in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Message ID | Enter the unique ID of the message to retrieve. |

## Output

| Field | Description |
| --- | --- |
| Room type | The type of the room where the message was posted. |
| HTML | The HTML content of the message. |
| Message ID | The unique ID of the message. |
| Person ID | The ID of the person who sent the message. |
| Person email | The email address of the person who sent the message. |
| Room ID | The ID of the room where the message was posted. |
| Message | The text content of the message. |
| Markdown | The Markdown content of the message. |
| Attachments | An array of attachments included in the message. |
| Recipient ID | The ID of the recipient for private messages. |
| Recipient email | The email address of the recipient for private messages. |
| Created | The timestamp when the message was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/get-person-details.md
description: >-
  The Get person details action in the Cisco Webex Teams connector lets you
  retrieve details of a specific person by their unique ID.
---

# Cisco Webex Teams - Get person details action

This action retrieves the details of a specific person in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Person ID | Enter the unique ID of the person to retrieve details for. |

## Output

| Field | Description |
| --- | --- |
| Person ID | The unique ID of the person. |
| Display name | The display name of the person. |

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/get-room-details.md
description: >-
  The Get room details action in the Cisco Webex Teams connector lets you
  retrieve details of a specific room, such as its topic and creator.
---

# Cisco Webex Teams - Get room details action

This action retrieves the details of a specific room in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Room name | Select the room to retrieve details for. You can choose from a list of rooms or use a specific room ID. |

## Output

| Field | Description |
| --- | --- |
| Creator ID | The ID of the person who created the room. |
| Room ID | The unique ID of the room. |
| Topic | The topic of the room. |
| Type | The type of the room. |
| Is locked | Indicates whether the room is locked. |
| Last activity | The timestamp of the last activity in the room. |
| Created | The timestamp when the room was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/post-message.md
description: >-
  The Post message action in the Cisco Webex Teams connector lets you post a
  message to a specified room or to a specific person.
---

# Cisco Webex Teams - Post message action

This action posts a message in a specified room or to a specific person in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Room name | Select the room where you plan to post the message. You can choose from a list of rooms or use a specific room ID. |
| Alternate text | Enter alternate text for the message. Required if **Message** is left blank. |
| Message | Enter the text content of the message. Required if **Alternate text** is left blank. |

Refer to the Webex [buttons and cards](https://developer.webex.com/docs/buttons-and-cards) documentation to learn how to design a message using blocks.

## Output

| Field | Description |
| --- | --- |
| Room type | The type of the room where the message was posted. |
| HTML | The HTML content of the message. |
| Message ID | The unique ID of the message. |
| Person ID | The ID of the person who sent the message. |
| Person email | The email address of the person who sent the message. |
| Room ID | The ID of the room where the message was posted. |
| Message | The text content of the message. |
| Markdown | The Markdown content of the message. |
| Attachments | An array of attachments included in the message. |
| Recipient ID | The ID of the recipient for private messages. |
| Recipient email | The email address of the recipient for private messages. |
| Created | The timestamp when the message was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/cisco-webex-teams/actions/update-room.md
description: >-
  The Update room action in the Cisco Webex Teams connector lets you change the
  topic of a specific room and return its updated details.
---

# Cisco Webex Teams - Update room action

This action updates the topic of a specific room in Cisco Webex Teams.

## Input

| Field | Description |
| --- | --- |
| Room name | Select the room to update. You can choose from a list of rooms or use a specific room ID. |
| Topic | Enter the new topic for the room. |

## Output

| Field | Description |
| --- | --- |
| Creator ID | The ID of the person who created the room. |
| Room ID | The unique ID of the room. |
| Topic | The topic of the room. |
| Type | The type of the room. |
| Is locked | Indicates whether the room is locked. |
| Last activity | The timestamp of the last activity in the room. |
| Created | The timestamp when the room was created. |

---
