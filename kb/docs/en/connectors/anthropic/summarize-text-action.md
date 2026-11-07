---
url: 'https://docs.workato.com/en/connectors/anthropic/summarize-text-action.md'
description: The Summarize text action summarizes inputted text into a shorter version.
---

# Anthropic - Summarize text action

The **Summarize text** action condenses your input text into a shorter version in Anthropic. You can configure the length of the summary.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Anthropic model to use. For example, `Claude 3 Haiku`. |
| Source text | Enter the text you plan to summarize. |
| Maximum words | Enter the maximum number of words for the summary. Defaults to `200` if left blank. |
| Max tokens | Enter the maximum number of tokens to generate before stopping. Defaults to `4096` if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Anthropic reply | The generated summary of the input text. |

---
