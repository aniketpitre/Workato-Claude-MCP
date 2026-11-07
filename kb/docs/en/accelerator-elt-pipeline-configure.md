---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-configure.md'
description: >-
  Configure the ELT Pipeline for Snowflake accelerator by setting up lookup
  tables, a custom OAuth profile, and an OPA and OPG.
---

# Configure the ELT Pipeline for Snowflake accelerator

Before you start this accelerator, you must configure your [lookup tables](#lookup-tables), [custom OAuth profile](#oauth-setup), and an [OPA and OPG](#opa-opg-setup).

## Set up your lookup tables

You must set up the [ELT | User Access lookup table](#user-access-table) and [ELT | System Access lookup table](#system-access-table) before starting the accelerator.

## Set up the **ELT | User Access** lookup table

1. Navigate to **Tools > Lookup tables**.
   
2. Select **ELT | User Access** from the list of available lookup tables.
   
3. Add a user to your lookup table. Assign them to an Admin role.
   
   ![Add user to lookup table](/assets/elt-lookup-table-edit.DKWm42bM.png)
   

* * *

## Set up the **ELT | Systems** lookup table

Workato preconfigures the **ELT | Systems** lookup table with four sources:

- Salesforce
- SQL Server
- PostgreSQL
- On-prem files

If you don't need to use some of these sources, you can remove them by editing this lookup table.

1. Navigate to **Tools > Lookup tables**.
   
2. Select **ELT | System Access** from the list of available lookup tables.
   
3. Edit or remove sources, as necessary.
   
   ![Edit lookup table](/assets/system-lookup-table.DUqn0JVo.png)
   

* * *

## Set up an OPA and OPG

See our [On-prem connectivity](/en/on-prem) documentation for instructions on setting up your on-prem agent (OPA) and on-prem group (OPG).

When setting up an OPA, you must create a [connection profile](/en/on-prem/agents/connection/profile#connection-profiles) for each application. The application profile uniquely identifies each application and contains the configuration information required to connect. See the [ELT pipeline accelerator connections](/en/accelerator-elt-pipeline-connect) documentation for a list of profiles you must create.

* * *

## Set up a Custom OAuth Profile for Workbot

The ELT Pipeline Workbot requires a Custom OAuth profile. Create the profile before connecting to Slack or Microsoft Teams. See our [Setting up a Slack Enterprise Workbot](/en/workbot/workbot-custom-bots) or [Setting up an Microsoft Teams Workbot](/en/workbot-for-teams/guides/creating-enterprise-workbot) documentation for instructions.

* * *

---
