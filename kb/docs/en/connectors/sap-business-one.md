---
url: 'https://docs.workato.com/en/connectors/sap-business-one.md'
description: >-
  The SAP Business One connector lets you automate ERP workflows: create,
  update, search, and delete records, run batch operations, and trigger on
  changes.
---

# SAP Business One

[SAP Business One](https://www.sap.com/sea/products/erp/business-one.html) is an enterprise resource planning (ERP) solution designed for small and medium-sized businesses. It centralizes key business functions such as financial management, sales, inventory, and customer relationship management, enabling streamlined operations and improved decision-making.

This connector supports connecting through on-prem agents to support the SAP Business One deployment behind the company firewall.

## Prerequisites

To establish a connection to SAP Business One you must have the following:

- SAP Business One Version 10.0 or above.
- _Alternatively_, this connector is compatible with older versions of SAP Business One starting at version 9.1 and above if the instance uses SAP HANA as the underlying database.
- An active SAP Business One user account.

Additionally, to use this connector, the SAP Business One Service Layer must be installed and set up in SAP Business One.

### User accounts

You can create user accounts in SAP Business One by navigating to **Administration > Setup >General > Users**.

Refer to the official [SAP help documentation](https://help.sap.com/docs/SAP_BUSINESS_ONE/68a2e87fb29941b5bf959a184d9c6727/4506da3dd8696c30e10000000a114a6b.html) for detailed steps on creating user accounts. ![User accounts](/assets/user-accounts.hpbHqfBm.png)_User accounts_

## Connection setup

Establishing a connection to SAP Business One in Workato consists of the following steps:

- [Connect to on-premise SAP systems](#on-prem-connect)
- [Complete setup in Workato](#workato-setup)

### Connect to on-premise SAP systems

Complete the following steps to connect to the on-premise SAP system using an [on-prem agent](/en/on-prem):

1. Navigate to the OPA installation file structure that allows you to grant agent access to [HTTP resources](/en/on-prem/agents/connection/profile#http-profile).
   
2. Navigate to the **config** directory and configure your `config.yml` file.
   
3. For development environments, you can test your connection by maintaining the following entry in the `config.yml` file located in the OPA installation directory `conf` folder:
   
   ```yaml
   http:
     trustAll: true
     verifyHost: false
   ```
   
4. Alternatively, if you plan to connect to the on-premise SAP systems without an on-prem agent, then you can allow traffic from Workato by allowlisting these [IP addresses](/en/security/ip-allowlists#traffic-from-workato) for HTTPS port in the inbound rules of the SAP server's firewall.
   

### Complete setup in Workato

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `SAP Business One` as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select a **Connection type** from the drop-down. Choose an on-prem agent if your SAP instance is running in a network that does not allow direct connection. Before you connect, ensure you have an active on-prem agent. Refer to the [On-prem connectivity](/en/on-prem) guide for more information.
   
   If you select `Cloud`, requests are sent directly from Workato's servers.
   
6. Provide a **Server name**. This can be either a DNS name or an IP address. If present, this describes a direct connection to the SAP host. It can be in the format `xx.xx.xx.xx`. If you choose to provide an IP address, use the IP address of the SAP Business One application you are directly connecting to.
   
7. Provide the SAP Business One service layer port in the **Port** field. This is typically `50000`.
   
8. Provide the Company database in the SAP Business One application that you plan to connect with in the **Company DB** field.
   
9. Supply the provisioned SAP user's name in the **User name** field.
   
10. Enter your SAP user password in the **Password** field.
    
11. Click **Connect**.
    
    ![Connection setup](/assets/connection-setup.DiWt_scZ.png)_Connection setup_

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-business-one/new-updated-record-trigger.md
description: >-
  The New/updated record trigger in the SAP Business One connector runs your
  recipe when a selected object, such as an order, is created or updated.
---

# SAP Business One - New/updated record trigger

The **New/updated record** trigger runs the recipe when you create or update a specific SAP Business One object, such as an order.

![SAP Business One - New/Updated record trigger](/assets/new-update-record-trigger.PNIT8OGs.png)_SAP Business One New/updated record trigger_

## Input

| Input Field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for new events. Defaults to every 10 minutes if left blank. |
| Object | Select a SAP Business One object from the drop-down list. |
| Object key | Select the ID that the recipe uses to identify the monitored object. |
| When first started, this recipe should pick up events from | Objects created after this date and time will be processed in the trigger. If left blank, the trigger will pick up entries created one hour before the recipe is first started. |
| Set trigger condition | Defines further guidelines added to a specific trigger to filter the type of trigger events selected for processing. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-business-one/create-record-action.md
description: >-
  The Create record action in the SAP Business One connector lets you create a
  record of a selected object in SAP Business One.
---

# SAP Business One - Create record action

The **Create record** action enables you to create a record in SAP Business One.

![SAP Business One - Create record action](/assets/create-record-action.BxGMTfJK.png)_SAP Business One - Create record action_

## Input

| Input Field | Description |
| --- | --- |
| Object | Specify the object you plan to create. Fields dynamically load based on the selected object. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-business-one/create-records-batch-action.md
description: >-
  The Create records batch action in the SAP Business One connector lets you
  create multiple records of a selected object in a single batch.
---

# SAP Business One - Create records batch action

The **Create records** batch action enables you to create multiple records in SAP Business One.

![SAP Business One - Create records batch action](/assets/create-record-batch-action.pK8Y89iw.png)_SAP Business One Create records batch action_

## Input

| Input Field | Description |
| --- | --- |
| Object | Specify the object you plan to create. Fields load dynamically based on the object you select. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---
