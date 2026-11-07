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
