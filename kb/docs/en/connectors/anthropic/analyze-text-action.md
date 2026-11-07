---
url: 'https://docs.workato.com/en/connectors/anthropic/analyze-text-action.md'
description: >-
  The Analyze text action performs a contextual analysis of text to answer
  user-provided questions in Anthropic.
---

# Anthropic - Analyze text action

The **Analyze text** action analyzes a block of text to answer questions you provide in Anthropic. The datapill is empty if the answer isn't found in the text.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Anthropic model you plan to use. For example, `Claude 3 Haiku`. |
| Source text | Enter the text you plan to analyze. |
| Instruction | Enter analysis instructions, such as an analysis technique or question to answer. |
| Max tokens | Enter the maximum number of tokens to generate before stopping. Defaults to `4096` if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Anthropic reply | The answer to the user's question, based on the analyzed text. Empty if the answer isn't found in the text. |

---
