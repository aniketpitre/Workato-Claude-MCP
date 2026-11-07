---
url: 'https://docs.workato.com/en/data-orchestration/large-volume-data-scale.md'
description: >-
  Learn how Workato scales large volume data transfers with batch processing,
  parallel execution, buffering, and data streaming strategies.
---

# Scale for large volume data transfers

Scaling for large volume data transfers ensures efficient processing and handling of substantial amounts of data. Workato offers several features and best practices to accommodate the requirements of organizations dealing with large volumes of data.

## Strategies for handling large datasets in Workato

- Batch processing
  
- Workato supports batch processing capabilities, allowing you to split large datasets into smaller batches for processing. This approach helps prevent resource bottlenecks and improves the stability and performance of data transfers, especially when dealing with large volumes of data.
  
- Parallel execution
  
- Workato allows users to process data tasks in parallel to improve throughput and reduce processing time. By distributing workloads across multiple workers or instances, Workato can handle large volumes of data more efficiently.
  
- Buffering and storage
  
- Workato's buffering capabilities manage the flow of data between systems that operate at different frequencies or volumes. For example, data from HubSpot can be aggregated and buffered, then streamed to Snowflake once a day.
  
- Data streaming
  
- Workato uses streaming mechanisms for scalable and high-speed data transfers. You can also use [FileStorage](/en/features/workato-filestorage) to store output data as files and use them across jobs or different recipes.

---
