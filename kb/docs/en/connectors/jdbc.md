---
url: 'https://docs.workato.com/en/connectors/jdbc.md'
description: >-
  The JDBC connector lets you work with any ANSI-compliant database: insert,
  update, delete, and select rows, run custom SQL, and trigger on new rows.
---

# JDBC

The JDBC connector enables you to connect to any ANSI-compliant database using a JDBC driver and Workato's on-prem agent. You can use it to integrate with systems that support JDBC and SQL.

## Supported databases

The JDBC connector supports any database that complies with ANSI SQL standards and provides a compatible JDBC driver. This includes databases such as **Snowflake** and **SAP HANA**. The database must support binding variables to use some actions such as **INSERT**.

## How to connect to JDBC on Workato

You must use an [on-prem agent](/en/on-prem) to connect to a JDBC source in Workato. The agent enables secure communication between your local database and Workato.

Refer to the [on-prem agent profile](/en/on-prem/agents/connection/profile#example-database-profiles) guide to learn how to connect to a JDBC-compliant database.

Complete the following steps to create a JDBC connection:

1. Provide a unique **Connection name** to identify your JDBC connection.
   
   ![Connect to JDBC](/assets/connect-jdbc.C1_cXxih.png)_Connect to JDBC_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **On-prem group** drop-down menu to select the connection profile you plan to use.
   
4. Enter your **JDBC connection URL**.
   
5. Enter the **JDBC driver class name**.
   
6. Enter your database username in the **User name** field.
   
7. Provide a **Password** if your database requires username/password authentication.
   
8. Configure **Pooling settings** to control the number of open connections to your database.
   
9. Enter the **Schema** if your JDBC driver or database requires a specific schema to access tables and views.
   
10. Expand the **Additional properties for JDBC connection** section to display the advanced configuration fields. Use this section to add authentication keys or other custom JDBC parameters.
    
11. Click **Connect**.
    

### Snowflake connection using key-pair authentication

Use this method to connect to Snowflake through the JDBC connector using an on-prem agent and key pair authentication.

> **PREREQUISITES**
> 
> You must complete the following tasks before you create a Snowflake JDBC connection using key pair authentication:
> 
> - Ensure the on-prem agent is installed and connected. Refer to the [On-prem agent](/en/on-prem/agents) guide for more information.
> - Register your private key with your Snowflake user. Refer to the Snowflake [Configure private key authentication](/en/connectors/snowflake#configure-private-key-authentication) section for more information.

Complete the following steps to configure the JDBC connector with Snowflake key pair authentication:

1. [Download the JDBC driver version 3.22.0](https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/3.22.0/snowflake-jdbc-3.22.0.jar) from the official Maven repository. This is the version currently supported by Workato for Snowflake connections.
   
2. Move the driver file to your on-prem agent's `lib_ext/` folder.
   
3. **Windows**
   
   1. Open the Windows **Start** menu.
      
   2. Go to **All apps > Workato**.
      
   3. Open the **Service Wrapper Configuration** app for the agent you plan to configure.
      
   4. Go to the **Java** tab.
      
   5. Enter the following parameters in the **Java Options** field:
      
      ```shell
      -Dnet.snowflake.jdbc.enableBouncyCastle=TRUE
      --add-opens=java.base/java.nio=ALL-UNNAMED
      ```
      
   6. Click **Apply**.
      
   7. Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.
      
   
   **Linux, Mac, and Docker**
   
   1. Open a terminal and set the working directory to your on-prem agent folder.
      
   2. Open `bin/run.sh` and add the following Java options to the `JAVA_OPTIONS` variable:
      
      ```bash
      JAVA_OPTIONS="${JAVA_OPTIONS:-} -Dnet.snowflake.jdbc.enableBouncyCastle=TRUE --add-opens=java.base/java.nio=ALL-UNNAMED"
      ```
      
   3. Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.
      
   
4. Go to Workato and select the recipe where you plan to connect to Snowflake through JDBC.
   
5. Search for and select **JDBC** on the **New connection** page.
   
6. Provide a name for your connection in the **Connection name** field.
   
   ![Connect to JDBC](/assets/connect-jdbc.C1_cXxih.png)_Connect to JDBC_
   
7. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
8. Use the **On-prem group** drop-down menu to select the connection profile you plan to use.
   
9. Enter the following in the **JDBC connection URL field**:
   
   ```text
   jdbc:snowflake://<your_domain>.snowflakecomputing.com/?warehouse=COMPUTE_WH&db=TESTING_DB&schema=PUBLIC&JDBC_QUERY_RESULT_FORMAT=JSON
   ```
   
   Replace `<your_domain>` with your Snowflake account domain. Note that the `JDBC_QUERY_RESULT_FORMAT=JSON` flag is required.
   
10. Replace `COMPUTE_WH`, `TESTING_DB`, and `PUBLIC` with your warehouse, database, and schema names.
    
11. Enter `net.snowflake.client.jdbc.SnowflakeDriver` in the **JDBC driver class name** field.
    
12. Enter your Snowflake username in the **User name** field.
    
13. Leave the **Password** field blank.
    
14. Expand the **Additional properties for JDBC connection** section.
    
15. Add the `private_key_base64` connection property. This value is the base64-encoded content of your PKCS#8 private key file.
    
    ![Connect to JDBC](/assets/add-jdbc-properties.CSgKchZH.png)_Add additional properties_
    
    You can generate it with the following command:
    
    ```shell
    cat rsa_key.p8 | base64
    ```
    
16. Add the `private_key_pwd` property if your private key is encrypted. Otherwise, omit this property.
    
17. Click **Connect**.
    

## Working with the JDBC connector

### Table and view

The JDBC connector works with all tables and views available to the credentials used to establish the connection. These are available in pick lists in each trigger/action, or you can provide the exact name.

![Table selection from pick list](/assets/table_pick_list.CcR6ntMB.png)_Select a table/view from the pick list_

![Exact table name provided](/assets/table_name_text.DVXvVT29.png)_Provide the exact table/view name in a text field_

The case sensitivity of the name of a table/view depends on your database implementation.

### Single rows and batch rows

The JDBC connector can read or write to your database as a single row or in batches. When using batch triggers/actions, you must provide the batch size you wish to work with. The batch size can be any number between 1 and 100, with 100 being the maximum batch size.

![Batch trigger inputs](/assets/batch_trigger_input.3nQT2LSs.png)_Batch trigger inputs_

Besides the difference in input fields, there is also a difference between the outputs of these two types of operations. A trigger that processes rows one at a time has an output datatree that enables you to map data from that single row.

![Single row output](/assets/single_row_trigger_output.38QSb0oQ.png)_Single row output_

However, a trigger that processes rows in batches outputs them as an array of rows. The Rows datapill indicates that the output is a list containing data for each row in that batch.

![Batch trigger output](/assets/batch_trigger_output.BNjMc3gK.png)_Batch trigger output_

As a result, the output of batch triggers/actions must be handled differently. The output of the trigger can be used in actions with batch operations (like the Salesforce **Create objects in bulk** action) that requires mapping the Rows datapill into the source list. Learn how to [work with lists in Workato](/en/features/list-management#using-datapills-from-lists).

![Using batch trigger output](/assets/using_batch_output.BOkwYCVP.png)_Using batch trigger output_

### WHERE condition

This input field filters and identifies rows to perform an action on. You can use the WHERE condition in multiple triggers and actions in the following ways:

- filter rows to be picked up in triggers
- filter rows in **Select rows** action
- filter rows to be deleted in **Delete rows** action

This clause is used as a `WHERE` statement in each request. It should follow basic SQL syntax.

#### Simple statements

Enclose string values in single quotes (`''`). Columns used must exist in the table/view.

A simple `WHERE` condition to filter rows based on values in a single column looks like this.

```sql
currency = 'USD'
```

If used in a **Select rows** action, this `WHERE` condition returns all rows that have the value 'USD' in the `currency` column. Remember to wrap datapills with single quotes in your inputs.

![Using datapills in WHERE condition](/assets/use_datapill_in_where.CcqcM98j.png)_Using datapills in `WHERE` condition_

Enclose column names with spaces in double quotes (`""`) or square brackets (`[]`). For example, to use **currency code** as an identifier, enclose it in brackets.

```sql
[currency code] = 'USD'
```

![WHERE condition with enclosed identifier](/assets/where-condition-with-enclosed-identifier.ESqH1ukn.png)_`WHERE` condition with enclosed identifier_

#### Complex statements

Your `WHERE` condition can also contain subqueries. The following example selects inactive employees from the `compensation` table.

```sql
id in (select compensation_id from users where active = 0)
```

When used in a **Select rows** action, this selects all rows in the `compensation` table related to users who are no longer active (`active = 0`).

![Using subquery in WHERE condition](/assets/subquery-in-where-condition.vK4FaIcD.png)_Using subquery in WHERE condition_

---
