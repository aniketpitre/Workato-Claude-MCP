---
url: 'https://docs.workato.com/en/insights/queries.md'
description: >-
  Build queries on your Insights data with a no-code, step-based query builder
  that filters, summarizes, joins, sorts, and adds calculated columns.
---

# Query components

Insights enables you to perform queries on your data using a no-code interface.

![Query builder](/assets/insights-query-run.BfCIhzZj.png)_Build a query_

* * *

## How it works

The query builder occupies the left part of the page. Similar to the recipe editor, you can build queries in a series of sequential steps (operations).

- Each step operates on the columns derived from the previous steps. Initially, the available columns is defined by the data source you select. Some queries, including summarize and join, can change the column set.
  
- You can build queries with steps in any order. Your queries can contain any amount of steps.
  
- Workato also generates a data preview (results table) for your query, occupying the bottom right of the page. Before you visualize your data, make sure this preview appears as expected.
  

* * *

### Available queries

Insights supports the following queries:

- [Filter](#filter-by)
- [Summarize](#summarize)
- [Join to](#join-to)
- [Sort](#sort-by)
- [Row limit](#row-limit-to)
- [Calculated column](#custom-column)

![Available queries](/assets/insights-queries.pnyT96qh.png)_Available queries_

* * *

## Filter

Extract the information you need from your dataset by specifying criteria the data must satisfy.

To filter your data, specify the following:

- Data column
  
- Select the data column you plan to filter.
  
- Condition
  
- Specify the criteria the data you've chosen must satisfy. Available conditions depend on the type of data you select. You can chain conditions using **AND**.
  
- Value
  
- Certain conditions require you to specify the **Value**. For example, if you apply a filter to a **Short text** column and apply an **Equals** condition, you must supply the **Value** your data must equal.
  

The following conditions are available, based on data type:

Text

**Available operands:**

- Equals
- Contains
- Starts with
- Ends with
- Is not equal to
- Is null
- Is not null

Integer

**Available operands:**

- Equals
- Is not equal to
- Is less than
- Is greater than
- Is less or equals
- Is greater or equals
- Is null
- Is not null

Decimal

**Available operands:**

- Equals
- Is not equal to
- Is less than
- Is greater than
- Is less or equals
- Is greater or equals
- Is null
- Is not null

Boolean

**Available operands:**

- Is true
- Is false
- Is null
- Is not null

Date

**Available operands:**

- Is
- Within
- Is on or before
- Is on or after
- Is null
- Is not null

DateTime

**Available operands:**

- Is
- Within
- Is on or before
- Is on or after
- Is null
- Is not null

* * *

## Summarize

Present aggregated or summarized information from your dataset.

- Metrics
- You can summarize your data using the following available metrics:

- Count of rows
- Sum of
- Average of
- Median of
- Max of
- Min of
- Cumulative count of rows
- Cumulative sum of
- Cumulative average of

Cumulative functions are usually used with grouping by a Date or Date Time column and enable you to display the total progress of a certain metric over time.

- Data column
  
- Select the data column on which you plan to perform the function.
  
- by Data column
  
- In the **By data column** block, determine how to organize (group) the data. In the following example, we used a summarize query to return the sum of dollars saved, organized by process.
  

![Summarize query](/assets/insights-query-summarize.Dfzr3HPB.png)_Summarize query_

- by Rule
- This function is only available for date and datetime data types. Available rules include:
  - - By week
    - By month
    - By day

* * *

## Join to

Combine data from multiple sources into a single result set. This feature helps retrieve related information from different tables or datasets, such as getting details about orders along with customer information.

You can also join data sources of different types. For example, you can combine the following data sources using a join:

- Job history report table
- Customer data table

In this example, both data sources include the **Customer ID** calculated column. Use this column to connect customer information from the customer data table with the job history report table.

### Join types

- Insights supports the following join types. The behavior of each join type uses the preceding example:
  - Inner join
  - Combines rows from both tables where the **Customer ID** matches. It appends columns from the customer data table to the job history report. Only rows with a corresponding **Customer ID** in both tables are included in the result.
  - Left join
  - Starts with all rows from the job history report (left table) and adds matching columns from the customer data table (right table) where the **Customer ID** matches. If no match exists, columns from the customer data table contain NULL values.
  - Right join
  - Starts with all rows from the customer data table (right table) and adds matching columns from the job history report (left table) where the **Customer ID** matches. If no match exists, columns from the job history report table contain NULL values.
- Source type
- Select the type of data you plan to use. You can choose from any of the [data sources](/en/insights/data-sources) Insights supports.
- Data source
- Select the specific data source.
- On current result
- Select a data column from your original data source that you plan to join with your secondary data source.
- {Data source}
- The name of this field is dynamic and depends on the data source you select from the drop-down menu. Select a data column from your secondary data source that you plan to join to your original data source.

* * *

## Sort by

Sort your data by choosing one or more columns from the drop-down menu. If you select multiple columns, the data sorts first by the primary column (the first column). For rows with identical values in the primary column, sorting proceeds by the secondary column, and so on. You can sort data in ascending or descending order.

- Data column
  
- Select a column from the drop-down.
  
- Order
  
- Sort the data in **Ascending** or **Descending** order.
  

> **SORT ORDER**
> 
> You can place the sort step last in your query to ensure results appear in a specific order. Steps added after sort may change or override the sort order.

* * *

## Row limit to

Limit the number of rows of data Workato displays.

- Limit row number
- Determine the number of entries to display.

* * *

## Calculated column

Create [calculated columns](/en/insights/custom-columns) using [string](/en/insights/string-functions), [datetime](/en/insights/datetime-functions), and [mathematical](/en/insights/math-functions) functions and [operators](/en/insights/operators).

- Column name
  
- Provide a unique name for the new calculated column that identifies what this column reports on.
  
- Column expression
  
- Map in datapills, functions, and operators to perform data manipulations and transformations. The result of the custom manipulation results in a new column.
  

> **FURTHER READING**
> 
> - [Dashboards](/en/insights/dashboards)
> - [Data sources and available data](/en/insights/data-sources)
> - [Chart types](/en/insights/charts)

---
