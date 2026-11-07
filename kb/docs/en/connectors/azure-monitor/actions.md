---
url: 'https://docs.workato.com/en/connectors/azure-monitor/actions.md'
description: >-
  Browse the actions supported by the Azure Monitor connector in Workato for
  sending and injecting custom logs into Azure Monitor.
---

# Azure Monitor - Actions

The Azure Monitor connector supports the following actions:

- [Inject custom logs action](/en/connectors/azure-monitor/actions/inject-custom-logs)
- [Send custom log action](/en/connectors/azure-monitor/actions/send-custom-log)

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-monitor/actions/inject-custom-logs.md
description: >-
  The Inject custom logs action sends custom log events to Azure Monitor. It
  allows you to define the structure of your log events and send them to a
  specified Data Collection Rule (DCR) stream.
---

# Azure Monitor - Inject custom logs action

The **Inject custom logs** action sends custom log events to Azure Monitor. It defines the structure of your log events and sends them to a specified Data Collection Rule (DCR) stream.

> **CLIENT CREDENTIALS AUTH REQUIRED**
> 
> This action requires a connection that uses [client credentials authentication](/en/connectors/azure_monitor#client-credentials).

## Input

| Field | Description |
| --- | --- |
| Data collection rule ID | Enter the unique identifier of the Data Collection Rule in your Azure subscription. Learn more about the [configuration of data collection rules](/en/connectors/azure_monitor#register-app-client-creds) |
| Stream name | Enter the name of the stream defined in your Data Collection Rule (DCR). Custom streams use the format `Custom-<TableName>_CL`. For example, if your custom table is `WorkatoLogs_CL`, the stream name is `Custom-WorkatoLogs_CL`. Learn more about [DCR stream configuration](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-structure#input-streams). |
| API version | Select the Azure Monitor Logs API version. Defaults to the latest version. |
| Log schema | Define the structure of each log record. Add fields to match the properties you send. |

## Output

| Field | Description |
| --- | --- |
| Success | Indicates whether the log injection was successful. |

---

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

---
