---
url: 'https://docs.workato.com/en/data-orchestration/cdc-with-triggers.md'
description: >-
  Learn how Workato uses triggers for Change Data Capture (CDC) to monitor,
  capture, and sync database inserts, updates, and deletions in near real time.
---

# Change Data Capture (CDC) with triggers

Change Data Capture (CDC) is a process used to capture and track changes made to data in a database. This process enables real-time or near-real-time monitoring and synchronization of data changes. This allows applications to stay up-to-date with the latest changes in the database without using continuous polling.

The primary goal of CDC is to identify and capture changes such as inserts, updates, and deletions made to database tables. These changes are then propagated to downstream systems, data warehouses, or analytics platforms, ensuring that all systems have access to the most current data.

## How CDC works in Workato

Workato uses [triggers](/en/workato-concepts#triggers) to monitor changes in an app or system you specify. Workato triggers handle CDC by monitoring changes in real-time and providing notifications for those changes, which facilitates data replication and synchronization across different systems.

Triggers follow in-sequence delivery, maintain processed jobs records, prevent duplicate processing, and ensure job completion in order. Trigger dispatches can be single (real-time data sync) or bulk/batch. Bulk/batch provides improved throughput if you are working with large data volumes.

## Supported data sources for CDC

Workato supports CDC for the following data sources:

- Software as a Service (SaaS) platforms
- On-premise systems
- Various databases, such as MySQL, PostgreSQL, and Snowflake
- Workato FileStorage
- Cloud storage services like Amazon S3
- Enterprise Resource Planning (ERP) systems

## Advanced strategies

Explore advanced CDC strategies, including filtering and conditional triggers, handling large volumes of changes, and optimizing performance:

- Filtering and conditional triggers
  
- Advanced CDC strategies include the use of filtering and conditional triggers to manage the flow of data changes. This allows for more granular control over which changes to capture and propagate to downstream systems.
  
- Handling large volumes of changes
  
- Batch processing and micro-batching can be used to efficiently process and transfer if you are working with large volumes of data changes. This helps manage the change load and ensure timely data synchronization.
  
- Optimizing performance
  
- Performance optimization can be achieved through techniques such as built-in cursor management for tracking high watermarks, auto-deduplication, and in-order processing.
  
- Variable speed data pipelines
  
- Workato supports the setup of variable speed data pipelines, including near real-time/continuous data streaming, micro-batches for frequent polling, and batching for periodic schedules. This flexibility allows for tailored data integration strategies that fit specific business needs.

---
