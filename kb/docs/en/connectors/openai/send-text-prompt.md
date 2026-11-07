---
url: 'https://docs.workato.com/en/connectors/openai/send-text-prompt.md'
description: >-
  The Send text prompt action in the OpenAI connector generates text completions
  for a prompt to autocomplete text, answer questions, or create content.
---

# OpenAI - Send text prompt action

This action generates completions for a given prompt using OpenAI's powerful language models. Simply provide a prompt and desired parameters, and the action will return one or multiple predicted completions. Use this action to autocomplete text, answer questions, and generate new content with ease.

![Send text prompt action](/assets/send-text-prompt.DkJhbntz.png)_Send Text Prompt Action_

## Input

| Field | Description |
| --- | --- |
| Model | Use the **Model** drop-down menu to select the OpenAI model you plan to use. You can click into the **Model** field and enter the model if it isn't listed. |
| Prompt | The prompt to generate completions for. If a prompt is not specified, the model generates as if from the beginning of a new document. If you plan to create responses for multiple strings, or by using tokens, input the relevant information as a datapill. Refer to [OpenAI's documentation](https://platform.openai.com/docs/api-reference/completions/create#completions/create-promp) for more information on prompt formats. |
| Maximum Tokens | The maximum number of tokens to generate in the completion. The token count of your prompt plus the value here cannot exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096). |
| Suffix | The suffix that comes after the completion of inserted text. |
| Top p | Enter a value between 0 and 1 for controlling the diversity of completions. A higher value will result in more varied responses. We recommend using this or temperature but not both. Refer to the OpenAI [top\_p parameter](https://platform.openai.com/docs/api-reference/edits/create#edits/create-top_p) documentation for more information. |
| Temperature | Enter a value between 0 and 2 to control the randomness of completions. Higher values will make the output more random, while lower values will make it more focused and deterministic. We recommend using this or top p but not both. Refer to the OpenAI [temperature parameter](https://platform.openai.com/docs/api-reference/edits/create#edits/create-temperature) documentation for more information. |
| Number of completions | The number of completions to generate for the prompt. |
| Log probabilities | Enter a number to obtain the log probabilities on the next n (determined by this value) set of likely tokens and the chosen token. Refer to the OpenAI [log probabilities parameter](https://platform.openai.com/docs/api-reference/completions/create#completions/create-logprobs) documentation for more information. |
| Stop phrase | A specific stop phrase that will end generation. For example, if you set the stop phrase to a period (.) the model will generate text until it reaches a period, and then it will stop. Use this to control the amount of text generated. |
| Presence penalty | A number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. |
| Frequency penalty | A number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood of repeating the same line verbatim. |
| Best of | Controls how many results are actually generated before being sent over. Note that number of completions cannot be less than the value input here. |
| Logit bias | Input a JSON containing the tokens and the change in logit for each of those specific tokens. For example, you can pass {"50256": -100} to prevent the `<|endoftext|>` token from being generated. Refer to the OpenAI [logit bias parameter](https://platform.openai.com/docs/api-reference/completions/create#completions/create-logit_bias) documentation for more information. |
| User | A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. |

## Output

| Field | Description |
| --- | --- |
| Created | The datetime stamp of when the response was generated. |
| ID | Unique identifier denoting the specific request and response that was sent over. |
| Model | The model used to generate the text completion. |
| Choices | Text | The response of the model for the specified input. |
| Finish reason | The reason why the model stopped generating more text. This is often due to stop words or length. |
| Logprobs | An object containing the tokens as well as their corresponding probabilities. For example, if log probabilities was set to 5, you will receive a list of the 5 most likely tokens. The response contains the logprob of the sampled token, so there may be up to logprobs+1 elements in the response. |
| Best choice | Contains the response which OpenAI probabilistically considers to be the ideal selection. |
| Usage | Prompt tokens | The number of tokens utilized by the prompt. |
| Completions tokens | The number of tokens utilized for the completions of text. |
| Total tokens | The total number of tokens utilized by the prompt and response. |

---
