---
url: 'https://docs.workato.com/en/connectors/youtube/search-records-action.md'
description: >-
  The Search records action searches for videos or comments matching the
  criteria you specify in YouTube.
---

# YouTube - Search records action

The **Search records** action searches for videos or comments matching the criteria you specify in YouTube.

> **PREREQUISITES**
> 
> Searching comments requires OAuth 2.0 authentication with a scope that includes **Force SSL (secure access)** (`youtube.force-ssl`). A read-only scope isn't sufficient.

## Input

Input fields are dynamically generated based on the object you select. The following fields are common to all object types:

| Field | Description |
| --- | --- |
| Object type | Select the type of YouTube object to search for. Options are **Videos** or **Comments**. |
| Max results | Enter the maximum number of results to return. Valid values are 1-50. Default is 25 for comments and 5 for videos. |
| Page token | Enter the token for retrieving a specific page of results. |

## Output

Output fields are dynamically generated based on the object you select. The following fields are common to all object types:

| Field | Description |
| --- | --- |
| Kind | The API resource type, for example `youtube#commentThreadListResponse`. |
| Etag | The ETag of the resource. |
| Next page token | Token for retrieving the next page of results. |
| Prev page token | Token for retrieving the previous page of results. |
| Page info | Contains `Total results` and `Results per page`. |
| Items | An array of comment threads or search results. |

---
