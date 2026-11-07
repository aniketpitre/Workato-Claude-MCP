---
url: 'https://docs.workato.com/en/insights/charts.md'
description: >-
  Reference for Insights chart types, including tables, line, area, and bar
  graphs, pie charts, and KPI charts for visualizing your data.
---

# Chart types

![Chart editor](/assets/insights-pie-graph-setup.DLr9X1fr.png)_Chart editor_

You can create custom charts with your data after you've chosen a [data source](/en/insights/data-sources) and prepared it by performing [queries](/en/insights/queries). Visualizing your data involves determining the metrics and dimensions you plan to represent.

- **Metric**: Quantitative values that you plan to analyze, track, and present visually. Metrics can be aggregated to find the sum, average, or count. It's typically the key performance indicator (KPI) or main value you plan to report on.
- **Dimension**: Categorical variables that give context or descriptive information to the metrics in your report. Dimensions are used for slicing, grouping, and filtering data.

For example, you might plan to analyze the number of successful and failed jobs (metric) by Environment (dimension). You can use the Environment dimension to determine if integrations are performing well in your DEV, TEST, or PROD environments. Similarly, you can analyze money saved (metric) by project (dimension) to understand which projects are saving you the most money.

Insights displays your data as a table by default. You can use the **Type** drop-down menu to select a chart and customize it. Insights supports the following chart types for data visualizations:

- [Table](#table)
- [Line graph](#line-graph)
- [Area graph](#area-graph)
- [Bar graph](#bar-graph)
- [Pie chart](#pie-chart)
- [KPI chart](#kpi-chart)

* * *

## Table

Tables are a structured way to present organized information with rows and columns. They are particularly useful when presenting data with multiple dimensions, comparisons, or detailed information.

For example, the following table contains data for all business processes and provides detailed, exact data on the cost for each workflow run.

![Table (default view)](/assets/insights-table.CWVe63Xt.png)_Table_

By default, Insights displays your data as a table. To customize this table, configure the following input fields:

- Title
  
- Name your chart. The name you enter here displays on your Insights dashboard.
  
- Displayed columns
  
- Select the columns you plan to display in your chart. Click **Select all** to select/deselect all columns for display or select columns individually. Reorganize your columns by dragging and dropping them into place. This output is dynamic and depends on the **data source** you select. See [Data sources](/en/insights/data-sources) for a description of the data available, organized by source.
  

* * *

## Line graph

Line graphs are suited for displaying trends and changes over time. They are particularly effective at illustrating how a variable or multiple variables change in relation to each other as time progresses.

**Visualize request volume**

The following line graph represents the number of onboarding requests an HR team receives each day.

![Line graph](/assets/insights-line-graph.BwVoPyDg.png)_Line graph_

**Customize colors**

Customize the colors of your line graph by clicking the color swatch next to the data column you plan to change.

![Customize the colors of your line graph](/assets/line-graph-colors-customize.DFQ2JVkp.png)_Customize the colors of your line graph_

**Segment data**

The following line graph segments data to represent the distribution of task usage across environments.

![Break down your data by data column](/assets/line-graph-breakdown.C-SNjZiY.png)_Break down your data by data column_

**Segment data detail**

Hover over your chart to view the exact distribution of data for each segment.

![More details on hover](/assets/line-graph-breakdown-hover.e9hbvU_n.png)_Hover over your chart to view the exact distribution of data_

To customize your line graph, configure the following input fields:

- Title
  
- Name your chart. The name you enter here displays on your Insights dashboard.
  
- X-axis
  
- - Data column
    
  - Determine a dimension column. The option you select here appears as categories on the x-axis.
    
  - Breakdown by data column
    
  - _Optional_. Line graphs can display segments of your data in different colors, enhancing understanding by visually distinguishing between categories or groups. This facilitates quick comparisons and highlights trends or patterns, making it useful for displaying job success and error rates, as well as trends over time, such as task consumption across environments.
    
  - Label
    
  - Provide a label for the x-axis. If you do not enter a label, Insights supplies the name of the data column you selected in the **Data** field.
    
- Y-axis
  
- - Data column
    
  - Determine a measure column. The option you select here appears as values on the y-axis. Insights only displays numeric data columns (integer or decimal) for the y-axis.
    
  - Label
    
  - Provide a label for the y-axis. If you do not enter a label, Insights supplies the name of the data column you selected in the **Data** field.
    

* * *

## Area graph

Area graphs are useful for displaying quantitative data over time, typically illustrating how values change in relation to one another. They are particularly suited to displaying trends, such as task consumption over time.

**Visualize task consumption**

The following area graph displays cumulative task consumption for the past 365 days. ![Area graph](/assets/insights-area-setup.CUMuy9kA.png)_Use an area graph to visualize task consumption_

**Customize colors**

Customize the colors of your area graph by clicking the color swatch next to the data column you plan to change.

![Customize the colors of your area graph](/assets/area-graph-colors-customize.CmNRRzCx.png)_Customize the colors of your area graph_

**Segment data**

The following area graph segments data to represent the distribution of task usage across environments.

![Break down your data by data column](/assets/area-graph-breakdown.DoT2noMi.png)_Break down your data by data column_

**Segment data detail**

Hover over your chart to view the exact distribution of data for each segment.

![More details on hover](/assets/area-graph-breakdown-hover.C2gveMV0.png)_Hover over your chart to view the exact distribution of data_

To customize your area graph, configure the following input fields:

- Title
  
- Name your chart. The name you enter here displays on your Insights dashboard.
  
- X-axis
  
- - Data column
    
  - Select a column to measure. The column you select is represented as a block of color on the x-axis.
    
  - Breakdown by data column
    
  - _Optional_. Area graphs can display segments of your data in different colors, enhancing understanding by visually distinguishing between categories or groups. This facilitates quick comparisons and highlights trends or patterns, making it useful for showing job success and error rates, as well as trends over time, such as task consumption across environments.
    
  - Label
    
  - Provide a label for the x-axis. If you do not enter a label, Insights supplies the name of the data column you selected in the **Data column** field.
    
- Y-axis column
  
- - Data column
    
  - Select a column to use to measure the category you selected for the x-axis. The data column you select determines the area of the graph that is filled. Insights only displays numeric data columns (integer or decimal) for the y-axis.
    
  - Label
    
  - Provide a label for the y-axis. If you do not enter a label, Insights supplies the name of the data column you selected in the **Data column** field.
    

* * *

## Bar graph

Bar graphs are particularly effective for representing categorical data and comparing discrete values across different categories.

**Visualize success and failure rates**

The following bar graph displays the number of successful and failed jobs over time:

![Successful and failed jobs](/assets/insights-bar-graph.BTxAkIEq.png)_Successful and failed jobs over time_

**Customize colors**

Customize the colors of your bar graph by clicking the color swatch next to the data column you plan to change.

![Select a color](/assets/bar-graph-color-select.DtHt-p7G.png)_Customize the colors of your bar graph_

**Segment data**

The following bar graph segments data to represent the relationship between successful and failed jobs in a workspace over time.

![Break down your data by data column](/assets/bar-graph-breakdown.DfgjydY1.png)_Break down your data by data column_

**Segment data detail**

Hover over your chart to view the exact distribution of data for each segment.

![More details on hover](/assets/bar-graph-breakdown-hover.B4Shk9gE.png)_Hover over your chart to view the exact distribution of data_

To customize your bar graph, configure the following input fields:

- Title
  
- Name your chart. The name you enter here displays on your Insights dashboard.
  
- X-axis
  
- - Data column
    
  - Determine a dimension (category) column. Each category is represented as a bar on the x-axis.
    
  - Breakdown by data column
    
  - _Optional_. Bar charts can display segments of your data in different colors, enhancing understanding by visually distinguishing between categories or groups. This facilitates quick comparisons and highlights trends or patterns, making it useful for showing job success and error rates, as well as trends over time, such as task consumption across environments.
    
  - Label
    
  - Provide a label for the x-axis. If you do not enter a label, Insights supplies the name of the data column you selected in the **Data column** field.
    
- Y-axis
  
- - Data column
    
  - Determine a measure column. The data column you select dictates the size of the bars in your graph. Insights only displays numeric data columns (integer or decimal) for the y-axis.
    
  - Label
    
  - Provide a label for the y-axis. If you do not enter a label, Insights supplies the name of the data column you selected in the **Data column** field.
    

* * *

## Pie chart

Pie charts are ideal for displaying parts of a whole, emphasizing the proportion of each category relative to the total. They are especially effective for showing the distribution of a single data set into different categories.

**Visualize active recipes**

The following pie chart represents the distribution of active recipes across environments.

![Pie chart](/assets/insights-pie-chart.Cfk2nrgY.png)_Pie chart_

**Customize colors**

Customize the colors of your pie chart by clicking the color swatch next to the data column you plan to change.

![Customize colors](/assets/pie-chart-color-select.DVVEWlHG.png)_Customize the colors of your pie chart_

To customize your pie chart, configure the following input fields:

- Title
  
- Name your chart. The name you enter here displays on your Insights dashboard.
  
- Dimension
  
- Determine the value you plan to measure.
  
- Measure
  
- Determine the measure. The measure determines the angle of each slice in a pie chart. This value must be an integer or decimal column.
  

* * *

## KPI chart

KPI charts draw attention to data you plan to emphasize in your dashboard, such as conclusions, outliers, or high-performing metrics.

For example, the following KPI chart represents average task consumption per month for the last 365 days.

![KPI chart](/assets/insights-number-graph.DpJMrjIM.png)_KPI chart_

To customize your KPI chart, configure the following input fields:

- Title
  
- Name your chart. The name you enter here displays on your Insights dashboard.
  
- Measure
  
- Determine the measure, which is a column containing the value you plan to display on the chart. This value must be an integer or decimal column.
  

> **FURTHER READING**
> 
> - [Data sources and available data](/en/insights/data-sources)
> - [Queries](/en/insights/queries)

---
