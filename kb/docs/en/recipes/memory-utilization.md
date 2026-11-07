---
url: 'https://docs.workato.com/en/recipes/memory-utilization.md'
description: >-
  Learn how to optimize recipe memory use, avoid temporary job dispatch
  failures, and handle large batches and files with batch and streaming actions.
---

# Memory optimization best practices

Every recipe job runs in a container that has finite memory allocation. Sometimes, actions in a recipe can cause the container to run out of memory. This leads to a **Temporary job dispatch failure** error. Here are some common recipe design issues with recommended solutions.

## Repeat actions with large batches

Working with large batches in a single job can help to decrease total processing time. This is a very common design pattern than is employed in numerous production recipes. However, it can quickly lead to a heavy memory footprint if these batches are not handled appropriately.

> **Problematic pattern**
> 
> A common mistake is to loop through a large batch and process them individually. To make things worse, it is very common to require multiple steps in each iteration. For example, when looping through a batch of employee records, your recipe logic may require you to search for an existing record, before updating or creating a new record. This can lead to very high memory utilization.

### Solution: Pair batch actions

Batch processing can drastically reduce the cost of working with large batches of records. It also has the benefit of increasing total throughput. Here are some recommended steps:

1. Use batch upsert actions instead of doing search-update-create in a loop. (for example, [SQL Server upsert rows action](/en/connectors/mssql/upsert#upsert-batch-of-rows))
2. If there is a size mismatch between source and destination batch sizes, **repeat in batches** instead of repeating individually.

* * *

## Loading large files into memory

To avoid running into memory issues while transferring large files, Workato actions use [streaming capability](/en/features/file-streaming). This allows a job to transfer large files without consuming memory when running a job.

> **Problematic pattern**
> 
> A common use case is to check the file size using the [`bytesize` formula](/en/formulas/string-formulas#bytesize). This is **not recommended**, as it forces the action to download the entire file into memory to calculate the size of the file.

### Solution: Use file metadata output

All file streaming actions contain additional information about the file in the output datatree. These datapills can be used to determine metadata such as file size without overloading memory. For example, you can use the Size datapill from the [Amazon S3 **Download file** action](/en/connectors/s3/action-download-file).

![Amazon S3 - Download file action](/assets/download-file-action.BLq4JS22.png)_Amazon S3 - Download file action_

### Other recommendations

1. Use file streaming wherever possible, especially if the file is over 100 MB.
2. Use [JDBC Export action](/en/connectors/jdbc/export-query-result) to transfer large query result set

* * *

## Unnecessary use of Collections

[Collections](/en/features/collection) is an in-memory database. This tool allows you to join datasets across various sources before loading into a data warehouse. However, overusing Collections in your recipe can lead to memory issues.

> **Problematic pattern**
> 
> A common mistake is to use Collections to parse a CSV file. While Collections may seem like the right choice, it is not efficient. In fact, this approach requires additional steps to query the data.

### Solution: CSV Parser

Use CSV Parser to achieve the same outcome without incurring additional costs.

---
