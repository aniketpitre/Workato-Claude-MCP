---
url: 'https://docs.workato.com/en/accelerator-approval-bot-assets.md'
description: >-
  Reference for the Approval bot accelerator asset packages for Microsoft Teams
  and Slack, including recipes, lookup tables, and connections.
---

# Approvals bot assets

This accelerator's assets include the following files and their components:

- [approval-bot-msteams.zip](#bot-teams) is the core asset package that you import into your Workato workspace to implement the Approval bot in Microsoft Teams.
- [approval-bot-slack.zip](#bot-slack) is the core asset package that you import into your Workato workspace to implement the Approval bot in Slack.

* * *

## approval-bot-msteams.zip

You must install this core asset package into your workspace to implement the Approval bot in Microsoft Teams.

This package includes the following components:

- 7 recipes
  - 5 Workbot action recipes (commands to the workbot for Microsoft Teams)
  - 1 custom schedule recipe
  - 1 callable recipe
- 1 lookup table
  - approval\_bot\_teams.lookup\_table.json
- 2 Connections
  - ABT | CON-001 | Microsoft Teams
  - ABT | CON-002 | Google Sheets
- 1 common data model
  - Microsoft Teams Adaptive Cards Structure

* * *

## approval-bot-slack.zip

You must install this core asset package into your workspace to implement the Approval bot in Slack.

This package includes the following components:

- 6 recipes
  - 2 callable recipes
  - 4 standard recipes
- 1 lookup table
  - approval\_bot\_slack.lookup\_table.json
- 2 connections
  - ABS | CON-001 | Slack
  - ABS | CON-002 | Google Sheets

---
