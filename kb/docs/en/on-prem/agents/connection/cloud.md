---
url: 'https://docs.workato.com/en/on-prem/agents/connection/cloud.md'
description: >-
  Set up on-prem agent connections directly in Workato with cloud profiles,
  without editing a config file on the agent's machine.
---

# Cloud Profiles

A single Workato on-prem agent (OPA) can connect to multiple on-prem applications. A **cloud profile** allows you to set up a connection directly in Workato. This option can be selected when [creating a new on-prem group](/en/on-prem/groups/create-group).

> **SUMMARY**
> 
> - Cloud profiles let you configure on-prem connections directly in Workato, rather than manually editing a local config file on the agent's system.
> - Cloud profiles support databases, on-prem file systems, SAP, Apache Kafka, certain secrets management systems, and other systems.
> - OPA versions starting from `2.15.0` support cloud profiles.
> - When you create a new connection, Workato automatically propagates the configuration details to all agents in the on-prem group.

* * *

## Basics

- [What's a cloud profile?](#what-is-a-cloud-profile)
- [What types of systems can I connect to?](#system-types)
- [How do I apply a new configuration?](#applying-a-new-configuration)

### What's a cloud profile?

A cloud profile is a new way of setting connection for on-prem agent. Since OPA version `2.15.0` you can configure on-prem connections directly in Workato instead of editing local on-prem agent config file. This is a big simplification of the existing process as you no longer need a direct access to the machine where the agent is installed. Just make sure your agent is up and running.

When creating a connection you will see the input field called `Connection type`. It is a list of existing on-prem groups. For some of the cloud connectors there can be a default `Cloud` setting. Make sure you select on-prem group that supports cloud profiles so you can create a connection directly in Workato.

Below is an example of SQL Server connection when on-prem group with cloud profiles is selected. As you can see database connection properties can be set just like for a normal cloud connector.

![SQL Server cloud profile connection](/assets/on-prem-agent-cloud-profile-example.BQZ8QmfO.png)_SQL Server cloud profile connection_

### What types of systems can I connect to?

Cloud profiles are supported by the following system types:

- [Databases](#database-profile)
- [On-prem file systems](#on-prem-files-profile)
- [SAP](#sap-profile)
- [Java messaging service](#jms-profile)
- [Apache Kafka](#apache-kafka-profile)
- [Active Directory](#active-directory-profile)
- [Command-line scripts](#command-line-scripts-profile)

> **WARNING**
> 
> Please note that configuring some additional settings like google secrets manager, azure key vault or more advanced settings is not yet supported by cloud profiles. If you want to use them please check [connection profiles](/en/on-prem/agents/connection/profile).

### How do I apply a new configuration?

When you create a new connection the details are automatically propagated to all agents in the specific on-prem group. It should happen almost immediately but in some cases it might take a while for an agent to get updated connection details.

## Database cloud profiles

Database cloud profiles provide the information your on-prem agent (OPA) uses to connect to a database.

> **JDBC DRIVER REQUIREMENT**
> 
> To establish a connection with a JDBC database, copy the appropriate JDBC driver to the `lib_ext` folder of your on-prem agent. The on-prem agent can't connect to the database without this driver.

All database connectors allow you to connect through an on-prem agent. In the connection fields, choose the on-prem group from the **Connection type** field.

After [creating an on-prem group](/en/on-prem/groups/create-group) that supports cloud profile configuration, you can configure the connection in Workato as a cloud connector. Fill in the required fields and click **Connect**.

![Database connection using cloud profiles](/assets/on-prem-agent-db-cloud.DxhDh-9a.png)_Database connection using cloud profile_

In this section, we'll cover:

- [Profile properties](#profile-properties)
- [Supported database types](#supported-databases)

### Profile Properties

Database cloud connection profiles can contain the following properties:

| Property name | Description |
| --- | --- |
| **url/host** _required_ | The host address of the database. For example, `localhost`. **Note:** A `url` or `host` value must be provided to fully configure the connection profile. |
| **port** _conditional_ | The port of the database. This property may be omitted if using the default port for a database type. For example, PostgreSQL databases use port `5432` by default. If your PostgreSQL uses this port, you don't need to add a `port` property to the connection profile. Default ports are listed in the [Supported databases](#supported-databases) section. |
| **database** _conditional_ | The name of the database. For example: `sales` **Note:** This property may be omitted if the `url` property is provided. |
| **username** _required_ | The username of a database user that will be used to connect to the database. |
| **password** _required_ | The password of the database user (`username`). |
| **ssl** _optional_ | Options for configuring SSL connections. SSL is supported for the following databases: **MySQL**: version 5.7 and higher, **PostgreSQL**: version 11.x and higher Contains the following properties: **Server certificate** (optional): X509 server certification in .pem format., **SSL certificate** (optional): X509 client certificate in .pem format., **SSL certificate key** (optional): RSA client key in .pem format. |

### Supported Databases

The following table contains information about the databases OPA currently supports.

| Database name | Default port |
| --- | --- |
| Amazon Redshift | `5439` |
| JDBC-compatible databases | N/A |
| Microsoft SQL Server | `1433` |
| MySQL | `3306` |
| Oracle | `1521` |
| PostgreSQL | `5432` |

* * *

## On-prem files Cloud Profile

Refer to the [On-prem files connector documentation](/en/connectors/on-prem-files) for more information.

* * *

## FTP(S) Cloud Profile

Refer to the [FTP connector documentation](/en/connectors/ftp).

* * *

> **ON-PREM AGENT VERSION**
> 
> OPA 25.0 or newer is required to use the FTP(S) connector.

## SFTP Cloud Profile

Refer to the [SFTP connector documentation](/en/connectors/sftp).

* * *

> **ON-PREM AGENT VERSION**
> 
> OPA 24.0 or newer is required to use the SFTP connector.

## SMB Cloud Profile

Refer to the [SMB connector documentation](/en/connectors/smb) for additional information.

* * *

> **ON-PREM AGENT VERSION**
> 
> OPA 26.0 or newer is required to use the SMB connector.

## SAP Cloud Profile

There are two connection types that the SAP connector supports - [Direct connections](#sap-direct-connection) or [Message Server connections](#sap-message-server-connection).

> **SAP DEFAULT PORTS**
> 
> The SAP connector uses the following ports by default:
> 
> - **With SAP Message Server**: `36xx`, where `xx` is the SAP system number.
> - **Without SAP Message Server** (such as a direct call to SAP): `48xx` with SNC, or `33xx` without SNC.
> 
> For HTTP(S) inbound communication, such as consuming REST OData services and SOAP web services provisioned from SAP, ports default to `8000` for HTTP and `44300` for HTTPS. Complete the following steps to find the ports to use for a custom SAP configuration:
> 
> 1. Go to the ICM Monitor **(SMICM)** transaction.
>    
> 2. Select **Goto > Services** to display the services configured in ICM and their corresponding ports.
>    

If the ports vary from our defaults, ensure port overrides are included in the connection details using the optional inputs for 'Client MS Server' and 'MS Server'.

> **IDOC RECEPTION STRATEGY**
> 
> Effective on-prem agent (OPA) v32.2, you can set the IDoc reception strategy using the **IDoc reception strategy** connection property. Supported values are:
> 
> - `LEGACY`: Default. Retained for backward compatibility. No configuration change is required to keep the existing behavior, because OPA uses `LEGACY` by default.
> - `SAPIDOC`: Recommended. Supports multi-byte characters. Non-unicode systems must select `SAPIDOC` after upgrading OPA to version 32.2.
> 
> Ensure that all connections pointing to the same on-prem group maintain consistent values for this property.

### SAP - Direct Connection

Below is the example of `Direct` connection type. Use this connection type if SAP system is directly exposed as an application server.

![On-prem sap direct connection using cloud profile](/assets/on-prem-sap-cloud-direct.C7ChE_AY.png)_On-prem sap direct connection using cloud profile_

| Parameter | Description | Click to expand image |
| --- | --- | --- |
| **Gateway host** (jco.client.ashost) | Can be either DNS name or IP address. If present, this describes a direct connection to the SAP host. Can be in the format `xx.xx.xx.xx`. This is the IP Address of the SAP application server you are directly connecting to. This can be seen on the SAP Logon Pad which is used to log in to your on-premise SAP Application server. | ![Host](/assets/ashost.rqJKl26m.png) |
| **System number** (jco.client.sysnr) | Two-digit SAP system number. It identifies the logical port on which the application server is listening for incoming requests. Commonly found from the TCP Port 33XX where XX is the system number. _This defaults to `00` if not provided_. | ![System number](/assets/system-number.CUyQ5smV.png) |
| **Program ID** (jco.server.progid) | This matches the program ID given to the RFC destination linked to Workato in Tcode `SM59`. | ![Program ID](/assets/program-id.CG_7iNiZ.png) |
| **Quality of protection** (jco.client.snc\_qop) | **Optional**. Only required if you configure Secure Network communication. If selected, JCO property `jco.client.snc_mode` is set to `1`. _This defaults to `No encryption` if not provided_ |  |
| **SAPcrypto library path** (jco.client.snc\_lib) | **Optional**. Only required if you configured Secure Network communication. Provide the filesystem path to l`ibsapcrypto.so` (Linux), l`ibsapcrypto.dylib` (Mac), `sapcrypto.dll` (Windows) within the server where your OPA is hosted. For example: `C:\sec\sapcrypto.dll` |  |
| **SNC partner name** (jco.client.snc\_partnername) | **Optional**. Only required if you configured Secure Network communication. SNC partner found in STRUST under SNC `SAPCryptolib`. Must be prepended with the letter "p:". For example: `p:CN=EH8, OU=I0021153688, OU=SAP Web AS, O=SAP Trust Community, C=DE` |  |
| **Client** (jco.client.client) | The SAP client you plan to use for the connection. This is a three-digit value. For example: `100` or `080` | ![Client](/assets/client.B631BRxq.png) |
| **Language** (jco.client.lang) | **Optional**. Represents the logon language. If the language property is not provided, it defaults to the language configured for the user in SAP. Valid values are two-character ISO language codes or one-character SAP language codes. | ![Language](/assets/language.DvcNbKFf.png) |
| **User** (jco.client.user) | SAP user provisioned for Workato. Using background user and disabling dialog properties are recommended. | ![User](/assets/user.DADs65Xp.png) |
| **Password** (jco.client.passwd) | SAP user password. | ![Password](/assets/password.Bs36JuNY.png) |
| **metadata\_refresh\_interval** | The interval in minutes to refresh metadata from SAP (except JCo cache). Default is 1440 minutes (24 hours). |  |
| **SNC name** (jco.client.snc\_myname) | **Optional**. Canonical name of the client certificate you plan to use for the connection. |  |
| **Trace** (jco.client.trace) | **Optional**. This enables or disables RFC trace. Valid values are `0` or `1`. |  |
| **SAP Router** (jco.client.saprouter) | **Optional**. SAP Router string to be passed in the format `/H/<Hostname/Public IP of the SAP Router>/S/<Port>`. |  |
| **Connection pool capacity** | **Optional**. Maximum number of active connections that are kept open in the connection pool. Consult SAP admin to set value for this parameter. |  |
| **Connection peak limit** | **Optional**. Maximum number of active connections that can be created beyond the pool capacity during periods of high demand. After the load decreases, the additional connections are closed. Consult SAP admin to set value for this parameter. |  |
| **Connection count** (jco.server.connection\_count) | **Optional**. Enter the number of server connections. Valid range is from `1` to `100`. Default value is `2`. |  |
| **Maximum startup retry delay** (jco.server.max\_startup\_delay) | **Optional**. The maximum time (in seconds) between two startup attempts in case of failures. |  |
| **IDoc schema cache validity** | **Optional**. Provide the IDoc schema cache validity in seconds. A value of `0` refreshes on every event (default). A value of `3600` refreshes hourly. Applicable for on-prem agent (OPA) v32.0 and later. |  |
| **IDoc reception strategy** | **Optional**. Determines how the on-prem agent receives IDocs. Select `LEGACY` for backward compatibility (default), or `SAPIDOC` for multi-byte character support (recommended). Applicable for on-prem agent (OPA) v32.2 and later. |  |

> **CONNECTION POOLING**
> 
> It's crucial for the SAP BASIS team to monitor performance after configuring the parameters (**Connection pool capacity** and **Connection peak limit**) to ensure that the connection pool can efficiently handle the workload without exhausting resources or overloading the SAP server.

### SAP - Message Server Connection

Below is the example of `Message server` connection type. Use this connection type when SAP system is behind message server gateway.

![On-prem sap message server connection using cloud profile](/assets/on-prem-sap-cloud-server.ylt5I3aS.png)_On-prem sap message server connection using cloud profile_

| Parameter | Description | Click to expand image |
| --- | --- | --- |
| **Message server host** (jco.client.mshost) | Message Server host in the format of `xx.xx.xx.xx`. This is the IP Address of the Message Server you are connecting. | ![Message Server Host](/assets/mhost.bEHbtMbD.png) |
| **System ID** | The system ID of the system the message server belongs to. See SAP Note 52959 in case of connection error. |  |
| **Logon group** (jco.client.group) | **Optional**. Logical group name of the application servers. Can be found in SAP Tcode `SMLG` | ![Group](/assets/group.TObmNvKj.png) |
| **Program ID** (jco.server.progid) | This matches the program ID given to the RFC destination linked to Workato in Tcode `SM59`. | ![Program ID](/assets/program-id.CG_7iNiZ.png)_Program ID_ |
| **Quality of protection** (jco.client.snc\_qop) | **Optional**. Only required if you configure Secure Network communication. Defaults to `No encryption`. If selected, JCO property `jco.client.snc_mode` is set to `1`. |  |
| **SAPcrypto library path** (jco.client.snc\_lib) | **Optional**. Only required if you configured Secure Network communication. Provide the filesystem path to `libsapcrypto.so` (Linux), `libsapcrypto.dylib` (Mac), `sapcrypto.dll` (Windows) within the server that your OPA is hosted. For example: `C:\sec\sapcrypto.dll` |  |
| **SNC partner name** (jco.client.snc\_partnername) | **Optional**. Only required if you configured Secure Network communication. SNC partner found in STRUST under SNC `SAPCryptolib`. Must be prepended with the letter "p:". For example: `p:CN=EH8, OU=I0021153688, OU=SAP Web AS, O=SAP Trust Community, C=DE` |  |
| **Client** (jco.client.client) | The actual client number which is used for connecting to Workato. Use the same one you log into with your SAP Logon Pad. It's a 3 digit integer. | ![Client](/assets/client.B631BRxq.png) |
| **Language** (jco.client.lang) | **Optional**. Represents the logon language. If the language property is not provided, it defaults to the language configured for the user in SAP. Valid values are two-character ISO language codes or one-character SAP language codes. | ![Language](/assets/language.DvcNbKFf.png) |
| **User** (jco.client.user) | SAP user provisioned for Workato. Using background user and disabling dialog properties are recommended. | ![User](/assets/user.DADs65Xp.png) |
| **Password** (jco.client.passwd) | SAP user password. | ![Password](/assets/password.Bs36JuNY.png) |
| **metadata\_refresh\_interval** | The interval in minutes to refresh metadata from SAP (except JCo cache). Default is 1440 minutes (24 hours). |  |
| **SNC name** (jco.client.snc\_myname) | **Optional**. Canonical name of the client certificate you plan to use for the connection. |  |
| **Client MS Server** (jco.client.msserv) | **Optional**. Client port number. Overrides the default `3600` port number. |  |
| **MS Server** (jco.server.msserv) | **Optional**. Message server port number. Overrides the default `3600` port number. |  |
| **Trace** (jco.client.trace) | **Optional**. This enables or disables RFC trace. Valid values are `0` or `1`. |  |
| **SAP Router** (jco.client.saprouter) | **Optional**. SAP Router string to be passed in the format `/H/<Hostname/Public IP of the SAP Router>/S/<Port>`. |  |
| **Connection pool capacity** | **Optional**. Maximum number of active connections that are kept open in the connection pool. Consult SAP admin to set value for this parameter. |  |
| **Connection peak limit** | **Optional**. Maximum number of active connections that can be created beyond the pool capacity during periods of high demand. After the load decreases, the additional connections are closed. Consult SAP admin to set value for this parameter. |  |
| **Connection count** (jco.server.connection\_count) | **Optional**. Enter the number of server connections. Valid range is from `1` to `100`. Default value is `2`. |  |
| **Maximum startup retry delay** (jco.server.max\_startup\_delay) | **Optional**. The maximum time (in seconds) between two startup attempts in case of failures. |  |
| **IDoc schema cache validity** | **Optional**. Provide the IDoc schema cache validity in seconds. A value of `0` refreshes on every event (default). A value of `3600` refreshes hourly. Applicable for on-prem agent (OPA) v32.0 and later. |  |
| **IDoc reception strategy** | **Optional**. Determines how the on-prem agent receives IDocs. Select `LEGACY` for backward compatibility (default), or `SAPIDOC` for multi-byte character support (recommended). Applicable for on-prem agent (OPA) v32.2 and later. |  |

> **CONNECTION POOLING**
> 
> It's crucial for the SAP BASIS team to monitor performance after configuring the parameters (**Connection pool capacity** and **Connection peak limit**) to ensure that the connection pool can efficiently handle the workload without exhausting resources or overloading the SAP server.

* * *

## JMS Cloud Profile

The following JMS providers are supported by the cloud profile on-prem agent:

- Amazon Simple Queue Service
- Apache ActiveMQ
- Azure Service Bus

### Amazon SQS

You need the following configuration properties when connecting to Amazon SQS:

![On-prem cloud profile amazon](/assets/on-prem-jms-amazon.0INO6hRH.png)_On-prem cloud profile amazon_

| Property name | Comment |
| --- | --- |
| region | Your Amazon API region, eg 'us-east-2' |
| accessKey | Your Amazon API access key |
| secretKey | Your Amazon API secret |

Ensure your SQS queue exists before sending messages.

### Apache ActiveMQ

For connecting to a running ActiveMQ broker you only need to specify the broker URL:

![On-prem cloud profile activemq](/assets/on-prem-jms-activemq.CqEk9UWH.png)_On-prem cloud profile activemq_

The ActiveMQ broker can't be embedded in the agent. OPA doesn't support `vm://` broker connections.

### Azure Service Bus

Azure Service Bus uses a custom JMS provider. Use the following configuration properties to connect, replacing `<HOST_NAME>`, `<POLICY_NAME>`, and `<PRIMARY_KEY>` with values from Azure Service Bus:

```yaml
jms:
  azureServiceBus:
    provider: custom
    class: org.apache.qpid.jms.JmsConnectionFactory
    remoteURI: amqps://<HOST_NAME>.servicebus.windows.net
    username: <POLICY_NAME>
    password: "<PRIMARY_KEY>"
```

Download the required [JAR files and dependencies](https://mvnrepository.com/artifact/org.apache.qpid/qpid-jms-client) and place them in your `lib_ext` folder.

Add the classpath inside the `config.yml` file.

```yaml
server:
  classpath: lib_ext
```

* * *

## Apache Kafka Cloud Profile

Refer to the [Apache Kafka connector documentation](/en/connectors/kafka).

* * *

## Active Directory Cloud Profile

Refer to the [Active Directory connector documentation](/en/connectors/active_directory).

* * *

## HTTP NTLM Cloud Profile

Please refer to [HTTP connector NTLM documentation](/en/developing-connectors/http/connection-setup#authentication-type-on-prem-ntlm).

* * *

## Command-line Scripts Cloud Profile

Refer to the [On-prem files connector documentation](/en/connectors/on-prem-command-line-scripts) for more information.

---
