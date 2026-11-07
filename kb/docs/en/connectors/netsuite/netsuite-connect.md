---
url: 'https://docs.workato.com/en/connectors/netsuite/netsuite-connect.md'
description: >-
  Set up and connect NetSuite SOAP in Workato using token-based authentication
  with an application ID, consumer key and secret, and token ID and secret.
---

# Connect to NetSuite SOAP on Workato

To connect to NetSuite using token-based authentication, you must generate an application ID, a consumer key, a consumer secret, a token ID, and a token secret.

For a step-by-step guide, refer to the following video tutorial:

[Video](https://www.youtube.com/embed/F29lbb9jN74)

* * *

## Prerequisites

To connect to NetSuite in Workato, ensure you have the following:

- The privilege to [create connections](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets) in Workato.
- Access to a NetSuite Admin account.
- An understanding of the required NetSuite permissions.

* * *

## Enable web services and token-based authentication

Complete the following steps to enable web services and token-based authentication in your NetSuite instance:

Watch a demonstration of this step

[Video](https://www.youtube.com/embed/F29lbb9jN74?rel=0&start=81&end=136)

1. Navigate to **Setup > Company > Enable Features > SuiteCloud**.
   
   ![Navigate to Setup > Company > Enabled Features > SuiteCloud](/assets/enable-web-services-1.ByhOSi9g.png)_Navigate to **Setup > Company > Enable Features > SuiteCloud**_
   
2. Select the **Client SuiteScript** and **Server SuiteScript** checkboxes.
   
   ![Check the Client SuiteScript and Server SuiteScript checkboxes](/assets/netsuite-suitescript-setup.C_XBgvF2.png)_In the **SuiteCloud** tab, check the **Client SuiteScript** and **Server SuiteScript** checkboxes_
   
3. Navigate to the SuiteTalk (Web Services) section and select the **SOAP Web Services** and **REST Web Services** checkboxes.
   
4. Navigate to the Manage Authentication section and select the **Token-based authentication** and **OAuth 2.0** checkboxes.
   
   ![Select the SOAP Web Services, REST Web Services, Token-based authentication, and OAuth 2.0 checkboxes](/assets/enable-web-services-2.qoBpgFJ6.png)_In the SuiteCloud tab, select the SOAP Web Services, REST Web Services, Token-based authentication, and OAuth 2.0 checkboxes_
   
5. Click **Save**.
   

* * *

## Create an integration record

Complete the following steps to create a new integration record. The integration record represents an app, platform, or tool you plan to integrate with NetSuite.

Watch a demonstration of this step

[Video](https://www.youtube.com/embed/F29lbb9jN74?rel=0&start=137&end=211)

1. Navigate to **Setup > Integration > Manage Integrations > New**.
   
2. Provide a name in the **Name** field.
   
3. Ensure the **State** field is set to **Enabled**.
   
4. Ensure that the **Token-based authentication** checkbox is selected.
   
5. Clear the **TBA: Authorization flow** and **Authorization code grant** checkboxes.
   
6. Click **Save**.
   
7. Copy the **Consumer key / Client ID** and **Consumer secret / Client secret** and store them in a secure location. Workato requires these values to establish a NetSuite connection in Workato.
   

* * *

## Create an integration role

Complete the following steps to create an integration role.

Watch a demonstration of this step

[Video](https://www.youtube.com/embed/F29lbb9jN74?rel=0&start=212&end=412)

1. Navigate to **Setup > Users/Roles > Manage Roles > New** to create an integration role.
   
   ![Navigate to Setup > Users/Roles > Manage Roles](/assets/setup-integration-role-1.D-2hPdjY.png)_Navigate to **Setup > Users/Roles > Manage Roles > New**_
   
2. Provide a name for your integration role in the **Name** field.
   
3. Configure how you plan this role to interact with subsidiaries in the **Subsidiary Restrictions** section.
   
4. Optional. Select the **Web Services Only Role** checkbox in the **Authentication** section to restrict this role to API interactions only. This prevents access through NetSuite's user interface (UI).
   
   > **WEB SERVICES ONLY AUTHENTICATION**
   > 
   > Roles with the **Web Services Only** restriction don't work with RESTlets. Assigning this authentication in the role impacts the `Execute RESTlet script` action in the NetSuite REST connector.
   
5. Navigate to the **Permissions** tab to specify the extent to which Workato and other applications can interact with NetSuite.
   
   ![Set up integration-specific permissions](/assets/setup-integration-role-4.K5vES586.png)_Set up integration-specific permissions_
   
   For example, if you plan to create sales orders in NetSuite, search for and select the **Sales Order** permission and assign it the **Create** level. If you plan to create, update, and read sales order data, select the **Full** permission level.
   
6. Click **Setup**.
   
   ![Click Setup](/assets/click-setup.Bb_wUdl5.png)_Click **Setup**_
   
7. Search for the following permissions, set their permission level to **Full**, and then click **Add**:
   
   - **Log in using Access Tokens**
   - **Log in using OAuth 2.0 Access Tokens**
   - **REST Web Services**
   - **SOAP Web Services**
   - **Set Up Company**
   - **SuiteScript**
   - **User Access Tokens**
   - **Set Up SOAP Web Services**
   - **Custom Body Fields**
   - **Custom Address Form**
   - **Deleted Records** (required for the [Deleted standard record](/en/connectors/netsuite/deleted-standard-record-trigger) trigger)
   
   > **REST WEB SERVICE PREREQUISITES**
   > 
   > Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html#subsect_158219919831) guide for more information about the features and permissions required for REST Web Services.
   
8. Click **Save**.
   

* * *

## Set up an integration user

After configuring the integration role, you must assign it to the integration user. We recommend creating a separate user for your integrations.

Complete the following steps to edit an existing integration user or create a new one:

Watch a demonstration of this step

[Video](https://www.youtube.com/embed/F29lbb9jN74?rel=0&start=413&end=471)

**Edit an existing user**

1. Navigate to **Setup > Users/Roles > Manage Users** to edit an existing user.
   
   ![Set up other permissions and permission levels](/assets/setup-integration-user-1.Dqkn9i22.png)_Navigate to Setup > Users/Roles > Manage Users_
   
2. Navigate to the **Access** tab and ensure the **Give access** checkbox is selected.
   
3. Select the integration role you created in the [Create an integration role](#step-3) step in the **Role** field to assign it to the new user.
   

**Create a new user**

1. Navigate to **Lists > Employees > Employees > New** to create a new user.
   
2. Enter a name and email address for the user in the **Name** and **Email** fields.
   
3. Select the subsidiary they belong to in the **Subsidiary** menu.
   
4. Navigate to the **Access** tab and select the **Give access** checkbox.
   
5. Select the integration role you created in the [Create an integration role](#step-3) step in the **Role** field to assign it to the new user.
   
   ![Assign integration role](/assets/setup-integration-user-2.DWZQnQ73.png)_Assign the integration role to a user_
   

* * *

## Create an access token

Complete the following steps to create an access token for the integration user:

> **ACCESS TOKENS**
> 
> If the integration user has the **User Access Tokens** permission, they can create and revoke their own tokens. If the integration user has only the **Log in using Access Tokens** permission, a user with the **Access Token Management** permission must create an access token for the integration user.

Watch a demonstration of this step

[Video](https://www.youtube.com/embed/F29lbb9jN74?rel=0&start=472&end=517)

1. Navigate to **Setup > Users/Roles > Access Tokens > New**.
   
   ![Setup > Users/Roles > Access Tokens > New](/assets/access-token.BbvvWKbs.png)_In NetSuite, go to Setup > Users/Roles>Access Tokens > New_
   
2. Select the [integration record](#step-2) you created in the **Application name** field.
   
3. Select the [user](#step-4) you created or edited in the **User** field.
   
4. Select the [role](#step-3) you created in the **Role** field.
   
5. Use NetSuite's default name or provide one in the **Token name** field.
   
6. Click **Save**.
   
7. Copy the **Token ID** and **Token secret** and store them in a secure location. Workato requires these values to establish the NetSuite connection.
   

* * *

## Connect to NetSuite on Workato

Complete the following steps to establish a connection with NetSuite SOAP in Workato:

Watch a demonstration of this step

[Video](https://www.youtube.com/embed/F29lbb9jN74?rel=0&start=519&end=569)

1. Provide a **Connection name** that identifies which NetSuite instance Workato is connected to.
   
   ![NetSuite Connection setup](/assets/netsuite-connection-setup.Byi_p2_F.png)_Connection setup_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Enter your NetSuite **Account ID**. You can find your account ID by signing in to NetSuite as an administrator and going to **Setup > Integration > SOAP Web Services Preferences**.
   
4. Enter your NetSuite **Token ID** and **Token Secret**.
   
5. Use the **NetSuite account timezone** menu to select the timezone in which your NetSuite instance operates.
   
6. Configure the **Ignore read-only fields** to specify whether to ignore read-only fields in add and update operations. Select **No** to prevent read-only fields from being overwritten and generate an error when attempts are made to overwrite them.
   
7. Expand the **Advanced settings** section and enter the integration record's **Consumer key** and **Consumer secret**. If left blank, the global consumer key and secret are used.
   
8. Use the **Run SuiteScript and trigger workflows** field to select whether to enable server SuiteScripts and trigger workflows. Leave this field blank to use the company preference configured in NetSuite. Refer to NetSuite's [Request-Level Preferences](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4170181850.html#bridgehead_4629750371) documentation for more information.
   
9. Click **Connect** to authorize a connection between Workato and your NetSuite SOAP account.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-classification-object-trigger.md
description: >-
  The Classification object trigger in the NetSuite SOAP connector monitors
  classification objects such as departments, locations, and classifications.
---

# NetSuite SOAP - Classification object trigger

Some objects in NetSuite are classification objects: departments, locations, and classifications.

Select the classification object to monitor.

When the recipe runs for the first time, it picks up all existing instances of the selected object. Subsequently, the recipe processes only newly created instances.

![New classification object trigger](/assets/new-classification-object-trigger.4nlRkXuk.png)_New classification object trigger_

For example, if I select **departments** as the triggering object, the trigger picks up all existing department objects when the recipe runs for the first time. Subsequently, if the recipe keeps running, it only picks up newly created departments.

> **Stopping and re-starting recipes**
> 
> If the recipe stops and then starts again, it picks up all new departments that you create during the stoppage interval.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/export-new-updated-record-bulk-trigger.md
description: >-
  The bulk export triggers in the NetSuite SOAP connector run when standard or
  custom records are created or updated, streaming them as a CSV in batches.
---

# NetSuite SOAP - Export new and updated standard or custom records triggers (bulk)

These triggers run when a record in a custom or standard NetSuite object is created or updated. These triggers retrieve the records in batches and stream them as a CSV.

Workato has the following triggers:

- Export new standard records (bulk)
- Export new custom records (bulk)
- Export new/updated standard records (bulk)
- Export new/updated custom records (bulk)

### Input

| Input field | Description |
| --- | --- |
| Standard or custom object | Select a NetSuite object to fetch. |
| When exporting records to form the CSV, fetch them in batches of | _Optional_. Use this field to control the size of the batch. The minimum value is 50 and the maximum value is 100. Defaults to 100 records. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Defaults to one hour after the recipe starts. After the recipe runs or is tested, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

### Output

| Field | Description |
| --- | --- |
| File content | This datapill contains the output of the trigger. |
| Object name | The name of the retrieved object. |
| Object schema | The schema of the retrieved object, based on the user-selected fields. Each field contains an associated name, label, original datatype, mapped datatype, length, precision, scale, and custom field. This allows for easy processing. |
| Created or updated from | The time and date the record was created or updated. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-new-records-trigger.md
description: >-
  The new standard object and new custom object triggers in the NetSuite SOAP
  connector pick up newly created records of the selected object type.
---

# NetSuite SOAP - New standard object and new custom object trigger

The new standard object and new custom object triggers are very similar.

> **Limited support**
> 
> Because of API limitations, Workato does not support [some types of records](/en/connectors/netsuite/netsuite-unsupported-records).

## Configure the trigger

To use this trigger, first, we must select the standard object or the custom object to monitor. We also must input the datetime in the **From** field to pinpoint the exact date from which the recipe should start processing records.

![Unconfigured NetSuite new object trigger](/assets/unconfigured-netsuite-new-trigger.CF9Wj014.png)_NetSuite new object trigger - unconfigured. Select the object to monitor for newly created records._

When the recipe starts for the first time, it picks up all existing instances of the selected object created after the datetime in the **From** field. Subsequently, it processes only the new instances.

Consider the selected sales order and 1 Jan, 2017 midnight trigger:

![Configured NetSuite new object trigger](/assets/configured-netsuite-new-trigger.Ds-tMDTh.png)_NetSuite new object trigger - configured_

On first run, the recipe processes all sales orders from or after 1 Jan, 2017 midnight. Subsequently, if the recipe continues to run, the recipe picks up only new sales.

> **Trigger behavior when you stop and restart a recipe**
> 
> If you stop the recipe, the recipe processes all new sales orders created during the stoppage interval when restarted.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-updated-records-trigger.md
description: >-
  The new/updated standard object and custom object triggers in the NetSuite
  SOAP connector pick up records created or updated after a set date and time.
---

# NetSuite SOAP - New/Updated standard object and new/updated custom object triggers

The new/updated standard object and new/updated custom object triggers are very similar.

> **Limited support**
> 
> Because of API limitations, Workato does not support [some types of records](/en/connectors/netsuite/netsuite-unsupported-records).

When a recipe that updates records starts for the first time, it processes all instances of the selected object created or updated after the datetime in the **From** field.

Subsequently, the recipe processes all newly created instances or updated instances.

## Configure the trigger

To use this trigger, follow these steps:

1. Select the standard object or the custom object to monitor.
   
2. Identify the datetime in the **From** field so the recipe starts processing the correct records.
   
   ![Unconfigured NetSuite new/updated object trigger](/assets/unconfigured-netsuite-new-updated-trigger.Ci6wvg7K.png)_NetSuite new/updated object trigger - unconfigured. Select the object to monitor for newly created or updated records._
   

## Example

Consider the selected sales order and 1 Jan, 2017 midnight trigger:

![Configured NetSuite new/updated object trigger](/assets/configured-netsuite-new-updated-trigger.DJnRXlp5.png)_NetSuite new/updated object trigger - configured_

On the first run, the recipe processes all sales orders from or after 1 Jan. 2017 at midnight. Subsequently, if the recipe continues to run, the recipe picks up only new sales.

> **Trigger behavior when the recipe stops and restarts**
> 
> If you stop the recipe, it processes all new sales orders created during the stoppage interval when you restart it.
> 
> The recipe only picks up the most recent version of the search record. So, if a record updates three (3) times during the outage interval, the recipe only picks up the last version of the record when it restarts.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-new-records-batch-trigger.md
description: >-
  The New/updated records (batch) trigger in the NetSuite SOAP connector
  retrieves records created or updated since the last run, every five minutes in
  batches.
---

# NetSuite SOAP - New/updated records trigger (batch)

Triggers every five minutes. Depending on the name of the trigger you selected, the trigger retrieves a list of NetSuite records created and/or updated after the last time the recipe was triggered. The maximum batch size is 100 records.

## Input

Select the NetSuite object to monitor. In this example, we select `Customer`.

![Select Netsuite record](data:image/png;base64,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)

Optionally, you can configure these two optional fields:

- When first started, this recipe should pick up events from
  
- Trigger will retrieve NetSuite records created/updated from this date/time. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
  
- Batch size
  
- Trigger may detect many new NetSuite records and process the records in several smaller batches. This field determines how many NetSuite records to retrieve in a batch.
  

After that, you can proceed to configure the section `Output field configuration`. This section allows you to shortlist which NetSuite fields you want to use. Only those shortlisted fields are displayed in the trigger's output. This makes it easier to work with complex NetSuite objects with hundreds of fields.

In this example, we use the fields `First name`, `Last name`, `Email`, `phone` from the `Customer` record:

![Field configuration](/assets/field-config.BzJN6Hx_.png)

The followings are all input fields in this section:

- Fields
  
- The Netsuite record's main fields to be shortlisted.
  
- Custom fields
  
- The Netsuite record's custom fields to be shortlisted.
  
- Custom segment schema
  
- If your Netsuite record has custom schema, you can define the custom schema here.
  
- Line item custom fields
  
- The Netsuite record's line item custom fields to be shortlisted.
  
- Line item custom segment schema
  
- If your Netsuite line item has a custom schema, you can define the custom schema here.
  

## Output

- Range
  
- Trigger may detect many new NetSuite records and process the records in several smaller batches, based on the configured `Batch size`. This output field contains the first batch's job ID and last batch's job ID.
  
- First batch's job ID
  
- Trigger may detect many new NetSuite records and process the records in several smaller batches, based on the configured `Batch size`. This output field is the job ID of the first batch.
  
- Last batch's job ID
  
- Trigger may detect many new NetSuite records and process the records in several smaller batches, based on the configured `Batch size`. This output field is the job ID of the first batch.
  
- Records
  
- A [list datapill](/en/features/list-management) that contains all NetSuite records retrieved by the trigger in this batch. You can use this to [iterate through all records in the list](/en/features/list-management).
  
  Expand this datapill to find the NetSuite record's fields. Only fields shortlisted in the `Output field configuration` section are displayed here.
  
- Total number of record
  
- Total number of records in this batch.
  
- First batch
  
- Whether this is the first batch.
  
- Last batch
  
- Whether this is the last batch.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-new-saved-search-trigger.md
description: >-
  The New saved search trigger in the NetSuite SOAP connector retrieves new
  records that meet the criteria of a saved search.
---

# NetSuite SOAP - New saved search trigger

The **New saved search** trigger retrieves new records that meet the criteria of the saved search.

For example, consider a saved search that fetches customer records with an industry type of `Hardware`. A recipe can pick up the trigger event when new customers with this industry type are added. If you update existing customers to the `Hardware` industry type, the trigger picks up records where the **Date created** value meets the criteria set in the **When first started, this recipe should pick up events from** field.

## Configure your NetSuite saved search

Complete the following steps to configure your saved search in NetSuite:

1. Configure the columns **Internal ID** and **Date created** as result columns in the saved search to ensure the trigger works.
   
2. Navigate to the saved search page and edit it.
   
   ![Edit saved search](/assets/edit-saved-search.DF88b1m4.gif)_Edit the saved search_
   
3. Click the **Results** tab, navigate to the **Columns** section, and add the two fields to the list of columns if they are not already present.
   
   ![Add Internal ID and Date created columns in saved search](/assets/new-results-in-saved-search.BZhBeWZ_.gif)_Add Internal ID and Date created columns in saved search for New trigger_
   
4. Remove the **Dashboard** column from the saved search results if present. This column causes the trigger to return an error.
   
   ![Remove Dashboard column in saved search](/assets/delete-dashboard-field.B74rdRHE.gif)_Remove Dashboard column in saved search_
   

> **LIMITED SUPPORT**
> 
> Due to API limitations, Workato doesn't support certain NetSuite record types. Refer to [Unsupported records in NetSuite](/en/connectors/netsuite/netsuite-unsupported-records) for more information.

## Configure your New saved search trigger

The configuration for this trigger is similar to the [New/updated saved search trigger](/en/connectors/netsuite/netsuite-update-saved-search-trigger) configuration.

Complete the following steps to configure your trigger:

1. Use the calendar modal to select the date from which your recipe should begin to monitor events in the **When first started, this recipe should pick up events from** field. The recipe only retrieves records created after this date. When an existing record meets the saved search criteria, the recipe processes it only if it has a **Date created** value later than this value.
   
   ![Configure new saved search results trigger](/assets/new-saved-search.DPKXrpMD.png)_Configure the new saved search results trigger_
   
2. Select the **Record type** you plan to monitor.
   
3. Select the **Saved search** you plan to monitor for new records.
   
   > **SAVED SEARCH MISSING**
   > 
   > Complete the following checks if your saved search is missing from the **Saved search** drop-down menu:
   > 
   > - Ensure that the transaction (record) permission in the integration role is present.
   > - Ensure that the saved search is public or shared.
   > - Refresh your NetSuite connection to ensure that the trigger is pulling the most recent information.
   
4. Select the **Record list** you plan to retrieve in the trigger output.
   
5. Select the data you plan to use in the recipe in the input **Fields**. You can enter multiple values. All fields are returned if left blank.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/new-custom-records-saved-search-batch.md
description: >-
  The New custom records in a saved search trigger (batch) retrieves batches of
  new custom records from a saved search in NetSuite.
---

# NetSuite SOAP - New custom records in a saved search trigger (batch)

The **New custom records in a saved search** trigger (batch) retrieves batches of new custom records from a saved search in NetSuite. Ensure the saved search results include the following fields:

- The **Internal ID** and **Date Created** fields of the base object.
- The **Internal ID** field for all joined objects.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which this recipe retrieves trigger events. You can't change this value after you test or run this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Custom Record | Select the NetSuite custom record to retrieve. |
| Saved search | Select an option from the drop-down menu, or enter the saved search ID from the URL of the saved search page. |
| Batch size | Enter the number of NetSuite records to retrieve at a time. The minimum value is `1`, and the maximum is `100`. |
| Output field configuration | Select the NetSuite fields to include in the trigger output. |
| Object list | Select the records to include in the trigger output. |
| Fields | Select the fields to include in the trigger output. You must select the **Internal ID** checkbox for each record in the **Record list** field. |
| Custom record custom fields | Select custom fields to include in the trigger output. |

## Output

| Output field | Description |
| --- | --- |
| Range | The range of records retrieved in the current batch. |
| First batch ID | The unique identifier of the first batch retrieved during the trigger's execution. |
| Last batch ID | The unique identifier of the last batch retrieved during the trigger's execution. |
| Records | A list datapill containing the records that match the saved search criteria. |
| Basic (records) | An object containing fields specific to your selected **Custom Record**. The fields included are determined by your selections in the **Object list** and **Fields** input fields. |
| Total number of records | The total count of records retrieved from the saved search across all batches. |
| First batch | Indicates whether this batch is the first batch of records retrieved. |
| Last batch | Indicates whether this batch is the last batch of records retrieved. |
| Starting offset | The position of the first record in the current batch within the overall dataset. |
| Ending offset | The position of the last record in the current batch within the overall dataset. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/new-standard-records-saved-search-batch.md
description: >-
  The New standard records in a saved search trigger (batch) retrieves batches
  of new standard records from a saved search in NetSuite.
---

# NetSuite SOAP - New standard records in a saved search trigger (batch)

The **New standard records in a saved search** trigger (batch) retrieves batches of new standard records from a saved search in NetSuite. Ensure the saved search results include the following fields:

- The **Internal ID** and **Date Created** fields of the base record.
- The **Internal ID** field for all joined records.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which this recipe retrieves trigger events. You can't change this value after you test or run this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Record type | Select the [record type](#record-types) to retrieve. |
| Saved search | Select an option from the drop-down menu, or enter the saved search ID located in the URL of the saved search page. |
| Batch size | Enter the number of NetSuite records to retrieve at a time. The minimum value is `1`, and the maximum is `100`. |
| Output field configuration | Select the NetSuite fields to include in the trigger output. |
| Record list | Select the records to include in the trigger output. |
| Fields | Select the fields to include in the trigger output. You must select the **Internal ID** checkbox for each record in the **Record list** field. |
| `{RECORD_TYPE}` custom fields | Select custom fields to include in the trigger output. |

### Record types

This trigger retrieves records from the saved search for the following record types:

- Accounting Transaction
- Calendar Event
- Campaign
- Charge
- Contact
- Customer
- Employee
- File
- Gift Certificate
- Issue
- Item
- Item Demand Plan
- Item Supply Plan
- Job
- Opportunity
- Partner
- Project Task
- Support Case
- Task
- Time Bill
- Time Entry
- Transaction
- Vendor

## Output

| Output field | Description |
| --- | --- |
| Range | The range of records retrieved in the current batch. |
| First batch ID | The unique identifier of the first batch retrieved during the trigger's execution. |
| Last batch ID | The unique identifier of the last batch retrieved during the trigger's execution. |
| Records | A list datapill containing the records that match the saved search criteria. |
| Basic (records) | An object containing fields specific to your selected **Record type**. The fields included are determined by your selections in the **Record list** and **Fields** input fields. |
| Total number of records | The total count of records retrieved from the saved search across all batches. |
| First batch | Indicates whether this batch is the first batch of records retrieved. |
| Last batch | Indicates whether this batch is the last batch of records retrieved. |
| Starting offset | The position of the first record in the current batch within the overall dataset. |
| Ending offset | The position of the last record in the current batch within the overall dataset. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-update-saved-search-trigger.md
description: >-
  The New/updated saved search trigger in the NetSuite SOAP connector retrieves
  new and updated records that meet the criteria of a saved search.
---

# NetSuite SOAP - New/updated saved search trigger

The **New/updated saved search** trigger retrieves new and updated records that meet the criteria of the saved search.

For example, consider a saved search that fetches customer records with an industry type of `Hardware`. A recipe can pick up the trigger event when customers with this industry type are added or updated. If you update existing customers to the `Hardware` industry type, the trigger picks up records where the **Date created** value meets the criteria set in the **When first started, this recipe should pick up events from** field.

## Configure your NetSuite saved search

1. Configure the columns **Internal ID** and **Date created** as result columns in the saved search to ensure the trigger works.
   
2. Navigate to the saved search page and edit it.
   
   ![Add Internal ID and Last modified columns in saved search](/assets/edit-saved-search.DF88b1m4.gif)_Add Internal ID and Last modified columns in saved search for New/updated trigger_
   
3. Click the **Results** tab, navigate to the **Columns** section, and add the two fields to the list of columns if they are not already present.
   
   ![Add Internal ID and Date created columns in saved search](/assets/new-results-in-saved-search.BZhBeWZ_.gif)_Add Internal ID and Date created columns in saved search for New trigger_
   
4. Remove the **Dashboard** column from the saved search results if present. This column causes the trigger to return an error.
   
   ![Remove Dashboard column in saved search](/assets/delete-dashboard-field.B74rdRHE.gif)_Remove Dashboard column in saved search_
   

> **LIMITED SUPPORT**
> 
> Due to API limitations, Workato doesn't support certain NetSuite record types. Refer to [Unsupported records in NetSuite](/en/connectors/netsuite/netsuite-unsupported-records) for more information.

## Configure your New/updated saved search trigger

The configuration for this trigger is similar to the [New saved search trigger](/en/connectors/netsuite/netsuite-new-saved-search-trigger) configuration.

Complete the following steps to configure your trigger:

1. Use the calendar modal to select the date from which your recipe should begin to monitor events in the **When first started, this recipe should pick up events from** field. The recipe only retrieves records created after this date. When an existing record meets the saved search criteria, the recipe processes it only if it has a **Date created** value later than this value.
   
   ![Configure new/updated saved search trigger](/assets/new-updated-saved-search.avU657TO.png)_Configure the new/updated saved search results trigger_
   
2. Select the **Record type** for which you plan to retrieve the saved searches. This example uses the customer record type.
   
3. Select the **Saved search** you plan to monitor for new or updated records.
   
   > **SAVED SEARCH MISSING**
   > 
   > Complete the following checks if your saved search is missing from the **Saved search** drop-down menu:
   > 
   > - Ensure that the transaction (record) permission in the integration role is present.
   > - Ensure that the saved search is public or shared.
   > - Refresh your NetSuite connection to ensure that the trigger is pulling the most recent information.
   
4. Select the **Record list** you plan to retrieve in the trigger output. You can select multiple values.
   
5. Select the data you plan to use in the recipe input **Fields**. You can select multiple values. All fields are returned if left blank.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/new-updated-custom-records-saved-search-batch.md
description: >-
  The New/updated custom records in a saved search trigger (batch) retrieves
  batches of new or updated custom records from a saved search in NetSuite.
---

# NetSuite SOAP - New/updated custom records in a saved search trigger (batch)

The **New/updated custom records in a saved search** trigger (batch) retrieves batches of new or updated custom records from a saved search in NetSuite. Ensure the saved search results include the following fields:

- The **Internal ID** and **Last Modified** fields of the base object.
- The **Internal ID** field for all joined objects.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which this recipe retrieves trigger events. You can't change this value after you test or run this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Custom Record | Select the NetSuite custom record to retrieve. |
| Saved search | Select an option from the drop-down menu, or enter the saved search ID located in the URL of the saved search page. |
| Batch size | Enter the number of NetSuite records to retrieve at a time. The minimum value is `1`, and the maximum is `100`. |
| Output field configuration | Select the NetSuite fields to include in the trigger output. |
| Object list | Select the records to include in the trigger output. |
| Fields | Select the fields to include in the trigger output. You must select the **Internal ID** checkbox for each record selected in the **Record list** field. |
| Custom record custom fields | Select custom fields to include in the trigger output. |

## Output

| Output field | Description |
| --- | --- |
| Range | The range of records retrieved in the current batch. |
| First batch ID | The unique identifier of the first batch retrieved during the trigger's execution. |
| Last batch ID | The unique identifier of the last batch retrieved during the trigger's execution. |
| Records | A list datapill containing the records that match the saved search criteria. |
| Basic (records) | An object containing fields specific to your selected **Custom Record**. The fields included are determined by your selections in the **Object list** and **Fields** input fields. |
| Total number of records | The total count of records retrieved from the saved search across all batches. |
| First batch | Indicates whether this batch is the first batch of records retrieved. |
| Last batch | Indicates whether this batch is the last batch of records retrieved. |
| Starting offset | The position of the first record in the current batch within the overall dataset. |
| Ending offset | The position of the last record in the current batch within the overall dataset. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/new-updated-standard-records-saved-search-batch.md
description: >-
  The New/updated custom records in a saved search trigger (batch) retrieves
  batches of new or updated standard records from a saved search in NetSuite.
---

# NetSuite SOAP - New/updated standard records in a saved search trigger (batch)

The **New/updated custom records in a saved search** trigger (batch) retrieves batches of new or updated standard records from a saved search in NetSuite. Ensure the saved search results include the following fields:

- The **Internal ID** and **Last Modified** fields of the base record.
- The **Internal ID** field for all joined records.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which this recipe retrieves trigger events. You can't change this value after you test or run this recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Record type | Select the [record type](#record-types) to retrieve. |
| Saved search | Select an option from the drop-down menu, or enter the saved search ID located in the URL of the saved search page. |
| Batch size | Enter the number of NetSuite records to retrieve at a time. The minimum value is `1`, and the maximum is `100`. |
| Output field configuration | Select the NetSuite fields to include in the trigger output. |
| Record list | Select the records to include in the trigger output. |
| Fields | Select the fields to include in the trigger output. You must select the **Internal ID** checkbox for each record selected in the **Record list** field. |
| `{RECORD_TYPE}` custom fields | Select custom fields to include in the trigger output. |

### Record types

This trigger retrieves records from the saved search for the following record types:

- Accounting Transaction
- Calendar Event
- Campaign
- Charge
- Contact
- Customer
- Employee
- File
- Gift Certificate
- Issue
- Item
- Item Demand Plan
- Item Supply Plan
- Job
- Opportunity
- Partner
- Project Task
- Support Case
- Task
- Time Bill
- Time Entry
- Transaction
- Vendor

## Output

| Output field | Description |
| --- | --- |
| Range | The range of records retrieved in the current batch. |
| First batch ID | The unique identifier of the first batch retrieved during the trigger's execution. |
| Last batch ID | The unique identifier of the last batch retrieved during the trigger's execution. |
| Records | A list datapill containing the records that match the saved search criteria. |
| Basic (records) | An object containing fields specific to your selected **Record type**. The fields included are determined by your selections in the **Record list** and **Fields** input fields. |
| Total number of records | The total count of records retrieved from the saved search across all batches. |
| First batch | Indicates whether this batch is the first batch of records retrieved. |
| Last batch | Indicates whether this batch is the last batch of records retrieved. |
| Starting offset | The position of the first record in the current batch within the overall dataset. |
| Ending offset | The position of the last record in the current batch within the overall dataset. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/deleted-standard-record-trigger.md
description: >-
  The Deleted standard record trigger checks for records deleted after the
  specified date.
---

# NetSuite SOAP - Deleted standard record trigger

The **Deleted standard record** trigger checks for records deleted after the specified date. Subsequently, the recipe checks for deleted records once every polling interval.

> **PREREQUISITES**
> 
> Ensure that you've added the **Deleted Records** and **SOAP Web Services** permissions to the role used in your Workato connection. Refer to [Create an integration role](/en/connectors/netsuite/netsuite-connect#step-3) for detailed steps.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Set how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which to pick up trigger events when you start the recipe for the first time. Defaults to fetching records deleted an hour ago if left blank. You can't change this value after running or testing the recipe. |
| Standard record | Select a NetSuite standard record to monitor for deleted records. |

Supported records

This trigger supports monitoring the following NetSuite standard records for deleted records:

- Accounting Period
- Adv Inter Company Journal Entry
- Assembly Build
- Assembly Item
- Assembly Unbuild
- Billing Account
- Billing Schedule
- Bin
- Bin Transfer
- Bin Worksheet
- Budget
- Calendar Event
- Cash Refund
- Cash Sale
- Charge
- Check
- Contact
- Contact Category
- Contact Role
- Cost Category
- Coupon Code
- Credit Memo
- Custom List
- Custom Purchase
- Custom Record
- Custom Sale
- Custom Transaction
- Customer
- Customer Category
- Customer Deposit
- Customer Message
- Customer Payment
- Customer Refund
- Customer Status
- Deposit
- Deposit Application
- Description Item
- Discount Item
- Download Item
- Employee
- Entity Group
- Estimate
- Expense Category
- Expense Report
- Fair Value Price
- File
- Folder
- Gift Certificate
- Global Account Mapping
- Inter Company Journal Entry
- Inventory Adjustment
- Inventory Cost Revaluation
- Inventory Item
- Inventory Number
- Inventory Transfer
- Invoice
- Issue
- Item Account Mapping
- Item Demand Plan
- Item Fulfillment
- Item Group
- Item Receipt
- Item Supply Plan
- Job
- Job Status
- Job Type
- Journal Entry
- Kit Item
- Lot Numbered Assembly Item
- Lot Numbered Inventory Item
- Manufacturing Cost Template
- Manufacturing Operation Task
- Manufacturing Routing
- Marketing Campaign
- Markup Item
- Nexus
- Non Inventory Purchase Item
- Non Inventory Resale Item
- Non Inventory Sale Item
- Opportunity
- Other Charge Purchase Item
- Other Charge Resale Item
- Other Charge Sale Item
- Other Name Category
- Partner
- Partner Category
- Paycheck Journal
- Payment Item
- Payment Method
- Payroll Item
- Period End Journal
- Phone Call
- Price Level
- Pricing Group
- Project Task
- Promotion Code
- Purchase Order
- Purchase Requisition
- Return Authorization
- Rev Rec Schedule
- Rev Rec Template
- Sales Order
- Sales Role
- Serialized Assembly Item
- Serialized Inventory Item
- Service Purchase Item
- Service Resale Item
- Service Sale Item
- Site Category
- Solution
- Statistical Journal Entry
- Subtotal Item
- Support Case
- Task
- Term
- Time Bill
- Time Entry
- Time Sheet
- Topic
- Transfer Order
- Units Type
- Vendor
- Vendor Bill
- Vendor Category
- Vendor Credit
- Vendor Payment
- Vendor Return Authorization
- Win Loss Reason
- Work Order
- Work Order Close
- Work Order Completion
- Work Order Issue

## Output

| Output field | Description |
| --- | --- |
| Name | The name of the deleted record. |
| Internal ID | The unique internal identifier of the deleted record. |
| Type | The record type of the deleted record. |
| Deleted date | The date and time when the record was deleted. |

---
