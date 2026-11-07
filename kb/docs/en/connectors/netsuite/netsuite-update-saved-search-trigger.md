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
