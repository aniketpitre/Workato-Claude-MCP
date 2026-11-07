---
url: 'https://docs.workato.com/en/on-prem/agents/connection/profile.md'
description: >-
  Set up on-prem agent connection profiles in the config.yml file to identify
  and connect to each on-prem application.
---

# Connection Profiles

A single Workato on-prem agent (OPA) can connect to multiple on-prem applications. A **connection profile** uniquely identifies each application and contains configuration information required to connect.

* * *

## Basics

- [What's a connection profile?](#what-is-a-connection-profile)
- [What types of systems can I connect to?](#system-types)
- [How do I apply a new configuration?](#applying-a-new-configuration)

### What's a connection profile?

A connection profile is a file that uniquely identifies and contains information for an on-prem application. Profiles are stored in a configuration file located at `<INSTALL_HOME>/conf/config.yml`.

A typical config file looks something like this:

```yaml
database:
  profile1:   # Connection names can't contain
    ...       # spaces or special characters
  profile2:   # But may contain underscores (_) and hyphens (-)
    ...

files:
  profile3:
    ...
  profile4:
    ...

jms:
  profile5:
    ...

ldap:
  profile6:
    ...

server:
  classpath:
    ...
  staging:
    ...
```

### What types of systems can I connect to?

A `config.yml` file can contain profiles for the following system types:

- [Databases](#database-profile)
- [On-prem file systems](#on-prem-files-profile)
- [SAP](#sap-profile)
- [Java messaging service](#jms-profile)
- [Apache Kafka](#apache-kafka-profile)
- [Active Directory](#active-directory-profile)
- [HTTP profile](#http-profile)
- [NTLM](#ntlm-profile)
- [Command-line scripts](#command-line-scripts-profile)
- [Extensions](#extensions-profile)
- [Server](#server-profile)

You can also configure [proxy servers](/en/on-prem/agents/proxy) for OPAs installed on a server with limited internet connectivity.

### How do I apply a new configuration?

By default, your OPA must be restarted whenever a change is made to `config.yml`. Refer to the [Running your on-prem agent guide](/en/on-prem/agents/run) for more info.

To allow the on-prem agent apply the changes automatically, add the following to the top of your `config.yml` file to use the `autoReload` option

```yaml
config:
  autoReload: true
```

When enabled, changes made to `config.yml` will be picked up by `autoReload`. You won't need to manually restart the OPA.

> **AUTORELOAD AND SERVER PROFILES**
> 
> `autoReload` doesn't apply to changes made to [server profiles](#server-profile). To apply these changes, manually start and stop the OPA.

## Database profiles

Database connection profiles provide the information your on-prem agent (OPA) uses to connect to a database. Connection profiles are located in the `database` section of the `config.yml` file.

> **JDBC DRIVER REQUIREMENT**
> 
> To establish a connection with a JDBC database, copy the appropriate JDBC driver to the `lib_ext` folder of your on-prem agent. The on-prem agent can't connect to the database without this driver.

OPA supports connections to multiple databases. Add a section under the `database` key for each database you plan to connect to. For example:

```yaml
database:
  your-connection-name:         # Specify the connection name, ex: sales-database
    adapter: sqlserver
    host: localhost
    port: 1433
    database: sales
    username: sales_analyst
    password: secretPassword456
```

In this section, we'll cover:

- [Profile properties](#profile-properties)
- [Supported database types](#supported-databases)
- [Example profile configurations](#example-database-profiles)

### Profile Properties

Database connection profiles can contain the following properties:

| Property name | Description |
| --- | --- |
| **adapter** _optional_ | The type of database the profile is for. For example, if the profile is for a PostgreSQL database, this value would be `postgresql`. Must be one of the [databases supported by OPA](#supported-databases). Refer to the [configuration example](#example-adapter) for more info. |
| **url** _optional_ | The JDBC connection URL for the database. For example, `jdbc:postgresql://sales.database:5432/sales` connects to a PostgreSQL database. **Note:** A `url` or `host` value must be provided to fully configure the connection profile. Refer to the [configuration example](#example-url) for more info. |
| **host** _optional_ | The host address of the database. For example, `localhost`. **Note:** A `url` or `host` value must be provided to fully configure the connection profile. |
| **port** _conditional_ | The port of the database. This property may be omitted if using the default port for a database type. For example, PostgreSQL databases use port `5432` by default. If your PostgreSQL uses this port, you don't need to add a `port` property to the connection profile. Default ports are listed in the [Supported databases](#supported-databases) section. |
| **database** _conditional_ | The name of the database. For example: `sales`. **Note:** This property may be omitted if the `url` property is provided. |
| **username** _required_ | The username of a database user that will be used to connect to the database. |
| **password** _required_ | The password of the database user (`username`). This value can be a secret from an external [secrets manager](/en/on-prem/agents/secrets-manager). Refer to the [configuration example](#example-secret-password) for more info. |
| **driverClass** _required_ | **Required only for JDBC connections.** The fully-qualified name of the JDBC driver class for the given database. The driver class must be available on the agent's [`classpath` property](#server-profile-properties). |
| **pooled** _optional_ | Options for configuring database connection pooling, which reduces lag between reconnection attempts. Contains the following properties: **minSize** (optional): Minimum connection pool size. Default is 1.; **maxSize** (optional): Maximum connection pool size. Default is 10.; **idleTimeout** (optional): Idle time after which the connection will be recycled, in milliseconds.; **maxLifetime** (optional): Maximum life time of a connection, in milliseconds.; **timeout** (optional): Maximum duration for which a client awaits for a connection from the pool, in milliseconds. |
| **ssl** _optional_ | Options for configuring SSL connections. SSL is supported for the following databases: **MySQL**: version 5.7 and higher, **PostgreSQL**: version 11.x and higher Contains the following properties: **cert** (required): The file path to the SSL certificate., **trustAll** (optional): Forces the client to trust any certificate chain if set to `true`. Self-signed server certificates are supported. Defaults to `false`., **verifyHost** (optional): Matches the name stored in the server certificate against the domain name if set to `true`. Defaults to `false`. Refer to the [configuration example](#example-ssl) for more info. |

### Supported Databases

The following table contains information about the databases OPA currently supports, including:

- **Database name**: The name of the database
- **Adapter**: The `adapter` value for the database. This value is used to specify the type of database OPA is connecting to.
- **Default port**: The default `port` for the database.
- **Notes**: Notes about configuring the database.

| Database name | Adapter | Default port | Notes |
| --- | --- | --- | --- |
| Amazon Redshift | `redshift` | `5439` |  |
| JDBC-compatible databases | `jdbc` | N/A | Requires `url` and `driverClass` properties in the connection profile, and a configured `server` profile. Refer to the [JDBC example](#example-jdbc-profile) for more info. |
| Microsoft SQL Server | `sqlserver` | `1433` |  |
| MySQL | `mysql` | `3306` | By default, the driver streams result sets row-by-row. To change the buffer size, use the [`defaultFetchSize`](https://dev.mysql.com/doc/connector-j/8.0/en/connector-j-connp-props-performance-extensions.html#cj-conn-prop_defaultFetchSize) property. |
| Oracle | `oracle` | `1521` | The `url` property is required if using Oracle Service. Either the `adapter` or `url` property may be used if using a SID. Refer to the [Oracle example](#example-oracle-database) for more info. |
| PostgreSQL | `postgresql` | `5432` |  |

### Example Configurations

Click the blocks to display the example.

Using the adapter property

#### Using the adapter property

The following example uses the `adapter` property to connect to Microsoft SQL Server and Amazon Redshift databases:

```yaml
database:
  sales:
    adapter: sqlserver
    host: localhost
    port: 1433
    database: sales
    username: sales_analyst
    password: secretPassword123
  operations:
    adapter: redshift
    host: localhost
    port: 5439
    database: customers
    username: cs_analyst
    password: secretPassword789
```

Using the url property

#### Using the url property

The following example uses the `url` property to connect to a PostgreSQL database.

```yaml
database:
  sales:
    url: jdbc:postgresql://sales.database:5432/sales
    username: sales_analyst
    password: secretPassword123
    ApplicationName: workato
```

Using a secret for the password property

#### Using a secret for the password property

The following example uses a secret from an external secrets manager to provide the database password. Refer to the [Secrets Manager](/en/on-prem/agents/secrets-manager) for more info.

```yaml
database:
  sales_database:
    adapter: sqlserver
    host: localhost
    port: 1433
    database: test
    username: sales_user
    password: { secret: 'sales-db-password-password' }
```

Connecting to Oracle databases

#### Connecting to Oracle databases

You can connect to either a **SID** or **Service** when connecting to Oracle databases.

If using a **SID**, you can use either the [`adapter`](#example-adapter) or [`url`](#example-url) property.

If using a **Service**, the `url` property must be provided:

```yaml
database:
  erp:
    url: jdbc:oracle:thin:@localhost:1521/PROD
    username: admin
    password: SecretPassword456
```

Connecting to JDBC-compatible databases

#### Connecting to JDBC-compatible databases

Connections to JDBC-compatible databases require the following:

- `url` and `driverClass` [properties](#profile-properties) in the connection profile
- A configured [`server` profile](#server-profile)

```yaml
database:
  tpc:
    url: jdbc:presto://warehouse.intra:8889/tpch
    driverClass: com.facebook.presto.jdbc.PrestoDriver
    adapter: jdbc
    username: my_user

server:
  classpath: jdbc
```

Connecting to a specific SQL Server instance

The following example shows how to define a JDBC `url` for a specific SQL Server instance when there are multiple instances on the same server.

**Note:** You only need to provide the instance name if you don't know the port number.

```yaml
database:
  sales:
    adapter: sqlserver
    url: jdbc:sqlserver://[Server/Host]\[Instance]
    username: user
    password: Secret123
```

Enabling SSL

#### Enabling SSL

The following example configures SSL for a PostgreSQL database.

**Note**: Currently, SSL connections are supported for MySQL (5.7+) and PostgreSQL (11+) databases.

```yaml
database:
  sales:
    adapter: postgresql
    host: localhost
    port: 5432
    database: sales
    username: sales_analyst
    password: secretPassword123
    ssl:
      cert: /path/client_ca.crt
      trustAll: false
      verifyHost: true
```

* * *

## On-prem files Profile

Working with on-prem files requires you to define a file system profile in the `files` section. You need to specify the base folder for file access as it will be used for resolving relative paths. A folder named `HR` in the `C:\Documents\` directory will be configured like this:

```yaml
files:
  hrfiles:
    base: "C:\\Documents\\HR"
```

In another example, if you wish to provide access to the `employees` folder in the Desktop directory, the configuration will have a file path that looks something like this:

```yaml
files:
  hrfiles:
    base: "/Users/me/Desktop/employees"
```

* * *

## FTP(S) Profile

To set up the FTP(S) connection you have to define a profile in the `ftp` section. You need to specify the host and the port of the FTP server along with the credentials. A simple connection to the FTP server will be configured like this:

```yaml
ftp:
  ftp_profile_1:
    hostname: myftpserver.com
    port: 21
    user: username
    password: secretpassword
```

  

> **ON-PREM AGENT VERSION**
> 
> OPA 25.0 or newer is required to use the FTP(S) connector.

The following properties are supported:

| Property name | Description |
| --- | --- |
| **hostname** _required_ | The address of your FTP server. |
| **port** _optional_ | The default port for FTP is 21. |
| **username** _required_ | The user name of the FTP server to be connected. |
| **password** _required_ | The password credential to the FTP server to be connected. |
| **implicit** _optional_ | Explicit FTPS connection type. Set to `true` for an implicit FTPS connection type. Default value is `false`. |
| **cert** _optional_ | X509 server certificate in .pem format. |
| **trustAll** _optional_ | Forces the client to trust any certificate chain. Self-signed server certificates are supported. |

Below is an example for public/private key pair and password authentication type:

```yaml
ftp:
  ftp_profile_key_protected:
    hostname: myftpserver.com
    port: 21
    user: username
    password: secretpassword
    ssl:
      implicit: false
      cert: /path/to/PEM-encoded-certificate-or-trusted-CA
      trustAll: true
```

Refer to the [FTP connector documentation](/en/connectors/ftp) for more information.

* * *

## SFTP Profile

To set up the SFTP connection you have to define a profile in the `sftp` section. You need to specify the host and the port of the SFTP server along with the credentials. A simple connection to the SFTP server will be configured like this:

```yaml
sftp:
  sftp_profile_1:
    host: mysftpserver.com
    port: 22
    user: username
    password: secretpassword
```

  

> **ON-PREM AGENT VERSION**
> 
> OPA 24.0 or newer is required to use the SFTP connector.

The following properties are supported:

| Property name | Description |
| --- | --- |
| **host** _required_ | The address of your SFTP server. |
| **port** _optional_ | The default port for SFTP is 22. |
| **username** _required_ | The user name of the SFTP server to be connected. |
| **password** _conditional_ | The password credential to the SFTP server to be connected. Required for username/password authentication, or public/private key pair authentication combined with a password. |
| **private\_key** _conditional_ | Path to the private key. Required for public/private key pair authentication, with or without a password. |
| **passphrase** _optional_ | Optional password if the private key is password protected. Applies to public/private key pair authentication, with or without a password. |
| **host\_key** _optional_ | A hash of the SSH public key. Contact your SFTP server administrator for the public key in Base64 format. |
| **server\_host\_key** _optional_ | Required if the server uses the SSH-RSA host key algorithm. SSH-RSA authentication isn't supported for cloud SFTP connections. Refer to the [SSH-RSA support](#ssh-rsa-support) section for more information. |
| **PubkeyAcceptedAlgorithms** _optional_ | Required if the server uses the SSH-RSA host key algorithm. Enter the required algorithm, for example, `ssh-ed25519,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,rsa-sha2-512,rsa-sha2-256,ssh-rsa`. SSH-RSA authentication isn't supported for cloud SFTP connections. Refer to the [SSH-RSA support](#ssh-rsa-support) section for more information. |

Below is an example for public/private key pair and password authentication type:

```yaml
sftp:
  sftp_profile_key_protected:
    host: mysftpserver.com
    port: 22
    user: username
    password: secretpassword
    host_key_fingerprint: AAAAC3NzaC1lZDI1NTE5AAAAIDnkCeZXGyvQmXJ7VfbTD65NG2u0wcMA1gC5Um3tJ/2P
    private_key: /path/to/id_rsa
    passphrase: password  #if private_key is password-protected
```

Refer to the [SFTP connector documentation](/en/connectors/sftp) for more information.

### SSH-RSA support

SSH-RSA relies on SHA-1, which no longer meets modern security standards. Workato doesn't support SSH-RSA authentication for cloud connections to SFTP. Use the [Workato OPA](/en/on-prem/agents) to create an on-prem connection if you need to authenticate using SSH-RSA, or contact your server administrator to enable a stronger host key algorithm.

* * *

## SMB Profile

To set up the SMB connection to your shared network location you must first define a profile in the **smb** section. You must specify the `host`, `port`, and `share name` of the SMB along with the credentials. The following example configures a simple connection to the SMB:

```yaml
smb:
  smb_profile_1:
    host: some-host.amazonaws.com
    port: 445
    shareName: SampleSharedFolder
    username: username
    password: secretpassword
    domain: optionalDomainName
```

  

> **ON-PREM AGENT VERSION**
> 
> OPA 26.0 or newer is required to use the SMB connector.

The following properties are supported:

| Property name | Description |
| --- | --- |
| **host** _required_ | The address of your SMB server. |
| **port** _required_ | The default port for SMB is 445. |
| **shareName** _required_ | Name of the shared folder in the destination. |
| **username** _required_ | The user name that can access the SMB share. |
| **password** _required_ | The password credential. |
| **domain** _optional_ | Optional domain name of the user. |

Refer to the [SMB connector documentation](/en/connectors/smb) for more information.

* * *

## SAP Profile

For a SAP connection profile, you must define the `server` and `sap` section together.

> **SAP JCO LIBRARY DIRECTORY**
> 
> In the Server profile, the `lib_ext` is the directory where the SAP JCo connector libraries are stored. If this directory doesn't already exist, create it in the OPA root directory and place the SAP JCo connector libraries inside it. The `lib_ext` folder should contain `sap-connector-impl-X.X.jar`. Refer to the [Server profile](#server-profile) section for more information.

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

If these ports differ from our defaults, please contact Workato support.

> **SNC CONNECTION**
> 
> Refer to [SNC encryption](/en/connectors/sap/snc-encryption) for more information on Secure Network Communication setup.

> **IDOC RECEPTION STRATEGY**
> 
> Effective on-prem agent (OPA) v32.2, you can configure the IDoc reception strategy by setting the `opt.idoc_reception_strategy` JCo override in the OPA `config.yml`. Supported values are:
> 
> - `LEGACY`: Default. Retained for backward compatibility. No configuration change is required to keep the existing behavior as OPA continues to use `LEGACY` by default. For example: `opt.idoc_reception_strategy: LEGACY`
> - `SAPIDOC`: Recommended. Supports multi-byte characters. Non-unicode systems must use `SAPIDOC` in the `config.yml` after upgrading OPA to version 32.2. For example: `opt.idoc_reception_strategy: SAPIDOC`
> 
> ```yaml
> jco_overrides:
>   opt.idoc_reception_strategy: 'LEGACY'   # Value is case-insensitive
> ```

### SAP - Direct Connection

The following is an example of a `Direct` connection type. Use this connection type if the SAP system is directly exposed as an application server.

```yaml
server:
  classpath:
    - lib_ext

sap:
  sap_profile_1: # The on-prem agent connection profile name.
    network_connection:
      gateway_host: "xx.xx.xx.xx"
      system_number: "XX"
      program_id: "WORKATO"
      metadata_refresh_interval: "10"
      quality_of_protection: 3
      partner_name: "p:CN=EH8, OU=I0021153688, OU=SAP Web AS, O=SAP Trust Community, C=DE"
    user_logon:
      client: "800"
      language: "EN"
      user: "USERN"
      password: "PASSW"
    jco_overrides:
      jco.client.snc_myname: "Canonical name of the client certificate"
```

| Parameter (JCO Connection Property) | Description | Click to expand image |
| --- | --- | --- |
| **gateway\_host** (jco.client.ashost) _required_ | The IP address or DNS name of the SAP application server you are directly connecting to. This can be seen on the SAP Logon Pad used to log in to your on-premise SAP application server. Accepts the following format: `xx.xx.xx.xx`. | ![Host](/assets/ashost.rqJKl26m.png) |
| **system\_number** (jco.client.sysnr) _optional_ | The SAP system number that identifies the logical port on which the application server listens for incoming requests. Commonly found from TCP port `33XX`, where `XX` is the system number. Defaults to `00`. | ![System number](/assets/system-number.CUyQ5smV.png) |
| **program\_id** (jco.server.progid) _conditional_ | The program ID given to the RFC destination linked to Workato in the `SM59` transaction. _Required_ if you use IDocs. Not needed for connections that use only RFCs. | ![Program ID](/assets/program-id.CG_7iNiZ.png) |
| **metadata\_refresh\_interval** _optional_ | The interval in minutes to refresh metadata from SAP (except JCo cache). Defaults to `1440` minutes (24 hours). |  |
| **quality\_of\_protection** (jco.client.snc\_qop) _optional_ | The quality of the protection level to apply. Enter one of the following numbers: `1`: Authentication only, `2`: Integrity protection (authentication), `3`: Privacy protection (integrity and authentication), `8`: Default protection, `9`: Maximum protection |  |
| **partner\_name** (jco.client.snc\_partnername) _conditional_ | The SNC partner found in the `STRUST` transaction under SNC `SAPCryptolib`. Must be prepended with `p:`. For example: `p:CN=EH8, OU=I0021153688, OU=SAP Web AS, O=SAP Trust Community, C=DE`. _Required_ if you configure Secure Network Communication (SNC). |  |
| **client** (jco.client.client) _required_ | The three-digit client number used to connect to Workato. Use the same client you log in to with your SAP Logon Pad. | ![Client](/assets/client.B631BRxq.png) |
| **language** (jco.client.lang) _optional_ | The SAP Logon language to use. Valid values include two-character ISO language codes or one-character SAP language codes. Defaults to the user or system's default language. | ![Language](/assets/language.DvcNbKFf.png) |
| **user** (jco.client.user) _required_ | The SAP user provisioned for Workato. We recommend you use a background user and disable dialog properties. | ![User](/assets/user.DADs65Xp.png) |
| **password** (jco.client.passwd) _required_ | The SAP user password. | ![Password](/assets/password.Bs36JuNY.png) |
| **jco.client.snc\_myname** _conditional_ | The canonical name of the client certificate to use for the connection. _Required_ if you configure SNC. |  |

### SAP - Message Server Connection

The following is an example of a `Message Server` connection type. Use this connection type when the SAP system is behind a message server gateway.

```yaml
server:
  classpath:
    - lib_ext

sap:
  sap_profile_2: # The on-prem agent connection profile name.
    network_connection:
      message_server_host: "xx.xx.xx.xx"
      logon_group: "XXXXX"
      system_id: "XXX"
      program_id: "WORKATO"
      metadata_refresh_interval: "10"
      quality_of_protection: 3
      partner_name: "p:CN=EH8, OU=I0021153688, OU=SAP Web AS, O=SAP Trust Community, C=DE"
    user_logon:
      client: "800"
      language: "EN"
      user: "USERN"
      password: "PASSW"
    jco_overrides:
      jco.client.snc_myname: "Canonical name of the client certificate"
      jco.client.msserv: "36<XX>"
      jco.server.msserv: "36<XX>"
```

| Parameter (JCO Connection Property) | Description | Click to expand image |
| --- | --- | --- |
| **message\_server\_host** (jco.client.mshost) _required_ | The IP address or DNS name of the Message Server you are connecting to. Accepts the following format: `xx.xx.xx.xx`. | ![Message Server Host](/assets/mhost.bEHbtMbD.png) |
| **logon\_group** (jco.client.group) _optional_ | The logical group name of the application servers. Can be found in the `SMLG` transaction. Common default group names include `PUBLIC` or `SPACE`. | ![Group](/assets/group.TObmNvKj.png) |
| **system\_id** _required_ | The system ID of the system the message server belongs to. Refer to SAP Note 52959 if you encounter a connection error. |  |
| **program\_id** (jco.server.progid) _conditional_ | The program ID given to the RFC destination linked to Workato in the `SM59` transaction. _Required_ if you use IDocs. Not needed for connections that use only RFCs. | ![Program ID](/assets/program-id.CG_7iNiZ.png) |
| **metadata\_refresh\_interval** _optional_ | The interval in minutes to refresh metadata from SAP (except JCo cache). Defaults to `1440` minutes (24 hours). |  |
| **quality\_of\_protection** (jco.client.snc\_qop) _optional_ | The quality of the protection level to apply. Enter one of the following numbers: `1`: Authentication only, `2`: Integrity protection (authentication), `3`: Privacy protection (integrity and authentication), `8`: Default protection, `9`: Maximum protection |  |
| **partner\_name** (jco.client.snc\_partnername) _conditional_ | The SNC partner found in the `STRUST` transaction under SNC `SAPCryptolib`. Must be prepended with `p:`. For example: `p:CN=EH8, OU=I0021153688, OU=SAP Web AS, O=SAP Trust Community, C=DE`. _Required_ if you configure Secure Network Communication (SNC). |  |
| **client** (jco.client.client) _required_ | The three-digit client number used to connect to Workato. Use the same client you log in to with your SAP Logon Pad. | ![Client](/assets/client.B631BRxq.png) |
| **language** (jco.client.lang) _optional_ | The SAP Logon language to use. Valid values include two-character ISO language codes or one-character SAP language codes. Defaults to the user or system's default language. | ![Language](/assets/language.DvcNbKFf.png) |
| **user** (jco.client.user) _required_ | The SAP user provisioned for Workato. We recommend you use a background user and disable dialog properties. | ![User](/assets/user.DADs65Xp.png) |
| **password** (jco.client.passwd) _required_ | The SAP user password. | ![Password](/assets/password.Bs36JuNY.png) |
| **jco.client.snc\_myname** _conditional_ | The canonical name of the client certificate to use for the connection. _Required_ if you configure SNC. |  |
| **jco.client.msserv** _optional_ | The client port number. Can be found in the `SMMS` transaction. Overrides the default `3600` port number. |  |
| **jco.server.msserv** _optional_ | The message server port number. Can be found in the `SMMS` transaction. Overrides the default `3600` port number. |  |

* * *

## JMS Profile

JMS connection profiles must be defined in the `jms` section. A JMS provider is specified by `provider` property of a connection profile. The following JMS providers are supported by the on-prem agent:

| Messaging service | provider |
| --- | --- |
| Amazon Simple Queue Service | `amazon-sqs` or `sqs` |
| Apache ActiveMQ | `activemq` |
| Azure Service Bus | `custom` |

### Amazon SQS

You need the following configuration properties when connecting to Amazon SQS:

```yaml
jms:
  MyAmazonProfile:
    provider: amazon-sqs
    region: <Your Amazon API region, eg 'us-east-2'>
    accessKey: <Your Amazon API access key>
    secretKey: <Your Amazon API secret>
```

Ensure your SQS queue exists before sending messages.

### Apache ActiveMQ

For connecting to a running ActiveMQ broker you only need to specify the broker URL:

```yaml
jms:
  MyActiveMQProfile:
    provider: activemq
    url: tcp://localhost:61616
```

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

## Apache Kafka Profile

Kafka connection profiles must be defined in the `kafka` section. You need the following configuration properties when connecting to Kafka:

```yaml
kafka:
  MyKafkaProfile:
    ... connection properties ...
```

You can provide any Kafka [producer](https://kafka.apache.org/documentation/#producerconfigs) or [consumer](https://kafka.apache.org/documentation/#newconsumerconfigs) configuration properties, for example, `bootstrap.servers` or `batch_size`.

However, some properties are overridden by the on-prem agent and cannot be configured. You will get a warning when trying to redefine a protected property. Some examples of these protected properties:

| Property name | Comment |
| --- | --- |
| key.serializer | Only `StringSerializer` is supported by agent. |
| value.serializer | Only `StringSerializer` is supported by agent. |
| key.deserializer | Only `StringSerializer` is supported by agent. |
| value.deserializer | Only `StringSerializer` is supported by agent. |
| auto.offset.reset | Defined by recipes |
| enable.auto.commit | Defined internally |

Workato Agent also supports the following (non-Kafka) configuration properties:

| Property name | Description |
| --- | --- |
| timeout | General operation timeout, milliseconds. |
| url | Comma-separated list of server URLs where protocol is either `kafka` or `kafka+ssl`. |
| ssl.truststore | Allows inlining of PEM-encoded truststore for secure connection to Kafka |
| ssl.keystore.key | Allows inlining of private key for secure connection to Kafka |
| ssl.keystore.cert | Allows inlining of client certificate for secure connection to Kafka |

`ssl.*` options above can be used when connecting to Kafka using SSL/TLS and allows you to keep PEM-encoded certificates and private keys inside the `config.yml` file. Any YAML-compatible multiline syntax could be used, for instance:

```yaml
kafka:
  MyKafkaProfile:
    ssl.truststore:
    |
      -----BEGIN CERTIFICATE-----
      502mPNNAYkY4a7Zu84DLCXLFurEa4BhLBqLkzC6WdTrBN9z6Rp/svTIl6VgjSTP6
      .....
      -----END CERTIFICATE-----
```

Note that password-protected private keys cannot be inlined.

You must configure Workato's on-prem agent as a Kafka client to connect Apache Kafka to Workato.

**MSK IAM**

Complete the following steps to authenticate Kafka using AWS MSK IAM:

1. Download the AWS MSK IAM authentication JAR from the [official AWS repository](https://github.com/aws/aws-msk-iam-auth/releases) and place it in your OPA's `lib_ext` directory.
   
2. Ensure your Kafka broker is configured to accept AWS MSK IAM authentication.
   
3. Add the following properties to your Kafka client configuration:
   
   ```yaml
   security.protocol: SASL_SSL
   sasl.mechanism: AWS_MSK_IAM
   sasl.jaas.config: software.amazon.msk.auth.iam.IAMLoginModule required;
   sasl.client.callback.handler.class: software.amazon.msk.auth.iam.IAMClientCallbackHandler
   ```
   

Refer to the AWS [IAM access control](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html) guide for more information about IAM configuration.

**SASL SCRAM SHA-256**

Complete the following steps to authenticate Kafka using SHA-256:

1. Ensure your Kafka broker is configured to accept SCRAM-SHA-256 authentication.
   
2. Add the following properties to your Kafka client configuration:
   
   ```yaml
   security.protocol: SASL_SSL
   sasl.mechanism: SCRAM-SHA-256
   sasl.jaas.config: org.apache.kafka.common.security.scram.ScramLoginModule required username=YOUR_USERNAME password=YOUR_PASSWORD;
   ```
   
3. Replace the following placeholders:
   
   | Placeholder | Definition |
   | --- | --- |
   | YOUR\_USERNAME | The username for your Kafka client. |
   | YOUR\_PASSWORD | The password for your Kafka client. |
   

**SSL**

Complete the following steps to authenticate Kafka using SSL:

1. Ensure your Kafka broker is configured to accept SSL authentication.
   
2. Add the following properties to your Kafka client configuration:
   
   ```yaml
   security.protocol: SSL
   ssl.keystore.location: /PATH/TO/KEYSTORE.jks
   ssl.keystore.password: YOUR_KEYSTORE_PASSWORD
   ssl.truststore.location: /PATH/TO/TRUSTSTORE.jks
   ssl.truststore.password: YOUR_TRUSTSTORE_PASSWORD
   ```
   
3. Replace the following placeholders:
   
   | Placeholder | Definition |
   | --- | --- |
   | /PATH/TO/KEYSTORE.jks | The file path to your keystore `.jks` file. |
   | YOUR\_KEYSTORE\_PASSWORD | The password to your keystore. |
   | /PATH/TO/TRUSTSTORE.jks | The file path to your truststore `.jks` file. |
   | YOUR\_TRUSTSTORE\_PASSWORD | The password to your truststore. |
   

* * *

## Active Directory Profile

Active Directory connection profiles must be defined in the `ldap` section. Example profile:

```yaml
ldap:
  active_directory_main:
    url:
      - ldap://acme1.ldap.com:389
      - ldaps://acme2.ldap.com:636
    username: Administrator
    password: foobar
    base: dc=acme,dc=com
    ssl:
      cert: /path/to/PEM-encoded-certificate-or-trusted-CA
      trustAll: true
```

| Property name | Description |
| --- | --- |
| **url** _required_ | The URL of the LDAP server to use, in the format `ldap://myserver.example.com:389`. Use the LDAPS protocol, in the format `ldaps://myserver.example.com:636`, for SSL access. You can provide more than one URL for fail-over functionality. |
| **username** _required_ | The username (principal) to use when authenticating with the LDAP server. This is usually the distinguished name of an admin user. For example, `cn=Administrator` or simply `Administrator`. |
| **password** _required_ | The password (credentials) to use when authenticating with the LDAP server. |
| **base** _optional_ | The base DN for all requests. When configured, all distinguished names supplied to and received from LDAP operations are relative to this LDAP path, which can significantly simplify working with a large LDAP tree. |
| **ssl** _optional_ | Options for configuring SSL connections. Contains the following properties: **cert**: Path to a PEM-encoded certificate. This can be either a CA certificate to verify the server's identity, or a client certificate for mutual TLS (mTLS) authentication.; **pem**: Full content of a PEM-encoded client certificate for mTLS authentication. Requires `key`.; **key**: Private key for mutual TLS (mTLS) authentication. Required when using a client certificate in `cert` or `pem`.; **trustAll**: Set to `true` to trust all certificates, including self-signed. Defaults to `false`. |

* * *

## HTTP Profile

The `http` configuration section enables you to configure agent access to internal HTTPS resources. Refer to the following yaml file as an example of an http `config.yml`:

```yaml
http:
  connectTimeout: 5000
  keepAlive: true
  ssl:
    trustAll: false
    verifyHost: true
    cert:
    |
      -----BEGIN CERTIFICATE-----
      MIIF3TCCBMWgAwIBAgIQBlp2+roj8DZRf7VwurC8BjANBgkqhkiG9w0BAQsFADBG
      .....
      -----END CERTIFICATE-----
    key: /path/PEM-encoded-private-key
    pem: /path/PEM-encoded-certificate-or-trusted-CA
```

OPA uses a set of root Certification Authority (CA) certificates from the built-in JRE to validate HTTPS connections by default. For internal HTTPS resources that use self-signed certificates, you can configure the agent to allow access by setting the `ssl.cert` property to the server certificate file path or its PEM-encoded value to enable self-signed certificates. Alternatively, you can set the `ssl.trustAll` property to `true` to trust all server certificates.

The agent also supports mutual TLS (mTLS) for enhanced security. You must specify the client’s private key with the `ssl.key` property and provide the client certificate with the `ssl.pem` property if you plan to use mTLS.

Server certificates typically require the Common Name or Subject Alternate Name to match the target hostname. If a mismatch occurs, disable hostname verification by setting the `ssl.verifyHost` property to `false`. Hostname verification is enabled with this property set to `true` by default.

* * *

## NTLM Profile

Certain HTTP resources require NTLM authentication. This can be done using a NTLM connection profile. Here are some example NTLM profiles:

```yaml
ntlm:
  MyNtlmProfile:
    auth: "username:password@domain/workstation"
    base_url: "http://myntlmhost.com"
    cm_default_max_per_route: 15
    cm_max_total: 100
    verifyHost: true
    trustAll: false

  AnotherNtlmProfile:
    auth: "domain/workstation"
    username: "username"
    password: "password"
    base_url: "http://myntlmhost.com"
    cm_default_max_per_route: 15
    cm_max_total: 100
    verifyHost: true
    trustAll: false
```

The following profile properties are supported:

| Property name | Description |
| --- | --- |
| auth | Full NTLM authentication credentials. This can include username, password, domain, and workstation. **Username** and **password** can be configured separately if they contain special characters like `@` and `/`. |
| username | Username for NTLM authentication |
| password | Password for NTLM authentication |
| base\_url | The base URL for NTLM resources |
| cm\_default\_max\_per\_route | **Optional**. Sets the number of connections per route/host (must be a positive number, default 5) |
| cm\_max\_total | **Optional**. Sets the maximum number of connections (must be a positive number, default 10) |
| http\_connect\_timeout | **Optional**. The timeout in milliseconds used when requesting a connection (must be a positive number, default 10000) |
| http\_connection\_request\_timeout | **Optional**. The timeout in milliseconds until a connection is established (must be a positive number, default 10000) |
| http\_socket\_timeout | **Optional**. The socket timeout in milliseconds, which is the timeout for waiting for data or, put differently, a maximum period inactivity between two consecutive data packets (must be a positive number, default 10000) |
| verifyHost | **Optional**. Specifies whether to enable verification of the host name for SSL/TLS connections (default true) |
| trustAll | **Optional**. Specifies whether trust all certificates for SSL/TLS connections (default false) |

HTTP methods supported for NTLM connections are `GET`, `POST`, `PUT`, `PATCH`, `DELETE` and `HEAD`.

* * *

## Command-line Scripts Profile

This profile allows users to run arbitrary scripts or commands on OPA. The script definition in the config file can have parameters.

When you declare an action, you need to specify the values of the parameters.

An example profile on Unix can look like this:

```yaml
command_line_scripts:
  workday_reports:
    concurrency_limit: 3
    timeout: 30
    scripts:
     copy_file:
       name: Copy file
       command:
         - /bin/cp
         - '{{source_file}}'
         - '{{target_directory}}'
       parameters:
         - { name: source_file }
         - { name: target_directory }

     append_file_to_another:
       name: Append file to another
       command:
         - bash
         - -c
         - cat {{source_file}} >> {{target_file}}
       parameters:
         # Parameter quoting
         - { name: source_file, quote: '"' }
         # Advanced parameter quoting
         - { name: target_file, quote: { start: '"', end: '"', quote: '"', escape_char: \ } }

     generate_report:
       name: Generate report
       command:
         - python
         - /home/user/script.py
         - --from
         - '{{from_date}}'
         # Conditional fragment
         - { value: --to, if: to_date }
         # Conditional fragment
         - { value: '{{to_date}}', if: to_date }
       parameters:
         - { name: from_date }
         - { name: to_date, schema: { optional: true, control_type: select, pick_list: [01/01/2018, 02/02/2018] } }
```

The command-line script profiles are placed in the `command_line_scripts` section in config.yml. Each profile can contain multiple scripts. The profile configuration properties are as follows:

| Property name | Description |
| --- | --- |
| scripts | The scripts hash. The value for each key contains the script profile. |
| concurrency\_limit | **Optional**. Maximum number of concurrently executed scripts. Defaults to 10 when not provided. After reaching the quota, requests are queued. |
| timeout | **Optional**. Maximum duration(seconds) for each script execution. Defaults to 90 seconds when not provided. |

  
The hash key is used as an unique identifier for a script profile. The script configuration properties are as follows:

| Property name | Description |
| --- | --- |
| name | Friendly name for the script that will be displayed in the recipe UI. |
| command | The command invocation array. The value of each item can use [Mustache](https://mustache.github.io/mustache.5.html) template variables to substitute the parameter values. |
| parameters | **Optional**. The parameter array (defaults to an empty array). |

  
The command invocation element configuration can be just a string, but also can contain these properties:

| Property name | Description |
| --- | --- |
| value | The command invocation element value. |
| if | The parameter name. If parameter value is empty, this command invocation element is not taken into account. |

  
The parameter configuration properties are as follows:

| Property name | Description |
| --- | --- |
| name | The parameter name. |
| quote | **Optional**. The rules of parameter quoting (defaults to no rules). |
| schema | **Optional**. The parameter schema. |

  
The quote configuration can just be a string or have properties. The properties are as follows:

| Property name | Description |
| --- | --- |
| start | The opening quote character. |
| end | The closing quote character. |
| quote | The quote character in the parameter value to be escaped. |
| escape\_char | The escape character. |

If the quote configuration is a string, its value is considered as the value of the `start`, `end` and `quote` properties, and the `escape_char` property value is set to '\\' on Unix and '""' on Windows.

  
The parameter schema configuration can have properties as follows:

| Property name | Description |
| --- | --- |
| optional | **Optional**. The optional flag of the parameter (defaults to false). |
| label | **Optional**. Friendly name for the script, that will be displayed in the recipe UI (defaults to the parameter name). |
| control\_type | **Optional**. Can be 'text' or 'select'. If it's 'select', property 'pick\_list' should also be defined. Defaults to 'text'. |
| pick\_list | **Optional**. Values for selecting the parameter value. This property should be defined if property 'control\_type' has value 'select'. |

* * *

## Extensions Profile

Working with Java extensions requires you to define an extensions profile. You need a `server` section to define where the `jar` files are located, and an `extensions` section to create individual profiles for the Java classes. A Java extension will be configured like this.

```yaml
server:
  classpath: ext

extensions:
  security:
    controllerClass: com.mycompany.onprem.SecurityExtension
    secret: HA63A3043AMMMM
```

The **server** parameter configuration property is as follows:

| Property name | Description |
| --- | --- |
| classpath | Specifies the location of user-defined class |

  

Each **extensions** profile configuration properties are as follows:

| Property name | Description |
| --- | --- |
| controllerClass | A required field to inform the OPA which Java class to map the extension to. |
| secret | Optional environment property that is used in the Java class. Multiple properties can be added. |

Find out [how to create a Java extension](/en/on-prem/agents/extension).

* * *

## Server Profile

Server profiles define where OPA assets are located on the on-prem server. Server profiles are located in the `server` section of `config.yml`.

```yaml
server:
  classpath: lib_ext
  staging: staging
```

In this section, we'll cover:

- [Profile properties](#server-profile-properties)
- [Example profile configurations](#example-server-profiles)

### Profile Properties

Server profiles can contain the following properties:

| Property name | Description |
| --- | --- |
| **classpath** _required_ | Defines the directory that contains Java driver or user-defined classes. For example, [jar files](#sap-profile) or [driver classes](#example-jdbc-profile). **Note**: This must be a pre-existing subdirectory in the OPA installation folder. |
| **staging** _optional_ | Defines a staging folder to temporarily store data during loading to the target system. **Note**: This must be a pre-existing subdirectory in the OPA installation folder. If left unspecified, OPA manages the staging folder internally. A file stored in the staging folder is automatically deleted after OPA finishes loading it to the target system. |

### Example Configurations

Let's look at some example profile configurations using the following directory structure. In this example, the on-prem agent is installed in `/opt/workato-agent`:

```yaml
/opt
├── /workato_agent
    ├── /conf
    ├── /bin
    ├── /lib_ext
    ├── /staging
```

The following example defines a `jdbc` directory that contains Java driver classes or user-defined classes:

```yaml
server:
  classpath: lib_ext
```

Next, we'll demonstrate setting the `staging` property. This property defines where the OPA temporarily stores files during loading to the target system.

For example, when executing the SQL Server [Export query result action](/en/connectors/mssql/export-query-result#export-query-result), CSV output will be temporary stored in the `/staging` directory and deleted after the file is loaded:

```yaml
server:
  classpath: lib_ext
  staging: staging
```

---
