---
url: 'https://docs.workato.com/en/connectors/oracle/introduction.md'
description: >-
  Set up and connect Oracle in Workato, including the database host, port, user
  credentials, and SID or service name prerequisites.
---

# Connect Oracle to Workato

This guide shows you how to connect an Oracle database to Workato. Complete the following steps:

- [Step 1: Set up an Oracle database user](#step-1-set-up-an-oracle-database-user).
- [Step 2: Connect Oracle to Workato](#step-2-connect-oracle-to-workato).

## Prerequisites

Ensure you have the following before you begin:

- An Oracle database user with the required privileges.
- The database host and port.
- A service name, SID, or TNS definition provided by your DBA.
- An active On-prem agent if your database runs in a private network.

## Step 1: Set up an Oracle database user

At a minimum, the database user account must have the `SELECT` permission for the database specified in the [connection settings](#step-2-connect-oracle-to-workato). Refer to the following example to set up permissions.

> **Click here to find out how to set up permissions**
> 
> If we are trying to connect to a named schema (`HR_PROD`) in an Oracle instance, using a new database user `WORKATO`, the following example queries can be used.
> 
> First, create a new user dedicated to integration use cases with Workato.
> 
> ```
> CREATE USER WORKATO IDENTIFIED BY password
> ```
> 
> Next, grant `CONNECT` to this user.
> 
> ```
> GRANT CONNECT TO WORKATO;
> ```
> 
> This allows the user to have login access to the Oracle instance. However, this user does not have access to any tables.
> 
> The next step is to grant access to `SUPPLIER` table in the `HR_PROD` schema. In this example, we only wish to grant `SELECT` and `INSERT` permissions.
> 
> ```
> GRANT SELECT,INSERT ON HR_PROD.SUPPLIER TO WORKATO;
> ```
> 
> Finally, check that this user has the necessary permissions. Run a query to see all grants.
> 
> ```
> SELECT * FROM DBA_ROLE_PRIVS WHERE GRANTEE = 'WORKATO';
> SELECT * FROM DBA_TAB_PRIVS WHERE GRANTEE = 'WORKATO';
> ```
> 
> This should return the following minimum permission to create a Oracle connection on Workato.
> 
> ```
> +---------+--------------+--------------+--------------+
> | GRANTEE | GRANTED_ROLE | ADMIN_OPTION | DEFAULT_ROLE |
> +---------+--------------+--------------+--------------+
> | WORKATO | CONNECT      | NO           | YES          |
> +---------+--------------+--------------+--------------+>
> 
> +---------+---------+------------+---------+-----------+-----------+-----------+
> | GRANTEE | OWNER   | TABLE_NAME | GRANTOR | PRIVILEGE | GRANTABLE | HIERARCHY |
> +---------+---------+------------+---------+-----------+-----------+-----------+
> | WORKATO | HR_PROD | SUPPLIER   | ROOT    | SELECT    | NO        | NO        |
> | WORKATO | HR_PROD | SUPPLIER   | ROOT    | INSERT    | NO        | NO        |
> +---------+---------+------------+---------+-----------+-----------+-----------+
> 3 rows in set (0.61 sec)
> ```

## Step 2: Connect Oracle to Workato

Workato supports the following Oracle connection types:

- [Cloud connection](#oracle-cloud-connection): Use this option when your Oracle database is accessible over the public internet.
- [On-prem agent connection](#oracle-opa-connection): Use this option when your Oracle database runs in a private network and requires an On-prem agent (OPA) to establish connectivity.

### Cloud connection

Complete the following steps to connect to Oracle using a Cloud connection:

1. Click **Create > Connection**.
   
2. Search for and select **Oracle** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Cloud** in the **Connection type** field.
   
6. Enter the database host address in the **Database host** field.
   
7. Enter the number of the **Database port** the server is running on, typically `1521`.
   
8. Enter the database user's **User name** from [Step 1](#step-1-set-up-an-oracle-database-user).
   
9. Enter the database user's **Password**.
   
10. Optional. Enter the database schema in the **Schema** field.
    
11. Optional. Expand [Advanced settings](#configure-advanced-settings) to configure additional connection options.
    
12. Optional. Expand **SSL settings** to connect over TLS (TCPS) or mutual TLS (mTLS):
    
    | Field | Description |
    | --- | --- |
    | Server certificate | Provide the X.509 CA certificate of the database server in `.pem` format, such as the Amazon RDS certificate bundle. If left blank, the server certificate must be issued by a publicly trusted certificate authority. |
    | SSL certificate | Provide the X.509 client certificate in `.pem` format for mTLS. Requires the **SSL certificate key**. |
    | SSL certificate key | Provide the RSA client key in `.pem` format. Requires the **SSL certificate**. |
    | Trust all | Specify whether the client should trust any certificate chain. Self-signed server certificates are supported. Workato ignores the **Server certificate** if you enable this setting. |
    | Verify host | Specify whether to match the name in the server certificate against the database host. Enabled by default unless **Trust all** is enabled. |
    
    Workato connects over TLS if you set any SSL field and doesn't fall back to an unencrypted connection if TLS fails. Leave all SSL fields blank to connect without TLS. Enter the port of the database's TCPS listener in the **Database port** field when you use TLS.
    
    > **ORACLE AUTONOMOUS DATABASE**
    > 
    > Provide the **SSL certificate** and **SSL certificate key** and leave **Server certificate** blank to connect to Oracle Autonomous Database over mTLS. Its server certificate chains to a public certificate authority.
    
13. Click **Connect**.
    

### On-prem agent connection

Use an on-prem agent connection when your Oracle database is located in a private network that can't be accessed directly from the internet.

Complete the following steps to connect to Oracle using an on-prem agent (OPA):

1. Click **Create > Connection**.
   
2. Search for and select **Oracle** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select your **on-prem group** in the **Connection type** field.
   
6. Select a **Database type**. Available options include **Service name**, **SID**, and **TNS**.
   
   SID and TNS database types require On-prem agent version 27.1 or later.
   
   Refer to the [Database types](#database-type-reference) section for more information.
   
7. Provide the following fields based on the **Database type** selected:
   
   **Service name**
   
   Enter the Oracle service name for the database in the **Service name** field.
   
   **SID**
   
   Enter the Oracle system identifier (SID) for the database instance in the **SID** field.
   
   **TNS**
   
   Enter the full Oracle Net connection descriptor from your `tnsnames.ora` configuration in the **TNS Definition** field.
   
8. Complete the following fields if you selected **Service name** or **SID** as the **Database type**:
   
   1. Enter the database host address in the **Database host** field.
      
   2. Enter the number of the **Database port** the server is running on, typically `1521`.
      
9. Enter the database user's **User name** from [Step 1](#step-1-set-up-an-oracle-database-user).
   
10. Enter the database user's **Password**.
    
11. Optional. Enter the database schema in the **Schema** field.
    
12. Optional. Expand [Advanced settings](#configure-advanced-settings) to configure additional connection options.
    
13. Optional. Expand **Pooling settings** to configure Oracle database connection pooling.
    
14. Optional. Expand **Additional properties for Oracle connection** to add custom Oracle connection parameters.
    
15. Click **Connect**.
    

## Database types

Workato displays the **Database type** field only when you select an **On-prem group** in the **Connection type** field while creating an Oracle connection.

Refer to [Step 2: Connect Oracle to Workato](#step-2-connect-oracle-to-workato) for instructions on configuring the connection.

Select one of the following **Database type** options when connecting through an On-prem agent (OPA).

### Service name

Use **Service name** to connect to a database service within an Oracle instance. For example, `ORCLPDB1`.

> **ORACLE 12C+ PDB ENVIRONMENTS**
> 
> We recommend using **Service name** instead of **SID** in Oracle 12c and later environments that use multitenant architecture (CDB/PDB).
> 
> In these environments:
> 
> - **SID** connections may connect to the **CDB root container**
> - **Service name** connections may connect to a specific **pluggable database (PDB)**
> 
> If a database user exists in a PDB, authentication can fail when connecting through the CDB root even if the username and password are correct.
> 
> Use **Service name** to ensure the connection targets the correct PDB.

Service names have the following characteristics:

- Map to database services registered with the Oracle listener
- Support Real Application Clusters and load balancing
- Identify logical database services rather than specific instances

Use this option for most modern Oracle deployments.

### SID

Use **SID** (System Identifier) to connect to a specific Oracle database instance. For example, `ORCL`.

SIDs have the following characteristics:

- Identify a single Oracle database instance
- Do not support load balancing
- Commonly appear in older Oracle deployments

Use this option when your DBA provides an SID instead of a service name.

### TNS

Use **TNS** when you have a full Oracle Net connect descriptor.

TNS definitions have the following characteristics:

- Reference connection entries defined in the `tnsnames.ora` file
- Abstract the underlying connection details
- May internally use a **SID** or **Service name**
- Support advanced configurations such as load balancing and high availability

Enter the full TNS descriptor in the **TNS definition** field. For example:

```text
(DESCRIPTION=
(ADDRESS=(PROTOCOL=TCP)(HOST=db.example.com)(PORT=1521))
(CONNECT_DATA=
(SERVICE_NAME=ORCLPDB1)
)
)
```

## Configure advanced settings

Oracle connectors have the following advanced settings:

> **TIP**
> 
> While this step is optional, we strongly recommend defining the **Use improved datetime handling** settings. These settings allow you to set your local database timezone and improve datetime timezone conversion during insertion.

| Field | Description |
| --- | --- |
| **Use improved datetime handling** | Overrides the default database timezone of `UTC`. If enabled, `date` and `timestamp` data types are converted during insertion to the **Database timezone** you provide. **Note**: This setting only affects [Insert actions](/connectors/oracle/insert.html). |
| **Database timezone** | Defines the local timezone of your database and requires \*\*Use improved datetime handling\*\* to be enabled. If not defined, Workato uses `UTC` as the timezone. Additionally, if \*\*Use improved datetime handling\*\* is not enabled, this setting is not respected. **Note**: This setting only affects [Insert actions](/connectors/oracle/insert.html). |

Let's look at some examples of how these settings affect how `datetime` data is handled in [Insert actions](/en/connectors/oracle/insert).

**All examples assume the Database timezone is set to UTC -04:00 (Eastern Standard Time).**

| Source value | Destination column | Destination value |
| --- | --- | --- |
| `2020-12-02 10:00:00` Source value doesn't have a timezone component | NOT timezone capable (DATE or TIMESTAMP) | `2020-12-02 10:00:00` Value is inserted as-is, as conversion is unnecessary |
| `2020-12-02 10:00:00` Source value doesn't have a timezone component | Timezone capable (TIMESTAMP WITH TIME ZONE) | `2020-12-02 10:00:00 -04:00` Value has **Database timezone** applied |
| `2020-12-02 10:00:00 -07:00` Source value has a timezone component, but it's not the same as the **Database timezone** (`UTC -04:00`) | NOT timezone capable (DATE or TIMESTAMP) | `2020-12-02 13:00:00` Value is converted using the **Database timezone** |
| `2020-12-02 10:00:00 -07:00` Source value has a timezone component, but it's not the same as the **Database timezone** (`UTC -04:00`) | Timezone capable (TIMESTAMP WITH TIME ZONE) | `2020-12-02 13:00:00 -04:00` Value is converted using the **Database timezone** |

## What's next?

Learn more about the Oracle connector:

- [Working with Oracle](/en/connectors/oracle/working-with-the-oracle-connector)
- [Best practices](/en/connectors/databases/best-practices)
- [Use cases](/en/connectors/database-common-use-cases)
- [Troubleshooting](/en/connectors/oracle/trouble-shooting)

---
