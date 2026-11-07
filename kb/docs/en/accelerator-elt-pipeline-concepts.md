---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-concepts.md'
description: >-
  Learn the core concepts behind the ELT Pipeline for Snowflake accelerator:
  ELT, pipelines, sources, staging, targets, and data warehouses.
---

# ELT Pipeline concepts

The following concepts form the underlying logic of the **ELT Pipeline for Snowflake accelerator**.

- [ELT](#elt)
- [Pipeline](#pipeline)
- [Source](#source)
- [Staging](#staging)
- [Target](#target)
- [Data warehouse](#data-warehouse)

## ELT

This accelerator follows an ELT (extract, load, and transform) approach, as opposed to ETL (extract, transform, and load). In ELT, Workato extracts data from a source application, loads it into a data lake or warehouse, and then performs any necessary transformations to the data. By removing the rigid extract and transform (ET) bottleneck from the initial phase this accelerator makes data available for querying and analysis without requiring complex logic before loading the data for storage in a data lake or warehouse.

Data lakes provide unstructured data support and more flexibility for thorough data analysis. They also enable users to continue building data pipelines iteratively. Data lakes, cloud storage, and modern data warehouses analytics provide simpler architecture to build pipelines. These frameworks remove extra management as it scales automatically based on the workload. This approach lowers total upfront cost, provides fast extraction and loading, more flexibility and lower maintenance costs.

## Pipeline

In an ELT context, a pipeline is a framework designed to extract data from the source to target using scheduling and bulk batch processing capabilities. Source, staging, and target connectors provide the underlying actions and triggers for creating, maintaining, extracting, staging, and loading data in a pipeline. The connectors you use can vary. You can use bulk and streaming actions coupled with cost effective cloud storage and modern cloud data warehouses to increase pipeline efficiency. Pipelines can have one or multiple [jobs](/en/accelerator-elt-pipeline-design#job-types) depending on their frequency.

## Source

Workato's wide range of SAAS and on-prem agent (OPA) connectors provide various options on how to extract data from source applications using APIs, recipes, or SQL or OS file transfer commands. Typically, sources are transactional SaaS, on-prem databases, file systems (CSV and JSON formats), and web logs.

Each source system has its own nuances and challenges. Some source connectors, including Salesforce provide bulk actions which are used in this accelerator.

## Staging

Staging is a cost effective storage solution that involves dumping data without structure or query optimization in a data lake. Staging is the intermediate step between loading raw data in the data warehouse with some minor transformation. Staging tables are either ephemeral or persistent and can be used at different stages of a pipeline. You may archive persistent tables into cold storage if necessary. This accelerator uses S3 and Snowflake's internal file system as a staging area for raw data.

## Target

Target tables are intermediate to final destinations in a subset of a pipeline where a more refined version of the source tables are inserted, updated, or merged. Use these tables as a cleansed, restructured, and integrated version of tables originating from the source. Apply business rules to transform, structure, and optimize data for further analysis and transformations.

## Data warehouse

A data warehouse is an optimized storage, transformation, and analytics engine. There are multiple iterations of cleansing, integrating, and restructuring intermediate tables before a final version with wide table or star schema model is applied.

The majority of data warehouses are built on highly scalable columnar databases which can run transformations on large data sets in a cost effective manner by using its internal efficient I/O, data compression, and multi node processing. Workato uses Snowflake as a data warehouse for this accelerator.

---
