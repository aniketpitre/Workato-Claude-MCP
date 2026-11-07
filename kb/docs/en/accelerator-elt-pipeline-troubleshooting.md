---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-troubleshooting.md'
description: >-
  Tips and troubleshooting for the ELT Pipeline for Snowflake accelerator,
  covering source, target, staging, schema, and control table setup.
---

# ELT Pipeline for Snowflake accelerator - tips and troubleshooting

## Source

### Customize the source system

If you want to use a different source system than Salesforce, you can use the Salesforce recipe as a model to guide your development. Salesforce uses bulk actions and triggers. If the source you plan to use does not have bulk functionality, you can modify your recipe to include pagination inside the Workato recipe as a workaround.

### File system sources

If you are using a file system as the source, an OPA enables you to run existing on-prem files or on-prem command-line scripts. You can also use the scheduler to move files from the on-prem network file system to S3 or Snowflake's internal file system. The on-prem files connector also offers pattern matching for filtering files. Refer to our [On-prem files](/en/connectors/on-prem-files#on-prem-files) and [On-prem command line](/en/connectors/on-prem-command-line-scripts#execute-command-line-script-action) documentation for information to guide you.

### Database source system

Using a database as a source, the ELT Accelerator demonstrates Workato’s cloud and on-prem connector for the SQL server. This method avoids putting strain on the database. If you plan to use other databases as a source, you can use recipes in the ELT accelerator as an example. You can implement other databases as a source, depending on the availability and maturity of the connector.

## Target

Target tables are more refined versions of the raw tables the accelerator initially extracts from the source. You can use Workato's connectors library and sample recipes to help you extend targets to other connectors. Check the connector details to see if the bulk write to data lake/data warehouse capability is already part of the connector.

After Workato extracts the data, you can use other tools available on the market to manage data pipelines, SQL code repositories, and to support parameterization. These tools include GIT, DBT, Dataform, and LookerML.

## Staging

You can use Workato's connectors to support multiple staging areas. For example, users may decide to use a combination of S3, Snowflake, or on-prem internal file system recipes. Further, you can use this accelerator's ELT framework to schedule and dispatch warehouse refined-data, and integrated and merged tables. You can also configure the accelerator to fire SQLs and Lambdas on the platform of your choice, such as Snowflake and AWS Lambda.

## Schema preprocessing

Preserving the schema and metadata from the source system is one of the key challenges users face regarding data replication.

This accelerator provides a solution to preserving the schema and metadata by processing the schema from the **Source System > Replicating schema** to **Snowflake > LOAD**.

## Control table

Using ELT as a starting point, you can extend control tables to support chaining tasks and idempotency.

If you need to track additional metrics or statuses while running the workflow your team requires, add them to the control table.

## Job table

Using ELT as a starting point, you can extend job tables to support chaining tasks and idempotency.

If you need to track additional metrics or statuses while running the workflow that your team requires, add them to the control table.

## Dispatcher

You can develop more source recipes and add them to the dispatcher. Refer to the dispatcher recipe logic to add recipes for **FULL** and **Incremental/Extract** job types.

You can define more fine-grained notifications and errors and add them to the dispatcher.

When you are scheduling jobs, ensure that their timeframes don't overlap. If jobs overlap, the accelerator adds jobs to the queue. This delays processing the jobs.

## Scheduler

The scheduler has a single concurrency, and should run at all times to avoid pipeline failures.

You can add additional pipeline and jobs metadata to the scheduler with the Control and Jobs table. You can filter the scheduler while using it with the control table.

You can use the scheduler to customize additional errors and notifications.

## Notifications

You can customize the notifications that the ELT Pipeline bot sends in Slack or Microsoft Teams. We have preconfigured this accelerator to send notifications when a user **Creates** or **Starts** a pipeline and when a pipeline **Completes**.

You can customize notifications to add more information. By default, the **Create**, **Start**, and **Completed** notifications only describe the pipeline's name and the **load type**.

You can also configure this accelerator to pass notifications to your organization's service and ticketing systems.

## Latency and bandwidth of source/target systems

Frequent extraction of high volumes from source/target systems is subject to API rate limits, slow downloads, and connection timeouts.

You should schedule pipelines to run during times that don't impact business operations.

Adding additional resources to a source or target system should boost performance.

OPA-based extract systems depend on the network and write throughput of the target S3 bucket or Snowflake. Adding more threads and creating virtual private networks should boost the extract rate.

## Handling changes in a source system

You must customize this accelerator to store the state of a particular schema.

Only Salesforce supports schema replication and management.

## CDC handling deletes

If the source application supports deletes, it provides a **last modified date**. Some source applications support soft deletes. In this scenario, the date when the record was retired or deactivated is available in the source.

You can configure triggers to capture deletes and load them to a separate table in source databases. You must configure them from the customer's end.

## Bots

We recommend you use an enterprise bot because it has all the required features to manage an ELT Pipeline from Slack or Microsoft Teams. If you do not have an enterprise bot, you can use a regular workbot. If you plan to use a regular workbot, you must fire commands instead of using a central dashboard, as with the Enterprise workbot. The other method to control the pipeline is to use lookup tables. This method is error-prone and not recommended.

---
