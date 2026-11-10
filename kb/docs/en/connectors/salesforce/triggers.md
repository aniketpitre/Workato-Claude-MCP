---
url: 'https://docs.workato.com/en/connectors/salesforce/triggers.md'
description: >-
  Explore triggers in the Salesforce connector for Workato, including new,
  updated, deleted, exported, and real-time change data capture records.
---

# Salesforce triggers

The Salesforce connector supports the following triggers:

> **DEPRECATION NOTICE PERTAINING TO REAL-TIME TRIGGERS**
> 
> Real-time triggers in Workato rely on Salesforce Workflow rules. These existing Workflow rules will continue to be supported. However, we recommend that all new recipes use Salesforce Flows, as Workflow rules and Process Builder have been [deprecated](https://admin.salesforce.com/blog/2021/go-with-the-flow-whats-happening-with-workflow-rules-and-process-builder) by Salesforce. There is a [migration tool](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_flow_mgmt_migrate_to_flow_tool.htm&type=5&release=236) to move your Workflow rules into Flows.
> 
> As the outbound messages configured in Salesforce will remain the same, the process should not affect Workato recipes. Nevertheless, we recommend testing the migration in the Salesforce sandbox account first to ensure that there are no unexpected issues.

## New/updated record

The [New/updated record](/en/connectors/salesforce/triggers/new-updated-record) trigger checks Salesforce for newly created or updated objects at an interval you specify.

## New record

The [New record](/en/connectors/salesforce/triggers/new-record) trigger checks Salesforce for newly created objects every five minutes.

## Deleted record

The [Deleted record](/en/connectors/salesforce/triggers/deleted-record) trigger monitors Salesforce for deleted objects of a type you specify. The object picklist only fetches soft-deleted records which remain in Salesforce for a limited period (typically 15 days) after deletion and are stored in the Recycle Bin.

## Export new records

The [Export new records](/en/connectors/salesforce/triggers/export-new-records) trigger monitors Salesforce for new records that match the SOQL WHERE clause you provide and retrieves them as a CSV stream. There is an expected delay when this trigger creates a job. The job processes after a query is completed in Salesforce.

## Export new/updated records

The [Export new/updated records](/en/connectors/salesforce/triggers/export-new-updated-records) trigger monitors Salesforce for newly created or updated records that match the SOQL WHERE clause you provide and retrieves them as a CSV stream. There is an expected delay when this trigger creates a job. The job processes after a query is completed in Salesforce.

## Monitor changes in a record (real-time)

The [Monitor changes in a record](/en/connectors/salesforce/change-data-capture-trigger) trigger monitors Salesforce [change data capture](/en/data-orchestration/change-data-capture) events in real-time for changes to object fields you specify. You can use this trigger to keep external systems in sync with Salesforce and perform specific actions based on the changed field and event type.

## New Outbound message (real-time)

The [New Outbound message](/en/connectors/salesforce/triggers/new-message) trigger monitors Salesforce in real-time for new Outbound messages.

## New PushTopic event (real-time)

The [New PushTopic event](/en/connectors/salesforce/triggers/new-event) trigger uses the [Salesforce Streaming API](https://developer.salesforce.com/docs/atlas.en-us.202.0.api_streaming.meta/api_streaming/intro_stream.htm) to monitor Salesforce in real-time for new PushTopic events in subscribed channels.

## New platform event (real-time)

The [New platform event](/en/connectors/salesforce/triggers/new-platform-event) trigger monitors Salesforce in real-time for new platform events. The trigger also fetches past platform events available in Salesforce by default when the recipe starts. Salesforce keeps high-volume platform events for up to 72 hours.

## New record (real-time)

The [New record](/en/connectors/salesforce/triggers/new-record-real-time) trigger monitors Salesforce in real-time for newly created objects.

## New records (batch)

The [New records](/en/connectors/salesforce/triggers/new-records-batch) trigger monitors Salesforce for newly created records and retrieves them in batches.

## New/updated record (real-time)

The [New/updated record](/en/connectors/salesforce/triggers/new-updated-record-real-time) trigger monitors Salesforce in real-time for newly created or updated objects.

## New/updated records (batch)

The [New/updated records](/en/connectors/salesforce/triggers/new-updated-records-batch) trigger monitors Salesforce for newly created or updated objects and retrieves them in batches.

## Scheduled record search using SOQL query WHERE clause (batch)

The [Scheduled record search using SOQL query WHERE clause](/en/connectors/salesforce/triggers/scheduled-search-soql-where) trigger searches Salesforce using a SOQL query WHERE clause on a schedule you specify and returns the results in batches.

## Scheduled records search using SOQL query (batch)

The [Scheduled records search using SOQL query](/en/connectors/salesforce/triggers/scheduled-search-soql) trigger searches Salesforce using a SOQL query on a schedule you specify.

## Threshold met for new records created (batch)

The [Threshold met for new records created](/en/connectors/salesforce/triggers/threshold-met-batch) trigger monitors Salesforce for when the number of newly created objects reaches a threshold you specify. When Salesforce reaches the new object threshold, Workato triggers a job, retrieves the newly created objects in batches, and waits for the number of new jobs to reach the threshold again.

---
