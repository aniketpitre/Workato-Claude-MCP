---
url: 'https://docs.workato.com/en/connectors/veeva-vault/run-vql-query-action.md'
description: >-
  The Run VQL query action submits a raw Vault Query Language (VQL) query
  against documents, objects, or system tables in Veeva Vault.
---

# Veeva Vault - Run VQL query action

The **Run VQL query** action submits a raw Vault Query Language (VQL) query against documents, objects, or system tables in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| VQL query | Enter the VQL query to run. |
| Include query describe metadata | Select `Yes` or `No` to set the `X-VaultAPI-DescribeQuery: true` header on the request. Defaults to `No`. |
| Record properties | Select `All`, `Hidden`, `Redacted`, or `Weblink` to indicate how to apply the `X-VaultAPI-RecordProperties` header. Omit to skip the header. |
| Record schema | Optional. Enter the schema for the records returned by the query. Define fields to expose them as typed datapills downstream. Leave blank to return the records as raw JSON objects. |

## Output

| Output field | Description |
| --- | --- |
| Total | The total number of records matching the query. |
| Size | The number of records returned. |
| Page size | The page size used for this query. |
| Page offset | The page offset used for this query. |
| Next page | The URL to fetch the next page of results, if any. |
| Previous page | The URL to fetch the previous page of results, if any. |
| Records | An array of records. If you defined a **Record schema**, each record has the fields you defined. Otherwise, each record is returned as raw JSON. |

---

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

---
