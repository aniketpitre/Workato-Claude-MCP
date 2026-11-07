---
url: >-
  https://docs.workato.com/en/connectors/qualtrics/get-response-details-action.md
description: Retrieve the complete details of a survey response using its response ID.
---

# Qualtrics - Get response details action

Use the **Get response details** action to retrieve the complete details of a survey response through its response ID.

## Input

| Input field | Description |
| --- | --- |
| Survey | Select the survey from the drop-down list, or toggle to provide a custom Survey ID. |
| Response ID | Provide the unique identifier of the response to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Response ID | The unique identifier of the survey response. |
| Values | An object containing all response values. |
| Start date (Values) | When the respondent started the survey. |
| End date (Values) | When the respondent completed the survey. |
| Status (Values) | The completion status code. |
| IP address (Values) | The respondent's IP address. |
| Progress (Values) | Completion percentage (0-100). |
| Duration (Values) | Time spent on the survey in seconds. |
| Finished (Values) | Whether the survey was completed (1 for finished, 0 for unfinished). |
| Recorded date (Values) | When the response was recorded. |
| Location latitude (Values) | Geographic latitude of the respondent. |
| Location longitude (Values) | Geographic longitude of the respondent. |
| Distribution channel (Values) | How the survey was distributed. |
| User language (Values) | The respondent's language. |
| Question responses (Values) | Values for each question in the survey. |
| Labels | An object containing human-readable labels for response values. |
| Displayed fields | An array of field names that were displayed to the respondent. |
| Displayed values | An object containing the displayed values for fields. |
