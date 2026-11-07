---
url: 'https://docs.workato.com/en/connectors/assemblyai/get-record-action.md'
description: >-
  Retrieve a transcript by ID, including its full text and word-level details,
  from AssemblyAI.
---

# AssemblyAI - Get record action

The **Get record** action retrieves a record, such as a transcript, by ID from AssemblyAI.

> **FETCH THE FINISHED TRANSCRIPT**
> 
> Use this action after the [Create record](/en/connectors/assemblyai/create-record-action) action or the [Completed transcript](/en/connectors/assemblyai/completed-transcript-trigger) trigger to retrieve the full transcript text and metadata. This is necessary because the **Create record** action and the **Completed transcript** trigger don't return the finished content directly.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object, such as **Transcript**. |
| Transcript ID | Enter the transcript's UUID. Use the **ID** output from the [Create record](/en/connectors/assemblyai/create-record-action) or the [Transcribe and wait](/en/connectors/assemblyai/transcribe-and-wait-action) actions, or the **Transcript ID** output from the [Completed transcript](/en/connectors/assemblyai/completed-transcript-trigger) trigger. |

## Output

Output fields are dynamically generated based on the object you select. The following output fields are common to every object. Refer to the AssemblyAI [Transcript](https://www.assemblyai.com/docs/api-reference/transcripts/get) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| ID | The record's unique identifier. |
| Status | The record's status, for example `completed`. |
| Text | The transcribed text. The **Text** field is only available when **Status** is `completed`. |
| Words | A list of word-level objects. The **Words** field is only available when **Status** is `completed`. |
| Text (Words) | The word's transcribed text. |
| Start (Words) | The word's start time, in milliseconds. |
| End (Words) | The word's end time, in milliseconds. |
| Confidence (Words) | The model's confidence score for this word, between 0 and 1. |
| Speaker (Words) | The identified speaker label for this word. The **Speaker** field is only available when **Speaker labels** is **Yes** on the submit action. |
| Channel (Words) | The audio channel this word came from, for multichannel audio recordings. |

---
