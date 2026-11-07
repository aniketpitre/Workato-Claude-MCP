---
url: >-
  https://docs.workato.com/en/connectors/google-text-to-speech/action-synthesize-text.md
description: >-
  The Convert text to speech action converts text into synthetic voice audio,
  supporting 30 voices and multiple languages.
---

# Google Text to Speech - Convert text to speech action

The **Convert text to speech** action converts text into synthetic voice audio, supporting 30 voices and multiple languages.

## Input

| Input field | Description |
| --- | --- |
| Text | Input the text you plan to convert into voice audio. This field can accept a datapill or raw text. |
| Voice language | Specify the [language code](https://cloud.google.com/speech-to-text/docs/languages) of the voice. Note that the conversion accuracy differs across languages. Google may not yet have full support for certain languages. |
| Voice gender | Specify the gender of the voice. |
| Audio encoding | Specify the encoding of the output audio file. |

## Output

| Output field | Description |
| --- | --- |
| Audio content | The string content of the converted audio. You can map this datapill to the **File contents** field of an **Upload file** action from any file connector such as Box or Dropbox and create an audio file. |
