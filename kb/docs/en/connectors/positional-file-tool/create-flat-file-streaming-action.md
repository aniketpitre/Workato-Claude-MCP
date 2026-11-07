---
url: >-
  https://docs.workato.com/en/connectors/positional-file-tool/create-flat-file-streaming-action.md
description: >-
  The Create flat file (streaming) action creates a positional flat file from
  streaming CSV or JSON input in Positional file tool.
---

# Positional file tool - Create flat file (streaming) action

The **Create flat file (streaming)** action creates a positional flat file from streaming CSV or JSON input in Positional file tool.

## Input

| Input field | Description |
| --- | --- |
| Streaming content | Enter streaming content datapills from a file connector in CSV or JSON format. |
| Streaming input format | Select the format of the streaming input. Options are `CSV` or `JSON`. |
| Chunk size (MB) | Select the chunk size, in MB, to stream. |
| Line ending | Select the line ending character for the output flat file. |
| Merge flat file output? | Select `Yes` or `No` to decide to merge all schemas with the flat file output into a single file. |
| Schemas | Fields to define columns for the schema. Schema fields include `Schemas source list`, `Schemas fields`, `Schema name`, `Data source`, `Output destination`, `Upload URL`, and `Column specification`. |

## Output

| Output field | Description |
| --- | --- |
| Total lines generated | The total number of lines in the response flat file. |
| Total chunks processed | The total number of chunks processed in the streaming flat file. |
| Status | The status of the flat file response. |
