---
url: 'https://docs.workato.com/en/connectors/google-gemini.md'
description: >-
  The Google Gemini connector enables you to automate AI workflows with a
  multimodal LLM that interprets and generates text, images, audio, and code.
---

# Google Gemini

[Google Gemini](https://gemini.google.com/) is a large language model (LLM) and AI chatbot developed by Google. Gemini is a multimodal AI, meaning it can interpret and generate text, images, audio, and code. Gemini is designed to be a versatile tool for various tasks, from answering questions and generating creative content to assisting with research, coding, and even acting as a personal assistant within Google Workspace apps.

## Prerequisites

Workato requires an API key to connect to Gemini. Complete the following steps to generate an API key:

1. Sign in to [Google AI Studio](https://aistudio.google.com/app/apikey). Ensure billing is configured correctly if you plan to use paid features or exceed free quotas.
   
2. Accept the terms and conditions if prompted.
   
3. Click **\+ Create API key**.
   
4. Select a project to store the API key in.
   
5. Click **Create API key**.
   
6. **Copy** the key and store it securely.
   

## How to connect to Google Gemini

Connecting to the Google Gemini involves the following steps:

1. [Download the Google Gemini connector from the community](#community-download)
2. [Complete setup in Workato](#workato-setup)

### Download the Gemini connector from the community

Complete the following steps to install the Google Gemini connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Complete setup in Workato

Complete the following steps to establish a connection to Google Gemini in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Gemini** as your connection in the **New connection** page.
   
3. Provide a **Connection name** that identifies which Gemini instance Workato is connected to. ![Google Gemini connection](/assets/connection.Dlx0LAIE.png)_Google Gemini connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Gemini **API Key**. Refer to the [Prerequisites](#prerequisites) section to retrieve this value.
   
6. Click **Sign in with Google** to establish the connection.

---
