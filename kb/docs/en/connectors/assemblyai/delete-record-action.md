---
url: 'https://docs.workato.com/en/connectors/assemblyai/delete-record-action.md'
description: Permanently redact a transcript's content in AssemblyAI.
---

# AssemblyAI - Delete record action

The **Delete record** action permanently redacts a record's content, such as a transcript, in AssemblyAI.

> **CONTENT IS REDACTED, NOT REMOVED**
> 
> AssemblyAI doesn't remove the transcript record. It redacts the content instead. For example, **Text** becomes `Deleted by user.`, **Audio URL** becomes `http://deleted_by_user`, and **Status** stays `completed`.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object, such as **Transcript**. |
| Transcript ID | Enter the UUID of the transcript to delete. |

## Output

Output fields are dynamically generated based on the object you select. Refer to the AssemblyAI [Transcript](https://www.assemblyai.com/docs/api-reference/transcripts/get) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| ID | The record's unique identifier. |
| Status | The record's status. The status stays `completed` after deletion. |
| Text | Redacted to `Deleted by user.`. |
| Audio URL | Redacted to `http://deleted_by_user`. |

---
