---
url: >-
  https://docs.workato.com/en/connectors/qualtrics/new-survey-response-trigger.md
description: >-
  Monitor for new survey responses in real time using Qualtrics webhooks.
  Triggers immediately when a respondent completes a survey.
---

# Qualtrics - New survey response trigger

The **New survey response** trigger monitors for new survey responses in real time using Qualtrics webhooks. When a respondent completes a survey, the trigger fires immediately and provides response information.

## Input

| Input field | Description |
| --- | --- |
| Survey | Select the survey to monitor from the drop-down menu, or toggle to provide a custom Survey ID. |

## Output

| Output field | Description |
| --- | --- |
| Topic | The webhook topic that triggered the event, identifying the survey and event type. |
| Status | The completion status of the survey response. For example, `Complete`. |
| Survey ID | The unique identifier of the survey. |
| Response ID | The unique identifier of the response. Use this ID with the **Get response details** action to retrieve complete response data. |
| Recipient ID | The identifier of the recipient who completed the survey. |
| Response event context | Additional context information about the response event. |
| Distribution ID | The identifier of the distribution through which the survey was sent. |
| Completed date | The date and time when the survey response was completed. |
| Brand ID | The identifier of the Qualtrics brand associated with the survey. |
