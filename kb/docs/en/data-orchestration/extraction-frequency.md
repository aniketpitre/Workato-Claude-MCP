---
url: 'https://docs.workato.com/en/data-orchestration/extraction-frequency.md'
description: >-
  Set up how often Workato extracts data from source systems using batch, bulk,
  real-time, or micro-batch polling processing methods.
---

# Set up extraction frequency

Define how often Workato extracts data from your source systems. Workato supports the following methods for data processing:

- [Batch](/en/recipes/triggers#batch-triggers)
  
- Extracts and processes data in groups of multiple records or rows. You can use batch processing to move large volumes of data efficiently during scheduled transfers.
  
- [Bulk](/en/recipes/triggers#bulk-triggers)
  
- Extracts larger datasets than batch processing, maximizing throughput and efficiency. You can use bulk processing for full data loads or large-scale migrations.
  
- [Real-time](/en/recipes/triggers#real-time-triggers)
  
- Extracts and processes data immediately as it becomes available. You can use real-time extraction when you need instant data access, such as for monitoring, alerting, or live dashboards.
  
- [Micro-batch/polling](/en/recipes/triggers#polling-triggers)
  
- Checks for new data at regular intervals and processes small sets of records. You can use micro-batch or polling to balance timely data updates with reduced system load.

---
