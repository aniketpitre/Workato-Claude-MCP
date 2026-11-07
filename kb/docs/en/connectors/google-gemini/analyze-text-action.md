---
url: 'https://docs.workato.com/en/connectors/google-gemini/analyze-text-action.md'
description: >-
  The Analyze text action performs a contextual analysis of a text to answer
  user-provided questions.
---

# Google Gemini - Analyze text action

The **Analyze text** action performs a contextual analysis of a text to answer user-provided questions. The response datapill is returned empty if an answer isn't found in the text.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Gemini model to use. |
| Source text | Enter the text to analyze. |
| Instructions | Enter instructions for the analysis. For example, you can specify an analysis technique or a question to answer. |

## Output

| Output field | Description |
| --- | --- |
| Gemini reply | The text reply from Gemini. |
| Sexually explicit | The likelihood that the text contains sexually explicit content. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Hate speech | The likelihood that the text contains hate speech, such as discriminatory symbols or content targeting protected groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Harassment | The likelihood that the text contains harassing behavior, threats, or abuse toward individuals or groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Dangerous content | The likelihood that the text contains dangerous or harmful content such as violence, self-harm, or instructions for unsafe behavior. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |

---
