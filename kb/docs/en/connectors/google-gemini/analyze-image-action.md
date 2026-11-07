---
url: 'https://docs.workato.com/en/connectors/google-gemini/analyze-image-action.md'
description: The Analyze image action analyses an image and answers a related question.
---

# Google Gemini - Analyze image action

The **Analyze image** action analyses an image and answers a related question.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Gemini model to use. |
| Your question about the image | Specify a question for the image analysis. |
| Image data | Provide a base64 encoded image for analysis. |

## Output

| Output field | Description |
| --- | --- |
| Gemini reply | The text reply from Gemini. |
| Sexually explicit | The likelihood that the image contains sexually explicit content. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Hate speech | The likelihood that the image contains hate speech, such as discriminatory symbols or content targeting protected groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Harassment | The likelihood that the image contains harassing behavior, threats, or abuse toward individuals or groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Dangerous content | The likelihood that the image contains dangerous or harmful content such as violence, self-harm, or instructions for unsafe behavior. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |

---
