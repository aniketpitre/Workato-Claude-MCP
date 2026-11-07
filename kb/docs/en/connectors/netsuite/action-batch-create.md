---
url: 'https://docs.workato.com/en/connectors/netsuite/action-batch-create.md'
description: >-
  The batch create actions in the NetSuite SOAP connector create multiple
  standard or custom records synchronously and return success and failure data.
---

# NetSuite SOAP - Create standard and custom records in batch actions

The NetSuite actions **Create standard records in batch** and **Create custom records in batch** allow you to create multiple records in batches in NetSuite. These actions return the IDs of records successfully uploaded to NetSuite and the list of data that failed to upload to NetSuite.

These actions are synchronous, meaning that Workato sends a request to NetSuite to create a custom or standard record and then waits for Netsuite to complete before beginning other recipe actions. This is in contrast to our bulk actions which are asynchronous API calls - meaning Workato calls NetSuite and then must poll for the job status, which can cause delays and longer job times.

Synchronous actions can be especially useful during high volume data loads where ingestion time is critical.

> **API CONCURRENCY**
> 
> Synchronous actions may result in more performance benefits in terms of ingestion but also consume your organization's API concurrency. By default, this is set to 5 but you may have purchased more from NetSuite. At API concurrency of 5, this means that you may have up to 5 concurrent NetSuite requests across your workspace but allows you to ingest up to 5 times more records than our asynchronous bulk actions. However, you should be conscious of your concurrency quotas during large data volume loads, as this could also impact your other integrations that need concurrency. A simple way to limit API concurrency on Workato would be through [Recipe Concurrency](/en/recipes/settings#concurrency). Buying more API concurrency increases the number of batches you can process simultaneously in your workspace. Contact your Netsuite Customer Support Representative for more information.
> 
> One thing to note - Netsuite bulk actions, whilst less performant, utilize significantly less API concurrency since jobs are processed in a single queue on Netsuite.

## Limitations

Workato limits the processing time for each action to 180 seconds, but in some cases, NetSuite can take much longer to process synchronous API calls containing large batches of records. This can result in a timeout error in Workato. To prevent this, we recommend reducing your batch size for this specific record to ensure optimal processing in less than seconds.

## Input

Select the **Standard record** or **Custom record** that you plan to create.

In our example, we create a standard record and select **Customer**.

![Select Netsuite record](/assets/record-name.C5pTIkKn.png)_Select a NetSuite record_

### Field configuration

Configure the following input fields to shortlist the NetSuite fields you plan to use. The action's input and output then display only these fields. This optimizes your NetSuite API requests and makes working with complex NetSuite objects containing hundreds of fields easier.

In this example, we used the fields **Company name**, **External ID**, and the custom field **Product interest**.

![Field configuration](/assets/fields-config.DaTzcE-x.png)_Shortlist NetSuite fields_

- Fields
  
- The Netsuite record's main fields that you plan to shortlist. If left blank, all fields are displayed in the input and output datatree.
  
- Custom fields
  
- The Netsuite record's custom fields that you plan to shortlist. If no fields are selected, Workato retrieves 50 custom fields by default.
  
- Custom segment schema
  
- If your Netsuite record has a custom schema, you can define the custom schema here.
  
- Line item custom fields
  
- The Netsuite record's line item custom fields to be shortlisted. If no fields are selected, Workato retrieves 50 custom fields by default.
  
- Line item custom segment schema
  
- If your Netsuite line item has custom schema, you can define the custom schema here.
  

### Record

The name of this section is dynamic and is based on the **Standard record** or **Custom record** you selected in the previous step. In our example, this section is named **Customers**. Here are the data mappings for creating NetSuite records.

In the following example, we map the data from the Box trigger **New CSV file in directory** to NetSuite record **Customer**. Notice that it only displays the shortlisted fields **Company name**, **External ID**, and **Product interest**.

![Field mappings](/assets/datapill-mapping.Dq0Eld3A.png)

These are the input fields:

- Record source list
  
- Provide a [list datapill](/en/features/list-management).
  
  For example, use a list of rows in a CSV file. The action automatically iterates through all items in the list, and maps them to NetSuite records.
  
- Record fields
  
- Map the datapills under the preceding list datapill.
  
  For example, the CSV column names under the CSV Rows list datapill. This action automatically iterates through all items in the list, and maps them to NetSuite records.
  

## Output

- Number of processed records
  
- The total number of records processed.
  
- Number of successful records
  
- The number of records successfully created.
  
- Number of failed records
  
- The number of records failed to be created.
  
- Successful records
  
- A list datapill containing all successful records.
  
  Use this to [iterate through all records in the list](/en/features/list-management).
  
  The data fields of each record are:
  
  - Internal ID
    
  - The internal ID of this record.
    
  - External ID
    
  - The external ID of this record.
    
  - Record
    
  - Contains all data fields of this record.
    
  - List size
    
  - Number of successful records in this list.
    
- Failed records
  
- A list datapill containing all failed records.
  
  Use this to [iterate through all records in the list](/en/features/list-management).
  
  The data fields of each record are:
  
  - Error
    
  - A list datapill containing all errors of this record.
    
    Use this to [iterate through all errors in the list](/en/features/list-management).
    
  - Record
    
  - Contains all data fields of this record.
    
  - List size
    
  - The number of failed records in this list.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-create-object-batch-action.md
description: >-
  The Create records in bulk action in the NetSuite SOAP connector lets you
  create multiple standard or custom records at the same time.
---

# NetSuite SOAP - Create records in bulk action

The `Create standard records in bulk` and `Create custom records in bulk` actions enable you to create multiple standard records or custom records at the same time.

## Limitations

These actions are subject to the following limitations:

- **List size**: These actions accept a list of 400 records maximum. Actions fail if you provide more than 400 records.
- **Processing times**: NetSuite bulk actions are processed in a single queue on NetSuite, which can lead to processing delays. These actions are asynchronous, meaning Workato must poll for job status updates. As a result, processing times can vary depending on the load and availability of the NetSuite system.

## Input

Select the **Standard record** or **Custom record** that you plan to create. In this example, we select **Customer**:

![Select Netsuite record](data:image/png;base64,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)

Proceed to configure the following sections:

### Field configuration

In this section, you can shortlist the NetSuite fields you plan to use. The action's input and output then displays only these fields. This approach makes it easier to work with complex NetSuite objects that may have hundreds of fields.

In this example, we use the fields **First name**, **Last name**, **Email**, and **phone** from the **Customer** record:

![Field configuration](/assets/field-config.BzJN6Hx_.png)

The followings are all input fields in this section:

- Fields
  
- The Netsuite record's main fields that you plan to shortlist.
  
- Custom fields
  
- The Netsuite record's custom fields that you plan to shortlist.
  
- Custom segment schema
  
- If your Netsuite record has custom schema, you can define the custom schema here.
  
- Line item custom fields
  
- The Netsuite record's line item custom fields to be shortlisted.
  
- Line item custom segment schema
  
- If your Netsuite line item has custom schema, you can define the custom schema here.
  

### Record

This section's name changes based on your selected **Standard record** or **Custom record**. Here are the data mappings for creating NetSuite records.

In the following example, we map the data from the Box trigger **New CSV file in directory** to NetSuite record **Customer**. Notice that it only displays the shortlisted fields **First name**, **Last name**, **Email**, and **phone**.

![Field mappings](/assets/batch-mapping.DDCD4P4j.png)

These are the input fields:

- Record source list
  
- Provide a [list datapill](/en/features/list-management).
  
  For example, use a list of rows in a CSV file. The action automatically iterates through all items in the list, and maps them to NetSuite records.
  
- Record fields
  
- Map the datapills under the preceding list datapill.
  
  For example, the CSV column names under the **CSV Rows** list datapill. This action automatically iterates through all items in the list, and maps them to NetSuite records.
  

## Output

- Number of processed records
  
- Total number of records processed.
  
- Number of successful records
  
- Number of records successfully created.
  
- Number of failed records
  
- Number of records failed to be created.
  
- Successful records
  
- A list datapill containing all successful records.
  
  Use this to [iterate through all records in the list](/en/features/list-management).
  
  The data fields of each record are:
  
  - Internal ID
    
  - Internal ID of this record.
    
  - External ID
    
  - External ID of this record.
    
  - Record
    
  - Contains all data fields of this record.
    
  - List size
    
  - Number of successful records in this list.
    
- Failed records
  
- A list datapill containing all failed records.
  
  Use this to [iterate through all records in the list](/en/features/list-management).
  
  The data fields of each record are:
  
  - Error
    
  - A list datapill containing all errors of this record.
    
    You can use this to [iterate through all errors in the list](/en/features/list-management).
    
  - Record
    
  - Contains all data fields of this record.
    
  - List size
    
  - Number of failed records in this list.

---
