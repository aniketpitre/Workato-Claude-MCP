---
url: 'https://docs.workato.com/en/connectors/assemblyai/search-records-action.md'
description: >-
  List transcripts in AssemblyAI, with filters for status, creation date, and
  pagination.
---

# AssemblyAI - Search records action

The **Search records** action lists records, such as transcripts, in AssemblyAI.

> **PAGE BY CHAINING IDS**
> 
> AssemblyAI paginates with **Before ID** / **After ID** instead of with page numbers. Copy a transcript ID from **Records**, or parse the `after_id` value from **Page details**' **Next URL**, and pass it as this action's **After ID** input to paginate through search results.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object, such as **Transcript**. |
| Limit | Optional. Enter the maximum number of transcripts to return. Valid values are 1-200. The default is **10**. |
| Status | Optional. Select a status to filter by, such as **Completed**. |
| Created on | Optional. Enter a date (`YYYY-MM-DD`) to only return transcripts created on that date. |
| Before ID | Optional. Enter a transcript ID to return transcripts created before it. Don't use this together with **After ID**. |
| After ID | Optional. Enter a transcript ID to return transcripts created after it. Don't use this together with **Before ID**. |
| Throttled only | Optional. Select **Yes** or **No** to only return throttled transcripts. This field overrides **Status**. |

## Output

The following are a representative set of output fields. Refer to the AssemblyAI [List transcripts](https://www.assemblyai.com/docs/api-reference/transcripts/list) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Records | A list of matching transcripts. |
| ID (Records) | The transcript's unique identifier. Use this to paginate with **Before ID** or **After ID**. |
| Status (Records) | The transcript's status, for example `completed`. |
| Created (Records) | The date and time the transcript was created. |
| Completed (Records) | The date and time the transcript finished processing. The **Completed** field is only available when **Status** is `completed`. |
| Page details | Pagination information. |
| Limit (Page details) | The **Limit** value used for this request. |
| Result count (Page details) | The number of records returned on this page. |
| Next URL (Page details) | The URL to fetch the next page of results. Parse its `after_id` value to paginate with **After ID**. |

Each record in **Records** also includes **Resource URL**, **Audio URL**, **Error**, and **Region**. **Page details** also includes **Current URL** and **Prev URL**. Refer to the AssemblyAI [List transcripts](https://www.assemblyai.com/docs/api-reference/transcripts/list) documentation for more information on these fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/assemblyai/transcribe-and-wait-action.md
description: >-
  Submit an audio file for transcription and poll AssemblyAI until the
  transcript completes, in a single action.
---

# AssemblyAI - Transcribe and wait action

The **Transcribe and wait** action submits an audio file to AssemblyAI for transcription, then polls every 60 seconds until the transcript's status reaches **completed**, and returns the finished transcript.

> **SYNCHRONOUS SUBMIT, BOUNDED WAIT**
> 
> This action polls for a maximum of 60 minutes and this setting is configurable in the **Max poll minutes** field, which is 60 by default. Use the [Create record](/en/connectors/assemblyai/create-record-action) action with a **Webhook URL** and the [Completed transcript](/en/connectors/assemblyai/completed-transcript-trigger) trigger for longer running jobs.

## Input

The following are a representative set of input fields. Refer to the AssemblyAI [Transcript audio](https://www.assemblyai.com/docs/api-reference/transcripts/submit) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Audio URL | Enter a publicly reachable audio URL, or the **Upload URL** output from the [Upload audio file](/en/connectors/assemblyai/upload-audio-file-action) action. |
| Custom spelling | Optional. Map custom spellings, each with one or more **From** terms and a single **To** replacement. |
| Redact static entities | Optional. Enter static entity redaction labels and terms. Converted to a map in the API payload. |
| Language code | Optional. Select the audio's language. Don't use this field together with **Language detection**. |
| Language detection | Optional. Select **Yes** or **No** to automatically detect the audio's language. Don't use this field together with **Language code**. |
| Speaker labels | Optional. Select **Yes** or **No** to enable speaker diarization labels. |
| Auto highlights | Optional. Select **Yes** or **No** to enable key phrase detection. AssemblyAI supports similar toggles for entity detection, sentiment analysis, IAB category detection, and content safety. |
| Redact PII | Optional. Select **Yes** or **No** to redact personally identifiable information from the transcript. |
| Redact PII policies | Select the PII categories to redact. Required when **Redact PII** is **Yes**, for newer accounts. |
| Max poll minutes | Optional. Enter how many minutes to keep polling before the action times out. Default and maximum **60**. |

## Output

The following output fields are common to every response. Refer to the AssemblyAI [Transcript](https://www.assemblyai.com/docs/api-reference/transcripts/get) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| ID | The record's unique identifier. |
| Status | The record's status. Displays `completed` on this action's response. |
| Text | The transcribed text. |
| Words | A list of word-level objects. |
| Text (Words) | The word's transcribed text. |
| Start (Words) | The word's start time, in milliseconds. |
| End (Words) | The word's end time, in milliseconds. |
| Confidence (Words) | The model's confidence score for this word, between 0 and 1. |
| Speaker (Words) | The identified speaker label for this word. The **Speaker** field is only available when **Speaker labels** is **Yes**. |
| Channel (Words) | The audio channel this word came from, for multichannel audio recordings. |

---
