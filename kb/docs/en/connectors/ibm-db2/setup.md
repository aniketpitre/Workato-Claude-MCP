---
url: 'https://docs.workato.com/en/connectors/ibm-db2/setup.md'
description: >-
  Set up and connect IBM Db2 in Workato using an on-prem agent, including
  deploying the database, the JDBC driver, and connection profile prerequisites.
---

# IBM Db2 Connection setup

## Setup prerequisites

To connect to IBM Db2, ensure that you first complete the following steps:

1. Deploy an IBM Db2 instance.
2. Create a database user with both **read** and **write** permissions for the target database.
3. Configure a Workato on-prem agent (OPA), version 2.11.0 or newer. It must have network access to the Db2 instance.
4. Downloaded the [IBM Db2 Driver](https://mvnrepository.com/artifact/com.ibm.db2.jcc/db2jcc/db2jcc4) (db2jcc4.jar) to the same machine that runs the OPA.
5. Allow [Workato IPs](/en/security/ip-allowlists) to connect to your OPA.

## Step 1: Configure the on-prem agent

Configure the IBM Db2 [database profile](/en/on-prem/agents/connection/profile#database-profile) in the OPA.

```yaml
database:
  db2ConnectionProfile: # name of the connection profile
  url: jdbc:db2://uri:port/database_name
  driverClass: com.ibm.db2.jcc.DB2Driver
  username: db2instl
  password: your_password

  # SSL configuration (skip if not using SSL)
  sslConnection: true
  sslTrustStoreLocation: C:\path\to\truststore.jks # required if `sslConnection` is true
  sslTrustStorePassword: 12345678 # SSL Trust Store Password
```

## Step 2: Complete the setup in Workato

Enter the following connection field information in Workato:

<dl><dt>Connection name</dt><dd>Required field</dd><dd>The name of this Db2 Connection</dd></dl>

<dl><dt>Location</dt><dd>Required field</dd><dd>The project to save this Db2 Connection</dd></dl>

<dl><dt>On-prem connection profile</dt><dd>Required field</dd><dd>The name of the database profile in your on-prem agent configuration (e.g. db2ConnectionProfile)</dd></dl>

<dl><dt>Schema</dt><dd>Optional field</dd><dd>The name of the database schema to use. Leave this blank to use the default.</dd></dl>

<dl><dt>Is this app in a private network?</dt><dd>Required field</dd><dd>Select the on-prem gateway containing the on-prem agent(s) which connect to your Db2 instance</dd></dl>

---
