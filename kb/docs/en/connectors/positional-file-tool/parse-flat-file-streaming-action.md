---
url: >-
  https://docs.workato.com/en/connectors/positional-file-tool/parse-flat-file-streaming-action.md
description: >-
  The Parse flat file (streaming) action parses large positional flat files in
  chunks in Positional file tool.
---

# Positional file tool - Parse flat file (streaming) action

The **Parse flat file (streaming)** action parses large positional flat files in chunks in Positional file tool.

## Input

| Input field | Description |
| --- | --- |
| File content | Enter file content datapills from a connector. |
| Chunk size (MB) | Select the chunk size, in MB, to stream. |
| Merge file storage output? | Select `Yes` or `No` to decide to merge all schemas with the flat file output into a single file. |
| Output format | Select the format of the output. Options are `CSV` or `JSON`. |
| Record position validations | Optional. Enter a record you expect to appear at a selected line or line range. Each record entry includes an `Identifier value` and a `Line / range`. Enable `Strict match` to require every line in a range to match, instead of one line. The action fails if a validation isn't met. Blank lines aren't counted, and validation is skipped if left empty. |
| Schemas | Fields to define columns for the schema. Schema fields include `Schema name`, `Identifier start position`, `Identifier length`, `Identifier value`, `Output destination`, `Upload URL`, and `Column specification`. |

## Output

| Output field | Description |
| --- | --- |
| Total lines processed | The total number of lines processed in the response flat file. |
| Total chunks processed | The total number of chunks processed in the streaming flat file. |
| Status | The status of the flat file response. |
