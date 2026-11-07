---
url: >-
  https://docs.workato.com/en/connectors/google-translate/action-translate-text.md
description: Allows you to translate any text into another language.
---

# Google Translate - Translate text action

This action allows you to translate any text into another language. You can define the source language or let Google detect the source language automatically.

## Input

| Input field | Description |
| --- | --- |
| Text | Provide the text to translate. This field accepts a text datapill or raw text. |
| Target language | Specify the target language to translate to. |
| Source language | Optionally, specify the source language of the text. If left blank, Google automatically detects the language. |

## Output

| Output field | Description |
| --- | --- |
| Translated text | The text translated to the target language. |
| Detected source language | Source language of the text that Google automatically detected. |
