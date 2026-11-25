---
url: 'https://docs.workato.com/en/connectors/deepgram/list-models-action.md'
description: >-
  List the speech-to-text and text-to-speech models available in Deepgram, with
  the option to include outdated versions.
---

# Deepgram - List models action

The **List models** action lists the public speech-to-text (STT) and text-to-speech (TTS) models in Deepgram. Optionally include outdated model versions.

## Input

| Input field | Description |
| --- | --- |
| Include outdated | Optional. Select **Yes** to include outdated model versions. Leave blank to return only the latest versions. |

## Output

The following are a representative set of output fields. Refer to the Deepgram [API](https://developers.deepgram.com/reference/manage/models/list) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| STT | The speech-to-text models. |
| Name (STT) | The name of the model. |
| Canonical name (STT) | The canonical name of the model. |
| Version (STT) | The version of the model. |
| TTS | The text-to-speech models. |
| Name (TTS) | The name of the model. |
| Canonical name (TTS) | The canonical name of the model. |
| Version (TTS) | The version of the model. |
| Languages | The languages Deepgram supports. |
| Code (Languages) | The language code. |

---
