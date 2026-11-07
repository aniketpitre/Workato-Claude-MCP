---
url: 'https://docs.workato.com/en/connectors/anthropic/draft-email-action.md'
description: >-
  The Draft email action generates an email based on a user description in
  Anthropic.
---

# Anthropic - Draft email action

The **Draft email** action generates an email in Anthropic and parses the result into separate subject and body datapills. The body contains placeholder text for a salutation if your email description doesn't include one.

## Input

| Input field | Description |
| --- | --- |
| Model | Select the Anthropic model to use. For example, `Claude 3 Haiku`. |
| Email description | Enter a description for the email. |
| Max tokens | Enter the maximum number of tokens to generate before stopping. Defaults to `4096` if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Email subject | The generated subject line of the email. |
| Email body | The generated body of the email. |

---
