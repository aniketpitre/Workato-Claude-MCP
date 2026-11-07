---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-install.md'
description: >-
  Install the ELT Pipeline for Snowflake accelerator, including prerequisites,
  asset package setup, and required Snowflake, S3, and OPA instances.
---

# Install the ELT Pipeline for Snowflake accelerator

We recommend you install the accelerator in a development, testing, or production environment. Make changes to naming conventions as necessary to suit your needs.

* * *

## Prerequisites

- You must have a Workato subscription.
  
- You must have the following Workato capabilities and features:
  
  - ELT/ETL
  - Enterprise workbot for Slack/Microsoft Teams
- You must have one of the following packages:
  
  - ELT Pipeline for Slack.zip (for Slack implementations)
  - ELT Pipeline for Teams.zip (for Microsoft Teams implementations)
- You must have the following instances:
  
  - Snowflake
  - A Salesforce/ SQL/ Windows File System instance
  - An S3 bucket for staging data
  - A Slack/Microsoft Teams workspace
- 2 OPAs (On-prem agents)
  
- 1 OPG (On-prem group)
  

* * *

## Install the asset package

To install the package into your workspace:

1. In Workato, create a new project. Depending on where you plan to implement the ELT Pipeline bot, name the project **ELT Pipeline for Snowflake** or **ELT Pipeline for Microsoft Teams**.
   
2. Within the newly-created **ELT Pipeline for Snowflake** project, create a new folder. Name the folder **Slack** or **Microsoft Teams**.
   
3. Import the package **ELT Pipeline for Slack.zip** or **ELT\_Pipeline\_for\_MS\_Teams.zip** using the [Recipe Lifecycle Management](/en/recipe-development-lifecycle/import) tool or with the [Import package into a folder API.](/en/workato-api/recipe-lifecycle-management#import-package-into-a-folder)
   

* * *

---
