---
url: 'https://docs.workato.com/en/insights/workflow-app-dashboard-add.md'
description: >-
  Create and assign an Insights dashboard inside a Workflow app to visualize
  automation data, with end-user download and print support.
---

# Workflow apps dashboards

You can create an Insights dashboard within Workflow apps to visualize and manipulate data to gain valuable insights into your automation projects.

End-users can [download and print](/en/workflow-apps/application-page#print-pages) dashboard pages in the Workflow apps portal. Downloads are saved as PNG images.

## Create a Workflow apps dashboard

You can add a dashboard to your Workflow app in two ways:

- [**Create and assign a dashboard**](#create-and-assign-a-dashboard): Automatically adds the dashboard as a tab in your app.
- [**Create an unassigned dashboard**](#create-an-unassigned-dashboard): Allows you to configure the dashboard before you assign it to your app.

### Create and assign a dashboard

Complete the following steps to create and assign a dashboard to your Workflow app:

1. Select a project that contains an existing Workflow app.
   
2. Go to the **Workflow app** tab, locate the **Interface** section, and click **\+ Create new tab**. ![Add tabs](/assets/app-view-interface-tab.1Mp4JLQ0.png)_Add tabs_
   
3. Enter a [tab](/en/workflow-apps/interface#tabs-add) name in the **Tab name** field.
   
   ![Add new tab](/assets/new-tab.CFqSvCZy.png)_Add new tab_
   
4. Configure which users can view this tab in the **Display tab to** field.
   
   > **DISPLAY TAB TO FIELD**
   > 
   > Select **Nobody** from the **Display tab to** drop-down menu when creating a new dashboard with this method. This hides the dashboard until you make it visible.
   
5. Click **Create tab**.
   
6. Click **Create page** to add a new Insights dashboard to this tab.
   
   ![Create the page](/assets/create-page-tab-method.BRHW11-K.png)_Create the page_
   
7. Enter a name in the **Page name** field. ![Name the page](/assets/page-setup.DtA8n5IC.png)_Name the page_
   
8. Use the **Location** drop-down menu to select the project or folder where you plan to store this page.
   
9. Select **Dashboard** from the list of [page templates](/en/workflow-apps/page-templates). ![Select dashboard](/assets/insights-dashboard-setup-2.CqgG80pp.png)_Select the dashboard template_
   
10. Click **Start building**. This creates a new Workflow apps [page](/en/workflow-apps/page-templates) using the dashboard template:
    
    ![Create the dashboard page](/assets/workflow-apps-dashboard-blank.B54QUsG9.png)_Create the dashboard page_
    
    After you assign an Insights dashboard to your app, it appears in the Workflow apps portal as a separate tab:
    
    ![Insights appears as a separate tab](/assets/dashboard-tab.CPeXJEjr.png)_Insights dashboards appear as a separate tab in the Workflow apps portal_
    

After you create the dashboard, proceed to [configure the dashboard](#configure-the-dashboard).

### Create an unassigned dashboard

Complete the following steps to create the dashboard page separately before you assign it to your Workflow app:

1. Select a project that contains an existing Workflow app. Alternatively, go to **Assets > Pages**.
   
2. Click **Create > Page** or press C+A.
   
   ![Create a new page](/assets/create-page.CyqRLXqu.png)_Create a new page_
   
3. Enter a name in the **Page name** field.
   
   ![Name the page](/assets/page-setup.DtA8n5IC.png)_Name the page_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store this page.
   
5. Select **Dashboard** from the list of [page templates](/en/workflow-apps/page-templates).
   
   ![Select Dashboard as your template](/assets/select-dashboard.Y1Skdbrg.png)_Select **Dashboard** as your template_
   
6. Select a **Data table** for your page:
   
   - If this is the first page in your project, choose a data table from the **Data table** drop-down menu.
   - If no data table exists, [create a new one](/en/data-tables/user-interface/create).
   - If this isn't the first page, the data table is linked automatically.
   
   ![Select a data table for your page](/assets/link-to-table.DP9osLKv.png)_Select a data table for your page_
   
7. Click **Start building**. This creates a new Workflow apps [page](/en/workflow-apps/page-templates) using the dashboard template:
   
   ![Create the dashboard page](/assets/workflow-apps-dashboard-blank.B54QUsG9.png)_Create the dashboard page_
   

After you create the dashboard, [configure it](#configure-the-dashboard) before you assign it to your Workflow app.

## Configure the dashboard

Complete the following steps to configure the Workflow apps dashboard:

1. Drag and drop chart components onto your page in the page editor.
   
   ![Add chart components](/assets/workflow-apps-dashboard-blank.B54QUsG9.png)_Add chart components_
   
   > **PAGE DATA AND DISPLAY COMPONENTS**
   > 
   > Workflow app dashboards are a type of Workflow app page, which means you can use datapills from the **Page data** menu and components from the **Display** section, such as containers and images.
   > 
   > While these datapills and components can't be used within charts, you can use datapills in other areas of the page, including text fields. Display components allow you to control when a container is visible and add images to the page or dashboard for a more customized experience.
   > 
   > Learn more about the [Page data menu](/en/workflow-apps/pages-customize#page-data), [using datapills in pages](/en/workflow-apps/pages-datapill), and [page components](/en/workflow-apps/page-components#display).
   
2. Select a [data source](/en/insights/data-sources) from the list of supported sources.
   
   Workato displays your data as a table by default.
   
3. Run [queries](/en/insights/queries) on your data. Workato previews the results table for each query. ![Results table](/assets/insights-pie-graph-setup-3.DbYAoHk1.png)_Results table_
   
4. Select the type of [chart](/en/insights/charts) you plan to build. Workato previews the auto-generated chart based on your selected data source.
   
5. Configure **Chart settings** to customize your chart. Chart settings are dynamic and depend on the [chart type](/en/insights/charts) you select. ![Chart types](/assets/insights-pie-graph-setup-2.Cka4WWNG.png)_Chart settings_
   
6. Save your chart to your dashboard.
   
7. Click **Save** and **Exit** after you edit the page to return to the [app settings](/en/workflow-apps/app-settings) page.
   

Continue to [assign the dashboard to your Workflow app](#assign-an-existing-dashboard-to-your-workflow-app) if you created an unassigned dashboard. The process is complete if you created an assigned dashboard.

## Assign an existing dashboard to your Workflow app

Complete the following steps to add an unassigned dashboard to your Workflow app:

1. Go to the **Workflow app** tab, locate the **Interface** section, and click **\+ Create new tab**. ![Add tabs](/assets/app-view-interface-tab.1Mp4JLQ0.png)_Add tabs_
   
2. Enter a [tab](/en/workflow-apps/interface#tabs-add) name in the **Tab name** field.
   
   ![Add new tab](/assets/new-tab.CFqSvCZy.png)_Add new tab_
   
3. Configure which users can view this tab in the **Display tab to** field.
   
4. Click **Create tab**.
   
5. Click **Assign existing pages**.
   
   ![Create the page](/assets/create-page-tab-method.BRHW11-K.png)_Create the page_
   
6. Select the dashboard to display in the tab and click **Save changes**.
   
   ![Assign the dashboard to your Workflow app](/assets/assign-existing-page.PQZJRoEg.png)_Assign the dashboard to your Workflow app_
   
   After you assign an Insights dashboard to your app, it appears in the Workflow apps portal as a separate tab:
   
   ![Insights appears as a separate tab](/assets/insights-tab-apps-portal.CS2ySXuv.png)_Insights dashboards appear as a separate tab in the Workflow apps portal_

---
