---
url: 'https://docs.workato.com/en/insights/build-your-first-dashboard.md'
description: >-
  Create a simple dashboard showing active recipes in your workspace using
  either the report builder or query builder.
---

# Build your first dashboard

In this walkthrough, you'll build a workspace activity overview with three at-a-glance metrics and a breakdown of your most active projects.

![Example dashboard showing active recipes](/assets/first-dashboard-complete.Cv-h46rZ.png)_Example: Active recipes dashboard_

## Before you start

This walkthrough assumes your workspace has some recipes running. If you're new to Workato, [create your first recipe](/en/getting-started/build-first-recipe) first, then return here.

Follow the **Report builder** or **Query builder** tabs throughout. The query builder requires more manual configuration: you'll build filter conditions, summarize data, and sort results for each chart.

> **PRIVATE BETA**
> 
> The report builder is in private beta. Private beta features are available by invite only. Contact your Customer Success Manager to enable this feature.
> 
> Workato may update feature functionality or change availability without prior notice during the private beta.

## Create a new dashboard

Complete the following steps to create your dashboard:

1. Go to **Platform > Insights** and select **Create dashboard**.
   
   ![Create new dashboard](/assets/create-dashboard.CyVefYA4.png)_Create a new dashboard_
   
2. Name your dashboard `Workspace activity` and select the **Blank** template.
   
   ![Name and select template](/assets/name-dashboard.BkLtDtFz.png)_Name your dashboard_
   
   > **DASHBOARD TEMPLATES**
   > 
   > The **Blank** template lets you build a dashboard from scratch. [Dashboard templates](/en/insights/dashboard-templates) are also available for common workspace and project views.
   
3. Click **Create dashboard** to open the dashboard editor.
   

### About the dashboard editor

The dashboard editor has [four main areas](/en/insights/navigate#dashboard-editor):

- **Components panel**: contains the components you can add to your dashboard, including containers, text, dividers, and chart components.
- **Dashboard canvas**: the area your viewers see. Drag components here to build your layout.
- **Editor panel**: contains buttons to preview, save, and exit the dashboard.
- **Component properties panel**: appears when you select a component, letting you configure it.

Clicking **Edit** on a chart component opens the chart editor, where you set up the data query and choose how to display the results.

The components panel looks different depending on whether you have report builder access:

**Report builder**

![Dashboard editor with Report builder](/assets/dashboard-editor-v2.pKFt99_J.png)_Dashboard editor with Report builder: the components panel shows specific chart types (KPI, Table, Bar, and others) along with a Filter group option_

**Query builder**

![Dashboard editor with Query builder](/assets/dashboard-editor-v1.BqKTi-tp.png)_Dashboard editor with Query builder: the components panel shows a generic Chart component and a Filter group option_

## Set up your layout

Complete the following steps to set up your layout:

1. Clear the existing charts from the canvas by selecting each component and clicking **Delete**.
   
2. Drag chart components from the components panel onto the canvas:
   
   **Report builder**
   
   - 3 **KPI** chart components
   - 1 **Table** chart component
   
   **Query builder**
   
   - 4 **Chart** components
   
3. Drag chart edges and corners to resize and arrange the charts.
   
   **Report builder**
   
   ![Dashboard with three KPI chart components across the top row and one Table chart spanning the full width below](/assets/layout-setup-report-builder.DcTBjeYG.png)_Target layout: three KPI charts on the top row, table spanning full width below_
   
   **Query builder**
   
   ![Dashboard with three Chart components across the top row and one Chart spanning the full width below](/assets/layout-setup-query-builder.Cgcn3_ay.png)_Target layout: three charts on the top row, one chart spanning full width below_
   
     
   
   > **DISPLAY COMPONENTS**
   > 
   > Add **Container** and **Text block** components to provide context and help viewers understand what each chart represents. Use headings and descriptions to add background.
   

## Configure your charts

Select a chart on the canvas and click **Edit** to open the chart editor. The **Report builder** lets you pick a pre-built metric with minimal configuration. The **Query builder** requires you to build the query yourself step by step.

> **QUERY BUILDER PATTERN**
> 
> Each chart in the query builder follows the same pattern:
> 
> - Select a **data source**
> - Add **Filter** steps to narrow the data
> - Add a **Summarize** step to aggregate it into a metric
> - Configure **Chart settings** to choose how it's displayed
> 
> The results table updates after each step so you can see what your query returns.

### Chart 1: Active recipes

This KPI chart shows how many recipes are currently running in your workspace. Use this to verify that your automations are running as expected.

![Active recipes KPI chart on the dashboard](/assets/active-recipes-result.35E44hHj.png)_Active recipes KPI chart_

**Report builder**

1. Select the KPI chart component and click **Edit**.
   
2. Set **Metric** to **Active recipes**.
   
   ![EDIT CHART panel with Metric set to Active recipes and Type set to KPI](/assets/active-recipes-report-builder.Elv-MyIm.png)_Active recipes chart configured in the Report builder_
   
3. Click **Save to page** to add the chart to your canvas. This doesn't save the dashboard itself. You'll save the dashboard at the end.
   

**Query builder**

1. Select the Chart component and click **Edit**, then set:
   
   - **Source type**: Workspace data
   - **Data source**: Recipes
2. Click **+** and select **Filter**, then set:
   
   - **Data column**: Is active
   - **Condition**: Yes
3. Add a **Summarize** step:
   
   - **Metrics**: Count of rows
4. Configure **Chart settings**:
   
   - **Type**: KPI
   - **Data column**: Count of rows
   - **Label**: Active recipes
   
   ![Active recipes chart configured in the query builder](/assets/active-recipes-query-builder.hRt5etzI.png)_Active recipes chart configured in the query builder_
   
5. Click **Save to page** to add the chart to your canvas. This doesn't save the dashboard itself. You'll save the dashboard at the end.
   

### Chart 2: Total jobs (last 30 days)

This KPI chart shows how many jobs ran in your workspace over the past 30 days. Use this to measure how actively your automations are being used.

![Total jobs KPI chart on the dashboard](/assets/total-jobs-result.Ce4-kT7j.png)_Total jobs chart_

**Report builder**

1. Select the KPI chart component and click **Edit**.
   
2. Set **Metric** to **Started jobs**.
   
3. Click **\+ Add filter** and set:
   
   - **Data**: **Event time**
   - **Condition**: **within**
   - **Value**: **Last 30 days**
4. Set **Label** to `Total jobs (last 30 days)`.
   
   ![EDIT CHART panel showing Metric set to Started jobs with an Event time filter for the last 30 days and Label set to Total jobs (last 30 days)](/assets/total-jobs-last-30-days-report-builder.XLdRQpMw.png)_Total jobs chart with date filter and custom label_
   
5. Click **Save to page**.
   

**Query builder**

1. Select the Chart component and click **Edit**, then set:
   
   - **Source type**: Workspace data
   - **Data source**: Job history
2. Add a **Filter**:
   
   - **Data column**: Started at
   - **Condition**: within
   - **Value**: Last 30 days
3. Add a **Summarize** step:
   
   - **Metrics**: Count of rows
4. Configure **Chart settings**:
   
   - **Type**: KPI
   - **Data column**: Count of rows
   - **Label**: Total jobs (last 30 days)
   
   ![Total jobs chart with date filter and custom label](/assets/total-jobs-last-30-days-query-builder.q0Aeic81.png)_Total jobs chart with date filter and custom label_
   
5. Click **Save to page**.
   

### Chart 3: Successful jobs (last 30 days)

This KPI chart shows how many jobs completed without errors in the past 30 days. Use this alongside total jobs to see how reliably your automations are running.

![Successful jobs KPI chart on the dashboard](/assets/successful-jobs-result.C7I8UYx_.png)_Successful jobs chart_

**Report builder**

1. Select the KPI chart component and click **Edit**.
   
2. Set **Metric** to **Successful jobs**.
   
3. Click **\+ Add filter** and set:
   
   - **Data**: **Event time**
   - **Condition**: **within**
   - **Value**: **Last 30 days**
4. Set **Label** to `Successful jobs (last 30 days)`.
   
   ![EDIT CHART panel showing Metric set to Successful jobs with an Event time filter for the last 30 days and Label set to Successful jobs (last 30 days)](/assets/successful-jobs-last-30-days-report-builder.BeqT6ZUt.png)_Successful jobs chart with date filter and custom label_
   
5. Click **Save to page**.
   

**Query builder**

1. Select the Chart component and click **Edit**, then set:
   
   - **Source type**: Workspace data
   - **Data source**: Job history
2. Add a **Filter**:
   
   - **Data column**: Is successful
   - **Condition**: Yes
3. Add a second **Filter**:
   
   - **Data column**: Started at
   - **Condition**: within
   - **Value**: Last 30 days
4. Add a **Summarize** step:
   
   - **Metrics**: Count of rows
5. Configure **Chart settings**:
   
   - **Type**: KPI
   - **Data column**: Count of rows
   - **Label**: Successful jobs (last 30 days)
   
   ![Successful jobs chart with date filter and custom label](/assets/successful-jobs-last-30-days-query-builder.BPM1xl-e.png)_Successful jobs chart with date filter and custom label_
   
6. Click **Save to page**.
   

### Chart 4: Top active projects

This table ranks your projects by the number of active recipes. Use this to see which projects have the most automations running and understand automation adoption across teams or departments.

![Top active projects table on the dashboard](/assets/top-active-projects-result.BnNTjCX1.png)_Top active projects chart_

**Report builder**

1. Select the Table chart component and click **Edit**.
   
2. Set **Dimensions** to **Project name**.
   
3. Set **Metrics** to **Active recipes**.
   
4. Click **\+ Add sort** and set:
   
   - **Data**: **Active recipes**
   - **Order**: **Descending**
5. Set **Title** to `Top active projects`.
   
   ![EDIT CHART panel showing Dimensions set to Project name, Metrics set to Active recipes, and Sort set to Active recipes in descending order](/assets/top-active-projects-report-builder.CobnTQk7.png)_Top active projects table configured with dimensions, metrics, and sort order_
   
6. Click **Save to page**.
   

**Query builder**

1. Select the Chart component and click **Edit**, then set:
   
   - **Source type**: Workspace data
   - **Data source**: Recipes
2. Add a **Filter**:
   
   - **Data column**: Is active
   - **Condition**: Yes
3. Add a **Summarize** step:
   
   - **Metrics**: Count of rows
   - **By data column**: Project name
4. Add a **Calculated column** step to rename the column. The Summarize step labels this column `Count of rows`. Rename it here so it appears with a user-friendly name in the table:
   
   - **Column name**: `Active recipes`
   - **Column expression**: `Count of rows`
5. Add a **Sort** step:
   
   - **Data column**: Active recipes
   - **Order**: Descending
6. Configure **Chart settings**:
   
   - **Type**: Table
   - **Title**: Top active projects
   - **Displayed columns**: Select Project name and Active recipes
   
   ![Top active projects table configured with dimensions, metrics, and sort order](/assets/top-active-projects-query-builder.D7kypUaK.png)_Top active projects table configured with dimensions, metrics, and sort order_
   
7. Click **Save to page**.
   

## Save your dashboard

Complete the following steps to save and view your dashboard:

1. Click **Save** in the dashboard editor.
   
2. Click **Preview** to see how your dashboard looks to viewers.
   
   ![Example dashboard showing active recipes](/assets/first-dashboard-complete.Cv-h46rZ.png)_Example: Active recipes dashboard_
   
   Your dashboard shows:
   
   - Three key metrics about workspace activity
   - A table of your most active projects
3. Click **Exit** to return to the Insights homepage.
   

Your dashboard updates automatically as new jobs run in your workspace.

---
