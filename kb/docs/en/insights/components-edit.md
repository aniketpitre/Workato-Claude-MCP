---
url: 'https://docs.workato.com/en/insights/components-edit.md'
description: >-
  Edit Insights components to analyze and present your data, including how to
  edit chart data, clone a component, and delete a component.
---

# Edit components

You can customize Insights components to better analyze and present your data. Insights supports the following operations:

- [Edit a chart](#edit)
- [Clone a component](#clone)
- [Delete a component](#delete)

Refer to the [Edit dashboards](/en/insights/dashboards-edit) guide to learn how to manipulate dashboards.

## Edit a chart

Edit chart data by selecting a data source, transforming datasets, and creating visualizations to match your reporting needs.

Complete the following steps to edit chart data:

1. Select a chart and click **Edit chart data**.
   
   ![Edit chart data](/assets/chart-edit.BOUBHF9c.png)_Edit chart data_
   
2. [Select your main data source](/en/insights/data-sources): Choose a **Source type** from the drop-down, such as Workflow apps, data tables, recipe job history, or workspace usage. Then, select the specific **Data source** you plan to use.
   
   ![Select a data source](/assets/data-source-setup.BVNhYhRh.png)_Select your data source_
   
3. [Transform your data](/en/insights/queries): Use the no-code query builder to filter, sort, summarize, join, and transform data from multiple sources.
   
   ![Perform queries](/assets/data-source-summarize.CKuu-3yG.png)_Perform queries on your data_
   
   For example, you can **Join** job history data to ROI data stored in a data table, and then **Summarize** the total hours per run and group the results by department.
   
   To add a transformation between queries, hover between them and click **Add query**.
   
   ![Add a query between existing queries](/assets/insights-add-query-between.Q3ohg-Oa.png)_Add a query between existing queries_
   
4. [Visualize your data](/en/insights/charts): Create interactive charts and organize them in dashboards with a WYSIWYG (what-you-see-is-what-you-get) editor.
   
   ![Visualize your data](/assets/visualize.DKvLdNvW.png)_Visualize your data_
   
5. Click **Save to page** to save your changes to the chart.
   
6. Click the **Preview** tab to preview your dashboard.
   
   ![Preview your dashboard](/assets/preview-dashboard.BiBszXej.png)_Preview your dashboard_
   
7. Click **Save** to save your dashboard, then click **Exit** when finished.
   

## Clone a component

Duplicating dashboard components allows you to reuse existing designs and experiment with different views and visualizations, while preserving the integrity of your original data.

You can clone components even if they’re in progress or contain errors. However, the dashboard can’t be saved until any errors in cloned components are resolved.

Insights supports cloning all components, including:

- Chart components
- Filter components
- Display components

Complete the following steps to clone a component:

1. Go to **Platform > Insights** and select a dashboard.
   
2. Click **Edit dashboard** to open the dashboard editor.
   
3. Select a component.
   
4. Click the **Clone** icon.
   
   ![Clone component](/assets/components-clone.BEpRGvB3.gif)_Clone component_
   
5. Customize the component as necessary.
   

## Delete a component

Complete the following steps to delete a component:

1. Go to **Platform > Insights** and select a dashboard.
   
2. Go to the **Dashboard canvas** and select a component.
   
3. Click the **Delete** icon.
   
   ![Delete component](/assets/components-delete.aSRrrWYZ.gif)_Delete component_

---
