---
url: 'https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains.md'
description: >-
  Connect Microsoft Dynamics Great Plains to Workato to automate business
  management and ERP workflows for small and mid-sized organizations.
---

# Microsoft Dynamics Great Plains

[Microsoft Dynamics Great Plains](https://learn.microsoft.com/en-us/dynamics-gp/) is a business management solution for small and mid-sized organizations that automates and streamlines business processes and helps you manage your business.

## Prerequisites

Complete the following steps to enable integration between Microsoft Dynamics Great Plains (GP) and Workato:

1. Install Microsoft Dynamics GP and SQL Server. Ensure that Dynamics GP and its associated SQL Server database are installed and operational within your network environment.
   
2. Set up the Workato [on-prem agent](/en/on-prem/agents) if your Dynamics GP instance is hosted on-premise. Ensure the agent is on the same server that hosts both eConnect and the SQL Server running the Dynamics GP database to minimize configuration complexity and improve performance. Additionally, ensure the agent has network access to the SQL Server and the necessary eConnect libraries.
   
3. Create an SQL Server login for a Windows domain user and assign it to the `DYNGRP` database role within the **DYNAMICS** database to enable the necessary read and write access.
   
4. Optional (recommended). Install eConnect Libraries using the **Additional Products** section of the Dynamics GP installer. You do not need to install the full eConnect Runtime module, only the eConnect libraries.
   
5. Install the eConnect Integration Service. This service allows communication between Workato and Dynamics GP through eConnect APIs, which facilitates transactions such as creating and updating records.
   

> **ADVANCED AND UNSUPPORTED USE CASES**
> 
> eConnect APIs do not support all GP entities. Use the [SQL Server](/en/connectors/mssql/introduction) connector to query or write directly to the backend database for modules not exposed through eConnect, such as custom tables and certain third-party add-ons.

> **ECONNECT SCHEMAS**
> 
> Refer to the eConnect schema [documentation](https://learn.microsoft.com/en-us/previous-versions/dynamicsgp/developer/cc508691\(v=msdn.10\)) for more information about table structures and relationships.

### Add an HTTP endpoint to eConnect

The **Microsoft Dynamics Great Plains** connector requires an HTTP endpoint in eConnect to access your GP database.

Complete the following steps to connect Workato to the GP database:

1. Stop the eConnect service if it is currently running.
   
2. Go to the eConnect `Service` folder. The path to the `Service` folder varies based on your installation location and version. For example: `C:\Program Files\Microsoft Dynamics\eConnect12\Service`.
   
3. Open the `Microsoft.Dynamics.GP.eConnect.Service.exe.config` file.
   
4. Add a new `<basicHttpBinding>` element to the `<bindings>` element:
   
   ```xml
   <basicHttpBinding>
   	<binding name="eConnectBasicHttpConfig" closeTimeout="00:10:00"
   		sendTimeout="00:10:00" allowCookies="false" maxBufferSize="2147483647"
   		maxBufferPoolSize="2147483647" maxReceivedMessageSize="2147483647">
   		<security mode="TransportCredentialOnly">
   			<transport clientCredentialType="Basic" />
   		</security>
   	</binding>
   </basicHttpBinding>
   ```
   
5. Add a new `<endpoint>` element to the `Microsoft.Dynamics.GP.eConnect.service <service>` element:
   
   ```xml
   <endpoint address="EntityOperations" binding="basicHttpBinding"
   	bindingConfiguration="eConnectBasicHttpConfig" name="eConnectServiceBasicHttpEndpoint"
   	contract="Microsoft.Dynamics.GP.eConnect.IEconnect">
   	<identity>
   		<dns value="localhost" />
   	</identity>
   </endpoint>
   ```
   
6. Add a new `<add>` element to the `<baseAddresses>` element:
   
   ```xml
   <add baseAddress="http://localhost/Microsoft/Dynamics/GP/eConnect/" />
   ```
   
7. Save your changes to the configuration file.
   
8. Start the eConnect service.
   

## How to connect to Microsoft Dynamics Great Plains

Connecting to the Microsoft Dynamics Great Plains involves the following steps:

1. [Download the Microsoft Dynamics Great Plains connector from the community](#community-download)
2. [Complete setup in Workato](#workato-setup)

> **MICROSOFT MFA ENFORCEMENT**
> 
> Microsoft is rolling out mandatory multifactor authentication (MFA) gradually to different applications and accounts in phases. This enforcement continues throughout 2025 and beyond. Refer to the Microsoft [Mandatory multifactor authentication for Azure and admin portals](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication?tabs=dotnet) documentation for more information.
> 
> We strongly recommend enabling MFA now for all Microsoft accounts used with Workato to avoid service disruptions from short-notice enforcement changes.
> 
> Complete the following steps to maintain uninterrupted service:
> 
> 1. Enable MFA for your Microsoft organization following the Microsoft MFA setup guide. Refer to [Set up multifactor authentication for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide) for more information.
>    
> 2. Reconnect your Microsoft connection in Workato.
>    
> 3. Complete the OAuth flow with MFA when prompted.
>    
> 4. Test your recipes to ensure they work with the updated connection.
>    

### Download Microsoft Dynamics Great Plains connector from the community

Complete the following steps to install the Microsoft Dynamics Great Plains connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

> **DATA INTEGRITY**
> 
> Be cautious when interacting directly with Microsoft Dynamics GP tables to avoid compromising data integrity.

### Complete setup in Workato

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Microsoft Dynamics Great Plains** as your connection in the **New Connection** page.
   
3. Provide a **Connection name** that identifies which Microsoft Dynamics Great Plains instance Workato is connected to. ![Microsoft Dynamics Great Plains Connection](/assets/connection.agIMKrF9.png)_Microsoft Dynamics Great Plains Connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select your **Connection type** from the drop-down menu.
   
6. Provide the Windows domain user's **Username** and **Password**. Ensure the domain user has access to the Microsoft Dynamics GP SQL Server database machine. The user name must be configured in the SQL Server database and granted the `DYNGRP` security role.
   
7. Provide the **Econnect service endpoint**, which you can find in your Econnect WSDL or infer from your Econnect WSDL endpoint. For example, if your WSDL endpoint is `http://10.11.12.1/Microsoft/Dynamics/GP/eConnect/mex?singleWsdl`, then your Econnect Service URL is likely `http://10.11.12.1/Microsoft/Dynamics/GP/eConnect/EntityOperations`.
   
   > **ON-PREM CONNECTIVITY**
   > 
   > Set the **Econnect service endpoint** URL to the internal domain name (localhost) or internal IP address for on-prem connections.
   
8. Provide the **DB connection string** for all actions. This will be used if the DB connection string is not provided in the action itself, for example: `Integrated Security=true;Persist Security Info=false;Database=WORKATO;Data Source=EC2AMAZ-DEMO\SQLEXPRESS`
   
9. Click **Connect** to establish the connection.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/apply-document-to-invoice-action.md
description: >-
  The Apply document to invoice action applies a credit memo, return or cash
  receipt to an invoice, debit memo, finance charge, service/repair or warranty
  in Microsoft Dynamics GP.
---

# Microsoft Dynamics Great Plains - Apply document to invoice action

The **Apply document to invoice** action applies a credit memo, return or cash receipt to an invoice, debit memo, finance charge, service/repair or warranty in Microsoft Dynamics GP.

## Input

| Input field | Description |
| --- | --- |
| Apply from - document type | Select the source document type you plan to apply to the target document. |
| Apply to - document type | Select the target document type you plan to apply the source document to. |
| Apply to - document number | Provide the target document number you plan to apply the source document to. |
| Apply from - document number | Provide the source document number you plan to apply to the target document. |
| Amount to apply | Enter an amount for the invoice. |
| DB connection string | Enter the database connection string to use for the action. |
| Discount taken | Specify the discount taken, if applicable. |
| Write-off amount | Specify the write-off amount, if applicable. |
| Apply date | Select the apply date from the calendar. |
| Apply posting date | Select the posting date from the calendar. |

## Output

| Output field | Description |
| --- | --- |
| Create entity result | The status of the apply action. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/create-record-action.md
description: The Create record action creates a new record in Microsoft Dynamics GP.
---

# Microsoft Dynamics Great Plains - Create record action

The **Create record** action creates a new record in Microsoft Dynamics GP. Select the object to create to generate the relevant fields for that object. For example, the following are the input and output schemas if you select **Post bank deposit** as the object:

## Input

| Input field | Description |
| --- | --- |
| DB connection string | Enter the database connection string to use for the action. |
| Checkbook ID | Provide the ID of the checkbook for the bank deposit. |
| Deposit number | Provide the deposit number for posting. |
| Requester transaction | Select whether to populate the requester shadow table. |
| User ID for posting | Provide the user ID for posting. |
| User-defined fields 1-5 | Provide additional information in these fields, which are for developer use only. |

## Output

| Output field | Description |
| --- | --- |
| Create entity result | The status of the **Create record** action. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/create-record-batch-action.md
description: >-
  The Create records in batches action creates records in Microsoft Dynamics GP
  in batches.
---

# Microsoft Dynamics Great Plains - Create records in batches action

The **Create records in batches** action creates records in Microsoft Dynamics GP in batches. This action requires a list of records as an input. For example, the following are the input and output schemas if you select **Cash receipt** as the object:

## Input

| Input field | Description |
| --- | --- |
| DB connection string | Enter the database connection string to use for the action. |
| Customer number | Enter the unique identifier of the customer making the payment. |
| Document number | Provide the unique reference number for the cash receipt transaction. |
| Document date | Select the creation date for the cash receipt document. |
| Transaction amount | Enter the total amount received from the customer. |
| GL posting date | Enter the date to post the transaction to the general ledger. |
| Batch number | Specify the batch number to assign this cash receipt to. |
| Cash receipt type | Select the type of receipt, such as cash, check, or credit card. |
| Checkbook ID | Enter the ID of the checkbook to deposit the receipt in. |
| Check number or credit card number | Provide the check number or credit card number used for the payment. |
| Credit card ID | Enter the identifier for the credit card, if applicable. |
| Transaction description | Add a brief description or note about the cash receipt transaction. |
| Last user to edit | Specify the username of the last person who modified this transaction. |
| Checkbook ID for the batch | Provide a checkbook ID to associate with the batch, if different from the transaction's `Checkbook ID`. |
| Currency ID | Select the currency used for this transaction. |
| Exchange rate | Enter the applicable exchange rate if using a foreign currency. |
| Rate type ID | Specify the rate type ID used to calculate the exchange rate. |
| Expiration date | Provide the expiration date for the exchange rate. |
| Exchange ID description | Add a description for the exchange rate ID, if applicable. |
| Exchange rate source | Specify the source of the exchange rate. |
| Rate expiration | Enter the date or time to no longer use the exchange rate. |
| Days to increment | Set the number of days to increment for calculating due or expiration dates. |
| Rate variance | Define the allowable variation in exchange rate for the transaction. |
| Transaction date | Enter the actual date when the transaction occurred. |
| Rate calculation method | Select the method for exchange rate calculation. |
| Previous day’s quotas | Specify the acceptable range or quotas for the previous day’s exchange rate. |
| Date limits | Set constraints on the transaction date, if required. |
| Time 1 | Provide a timestamp or time reference for posting or workflow purposes. |
| Flag to autocreate distributions | Select whether to automatically generate distribution entries for the transaction. |
| Requester transactions | Select whether to populate the requester shadow table. |
| User-defined fields 1–5 | Use these fields to capture any additional custom information needed for your use case. |

## Output

| Output field | Description |
| --- | --- |
| Create entity result | The status of the **Create records in batches** action. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/get-next-document-number-action.md
description: >-
  The Get next document number action retrieves the next document in Microsoft
  Dynamics GP.
---

# Microsoft Dynamics Great Plains - Get next document number action

The **Get next document number** action retrieves the next document in Microsoft Dynamics GP.

## Input

| Input field | Description |
| --- | --- |
| Document type | Select the document type to retrieve, for example, `General Ledger`. |
| DB connection string | Enter the database connection string to use for the action. |
| Increase/decrease number | Select whether to increase or decrease the document number. This field defaults to `Increment` when left empty. |

## Output

| Output field | Description |
| --- | --- |
| Document number | The next document number matching the specified criteria. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/search-records-using-query-action.md
description: >-
  The Search records using query action searches records in Microsoft Dynamics
  GP.
---

# Microsoft Dynamics Great Plains - Search records using query action

The **Search records using query** action searches records in Microsoft Dynamics GP. Datapill introspection for search queries is only available when `DB connection string` is defined in your [connection settings](/en/connectors/microsoft-dynamics-great-plains#connection-setup) and at least one record of the selected object type exists in your GP instance. Workato generates datapills based on the first record retrieved from your GP. You can use the `Output schema (Override)` field to manually define the output schema.

## Input

| Input field | Description |
| --- | --- |
| Select the object to search for | Select the object type to search for. |
| DB connection string | Enter the database connection string to use for the action. |
| Where clause | Enter a where clause to filter the query, such as `CUSTNMBR = AMERICAN0001`. |
| Row count limit | Specifies the number of records to return in the response. |
| Output type | Select the response structure for the query. This field defaults to `Complete document` when left empty. |
| Output schema (override) | Manually define or override the default output schema for this action. |

## Output

This action returns the array of objects. You can manually define the structure using the `output schema (Override)` field.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/update-record-action.md
description: The Update record action updates a new record in Microsoft Dynamics GP.
---

# Microsoft Dynamics Great Plains - Update record action

The **Update record** action updates a new record in Microsoft Dynamics GP. Select the object to update to generate the relevant fields for that object. For example, the following are the input and output schemas if you select **Country code** as the object:

## Input

| Input field | Description |
| --- | --- |
| DB connection string | Enter the database connection string to use for the action. |
| Country code | Enter the standard country code representing the country. |
| Country code description | Provide a short description or name of the country corresponding to the country code. |
| EU member | Indicate whether the country is a member of the European Union. |
| Update if exists | Indicate whether to update the existing record if the provided country code is already in use. |
| Requester transaction | Select whether to populate the requester shadow table. |
| User-defined field 1-5 | Use these fields to capture any additional custom information needed for your use case. |

## Output

| Output field | Description |
| --- | --- |
| Update entity result | The status of the **Update record** action. |

---
