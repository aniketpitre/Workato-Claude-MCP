---
url: 'https://docs.workato.com/en/connectors/telegram.md'
description: >-
  Connect Telegram to Workato to send messages and media, manage chats, and
  automate bot interactions with Telegram's Bot API.
---

# Telegram

[Telegram](https://telegram.org/) is a cloud-based instant messaging service. The Telegram connector uses the Telegram Bot API to let a Telegram bot send messages and automate interactions on your behalf.

Use the Telegram connector to:

- Send and update text messages, photos, documents, animations, stickers, locations, and venues in Telegram chats.
- Send messages with inline buttons or voice notes, and respond to button taps with callback query answers.
- Retrieve chat member and file information, and download files sent to your bot.
- Trigger recipes on new Telegram events, such as channel posts or messages.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any Telegram Bot API endpoint. Refer to the [Telegram Bot API documentation](https://core.telegram.org/bots/api) for endpoint details.

## Install Telegram from the community library

Complete the following steps to install the Telegram connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Telegram connector uses API token authentication.

### Telegram setup for API token authentication

Complete the following steps to create a Telegram bot and obtain its API token using the Telegram [BotFather](https://core.telegram.org/bots#6-botfather):

1. Open Telegram and start a chat with [@BotFather](https://t.me/botfather).
   
2. Send the `/newbot` command.
   
3. Follow the prompt to provide a name for your bot.
   
4. Follow the prompt to provide a username for your bot. The username must be unique and end in `bot`, for example `sample_workato_bot`. The username can't be changed later.
   
5. Copy the **API token**. Store it securely because anyone with the token has full control over the bot.
   

> **BOT PERMISSIONS APPLY TO THE CONNECTION**
> 
> This connector acts as your Telegram bot, so it can only do what that bot is allowed to do in Telegram. Add the bot to any chat, group, or channel you plan to automate, and grant it administrator rights if the actions you plan to use require them, such as posting to a channel.

### Connect to Telegram using API token authentication

Complete the following steps to set up a Telegram connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Telegram` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Connect to Telegram dialog details](/assets/telegram-connection-setup.CySKv3X6.png)_Telegram connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **API token**. Refer to [Telegram setup for API token authentication](#telegram-setup) for more information.
   
6. Click **Connect**.

---
