---
url: 'https://docs.workato.com/en/connectors/tavily/run-deep-research-action.md'
description: >-
  The Run deep research action submits a research question to Tavily and returns
  a completed report with sources.
---

# Tavily - Run deep research action

The **Run deep research** action submits a research question to Tavily and returns a report with sources. This action can take several minutes to complete.

## Input

| Input field | Description |
| --- | --- |
| Research question | Enter the research task or question you plan to investigate. |
| Model | Select the research model you plan to use. **Mini** is fast and targeted. **Pro** is comprehensive. Defaults to **Mini**. |
| Include domains | Enter a soft preference for source domains. Maximum is `20`. Matching a domain also includes its subdomains. |
| Exclude domains | Enter a hard blocklist of source domains. Maximum is `20`. |
| Files | Attach up to 5 extra files to use as sources. Accepted formats include `.txt`, `.md`, `.json`. Maximum is `80,000` words combined. Each file requires a file name and base64-encoded data. |

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
