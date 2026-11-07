---
url: 'https://docs.workato.com/en/insights/roi-dashboard.md'
description: Learn how to build an ROI dashboard in Insights using an example scenario.
---

# Build an ROI dashboard

This guide demonstrates how to create a dashboard from start to finish, using an example scenario. The scenario follows an Integration Lead tasked with creating a strategic ROI dashboard to help senior leadership understand the impact of automation adoption at their company.

> **NEW TO INSIGHTS?**
> 
> Start with [Build your first dashboard](/en/insights/build-your-first-dashboard) to learn the basics before following this guide.

![Completed ROI dashboard](/assets/roi-automation-impact.B50qCe6R.png)_Completed ROI dashboard_

## Plan your dashboard

You must define your audience, audience needs, and determine the high-level purpose of your dashboard. You can also define the key business questions your dashboard must answer.

In our example scenario, the Integration Lead has identified the following audience and business questions.

**Audience, needs, and dashboard purpose**

- The primary audience of this dashboard is senior leadership (business users).
- They need to understand how automation contributes to cost-savings and apply these insights to guide the direction of the company.
- The dashboard's main purpose is to provide an overview of how well automation is adopted, the value it delivers, and which teams are using it the most.
- It requires reporting on high-level KPIs (key performance indicators).

**Business questions**

- How many integrations have been built company-wide?
- How many are actually being used?
- How much time and money has the company saved?
- Which projects save the most money?
- Which departments are using Workato the most?
- How has automation contributed to efficiency gains?

The next steps are to identify the metrics and dimensions required to answer your questions and ensure you're prepared to capture these values effectively.

### Identify your metrics and dimensions

The following table demonstrates how you can analyze your business questions to identify your metrics and dimensions.

| Question | Metric | Dimension |
| --- | --- | --- |
| How many integrations have been built company-wide? | Count of recipes | Time (week, month, or year) |
| How many are actually being used? | Count of active recipes | Time (week, month, or year) |
| How much money has the company saved? | Sum of money saved | Time (week, month, or year) |
| Which use cases are saving the most money? | Sum of money saved | Use cases |
| Which departments are using Workato the most? | Count of active recipes | Departments |
| How has automation contributed to efficiency gains? | Sum of processed orders count, Sum of processed invoices count, Sum of employees hired count, Sum of marketing campaigns count | Time (week, month, or year) |

This analysis enables you to conceptualize the sections to include in your dashboard. In our example, we also plan to include filter groups to allow our dashboard viewers to drill-down into specific subsets of our reports so that they can segment the data as required.

### Set up data sources

Now that you've identified the key metrics and dimensions you plan to analyze, ensure you're set up to capture the necessary data. This can involve entering records in data tables, customizing job reports, and more.

#### Add records to data tables

Use the [Data table connector](/en/data-tables/data-table-connector) in your recipes to create, update, or upsert records in a data table. This enables you to log meaningful workflow events which you can use in your data analysis.

In this example, the Integration Lead is assessing the effectiveness of an automated resume screening workflow to evaluate efficiency gains driven by automation. They must log information obtained from a job application, such as the application ID, candidate ID, and job ID, during key stages of the process, such as when a new application is submitted. They must create a data table to store business events and add a step to their recipe to log events from Greenhouse in the table.

Set up your data table

You must create a dedicated data table with the necessary columns before adding records to data tables in your recipe.

Complete the following steps to create a data table:

1. Go to the project that contains the recipe you plan to capture details from.
   
2. Click **Create > Data table** or press C+T.
   
3. Provide a unique name for your data table, such as `Resume screening`.
   
4. Click **Start building**.
   
5. Click **+** to create a new column.
   
6. Go to the **Column name** field and supply a unique name, such as `application_id`.
   
7. Use the **Column type** menu to select `Short text`.
   
8. Go to the hint field and enter `Greenhouse application ID`.
   
9. Click **Add column**.
   
   ![Add a data column](/assets/column-add.CJdt1UDw.png)_Add a data column_
   
10. Repeat this process to create the following additional columns:
    
    | Column name | Data type | Hint text |
    | --- | --- | --- |
    | candidate\_id | Short text | Greenhouse candidate ID |
    | job\_id | Short text | Greenhouse job ID |
    | department | Short text | Hiring department |
    | recruiter | Short text | Recruiter name |
    | task\_name | Short text | Workflow stage |
    

Add a Create record in a data table step to your recipe

This example recipe automates the process of evaluating job applications submitted in Greenhouse, generates scorecards using OpenAI, and logs the results in a data table for further review. This example captures details after a new application is submitted in Greenhouse.

Complete the following steps to log business events in a data table:

1. Click **\+ Add step** and select **Action in app** after the business event you plan to log. In this example, we add it to **Step 4**.
   
   ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
   
2. Search for `Data tables` and select it as your app.
   
3. Select the **Create record** action.
   
4. Use the **Data table** menu to select `Resume screening`.
   
5. Complete the following actions in the **New record fields** section:
   
   1. Map the Application ID (Step 1) datapill to the **application\_id** field.
      
   2. Map the Candidate ID (Step 1) datapill to the **candidate\_id** field.
      
   3. Map the Job ID (Step 1) datapill to the **job\_id** field.
      
   4. Map the Candidate ID (Step 1) datapill to the **candidate\_id** field.
      
   5. Map the Department (Step 2) datapill to the **department** field.
      
   6. Map the First name (Step 1) and Last name (Step 1) datapills to the **recruiter** field.
      
   7. Enter `Application submitted` in the **task\_name** field.
      
   
   Your configuration should look as follows:
   
   ![Map datapills](/assets/datapill-map.CLViVyQa.png)_Map datapills from meaningful business events in other applications to create a record in a data table_
   
6. Click **Save**.
   

You can also create and update records manually using the [Data tables interface](/en/data-tables).

#### Customize job reports

[Customize your job reports](/en/recipes/jobs#customizing-job-reports) to surface meaningful information from your recipes. You can add up to 10 additional columns and custom job report columns support datapill input. Job reports are subject to your workspace's [data retention policy](/en/security/data-protection/data-retention/).

In this example, the Integration Lead is assessing the effectiveness of an automated order processing workflow to evaluate efficiency gains driven by automation. They plan to surface data from the order, such as the order ID, fulfillment status, name, item quantity, and price in their job reports.

Customize your job report

1. Select a recipe job report to customize. Your recipe must be inactive to customize its job report.
   
2. Go to the **Jobs** tab.
   
3. Click the **...** (ellipsis) and select **Customize job report**.
   
4. Click **\+ Add a new column**.
   
5. Create the following custom columns:
   
   1. Go to the **Column name** field, type `Item name`, and map the Name (Step 2) datapill to the **Column value** field.
      
   2. Go to the **Column name** field, type `Quantity`, and map the Quantity (Step 2) datapill to the **Column value** field.
      
   3. Go to the **Column name** field, type `Price`, and map the Price (Step 2) datapill to the **Column value** field.
      
   4. Go to the **Column name** field, type `Order ID`, and map the Order ID (Step 1) datapill to the **Column value** field.
      
   5. Go to the **Column name** field, type `Fulfillment status`, and map the Name (Step 1) datapill to the **Column value** field.
      
   
   Your configuration should look as follows:
   
   ![Customize job report](/assets/automation-impact-job-report-customize.Br4ciejX.png)_Map datapills to custom columns in your job reports_
   
6. Click **Apply changes**.
   

## Build your dashboard

Building a dashboard involves designing the dashboard layout and creating custom reports and visualizations with your data.

### Design your dashboard

Before you begin manipulating, querying, transforming, and visualizing your data, it's worth spending some time to ensure that your visual layout represents your data well. You can start with one of our [dashboard templates](/en/insights/dashboard-templates) or create a dashboard from scratch.

Design your dashboard layout

Complete the following steps to design your dashboard layout. This example uses a blank template.

1. Determine the width of your dashboard. Insights supports **Full** and **Fixed** width options.
   
   ![Determine the width](/assets/dashboard-width.CF5GZVBk.png)_Determine the width of your dashboard_
   
2. Add containers to define your layout. You can click and drag the edge of the container to resize it.
   
   ![Customize containers](/assets/container-customize.BIkvy_W8.gif)_Customize containers_
   
3. Add a title and additional text components to your dashboard as necessary. We recommend applying headings to containers in your dashboard to help categorize your visualizations.
   
   ![Add a text component](/assets/text-customize.BZ4Bv0zr.gif)_Add and customize text_
   
4. Customize container colors on your dashboard as necessary. We recommend [using color strategically](/en/insights/dashboards-styling#design-best-practice) throughout your dashboard to convey meaning. For example, choose white or a neutral color to maximize contrast between the background and your charts. Alternatively, choose a color to sync with your brand.
   
   ![Customize container colors](/assets/color-customize-2.DSbgbG6L.gif)_Customize container colors_
   
5. Add a divider. You can place dividers in between containers to create a visual separation between different groups of charts.
   
   ![Add a divider](/assets/divider-customize.Cn0HfgSh.gif)_Add and customize dividers_
   
6. Add chart components to your dashboard.
   
   ![Add chart](/assets/chart-add.DAORAw3-.gif)_Add charts to your dashboard_
   

### Create custom reports and visualizations

The next step in the dashboard building process is to build your charts. During the querying and chart building process a table displays by default.

Complete the following steps to build charts in your dashboard. This example demonstrates how to create a chart that displays the top money saving use cases. Refer to the [Metrics for additional charts](#metrics) section for guidance on completing additional charts.

1. Go to the dashboard editor, select a chart component, and click **Edit**.
   
2. Select a data source
   
   1. Go to the **Use data from** field and select `Workspace data` as the **Source type**, and `Job history` as the **Data source**.
      
      ![View the results table](/assets/automation-impact-data-source.DMKTsR_U.png)_Select a data source_
      
   
3. Click **+** (plus) and select **Join** from the query builder.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Join**_
   
4. Configure the join step
   
   This step joins job history data to data in a lookup table, `ROI lookup`. The `ROI lookup` table maps each recipe to its automated use case and associated cost savings.
   
   1. Use the **Join type** menu to select `Inner join`, use the **Source type** menu to select `Data tables`, and set the data source to `ROI lookup`.
      
   2. Use the **Current result** drop-down menu to select `Recipe ID` and use the **ROI Lookup** drop-down menu to select `Recipe ID`.
      
   3. Preview your data in the **Results** table. This table displays job history data joined to data in `ROI lookup`.
      
      ![View the results table](/assets/automation-impact-join-results.BW3BL5py.png)_Preview your data in the **Results table**_
      
   
5. Click **+** and select **Summarize** from the query builder.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Summarize**_
   
6. Configure the summarize step
   
   1. Use the **Metrics** drop-down menu to select `Sum of` and use the **Data column** drop-down menu to select `Money saved`.
      
   2. Use the **Data column** drop-down menu to select `Use case`.
      
   3. Preview your data in the **Results** table. This table displays use cases and the amount of money saved by each.
      
      ![View the results table](/assets/automation-impact-summarize-results.CoizXkH_.png)_Preview your data in the **Results table**_
      
   
7. Click **+** (plus) and select **Sort** from the query builder.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Sort**_
   
8. Configure the sort step
   
   1. Use the **Data column** drop-down menu to select `Sum of Money saved` and the **Order** drop-down menu to select `Descending`.
      
   2. Preview your data in the **Results** table. This table displays use cases sorted by the amount of money saved.
      
      ![View the results table](/assets/automation-impact-sort-results.DBFDKJQx.png)_Preview your data in the **Results table**_
      
   
9. Visualize your data
   
   Use the **Chart settings** panel to visualize your data and customize your chart.
   
   1. Use the **Type** drop-down menu to select `Bar`.
      
   2. Enter a title, such as `Top money saving use cases`.
      
   3. Use the **Data column** drop-down menu to select `Use case` as the X-axis.
      
   4. Use the **Data column** drop-down menu to select `Sum of Money saved` as the Y-axis.
      
   5. Optional. Provide a unique label for the X and Y axes, such as `Use cases` and `Money saved`. Otherwise, Insights uses the column names for the axes labels.
      
      ![Visualize your data](/assets/automation-impact-money-saved.AWXLmYgo.gif)_Visualize your data_
      
   
10. Click **Save**. You must also save your work at the dashboard level for your changes to persist.
    
11. Create additional charts as necessary. Refer to the tables in the [Metrics for additional charts](#metrics) section for more information.
    
12. Click **Exit** to return to your dashboard.
    
13. Click **Save** to save your work.
    

#### Metrics for additional charts

The following tables contain the metrics required to create the additional charts in this example dashboard.

**ROI: Automation impact**

| Chart title | Metrics | Description |
| --- | --- | --- |
| **Money saved** | Sum of money saved | View the total amount of money saved by automation adoption. |
| **Automated processes** | Count of automated processes | View the total number of automated processes in your workspace. |
| **% adoption** | Count of departments using automation, Count of departments not using automation | Understand the overall adoption of automation company-wide. |
| **Orders processed** | Count of processed orders | Understand efficiency gains by viewing the total number of orders processed through automation. |
| **Invoices processed** | Count of processed invoices | Understand efficiency gains by viewing the total number of invoices processed through automation. |
| **Employees onboarded** | Count of employees onboarded | Understand efficiency gains by viewing the total number of employees onboarded through automation. |
| **Marketing campaigns** | Count of marketing campaigns | Understand efficiency gains by viewing the total number of employees onboarded through automation. |

**Automated use cases**

| Chart title | Metrics | Description |
| --- | --- | --- |
| **Top money saving use cases** | Sum of money saved by project | Understand which projects save you the most money. |
| **Departments using automation** | Cumulative task consumption by department | Understand which teams are using automation the most. |
| **Money saved by use case** | Sum of money saved by project | View a detailed breakdown of how much money each project saves. |

**Workflows and users**

| Chart title | Metrics | Description |
| --- | --- | --- |
| **Total recipes** | Count of recipes | View the total number of recipes in your workspace. |
| **Active recipes (non function)** | Count of active recipes (non function) | View the total number of active recipes in your workspace. |
| **Active builders** | Count of users who have built at least one recipe | View the total number of active recipe builders in your workspace. |
| **Collaborators** | Count of users | View the total number of users provisioned with Workato. |
| **Recipe growth** | Count of recipes by time | Understand recipe building trends over a period of time. |
| **New builders** | Count of users with active recipes by time | Understand user adoption of Workato over time. |

### Add filters

Add [filters](/en/insights/filter-groups) to your dashboard to allow dashboard viewers to explore specific subsets of data. You set a default condition and view during the design stage, but viewers can modify filters, select different conditions, and see the dashboard update dynamically.

Add filters

Complete the following steps to add a filter to your dashboard. This example adds two filters that enable users to filter your report based on time.

1. Select **Filter group** and drag and drop it inside of a container within your dashboard. This allows you to apply a filter to a group of charts. Alternatively, you can apply a filter globally to all charts on your dashboard.
   
2. Go to the properties panel and click **\+ Add filter**.
   
3. Set **Data source** to `Job history` and **Data column** to `Completed at`.
   
4. Configure the **Default value**: Select `is on or after` and a date, for example `03/01/2024`.
   
5. Optional. Provide a custom label for your filter.
   
6. Click **Done**.
   
7. Go to the properties panel and click **\+ Add filter**.
   
8. Set **Data source** to `Job history` and **Data column** to `Completed at`.
   
9. Configure the **Default value**: Select `is on or before` and a date, for example `05/01/2024`.
   
10. Optional. Provide a custom label for your filter.
    
11. Click **Done** and then **Save** to apply the filter to your dashboard.
    
12. Click **Exit**.
    
13. View filter behavior on the Insights homepage. ![View filter behavior](/assets/automation-impact-filter.D6pGNWqp.png)_View filter_
    

## View your completed dashboard

Your dashboard is now complete and can be accessed from the Insights homepage.

![Finsihed ROI dashboard](/assets/roi-automation-impact.B50qCe6R.png)_Completed ROI dashboard_

---
