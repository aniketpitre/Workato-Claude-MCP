---
url: 'https://docs.workato.com/en/connectors/netsuite-rest/upsert-record-action.md'
description: >-
  The Upsert record action inserts or updates a record in NetSuite based on the
  selected object type and external ID.
---

# NetSuite REST - Upsert record action

The **Upsert record** action inserts or updates a record in NetSuite. This action uses NetSuite REST Web Services to locate a record by its **External ID**, then updates it if found or creates a new one if not.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to upsert. Only supported record types appear in the picklist. |
| External ID | Provide the external ID of the record to upsert. |
| Account | Optional. Enter the account number for this customer if your NetSuite instance uses accounts. |

## Output

Output fields vary depending on the selected record type. For example, if you select **Customer** as the record, the output includes the following fields:

| Output field | Description |
| --- | --- |
| Internal ID | Unique internal identifier for the record in NetSuite. |
| External ID | External identifier used to match the record. |
| Status | Result of the upsert operation. |
| Last modified date | Timestamp of the last update. |

---
