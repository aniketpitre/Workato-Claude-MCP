---
url: 'https://docs.workato.com/en/connectors/gong/search-calls.md'
description: >-
  The Search calls action in the Gong connector lists detailed call data for
  calls that match a date range, specific call IDs, or both.
---

# Gong - Search calls action

The **Search calls** action lists detailed call data from Gong for calls that match a date range, specific call IDs, or both.

## Input

| Input field | Description |
| --- | --- |
| Starting date time | Enter the date from which to list calls. Leave blank to start with the earliest recorded call. The date applies to call start time. |
| Ending date time | Enter the date until which to list calls. The date denotes the scheduled time for web-conference calls recorded by Gong, and the actual start time for all other calls. |
| Call IDs | Enter a list of call IDs to filter by. Leave blank to return all calls between Starting date time and Ending date time. Provide a single ID to retrieve one call. |
| Workspace | Select the workspace to filter calls by. |
| Timezone | Select the timezone whose offset replaces the offset on Starting date time and Ending date time. The date and time values stay the same. |
| Cursor | Provide the cursor value from the previous API call to fetch the next page of records. |

## Output

The action returns call-specific output fields, which vary based on the calls it finds. The table lists the output fields.

| Output field | Description |
| --- | --- |
| Calls | List of the following details for each call. |
| Collaboration (Calls) | An object containing a list of public comments. Each public comment contains details like audio start time, audio end time, comment user ID, and the comment text, among other fields. |
| Content (Calls) | An object with the information pertaining to structure, topic, trackers, and points of interest. |
| Context (Calls) | List of objects that contains the relevant fields, object ID, object type, as well as source system details. |
| Interaction (Calls) | An object with the information pertaining to interaction stats, questions, speakers, and video. |
| Media (Calls) | An object containing the video and audio URL of the call, as applicable. |
| Metadata (Calls) | Contains the metadata of the call, such as title, duration, and workspace. |
| Parties (Calls) | List of parties that were involved in the call. Each party object contains details such as name, email address, and affiliation. |
| List size (Calls) | Number of calls in the list. |
| List index (Calls) | Index of each call in the list. |
| Records | Metadata of the response. |
| Current page number (Records) | Necessary for repeat requests to ensure pagination. |
| Current page size (Records) | Number of records on the current page. |
| Cursor (Records) | UUID necessary for pagination. |
| Total records (Records) | Total number of records that can be queried. |
| Request ID | Unique ID that Gong generates for the request. Use it for troubleshooting. |

---
