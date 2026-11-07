---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/elevenlabs-mcp-server.md'
description: >-
  Use the ElevenLabs MCP server to connect your LLM to ElevenLabs with tools for
  voice and model inspection as well as text-to-speech audio generation.
---

# ElevenLabs MCP server

The ElevenLabs MCP server enables LLMs to interact with ElevenLabs for text-to-speech audio generation through natural conversation. It provides tools to list available voices, inspect voice metadata, identify supported TTS models, and generate spoken audio from text without requiring direct interaction with the ElevenLabs interface.

## Uses

Use the ElevenLabs MCP server to perform the following actions:

- Generate spoken audio from user-provided or agent-generated text
- Apply inline emotion and style tags so audio matches the tone of the source content
- Create accessibility playback for written content
- Produce product walkthrough narration
- Prototype voices and personas before committing to a final choice
- Browse the voices available to your configured account
- Inspect a specific voice's metadata and default settings
- Identify the TTS models supported by your account

### Example prompts

Use the following example prompts to invoke ElevenLabs MCP server tools:

- `Show me the voices available in my account.`
- `Get the details and default settings for the Rachel voice.`
- `Which TTS models can I use for audio generation?`
- `Convert this daily brief into audio using a clear, professional voice.`
- `Generate an MP3 narration of this product walkthrough.`
- `Create an audio version of this article for accessibility playback.`
- `Use the latest multilingual model to generate this narration.`
- `Narrate this announcement with an excited tone using the expressive eleven_v3 model.`
- `Try a few different voices for this intro so I can compare personas.`

## ElevenLabs MCP server tools

The ElevenLabs MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_voices](#list-voices-tool) | Lists the voices available to your configured account with metadata. |
| [get\_voice](#get-voice-tool) | Retrieves detailed metadata and default settings for a specific voice. |
| [list\_models](#list-models-tool) | Lists the TTS models available to your configured account. |
| [generate\_audio](#generate-audio-tool) | Generates spoken audio from text using a selected voice, model, output format, and optional voice settings. |

## Install the ElevenLabs MCP server

Complete the following steps to install a prebuilt MCP server to your project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
5. Click **Use this server**.
   
6. Provide a name for your MCP server in the **Server name** field.
   
7. Use the **Location** drop-down menu to select the project for the MCP server.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the MCP server template.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   ![Select your connection type](/assets/connection-type.Cor-6PJN.png)_Select your connection type_
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Complete the app-specific connection setup steps in the following section.
    

## ElevenLabs connection setup

View ElevenLabs connection setup steps

The ElevenLabs connector uses API key authentication.

### ElevenLabs setup for API key authentication

Refer to the ElevenLabs [Create API key](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create) guide to create an API key.

### Connect to ElevenLabs with an API key

View connect to ElevenLabs with an API key steps

Complete the following steps to connect to ElevenLabs in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `ElevenLabs` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![ElevenLabs connection](/assets/elevenlabs-connection-setup.CsWPn2u2.png)_ElevenLabs connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **API key**. Refer to the ElevenLabs [Create API key](https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/create) guide to create this value.
   
6. Use the **Region** drop-down menu to select the production region for ElevenLabs.
   
7. Click **Connect**.
   

## How to use ElevenLabs MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_voices tool

The **list\_voices** tool lists the voices available to your configured account and returns metadata that helps select an appropriate voice. Your LLM uses this tool to find which voices it can use and to choose one that matches a user's tone, language, or persona requirements.

**Try asking**:

- `Show me the voices available in my account.`
- `Which voices can I use for a narration?`
- `List the voices that work well for a calm, professional tone.`

### get\_voice tool

The **get\_voice** tool retrieves detailed metadata and default settings for a specific voice. Your LLM uses this tool to understand how a voice should be used and to confirm its default configuration.

**Try asking**:

- `Get the details for the Rachel voice.`
- `What are the default settings for this voice?`
- `Show me the configuration for the voice I selected.`

### list\_models tool

The **list\_models** tool lists the TTS models available to your configured account. Your LLM uses this tool to identify which models it can choose from.

**Try asking**:

- `Which TTS models can I use?`
- `List the available text-to-speech models.`
- `What model should I use for multilingual narration?`

### generate\_audio tool

The **generate\_audio** tool generates spoken audio from text using a selected voice, model, output format, and optional voice settings. Your LLM uses this tool to convert user-provided or agent-generated text into an audio file. The audio returns as an MP3 by default. You can use inline emotion and style tags, such as `[excited]` or `[whispering]`, for expressive output when you use a compatible model like `eleven_v3`.

**Try asking**:

- `Convert this daily brief into audio using a professional voice.`
- `Generate an MP3 narration of this script.`
- `Read this story aloud with [whispering] and [excited] emotion tags using the eleven_v3 model.`
- `Read this article aloud for accessibility playback.`

## Getting started

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.

---
