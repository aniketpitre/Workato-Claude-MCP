---
url: 'https://docs.workato.com/en/connectors/workato-edi/search-records.md'
description: >-
  Use the search records action (batch) to search for transactions or
  relationships in Orderful.
---

# Workato EDI - Search records action (batch)

Use the **Search records** action (batch) to search for transactions or relationships in Orderful.

## Input

The input fields are dynamic and depend on the object you select.

### Transaction object input fields

| Input field | Description |
| --- | --- |
| Object | Use the **Object** drop-down to select the type of record to search for. Available options include `Transaction` and `Relationship`. The remaining input fields change based on your selection. |
| Business number | Enter the business number associated with a transaction. Filters the results to transactions with a matching business number. |
| Transaction type | Enter the transaction type, such as `RAW_ORDER` or `850_PURCHASE_ORDER`. Filters the results to transactions of the matching type. Refer to Orderful's documentation for the list of [available transaction types](https://docs.orderful.com/reference/available-transaction-types). |
| Created from | Enter the earliest creation timestamp to include. Filters the results to transactions created on or after this timestamp. |
| Created to | Enter the latest creation timestamp to include. Filters the results to transactions created on or before this timestamp. Use together with **Created from** to filter by date range. |
| Validation status | Enter a validation status, such as `VALID` or `INVALID`. Filters the results to transactions with a matching validation status. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Delivery status | Enter a delivery status, such as `SENT` or `DELIVERED`. Filters the results to transactions with a matching delivery status. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Acknowledgment status | Enter an acknowledgment status, such as `ACCEPTED` or `REJECTED`. Filters the results to transactions with a matching acknowledgment status. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Sender interchange control header (ISA) ID | Enter the sender's ISA ID. Filters the results to transactions from a matching sender. |
| Receiver interchange control header (ISA) ID | Enter the receiver's ISA ID. Filters the results to transactions to a matching receiver. |
| Reference identifier | Enter a reference identifier for filtering or lookup. |
| Previous cursor | Provide the pagination token returned as `Previous cursor` in a previous response. Use to retrieve the previous page of results. |
| Next cursor | Provide the pagination token returned as `Next cursor` in a previous response. Use to retrieve the next page of results. |
| Stream | Enter a stream to filter by, such as `TEST` or `LIVE`. Filters the results to transactions in the matching stream. |
| Sender interchange reference identifier | Enter the sender's interchange reference identifier. |
| Sender group reference identifier | Enter the sender's group reference identifier. |
| Sender transaction reference identifier | Enter the sender's transaction reference identifier. |
| Receiver interchange reference identifier | Enter the receiver's interchange reference identifier. |
| Receiver group reference identifier | Enter the receiver's group reference identifier. |
| Receiver transaction reference identifier | Enter the receiver's transaction reference identifier. |

### Relationship object input

| Input field | Description |
| --- | --- |
| Object | Use the **Object** drop-down to select the type of record to search for. Available options include `Transaction` and `Relationship`. The remaining input fields change based on your selection. |
| Limit | Enter the maximum number of relationships to return in one response. |
| Previous cursor | Provide the pagination token returned as `Previous cursor` in a previous response. Use to retrieve the previous page of results. |
| Next cursor | Provide the pagination token returned as `Next cursor` in a previous response. Use to retrieve the next page of results. |
| Auto send | Filter the results by whether automatic sending is enabled for the relationship. Available options are `Enabled` and `Disabled`. |

## Output

### Transaction object output

| Output field | Description |
| --- | --- |
| Transactions | List of transactions that meet your search criteria. |
| Transaction ID | Unique identifier of the transaction. |
| URL | API endpoint URL for the transaction resource. |
| Version | API version used. For example, `v3`. |
| Sender | Object containing details about the sender trading partner. |
| Interchange control header (ISA) ID (Sender) | Sender’s interchange control header ID. |
| Interchange control header (ISA) ID qualifier (Sender) | Qualifier for the sender’s interchange control header ID. |
| Test Interchange control header (ISA) ID (Sender) | Test sender interchange control header ID. |
| Test Interchange control header (ISA) ID qualifier (Sender) | Qualifier for the test sender’s interchange control header ID. |
| Name (Sender) | Name of the sender trading partner. |
| Receiver | Object containing details about the receiver trading partner. |
| Interchange control header (ISA) ID (Receiver) | Receiver’s interchange control header ID. |
| Interchange control header (ISA) ID qualifier (Receiver) | Qualifier for the receiver’s interchange control header ID. |
| Test Interchange control header (ISA) ID (Receiver) | Test receiver interchange control header ID. |
| Test Interchange control header (ISA) ID qualifier (Receiver) | Qualifier for the test receiver’s interchange control header ID. |
| Name (Receiver) | Name of the receiver trading partner. |
| Type | Object describing the transaction type. |
| Name (Type) | Transaction type, such as `850_PURCHASE_ORDER` or `RAW_ORDER`. Refer to Orderful's documentation for more information about [available transaction types](https://docs.orderful.com/reference/available-transaction-types). |
| Stream | Indicates whether the transaction was sent to a production or test communication channel. Returns `TEST` for test communication channels and `LIVE` for production communication channels. |
| Business number | Business number associated with the transaction. |
| Reference identifiers | List of reference identifiers tied to the transaction. |
| Value (Reference identifiers) | The control number value captured from the EDI envelope. |
| Type (Reference identifiers) | The EDI envelope header the control number came from. Returns `INTERCHANGE`, `GROUP`, or `TRANSACTION`. |
| Owner (Reference identifiers) | The party that owns the reference identifier. Returns `SENDER` or `RECEIVER`. |
| Validation status | Status of EDI validation, such as `VALID` or `INVALID`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Delivery status | Status of delivery to the trading partner, such as `SENT`, `DELIVERED`, or `FAILED`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Acknowledgment status | Status of acknowledgment, such as `ACCEPTED`, `REJECTED`, or `NOT_ACKNOWLEDGED`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Acknowledgment | Object containing a link to the acknowledgment. |
| URL (Acknowledgment) | API endpoint URL for the transaction acknowledgment. |
| Created at | Timestamp when the transaction was created. |
| Last updated at | Timestamp when the transaction was last updated. |
| Message | Object containing a link to the transaction message. Also contains a nested `Download` object for **Any File** transactions. |
| URL (Message) | API endpoint URL for the transaction message. |
| Download (Message) | Object containing download details for the transaction file. Populated for **Any File** transactions. |
| Download URL (Download) | The download URL of the transaction file. Map the Download URL datapill into the [Download transaction file](/en/connectors/workato-edi/download-transaction-file) action to retrieve the file contents. The URL expires 24 hours after retrieval. |
| Pagination | Object containing the cursors that page through the full result set. |
| Previous cursor (Pagination) | Cursor token for the previous page of results. Pass this value into the **Previous cursor** input field on a subsequent run to retrieve the previous page. Returns `null` when there is no previous page. |
| Next cursor (Pagination) | Cursor token for the next page of results. Pass this value into the **Next cursor** input field on a subsequent run to retrieve the next page. |

### Relationship object output

| Output field | Description |
| --- | --- |
| Relationships | List of relationships that match your search criteria. |
| Relationship ID | Unique identifier of the relationship. |
| Created at | Timestamp when the relationship was created. |
| Updated at | Timestamp when the relationship was last updated. |
| Sender | Object containing details about the sender trading partner. |
| EDI account ID (Sender) | The sender’s EDI account ID. |
| Live Interchange control header (ISA) ID (Sender) | The live ISA ID for the sender. |
| Test Interchange control header (ISA) ID (Sender) | The test ISA ID for the sender. |
| Receiver | Object containing details about the receiver trading partner. |
| EDI account ID (Receiver) | The receiver’s EDI account ID. |
| Live Interchange control header (ISA) ID (Receiver) | The live ISA ID for the receiver. |
| Test Interchange control header (ISA) ID (Receiver) | The test ISA ID for the receiver. |
| Transaction type | Object describing the transaction type. |
| Name (Transaction type) | The transaction type, such as `850_PURCHASE_ORDER` or `RAW_WAREHOUSE_TRANSFER`. |
| Status | The current status of the relationship, such as `READY`. |
| Auto send | Indicates whether automatic sending is enabled for transactions. Returns `ENABLED` or `DISABLED`. |
| Pagination | Object containing the cursors that page through the full result set. |
| Previous cursor (Pagination) | Cursor token for the previous page of results. Pass this value into the **Previous cursor** input field on a subsequent run to retrieve the previous page. Returns `null` when there is no previous page. |
| Next cursor (Pagination) | Cursor token for the next page of results. Pass this value into the **Next cursor** input field on a subsequent run to retrieve the next page. |

---
