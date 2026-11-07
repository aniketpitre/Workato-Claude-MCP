---
url: 'https://docs.workato.com/en/features/batch-processing.md'
description: >-
  Learn how batch processing lets one Workato job handle multiple records at
  once to boost speed and throughput when moving large data volumes.
---

# Batch processing

Typically, 1 Workato [job](/en/recipes/jobs) processes 1 row of data or 1 record. Batch processing simply means that 1 job processes multiple rows of data or multiple records. This will increase speed and data throughput when you move a large number of records from one app to another.

Let's look at the example below to understand the concept of batch processing (or Batching).

![Batching example](/assets/batching-example.Sue2QbCn.png)_Simple example of Batching_

Larger batch size means we need fewer jobs and fewer API calls to move the same amount of data. As a result, [recipe](/en/workato-concepts#recipes) run time often decreases. The following chart shows how different batch sizes can reduce running time when Workato moves 100,000 rows of data.

![Batching example](/assets/batching-graph.BKaSvP9I.png)_Time saving using Batching_

You can find batching-supported [triggers](/en/recipes/triggers) and [actions](/en/recipes/actions) in certain connectors, such as database connectors (SQL Server, MySQL, etc.), cloud storage connectors that work with CSV files (for example, Box, Amazon S3), Salesforce connector, etc. We recommend matching a batch trigger with batch actions.

![Batch trigger example](data:image/png;base64,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)_Example of a Batch trigger_

![Batch action example](data:image/png;base64,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)_Example of a Batch action_

## Batch triggers

For normal triggers, 1 [trigger event](/en/recipes/triggers) often contains 1 data record. For example, "a new account is created in Salesforce" is 1 trigger event. It will trigger a Workato [recipe](/en/workato-concepts#recipes) to create a [job](/en/recipes/jobs) and process 1 data record (i.e. that new account in Salesforce).

For Batch triggers, 1 trigger event contains multiple records (for example, 50 accounts in Salesforce). A job will thus process multiple records at once. The `Batch size` determines the maximum number of records in 1 trigger event.

### Batch trigger example

The Salesforce batch trigger has a default value of 100. In this case, each trigger event will contain a maximum 100 account records.

![Batch trigger](/assets/batch_trigger_config.8SFV6Tcs.png)_Batch trigger with a batch size of 100_

The job details for each trigger event will contain the specific details of only the first and last record in the list.

![Batch trigger](/assets/trigger-output-new-accounts-batch.DPCYQT7T.gif)_Job details - trigger output for a batch of new accounts in Salesforce_

For example, when the following recipe was first started, 843 records were fetched from Jan 1, 2015, midnight PST. These records were broken up into 8 trigger events of 100 records each, and 1 trigger event of 43 records. The next poll, 5 minutes later, fetched only 2 new account records created.

![Batch trigger](/assets/batch_trigger_job_report.Csp15iyL.png)_Custom job report displaying account batches' details - names of first and last accounts in the batch, as well as batch size_

## Batch actions

Batch actions are typically of the form **Create batch** or **Update batch** or **Upsert batch**. Accordingly, these actions create a list of new records, update a list of existing records, or upsert (create if record doesn't exist, update if record exists) a list of records.

### Batch create actions

Batch create actions create multiple records in a single action (typically corresponding to a single API call). Batch create actions usually accept a list of records as input, therefore typically recipes will:

- move a list of records from source app to target app, or
- prepare a list of records via building and accumulating data in a custom list, then moving that prepared list into the target app

### Batch create action example

The following is an example scenario that imports new products from a Box CSV file into Salesforce via the **Bulk insert** action.

![Example recipe using list input](/assets/example-recipe-using-input-list.jrEpPeWr.png)_Example recipe using list input._

Actions that take lists as inputs will have a input field called **Source list**, which will only take in list pills. When these list input fields are selected, the datatree changes to offer only list pills. The Rows list object pill is mapped into the Salesforce product source list input field.

![Example input source list](/assets/example-input-source-list.Bvp_S8Zv.png)_Rows list object is mapped into the Salesforce products input source list_

For the list object passed into the input source list, the list will be transferred from the source app to the target app, with the values being transferred based on the fields mapped in the recipe. The three inventory items will be moved from Box into Salesforce as products.

![Mapping of list pills](/assets/mapping-of-list-pills.BV6V5f-P.gif)_Mapping of list datapills to list input_

The following shows the CSV file content.

![CSV trigger output](/assets/csv-trigger-output.BrTkGX5U.png)_Trigger output details displaying lines within the CSV file_

The action output in the job history shows that three products have been created accordingly in Salesforce.

![Salesforce bulk insert via input list](/assets/job-output-sf-bulk-insert.V3Z1CXL4.png)_Salesforce bulk insert via list input_

## Maximize data throughput with batch processing

To maximize data throughput, you must match batch triggers with batch actions.

You can also raise throughput even further by increasing recipe concurrency. This means Workato will run multiple jobs at the same time, instead of running them one by one.

The following pictures show how to enable concurrency in a Workato recipe, and how batching & concurrency work together.

![Enable concurrency](/assets/concurrency.CJkMDTmt.png)_Setup concurrency in a Workato recipe_

![Increasing throughput in Workato via different mechanisms](/assets/increasing-throughput.Ul6_OqSv.png)_Increasing throughput in Workato via batching & concurrency_

---
