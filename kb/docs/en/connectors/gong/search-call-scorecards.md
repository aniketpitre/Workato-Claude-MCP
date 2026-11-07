---
url: 'https://docs.workato.com/en/connectors/gong/search-call-scorecards.md'
description: >-
  The Search call scorecards action in the Gong connector retrieves scorecard
  answers by call date, review date, scorecard, or reviewed user.
---

# Gong - Search call scorecards action

This action will search call scorecards in Gong. Retrieves all the answers for the scorecards that were reviewed during a specified date range, for calls that took place during a specified date range, for specific scorecards or for specific reviewed users.

## Input

| Field | Description |
| --- | --- |
| Call start date | The date of the call from when to list calls. This value is inclusive. |
| Call end date | The date of the call until when to list calls. This value is exclusive. |
| Review start date | The review date from when to list calls. This value is inclusive. |
| Review end date | The review date until when to list calls. This value is exclusive. |
| Reviewed user IDs | List of users to be filtered. If not supplied, all users are returned. |

## Output

| Field | Description |
| --- | --- |
| Answered Scorecards _A list of following details for each scorecard_ | Visibility type | The aggregate details of a single user is contained within this list object. |
| Answered scorecard ID | Email address of the user whose information is at the corresponding index. |
| Scorecard ID | Gong User ID for the specific user. |
| Scorecard name | The list size of the users aggregate activity. |
| Answers | A list containing a series of answer objects. Each answer object contains within it details like question text, score, answer text, among others. |
| Call ID | ID of call for which this scorecard corresponds to. |
| Call start time | Start time of the call. |
| Reviewed user ID | ID of the user who was evaluated in this call. |
| Reviewer user ID | ID of the user who was reviewing this call. |
| Review time | Time when the review took place. |
| List Size | The list size of the call scorecards. |
| List Index | An index for each item in the list of call scorecards. |
| Records _Metadata of the response_ | Current page number | Necessary for repeat requests to ensure pagination. |
| Current page size | Number of records on the current page. |
| Cursor | UUID necessary for pagination. |
| Total Records | Total number of records that can be queried. |

---
