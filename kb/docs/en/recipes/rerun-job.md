---
url: 'https://docs.workato.com/en/recipes/rerun-job.md'
description: >-
  Learn how to rerun jobs in Workato, including scenarios, limitations, and best
  practices.
---

# Rerunning jobs

Workato provides the ability to rerun jobs, allowing the trigger event to go through the sequence of actions in the recipe again. This feature is useful in the following scenarios:

- Testing an edited recipe
- Rerunning a failed job after fixing the issue

> **RERUNNING JOBS MAY CREATE DUPLICATES**
> 
> When you rerun a job, the trigger event reprocesses the entire recipe. This may result in duplicate records. Verify and remove any duplicates before proceeding.

## How to rerun jobs

You can rerun jobs from two locations:

- [The job report](#job-report)
- [The job details page](#job-details)

### Rerun a job from the job report

Complete the following steps to rerun a job from the job report:

1. Select a recipe and go to the **Jobs** tab.
   
2. Select the checkbox next to the job you plan to repeat.
   
3. Click **Repeat job**.
   
   ![Job rerun from jobs report page](/assets/job-rerun-from-report.2jjOqnHL.png)_Rerunning jobs from jobs report page_
   

### Rerun a job from the job details page

Complete the following steps to rerun a job from the job details page:

1. Select a recipe and go to the **Jobs** tab.
   
2. Select a job to open the job details page.
   
3. Click **Repeat this job**.
   
   ![Job rerun from job details page](/assets/job-rerun-from-details.BRJ8FDWI.png)_Job rerun from job details page_
   

> **JOB RERUNS ARE IN-PLACE**
> 
> Job reruns maintain their original position in the job report. For example, a job first processed in August and rerun in September will still appear in the August jobs list.

## Cached trigger data in job reruns

All job reruns use cached data, meaning:

- The trigger event's original data is reused.
- Any changes made to the trigger event in the source application after the original job execution won't be reflected in the rerun.

## When should I not rerun a job?

Some scenarios where rerunning a job won't resolve your issues include:

- [Data issues in the trigger event](#data-issues)
- [Changes to the trigger event](#trigger-changes)

### Data issues in the trigger event

If the failed job resulted from incorrect trigger data, rerunning the job won't fix the issue. The same faulty data will be processed again, leading to failure.

### Changes to the trigger event

If you update the trigger event in the source app and intend for the recipe to process the new data, rerunning the job won't work. Instead:

- **For new object triggers**: Delete and recreate the object.
  
- **For new/updated object triggers**: Update the existing object so the recipe picks up the changes.
  

A new job will be created in these cases rather than modifying the cached data of the original job.

## View job rerun history

The job details page includes a job rerun history:

![Jobs history](/assets/jobs-history.BHyH_QIJ.png)_Jobs history_

If the job rerun is not the latest version, the **Repeat this job** button will be unavailable.

## Common use cases for rerunning jobs

- [Testing a new recipe](#testing-a-new-recipe)
- [Handling errors](#handling-errors)

### Testing a new recipe

When building or modifying a recipe, test different conditions by rerunning jobs. If your recipe includes conditional actions, ensure you test all logical branches.

For example, in the following recipe:

- A Salesforce account with a matching Zendesk organization follows steps 3-4.
- A Salesforce account without a matching Zendesk organization follows steps 5-7.

![Example recipe](/assets/example-recipe.D4jIpsfj.png)_Recipe with two logical branches. [Example recipe](https://www.workato.com/recipes/480358)_

To test both cases:

1. Create a Salesforce account without a matching Zendesk organization and check if steps 3-4 execute.
   
2. Update the same Salesforce account to have a matching Zendesk organization and check if steps 5-7 execute.
   

Using a **New object** trigger requires separate records for each test case, whereas a **New/updated object** trigger allows testing within a single record by updating it.

### Handling errors

If an error occurs during job execution and stops processing:

- Rerun the job to complete execution.
- If the error is due to incorrect trigger data, refer to the [Cached trigger data in job reruns](#cached-trigger-data-in-job-reruns) section.

If you've implemented an [error monitoring](/en/recipes/steps#handle-errors-step) step, it may help recover from errors automatically.

## Data retention policy

Workato's data retention policy applies to processed trigger events. Older jobs may not be available for reruns based on retention settings. Learn more about [data retention and its impact on job reruns](/en/security/data-protection/data-retention/#data-types).

---
