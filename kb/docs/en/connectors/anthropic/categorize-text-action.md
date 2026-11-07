---
url: 'https://docs.workato.com/en/connectors/anthropic/categorize-text-action.md'
description: >-
  The Categorize text action chooses the category that fits the input text from
  a list of user-defined categories in Anthropic.
---

# Anthropic - Categorize text action

The **Categorize text** action selects the category that fits the input text from a list of categories you define in Anthropic. The output datapill returns the category with the closest match, or an error if there is no match. Add an explicit no-match option to your list of categories to allow for no match.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Anthropic model you plan to use. For example, `Claude 3 Haiku`. |
| Source text | Provide the text you plan to categorize. |
| List of categories | Enter categories you plan to sort the text into. Each category has a **Category** name and an optional **Rule** providing additional details to help classify what the category represents. |
| Max tokens | Enter the maximum number of tokens to generate before stopping. Defaults to `4096` if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Best matching category | The category with the closest match to the input text. |

---
