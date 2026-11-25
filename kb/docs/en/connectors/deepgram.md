---
url: 'https://docs.workato.com/en/connectors/deepgram.md'
description: >-
  Connect Deepgram to Workato to transcribe audio, analyze text, generate
  speech, and list speech-to-text and text-to-speech models.
---

# Deepgram

[Deepgram](https://deepgram.com) provides voice AI APIs for speech-to-text, text intelligence, and text-to-speech. The Deepgram connector enables you to transcribe audio, analyze text, and generate speech in Workato.

Use the Deepgram connector to:

- Transcribe call recordings, meetings, and voicemails from a URL or uploaded file.
- Identify speakers and split transcripts into paragraphs and utterances.
- Summarize audio and text, and detect topics, intents, and sentiment.
- Convert text to speech with Aura voices.
- List available speech-to-text and text-to-speech models.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any Deepgram API endpoint. Refer to the Deepgram [API](https://developers.deepgram.com/reference/deepgram-api-overview) documentation for endpoint details.

## Install Deepgram from the community library

Complete the following steps to install the Deepgram connector from the [community library](https://www.workato.com/browse/connectors):

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

The Deepgram connector uses API key authentication. Workato sends the API key in the `Authorization` header.

### Deepgram setup for API key authentication

Complete the following steps to create a Deepgram API key:

1. Sign in to the [Deepgram Console](https://console.deepgram.com).
   
2. Use the **Projects** drop-down menu to select the project you want to associate with the API key. Deepgram creates a default project automatically during sign-up.
   
3. Click **Settings**.
   
4. Click **API Keys**.
   
5. Click **Create a New API Key**.
   
6. Enter a **Friendly name (Comment)**.
   
7. Select the expiration. Options are **Never**, **Duration**, or **Date**.
   
8. Optional. Expand the **Advanced** menu to change the role. Refer to the Deepgram [Project Roles](https://developers.deepgram.com/guides/deep-dives/working-with-roles) documentation for more information.
   
9. Click **Create Key**.
   
10. Copy and save the **Secret** for use in Workato.
    
    > **SAVE YOUR SECRET**
    > 
    > Deepgram displays the secret only once. You must create a new one if you lose the secret.
    
11. Click **Got it**.
    

### Connect to Deepgram using API key authentication

Complete the following steps to connect to Deepgram in Workato:

1. Click **Create > Connection**.
   
2. Search for `Deepgram` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Deepgram connection setup details](/assets/deepgram-connection-setup.C1BFbJZt.png)_Deepgram connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the secret you saved from Deepgram in the **API key** field. Refer to [Deepgram setup for API key authentication](#deepgram-setup) for more information.
   
6. Click **Connect**.

---
