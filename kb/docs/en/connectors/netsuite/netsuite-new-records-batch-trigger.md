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
