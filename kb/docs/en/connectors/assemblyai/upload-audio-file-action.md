---
url: 'https://docs.workato.com/en/connectors/assemblyai/upload-audio-file-action.md'
description: >-
  Send raw audio bytes to AssemblyAI and get back a URL you can pass to a
  transcription request.
---

# AssemblyAI - Upload audio file action

The **Upload audio file** action uploads raw audio bytes to AssemblyAI and returns a URL you can use as the audio source when you create a transcript.

> **SEND RAW BYTES, NOT JSON**
> 
> Map a file content datapill so the request body is raw audio bytes (`application/octet-stream`). Sending JSON instead returns a URL that fails when you try to transcribe it.

## Input

| Input field | Description |
| --- | --- |
| File contents | Map a file content datapill with the raw audio bytes to upload. |

## Output

| Output field | Description |
| --- | --- |
| Upload URL | The uploaded file's URL. Use this as the audio URL when you create a transcript. |

---
