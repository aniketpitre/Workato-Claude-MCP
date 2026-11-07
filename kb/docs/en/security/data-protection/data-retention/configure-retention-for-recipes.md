---
url: >-
  https://docs.workato.com/en/security/data-protection/data-retention/configure-retention-for-recipes.md
description: >-
  Configure the Jobs data retention setting at the recipe level in Workato to
  control whether job data is stored for individual recipes.
---

# Recipe-level data retention

Workato enables you to configure job data storage at the recipe level. This feature is useful for organizations with strict requirements for external data storage or API performance. Workato provides enhanced control over compliance, performance, and operational efficiency with this feature.

You can do the following with the **Jobs data retention** recipe setting:

- Comply with your organization's data protection and security standards.
- Ensure that sensitive data isn't stored outside your firewall.
- Decrease the latency of an [API recipe](/en/api-mgmt/api-recipes/).

In this guide, we'll cover how:

- [The Jobs data retention setting works](#basics)
- [To enable it for your recipes](#configuration)

* * *

## Basics

- [How does the Jobs data retention setting work?](#how-it-works)
- [How is data affected?](#affected-data)
- [How are test jobs affected?](#test-jobs)
- [How are repeated jobs affected?](#job-reruns)
- [How can I troubleshoot job failures?](#job-failures)
- [Will changing a recipe's retention setting affect existing data?](#existing-data)
- [How can I configure a recipe's data retention setting?](#configuration)

### How does the Jobs data retention setting work?

The **Jobs data retention** recipe setting defines if Workato stores job data for the recipe.

This setting, located in a recipe's **Settings > Data retention** tab, has three options:

- **[Default retention policy](/en/security/data-protection/data-retention/#workato-retention-policy)**. Your workspace's data retention policy applies when this option is selected. For example, if the retention policy is **30 days**, the recipe's data is retained for 30 days from the job's completion date.
  
- **Do not store trigger event only**: Workato doesn't store trigger event data when you select this option. This improves recipe performance while keeping job step data for troubleshooting. You won't be able to rerun jobs.
  
- **Do not store any data**. Workato doesn't store any data for the recipe when this option is selected. You might select this option to:
  
  - Manage risk associated with storing sensitive or personally-identifying data.
  - Decrease the latency of an [API recipe](/en/api-mgmt/api-recipes/) by skipping log creation.
  
  **Before selecting this option**, make sure the recipe doesn't require job logs. See the [How is data affected?](#affected-data) section for more information.
  

### How is data affected?

When you select **Do not store any data**, certain types of data or features in Workato may be modified or entirely unavailable. This changes jobs in the following ways:

- [**Job history summary**](/en/security/data-protection/data-retention/#job-history-summaries): No change. Job ID, history, and duration remain visible in the recipe's **Jobs** tab.
  
- [**Job history details**](/en/security/data-protection/data-retention/#job-history-details): Step inputs and outputs are unavailable, including for [recipe triggers](/en/security/data-protection/data-retention/#trigger-events):
  
  ![Job History Details page with retention disabledd](/assets/no-step-details.De0dBjCf.png)_Job History Details page with retention disabled_
  
  This is also true when a job fails:
  
  ![Job History Details page with retention disabled job failure](/assets/step-details-job-failed.CUtvlVsv.png)_Failed job on Job History Details page with retention disabled_
  
  Error information for failed jobs is only available for [test jobs](#test-jobs).
  
- [**Customized job reports**](/en/security/data-protection/data-retention/#customized-job-reports): Customized job report data is unavailable. This applies to jobs completed after you deactivate recipe-level data retention.
  
  Consider the following example. Non-test jobs completed after retention was deactivated are highlighted. Notice that the custom job report data isn't present for these jobs:
  
  ![Customized job reports with retention disabled](/assets/customized-job-report.C8XjC_dv.png)_Customized job reports with retention disabled_
  

### How are test jobs affected?

Deactivating recipe-level data retention doesn't affect test jobs, as test job data is stored to support testing and troubleshooting while building. Instead, your workspace's data retention policy applies to the retained test job data.

For example, consider the job history in the following image. Retention was deactivated for this recipe beginning with the **4:58:23 PM** job. Highlighted is a test job that was completed after retention was deactivated:

![Test job with retained data](/assets/test-job.BpB_zE4N.png)_Test job with data retained_

And the **Job history details** page for the job:

![Job history details page for test job](/assets/test-job-details.DbSNIQN6.png)_Job history details page for test job_

If a test job fails, details about the failure, including error messages, and IDs are visible on the **Job history details** page:

![Job history details page for failed test job](/assets/test-job-failed.CxYBHre1.png)_Job history details page for failed test job_

### How are repeated jobs affected?

You can't repeat a failed job if recipe-level data retention is deactivated, as no data will be available to perform the rerun:

![Disabled Repeat this job button in Job Details page](/assets/disabled-repeat-job.zOrKteTT.png)_Disabled Repeat this job button on the Job Details page_

### How can I troubleshoot job failures?

When retention is deactivated, error information is available only for test jobs, not for actual recipe runs. To avoid issues while your recipe is running, we recommend the following:

- Thoroughly test each recipe step during development.
- Add [error handling](/en/recipes/steps#handle-errors-step) steps into your recipe to account for potential issues during recipe execution.

Additionally, note that failed jobs [can't be repeated](#job-reruns) when you deactivate retention.

### Will changing a recipe's retention setting affect existing data?

No. Updating the **Jobs data retention** setting affects recipe data created **after** the setting has been updated.

For example, if you select the **Do not store any data** option for a recipe's data retention setting, the recipe's existing data will be retained until your [workspace's data retention period](/en/security/data-protection/data-retention/#workato-retention-policy) has passed. New data created after the setting is updated won't be stored.

This is demonstrated in the following screenshot. Retention was deactivated for this recipe beginning with the **4:58:23 PM** job. Jobs completed before this retain their data:

![Jobs before retention was disabled with data retained](/assets/retained-history.C_a2gacp.png)_Jobs before retention was disabled with data retained_

* * *

## Configure recipe data retention

Complete the following steps to configure data retention at the recipe level:

1. Select a recipe in your Workato workspace.
   
2. **If the recipe is currently running**, click **Stop recipe** before proceeding.
   
3. On the recipe's details page, click **Settings > Data retention**:
   
   ![Recipe-level data retention policy](/assets/recipe-data-retention-policy.dsiUjwwn.png)_Recipe-level data retention policy_
   
4. In the **Jobs data retention** field, select one of the following options:
   
   - **Default retention policy**: Data for the recipe is retained according to the [workspace's data retention policy](/en/security/data-protection/data-retention/#workato-retention-policy) if this option is selected. For example, if the workspace's retention policy is 45 days, data for the recipe is retained for 45 days from the job's completion date.
   - **Do not store trigger event only**: Workato doesn't store trigger event data when you select this option. This improves recipe performance while keeping job step data for troubleshooting. You won't be able to rerun jobs.
   - **Do not store any data**: Recipe data created after saving won't be stored if this option is selected.
5. Click **Save**.
