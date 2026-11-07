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
