---
url: 'https://docs.workato.com/en/features/sql-transformations-avro-parquet.md'
description: >-
  Learn how SQL Transformations reads Avro and Parquet files, infers their
  schema, and processes high-volume datasets faster than CSV or JSON.
---

# Transform Avro and Parquet files

SQL Transformations supports Avro and Parquet file formats as data sources. These formats allow SQL Transformations to process high-volume datasets more efficiently than CSV and JSON files, processing millions of records in seconds. Their compressed storage reduces file size and transfer time for efficient data processing and integration with modern data lake architectures.

> **CONFIGURATION STEPS**
> 
> Refer to the [Set up your data sources](/en/features/sql-transformations-data-source-setting) documentation for step-by-step instructions on adding data sources and configuring outputs. This page focuses on Avro and Parquet-specific features and behavior.

## How SQL Transformations handles Avro and Parquet files

SQL Transformations processes Avro and Parquet files differently from text-based formats like CSV. Both formats include schema information in the file itself. SQL Transformations reads this schema automatically and identifies available columns and data types without requiring manual configuration.

For Parquet files, SQL Transformations reads only the columns that your query needs, rather than processing entire rows. Parquet's built-in compression also reduces file sizes and accelerates data extraction and loading compared to uncompressed text formats.

You can also output results in Parquet format to improve performance in downstream workflows.

## Example: Analyze sales data from a Parquet file

This example processes quarterly sales data stored as a Parquet file in AWS S3. It transforms transaction records into regional sales performance insights and outputs results in Parquet format for optimal downstream processing.

![Parquet S3 configuration example](/assets/parquet-s3-config.LGrwA52K.png)_Parquet data source configuration from AWS S3_

**Configuration**:

- **Data source name**: `quarterly_sales`
- **Data source type**: Content stream (from S3 Download file action)
- **Content input stream**: File content (Step 2) datapill
- **File format**: Parquet
- **Column schema type**: Infer

**Sample data structure**:

```json
{
  "transaction_id": 847291,
  "sale_date": "2024-10-15",
  "customer_id": 28401,
  "customer_region": "West Coast",
  "product_name": "Wireless Headphones",
  "product_category": "Electronics",
  "product_price": 299.99
}
```

**SQL query for regional sales analysis**:

```sql
SELECT
    customer_region AS region,
    COUNT(*) AS total_transactions,
    SUM(product_price) AS total_revenue,
    AVG(product_price) AS avg_order_value
FROM quarterly_sales
WHERE sale_date >= '2024-10-01'
GROUP BY customer_region
ORDER BY total_revenue DESC
```

This query aggregates sales transactions by region. It identifies markets with the highest revenue and transaction volume and calculates the average purchase amount in each region.

This transformation converts detailed transaction records into executive-level regional performance metrics. The results are saved as `regional_sales_summary.parquet` for efficient loading into business intelligence tools and data warehouses.

**Sample results when loaded into analytics tools (Q4 regional performance)**:

| region | total\_transactions | total\_revenue | avg\_order\_value |
| --- | --- | --- | --- |
| West Coast | 2,847 | $1,247,892.15 | $438.22 |
| East Coast | 2,156 | $987,234.67 | $458.11 |
| Midwest | 1,923 | $756,891.33 | $393.74 |
| South | 1,654 | $612,445.89 | $370.23 |

## Example: Process event data from an Avro file

This example transforms user interaction events from an Avro file in Workato FileStorage into page performance metrics.

![Avro FileStorage configuration example](/assets/avro-filestorage-config.CnyvEw7a.png)_Avro data source configuration from Workato FileStorage_

**Configuration**:

- **Data source name**: `user_events`
- **Data source type**: FileStorage file
- **File path**: `/user_interactions.avro`
- **File format**: Avro
- **Column schema type**: Infer

**Sample event structure**:

```json
{
  "event_id": 1847392,
  "user_id": 28401,
  "user_session_duration": 245,
  "user_session_pages_viewed": 5,
  "event_data_action": "page_view",
  "event_data_page_name": "/product/wireless-headphones"
}
```

**SQL query for page performance analysis**:

```sql
SELECT
    event_data_page_name AS page_path,
    COUNT(*) AS total_visits,
    AVG(user_session_duration) AS avg_session_time_seconds
FROM user_events
WHERE event_data_action = 'page_view'
GROUP BY event_data_page_name
ORDER BY total_visits DESC
```

This transformation converts individual user events into page-level performance metrics. It identifies pages with the highest traffic and user engagement. SQL Transformations saves the results as `page_performance_analysis.csv` for use in BI tools or executive reports.

**Sample output**:

| page\_path | total\_visits | avg\_session\_time\_seconds |
| --- | --- | --- |
| `/home` | 3,247 | 98.5 |
| `/category/electronics` | 1,892 | 145.2 |
| `/product/wireless-headphones` | 847 | 187.3 |
| `/search` | 623 | 112.7 |
| `/account/dashboard` | 412 | 201.5 |
| `/checkout` | 156 | 312.8 |

## Best practices

- Use **Infer schema** for most cases since both formats include embedded schema information.
- For Parquet files, select only needed columns in your SQL queries to take advantage of columnar storage benefits.
- Choose these formats over CSV or JSON when processing large datasets (10M+ records) for faster transformation times.

## Read next

1. [Set up your query](/en/features/sql-transformations-query-setting)
2. [Configure your output](/en/features/sql-transformations-output-setting)
3. [Output fields](/en/features/sql-transformations-output-fields)

---
