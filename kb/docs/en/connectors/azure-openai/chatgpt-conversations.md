---
url: 'https://docs.workato.com/en/connectors/azure-openai/chatgpt-conversations.md'
description: >-
  The Send messages to ChatGPT action sends a message to Chat GPT and gathers a
  response using model GPT 3.5 Turbo from Azure OpenAI.
---

# Azure OpenAI - Send messages to ChatGPT action

The **Send messages to ChatGPT** action sends a message to ChatGPT and gathers a response using the GPT 3.5 Turbo model from Azure OpenAI. You can use this action as a single question-and-answer action or as a chat experience in your recipes.

![Send messages to ChatGPT action](/assets/azure-openai-chatgpt-conversations.CN0xx44s.png)_Send messages to ChatGPT action_

## Input

| Input field | Description |
| --- | --- |
| Deployment ID | Enter the deployment ID of the model you plan to use. You can find the deployment ID in **Azure AI Studio > Deployment**. |
| Single Message | Enter the message to send to the model with the role as user. |
| System role message | Optional. Enter a message that provides specific instructions to the model before starting a conversation. |
| Role | Select the role of the user corresponding to the specific message. |
| Content | Enter the message to send to the model for each corresponding role. |
| System role message | Optional. Enter a message to provide specific instructions to the model before starting a conversation. |
| Name | Enter the name of the author of a message. Often used for tracking chat transcripts. This can contain uppercase and lowercase characters, numbers, and underscores with a maximum length of 64 characters, with no blank spaces. |
| Model | Select the OpenAI model to which you plan to send the message. |
| Temperature | Enter a value between 0 and 2 for controlling the randomness of completions. Higher values make the output more random, while lower values make the output more focused and deterministic. Workato recommends using either `temperature` or `top p`. Refer to the [OpenAI documentation](https://platform.openai.com/docs/api-reference/edits/create#edits/create-temperature) for more information. |
| Number of chat completions | Enter the number of completions to generate as the message response. |
| Stop phrase | Enter a specific stop phrase that ends generation. For example, if you set the stop phrase to a period `.` the model generates text until it reaches a period, and then stops. Use this to control the amount of text generated. |
| Maximum tokens | Enter the maximum number of tokens to generate in the completion. The token count of your prompt, plus the maximum tokens value cannot exceed the model's context length. For longer prompts, Workato recommends setting a low value. Workato recommends leaving it blank if the prompt is likely to vary in length. |
| Presence penalty | Enter a presence penalty number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| User | Enter a unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. |

## Output

| Output field | Description |
| --- | --- |
| Created | The datetime stamp of when the response generated. |
| ID | A unique identifier denoting the request and response that was sent over. |
| Model | The model used to generate the text completion. |
| Message | The response of the model for the specified input. The role is `Assistant` by default. |
| Finish reason | The reason the model stopped generating more text. Possible reasons include `stop`, `length`, `content_filter`, and `null`. Refer to the [OpenAI documentation](https://platform.openai.com/docs/guides/text-generation/chat-completions-response-format) for more information. |
| Response | Contains the response which OpenAI considers to be the ideal selection. |
| Prompt tokens | The number of tokens used by the prompt. |
| Completions tokens | The number of tokens used for text completions. |
| Total tokens | The total number of tokens used by the prompt and response. |

---
