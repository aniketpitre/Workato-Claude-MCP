---
url: 'https://docs.workato.com/en/connectors/google-gemini/categorize-text-action.md'
description: The Categorize text action sorts text into categories.
---

# Google Gemini - Categorize text action

The **Categorize text** action sorts text into categories. The output datapill contains the category that matches most closely or an error if no category is found. You can create a `none` category using the **List of categories** parameter.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Gemini model to use. |
| Source text | Provide the text to categorize. |
| List of categories | Create a list of categories to sort the text into and provide rules to classify what each category represents. |

## Output

| Output field | Description |
| --- | --- |
| Best matching category | The category replied by Gemini. |
| Sexually explicit | The likelihood that the text contains sexually explicit content. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Hate speech | The likelihood that the text contains or promotes hate speech, such as discriminatory symbols or context targeting protected groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Harassment | The likelihood that the text contains harassing behavior, threats, or abuse toward individuals or groups. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |
| Dangerous content | The likelihood that the text contains dangerous or harmful content such as violence, self-harm, or instructions for unsafe behavior. `NEGLIGIBLE` indicates there is little to no risk of such content being present. |

---
