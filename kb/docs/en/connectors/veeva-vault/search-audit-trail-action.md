---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/search-audit-trail-action.md
description: >-
  The Search audit trail action retrieves audit history records for documents,
  objects, system events, domain events, or login events in Veeva Vault.
---

# Veeva Vault - Search audit trail action

The **Search audit trail** action retrieves audit history records for documents, objects, system events, domain events, or login events in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| Audit trail type | Select the audit trail you plan to query. |
| Start date | Enter the start of the date window. Defaults to the start of the previous day. The window can't exceed 30 days. |
| End date | Enter the end of the date window. Defaults to now. The window can't exceed 30 days from the **Start date**. |
| Events filter | Enter a comma-separated list of event types to return. Only shown for `Document audit trail` and `Object audit trail`. |
| Objects filter | Enter a comma-separated list of object API names you plan to filter by. Only shown for `Object audit trail`. |
| Limit | Enter the number of audit records per page. Defaults to `200`, maximum `1000`. |
| Offset | Enter the number of records to skip. Defaults to `0`. |

## Output

| Output field | Description |
| --- | --- |
| Total | The total number of audit records matching the query. |
| Size | The number of audit records returned. |
| Offset | The offset used for this query. |
| Limit | The quota used for this query. |
| Next page | The URL to fetch the next page of results, if any. |
| Previous page | The URL to fetch the previous page of results, if any. |
| Data | An array of audit records. Fields vary based on the selected **Audit trail type**. Refer to the [Veeva Vault](https://developer.veevavault.com/api/26.1/) documentation for more information. |
