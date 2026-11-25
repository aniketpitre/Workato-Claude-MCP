---
url: 'https://docs.workato.com/en/connectors/deepgram/transcribe-audio-action.md'
description: >-
  Transcribe pre-recorded audio or video in Deepgram from a media URL or file
  contents, with optional summaries, topics, intents, and sentiment.
---

# Deepgram - Transcribe audio action

The **Transcribe audio** action transcribes pre-recorded audio or video in Deepgram. Select a media URL or file contents, then choose the model and features such as diarization, paragraphs, summaries, and topics. The action waits for the transcription result only when **Callback URL** is blank.

## Input

Input fields dynamically generate based on the **Audio source** you select. The following are a representative set of input fields. Refer to the Deepgram [API](https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Audio source | Select **Media URL** to transcribe a hosted file, or **File contents** to upload the file bytes. |
| File contents | Enter the contents of the audio or video file to transcribe. The **File contents** field is only available when **Audio source** is **File contents**. |
| Media URL | Enter the publicly reachable URL of the audio or video file to transcribe. The **Media URL** field is only available when **Audio source** is **Media URL**. |
| Model | Optional. Select the model to use for transcription. Defaults to **base-general** if left blank. |
| Language | Optional. Select the language spoken in the audio. Defaults to **English (en)** if left blank. |
| Smart format | Optional. Select **Yes** to apply extra formatting, such as dates, currency, and numbers, for readability. Leave blank to skip smart formatting. |
| Summarize | Optional. Select **V2** to summarize the audio. Leave blank to return no summary. |
| Topics | Optional. Select **Yes** to detect the topics in the audio. Leave blank to skip topic detection. |
| Sentiment | Optional. Select **Yes** to analyze the sentiment of the audio. Leave blank to skip sentiment analysis. |
| Callback URL | Optional. Enter the URL where Deepgram sends the result when processing finishes. The action returns only the **Request ID** when you set a callback URL. Leave blank to return the result in the action output. |

## Output

The following are a representative set of output fields. Refer to the Deepgram [API](https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Request ID | The unique ID of the request. The **Request ID** field is only available when **Callback URL** is set. |
| Metadata | Information about the request. The **Metadata** field is only available when **Callback URL** is blank. |
| Request ID (Metadata) | The unique ID of the request. |
| Results | The transcription results. The **Results** field is only available when **Callback URL** is blank. |
| Channels (Results) | The transcription results for each audio channel. |
| Alternatives (Channels) | The transcription alternatives for the channel. |
| Transcript (Alternatives) | The transcript of the audio. |
| Summary (Results) | The summary of the audio. The **Summary** field is only available when **Summarize** is **V2**. |
| Topics (Results) | The topics detected in each segment of the audio. The **Topics** field is only available when **Topics** is **Yes**. |
| Sentiments (Results) | The sentiment of each segment and the average sentiment of the audio. The **Sentiments** field is only available when **Sentiment** is **Yes**. |

---
