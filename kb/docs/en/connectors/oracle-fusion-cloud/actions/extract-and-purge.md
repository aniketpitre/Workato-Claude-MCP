---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/extract-and-purge.md
description: >-
  The Extract and purge action extracts data from Oracle Fusion Cloud and
  removes the extracted records from the source system.
---

# Oracle Fusion Cloud - Extract and purge action

The **Extract and purge** action extracts data from Oracle Fusion Cloud and removes the extracted records from the source system. This action uploads load and import job output to the Universal Content Management (UCM) server and purges interface tables with callback and notification support.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Request IDs | Provide the request IDs of load job and import jobs. |
| Notification code | Enter a [two-digit number](https://docs.oracle.com/en/cloud/saas/financials/25c/oeswf/erpintegrationservice-d16510e420.html#extractAndPurge) to define when to send a bell or email notification. |
| Callback URL | Provide the web service based callback URL of the web service that has been implemented to receive the ESS job status upon job completion. Pass `#NULL` if web service based callback isn't needed. |
| Job options | Specify processing parameters as key-value pairs separated by commas to control extract-and-purge variations. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request ID of the first submitted Enterprise Scheduling Service job. |
