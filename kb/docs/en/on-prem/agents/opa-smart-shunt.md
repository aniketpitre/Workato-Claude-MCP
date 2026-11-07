---
url: 'https://docs.workato.com/en/on-prem/agents/opa-smart-shunt.md'
description: >-
  Learn how OPA Smart Shunt moves data directly between on-premise systems to
  stay compliant and avoid network latency and transfer quotas.
---

# OPA Smart Shunt

OPA Smart Shunt allows users to send data directly from the source system to its destination entirely on-premise.

![Smart Shunt for on-prem database extracts](/assets/opa_smartshunt.BTMYVJ7D.png)_Smart Shunt for on-prem database extracts_

### OPA Smart Shunt for compliance

The direct "ground-to-ground" integration means that your secure data doesn't leave the data center. This allows your team to remain compliant with your company's security requirements while using Workato to move data between on-premise systems.

### OPA Smart Shunt for increased performance

Additional, OPA Smart Shunt optimizes for high volume and high speed data transfer. When a workflow extracts and loads data entirely on-premise, it allows the workflow to avoid network latency and bypass file transfer size quotas.

## How to use OPA Smart Shunt

For each [on-premise database](#what-databases-support-opa-smart-shunt) connector, there is the **Export query result** action.

![Generic export query result action](/assets/generic-export-query-result-action.016jHnJ-.png)_Selected Database connectors have the Export Query Result action_

This action instructs the on-prem agent to query a local database and export the results as a CSV file. This CSV file is then streamed to an on-premise file storage.

> **GOT A STAGING ENVIRONMENT?**
> 
> Learn how to set up a staging area in your [OPA configuration file](/en/on-prem/agents/connection/profile#server-profile).

Subsequently, the CSV file can be loaded to a downstream data warehouse.

In this [example recipe](https://app.workato.com/recipes/1515656?st=78d12b), the OPA exports the results from an on-premise PostgreSQL database as a CSV file and uploads it to a local file storage.

## What databases support OPA Smart Shunt

OPA Smart Shunt is support on all databases that have Java Database Connectivity (JDBC) drivers. The databases that support OPA Smart Shunt include:

- [JDBC](/en/connectors/jdbc/export-query-result)
- [PostgreSQL](/en/connectors/postgresql/export-query-result)
- [SQL Server](/en/connectors/mssql/export-query-result)
- [MySQL](/en/connectors/mysql/export-query-result)
- [Oracle](/en/connectors/oracle/export-query-result)
- [IBM Db2](/en/connectors/ibm-db2/export-query-result)

## How to configure the export query result action

Read up on how to configure the **Export query result** action for each connector:

- [JDBC: Export query result](/en/connectors/jdbc/export-query-result#export-query-result)
- [PostgreSQL: Export query result](/en/connectors/postgresql/export-query-result#export-query-result)
- [SQL Server: Export query result](/en/connectors/mssql/export-query-result#export-query-result-action)
- [MySQL: Export query result](/en/connectors/mysql/export-query-result#export-query-result)
- [Oracle: Export query result](/en/connectors/oracle/export-query-result#export-query-result)

## How to enable OPA Smart Shunt

The OPA Smart Shunt feature is available to customers on specific pricing plans. To use this feature, you must have the OPA and ETL/ELT capabilities included in your plan. Refer to your pricing plan and contract to learn more.

---
