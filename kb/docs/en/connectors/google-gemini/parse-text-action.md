---
url: 'https://docs.workato.com/en/connectors/google-gemini/parse-text-action.md'
description: The Parse text action extracts data you specify from a provided text.
---

# Google Gemini - Parse text action

The **Parse text** action extracts data you specify from a provided text.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Gemini model to use. |
| Source text | Provide the text to parse. |
| Fields to identify | Enter the fields that you want to identify from the text. |

## Output

This action returns the fields defined in the **Fields to identify** section, along with the following fields:

| Output field | Description |
| --- | --- |
| Sexually explicit | The likelihood that the text contains sexually explicit content. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Hate speech | The likelihood that the text contains or promotes hate speech, such as discriminatory symbols or context targeting protected groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Harassment | The likelihood that the text contains harassing behavior, threats, or abuse toward individuals or groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Dangerous content | The likelihood that the text contains dangerous or harmful content such as violence, self-harm, or instructions for unsafe behavior. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |

---

---
url: >-
  https://docs.workato.com/en/connectors/google-gemini/send-messages-to-gemini-models-action.md
description: >-
  The Send messages to Gemini models action sends a message to and receives a
  response from a Gemini model you specify.
---

# Google Gemini - Send messages to Gemini models action

The **Send messages to Gemini models** action sends a message to and receives a response from a Gemini model you specify. Fields are loaded dynamically based on the **Message type** you select. For example, the following are the input and output schemas if you select `Single message` as the **Message type**:

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Gemini model to use. |
| Message type | Select the type of message to send. |
| Text to send | Enter a message to send to Gemini. |
| Category | Select a safety category to evaluate, such as `HARM_CATEGORY_HATE_SPEECH`. |
| Threshold | Select the value threshold that a message must meet in the selected **Category** in order to block it. |
| Stop sequence | Provide a list of strings that cause the model to stop generating text. |
| Temperature | Enter a number to control the randomness of the model's output. A higher **Temperature** results in a more random output, while a lower **Temperature** results in a more predictable output. |
| Max output tokens | Specify the maximum number of tokens that the model can generate. |
| TopP | Specify a number to control the probability of the model generating each token. A higher **TopP** results in the model generating more likely tokens, while a lower **TopP** results in the model generating more unlikely tokens. Allowed values include any decimal value between 0 and 1. |
| TopK | Specify a number to control the number of tokens that the model considers when generating each token. A higher **TopK** results in the model considering more tokens, while a lower **TopK** results in the model considering fewer tokens. Allowed values include any positive integer. |

## Output

| Output field | Description |
| --- | --- |
| Gemini reply | The response from Gemini. |
| Sexually explicit | The likelihood that the text contains sexually explicit content. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Hate speech | The likelihood that the text contains or promotes hate speech, such as discriminatory symbols or context targeting protected groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Harassment | The likelihood that the text contains harassing behavior, threats, or abuse toward individuals or groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Dangerous content | The likelihood that the text contains dangerous or harmful content such as violence, self-harm, or instructions for unsafe behavior. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |

---
