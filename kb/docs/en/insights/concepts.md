---
url: 'https://docs.workato.com/en/insights/concepts.md'
description: >-
  Learn key concepts and understand how Insights can help you answer business
  questions.
---

# Concepts

This page covers the core concepts you need to build dashboards in Insights: dashboards, charts, metrics, and dimensions.

## Dashboard

A dashboard is a collection of charts that present your data visually. You can create multiple dashboards for different audiences or purposes.

Dashboards can also include [display components](/en/insights/dashboards-styling) such as containers, text blocks, and dividers to add structure and descriptive text.

You can also add [filter groups](/en/insights/filter-groups) to a dashboard or container to let users interactively filter data without editing individual charts.

![Example Insights dashboard](/assets/strategic-dashboard-1.Br9JCWh-.png)_An Insights dashboard combining KPI charts, a pie chart, a bar chart, and a table_

## Chart

A chart displays your data as a table, graph, or other visualization. You configure each chart in the [chart editor](/en/insights/navigate#chart-editor), where it queries a data source and displays the results as one of several [chart types](/en/insights/charts).

![Chart editor](/assets/chart-editor-query-builder.BxOSqqKW.png)_The chart editor_

The chart editor offers two ways to define what your chart displays:

- **Report builder** _(private beta)_: A simplified builder for most use cases. Choose what to measure and how to group your data to populate your chart.
- **Query builder**: A step-by-step builder for complex or advanced needs, using steps such as Filter, Summarize, and Sort. Use this when the report builder doesn't cover your use case. Refer to [Query components](/en/insights/queries) for a full list of available query steps.

## Metric and dimension

A metric is the value your chart measures, such as number of jobs or money saved. A dimension is the category your chart uses to group that data, such as environment or project.

Metrics and dimensions both come from a [data source](/en/insights/data-sources), which is the dataset your chart queries. You can apply [filters](/en/insights/filter-groups) to narrow the data your chart displays.

For example, you can measure the number of successful and failed jobs (metric) grouped by environment (dimension) to understand how integrations are performing across environments.

![Jobs by environment chart](/assets/jobs-by-environment.CTITXMj3.png)_A chart configured with job count (metric) broken down by success and grouped by environment (dimension)_

Refer to [Build your first dashboard](/en/insights/build-your-first-dashboard) to start building, or [Navigate Insights](/en/insights/navigate) for a full overview of the interface.

---
