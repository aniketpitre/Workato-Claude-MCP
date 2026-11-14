---
url: 'https://docs.workato.com/en/insights/multiple-workspaces.md'
description: >-
  Learn which Insights data aggregates across parent and child workspaces, and
  which is scoped to the current workspace.
---

# Insights in Automation HQ and Embedded

Workspaces in [Embedded](/en/oem) and [Automation HQ](/en/automation-hq) are organized into a hierarchy: a **parent workspace** provides centralized administrative oversight for a group of **child workspaces**. Insights dashboards created in a parent workspace automatically combine [usage](/en/insights/data-sources#usage) data from the parent workspace and all of its child workspaces. This page explains which metrics roll up, how to filter usage data by workspace, and the current limitations.

This documentation uses **parent workspace** and **child workspace**. The equivalent names are:

|  | Embedded | Automation HQ |
| --- | --- | --- |
| **Parent workspace** | [Admin workspace](/en/oem/workspace-structure) | [HQ workspace](/en/ahq-hq-workspace) |
| **Child workspaces** | [Customer workspaces](/en/oem/workspace-structure) | [Managed workspaces](/en/ahq-managed-workspace) |

> **FEATURE AVAILABILITY**
> 
> Insights is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.
> 
> Usage data aggregation requires an eligible credit-based plan, and the report builder it depends on is in private beta. Contact your Customer Success Manager to enable it.

## What data is aggregated

Only [usage](/en/insights/data-sources#usage) metrics aggregate across a parent workspace and its child workspaces. They include the following:

- Credits
- Tasks
- API calls
- API proxy calls
- Events processed
- Genie actions
- IDP pages processed
- MCP tool calls
- Rows consumed

Refer to [Usage metrics](/en/pricing/usage-metrics#metrics) to learn how Workato measures each metric.

## Default behavior

Dashboards you build in the **parent workspace** combine usage data automatically. You can [apply a filter](#filter-by-workspace) to display data for specific workspaces.

Child workspaces maintain strict boundary isolation and can only view their own workspace data.

## Filter usage data by workspace

Complete the following steps to display usage data for individual workspaces:

1. Add a **Filter group** to the dashboard.
   
2. Click **\+ Add filter**.
   
3. Keep **Filter custom query chart?** set to **No**.
   
4. Search for **Workspace name** in the **Metric or dimension** list.
   
   ![Workspace name in the Metric or dimension search results](/assets/filter-workspace-name.Difjkrns.png)_Search for the **Workspace name** dimension_
   
5. Set a **Default value** with the workspace or workspaces to show, and add a **Label**.
   
6. Click **Done**, then **Save**.
   

Clear the filter to show combined data for all workspaces again.

You can also group a chart by the **Workspace name** dimension, for example credits by month for each workspace.

The same filter works with other [usage dimensions](/en/insights/data-sources#usage-dimensions), such as **Environment name**, **Project name**, and **Recipe name**. Filters match exact values.

## What data isn't aggregated

No other metrics, dimensions, or data sources aggregate. The following show data for the current workspace only:

- [Integrations](/en/insights/data-sources#integrations) metrics and dimensions, including job success rates, error rates, and job execution time
- [APIs](/en/insights/data-sources#apis) and [Audit and governance](/en/insights/data-sources#audit-governance) metrics and dimensions
- Every [query builder](/en/insights/data-sources#query-builder) data source, including the **Chart (Custom Query)** component

## Limitations

- Aggregation works only when you build charts in the [report builder](/en/insights/navigate#report-builder), not the query builder.
- The report builder's metric selector doesn't group metrics by category, so usage metrics can be hard to tell apart from others. Check that **Workspace name** is available as a dimension when you choose a metric.
- You must create dashboards separately in each workspace. You can't share a dashboard from the parent workspace with its child workspaces.

## FAQs

Get answers to frequently asked questions (FAQs) about Insights dashboards in Automation HQ and Embedded workspaces.

### Does my dashboard show only data from my current workspace by default?

View answer

- **Parent workspaces**: Dashboards built in the parent workspace automatically aggregate usage data from the parent and all connected child workspaces. You can [apply a filter](#filter-by-workspace) to isolate data for specific workspaces.
- **Child workspaces**: Child workspaces maintain strict boundary isolation and can only view their own workspace data.

### Can child workspaces see data from other workspaces?

View answer

No. Each child workspace can only view its own data.

### Do error rates and job history roll up to the parent workspace?

View answer

No. Only usage metrics aggregate.

> **FURTHER READING**
> 
> - [Data sources](/en/insights/data-sources)
> - [Filter groups](/en/insights/filter-groups)
> - [Navigate Insights](/en/insights/navigate)
> - [Manage roles and privileges](/en/insights/permissions)

---
