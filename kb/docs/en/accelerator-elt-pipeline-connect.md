---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-connect.md'
description: >-
  Reference for the connections in the ELT Pipeline for Snowflake accelerator,
  including Snowflake, SQL Server, S3, and Workbot connections.
---

# ELT Pipeline for Snowflake accelerator connections

The ELT Pipeline for Snowflake accelerator has eight connections that are common to both Slack and Microsoft Teams implementations:

- [ELT | CON | Snowflake through JDBC](#snowflake-jdbc)
- [ELT | CON | Snowflake](#snowflake)
- [ELT | CON | SQL Server through JDBC](#sql-jdbc)
- [ELT | CON | SQL Server](#sql)
- [ELT | CON | SF Partner Account](#sf-partner)
- [ELT | CON | S3](#s3)
- [ELT | CON | PostgreSQL through JDBC](#postgresql-jdbc)
- [ELT | CON | On-prem-Files](#on-prem-files)

In addition, this accelerator has two connections that are unique to either Slack or Microsoft Teams:

- [ELT | CON | Workbot for ELT Accelerator](#slack-connect)
- [ELT | CON | ELT Workbot for Microsoft Teams](#teams-connect)

## **ELT | CON | Snowflake through JDBC**

Complete this connection using our [JDBC connector](/en/connectors/jdbc#jdbc) documentation.

## **ELT | CON | Snowflake**

Complete this connection using our [Snowflake connection setup](/en/connectors/snowflake#snowflake) documentation.

- Choose an authentication type.
- Select `UTC` timezone.

## **ELT | CON | SQL Server through JDBC**

Complete the connection using our [JDBC connector](/en/connectors/jdbc#jdbc) documentation.

## **ELT | CON | SQL Server**

Complete this connection using our [SQL server](/en/connectors/mssql) documentation.

## **ELT | CON | SF Partner Account**

Complete this connection using our [Salesforce connector](/en/connectors/salesforce#how-to-connect-to-salesforce-on-workato) documentation.

## **ELT | CON | S3**

Complete this connection using our [Amazon S3 connector](/en/connectors/s3#connection-setup) documentation.

## **ELT | CON | PostgreSQL through JDBC**

Complete this connection using our [JDBC connector](/en/connectors/jdbc#jdbc) documentation.

- [Download the Postgres JDBC drivers for OPA](https://jdbc.postgresql.org/download/) based on your database/server configuration.

## **ELT | CON | On-prem-Files**

Complete this connection using our [On-prem files connector](/en/connectors/on-prem-files#how-to-connect-to-on-prem-files-on-workato) documentation.

## **ELT | CON | Workbot for ELT Accelerator**

Complete this connection using our [Workbot for Slack](/en/workbot/workbot-for-slack-setup#_3-create-a-workbot-for-slack-connection) documentation.

This connection is only required if you plan to implement the ELT Pipeline bot in Slack.

## **ELT | CON | ELT Workbot for Microsoft Teams**

Complete this connection using our [Workbot for Microsoft Teams](/en/workbot-for-teams/getting-started) documentation.

This connection is only required if you plan to implement the ELT Pipeline bot in Microsoft Teams.

---
