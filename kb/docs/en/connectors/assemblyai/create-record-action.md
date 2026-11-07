---
url: 'https://docs.workato.com/en/connectors/assemblyai/create-record-action.md'
description: >-
  Submit an uploaded audio file for transcription without waiting for the job to
  finish.
---

# AssemblyAI - Create record action

The **Create record** action submits an audio file to AssemblyAI for transcription and returns immediately, before the transcript finishes processing.

> **ASYNCHRONOUS SUBMIT**
> 
> This action doesn't wait for the transcript to complete before processing. Content fields such as **Text** and **Words** return empty until the job finishes. Chain a [Get record](/en/connectors/assemblyai/get-record-action) step, or set a **Webhook URL** and use the [Completed transcript](/en/connectors/assemblyai/completed-transcript-trigger) trigger, to retrieve the finished transcript.
> 
> Use the [Transcribe and wait](/en/connectors/assemblyai/transcribe-and-wait-action) action to create a record and wait for the transcript to finish processing in a single step instead.

## Input

The following are a representative set of input fields. Refer to the AssemblyAI [Transcript audio](https://www.assemblyai.com/docs/api-reference/transcripts/submit) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object | Select the object, such as **Transcript**. |
| Audio URL | Enter a publicly reachable audio URL, or the **Upload URL** output from the [Upload audio file](/en/connectors/assemblyai/upload-audio-file-action) action. |
| Custom spelling | Optional. Map custom spellings, each with one or more **From** terms and a single **To** replacement. |
| Redact static entities | Optional. Enter static entity redaction labels and terms. Converted to a map in the API payload. |
| Language code | Optional. Select the audio's language. Don't use this field together with **Language detection**. |
| Language detection | Optional. Select **Yes** or **No** to automatically detect the audio's language. Don't use this field together with **Language code**. |
| Speaker labels | Optional. Select **Yes** or **No** to enable speaker diarization labels. |
| Auto highlights | Optional. Select **Yes** or **No** to enable key phrase detection. AssemblyAI supports similar toggles for entity detection, sentiment analysis, IAB category detection, and content safety. |
| Redact PII | Optional. Select **Yes** or **No** to redact personally identifiable information from the transcript. |
| Redact PII policies | Select the PII categories to redact. Required when **Redact PII** is **Yes**, for newer accounts. |

## Output

Output fields are dynamically generated based on the object you select. The following output fields are common to every object. Refer to the AssemblyAI [Transcript](https://www.assemblyai.com/docs/api-reference/transcripts/get) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| ID | The record's unique identifier. |
| Status | The record's status, for example `queued` or `processing`. The **Status** field isn't `completed` yet on this action's response. |

---
