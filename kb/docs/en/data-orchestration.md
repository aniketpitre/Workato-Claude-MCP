---
url: 'https://docs.workato.com/en/data-orchestration.md'
description: >-
  Workato data orchestration lets you build data pipelines to combine,
  transform, and load data into databases and warehouses, then monitor runs.
---

# Data orchestration

Workato offers a powerful and flexible platform for [data orchestration](https://www.workato.com/platform/data-orchestration?utm_source=docs&utm_medium=referral&utm_campaign=data-orchestration), designed to streamline your data orchestration processes while maintaining simplicity. As a platform that supports hyper-automation, Workato enables users to accomplish a wide range of tasks while offering a seamless building experience and user interface (UI). This empowers citizen builders to build data orchestrations, without sacrificing on robust data orchestration capabilities.

Workato enables you to build effective data pipelines that can combine and harmonize data from different sources, applications, and systems within your organization, transform the data, and load it to databases or data warehouses to gather insights that can help to better understand your business and customers.

> **FEATURE AVAILABILITY**
> 
> Data orchestration is available on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Monitor orchestration activity

Go to **Platform > Data Orchestration** to open the data orchestration dashboard. You can use this dashboard to monitor pipeline run status and duration, and troubleshoot data ingestion pipelines. It displays historical activity, run outcomes, and data volume metrics across orchestration workflows in your workspace.

> **DASHBOARD SCOPE**
> 
> The dashboard currently supports data ingestion pipelines and selected connectors in recipes. It doesn't currently display activity from other pipeline types.

![Data orchestration dashboard](/assets/orchestration-dashboard.CXjpYmea.gif)_Data orchestration dashboard_

The dashboard provides a 30-day summary of pipeline activity, including counts of successful, failed, and stopped runs. It also tracks daily row volumes and average run durations over time. You can use these metrics to locate unusual patterns and determine whether pipelines run consistently, fail frequently, or stop unexpectedly.

## Run activity

The **Run activity** timeline allows you to explore pipeline behavior over the past 30 days. The chart shows the total runs per day, grouped by status. It also displays the average run duration and highlights changes in the volume of data processed.

![Data orchestration run activity](/assets/run-activity.DngWk6L_.gif)_Data orchestration run activity_

### Pipeline activity timeline

Select a day on the **Run activity** timeline to open the pipeline activity timeline for that date. You can use this view to compare runs across pipelines. The view spans 24 hours and includes a row for each pipeline.

Each bar represents a sync activity that includes one or more runs. The bar's width reflects the total duration of the sync, and its color indicates the outcome. You can hover over a bar to view run details such as timing, outcome distribution, total number of runs, and number of rows extracted and loaded.

![View run activity for a specific date](/assets/orchestration-day-activity.D2yiLjes.gif)_View run activity for a specific date_

## Filter dashboard data

You can use filters to refine the dashboard view by time period or pipeline status, such as **Active**, **Inactive**, or **Only failed runs**.

![Data orchestration run activity](/assets/filter-data-dashboard.Cu8DN4pk.gif)_Filter data orchestration dashboard_

By default, the dashboard displays all pipelines and statuses from the past 30 days.

## Troubleshoot pipelines

Click any sync activity in the pipeline activity timeline to open the [Object runs tab](/en/data-orchestration/data-pipeline-recipe/monitor#object-runs) for that pipeline. This view lists all object-level runs for the selected period.

![View object runs](/assets/view-object-runs.mPQThe8r.gif)_View object runs_

You can use this tab to track object run status, review the execution history, analyze pipeline activity, and troubleshoot failures.

Refer to the [Troubleshoot your data pipeline](/en/data-orchestration/data-pipeline-recipe/troubleshoot#identify-a-data-pipeline-issue) section to learn how to locate and resolve failed runs.

## Workato Data orchestration strengths

As a data orchestration platform, Workato has the following strengths.

- LCNC (Low-Code/No-Code)
  
- Workato is built on a low-code/no-code foundation, enabling users to create powerful data orchestration workflows with minimal coding. This approach provides flexibility without sacrificing simplicity, making it a versatile platform for users with varying technical backgrounds.
  
- Flexible
  
- The flexibility of Workato's recipe-based structure allows you to design and execute data orchestration processes tailored to your specific needs. You can customize your workflows and connect with any system, automate complex workflows, or orchestrate data transformations, Workato's flexibility ensures a customizable solution.
  
- Scalable
  
- Workato offers bulk actions and triggers that give you the ability to scale and handle large volume data in data orchestration Workflows.
  
- Reusable components
  
- Using reusable components such as [Recipe functions](/en/connectors/recipe-functions) in your data orchestration pipelines, enables you to build efficient and maintainable data orchestration workflows. This approach reduces the overhead of managing numerous recipes and promotes a more streamlined and organized data orchestration process.
  
- Observability
  
- Observability is a key aspect of Workato's data orchestration solution. Leveraging our [logging service](/en/features/logging-service) and [job report](/en/recipes/jobs), users can gain insights into the performance and status data orchestration pipelines. This ensures transparency and facilitates proactive monitoring and issue resolution.
  
- Performance
  
- Workato offers high performance through bulk operations and [file storage](/en/features/workato-filestorage) capabilities. These features contribute to the efficient execution of data orchestration tasks, ensuring optimal performance even with large datasets.
  

## ETL/ELT

Extract, Transform, and Load (ETL) and Extract, Load, and Transform (ELT) are processes used in data orchestration and data warehousing to extract, transform, and load data from various sources into a target destination, such as a data warehouse or a data lake.

### Bulk vs Batch

Bulk/Batch actions/triggers are available throughout Workato. Bulk processing gives you the ability to process large amounts of data in a single job, especially suited for ETL/ELT. Batch processing is restricted by batch sizes and memory constraints, and are generally less suitable in the context of ETL/ELT.

### Extract, Transform, and Load (ETL)

ETL begins with the extraction phase, where data is sourced from multiple heterogeneous sources, including databases, files, APIs, and web services. This raw data is then subjected to a transformation phase, such as cleaning or filtering before it is loaded into a target system, typically a data warehouse.

### Extract, Load, and Transform (ELT)

Similar to ETL, ELT starts with the extraction phase, where data is extracted from various sources. ELT focuses on loading the extracted data into a target system such as a data lake or distributed storage. Once the data is loaded, transformations occur within the target system.

---
