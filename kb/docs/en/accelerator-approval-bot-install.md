---
url: 'https://docs.workato.com/en/accelerator-approval-bot-install.md'
description: >-
  Install the Approval bot accelerator package in your Workato workspace for
  Slack or Microsoft Teams, including prerequisites and setup.
---

# Install the Approval bot accelerator

## Prerequisites

- A Workato account with the Enterprise bot feature.
- Microsoft Teams account with the workbot app installed (for use with Microsoft teams)
- A Slack workspace (for use with Slack)
- The `Core-ApprovalBot-Slack-V001.zip` or `Approval-bot-MSTeams.zip` package.

* * *

## Install the package

To install the package into your workspace:

1. In Workato, create a new project. Name the project **Approval Bot**.
   
2. Within the newly-created **Approval Bot** project, create a new folder. Name the folder **Slack** or **Microsoft Teams**.
   
3. If you plan to implement the Approval bot in Slack, import the package `Core-ApprovalBot-Slack-V001.zip` using the [Recipe Lifecycle Management](/en/recipe-development-lifecycle/import) tool or with the [Import package into a folder API.](/en/workato-api/recipe-lifecycle-management#import-package-into-a-folder)
   
   If you plan to implement the Approval bot in Microsoft Teams, import the package `Approval-bot-MSTeams.zip` using the same tools.

---
