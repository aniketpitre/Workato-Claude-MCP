---
url: >-
  https://docs.workato.com/en/security/data-protection/data-retention/data-retention-faqs.md
description: >-
  Answers to common questions about Workato data retention, including default
  periods, affected data types, and customizing retention.
---

# Data retention FAQs

Get answers to frequently asked questions (FAQs) about data retention.

What is Workato's data retention policy?

Workato's [data retention policy](/en/security/data-protection/data-retention/) defines how long specific types of data are stored, such as job histories, trigger events, and custom reports. The default retention period is either 30 or 90 days from the job's completion date, depending on your workspace type and pricing plan. Refer to your pricing plan and contract to learn more.

What types of data are subject to the data retention policy?

The following [data types](/en/security/data-protection/data-retention/) are subject to Workato's data retention policy:

- **Job history summaries**
- **Job history details**
- **Trigger events**
- **Customized job reports**

Does the retention period start when a recipe job begins or when it ends?

The retention period for a recipe job starts when the job ends.

For example, if your workspace's data retention policy is set to 30 days, the data from a recipe job is retained for 30 days starting from the job's completion date. This means that if a job begins on October 31st and completes on November 1st, the data associated with that job is retained until December 1st.

Can I customize the retention period for my workspace?

Yes. You can [customize data retention](/en/security/data-protection/data-retention/) in your workspace if you have an **Enterprise Workspace** or have the **Data Monitoring/Advanced Security & Compliance** capability. The retention period can range from 1 hour to 90 days from the job's completion date.

Can I configure data retention to store no data at all for a recipe?

Yes. You can use the **[Zero retention](/en/features/activity-audit-log-streaming-retry#zero-retention-recipes)** option to store no data for a recipe. This setting ensures that Workato retains no input or output data for a job.

What happens to data tables and FileStorage data under Workato's retention policy?

[Data tables](/en/data-tables#data-tables) and [FileStorage data](/en/features/workato-filestorage#usage-inspiration) are not automatically deleted. You must manually delete these records in the **Data tables** interface or by using the FileStorage delete action. Workato purges manually deleted data from backup drives within four days.

What happens to job history summaries after the retention period ends?

After the retention period ends, [job history summaries](/en/security/data-protection/data-retention/) remain accessible, but **job history details**, including action inputs and outputs, are deleted. You can still access basic information, such as job status, job ID, and duration.

Can I customize the retention period at the recipe level?

Yes. Workato allows you to [customize data retention at the recipe level](/en/security/data-protection/data-retention/) using the **Jobs data retention recipe setting**. You can choose whether to store job data for a specific recipe.

What happens if I change my workspace's data retention policy?

This varies, depending on whether you reduce or extend your data retention policy:

- **Reducing the data retention policy**: If you reduce the retention policy from 90 days to 60 days, the data for the reduced period (30 days) is not retroactive. For example, if the retention policy is changed on December 1, 2024, data from before October 2, 2024 is no longer retained by Workato.
- **Extending the data retention policy**: If you extend the retention policy from 30 days to 90 days, the additional data (30 days) is retroactive. For example, if the retention policy is changed on December 1, 2024, data from as far back as September 2, 2024, is retained.

Is job data retention retroactive?

This varies, depending on the job data type:

- **Job lines**: No, job lines are not retroactive.
- **Job history titles, errors, and custom columns**: Yes, these are retroactive and expire according to your current data retention settings.
