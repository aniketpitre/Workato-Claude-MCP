---
url: 'https://docs.workato.com/en/connectors/workato-edi/create-record.md'
description: >-
  Use the create record action to create a record in Orderful, such as a
  transaction or acknowledgment.
---

# Workato EDI - Create record action

Use the **Create record** action to create a record in Orderful, such as a `Transaction` or `Acknowledgment`.

> **SUPPORTED TRANSACTION FORMATS**
> 
> The **Create record** action supports creating transactions in both X12 and JSON formats. However, it supports creating an acknowledgment for JSON transactions only.
> 
> Acknowledgments for X12 transactions should be sent as 997 Functional Acknowledgments by the backend system that ingests the X12 file.
> 
> Orderful is configured to automatically acknowledge transactions by default, though this setting can be modified at the account and relationship level. You do not need to create an acknowledgment using the **Create record** action when automatic acknowledgments are enabled.
> 
> Refer to Orderful's documentation for more information about [acknowledging a transaction](https://docs.orderful.com/docs/acknowledge-a-transaction).

## Input

| Input field | Description |
| --- | --- |
| Object | Use the **Object** drop-down to select the record you plan to create. Available options include `Transaction` and `Acknowledgment`. You must be the recipient of a `Transaction` to create an `Acknowledgment`. |
| Transaction type | Object containing the transaction type details. Available when you select `Transaction` as the object to create. |
| Name (Transaction type) | Select a transaction type from the list of available EDI transaction types. Refer to Orderful's documentation for more information about [available transaction types](https://docs.orderful.com/reference/available-transaction-types). |
| Stream | Specify the stream that the transaction belongs to. Select `TEST` for your testing environment or `LIVE` for your production environment. Available when you select `Transaction` as the object to create. |
| Sender | Object containing sender details. Available when you select `Transaction` as the object to create. |
| Interchange control header (ISA ID) (Sender) | Select an ISA ID from your organization's EDI accounts. |
| Receiver | Object containing receiver details. Available when you select `Transaction` as the object to create. |
| Interchange control header (ISA ID) (Receiver) | Enter the trading partner's ISA ID. This identifies the organization you're sending the EDI transaction to. |
| Message | Provide the transaction document using the structure defined by the transaction type. Must be provided in JSON format. Available when you select `Transaction` as the object to create. |
| Transaction ID | Provide the ID of the transaction to acknowledge. Available when you select `Acknowledgment` as the object to create. |
| Status | Select an acknowledgment status: `Accepted` or `Rejected`. Available when you select `Acknowledgment` as the object to create. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Errors | Object containing error details for the acknowledgment. Available when you select `Acknowledgment` as the object to create. |
| Errors source list (Errors) | Input a list datapill containing the errors to include with the acknowledgment. |
| Path (Errors) | Input the error path, such as `message`. |
| Code (Errors) | Input the error code. |
| Message (Errors) | Input the error message. |

## Output

The output for this action is dynamic and depends on the object created in Orderful.

### Transaction object output

| Output field | Description |
| --- | --- |
| Transaction ID | Unique identifier of the transaction. |

### Acknowledgment object output

| Output field | Description |
| --- | --- |
| Status | Indicates whether the acknowledgment was created successfully. |

---

---
url: >-
  https://docs.workato.com/en/connectors/workato-edi/download-transaction-file.md
description: >-
  Use the Download transaction file action to download file content from an Any
  File transaction's download URL.
---

# Workato EDI - Download transaction file action

Use the **Download transaction file** action to download the file content of an **Any File** transaction from Orderful. **Any File** transactions contain arbitrary file payloads that fall outside standard EDI message formats, such as XML or flat positional files with custom structure and syntax.

Use this action with the **New transactions in polling bucket** trigger or the **Get record** action, both of which provide a download URL for each **Any File** transaction they return. After the file is downloaded, pass the File contents datapill to a downstream connector to parse or process the payload, such as [XML Tools by Workato](/en/connectors/xml-tools-workato) to parse an XML file.

Refer to Orderful's documentation for more information about [standard EDI vs. **Any File** transactions](https://docs.orderful.com/docs/standard-edi-vs-any-file).

> **DOWNLOAD URL EXPIRATION**
> 
> Orderful download URLs expires 24 hours after the transaction is first retrieved. Place this action in the same recipe as the trigger or **Get record** action that produced the URL, and download the file within 24 hours. Re-run the trigger or **Get record** action to refresh an expired URL.

## Input

| Input field | Description |
| --- | --- |
| URL | Provide the download URL of the transaction file. Map the Download URL datapill from the [New transactions in polling bucket](/en/connectors/workato-edi/new-transactions-bucket-trigger) trigger or the [Get record](/en/connectors/workato-edi/get-record) action into this field. |

## Output

| Output field | Description |
| --- | --- |
| File contents | The file contents retrieved from the transaction's download URL. |
| Size | The size of the downloaded file, in bytes. |

---
