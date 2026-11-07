---
url: 'https://docs.workato.com/en/connectors/anthropic/translate-text-action.md'
description: The Translate text action translates inputted text into a different language.
---

# Anthropic - Translate text action

The **Translate text** action translates your input text into a different language in Anthropic. Languages on the predefined list produce reliable translations. You can use other languages, but the results may be less reliable.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Anthropic model you plan to use. For example, `Claude 3 Haiku`. |
| Output language | Select the output language you plan to use, or toggle to enter a custom value. |
| Source language | Select the source language you plan to use, or toggle to enter a custom value. Anthropic automatically attempts to identify it if left blank. |
| Source text | Enter the text you plan to translate. Limit to `2,000` tokens. |
| Max tokens | Enter the maximum number of tokens to generate before stopping. Defaults to `4096` if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Anthropic reply | The translated text. |

---
