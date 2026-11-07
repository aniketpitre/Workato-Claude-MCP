---
url: 'https://docs.workato.com/en/connectors/aws-inspector-2/new-findings-trigger.md'
description: The New Findings trigger monitors AWS Inspector2 for new findings.
---

# AWS Inspector2 - New findings trigger

The **New findings** trigger monitors AWS Inspector2 for new findings.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for new events. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| AWS account ID | The AWS account where the finding was generated. |
| Description | A brief explanation of the finding. |
| Finding ARN | The unique Amazon Resource Name (ARN) identifies the finding. |
| First observed at | The first time this finding was observed. |
| Last observed at | The most recent time this finding was observed. |
| Remediation | Guidance to remediate the issue. |
| Resources | The list of affected AWS resources. |
| Severity | The level of risk, for example: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`. |
| Status | The current state of the finding, for example: `ACTIVE`, `CLOSED`. |
| Type | The category of finding, for example: `PACKAGE_VULNERABILITY`. |
| Code vulnerability details | Information about vulnerabilities in custom application code. |
| EPSS score | The Exploit Prediction Scoring System (EPSS) scores predict the likelihood of the vulnerability being exploited. |
| Exploitability details | Data on how exploitable the vulnerability is. |
| Exploit available | Indicates whether a public exploit is available (`YES` or `NO`). |
| Fix available | Indicates whether a fix is available for the finding (`YES` or `NO`). |
| Inspector score | The severity score assigned by AWS Inspector. |
| Inspector score details | Details on how the inspector's score was derived. |
| Network reachability details | Information about external network accessibility. |
| Package vulnerability details | Data about vulnerabilities in software packages. |
| Title | A title summarizing the finding. |
| Updated at | The last time the finding was updated. |

---
