---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-start.md'
description: >-
  Add the ELT Bot to your notification channel and start the accelerator recipes
  in the correct folder order to run your ELT pipelines.
---

# Start

Before you begin, ensure you have completed the following tasks:

- [Install the asset package](/en/accelerator-elt-pipeline-install)
- [Connect your applications](/en/accelerator-elt-pipeline-connect)
- [Set up your lookup tables](/en/accelerator-elt-pipeline-configure#lookup-tables)
- [Set up your OPA and OPG](/en/accelerator-elt-pipeline-configure#opa-opg-setup)
- [Set up your custom OAuth profile](/en/accelerator-elt-pipeline-configure#oauth-setup)

## Add the ELT Bot to the notification channel

You must add the ELT Pipeline Workbot you created in [Setting up a Custom OAuth Profile for Workbot](#oauth-setup) to the Slack notification channel you configured in the account properties. To add the ELT Pipeline Workbot to the channel, mention the bot in the channel with `@bot-name`.

* * *

## Start recipes

You must start the recipes in this accelerator in a specific order. This order depends on the recipes' parent folder. Start all recipes in each folder before proceeding to the next folder. The folder order is as follows:

1. 04 Functions
2. 03 Data Load
3. 01 UI
4. 02 Controller

---
