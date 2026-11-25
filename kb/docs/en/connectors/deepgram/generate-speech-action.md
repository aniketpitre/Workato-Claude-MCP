---
url: 'https://docs.workato.com/en/connectors/deepgram/generate-speech-action.md'
description: >-
  Convert text to speech audio in Deepgram with an Aura voice model and the
  audio format you choose.
---

# Deepgram - Generate speech action

The **Generate speech** action converts text to speech audio in Deepgram. Choose an Aura voice model and the output audio format.

## Input

The following are a representative set of input fields. Refer to the Deepgram [API](https://developers.deepgram.com/reference/text-to-speech/speak-request) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Text | Enter the text to convert to speech. |
| Voice model | Optional. Select the Aura voice model. Defaults to **aura-asteria-en** if left blank. |
| Encoding | Optional. Select the encoding of the output audio. Options include **Linear16 (16-bit PCM)**, **Mu-law**, or **MP3**. Leave blank to use Deepgram's default. |
| Container | Optional. Select the container for the output audio. Options are **WAV**, **None**, or **OGG**. Use **WAV** or **None** with the Linear16, Mu-law, and A-law encodings, and **OGG** with Opus. Leave blank for the MP3, FLAC, and AAC encodings. |
| Sample rate | Optional. Enter the sample rate in Hz, for example `24000`. You can't configure the sample rate for the MP3, Opus, and AAC encodings. Leave blank to use Deepgram's default. |
| Bit rate | Optional. Enter the bit rate in bps, for example `48000`. The bit rate applies only to the MP3, Opus, and AAC encodings. Leave blank to use Deepgram's default. |
| Speed | Optional. Enter the speaking rate multiplier. Deepgram doesn't support this field in all languages. Defaults to `1` if left blank. |
| Opt out of model improvement program | Optional. Select **Yes** to opt out of the Deepgram model improvement program. Opting out can affect pricing. Leave blank to stay in the program. |
| Tags | Optional. Enter comma-separated labels to attach to the request for usage reporting. Leave blank to send no tags. |
| Callback URL | Optional. Enter the URL where Deepgram sends the result when processing finishes. The action returns only the **Request ID** when you set a callback URL. Leave blank to return the audio in the action output. |

## Output

| Output field | Description |
| --- | --- |
| Audio content | The audio file contents. The **Audio content** field is only available when **Callback URL** is blank. |
| Content type | The MIME type of the audio, for example `audio/wav`. The **Content type** field is only available when **Callback URL** is blank. |
| Request ID | The unique ID of the request. |
| Model name | The name of the voice model that generated the audio. The **Model name** field is only available when **Callback URL** is blank. |
| Character count | The number of characters in the input text. The **Character count** field is only available when **Callback URL** is blank. |

---
