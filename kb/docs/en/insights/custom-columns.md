---
url: 'https://docs.workato.com/en/insights/custom-columns.md'
description: >-
  Calculated columns enable you to perform basic data manipulations and
  transformations within the dashboard.
---

# Calculated columns

The calculated columns feature enables you to create calculated columns within Insights dashboards. This allows you to perform custom data manipulations directly within the dashboard environment and eliminates the need for recipe-driven data processing. Calculated columns support [arithmetic, comparison, and logical](/en/insights/operators) operators and numerous built-in [datetime](/en/insights/datetime-functions), [mathematical](/en/insights/math-functions), and [string](/en/insights/string-functions) functions. This enables you to calculate date differences, report on calculated columns you define, manipulate strings, and more without leaving your Insights dashboards.

![Create a calculated column](/assets/custom-column.Dqv-n8rH.gif)_Create a calculated column_

## How to create calculated columns

Creating a calculated column in Insights follows a similar process to other data manipulations. You can begin with an existing dashboard or create a new one and add calculated columns using the query builder. Calculated columns can be used on their own or combined with other queries to help you extract the specific information you require.

![Query builder](/assets/insights-queries.pnyT96qh.png)_Build a calculated column in the query builder_

## Supported operators and functions

Calculated columns support the following operators and functions:

- [Operators](/en/insights/operators): Use arithmetic, comparison, and logical operators to manipulate your data.
- [Datetime functions](/en/insights/datetime-functions): Extract, modify, and calculate time-based values.
- [Mathematical functions](/en/insights/math-functions): Round and manipulate numerical values.
- [String functions](/en/insights/string-functions): Manipulate, format, and analyze text-based values.

## Example use case: Resume screening automation

This use case illustrates how to create a series of calculated columns to track and report on an automated resume screening process. In this example, we log all activities related to this workflow in a data table called `Resume screening`, and capture key details such as ticket IDs, statuses, start dates, and more. All calculated columns in our dashboard rely on this underlying data source.

**Resume screening dashboard**

![Data table](/assets/resume-screening-dashboard.DRD_e0og.png)_Use Calculated columns to report on a resume screening automation_

**Underlying data source**

![Data table](/assets/data-table.0KyksEuQ.png)_The `Resume screening` data table is the underlying data source_

This example use case includes instructions on how to create calculated columns that accomplish the following tasks:

- [Report total time saved in hours](#time-report)
- [Convert currency](#currency-convert)
- [Get open vs. resolved tickets as a ratio](#tickets-get)
- [Show new tickets per quarter](#tickets-new-show)
- [Transform text](#text-transform)

### Getting started

The following steps are common to all calculated columns created in this use case. Complete these steps to get started:

1. Go to **Platform > Insights**. Create a new dashboard or select one of your existing dashboards.
   
2. Add a new chart component to your dashboard and click **Edit chart data**.
   
3. Select a data source
   
   Select the event data source you plan to report on. Our example reports on the time saved from an automated resume screening process, which we capture in a data table.
   
   1. In the **Use data from** field, select `Data tables` as the **Source type** and `Resume screening` as the **Data source**.
      
      ![Data source](/assets/resume-screening-data-source.B9aN86Jo.png)_Select a data source_
      
   

### Report total time saved in hours

Complete the following steps to create a calculated column that reports the total time saved in hours in your Insights dashboard:

1. Click **+** (plus) and select the **Filter** step from the query builder.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Filter**_
   
2. Configure the filter to surface tickets with the Closed status only
   
   1. Select `Status` as the **Data column**.
      
   2. Select `equals` from the **Condition** drop-down.
      
   3. Select `Closed` as the **Value**.
      
   4. Preview your data in the **Results table**. This table displays tickets with the `Closed` status only.
      
      ![Results table](/assets/time-filter.BC_FzjjZ.png)_Preview your data in the **Results table**_
      
   
3. Click **+** (plus) and select **Calculated column** from the query builder.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Calculated column**_
   
4. Configure the calculated column
   
   1. Provide a unique name for the new column, such as `Processing time`.
      
   2. Create a custom **Column expression**. Select the `date_diff` function. Change the duration from `"day"` to `"hour"` and map in the Created at and Completed at datapills.
      
      **Column expression** (required):
      
      \= `date_diff("hour",`{{Created at}}`,`{{Completed at}}`)`
      
   3. Preview your data in the **Results table**. This table displays the time taken to complete a process.
      
      ![Results table](/assets/time-custom-column.DjV1Dwj0.png)_Preview your data in the **Results table**_
      
   
5. Click **+** (plus) and select **Summarize** from the query builder.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select Summarize_
   
6. Configure the summarize step
   
   1. Select `Sum of` from the **Metrics** drop-down and `Processing time` from the **Data column** drop-down.
      
   2. Click **\+ New metric**.
      
   3. Select `Sum of` from the **Metrics** drop-down and `Old processing time` from the **Data column** drop-down.
      
   4. Preview your data in the **Results table**. This table displays the total old processing time in hours and the total new processing time in hours.
      
      ![Results table](/assets/time-summarize.C-mbZvft.png)_Preview your data in the **Results table**_
      
   
7. Click **+** (plus) and select **Calculated column** from the query builder.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Calculated column**_
   
8. Configure the calculated column
   
   1. Provide a unique name for the new column, such as `Time saved (hours)`.
      
   2. Create a custom **Column expression**. Map in the Sum of Old processing time datapill, enter the `-` (subtract) operator, and map in the Sum of Processing time datapill:
      
      **Column expression** (required):
      
      \= {{Sum of Old processing time}}`-` {{Sum of Processing time}}
      
   3. Preview your data in the results table. The table displays the amount of time saved in hours.
      
      ![Results table](/assets/results-table-hours-saved.DVQCyvxG.png)_Preview your data in the **Results table**_
      
   
9. Visualize your data
   
   Use the **Chart settings** panel to visualize your data and customize your chart.
   
   1. Select `KPI` from the **Type** drop-down.
      
   2. Select `Time saved (hours)` from the **Data column** drop-down.
      
   3. Optionally, provide a unique label for this chart, such as `Total hours saved`. When you leave this field blank, the label is the column name you selected in the previous step.
      
   4. Click **Save to page** to save the chart to your dashboard.
      
      ![Visualize your data](/assets/time-saved.APoZKvVv.gif)_Visualize your data_
      
   
10. Click **Save** to save your dashboard.
    

### Convert currency

This example converts currency from EUR (Euros) to USD (US dollars) by multiplying a euro amount by a constant. This is helpful when your organization has multiple regional cost centers and must convert them to a common currency.

Complete the following steps to create a calculated column that converts currency from EUR to USD in your Insights dashboard:

1. Click **+** (plus) and select the **Summarize** query.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Summarize**_
   
2. Configure the summarize step to get a sum of total money saved in EUR
   
   1. Select `Sum of` from the **Metrics** drop-down.
      
   2. Select `Money saved (EUR)` from the **Data column** drop-down.
      
   3. Preview your data in the **Results table**. This table displays the new total sum of money saved in EUR.
      
      ![Results table](/assets/money-summarize.D1ad9Xz8.png)_Preview your data in the **Results table**_
      
   
3. Click **+** (plus) and select the **Calculated column** query.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Calculated column**_
   
4. Configure the calculated column
   
   1. Provide a unique name for the new calculated column, such as **Money saved (USD)**.
      
   2. Map in the Sum of Money saved (EUR) datapill and multiply it by the exchange rate, `1.05`.
      
      **Column expression** (required):
      
      \= {{Sum of Money saved (EUR)}}`*1.05`
      
   3. Preview your data in the **Results table**. This table displays the sum of money saved in USD.
      
      ![Results table](/assets/results-table-money-saved.a78aeVvw.png)_Preview your data in the **Results table**_
      
   
5. Visualize your data
   
   1. Select `KPI` from the **Type** drop-down.
      
   2. Select `Money saved (USD)` from the **Data column** drop-down.
      
   3. Optionally, provide a unique label for this chart, such as `Money saved (USD)`. When you leave this field blank, the label is the column name you selected in the previous step.
      
   4. Click **Save to page** to save the chart to your dashboard. ![Visualize your data](/assets/money-saved.FwYpY-YT.gif)_Visualize your data_
      
   
6. Click **Save** to save your dashboard.
   

### Get resolution rate as a percentage

This example demonstrates how to get a resolution rate as a percentage. In this example, we are interested in reporting on the efficiency of our resume screening process as it relates to our effectiveness in filling positions. To accomplish this, we track each position in a data table, where tickets with the `closed` status are filled and tickets with the `new` status are open.

Complete the following steps to create a calculated column that displays the ticket resolution rate as a percentage:

1. Click **+** (plus) and select the **Summarize** step.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Summarize**_
   
2. Configure the summarize step to get a count of rows
   
   1. Select `Count of rows` from the **Metrics** drop-down.
      
   2. Select `Status` from the **Data column** drop-down.
      
   3. Preview your data in the **Results table**. This table displays the number of closed and open tickets.
      
      ![Preview results table](/assets/percentage-summarize.BkqMgmNB.png)_Preview your data in the **Results table**_
      
   
3. Click **+** (plus) and select the **Summarize** step.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Summarize**_
   
4. Configure the Summarize step to obtain the minimum, maximum, and cumulative row count
   
   **_This step operates under the assumption that there are fewer resolved tickets than open tickets. If the contrary is true for your use case, adjust the logic accordingly. You can view the distribution of statuses in the results table of the preceding step._**
   
   1. Select `Min of` from the **Metrics** drop-down and `Count of rows` from the **Data column** drop-down. This step counts the number of resolved tickets (tickets with the `closed` status).
      
   2. Click **\+ New metric**.
      
   3. Select `Max of` from the **Metrics** drop-down and `Count of rows` from the **Data column** drop-down. This step counts the number of open tickets (tickets with the `new` status).
      
   4. Click **\+ New metric**.
      
   5. Select `Cumulative sum of` from the **Metrics** drop-down and `Count of rows` from the **Data column** drop-down. This step adds the number of open and closed tickets together to obtain the total number of tickets.
      
   6. Preview your data in the **Results table**. This table displays the number of closed, open, and total tickets.
      
      ![Preview results table](/assets/percentage-summarize-2.4JAs0Xl4.png)_Preview your data in the **Results table**_
      
   
5. Click **+** (plus) and select the **Calculated column** step.
   
6. Configure the calculated column to calculate the percentage of resolved tickets
   
   1. Provide a **Column name**, such as `Percentage`.
      
   2. Select the `round` function, divide the number of closed tickets (Min of Count of rows) by the number of total tickets (Cumulative count of rows), and multiply the result by 100.
      
      **Column expression** (required):
      
      \= `round(`{{Min of Count of rows}}`/`{{Cumulative count of rows}}`*100, 1)`
      
   3. Preview your data in the **Results table**. This table displays the number of resolved tickets as a percentage.
      
      ![Results table](/assets/percentage-results-table.CnHUxA6P.png)_Preview your data in the **Results table**_
      
   
7. Visualize your data
   
   1. Select `KPI` from the **Type** drop-down.
      
   2. Select `Percentage` from the **Data column** drop-down.
      
   3. Optionally, provide a unique label for this chart, such as `% Placement rate`. When you leave this field blank, the label is the column name you selected in the previous step.
      
   4. Click **Save to page** to save the chart to your dashboard.
      
      ![Visualize your data](/assets/percentage.sdv3logt.gif)_Visualize your data_
      
   
8. Click **Save** to save your dashboard.
   

### Show new tickets per quarter (custom date unit)

Calculated columns enable you to create custom date units, allowing you to track business events quarterly, regardless of when your fiscal year begins (January, February, or March).

Complete the following steps to create a calculated column that displays new tickets per quarter:

1. Click **+** (plus) and select the **Calculated column** query.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Calculated column**_
   
2. Configure the calculated column
   
   1. Provide a unique name for the new calculated column, such as `Quarter`.
      
   2. Select the `floor` and `month` function and map in the Created at datapill. This expression extracts the month from the date the ticket was created, rounds the input down, and divides the result to determine the quarter.
      
      **Column expression** (required):
      
      \= `floor((month(`{{Created at}}`)-2+12)/3%4)+1`
      
   3. Preview your data in the **Results table**. This table displays the quarter in which each ticket was created.
      
      ![Results table](/assets/tickets-custom-column.B6p45uE4.png)_Preview your data in the **Results table**_
      
   
3. Click **+** (plus) and select the **Summarize** query.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Summarize**_
   
4. Configure the Summarize query to get the number of tickets created each quarter
   
   1. Select `Count of rows` from the **Metrics** drop-down.
      
   2. Select `Quarter` from the **Data column** drop-down.
      
   3. Preview your data in the **Results table**. This table shows the number of tickets created each quarter.
      
      ![Results table](/assets/tickets-summarize.DwirS3kL.png)_Preview your data in the **Results table**_
      
   
5. Visualize your data
   
   1. Select `Bar` from the **Type** drop-down.
      
   2. Provide a unique title for this chart, such as `New tickets per quarter`.
      
   3. Optionally, customize your X- and Y-axis labels. Otherwise, the label is the data column name.
      
   4. Click **Save to page** to save the chart to your dashboard.
      
      ![Visualize your data](/assets/tickets.DnGtw7f8.gif)_Visualize your data_
      
   
6. Click **Save** to save your dashboard.
   

### Transform text

In this example, we plan to display each new hire's name and start date. However, our data contains a mix of lowercase and title case names.

Complete the following steps to create a calculated column that transforms text from lowercase to title case:

1. Click **+** (plus) and select the **Filter** query.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Filter**_
   
2. Configure the filter step to get closed tickets
   
   1. Select `Status` from the **Data column** drop-down.
      
   2. Select `equals` from the **Condition** drop-down.
      
   3. Select `Closed` as the **Value**.
      
   4. Preview your data in the **Results table**. This table displays closed tickets only.
      
      ![Results table](/assets/text-filter.D3pKdaSA.png)_Preview your data in the **Results table**_
      
   
3. Click **+** (plus) and select the **Calculated column** query.
   
   ![Available queries](/assets/insights-queries.pnyT96qh.png)_Select **Calculated column**_
   
4. Configure the calculated column
   
   1. Provide a unique name for the new calculated column, such as `Employee names`.
      
   2. Select the `titleize` function and map in the Candidate name datapill.
      
      **Column expression** (required):
      
      \= `titleize(`{{Candidate name}}`)`
      
   3. Preview your data in the **Results table**. This table displays the names of the new hires in title case.
      
      ![Results table](/assets/text-custom-column.BvKSNiSs.png)_Preview your data in the **Results table**_
      
   
5. Visualize your data
   
   1. Select `Table` from the **Type** drop-down.
      
   2. Provide a unique title for this chart, such as `New hires`.
      
   3. Select which columns to display in your table.
      
   4. Optionally, rearrange columns to customize the order in which they appear in the table.
      
   5. Click **Save to page** to save the chart to your dashboard.
      
      ![Visualize your data](/assets/text.Cjwig0MV.gif)_Visualize your data_
      
   
6. Click **Save** to save your dashboard.

---
