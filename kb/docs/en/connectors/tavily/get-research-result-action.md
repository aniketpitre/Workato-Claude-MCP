---
url: 'https://docs.workato.com/en/connectors/tavily/get-research-result-action.md'
description: >-
  The Get research result action retrieves the status and result of a research
  task by its request ID.
---

# Tavily - Get research result action

The **Get research result** action retrieves the status and result of a research task from Tavily by its request ID. This action returns only the status while the task is pending or in progress.

## Input

| Input field | Description |
| --- | --- |
| Request ID | Enter the research task ID returned by the [Run deep research](/en/connectors/tavily/run-deep-research-action) action. |
| Output schema | Enter the JSON schema you plan to use. This schema isn't sent to Tavily. |

## Output

| Output field | Description |
| --- | --- |
| Request ID | The unique identifier for this research task. |
| Created at | The date and time the research task was created. |
| Status | The status of the research task, for example `pending`, `in progress`, `completed`, or `failed`. |
| Content | The completed research report, as plain text by default. If **Output schema** was set on input, this field is shaped as an object matching that schema instead. |
| Sources | The sources used in the report. Each source includes a title, URL, and favicon. |
| Response time | The time Tavily took to process the request, in seconds. |

---
