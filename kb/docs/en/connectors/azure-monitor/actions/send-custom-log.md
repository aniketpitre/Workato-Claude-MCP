---
url: >-
  https://docs.workato.com/en/connectors/azure-monitor/actions/send-custom-log.md
description: >-
  Deprecated action that sends custom logs to Azure Monitor using the HTTP Data
  Collector API. Migrate to the Inject custom logs action.
---

# Azure Monitor - Send custom log action

The **Send custom log** action sends custom logs to Azure Monitor.

> **DEPRECATED - MIGRATION REQUIRED**
> 
> This action uses the [HTTP Data Collector API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api), which will be deprecated on December 8, 2025, and will stop working in September 2026.
> 
> We recommend that you migrate to the [Inject custom logs action](/en/connectors/azure-monitor/actions/inject-custom-logs). It uses the newer [Logs Ingestion API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-ingestion-api-overview) with [client credentials authentication](/en/connectors/azure_monitor#client-credentials).

## Input

| Input field | Description |
| --- | --- |
| Log type | Enter the record type of the submitted data. The log type must contain only letters, numbers, and underscores `_`, and be 100 characters or less. For example, `AzureMonitorTest`. |
| Events | Enter the log event you plan to send to Azure Monitor. Select any GUID record types as strings. You can use JSON or add fields manually. |
| Azure resource ID | Enter the resource ID of the Azure resource associated with the data. This populates the `_ResourceId` property and includes the data in resource-context queries. If this field is blank, the data is excluded from those queries. |

## Output

| Output field | Description |
| --- | --- |
| Status | Indicates if the custom log was sent successfully. |
