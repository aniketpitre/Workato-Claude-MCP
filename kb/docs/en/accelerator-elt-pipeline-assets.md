---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-assets.md'
description: >-
  Reference for the ELT Pipeline for Snowflake accelerator assets, including
  recipe packages, lookup tables, and properties.
---

# ELT Pipeline for Snowflake accelerator - Assets

## Installation files

This accelerator's assets include the following files, and their components:

- [ELT\_Pipeline\_for\_MS\_Teams.zip](#teams-package) is the core asset package you must import if you plan to implement the ELT Pipeline bot in Microsoft Teams.
- [ELT\_Pipeline\_for\_Slack.zip](#slack-package) is the core asset package you must import if you plan to implement the ELT Pipeline bot in Slack.

### ELT\_Pipeline\_for\_MS\_Teams.zip

You must import this core asset package to implement the ELT Pipeline bot in Microsoft Teams.

This package contains the following components:

- 13 Recipes
  
  - 3 active
  - 10 callable
- 7 Lookup tables
  
  - ELT | User Access
  - ELT | Systems
  - ELT | Objects
  - ELT | JOB TABLE
  - ELT | ERROR LOGS
  - ELT | CONTROL TABLE | MAIN
  - ELT | CONTROL TABLE | CHILD
- 10 Properties
  
  - elt.user\_section\_text
  - elt.user\_button1\_url
  - elt.user\_button1\_label
  - elt.snowflake\_url
  - elt.msteams\_notification\_channel
  - elt.s3bucketregion
  - elt.s3bucketname
  - elt.bot\_app\_id
  - elt.aws\_secret\_key
  - elt.aws\_key\_id
  - elt.admin\_guide
- 9 Connections
  
  - ELT | CON | Snowflake through JDBC
  - ELT | CON | Snowflake
  - ELT | CON | SQL Server through JDBC
  - ELT | CON | SQL Server
  - ELT | CON | SF Partner Account
  - ELT | CON | S3
  - ELT | CON | PostgreSQL through JDBC
  - ELT | CON | On-prem-File
  - ELT | CON | ELT Workbot for Microsoft Teams

### ELT\_Pipeline\_for\_Slack.zip

You must import this core asset package to implement the ELT Pipeline bot in Slack.

This package contains the following components:

- 13 Recipes
  
  - 3 active
  - 10 callable
- 7 Lookup tables
  
  - ELT | User Access
  - ELT | Systems
  - ELT | Objects
  - ELT | JOB TABLE
  - ELT | ERROR LOGS
  - ELT | CONTROL TABLE | MAIN
  - ELT | CONTROL TABLE | CHILD
- 10 Properties
  
  - elt.user\_section\_text
  - elt.user\_button1\_url
  - elt.user\_button1\_label
  - elt.snowflake\_url
  - elt.slack\_notification\_channel
  - elt.s3bucketregion
  - elt.s3bucketname
  - elt.bot\_app\_id
  - elt.aws\_secret\_key
  - elt.aws\_key\_id
  - elt.admin\_guide
- 9 Connections
  
  - ELT | CON | Snowflake through JDBC
  - ELT | CON | Snowflake
  - ELT | CON | SQL Server through JDBC
  - ELT | CON | SQL Server
  - ELT | CON | SF Partner Account
  - ELT | CON | S3
  - ELT | CON | PostgreSQL through JDBC
  - ELT | CON | On-prem-File
  - ELT | CON | ELT Workbot for Slack

---
