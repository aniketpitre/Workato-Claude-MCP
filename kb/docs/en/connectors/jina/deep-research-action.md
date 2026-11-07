---
url: 'https://docs.workato.com/en/connectors/jina/deep-research-action.md'
description: >-
  Get a structured research answer from Jina DeepSearch, with support for JSON
  schema output and hostname allow and block lists.
---

# Jina - Deep research action

The **Deep research** action runs a DeepSearch chat completion in Jina. The **Deep research** action reasons over a conversation, searches and reads web pages before answering a query.

> **STREAMING IS DISABLED**
> 
> This action waits for the full response. Keep **Reasoning effort** at the default setting, **Low**, to enable faster responses.

## Input

| Input field | Description |
| --- | --- |
| Model | Optional. Select a DeepSearch model, or enter a custom model ID. The default is `jina-deepsearch-v1`. |
| Messages | Enter one or more messages. |
| Role (Messages) | Select the message author's role. Options are **User**, **Assistant**, or **System**. |
| Content (Messages) | Enter the message text. |
| Reasoning effort | Optional. Select **Low**, **Medium**, or **High**. The default is **Low**. |
| Max returned URLs | Optional. Enter the maximum number of URLs to return. |
| Boost hostnames | Optional. Enter hostnames to prioritize during research. |
| Response format type | Optional. Select the type of response format. Options are **Text**, **JSON schema**, or **JSON object**. |
| Response format JSON schema | Optional. Enter a JSON schema for the response. The **Response format JSON schema** field is required when **Response format type** is **JSON schema**. |

This action also supports **Budget tokens**, **Max attempts**, and **No direct answer**. **Bad hostnames** and **Only hostnames** follow the same pattern as **Boost hostnames**, to exclude or restrict research to specific hostnames. Refer to the Jina [DeepSearch](https://jina.ai/deepsearch/) documentation for more information on these fields.

## Output

The following are a representative set of output fields. Refer to the Jina [DeepSearch](https://jina.ai/deepsearch/) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| ID | The completion's unique identifier. |
| Model | The model used. |
| Choices | The completion choices. |
| Message (Choices) | The generated message. |
| Role (Message) | The message author's role, for example `assistant`. |
| Content (Message) | The generated answer text. |
| Finish reason (Choices) | The reason the model stopped generating, for example `stop` or `length`. |
| Visited URLs | An array of URLs the research process visited. |
| Read URLs | An array of URLs the research process read in full. |
| Number of URLs | The total number of URLs used. |

---
