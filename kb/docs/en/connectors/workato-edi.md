---
url: 'https://docs.workato.com/en/connectors/workato-edi.md'
description: >-
  The Workato EDI connector, powered by Orderful, enables you to automate EDI
  workflows, exchanging purchase orders, invoices, and shipment notices.
---

# Workato EDI connector

The Workato EDI connector, powered by Orderful, enables seamless and automated Electronic Data Interchange (EDI) between businesses and their trading partners using Orderful’s modern cloud EDI platform. Use this connector to exchange critical business documents, such as purchase orders, invoices, and shipment notices in standardized EDI formats within Workato’s low-code automation environment.

> **WORKING WITH THE WORKATO EDI CONNECTOR**
> 
> The Workato EDI connector includes a **New transactions in polling bucket** trigger, which monitors a polling bucket for new transactions in Orderful. This trigger automatically approves delivery for each transaction it retrieves and clears your bucket right after retrieval to avoid data duplication. Note that the `Delivery status` of retrieved transactions shows as `Sent` rather than `Delivered`. This is because the status is captured at the moment of retrieval before the approval completes.

## API version

The Workato EDI connector uses the [Orderful API v3](https://docs.orderful.com/v3.0/reference/overview).

## Supported data formats

The Workato EDI connector supports the following formats:

- **EDIFACT**
- **X12**
- **Any File** (custom EDI). Send and receive files in formats other than standard EDI, such as custom JSON, XML, CSV, PDF, and JPEG. Use the [Send transaction file](/en/connectors/workato-edi/send-transaction-file) and [Download transaction file](/en/connectors/workato-edi/download-transaction-file) actions. Refer to the Orderful [EDI vs Any File](https://docs.orderful.com/docs/standard-edi-vs-any-file) documentation for more information.

> **JSON REPRESENTATION**
> 
> Workato represents EDIFACT and X12 transactions as JSON. Transaction data uses JSON structure rather than raw EDI segments in recipes.

## How to connect to the Workato EDI connector

Complete the following steps to establish a connection to Workato EDI in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Workato EDI** as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Create connection](/assets/connection-setup.D2MVKvhA.png)_Create your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Data center** drop-down menu to select the data center for your Workato EDI account. Defaults to **US**.
   
6. Enter your Orderful **API key**.
   
   You can retrieve your API key from Orderful in **Settings > API Credentials**.
   
7. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/workato-edi/new-transactions-bucket-trigger.md
description: >-
  Use the New transactions in polling bucket trigger to monitor a polling bucket
  for new transactions in Orderful.
---

# Workato EDI - New transactions in polling bucket trigger

The **New transactions in polling bucket** trigger monitors a polling bucket you specify for new transactions in Orderful. This trigger automatically approves delivery for each transaction it retrieves and clears your bucket immediately after retrieval to avoid data duplication. The `Delivery status` of retrieved transactions shows as `Sent` rather than `Delivered`. This is because the status is captured at the moment of retrieval before the approval completes.

> **ANY FILE TRANSACTIONS**
> 
> **Any File** transactions include a nested `Download` object with a `Download URL` datapill in the `Message` object output. Map this datapill into the [Download transaction file](/en/connectors/workato-edi/download-transaction-file) action to retrieve the file contents.
> 
> Refer to the Orderful documentation for more information about [**Any File** transactions](https://docs.orderful.com/docs/inbound-mft-receive-any-file).

> **TRANSACTION SIZE LIMIT**
> 
> This trigger skips transactions larger than 50 MB. Their `Delivery status` stays `Sent` instead of updating to `Delivered`, and each skipped transaction counts against the trigger's configured batch size without appearing in the output.
> 
> Transactions this large are extremely rare in practice. If one occurs, handle it manually in Orderful and Workato.

## Input

| Input field | Description |
| --- | --- |
| Bucket ID | Provide the ID of the polling bucket you plan to monitor for new transactions. To retrieve the polling bucket ID, sign in to Orderful, go to **Communication Channels**, select a communication channel, and locate the **Retrieval URL**. The polling bucket ID is the last sequence of digits in the URL. For example, if your channel's retrieval URL is `https://api.orderful.com/v3/polling-buckets/12345`, the bucket ID is `12345`. |
| Trigger poll interval | Determine how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Batch size | Specify the number of transactions to retrieve per batch. Accepts values from `1` to `100`. Defaults to `100` if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Transaction ID | Unique identifier of the transaction. |
| URL | The full API endpoint URL for the transaction resource. |
| Version | API version used. For example, `v3`. |
| Sender | Object containing details about the sender trading partner. |
| Interchange control header (ISA) ID (Sender) | Sender’s interchange control header ID. |
| Interchange control header (ISA) ID qualifier (Sender) | Qualifier for the sender’s interchange control header ID. |
| Test Interchange control header (ISA) ID (Sender) | Test sender interchange control header ID. |
| Test Interchange control header (ISA) ID qualifier (Sender) | Qualifier for the test sender’s interchange control header ID. |
| Receiver | Object containing details about the receiver trading partner. |
| Name (Sender) | Name of the sender trading partner. |
| Interchange control header (ISA) ID (Receiver) | Receiver’s interchange control header ID. |
| Interchange control header (ISA) ID qualifier (Receiver) | Qualifier for the receiver’s interchange control header ID. |
| Test Interchange control header (ISA) ID (Receiver) | Test receiver interchange control header ID. |
| Test Interchange control header (ISA) ID qualifier (Receiver) | Qualifier for the test receiver’s interchange control header ID. |
| Name (Receiver) | Name of the receiver trading partner. |
| Type | Object describing the transaction type. |
| Name (Type) | Transaction type, such as `850_PURCHASE_ORDER`. Refer to Orderful's documentation for more information about [available transaction types](https://docs.orderful.com/reference/available-transaction-types). |
| Stream | Indicates whether the transaction was sent to a production or test communication channel. Returns `TEST` for test communication channels and `LIVE` for production communication channels. |
| Business number | The primary business document identifier for the transaction. The value varies by transaction type. For example, this is the same value as the purchase order number for an 850 or an invoice number for an 810. |
| Reference identifiers | Control numbers from the EDI envelope headers (interchange, functional group, and transaction set) that Orderful captures from a processed transaction. |
| Value (Reference identifiers) | The control number value captured from the EDI envelope. |
| Type (Reference identifiers) | The EDI envelope header the control number came from. Returns `INTERCHANGE`, `GROUP`, or `TRANSACTION`. |
| Owner (Reference identifiers) | The party that owns the reference identifier. Returns `SENDER` or `RECEIVER`. |
| Message | Object containing the transaction message details. Also contains a nested `Download` object for **Any File** transactions. |
| URL (Message) | API endpoint URL to retrieve the transaction message. |
| Transaction message (Message) | Standard EDI transactions return the full transaction message of the delivered transaction in JSON. You can map the Transaction message datapill into downstream steps, such as the [Convert data format](/en/connectors/workato-edi/convert-data-format) action to convert data into the original EDI format or use another connector like [JSON Tools by Workato](/en/connectors/json-by-workato) to parse full message granular datapills. **Any File** transactions don't populate this field. Use the Download URL datapill and pass it to the [Download transaction file](/en/connectors/workato-edi/download-transaction-file) action to retrieve the file contents. |
| Download (Message) | Object containing download details for the transaction file. Populated for **Any File** transactions. |
| Download URL (Download) | The download URL of the transaction file. Map the Download URL datapill into the [Download transaction file](/en/connectors/workato-edi/download-transaction-file) action to retrieve the file contents. The URL expires 24 hours after retrieval and refreshes each time the bucket is polled. |
| Validation status | Status of EDI validation, such as `VALID` or `INVALID`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Delivery status | Status of delivery to the trading partner, such as `SENT` or `FAILED`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Acknowledgment status | Status of acknowledgment, such as `ACCEPTED`, `REJECTED`, or `NOT_ACKNOWLEDGED`. Refer to the Orderful [transaction statuses](https://docs.orderful.com/docs/transaction-statuses) documentation for more information. |
| Created at | Timestamp when the transaction was created. |
| Last updated at | Timestamp when the transaction was last updated. |
| Acknowledgment | Object containing acknowledgment details. |
| URL (Acknowledgment) | API endpoint URL for the acknowledgment, if available. |
| Delivery | Object containing delivery details. |
| Delivery ID (Delivery) | Unique identifier of the delivery. |
| URL (Delivery) | API endpoint URL for the delivery. |
| Approve (Delivery) | Object containing the API endpoint URL to approve the delivery. |
| URL (Approve) | API endpoint URL to approve the delivery. |
| Fail (Delivery) | Object containing the API endpoint URL to fail the delivery. |
| URL (Fail) | API endpoint URL to fail the delivery. |

---
