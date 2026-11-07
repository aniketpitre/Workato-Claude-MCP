---
url: 'https://docs.workato.com/en/connectors/salesforce/salesforce-generic.md'
description: >-
  Explore actions in the Salesforce connector for Workato, including uploading
  files and creating, updating, upserting, and deleting records.
---

# Salesforce actions

The Salesforce connector supports the following actions:

## Upload file

The [Upload file](/en/connectors/salesforce/actions/upload-file) action uploads a file to Salesforce.

## Create record

The [Create record](/en/connectors/salesforce/actions/create-record) action creates a record in Salesforce.

## Update record

The [Update record](/en/connectors/salesforce/actions/update-record) action updates a record in Salesforce by its ID.

## Upsert record

The [Upsert record](/en/connectors/salesforce/actions/upsert-record) action searches Salesforce records using a field you specify as the primary key. If a matching record is found, it is updated. If a matching record isn't found, one is created.

## Approve record in approval process

The [Approve record in approval process](/en/connectors/salesforce/actions/approve-record) action approves a Salesforce record and triggers all steps in the approval process.

## Create records in batches (batch)

The [Create records in batches](/en/connectors/salesforce/actions/create-records-in-batches) action creates Salesforce records in batches. Each job can create up to 2,000 records in 10 batches of 200.

## Create records in bulk from CSV file

The [Create records in bulk from CSV file](/en/connectors/salesforce/actions/create-records-from-csv) action creates Salesforce records in bulk from a CSV file.

## Delete record

The [Delete record](/en/connectors/salesforce/actions/delete-record) action deletes a Salesforce record by its ID.

## Download attachment

The [Download attachment](/en/connectors/salesforce/actions/download-attachment) action retrieves the contents of an attachment in Salesforce. The maximum attachment size is 25 MB.

## Download file

The [Download file](/en/connectors/salesforce/actions/download-file) action retrieves the contents of a file in Salesforce.

## Get object schema

The [Get object schema](/en/connectors/salesforce/actions/get-object-schema) action retrieves the schema of a standard or custom object in Salesforce. Use this action when you need to replicate a Salesforce object's fields in a data warehouse.

## Get record details by ID

The [Get record details by ID](/en/connectors/salesforce/actions/get-record-details) action retrieves the details of a Salesforce record by its ID.

## Get related list by parent record ID (batch)

The [Get related list by parent record ID](/en/connectors/salesforce/actions/get-related-list) action retrieves a related list of a Salesforce record in batches using a parent record's ID. In Salesforce, a related list is usually a child object that has a lookup or master-detail relationship to a parent record.

## Get report by ID

The [Get report by ID](/en/connectors/salesforce/actions/get-report) action retrieves columns and rows from a Salesforce report.

## List data category groups (batch)

The [List data category groups](/en/connectors/salesforce/actions/list-category-groups) action retrieves all data category groups from Salesforce in batches.

## Publish platform event

The [Publish platform event](/en/connectors/salesforce/actions/publish-platform-event) action publishes a platform event message in Salesforce.

## Reject record in approval process

The [Reject record in approval process](/en/connectors/salesforce/actions/reject-record) action rejects a Salesforce record and triggers all steps in the rejection process.

## Retrieve data category group hierarchy (batch)

The [Retrieve data category group hierarchy](/en/connectors/salesforce/actions/retrieve-category-group-hierarchy) action retrieves a data category group hierarchy from Salesforce using a source list.

## Retry bulk job for failed records from CSV file

The [Retry bulk job for failed records from CSV file](/en/connectors/salesforce/actions/retry-job-csv) action retries failed Salesforce jobs in bulk from a CSV file. Use this action after another Salesforce bulk action to resubmit failed records as a new bulk job.

## Search records (batch)

The [Search records](/en/connectors/salesforce/actions/search-records) action retrieves a list of Salesforce records that match the search criteria you provide. Each job can retrieve up to 2,000 records.

## Search records in bulk using SOQL query

The [Search records in bulk using SOQL query](/en/connectors/salesforce/actions/search-records-soql) action retrieves a CSV stream of Salesforce records that match the SOQL query you provide.

## Search records using SOQL query (batch)

The [Search records using SOQL query](/en/connectors/salesforce/actions/search-records-soql-batch) action retrieves a list of Salesforce records that match the SOQL query you provide. Each job can retrieve up to 2,000 records.

## Search records using SOQL query WHERE clause (batch)

The [Search records using SOQL query WHERE clause](/en/connectors/salesforce/actions/search-records-soql-where) action retrieves a CSV stream of Salesforce records that match the SOQL WHERE clause you provide. Each job can retrieve up to 2,000 records.

## Submit record for approval

The [Submit record for approval](/en/connectors/salesforce/actions/submit-record) action submits a record for approval in Salesforce. This action is equivalent to clicking `Submit for approval` on a record in Salesforce.

## Update records in batches (batch)

The [Update records in batches](/en/connectors/salesforce/actions/update-records-in-batches) action updates Salesforce records in batches. Each batch can update up to 2,000 records in 10 batches of 200.

## Update records in bulk from CSV file

The [Update objects in bulk from CSV file](/en/connectors/salesforce/actions/update-records-csv) action updates Salesforce records in bulk from a CSV file.

## Upsert records in batches (batch)

The [Upsert records in batches](/en/connectors/salesforce/actions/upsert-records-batch) action upserts Salesforce records in batches. Each batch can upsert up to 2,000 records in 10 batches of 200. If matching records are found, they are updated. If matching records aren't found, they are created.

## Upsert records in bulk from CSV file

The [Upsert objects in bulk from CSV file](/en/connectors/salesforce/actions/upsert-records-in-bulk-from-csv) action upserts Salesforce records in bulk from a CSV file and a primary key. If matching records are found, they are updated. If matching records aren't found, they are created.

---
