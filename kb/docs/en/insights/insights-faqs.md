---
url: 'https://docs.workato.com/en/insights/insights-faqs.md'
description: >-
  Answers to common questions about Workato Insights, including what it does,
  where to access it, and the types of data analysis it supports.
---

# Insights FAQs

Get answers to frequently asked questions (FAQs) about Insights.

## What is Workato Insights, and what does it do?

View answer

Workato [Insights](/en/insights) is a data visualization and manipulation engine integrated into the Workato and Workflow apps' no-code environment. It allows users to connect, manipulate, and visualize data in real-time to make data-driven decisions.

Insights is designed for business users, IT professionals, and citizen developers to build custom dashboards that provide visibility into the value created by automation. It leverages real-time data to eliminate the need for costly ETL/ELT and business intelligence practices.

## Where can I access Workato Insights, and how do I navigate it?

View answer

You can access Workato Insights from the side navigation bar at **Platform > Insights** within Workato. The [Insights dashboard](/en/insights/dashboard-templates) allows you to create and manage custom reports, connect data sources, and visualize key metrics for automation and workflow performance.

## What types of data analysis can I perform with Insights?

View answer

You can perform the following types of data analysis with Workato Insights:

- **[Usage analytics](/en/insights#usage-analytics)**: Track workspace usage, including recipe success rates, job consumption, and error rates.
- **[Automation impact](/en/insights#automation-impact)**: Measure the business impact of automation, including ROI, time savings, and cost reductions.
- **[App analytics](/en/insights#app-analytics)**: Analyze user-centric processes such as task processing and approval times.
- **[Workflow performance](/en/insights#workflow-performance)**: Evaluate automated workflow performance, such as order processing times and regional order breakdowns.

## How can Workato Insights help measure automation impact?

View answer

Workato Insights provides [metrics](/en/insights#automation-impact) to quantify the impact of automation on your business processes. Metrics, such as time saved, money saved, and reduced manual errors help determine ROI. Specific metrics include the following:

- **Total amount saved ($)**
- **Hours saved in the last month by a specific process**
- **Savings by process or department**

## What metrics can I track using usage analytics in Insights?

View answer

You can use Workato Insights' **[usage analytics](/en/insights#usage-analytics)** to track the following metrics:

- The number of tasks consumed by a recipe or environment
- The number of active recipes in an environment
- Error rates
- Job execution times

You can also track the full job history of a workspace, including the total number of tasks and active recipes consumed.

## Can I customize the queries in Workato Insights to filter and transform data?

View answer

Yes. Workato Insights allows you to perform the following actions to customize [queries](/en/insights/queries#available-queries):

- Filter
- Summarize
- Sort
- Join rows
- Limit rows
- Calculated columns

This feature enables you to transform and prepare the data for analysis before displaying it on your dashboard.

## How do I manage access to Workato Insights?

View answer

Access to Workato Insights is managed through role-based access control (RBAC):

- In the [new permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2), collaborators with the **Environment admin** or **Environment manager** role have full access to Insights by default. You can configure the [Insights permission](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#insights) for environment roles by going to **Workspace admin > Access control > Environment roles**.
  
- In workspaces using the legacy permissions model, collaborators with the legacy **Admin** or **Analyst** system roles have full access by default.
  

Access to dashboards in Workflow apps depends on your subscription plan.

## How does Insights help with Workflow performance analysis?

View answer

Insights provides metrics to evaluate the performance of automated workflows. For example, you can track the total number of orders processed in an Order-to-Cash process, the average order processing time, and order breakdown by region. These metrics help identify performance bottlenecks and improve [workflow performance](/en/insights#workflow-performance).

## How does Insights work in Embedded workspaces?

View answer

Insights is available in Embedded workspaces with the following limitations:

- **Data Aggregation:** You can create Insights dashboards in either the Embedded Admin workspace or individual customer workspaces. However, you can't aggregate data from multiple customer workspaces into a single dashboard in the Embedded Admin workspace.
  
- **Dashboard Sharing:** You must create Insights dashboards separately in each workspace. You can't create a dashboard in one workspace and share it with another workspace.

---
