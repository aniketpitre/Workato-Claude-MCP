---
url: 'https://docs.workato.com/en/connectors/google-analytics/get-report-action.md'
description: >-
  The Get report action returns a customized report of Google Analytics event
  data. Reports contain statistics derived from data collected by the Google
  Analytics tracking code.
---

# Google Analytics - Get report action

The **Get report** action returns a customized Google Analytics event data report. The report contains statistics derived from data collected by the Google Analytics tracking code.

## Input

| Input field | Description |
| --- | --- |
| Account | Select the account from the drop-down menu. |
| Property | Select the property from the drop-down menu. |
| Dimensions | Provide the dimensions source list and select the dimension fields from the drop-down menu. Dimensions are attributes of your data. |
| Metrics | Provide the metrics source list and select the metric fields from the drop-down menu. Metrics are the quantitative measurements of a report. |
| Date ranges | Provide the date ranges of data to read. The provided start date and end date will be included in the query. If left blank, the start date will default to seven days ago, and the end date will be today. |
| Dimension filters | Specify dimension filters to return only specific dimension values in the report. Provide `AND`, `OR` or `NOT` expressions as needed. |
| Metric filters | Provide the filter clause of metrics which will be applied after aggregating the report's rows. Provide `AND`, `OR`, or `NOT` expressions as needed. |
| Offset | Provide the row count of the start row. The first row is counted as row 0. |
| Limit | Specify the number of rows to return. If unspecified, 10,000 rows are returned. |
| Metric aggregations | Select the aggregation of metrics from the drop-down menu. |
| Order bys | Provide the parameters to sort the result sets. This field specifies how rows are ordered in the response. |
| Currency code | Provide the currency code in ISO format, such as USD. |
| Cohort spec | Provide the cohort specs such as cohorts, cohorts range, and cohort report settings. |
| Keep empty rows | Specify whether to keep empty rows. If false or unspecified, each row with all metrics equal to 0 is not returned. If true, these rows are returned. |
| Return property limit | Specify whether to return the current state of this Analytics property's quota. |

## Output

| Output field | Description |
| --- | --- |
| Dimension headers | A list of dimension columns. The number of dimension headers and ordering of dimension headers matches the dimensions present in rows. |
| Metric headers | A list of metric columns. The number of metric headers and ordering of metric headers matches the metrics present in rows. |
| Rows | Rows of dimension value combinations and metric values in the report. |
| Totals | Displays the totaled values of metrics if requested. |
| Maximums | Displays the maximum values of metrics if requested. |
| Minimums | Displays the minimum values of metrics if requested. |
| Row count | The total number of rows available for the report. This may be greater than the number of rows returned if pagination is used. |
| Metadata | Contains information about the report. |
| Property limit | Represents this Google Analytics property's quota state including this request. |
| Kind | Identifies what kind of resource this message is. |

---
