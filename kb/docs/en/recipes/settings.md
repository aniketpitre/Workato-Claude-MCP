---
url: 'https://docs.workato.com/en/recipes/settings.md'
description: >-
  Configure recipe settings in Workato, including concurrency, data retention,
  and sharing options from the Settings tab.
---

# Recipe settings

Recipe settings are available at the recipe level in the **Settings** tab.

![Recipe settings](/assets/recipe-settings.Dzir_PsB.png)_Recipe settings_

This page is divided into the following sections:

- [General](#general)
- [Data retention](#data-retention)
- [Sharing](#sharing)

* * *

## General

This section of the settings page enables you to determine recipe concurrency, keep track of recipes that monitor this particular recipe, and access resources to manage your recipes.

### Concurrency

The concurrency of a recipe determines the number of jobs that Workato can process simultaneously. Select a higher number for use cases that require high volume transactions.

The default recipe concurrency is 1 and the maximum depends on your contract and plan.

> **LONG ACTIONS AND CONCURRENCY**
> 
> When using [long actions](/en/recipes/long-actions#how-does-this-work) and setting the concurrency to `1`, note that these long actions unblock subsequent jobs, allowing them to start processing. This can result in unexpected behavior, with jobs starting before the previous one finishes, despite the concurrency setting of `1`.
> 
> To manage this, review the [list of long actions](/en/recipes/long-actions#list-of-long-actions) and understand their impact on job processing order. If you require strict sequential processing, minimize the use of long actions or explore alternative approaches. Regularly monitor your recipe's job processing to identify and adjust for any unexpected behavior.

### Resources

This tab provides links to information you can use to keep track of what's happening in your recipe.

- Usage metrics
  
- Track usage and operational metrics for this recipe. Workato provides a link to your workspace's [Dashboard](/en/features/admin-dashboard) with the relevant filters applied to allow you to view the metrics for this particular recipe.
  
- Dependencies
  
- See which assets are being used by this recipe. Workato provides a link to your workspace's [Dependency graph](/en/features/dependency-graph) with the relevant filters applied to allow you to view the assets dependent on this particular recipe.
  
- Activity audit
  
- Track activity related to this recipe's development. This section links to the [Activity audit log](/en/features/activity-audit-log) with the relevant filters applied to allow you to view the activity for this particular recipe.
  
- Copied from
  
- If this recipe was copied from another recipe, Workato provides a link to the parent recipe along with the date and time the recipe was copied.
  

### Recipe monitoring

If you are using other recipes to monitor particular events in this recipe, the names of the recipes appear here, along with links. If you are not monitoring this recipe with other recipes, this section of the settings page does not appear.

* * *

## Data retention

Determine whether Workato should store jobs data for this recipe. This setting has three options:

- Default retention policy
  
- Your workspace's [data retention policy](/en/security/data-protection/data-retention/#workato-retention-policy) applies when you select this option. For example, if the retention policy is **30 days**, the recipe's data will be retained for 30 days from the job's completion date.
  
- Do not store trigger event only
  
- Workato doesn't store trigger event data when you select this option. This improves recipe performance while keeping job step data for troubleshooting. You won't be able to rerun jobs.
  
- Do not store any data
  
- Workato doesn't store any recipe data when you select this option. You might select this option to:
  
  1. Manage risk associated with storing sensitive or personally-identifying data.
  2. Decrease the latency of an [API recipe](/en/api-mgmt/api-recipes/) by skipping log creation.
  
  **Before selecting this option**, make sure the recipe doesn't require job logs. Refer to our [data retention guide](/en/security/data-protection/data-retention/configure-retention-for-recipes#affected-data) for more information.
  

> **RETENTION PERIOD STARTS WHEN A JOB ENDS**
> 
> The retention period for a recipe job starts when the job ends.
> 
> For example, if your workspace's data retention policy is set to 30 days, the data from a recipe job is retained for 30 days starting from the job's completion date. This means that if a job begins on October 31st and completes on November 1st, the data associated with that job is retained until December 1st.

* * *

## Sharing

This interface allows you to share your recipes publicly in the community library or privately using a direct link.

> **RECIPE LIFECYCLE MANAGEMENT**
> 
> This interface allows you to share a single recipe, but does not facilitate sharing any of the recipe's assets or dependencies. For more robust recipe sharing capabilities, use the [Recipe lifecycle management](/en/recipe-development-lifecycle) feature to create manifest packages that include your recipe's connections, lookup tables, and more.

![recipe sharing](/assets/recipe-sharing.DwPTgWor.png)_Recipe sharing_

### Enable recipe sharing

Complete the following steps to enable recipe sharing in your workspace:

1. Go to **Workspace admin > General > Community profile**.
   
2. Click the **Allow recipes to be published on community** toggle.
   
   ![Allow recipes to be published on community](/assets/allow-recipe-publishing.CYwIwci3.png)_Click **Allow recipes to be published on community**_
   
3. Click **Save**.
   

### Share a recipe privately

Complete the following steps to share a recipe using a private link:

1. Go to the **Settings > Sharing** page of the recipe you plan to share.
   
2. Click **Generate link**. ![Click Generate link](/assets/recipe-share-link.B-Pt8pTq.png)_Click **Generate link**_
   
3. Click **Copy**. ![Click Copy](/assets/recipe-sharing-copy-link.BThwZdK0.png)_Click **Copy**_
   
4. Share the link.
   

You can revoke access to this recipe at any time by clicking **Revoke link**.

### Upload a recipe to the community library

Complete the following steps to upload a recipe to the community library:

1. Go to the **Settings > Sharing** page of the recipe you plan to upload.
   
2. Click **Publish recipe** to upload the recipe to the community library.
   
   ![Click Publish recipe](/assets/publish-recipe.DlSWKszO.png)_Click **Publish recipe**_
   
3. Monitor your recipe's status in the **Sharing with the Workato community** section.
   
   ![Monitor your recipe's status](/assets/monitor-recipe.C0eaps7k.png)_Monitor your recipe's status_
   

You can revoke access to this recipe at any time by clicking **Unpublish**.

> **ENABLE RECIPE SHARING**
> 
> Recipe sharing must be enabled in your workspace before you can upload a recipe to the community library. For more information, refer to [Enable recipe sharing](/en/community-library/upload-recipes#enable-recipe-sharing).

---
