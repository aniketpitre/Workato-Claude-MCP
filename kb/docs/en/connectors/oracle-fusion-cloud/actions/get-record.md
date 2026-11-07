---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/get-record.md
description: The Get record action retrieves a specific record by its internal ID.
---

# Oracle Fusion Cloud - Get record action

The **Get record** action retrieves a specific record by its internal ID. For example, to fetch a product, provide the **Inventory item ID**. The required field appears automatically after the object is selected.

> **MIXED API PROTOCOLS**
> 
> This action includes several SOAP-based objects alongside the standard REST objects:
> 
> - Get ESS job status
> - Get document IDs for file prefix
> - Get document for document ID
> - Get ESS execution details
> - Get default object attribute hints
> - Get service last update time

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object type of the record you plan to retrieve. |
| Object ID | Provide the ID of the record to retrieve. |
| Expand | Select related child and grandchild objects to include. By default, only the record and its child objects return. For example, under **Receivable credit memo**, include **attachments** (grandchild) for each **credit memo line** (child). |

## Output

The output contains details about the retrieved record.
