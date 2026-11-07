---
url: 'https://docs.workato.com/en/connectors/google-gemini/translate-text-action.md'
description: >-
  The Translate text action translates a provided text into a different
  language.
---

# Google Gemini - Translate text action

The **Translate text** action translates a provided text into a different language. While other languages may be possible, languages not on the predefined list may not provide reliable translations.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Gemini model to use. |
| Output language | Select the output language to translate to. |
| Source text | Provide the text to translate. |
| Source language | Select the source language for the text. |

## Output

| Output field | Description |
| --- | --- |
| Gemini reply | The response from Gemini. |
| Sexually explicit | The likelihood that the text contains sexually explicit content. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Hate speech | The likelihood that the text contains or promotes hate speech, such as discriminatory symbols or context targeting protected groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Harassment | The likelihood that the text contains harassing behavior, threats, or abuse toward individuals or groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Dangerous content | The likelihood that the text contains dangerous or harmful content such as violence, self-harm, or instructions for unsafe behavior. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |

---
