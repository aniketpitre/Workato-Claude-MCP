---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/fetch-extract-output.md
description: >-
  The Fetch extract output action retrieves the archived XML output produced by
  an extract process.
---

# Oracle Fusion Cloud - Fetch extract output action

The **Fetch extract output** action retrieves the archived XML output produced by an extract process.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Instance name | Enter the name of the archived flow instance. |
| Task name | Enter the name of the flow task. |
| Mode | Enter the name of the running mode, either `ARCHIVER` or `FLOW`. If mode is `ARCHIVER`, the output is returned based on flow instance name. If mode is `FLOW`, the output is returned based on flow instance name and flow task name. |
| Output fields | Define the schema for the expected output data structure using the schema designer. |

## Output

| Output field | Description |
| --- | --- |
| Result | The XML output. |
