---
url: 'https://docs.workato.com/en/agentic/agentx-support/data-tables.md'
description: >-
  Create AgentX Support data tables to store structured information the AI agent
  references in flows to respond to customer queries.
---

# AgentX Support - Data tables

Data tables allow you to store structured information that the AI agent can reference in flows to dynamically respond to customer queries. You can create data tables directly in AgentX Support or import them from Google Sheets.

> **FEATURE AVAILABILITY**
> 
> This feature requires data table access in your AgentX Support account.

## Create a data table

Complete the following steps to create a data table:

1. Go to **Advanced > Data Table**.
   
2. Click **New Data Table**.
   
3. Enter a name for the data table in the **Name** field. For example, `product-information`.
   
   ![Create the data table](/assets/create-data-table.CItjxEEU.png)_Create the data table_
   
4. Click **Submit** to create the data table.
   
5. Click **Add Column** and enter a column name.
   
   ![Add a column](/assets/add-column.B0DINUN2.png)_Add a column_
   
6. Click **Add**.
   
7. Continue adding columns to your data table.
   
8. Click **Add Row** to add rows to the data table.
   
   ![Add rows](/assets/add-row.BabaLkZC.png)_Add rows_
   
9. Fill in the rows.
   
   ![Fill in the data table](/assets/data-table-complete.Bjq094ti.png)_Fill in the data table_
   
10. Click **Save**.
    

## Import a Google Sheet as a data table

You can maintain your data table in an external Google Sheet shared within your organization and teams and import the sheet into AgentX Support.

1. Sign in to your Google Sheets account.
   
2. Share the Google Sheet you plan to import with the AgentX Support integration account:
   
   ```plaintext
   integration@astral-voyage-253107.iam.gserviceaccount.com
   ```
   
3. Open a new tab and sign in to AgentX Support.
   
4. Go to **Advanced > Data Table**.
   
5. Click **Import from Google Sheet**.
   
6. Enter a name for the data table in the **Data Table Name** field.
   
   ![Enter details about the data table to import](/assets/import-data-table.mlBLXffz.png)_Enter details about the data table to import_
   
7. Enter the sheet key in the **Sheet Key** field.
   
   The sheet key is the long string of characters that appears after `docs.google.com/spreadsheets/d/` and before the next slash in the URL.
   
   ![Enter the sheet key](/assets/sheet-key.vOzAn1on.png)_Enter the sheet key_
   
8. Enter the name of the sheet you plan to import in the **Worksheet Title** field.
   
9. Click **Submit**.
   
   > **UPDATING IMPORTED TABLES**
   > 
   > To update a table imported from Google Sheets, [repeat the import steps](#import-a-google-sheet-as-a-data-table).
   

## Supported operations

The following operations are available for retrieving data from data tables:

| Operation | Description |
| --- | --- |
| Lookup | Retrieves a single record using a key-value pair. |
| Search | Retrieves multiple records based on a key-value match. |
| Get All | Retrieves all records in the data table. |

## Use a data table in a flow

You can reference data tables in flows by using the [Data Table](/en/agentic/agentx-support/nodes/add-ons#data-table) add-on.

![Completed flow](/assets/product-info-flow.C0L5Qpon.png)_Completed flow_

In this example, the AI agent looks up product information based on the user's selection and returns relevant details such as price, availability, and description.

1. [Create a skill](/en/agentic/agentx-support/ai-agents/skills#create-a-skill) named `Product Information`.
   
   This skill is activated when users ask about available products.
   
2. Open the **Product Information** flow and add a **Question** node asking which product the user wants more information on.
   
   You can use **Quick Replies** to ensure the user's selection matches one of the product names in the table.
   
3. [Assign a parameter](/en/agentic/agentx-support/ai-agents/parameters#assign-parameter) to the question node:
   
   - **Name**: `user_input`
   - **Value**: `$sys_outgoing_transition`
   
   The value `$sys_outgoing_transition` is a [fixed parameter value](/en/agentic/agentx-support/ai-agents/parameters#fixed-values) that stores the user's selection.
   
   ![User input parameter](/assets/user-input.lY-vk7IF.png)_User input parameter_
   
4. Drag the **Data Table** node into the flow.
   
5. Configure the node:
   
   - **Table Name**: `product-information`
   - **Operation**: `Lookup`
   
   ![Configure the data table node](/assets/lookup-data-table.CJXcPQfA.png)_Configure the data table node_
   
6. Add a **Query** to find the product by name:
   
   - **Key**: `Name`
   - **Value**: `$user_input`
   
   When this node runs, it stores the matching record in a `tableOutput` object, where each column from the table is a key.
   
7. Add a **Message** node to present the product information using values from `tableOutput`.
   
   ![Product details](/assets/product-details.88E1juNH.png)_Product details_
   
   This example uses the following message:
   
   ```plaintext
   Here are the details for {{tableOutput.Name}}:
   
   💲 Price: {{tableOutput.Price}}
   📦 In Stock: {{tableOutput["In Stock"]}}
   📝 Description: {{tableOutput.Description}}
   ```
   
   The rendered output:
   
   > Here are the details for Comfort Headphones:
   > 
   > 💲 Price: $89.99
   > 
   > 📦 In Stock: Yes
   > 
   > 📝 Description: Wireless headphones with noise cancellation
   
   > **BRACKET NOTATION**
   > 
   > Use bracket notation to reference column names that contain spaces or special characters.
   
8. Optional. Add a follow-up message asking whether the information was helpful. Use quick replies (`Yes`, `No`) that route to either a **Thank You** or **Escalation** ending node.
   
9. Click **Save** to save your changes.
   
10. Click **Publish** to publish the flow.

---
