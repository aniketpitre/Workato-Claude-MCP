---
url: >-
  https://docs.workato.com/en/connectors/talent-palette/check-job-status-action.md
description: >-
  The Check job status action checks the status of bulk import jobs in Talent
  Palette.
---

# Talent Palette - Check job status action

The **Check job status** action checks the status of bulk import jobs in Talent Palette.

## Input

| Input field | Description |
| --- | --- |
| Job ID | Provide the Talent Palette ID of the registered job. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the current job in Talent Palette. |
| Registered date | The date and time the job was registered (JST). |
| Error | The error object, if the `Status` is `error`. |
| Retry Job ID | The Talent Palette ID of the retry job, if a 500 error occurred. |
