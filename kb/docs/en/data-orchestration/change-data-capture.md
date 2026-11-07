---
url: 'https://docs.workato.com/en/data-orchestration/change-data-capture.md'
description: >-
  Learn how Change Data Capture (CDC) in Workato tracks database inserts,
  updates, and deletions and syncs them to downstream systems using triggers.
---

# Change data capture

Change Data Capture (CDC) captures and tracks changes in a database, enabling real-time or near-real-time monitoring and synchronization. CDC allows applications to stay up-to-date with the latest database changes without continuous polling.

CDC identifies inserts, updates, and deletions in database tables and propagates these changes to downstream systems, data warehouses, or analytics platforms. This ensures that all systems access the most current data.

## How CDC works in Workato

Workato uses [triggers](/en/workato-concepts#triggers) to monitor changes in an app or system you specify. Workato triggers handle CDC by monitoring changes in real-time and providing notifications for those changes, which facilitates data replication and synchronization across different systems.

Triggers deliver jobs in sequence, track processed jobs, prevent duplicates, and ensure job completion in order. Triggers dispatch data as single events for real-time synchronization or in bulk/batch mode to improve throughput when processing large datasets.

## Supported data sources for CDC

Workato supports CDC for the following data sources:

- Software as a Service (SaaS) platforms
- On-premises systems
- Databases, such as MySQL, PostgreSQL, and Snowflake
- Workato FileStorage
- Cloud storage services such as Amazon S3
- Enterprise Resource Planning (ERP) systems

## Advanced CDC strategies

Leverage advanced CDC techniques in Workato to improve control, efficiency, and performance when you manage data changes. These strategies help optimize how you capture, process, and sync data across systems.

- Use filters and conditional triggers
  
- Apply filters and conditional triggers to control which data changes are captured and propagated to downstream systems. This granular control ensures you process only relevant changes, which reduces unnecessary data movement.
  
- Process large data volumes efficiently
  
- Use batch processing and micro-batching to manage large volumes of data changes. These methods help maintain synchronization and minimize performance bottlenecks.
  
- Optimize performance
  
- Improve performance with features such as built-in cursor management to track high watermarks, auto-deduplication to prevent duplicate records, and in-order processing to maintain data integrity.
  
- Adjust pipeline speeds to fit business needs
  
- Set up variable-speed data pipelines to match your business requirements. Workato supports near-real-time streaming, frequent micro-batches for fast polling, and periodic batch schedules for bulk updates.

---
