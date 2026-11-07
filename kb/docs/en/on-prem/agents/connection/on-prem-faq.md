---
url: 'https://docs.workato.com/en/on-prem/agents/connection/on-prem-faq.md'
description: >-
  Answers to common questions about on-prem agent connections, cloud profiles,
  and connection profiles in Workato.
---

# On-prem FAQs

Get answers to frequently asked questions (FAQs) about:

- On-prem agent connections
- On-prem cloud connections
- On-prem profile connections

## On-prem agent connections

What is the role of an on-prem agent connection in Workato, and how does it determine where requests originate?

A [connection in Workato](/en/on-prem/agents/connection#connections-using-on-prem-agent) determines the source from which requests are executed. Direct connection requests originate from Workato servers. Connections using an on-prem agent send requests from the environment where the agent is installed.

How can I set up a connection for an on-prem agent?

You can set up a connection for an on-prem agent using two methods: Cloud profile and Connection profile. [Cloud profiles](/en/on-prem/agents/connection/cloud) allow you to configure a connection directly within Workato. [Connection profiles](/en/on-prem/agents/connection/profile) require manual configuration in the on-prem agent's config file.

How does a cloud profile simplify connection setup for on-prem agents?

A [cloud profile](/en/on-prem/agents/connection#cloud-profile) lets you set up a connection directly in Workato, similar to regular connectors. This eliminates the need to manually open and edit the config file of the on-prem agent which is required with connection profiles.

Can I connect to a database using a cloud profile or a connection profile for an on-prem agent?

Yes, all database connectors offer the option to connect through an on-prem agent using a cloud profile or a connection profile.

[Cloud profile](/en/on-prem/agents/connection#cloud-profile): You must select the on-prem group you plan to use in the connection field.

[Connection profile](/en/on-prem/agents/connection#connection-profile): You must select the on-prem group you plan to use in the connection field. Enter the on-prem connection profile name and verify that it matches the configuration in the `config.yml` file of the on-prem agent.

How can I connect to an on-prem file system?

You can [connect to an on-prem file system](/en/on-prem/agents/connection#connecting-to-on-prem-file-system-profiles-using-connection-profile) with a cloud profile or connection profile:

**Cloud profile**: You must use an on-prem agent to connect to an on-prem file system. You must select the relevant on-prem group in the connection fields and provide the necessary properties for the on-prem file system.

**Connection profile**: You must select the relevant on-prem group and enter the on-prem connection profile name. This name must match the configuration in the **files** section of the `config.yml` file of the on-prem agent.

What is a connection profile, and how does it differ from a cloud profile?

A [connection profile](/en/on-prem/agents/connection#connection-profile) requires you to manually fill in the connection details in the configuration file of the on-prem agent. Cloud profiles provide direct setup in Workato.

Why am I receiving a Snowflake JDBC driver internal error?

Error:

```
JDBC driver internal error: exception creating result java.lang.ExceptionInInitializerError at net.snowflake.client.jdbc.internal.apache.arrow.memory.ArrowBuf.getDirectBuffer(ArrowBuf.java:231).: XX000
```

If you receive the preceding [Snowflake](/en/connectors/snowflake#snowflake) error when you execute a select query while using a custom SQL action, you can resolve it using one of the following methods:

- Add `&JDBC_QUERY_RESULT_FORMAT=JSON` to the connection URL (recommended)
- Use an older Snowflake JDBC driver version, for example 3.9.2

Why am I encountering a JDBC Connection error to Databricks?

Error:

```
java.lang.ExceptionInInitializerError: Exception java.lang.RuntimeException: Failed to initialize MemoryUtil. [in thread "pool-21-thread-1"]
```

This error may occur due to the driver's use of Apache Arrow for data transfer. To resolve this error, disable Apache Arrow by adding `EnableArrow=0` to your JDBC URL:

```
jdbc:spark://host.cloud.databricks.com:443/default;EnableArrow=0;
```

This parameter change bypasses the initialization error and allows for a successful connection.

## On-prem cloud connections

What's a cloud profile in Workato?

A [cloud profile](/en/on-prem/agents/connection/cloud#cloud-profiles) is a new way of configuring connections for on-prem agents (OPA) in Workato, introduced in OPA version 2.15.0. It allows you to set up on-prem connections directly within the Workato platform, eliminating the need to edit the local on-prem agent configuration file.

What types of systems can I connect to using cloud profiles?

Cloud profiles support various [system types](/en/on-prem/agents/connection/cloud#system-types), including:

- Databases
- On-prem file systems
- SAP
- Java messaging service
- Apache Kafka
- Active Directory
- Command-line scripts

How do I apply a new configuration using cloud profiles?

When you [create a new connection](/en/on-prem/agents/connection/cloud#applying-a-new-configuration) using a cloud profile, the details are automatically propagated to all agents within the specific on-prem group. This process usually happens almost immediately, but in some cases it might take more time for an agent to receive updated connection details.

What are the properties of a database cloud connection profile?

A database cloud connection profile can contain several [properties](/en/on-prem/agents/connection/cloud#profile-properties), including:

- Name
- URL/Host
- Port
- Database Name
- Username
- Password
- SSL Configuration (optional)

Which databases are supported by OPA's database cloud profiles, and what are their default ports?

OPA's database cloud profiles support the following [databases](/en/on-prem/agents/connection/cloud#supported-databases):

- Amazon Redshift: default port: 5439
- JDBC-compatible databases:
  - Microsoft SQL Server: default port: 1433
  - MySQL: default port: 3306
  - Oracle: default port: 1521
  - PostgreSQL: default port: 5432

What are the connection types supported by the SAP connector, and what are the default ports used?

The [SAP connector](/en/on-prem/agents/connection/cloud#sap-profile) supports two connection types:

- Direct connections
- Message Server connections

Default ports used by SAP depend on the connection type and configuration. Refer to the [SAP cloud profile documentation](/en/on-prem/agents/connection/cloud#sap-profile) for more information on default ports.

Which JMS providers are supported by the cloud profile on-prem agent?

The cloud profile on-prem agent supports the following [JMS providers](/en/on-prem/agents/connection/cloud#jms-profile):

- Amazon Simple Queue Service
- Apache ActiveMQ
- Azure Service Bus

What configuration properties are required when connecting to Amazon SQS using the cloud profile?

To connect to [Amazon SQS](/en/on-prem/agents/connection/cloud#amazon-sqs) using the cloud profile, you must configure the following properties:

- Region
- Access Key
- Secret Key

What is required to connect to a running ActiveMQ broker using the cloud profile?

The only required step to [run ActiveMQ broker](/en/on-prem/agents/connection/cloud#apache-activemq) is to specify the broker URL.

What configuration properties are required to connect to Azure Service Bus using the cloud profile?

To connect to [Azure Service Bus](/en/on-prem/agents/connection/cloud#azure-service-bus) using the cloud profile, you must configure the following properties:

- Provider
- Class
- Remote URI
- Username
- Password

## On-prem profile connections

What's a connection profile?

A [connection profile](/en/on-prem/agents/connection/profile#what-is-a-connection-profile) is a file that uniquely identifies and contains information for an on-prem application. Profiles are stored in a configuration file located at `<INSTALL_HOME>/conf/config.yml`.

What types of systems can I connect to?

You can connect to various types of [systems](/en/on-prem/agents/connection/profile#system-types), including:

- Databases
- On-prem file systems
- SAP
- Java messaging service
- Apache Kafka
- Active Directory
- HTTP profiles
- NTLM
- Command-line scripts
- Extensions
- Server configurations.

How do I apply a new connection profile configuration?

Your OPA must be restarted whenever a change is made to `config.yml`, including when you [apply a new connection profile](/en/on-prem/agents/connection/profile#applying-a-new-configuration). To allow the on-prem agent to apply the changes automatically, add `config: autoReload: true` to the top of your `config.yml` file. When enabled, changes made to `config.yml` are picked up by `autoReload`, and no manual restart is required. Note that `autoReload` doesn't apply to changes made to server profiles, which require you to manually start and stop the OPA.

What are database connection profiles used for?

[Database connection profiles](/en/on-prem/agents/connection/profile#database-profile) provide the information your OPA uses to connect to a database. These profiles are located in the database section of the `config.yml` file. OPA supports connections to multiple databases.

Which databases are supported by OPA for database connection profiles, and what properties can be included?

OPA supports various [databases](/en/on-prem/agents/connection/profile#supported-databases), including:

- Amazon Redshift
- JDBC-compatible databases:
  - Microsoft SQL Server
  - MySQL
  - Oracle
  - PostgreSQL

Database connection profiles can contain properties such as:

- Adapter
- URL
- Host
- Port
- Database name
- Username
- Password
- driverClass
- Pooled options
- SSL configurations

How can I configure an on-prem file system profile?

To work with [on-prem files](/en/on-prem/agents/connection/profile#on-prem-files-profile), define a file system profile in the files section of `config.yml`. You must specify the base folder for file access.

What is required for configuring a SAP connection profile?

A [SAP connection profile](/en/on-prem/agents/connection/profile#sap-profile) requires both a Server profile and a SAP section to be defined. The Server profile includes the location of SAP JCo connector libraries, while the SAP section contains details about the connection type, host, system number, program ID, and more.

What are the default ports used by the SAP connector?

The [SAP connector uses default ports](/en/on-prem/agents/connection/profile#sap-profile) such as 36xx for connections through SAP Message Server and 48xx (with SNC) or 33xx (without SNC) for direct calls to SAP.

What is the purpose of the HTTP profile?

The [HTTP profile](/en/on-prem/agents/connection/profile#http-profile) allows you to configure agent access to internal HTTPS resources. You can set properties, such as:

- `connectTimeout`
- `keepAlive`
- SSL configurations

When do I need an NTLM connection profile?

[NTLM connection profiles](/en/on-prem/agents/connection/profile#ntlm-profile) are used for certain HTTP resources requiring NTLM authentication. You can configure properties like auth, username, password, base\_url, and more.

How can I use the command-line scripts profile?

The [command-line scripts profile](/en/on-prem/agents/connection/profile#command-line-scripts-profile) allows you to run scripts or commands on the OPA. You can define scripts, parameters, and specify command execution properties.

What is the purpose of the extensions profile, and how do I configure it?

The [extensions profile](/en/on-prem/agents/connection/profile#extensions-profile) is used for working with Java extensions. You must define server and extensions sections, including `controllerClass` and `secret` properties for Java classes.

What does the server profile define, and what properties can it contain?

[Server profiles](/en/on-prem/agents/connection/profile#server-profile) define where OPA assets are located on the on-prem server. They can contain properties like `classpath` and `staging`, which specify the directories for Java classes and temporary file storage.

---
