---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-create.md'
description: >-
  Create a new data pipeline in the ELT Pipeline for Snowflake accelerator by
  choosing a source system and load type from the App homepage.
---

# Create a pipeline

You can create a new pipeline from the **App homepage**.

1. Open Slack or Microsoft Teams and navigate to your **App homepage**.
   
2. Select **Create Pipeline**.
   
3. Select a **Source System**. We preconfigured this accelerator to support the following sources:
   
   - Salesforce
   - MS SQL
   - MS Windows file system
4. Select a **Load Type** from the list of available options.
   
   <dl><dt>Full load (FULL)</dt><dd>Full refers to a full extract of the source table every time a job runs. These types of jobs usually do not have a start date. You can determine their frequency when you create the pipeline. For example, you can assign small to medium-sized lookup tables, including currency, or codes, to <strong>full load</strong>.</dd><dt>Incremental Load(INCR)</dt><dd>All incremental jobs begin with a full refresh. The refresh syncs the source to the target, and then the pipeline switches to incremental using the time/date-based CDC approach. You can determine INCR frequency when you create the pipeline. Rather than refresh the entire extract every time a job runs, the accelerator picks up the data that has changed after the last time the pipeline ran. For example, consider a scenario where you migrate an<strong> opportunities table from Salesforce</strong> completely and set the load frequency to daily. In this situation, only daily data changes are extracted and merged.</dd><dt>Extract Load (EXTR)</dt><dd>Extract loads pull data from within a given time frame, usually between two timestamps. You can use this load type to build custom reports, including audits.</dd></dl>
   
5. The **Create Pipeline** interface appears.
   
   Configure the following input fields in the **Create Pipeline** interface:
   
   <dl><dt>Source object</dt><dd>Object from the source system, such as contacts or accounts.</dd><dd><dl class="horizontal-dl"><dt>Sample values:</dt><dd>Lead, contact, or account.</dd></dl></dd><dt>Destination table/object</dt><dd>Name of the Snowflake table you plan to load data to. The name you choose must adhere to <a href="https://docs.snowflake.com/en/sql-reference/identifiers.html#:~:text=An%20identifier%20is%20a%20string,queries%20and%20DDL%2FDML%20statements">Snowflake naming conventions</a> and avoid double quotes (<code>"</code>).</dd><dd><dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>salesforce_leads_table_20220204170134</code></dd></dl></dd><dt>Start date</dt><dd>Pipeline start date relative to user's <a href="/en/accelerator-elt-pipeline-timezone.html">timezone</a>.</dd><dd><dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>2021-02-04</code></dd></dl></dd><dt>Start hours, minutes</dt><dd>Defines the pipeline start time. This value is relative to the Workato account owner's <a href="/en/accelerator-elt-pipeline-timezone.html">timezone</a>.</dd><dd><dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>11,30</code></dd></dl></dd><dt>End date (optional)</dt><dd>For extract pipelines, the <strong>end date</strong> specifies the end of the extraction timeframe. Not applicable to full load or incremental load pipelines.</dd><dd><dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>2021-02-04</code></dd></dl></dd><dt>End hours, minutes (optional)</dt><dd>Not applicable to full load or incremental load.</dd><dd><dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>15,25</code></dd></dl></dd><dt>Frequency</dt><dd>Defines the frequency at which the pipeline runs.</dd><dd><dl class="horizontal-dl"><dt>Can be one of:</dt><dd><ul><li>Hourly</li><li>Daily</li><li>Weekly</li><li>Monthly</li><li>Yearly</li></ul></dd></dl></dd></dl>
   
6. Click **Create**.
   
7. After you create the pipeline, the ELT Pipeline bot sends you a message containing the message format.
   
   ```
   ELT Control ID: 6f51a574-b52-426e-992d-2c06414eebe
   Source System: Salesforce
   Source Object: Lead
   Target Table: Leads_Test
   Start Date: 2022-05-18T00:00:00.000000-07:00
   Start Date Hours: 07
   Start Date Minutes: 55
   Frequency: MONTHLY
   ```

---
