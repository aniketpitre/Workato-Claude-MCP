---
url: 'https://docs.workato.com/en/security/data-protection/data-retention.md'
description: >-
  Learn how Workato data retention policies set the lifespan of job histories,
  trigger events, and reports, and how to customize them.
---

# Data retention policies

Workato retains specific recipe and usage data to power the [Dashboard](/en/features/admin-dashboard), display custom reports, repeat jobs, and troubleshoot errors. After the data retention period passes, this data is automatically and permanently deleted from the Workato platform.

> **SUMMARY**
> 
> - Workato's data retention policy determines the lifespan of data, such as job histories, trigger events, and custom reports. Workato deletes these data types after the specified time.
> - Default retention varies from 30 to 90 days from the job's completion date depending on your workspace type and platform plan. You can customize the retention time in certain cases.
> - You can set data retention at the workspace level or opt not to store data for specific recipes.
> - Store data beyond the default period by using audit log streaming to send data to supported applications.

The time data is retained is determined by a **data retention policy**. In this guide, we'll cover:

- [The basics of data retention policies in Workato](#basics)
- [The default retention periods in Workato](#workato-retention-policy)
- [What types of data are subject to the retention policy](#data-types)
- [How to customize your workspace's retention period](#configure-workspace-level)
- [How to selectively retain data at the recipe level](#configure-recipe-level)

* * *

## Basics

- [What is a data retention policy?](#what-is-it)
- [What is Workato's data retention policy?](#workato-retention-policy)
- [Can I customize the retention period for my workspace?](#customize-retention-period)
- [Can I customize retention at the recipe level?](#customize-recipe-level)
- [Can I store data for longer than the retention period?](#maximum-storage)
- [What types of data are subject to the data retention policy?](#data-types)
- [What happens if I change my data retention policy?](#policy-change)
- [Is job data retention retroactive?](#policy-retroactive)

### What is a data retention policy?

Workato's data retention policy specifies how long [specific types of data](#data-types) are stored for your account. The data retention period is 30 or 90 days from the job's completion date, depending on your workspace type and platform plan. Workato retains this data to support error recovery, duplicate detection, custom reports, and job re-runs.

Data subject to the retention policy is automatically and permanently deleted when the retention period passes. For example, if the retention period is 90 days, applicable data that is more than 90 days old is deleted.

### Retention policy duration

The retention period for a recipe job starts when the job ends.

For example, if your workspace's data retention policy is set to 30 days, the data from a recipe job is retained for 30 days starting from the job's completion date. This means that if a job begins on October 31st and completes on November 1st, the data associated with that job is retained until December 1st.

**Legacy plans**

For customers on legacy plans, the default data retention policy for your Workato account varies based on the type of workspace you use and any additional capabilities you select.

| Purchased? | Maximum retention | Customizable? |
| --- | --- | --- |
| None | 30 days | No |
| Enterprise Workspace | 90 days | Yes (1 hour minimum) |
| Data Monitoring capability | 90 days | Yes (1 hour minimum) |

**Usage-based pricing model**

For customers on our [usage-based pricing model](/en/pricing), the default data retention policy for your Workato account depends on your platform plan. Refer to your pricing plan and contract to learn more.

| Platform plan | Maximum retention | Customizable? |
| --- | --- | --- |
| Standard | 30 days | No |
| Business | 30 days | No |
| Enterprise | 90 days | Yes (1 hour minimum) |

  

> **MAXIMUM RETENTION AND CUSTOMIZATION OPTIONS**
> 
> The maximum retention period and the ability to customize it depends on your platform plan. Refer to your pricing plan and contract to learn more.

> **AGENT STUDIO GENIE CONVERSATION DATA**
> 
> These retention periods apply to job data. Agent Studio genie conversation data will soon follow a separate, fixed 90-day retention policy that isn't configurable. Refer to [Conversation data retention](/en/agentic/agent-studio/data#conversation-data-retention) for details.

### Can I customize the retention period for my workspace?

Yes, if you have an **Enterprise Workspace** or have the **Data Monitoring/Advanced Security & Compliance** capability.

Refer to the [Customization at the workspace level section](#configure-workspace-level) for more info.

### Can I customize retention at the recipe level?

Yes. The **Jobs data retention** recipe setting allows you to define whether Workato stores job data for the recipe:

![Recipe-level data retention policy](/assets/recipe-data-retention-policy.dsiUjwwn.png)_Recipe-level data retention policy_

See the [Defining data retention for recipes guide](/en/security/data-protection/data-retention/configure-retention-for-recipes) for more information.

### Can I store data for longer than the retention period?

To store data longer than the retention period, use [Audit log streaming](/en/features/activity-audit-log-streaming). Using this feature, you can send job and activity log data from Workato to your event management application of choice.

Workato supports the following applications:

- Amazon S3
- Data Dog
- Splunk
- Sumo Logic
- Any other application or service accessible over an HTTP endpoint

**Note**: Audit log streaming only includes data created **after** you configure the streaming. It does not apply to data created prior to the configuration.

### What types of data are subject to the data retention policy?

The following types of data are subject to your account's data retention policy:

- [Job history summaries](#job-history-summaries)
- [Job history details](#job-history-details)
- [Trigger events](#trigger-events)
- [Customized job reports](#customized-job-reports)

> **DATA TYPES EXEMPT FROM RETENTION POLICY**
> 
> The following types of data are not subject to your account's data retention policy:
> 
> - [Data tables](/en/data-tables) data, including data entered in [Workflow apps](/en/workflow-apps): Workato doesn't delete this data automatically. To delete this data, you must do so from the **Data tables** interface or programmatically.
> - [FileStorage](/en/features/workato-filestorage) data: Workato doesn't delete FileStorage data automatically. To delete this data, you must use the FileStorage delete action. Manually deleted data is purged from all backup drives within four days.
> - [SQL Transformations](/en/features/sql-transformations) data: Temporary contents received from different sources other than FileStorage, and the transformed output data are all automatically purged from primary and backup drives within 4 days.
> - [Agent Studio genie conversation data](/en/agentic/agent-studio/data#conversation-data-retention): Will soon follow a fixed 90-day retention policy instead of the job-based policy on this page, and won't be configurable.

### What happens if I change my data retention policy?

This varies, depending on whether you reduce or extend your data retention policy:

- **Reducing the data retention policy**: If you reduce the retention policy from 90 days to 60 days, the data for the reduced period (30 days) is not retroactive. For example, if the retention policy is changed on December 1, 2024, data from before October 2, 2024 is no longer retained by Workato.
- **Extending the data retention policy**: If you extend the retention policy from 30 days to 90 days, the additional data (30 days) is retroactive. For example, if the retention policy is changed on December 1, 2024, data from as far back as September 2, 2024, is retained.

### Is job data retention retroactive?

Retroactive job data retention varies depending on the job data type:

- **Job lines**: No, job lines are not retroactive.
- **Job history titles, errors, and custom columns**: Yes, these are retroactive and expire according to your current data retention settings.

#### Job history summary

Job history summary data provides job metadata on the **Job details** page. This includes information about the job such as:

- The job ID
- Status
- Description
- Starting time
- Duration

![Job history summary](/assets/job-summary-complete.CjRUrqxl.png)_Job history summary with successful job completion_

If the job resulted in an error, the summary would also contain details about the error:

![Job history summary](/assets/job-summary-error.Bo5bprY0.png)_Job history summary with error details_

#### Job history details

Job history detail data provides information about inputs and outputs for each action in the recipe:

![Action input and output](/assets/action-input-output.BEK8LjGI.gif)_Action input and output on the Job history details page_

After the data retention period has passed, only [job history summary](#job-history-summaries) data is retained. Action input and output data will be deleted.

#### Trigger events

Trigger event data is found on the **Job details** page in the **Output** tab of the trigger step:

![Trigger event data](/assets/trigger-event-data.5NX64ai8.png)_Trigger event data for a new issue in GitHub_

Trigger event data can be used to repeat a job without creating a new trigger event. After the retention period has passed and the trigger event data is deleted, this page's **Repeat this job** option is deactivated.

#### Customized job reports

Customized job reports are located in the [**Jobs** tab](/en/recipes/jobs) of the recipe. If a job report isn't customized, only the job's ID, status, and timestamp will display in the table.

A customized report is a quick, easy way to see data from a job without opening the **Job details** page. In the image below, for example, the job report has been customized to include the **GH issue**, **Team**, **Status**, **Priority**, and **Issue Type** columns:

![Custom job report](/assets/custom-report.Bu8QNnqT.png)_Custom job report showing data from the job execution_

After the retention period, only the job's **ID**, **status**, and **timestamp** will display in the job report. Data in customized columns will be deleted.

![Custom job report deleted](/assets/custom-report-deleted.ByqGGTds.png)_Custom job report after the retention period has passed_

* * *

## Customizing data retention

You can configure retention periods in the following ways:

- [At the workspace level](#configure-workspace-level)
- [At the recipe level](#configure-recipe-level)

> **FEATURE AVAILABILITY**
> 
> Configurable data retention is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.
> 
> Additionally, you must have the [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role, the legacy [Admin system role](/en/roles#system-roles), or be logged in as the [workspace owner](/en/roles#system-roles)/root login to make changes to your workspace's data retention policy.

> **DATA RETENTION POLICY CHANGES**
> 
> When you make changes to your workspace's data retention policy, Workato follows this logic:
> 
> If you reduce your workspace's data retention policy, the change is not retroactive. For example, if you change the retention policy from 90 days to 60 days on December 1, 2024, data from before October 2, 2024, is no longer retained by Workato. Conversely, if you extend the retention policy, the change is retroactive. For example, if you extend the retention policy from 30 days to 90 days on December 1, 2024, data from as far back as September 2, 2024, is retained.
> 
> For job data retention, job lines are not retroactive. However, job history titles, errors, and custom columns are retroactive and expire according to your current retention settings.

### Customization at the workspace level

1. Sign in to your Workato account and go to **Workspace admin > Settings > Data retention**.
   
2. Go to the **Data retention period unit** field and select `Hours` or `Days`.
   
3. Go to the **Data retention period** field and enter an integer to specify the duration of the retention period based on the selected **period unit**.
   
   For example, if the **period unit** is `Days` and you enter `45`, the retention period will be `45 days` from the job's completion date.
   
   ![Workspace-level data retention policy](/assets/account-data-retention-policy.CE3_LSRP.png)_Customized data retention policy of 45 days from the job's completion date_
   
   > **RETENTION PERIOD**
   > 
   > The retention period must be between **one (1) hour** and **90 days**. If set to a value outside this range, Workato will reset it to [the maximum for your workspace's plan type](#workato-retention-policy).
   
4. Click **Save**.
   

### Customization at the recipe level

Data retention can be configured on a recipe-by-recipe basis to use the [workspace retention policy](#configure-workspace-level) or to not store data at all.

Refer to the [Defining data retention for recipes](/en/security/data-protection/data-retention/configure-retention-for-recipes) guide for more info.

---

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

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/data-retention/data-retention-faqs.md
description: >-
  Answers to common questions about Workato data retention, including default
  periods, affected data types, and customizing retention.
---

# Data retention FAQs

Get answers to frequently asked questions (FAQs) about data retention.

## What is Workato's data retention policy?

View answer

Workato's [data retention policy](/en/security/data-protection/data-retention/) defines how long specific types of data are stored, such as job histories, trigger events, and custom reports. The default retention period is either 30 or 90 days from the job's completion date, depending on your workspace type and pricing plan. Refer to your pricing plan and contract to learn more.

## What types of data are subject to the data retention policy?

View answer

The following [data types](/en/security/data-protection/data-retention/) are subject to Workato's data retention policy:

- **Job history summaries**
- **Job history details**
- **Trigger events**
- **Customized job reports**

## Does the retention period start when a recipe job begins or when it ends?

View answer

The retention period for a recipe job starts when the job ends.

For example, if your workspace's data retention policy is set to 30 days, the data from a recipe job is retained for 30 days starting from the job's completion date. This means that if a job begins on October 31st and completes on November 1st, the data associated with that job is retained until December 1st.

## Can I customize the retention period for my workspace?

View answer

Yes. You can [customize data retention](/en/security/data-protection/data-retention/) in your workspace if you have an **Enterprise Workspace** or have the **Data Monitoring/Advanced Security & Compliance** capability. The retention period can range from 1 hour to 90 days from the job's completion date.

## Can I configure data retention to store no data at all for a recipe?

View answer

Yes. You can use the **[Zero retention](/en/features/activity-audit-log-streaming-retry#zero-retention-recipes)** option to store no data for a recipe. This setting ensures that Workato retains no input or output data for a job.

## What happens to data tables and FileStorage data under Workato's retention policy?

View answer

[Data tables](/en/data-tables#data-tables) and [FileStorage data](/en/features/workato-filestorage#usage-inspiration) are not automatically deleted. You must manually delete these records in the **Data tables** interface or by using the FileStorage delete action. Workato purges manually deleted data from backup drives within four days.

## What happens to job history summaries after the retention period ends?

View answer

After the retention period ends, [job history summaries](/en/security/data-protection/data-retention/) remain accessible, but **job history details**, including action inputs and outputs, are deleted. You can still access basic information, such as job status, job ID, and duration.

## Can I customize the retention period at the recipe level?

View answer

Yes. Workato allows you to [customize data retention at the recipe level](/en/security/data-protection/data-retention/) using the **Jobs data retention recipe setting**. You can choose whether to store job data for a specific recipe.

## What happens if I change my workspace's data retention policy?

View answer

This varies, depending on whether you reduce or extend your data retention policy:

- **Reducing the data retention policy**: If you reduce the retention policy from 90 days to 60 days, the data for the reduced period (30 days) is not retroactive. For example, if the retention policy is changed on December 1, 2024, data from before October 2, 2024 is no longer retained by Workato.
- **Extending the data retention policy**: If you extend the retention policy from 30 days to 90 days, the additional data (30 days) is retroactive. For example, if the retention policy is changed on December 1, 2024, data from as far back as September 2, 2024, is retained.

## Is job data retention retroactive?

View answer

This varies, depending on the job data type:

- **Job lines**: No, job lines are not retroactive.
- **Job history titles, errors, and custom columns**: Yes, these are retroactive and expire according to your current data retention settings.

---
