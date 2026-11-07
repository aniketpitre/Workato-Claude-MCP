---
url: 'https://docs.workato.com/en/recipes/viewing-jobs-faqs.md'
description: >-
  Answers to common questions about viewing Workato recipe jobs, including job
  reports, metadata, statuses, and data retention.
---

# Viewing Jobs FAQs

Get answers to frequently asked questions about viewing jobs.

What is a Recipe Job in Workato?

A [Recipe Job](/en/recipes/jobs#recipe-jobs) in Workato is created when an active recipe processes a trigger event and runs a series of actions. Each job holds a unique trigger event and executes its recipe logic based on that data.

How can I view job reports in Workato?

[To view job reports](/en/recipes/jobs#viewing-job-reports), click the **Jobs** tab in your recipe to open the Jobs report page. You can view details about specific jobs, customize reports, and repeat (rerun) jobs.

What is the data retention policy for job reports in Workato?

Job reports in Workato are retained according to your account's data retention policy. The duration for which the data is kept depends on the specific settings of your [Workato account](https://app.workato.com/).

Can I customize job reports in Workato?

Yes. You can [customize job reports](/en/recipes/jobs#customizing-job-reports) to show up to 10 additional columns, which can include any data available in the recipe.

What kind of metadata and statuses are included in job details?

The Job details page includes [metadata](/en/recipes/jobs#job-metadata-and-statuses) such as:

- Job ID
- Start time
- Recipe version
- Status
- Duration
- Tasks used
- Rerun number

[Job statuses](/en/recipes/jobs#job-statuses) are:

- Completed
- Failed
- Processing
- Paused
- Aborted

How are paused jobs handled in Workato?

[Paused jobs](/en/recipes/jobs#paused-jobs) occur when a recipe containing long actions is stopped. These jobs resume when the recipe is restarted, continuing with the same recipe version they began with.

Can I rerun a failed job?

Yes. You can [rerun jobs](/en/recipes/rerun-job#rerunning-jobs). When you rerun a job, the trigger event runs through the sequence of actions in the recipe again. Duplication may occur, so be sure to check and remove duplicates (if present) before re-running the job.

Why is my job stuck in processing status?

Some jobs may take a long time to complete. This can happen if the recipe is:

- Processing bulk data using [long actions](/en/recipes/long-actions)
- [Waiting for an recipe function](/en/connectors/recipe-functions/actions/wait-for-async-calls) to resolve
- Using a dedicated [waiting step](/en/features/scheduler#actions) from Scheduler by Workato

In such cases, the job may take a several minutes or hours to complete. It may even exceed the [normal timeout limit](/en/recipes/jobs#timeouts).

---
