---
url: 'https://docs.workato.com/en/connectors/workday/scheduled_report.md'
description: >-
  The Scheduled report trigger in the Workday connector runs a
  Report-as-a-Service report at defined intervals and returns the output in
  batches.
---

# Workday - Scheduled report trigger

The **Scheduled report** trigger runs a Workday Report-as-a-Service (RaaS) report at defined intervals. This trigger combines Workato's advanced scheduler with Workday's reporting API to retrieve data from a custom report.

The trigger returns results in [batches](/en/features/batch-processing). The batch size defaults to `200` and can be increased up to `10,000`.

## Input

| Input field | Description |
| --- | --- |
| Report URL | Enter the full RaaS (Report-as-a-Service) report URL from the **View URLs Web Service** page in Workday. [Learn how to retrieve this URL.](/en/connectors/workday/workday_raas). Workato uses this to fetch the report output. This must be a static string to enable automatic schema detection. |
| Schedule | Select the schedule for when the report runs. |
| Time zone | Select the time zone used to evaluate the scheduled run. |
| Hour | Enter the hour (in 24-hour format) when the report should run. Defaults to `00` (midnight). |
| Minute | Enter the minute past the hour. Use `00` for the top of the hour. |
| Day of month | Enter the day (1–31) of the month the report should run. Values above the last day of a given month are rounded down. Defaults to `1`. |
| Days of week (Sunday–Saturday) | Select **Yes** or **No** for each day to control which weekdays the schedule includes. All days default to Yes. |
| Format | Select the output format of the report. Options include **CSV** (default) or **JSON**. |
| Detect report schema automatically | Select **Yes** or leave blank to detect the report's input and output schema automatically. This only works if the **Report URL** is a static string. Schema detection doesn't run if the URL uses a datapill. |
| Remove empty fields | Select **Yes** to exclude fields with `null` values from the output. Defaults to **Yes**. |
| Additional fields | Add report fields that do not appear in the output schema automatically. You can define fields using JSON format or input them manually. |
| Replace report fields | Select Yes to replace fields in the original schema with any fields you added in **Additional fields**, if names match. |
| Report batch size | Define the number of rows to return in each batch. Defaults to 200. The maximum is 10,000. |

## Outputs

This trigger returns a number of fields:

| Field | Description |
| --- | --- |
| Scheduled time | The time that the report was ran. |
| Total number of records | The total number of rows generated in the scheduled run of the report. If this report has more rows than the specified batch size, they will be split into multiple batches with the specified number of rows in each. Each batch will then be processed as individual jobs, in the same sequence as returned by the Workday RaaS endpoint. |
| Starting offset | The offset number for the first row of this batch. For example, if there are `1000` rows in the report and the trigger uses a batch size of `200`. Given that, if the current job is showing the 2nd batch (rows `201` to `400`), the starting offset will be `200`. |
| Ending offset | The offset number for the last row of this batch. For example, if there are `1000` rows in the report and the trigger uses a batch size of `200`. Given that, if the current job is showing the 2nd batch (rows `201` to `400`), the ending offset will be `400`. |
| First batch | A boolean value indicating if this is the first batch. |
| Last batch | A boolean value indicating if this is the last batch. |
| Rows | Each batch of rows is returned as a list (array). Each item in this list corresponds to a row in the report. Similarly, each column in your report will be rendered as a field in the output datatree. |

#### Using first/last batch in your recipe logic

You can use the values from **first batch** and **last batch** and integrate them into your recipe logic. For example, this is useful when you want to create a file from the output of a Workday report. Your recipe will contain the following logic:

if `First batch` is `true`

- Create a new file with contents of the first batch

if `First batch` is `false`

- Append lines to an existing file

if `Last batch` is `true`

- Send notification about successful transfer of report content

## Limitations

Based on the [Workday documentation](https://doc.workday.com/r/3DMnG~27o049IYFWETFtTQ/sGhnezv85Vfp9LabNN~EWw), there is a quota of 2GB for advanced custom report enabled for web services and exposed for integrations.

## Scheduling reference

This trigger uses the advanced scheduler. Refer to the [Scheduler trigger documentation](/en/features/scheduler) to learn more about setting up complex schedules.

---
