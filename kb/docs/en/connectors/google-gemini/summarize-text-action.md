---
url: 'https://docs.workato.com/en/connectors/google-gemini/summarize-text-action.md'
description: The Summarize text action summarizes a provided text.
---

# Google Gemini - Summarize text action

The **Summarize text** action summarizes a provided text. You can configure the length of the summary using the **Maximum words** field.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Gemini model to use. |
| Source text | Provide the text to summarize. |
| Maximum words | Enter the maximum number of words for the summary. If left blank, this field defaults to `200`. |

## Output

| Output field | Description |
| --- | --- |
| Gemini reply | The response from Gemini. |
| Sexually explicit | The likelihood that the text contains sexually explicit content. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Hate speech | The likelihood that the text contains or promotes hate speech, such as discriminatory symbols or context targeting protected groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Harassment | The likelihood that the text contains harassing behavior, threats, or abuse toward individuals or groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Dangerous content | The likelihood that the text contains dangerous or harmful content such as violence, self-harm, or instructions for unsafe behavior. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |

---
