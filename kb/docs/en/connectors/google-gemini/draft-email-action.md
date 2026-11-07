---
url: 'https://docs.workato.com/en/connectors/google-gemini/draft-email-action.md'
description: The Draft email action generates an email from a prompt.
---

# Google Gemini - Draft email action

The **Draft email** action generates an email from a prompt. The response is split into Email subject and Email body datapills to facilitate mapping into subsequent recipe actions. The Email body datapill contains a placeholder greeting by default if the **Email description** is insufficient.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Gemini model to use. |
| Email description | Provide a description for the email as a prompt. |

## Output

| Output field | Description |
| --- | --- |
| Email subject | The email subject line returned by Gemini. |
| Email body | The email body returned by Gemini. |
| Sexually explicit | The likelihood that the text contains sexually explicit content. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Hate speech | The likelihood that the text contains or promotes hate speech, such as discriminatory symbols or context targeting protected groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Harassment | The likelihood that the text contains harassing behavior, threats, or abuse toward individuals or groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Dangerous content | The likelihood that the text contains dangerous or harmful content such as violence, self-harm, or instructions for unsafe behavior. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |

---

---
url: >-
  https://docs.workato.com/en/connectors/google-gemini/generate-text-embedding-action.md
description: >-
  The Generate text embedding action generates an embedding from the provided
  text.
---

# Google Gemini - Generate text embedding action

The **Generate text embedding** action generates an embedding from the provided text. Text embedding is a technique for representing text as numerical vectors. It uses deep neural networks trained on large text sets to generate vector representations that capture the meaning and context of a text.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Gemini model to use. |
| Text for embedding generation | Provide the text to convert into an embedding. Input text must not exceed 8192 tokens (approximately 6000 words). |

## Output

| Output field | Description |
| --- | --- |
| Value | The vector (embedding) returned by Gemini. |
| Sexually explicit | The likelihood that the text contains sexually explicit content. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Hate speech | The likelihood that the text contains or promotes hate speech, such as discriminatory symbols or context targeting protected groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Harassment | The likelihood that the text contains harassing behavior, threats, or abuse toward individuals or groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Dangerous content | The likelihood that the text contains dangerous or harmful content such as violence, self-harm, or instructions for unsafe behavior. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |

---
