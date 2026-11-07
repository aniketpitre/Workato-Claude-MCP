---
url: >-
  https://docs.workato.com/en/connectors/positional-file-tool/trim-csv-file-streaming-action.md
description: >-
  The Trim CSV file (streaming) action streams a large delimited file in chunks
  and splits it into row-range sections, such as header, detail, and trailer
  rows.
---

# Positional file tool - Trim CSV file (streaming) action

The **Trim CSV file (streaming)** action streams a large delimited file in chunks and splits it into row-range sections, such as header, detail, and trailer rows.

## Input

| Input field | Description |
| --- | --- |
| File content | Enter file content datapills from a connector. |
| Chunk size (MB) | Select the chunk size, in MB, to stream. |
| Schemas | Enter fields to define one or more row-range sections of the file. Schema fields include `Schema name`, `Start row`, `End row`, `Delimiter`, `Output destination`, and `Upload URL`. |
| Column names | Define column names for a schema's action output. Optionally, set a `Default value` per column. When a row is missing a value for that column (blank or absent), the default value is used instead. Applies to action output and CSV file output, though defaults on CSV output only apply when the delimiter is a comma. |

## Output

| Output field | Description |
| --- | --- |
| Total lines processed | The total number of lines processed in the response file. |
| Total chunks processed | The total number of chunks processed while streaming the file. |
| Status | The status of the file response. |
