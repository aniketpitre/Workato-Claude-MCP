---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-lookup-tables.md'
description: >-
  Reference for the lookup tables in the ELT Pipeline for Snowflake accelerator,
  covering user access, systems, objects, jobs, and control tables.
---

# ELT Pipeline for Snowflake accelerator - Assets - Lookup tables

The ELT Pipeline for Snowflake accelerator has seven lookup tables that are common to both Slack and Microsoft Teams implementations of the accelerator:

- [ELT | User Access](#user-access-table)
- [ELT | Systems](#systems-table)
- [ELT | Objects](#objects-table)
- [ELT | JOB TABLE](#job-table)
- [ELT | ERROR LOGS](#error-table)
- [ELT | CONTROL TABLE | MAIN](#control-table-main)
- [ELT | CONTROL TABLE | CHILD](#control-table-child)

## **ELT | User Access**

The **ELT | User Access** lookup table contains the following fields:

<dl><dt>Email</dt><dd>The user's email address.</dd><dt>Active</dt><dd>The pipeline's status.</dd><dt>Pipelines Pinned</dt><dd>The pipelines the user has pinned to their <strong>App homepage</strong>.</dd><dt>Role</dt><dd>The user's role. <strong>Admin</strong> or <strong>Analyst</strong>.</dd></dl>

## **ELT | Systems**

The **ELT | Systems** lookup table contains the following fields:

<dl><dt>SYSTEM_ID</dt><dd>References the <strong>SYSTEM_ID</strong> in the <strong>ELT | Systems</strong> lookup table.</dd><dt>SYSTEM</dt><dd>The source system.</dd><dt>TYPE</dt><dd>The type of application (source).</dd><dt>CREATED_BY</dt><dd>The email address of the person who created the object.</dd><dt>CREATED_ON</dt><dd>Date when the object was created.</dd></dl>

## **ELT | Objects**

The **ELT | Objects** lookup table contains the following fields:

<dl><dt>SYSTEM_ID</dt><dd>References the <strong>SYSTEM_ID</strong> in the <strong>ELT | Systems</strong> lookup table.</dd><dt>OBJECT</dt><dd>The object used for the pipeline.</dd><dt>CREATED_BY</dt><dd>The email address of the person who created the object.</dd><dt>CREATED_ON</dt><dd>Date when the object was created.</dd><dt>PRIMARY_KEY</dt><dd>Custom Primary Key for SQL-type sources.</dd></dl>

## **ELT | JOB TABLE**

The **ELT | JOB TABLE** lookup table contains the following fields:

<dl><dt>ELT_CONTROL_ID</dt><dd>Unique ID auto-generated when you create a pipeline. This ID corresponds to the <strong>ELT_CONTROL_ID</strong> in the **ELT | CONTROL TABLE | MAIN** lookup table.</dd><dt>JOB_ID</dt><dd>Unique Job ID of the running pipeline.</dd><dt>BATCH_START_DT</dt><dd>Start date-time of the job.</dd><dt>BATCH_END_DT</dt><dd>End date-time of the job.</dd><dt>ROWS_AFFECTED</dt><dd>Total Rows processed. (Salesforce only)</dd><dt>IS_SUCCESS</dt><dd>This value indicates whether the job was successful. Boolean value (true/false).</dd><dt>DISPATCHER_JOB_URL</dt><dd>Job URL of the evaluated workload.</dd><dt>WORKLOAD_JOB_URL</dt><dd>Job URL of the respective workload called by the dispatcher.</dd></dl>

## **ELT | ERROR LOGS**

The **ELT | ERROR LOGS** lookup table contains the following fields:

<dl><dt>ELT_CONTROL_ID</dt><dd>Unique ID auto-generated when you create a pipeline. This ID corresponds to the <strong>ELT_CONTROL_ID</strong> in the <strong>ELT | CONTROL TABLE | MAIN</strong> lookup table.</dd><dt>JOB_ID</dt><dd>Unique Job ID of the running pipeline.</dd><dt>ERROR_MSG</dt><dd>Error message on failure.</dd><dt>ERROR_CODE</dt><dd>Error code of failure. Use to determine reprocessing logic.</dd><dt>JOB_URL</dt><dd>URL of the failed job.</dd><dt>ACTION</dt><dd>Dependent on the error code. Use to determine reprocessing logic. Actions can include notifications.</dd></dl>

## **ELT | CONTROL TABLE | MAIN**

The **ELT | CONTROL TABLE | MAIN** lookup table contains the following fields:

<dl><dt>ELT_CONTROL_ID</dt><dd>Unique ID auto-generated when you create a pipeline.</dd><dt>SOURCE_SYSTEM_NAME</dt><dd>Source system where the data originates.</dd><dt>SOURCE_OBJECT_NAME</dt><dd>Name of the desired data entity. This is usually a table or file name in the case of file source systems.</dd><dt>TARGET_TABLE_NAME</dt><dd>The table where the accelerator loads the data.</dd><dt>LOAD_TYPE</dt><dd>Type of the load.</dd><dd><dl class="horizontal-dl"><dt>Allowed values:</dt><dd>Full, incremental, or extract.</dd></dl></dd><dt>STATUS</dt><dd>Pipeline status.</dd><dd><dl class="horizontal-dl"><dt>Allowed values:</dt><dd>Pending, Active, Inactive, Error, Processing, or Extract</dd></dl></dd><dt>COMM</dt><dd>Communication channel (Slack or Microsoft Teams)</dd><dt>CREATED_BY</dt><dd>Email of the user who created the pipeline.</dd><dt>UPDATED_BY</dt><dd>Email of the user who updated the pipeline.</dd></dl>

## **ELT | CONTROL TABLE | CHILD**

The **ELT | CONTROL TABLE | CHILD** lookup table contains the following fields:

<dl><dt>ELT_CONTROL_ID</dt><dd>Unique ID auto-generated when you create a pipeline. This ID corresponds to the <strong>ELT_CONTROL_ID</strong> in the **ELT | CONTROL TABLE | MAIN** lookup table.</dd><dt>PIPELINE_CREATED_DT</dt><dd>Date when the pipeline is created.</dd><dt>PIPELINE_UPDATED_DT</dt><dd>Date when the pipeline is updated.</dd><dt>HOUR</dt><dd>Hour of the day selected.</dd><dt>MINUTE</dt><dd>Minute of the hour of the day selected.</dd><dt>FREQUENCY</dt><dd>How frequently the pipeline runs.</dd><dd><dl class="horizontal-dl"><dt>Allowed values:</dt><dd>Daily, Weekly, Monthly, Hourly, or Yearly</dd></dl></dd><dt>START_TIME</dt><dd>The time when the user schedules the pipeline to start.</dd><dt>NEXT_TIME</dt><dd>The next time the pipeline must run.</dd><dt>LAST_SUCCESSFUL_JOB_URL</dt><dd>Jobs are sub-tasks in a pipeline. The accelerator records them on the first and subsequent runs. The accelerator updates this value when a job finishes successfully.</dd><dt>LAST_SUCCESSFUL_JOB_DT</dt><dd>Last time the job ran successfully.</dd></dl>

---
