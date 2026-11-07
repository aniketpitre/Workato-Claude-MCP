---
url: 'https://docs.workato.com/en/recipes/triggers.md'
description: >-
  Triggers define events for recipe execution, process data reliably, and
  operate using polling, real-time, scheduled, or change data capture mechanisms
  with single, batch, or bulk dispatches.
---

# Triggers

You can configure a trigger to define the event that executes a recipe.

> **SUMMARY**
> 
> - Triggers follow in-sequence delivery, maintain processed job records, prevent duplicate processing, and ensure job completion in order.
> - Trigger mechanisms come in four types: polling (checking regularly), real-time (immediate notifications, often through webhooks), scheduled (runs at specific times/intervals), and change data capture (CDC).
> - Trigger dispatches can be single (real-time data sync), batch (improved throughput with large data volumes), or bulk.

## What is a trigger?

A trigger defines the event that initiates a recipe's execution. Every recipe must have a trigger.

For example, the [New row in sheet in My Drive trigger](/en/connectors/google-sheets/trigger-new-row-my-drive) monitors a Google Sheet for new rows added to the bottom of the sheet. Each time this event occurs, the recipe executes the [actions](/en/recipes/steps#action-step) that follow the trigger.

![Example recipe](/assets/sample-recipe.DQZiA4Zn.png)_Example recipe_

Triggers can operate in real-time, poll for events periodically, or run on a schedule. Depending on the trigger and app capabilities, [jobs](/en/recipes/jobs) can be processed individually, in batches, or in bulk.

## How do recipes process trigger events?

Recipes pick up and queue trigger events in sequence to be processed as jobs. The recipe maintains a durable cursor that progresses through the trigger event queue synchronously, with adjustable throughput. Workato ensures that jobs aren't duplicated by keeping a record of all processed trigger events.

![Queued trigger events](/assets/queued-trigger-events.BGUlJlLR.png)_Trigger events are queued and processed by the recipe as jobs_

Workato triggers operate with the following behavior:

- In-sequence delivery
  
- Trigger events are delivered in chronological order, ensuring the oldest records are processed first or in the sequence they are sent to Workato.
  
- Durable cursor position
  
- Recipes remember their progress across stopped and running states. If a recipe stops, it resumes from the last processed event when restarted. For example, if a recipe is stopped on October 21, 2017, at 11:30 AM, it resumes processing trigger events from this point upon restart.  
  ![Durable cursor position](/assets/durable-cursor-position.BZj6kkMh.png)
  
- No duplication
  
- Workato ensures trigger events are processed only once by maintaining a record of all seen events.
  
- Flow control
  
- Recipes process trigger events synchronously, handling one job at a time. To optimize large data transfers, you can use [batch processing](#batch-triggers) or increase the [recipe concurrency](/en/recipes/settings#concurrency).
  
- Guaranteed delivery
  
- Workato guarantees that polling triggers reliably pick up events, even during server downtime or network issues. All triggers are processed in sequence to avoid data loss.
  

Webhook-based triggers, which power most real-time Workato integrations, may encounter dropped events. As a result, most Workato real-time triggers, except for HTTP webhook triggers, include a backup polling mechanism to recover missed events.

## How are triggers classified?

Triggers can be categorized based on the following criteria:

- **Trigger mechanism**, or how triggers **detect new events**.
- **Trigger dispatch**, or how triggers **group and deliver events**.

![Trigger types](/assets/trigger-types.CMUctkRK.png)_Trigger mechanisms and dispatches_

## How do triggers detect events?

Triggers use different mechanisms to detect events:

- [Polling triggers](#polling-triggers) periodically check for new data in an app.
- [Real-time triggers](#real-time-triggers) detect events instantly using webhooks or similar real-time capabilities.
- [Scheduled triggers](#scheduled-triggers) execute actions at specified intervals.
- [Change Data Capture (CDC)](#change-data-capture) is a process that monitors and captures database changes in real-time, enabling seamless synchronization between systems.

### Polling triggers

A polling trigger periodically checks for new events by querying an app at an interval you specify, which can be as frequent as every five minutes. Each poll can retrieve multiple events, potentially creating several jobs from a single poll.

When you start a recipe, the polling trigger collects events from the date specified in the [When first started, this recipe should pick up events from](#since-from) field.

For example, consider a recipe that fetches NetSuite customers created or updated since January 1, 2017, at 10:00 AM PST. After this initial fetch, the recipe polls regularly at an interval you specify. For instance, if the polling interval is set to five minutes, the recipe will retrieve any new or updated NetSuite customers from the last five minutes during each polling cycle.

When you stop a recipe, polling triggers stop fetching new events. When the recipe is restarted, the polling triggers retrieve all events that occurred while the recipe was stopped.

> **LONG ACTIONS JOB SEQUENCE**
> 
> If your recipe has a long action step and job, note that [when the action is put on hold](/en/recipes/long-actions#how-does-this-work), Workato automatically disregards the job sequence. The next job begins to process even if the previous job is not finished and the recipe concurrency is set to `1`.

#### Example

This recipe uses a polling trigger that polls every five minutes for new or updated Salesforce accounts.

![Polling intervals](/assets/polling_intervals.C6GN36qc.png)_Trigger hint regarding the specific polling interval_

Every five minutes, the recipe retrieves any Salesforce accounts created during the last polling cycle. If multiple accounts are created within a single interval, the recipe creates multiple jobs—one for each account.

If you stopped the recipe on February 1, 2017, and restarted it on March 10, 2017, Workato would retrieve all Salesforce accounts created since the time it stopped on February 1.

### Real-time triggers

A real-time trigger listens for specific events in an app and instantly notifies Workato when they happen. To enable this, the app must be registered to send event notifications through its API or interface.

Most real-time triggers in Workato use webhooks, which are highly efficient because they send notifications only when events occur, eliminating the need for frequent polling.

However, many real-time triggers (except HTTP real-time triggers) combine webhooks with polling. Unlike standard polling triggers that check for new data every few minutes, real-time triggers typically poll less frequently, such as once an hour. This polling also allows you to retrieve past events when first starting your recipe by specifying a date and time in the [When first started, this recipe should pick up events from](#since-from) field. This field is optional but useful for capturing earlier events.

### Scheduled triggers

A scheduled trigger executes at specified days and times, such as hourly, daily, or monthly.

![Salesforce scheduled trigger schedules](/assets/scheduled_trigger_schedules.C9FZ5qQq.png)_Various schedule options for Salesforce scheduled search trigger_

At each scheduled time or interval, the trigger fetches all events that match the specified criteria. Unlike other triggers, scheduled triggers can return events that were already picked up in previous runs.

Scheduled triggers process events in batches, similar to [batch triggers](#batch-triggers). You can configure the maximum batch size. For example, if the batch size is set to 100 and 420 new events are identified, five jobs are created: the first four jobs process 100 events each, and the fifth job processes the remaining 20 events.

#### Scheduler by Workato

The [New recurring event](/en/features/scheduler/triggers/new-recurring-event) trigger from [Scheduler by Workato](/en/features/scheduler) allows you to define when your recipe runs. You can create simple schedules, such as running a recipe hourly or daily, or set up more advanced configurations, like running a recipe every two weeks or only on weekdays.

For example, you can schedule your recipe to run every 15 minutes or at a specific time, such as 9:00 AM every Monday. To define a more complex schedule, select **Custom schedule** from the **Time unit** drop-down menu and enter a cron expression. The minimum supported interval is five minutes.

Scheduler by Workato offers precise control over recipe execution frequency, making it ideal for workflows that don't rely on events from other applications.

### Change data capture

Change Data Capture (CDC) is a process used to capture and track changes made to data in a database. This process enables real-time or near-real-time monitoring and synchronization of data changes, allowing applications to stay up-to-date with the latest changes in the database without using continuous polling.

The primary goal of CDC is to identify and capture changes such as inserts, updates, and deletions made to database tables. These changes are then propagated to downstream systems, data warehouses, or analytics platforms, ensuring that all systems have access to the most current data.

For more information, see [Change data capture](/en/data-orchestration/change-data-capture).

## How do triggers group and deliver events?

Trigger dispatches determine how a trigger groups and delivers events:

- [Single triggers](#single-triggers)
- [Batch triggers](#batch-triggers)
- [Bulk triggers](#bulk-triggers)

### Single triggers

Single triggers process and deliver each event as a separate job, making them ideal for real-time, continuous synchronization of data. For example, a single trigger can monitor Salesforce for closed opportunities. When an opportunity closes, the trigger processes it as a separate job and immediately transfers it to NetSuite as a sales order.

Most Workato triggers are single triggers.

### Batch triggers

Batch triggers process large amounts of data efficiently by retrieving multiple trigger events at once instead of one at a time. For example, you can use batch triggers to transfer large volumes of user activity data from Marketo into data warehouses like Redshift.

Batch triggers function similarly to [polling triggers](#polling-triggers) in how they fetch new events. However, they allow you to configure the group size or batch size during trigger setup, enabling more efficient processing of high-volume workflows.

![Batch triggers process trigger events in batches of user-specified sizes](/assets/batching-diagram.CpTc8wKI.png)_Batch triggers process trigger events in batches of user-specified sizes_

For more information about batch triggers, see [Batch processing](/en/features/batch-processing).

### Bulk triggers

Bulk triggers move large volumes of data efficiently. These triggers use CSV streaming, which enables data to be transferred from a source to a destination as a CSV object. While individual access to each record isn't possible, a large number of records can be processed and sent efficiently. Bulk triggers are ideal for tasks like exports or daily synchronization of high-throughput workflows, such as Jira tasks or updates to tables in ServiceNow.

Bulk triggers are integral to the ETL/ELT paradigm and serve as the primary method for consuming data from these sources in Workato. There is no upper limit on the number of records that can be exported as a single job, making bulk triggers well-suited for high-volume use cases. This approach also simplifies monitoring and tracking for large datasets.

Bulk triggers support both **New** and **New/Updated Records** and operate on a schedule, similar to scheduled triggers. They include the schema of the associated object, allowing for parsing of the CSV object at runtime within the recipe.

> **CANNOT RUN BULK TRIGGERS IN TEST MODE**
> 
> Bulk triggers require dedicated users to check periodically if the action is complete. This isn't available in [test mode](/en/recipes/testing).

## How can I configure trigger behavior?

Video guide: How to set up triggers correctly

[Video](https://www.youtube.com/embed/v0uS8HXthNo)

Workato provides several options to configure trigger behavior. These settings determine how and when the trigger detects events to process.

### When first started, this recipe should pick up events from

This input field allows you to specify the date and time from which the recipe retrieves past trigger events, allowing it to capture events that occurred before the recipe started.

#### Example

In the following example, the Salesforce [New object trigger](/en/connectors/salesforce/real-time-triggers#new-object-real-time) has a **When first started, this recipe should pick up events from** date set to July 14, 2020, 12:00 AM PST, with the **Account** object selected.

![Setting since date](/assets/set-since-date-for-trigger.C1S9PKTM.png)_Setting the **When first started, this recipe should pick up events from** field. The trigger picks up new accounts created since midnight of July 14, 2020._

When you start this recipe, it only picks up Salesforce accounts created after July 14, 2020, 12:00 AM PST.

Not all triggers have the **When first started, this recipe should pick up events from** input field. For triggers without this field, the date and time from which trigger events are fetched is predetermined by default, often set as an offset from the recipe's start time. Common default values include:

- When the recipe is first started
- An hour before the recipe is first started
- A day before the recipe is first started. This offset is typically mentioned in the trigger hint for the connector.

![Google Calendar since parameter](/assets/google_calendar_since_param.QdnxNL_O.png)_Trigger hint indicating the default offset of 1 hour ago for Google Calendar_

The **When first started, this recipe should pick up events from** value can only be set once. You can't change it after the recipe has run or been tested.

> **TIMEZONE**
> 
> For triggers without a dedicated **Timezone** input field, the timezone of the user who creates the recipe is used. When another user views the recipe, the time adjusts to their timezone, but the underlying value remains based on the creator's timezone. This means:
> 
> - If User A (with timezone `-0700 Pacific Time`) creates a recipe, the input time is stored with their timezone.
> - If User B (with timezone `+0530 Asia/Kolkata`) views or deploys the recipe, the time is displayed in their timezone but retains the original value set by User A.
> - The workspace timezone doesn't affect the **When first started, this recipe should pick up events from** input field unless explicitly set in the connector.

### Trigger conditions

Learn how to use trigger conditions in three minutes

[Video](https://www.youtube.com/embed/yuBOBZQ_fNo)

Trigger conditions are additional rules that define which trigger events are processed. For example, you can set a trigger condition that instructs a recipe to only process Salesforce accounts from California.

Workato evaluates trigger conditions after fetching the trigger events. This means Workato retrieves all new Salesforce accounts created in the last five minutes and then filters out accounts that aren't from California. As a result, with a **New Salesforce account** trigger, accounts that are later updated to reflect a California address won't be picked up. If your recipe appears to be missing expected events, this behavior might be the cause.

Trigger conditions typically don't monitor field changes. Instead, they check whether the condition is met when the trigger event is fetched. For example, to sync only closed-won opportunities from Salesforce into your ERP system, setting a trigger condition to check for the `Closed Won` state will cause every update made to an opportunity in this state to be picked up by the recipe. This differs from syncing the opportunity only when its status changes to `Closed Won` for the first time.

> **TRIGGER CONDITION USAGE WITH BATCH/BULK TRIGGERS**
> 
> Trigger conditions aren't recommended for batch triggers because they only evaluate the **first record** in each batch, not all records.
> 
> This may lead to unexpected behavior:
> 
> - If the first record meets your condition, Workato processes the entire batch (even if other records don't meet it)
> - If the first record doesn't meet it, Workato skips the entire batch (even if other records do meet it)
> 
> ![Trigger condition on batch trigger](/assets/trigger-condition-batch.Csul8ltm.png)_Example: This trigger condition only evaluates the first record in each batch_
> 
> **What to use instead:** Use your app's built-in filtering options. For example, with Salesforce batch triggers, use the **SOQL WHERE clause** field to filter records before they're batched. This ensures all records in the batch meet your criteria.
> 
> Trigger conditions also aren't recommended for bulk triggers.

#### Set a trigger condition

Complete the following steps to set a trigger condition:

1. Click the **Set trigger condition** toggle.
   
   ![Configure trigger filter](/assets/configure-trigger-filter.C5m9DopV.png)_Click the **Set trigger condition** toggle to configure trigger condition fields_
   
2. Open the **Recipe data** menu and map the datapill for your trigger condition to the **Trigger data** field.
   
3. Use the **Condition** drop-down menu to select a trigger condition. For more information on the conditions you can select, see [Conditions](/en/features/conditions).
   
4. Enter the value for your trigger condition in the **Value** field.
   
   For example, the following trigger condition ensures that only Salesforce accounts with a `Warm` rating value will be picked up by the trigger. Values are case-sensitive and must be exact.
   
   ![Define trigger filter](/assets/define-trigger-condition.BJC_sQKD.png)_Define the trigger condition_
   
5. To add another trigger condition, select **+**, then select **AND** or **OR**. The selected operator will define how all additional trigger conditions will be added.
   
   ![Adding trigger filter](/assets/adding-trigger-filter-with-or.BdrpKhOZ.png)_Adding another trigger condition with the OR operator_
   
6. Define the additional trigger condition. Values are case-sensitive and must be exact.
   
   The following trigger condition ensures that accounts with a `Hot` rating value will also be picked up by the trigger. Notice that from the third trigger condition and onward, trigger conditions will be combined with the previously selected operator (**OR** or **AND**).
   
   ![Define additional trigger condition](/assets/define-additional-trigger-condition.DT7coCws.png)_Define the additional trigger condition. Subsequent trigger conditions have to use the same AND operator_

---
