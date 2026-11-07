---
url: 'https://docs.workato.com/en/connectors/gong/search-call-transcripts.md'
description: >-
  The Search call transcripts action in the Gong connector lists transcripts of
  calls within a specified date range and matching specific call IDs.
---

# Gong - Search call transcripts action

This action will search call transcripts in Gong. Lists the transcripts of calls that took place during a specified date range and have specified call IDs.

## Input

| Field | Description |
| --- | --- |
| Starting date-time | The date from which to list calls. If not specified, the calls start with the earliest recorded call. The date applies to call start time. |
| Ending date-time | The date until which to list calls. For web-conference calls recorded by Gong, the date denotes its scheduled time, otherwise, it denotes its actual start time. |
| Call IDs | List of calls IDs to be filtered. If not supplied, returns all calls between Starting date time and Ending date time. To retrieve a single call, provide the ID of the call. |
| Workspace | Select the workspace to filter calls by. |

## Output

| Field | Description |
| --- | --- |
| Call Transcripts _A list of following details for each call transcript_ | Call ID | An index for each item in the list of users aggregate activity. |
| Transcript | A list containing a transcript object. Each transcript object contains within it details like speaker ID, Topic, and a list of Sentences. Each sentence object contains the start, end, and text fields. |
| List Size | The list size of the call transcripts. |
| List Index | An index for each item in the list of call transcripts. |
| Records _Metadata of the response_ | Current page number | Necessary for repeat requests to ensure pagination. |
| Current page size | Number of records on the current page. |
| Cursor | UUID necessary for pagination. |
| Total Records | Total number of records that can be queried. |

---
