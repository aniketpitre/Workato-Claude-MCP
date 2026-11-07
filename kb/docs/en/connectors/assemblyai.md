---
url: 'https://docs.workato.com/en/connectors/assemblyai.md'
description: >-
  Transcribe audio, export subtitles, and run LLM prompts over transcripts, then
  trigger recipes when jobs finish.
---

# AssemblyAI

[AssemblyAI](https://www.assemblyai.com) provides speech-to-text, speech understanding, and LLM Gateway APIs for voice AI workflows. The AssemblyAI connector lets you upload audio, transcribe it, export subtitles, and run LLM prompts over the results.

Use the AssemblyAI connector to:

- Upload an audio file and receive an upload URL for transcription.
- Submit a transcript and wait until it completes.
- Create, get, search, or delete transcripts.
- Export SRT or VTT subtitles for a completed transcript.
- Apply an LLM prompt to a transcript, or generate speech understanding, such as translation or speaker identification.
- Trigger a recipe when a transcript completes.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any AssemblyAI API endpoint. Refer to the [AssemblyAI Documentation](https://www.assemblyai.com/docs/api-reference/overview) for endpoint details.

## Install AssemblyAI from the community library

Complete the following steps to install the AssemblyAI connector from the [community library](https://www.workato.com/browse/connectors):

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

The AssemblyAI connector uses API key authentication.

### AssemblyAI setup for API key authentication

Complete the following steps to create an AssemblyAI API key:

1. Sign in to your [AssemblyAI dashboard](https://www.assemblyai.com/dashboard/).
   
2. Go to **Workspaces > Manage > API Keys**.
   
3. Click **Create New API Key**.
   
4. Enter a descriptive name, for example `Production API`.
   
5. Click **Create**.
   
6. Copy and save the API key for use in Workato.
   
   > **SAVE YOUR KEY**
   > 
   > You can't view the full API key again. If you lose it, you must create a new one.
   

### Connect to AssemblyAI using API key authentication

Complete the following steps to set up a AssemblyAI connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `AssemblyAI` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![AssemblyAI connection setup details](/assets/assemblyai-connection-setup.C8Z8VB2X.png)_AssemblyAI connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **API key**. Refer to [AssemblyAI setup for API key authentication](#assemblyai-setup) for more information.
   
6. Optional. Use the **Region** drop-down menu to select **US** or **EU**. The default is **US**. Select **EU** to route requests through AssemblyAI's EU-hosted API and LLM Gateway endpoints instead of the US endpoints. Refer to the AssemblyAI [EU data residency FAQ](https://www.assemblyai.com/docs/faq/do-you-offer-eu-data-residency) for what this assures from AssemblyAI.
   
7. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/assemblyai/completed-transcript-trigger.md
description: >-
  Fire a recipe when a transcript job finishes using a static webhook you set on
  the submit action.
---

# AssemblyAI - Completed transcript trigger

The **Completed transcript** trigger invokes when a transcript's status reaches **completed** in AssemblyAI.

> **STATIC WEBHOOK, NO SUBSCRIPTION API**
> 
> This trigger uses a static webhook URL. Copy the webhook URL from the trigger step after you save the recipe. Set it as the **Webhook URL** field on the [Create record](/en/connectors/assemblyai/create-record-action) or [Transcribe and wait](/en/connectors/assemblyai/transcribe-and-wait-action) action when you submit a transcript. AssemblyAI doesn't have a subscription API for this webhook.

> **NO TRANSCRIPT TEXT IN THE PAYLOAD**
> 
> AssemblyAI's webhook payload includes only the transcript ID and status, not the transcript text. Chain a [Get record](/en/connectors/assemblyai/get-record-action) action step using the trigger's **Transcript ID** output to fetch the full transcript.

## Input

| Input field | Description |
| --- | --- |
| Webhook auth header name | Optional. Enter the same header name you set as **Webhook auth header name** when you submitted the transcript, for example `X-My-Webhook-Secret`. Leave the **Webhook auth header name** field blank only if you didn't configure webhook authentication on the submit action. |
| Webhook auth header value | Optional. Enter the same header value you set as **Webhook auth header value** when you submitted the transcript. Leave the **Webhook auth header value** field blank only if you didn't configure webhook authentication on the submit action. |

## Output

| Output field | Description |
| --- | --- |
| Transcript ID | The completed transcript's unique identifier. |
| Status | The transcript's status, for example `completed`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/assemblyai/apply-llm-to-transcript-action.md
description: >-
  Run an LLM Gateway chat completion over a transcript's text, or a free-form
  prompt, in AssemblyAI.
---

# AssemblyAI - Apply LLM to transcript action

The **Apply LLM to transcript** action calls AssemblyAI's LLM Gateway to run a chat completion, optionally injecting a transcript's text into the prompt. Use this action for summaries, action items, or other free-form LLM tasks over a transcript.

> **INJECT THE TRANSCRIPT WITH A PLACEHOLDER**
> 
> Enter a **Transcript ID** and include the literal tag `{{ transcript }}` (exact spacing) in **Prompt** or **Messages**. AssemblyAI replaces the tag with the transcript's text before sending the request to the model.

## Input

The following are a representative set of input fields. Refer to the AssemblyAI [Chat completions](https://www.assemblyai.com/docs/llm-gateway/chat-completions) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Model | Select an LLM Gateway model, or enter a custom model ID. |
| Transcript ID | Optional. Enter a transcript's UUID to make it available to the `{{ transcript }}` placeholder. |
| Prompt | Enter a simple text prompt. Use this or **Messages**. |
| Messages | Enter OpenAI-style messages, each with a **Role** and **Content**. Use this or **Prompt**. |
| Max tokens | Optional. Enter the maximum number of tokens to generate. Default **1000**. |
| Temperature | Optional. Enter the sampling temperature. Valid values are 0-2. |
| Stream | Optional. Select **Yes** or **No** to stream SSE responses. Only for OpenAI models. Leave off for standard JSON responses in recipes. |
| Model region | Optional. Enter the model region to opt into global routing. The only accepted value is `global`. |

This action also supports function calling (**Tools**, **Tool choice**, **Tool choice function**), structured JSON output (**Response format**), model fallbacks (**Fallbacks**, **Fallback config**), and **Post processing steps**. Refer to the AssemblyAI [Chat completions](https://www.assemblyai.com/docs/llm-gateway/chat-completions) documentation for more information on these fields.

## Output

The following are a representative set of output fields. Refer to the AssemblyAI [Chat completions](https://www.assemblyai.com/docs/llm-gateway/chat-completions) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Request ID | The LLM Gateway request's unique identifier. |
| Choices | The completion choices. |
| Message (Choices) | The message choices. |
| Role (Message) | The message author's role, for example `assistant`. |
| Content (Message) | The generated message text. |
| Finish reason (Choices) | The reason the model stopped generating, for example `stop` or `length`. |
| Http status code | The LLM Gateway HTTP response status code. |
| Response time | The request's round-trip time, in milliseconds. |

This action's response also includes an echo of the request (**Request**) and token usage (**Usage**). Refer to the AssemblyAI [Chat completions](https://www.assemblyai.com/docs/llm-gateway/chat-completions) documentation for more information on these fields.

---
