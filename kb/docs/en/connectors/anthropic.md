---
url: 'https://docs.workato.com/en/connectors/anthropic.md'
description: >-
  Anthropic provides large language models, including the Claude family, for
  tasks such as text generation, analysis, and conversation.
---

# Anthropic

[Anthropic](https://www.anthropic.com/) provides large language models, including the Claude family, for tasks such as text generation, analysis, and conversation. The Anthropic connector enables you to send messages to Anthropic models, and use built-in actions to analyze, categorize, parse, summarize, and translate text, and draft emails.

## Install the Anthropic connector from the community library

Complete the following steps to install the Anthropic connector from the [community library](https://www.workato.com/browse/connectors):

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

The Anthropic connector uses API key authentication.

### Anthropic setup

Complete the following steps to create an API key to use in an Anthropic connection:

1. Log in to the [Anthropic console](https://console.anthropic.com).
   
2. Go to **Settings > API Keys > Create Key**.
   
3. Enter a name for your API key, then copy and securely store the key that's displayed.
   

### Connect to Anthropic using API key authentication

Complete the following steps to connect to Anthropic in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Anthropic` and select it as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Create an Anthropic connection in Workato](/assets/anthropic-create-connection.BpEgIahp.png)_Create an Anthropic connection in Workato_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your API key in the **API key** field.
   
6. Use the **Version** field to select an Anthropic API version, or toggle to enter a custom version number. Defaults to `2023-06-01`.
   
7. Click **Connect**.

---
