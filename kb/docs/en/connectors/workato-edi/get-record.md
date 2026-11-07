---
url: 'https://docs.workato.com/en/connectors/workato-edi/get-record.md'
description: >-
  Use the Get record action to retrieve details about a record, such as a
  transaction, transaction message, organization, acknowledgment, or delivery.
---

# Workato EDI - Get record action

Use the **Get record action** to retrieve details about a record you specify, such as a `Transaction`, `Transaction message`, `Organization`, `Acknowledgment`, or `Delivery`.

## Input

| Input field | Description |
| --- | --- |
| Object | Use the **Object** drop-down to select the type of record you plan to retrieve. Available options include `Transaction`, `Transaction message`, `Organization`, `Acknowledgment`, and `Delivery`. |
| Transaction ID | Provide the transaction ID of the record you plan to retrieve. Available when you select the `Transaction`, `Transaction message`, or `Acknowledgment` object. |
| Expand | Specify an object to embed into the response. This field only accepts `message` as input. Available when you select the `Transaction` object. |
| Delivery ID | Provide the delivery ID of the delivery you plan to retrieve. Available when you select the `Delivery` object. |

## Output

The output for this action is dynamic and depends on the object retrieved from Orderful.

### Transaction object output

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
| Name (Sender) | Name of the sender trading partner. |
| Receiver | Object containing details about the receiver trading partner. |
| Interchange control header (ISA) ID (Receiver) | Receiver’s interchange control header ID. |
| Interchange control header (ISA) ID qualifier (Receiver) | Qualifier for the receiver’s interchange control header ID. |
| Test Interchange control header (ISA) ID (Receiver) | Test receiver interchange control header ID. |
| Test Interchange control header (ISA) ID qualifier (Receiver) | Qualifier for the test receiver’s interchange control header ID. |
| Name (Receiver) | Name of the receiver trading partner. |
| Type | Object describing the transaction type. |
| Name (Type) | Transaction type, such as `850_PURCHASE_ORDER`. Refer to Orderful's documentation for more information about [available transaction types](https://docs.orderful.com/reference/available-transaction-types). |
| Stream | Indicates whether the transaction was sent to a production or test communication channel. Returns `TEST` for test communication channels and `LIVE` for production communication channels. |
| Business number | Business number associated with the transaction. |
| Reference identifiers | List of reference identifiers tied to the transaction. |
| Value (Reference identifiers) | The control number value captured from the EDI envelope. |
| Type (Reference identifiers) | The EDI envelope header the control number came from. Returns `INTERCHANGE`, `GROUP`, or `TRANSACTION`. |
| Owner (Reference identifiers) | The party that owns the reference identifier. Returns `SENDER` or `RECEIVER`. |
| Validation status | Status of EDI validation, such as `VALID` or `INVALID`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Delivery status | Status of delivery to the trading partner, such as `SENT` or `FAILED`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Acknowledgment status | Status of the acknowledgment, such as `ACCEPTED`, `REJECTED`, or `NOT_ACKNOWLEDGED`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Acknowledgment | Object containing a link to the acknowledgment. |
| URL (Acknowledgment) | API endpoint URL for the acknowledgment. |
| Created at | Timestamp when the transaction was created. |
| Last updated at | Timestamp when the transaction was last updated. |
| Message | Object containing a link to the transaction message. Also contains a nested `Download` object for **Any File** transactions. |
| URL (Message) | API endpoint URL for the transaction message. |
| Download (Message) | Object containing download details for the transaction file. Populated for **Any File** transactions. |
| Download URL (Download) | The download URL of the transaction file. Map the Download URL datapill into the [Download transaction file](/en/connectors/workato-edi/download-transaction-file) action to retrieve the file contents. The URL expires 24 hours after retrieval. |

### Transaction message object output

| Output field | Description |
| --- | --- |
| Transaction message | Standard EDI transactions return the full transaction message of the delivered transaction in JSON. You can map the Transaction message datapill into downstream steps, such as the [Convert data format](/en/connectors/workato-edi/convert-data-format) action to convert data into the original EDI format or use another connector like [JSON Tools by Workato](/en/connectors/json-by-workato) to parse full message granular datapills. **Any File** transactions that use this field contain the download URL for the transaction file. Map the Transaction message datapill into the [Download transaction file](/en/connectors/workato-edi/download-transaction-file) action to retrieve the file contents. |

### Organization object output

| Output field | Description |
| --- | --- |
| Organization ID | The unique identifier assigned to the organization in Orderful. Used for scoping trading partners, configurations, and transactions. |
| Name | The organization name. |
| EDI accounts | A list of EDI configurations used for trading partner connections. Each account defines its own ISA IDs and connection context. |
| EDI account ID (EDI accounts) | A unique ID for the EDI account within the organization. |
| Name (EDI accounts) | The name of the specific EDI account, usually referencing the trading partner and use case, such as `Buyer` or `Supplier`. |
| Live Interchange control header (ISA) ID (EDI accounts) | The ISA ID used in **production** environments for EDI transactions. Must match the trading partner’s expected value. |
| Test Interchange control header (ISA) ID (EDI accounts) | The ISA ID used in **test** or onboarding environments. Used for validating EDI flows before going live. |

### Acknowledgment object output

| Output field | Description |
| --- | --- |
| URL | The full API endpoint for the acknowledgment resource. |
| Created at | The ISO 8601 timestamp indicating when the acknowledgment was processed by Orderful. |
| Status | The final status of the acknowledgment, such as `ACCEPTED` or `REJECTED`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Transaction | Object containing a reference to the original transaction being acknowledged. |
| URL (Transaction) | API endpoint URL for the original transaction resource. |
| Transaction ID | The unique numeric identifier of the original transaction within Orderful. |

### Delivery object output

| Output field | Description |
| --- | --- |
| Delivery ID | Unique identifier of the delivery. |
| URL | API endpoint URL for the delivery resource. |
| Status | Status of the delivery, such as `SENT` or `FAILED`. Refer to Orderful's documentation for more information about [transaction statuses](https://docs.orderful.com/docs/transaction-statuses). |
| Created at | Timestamp when the delivery was created. |
| Last updated at | Timestamp when the delivery was last updated. |
| Note | Additional notes associated with the delivery, if any. |
| Approve | Object containing the API link to approve the delivery. |
| URL (Approve) | API endpoint URL for approving the delivery. |
| Fail | Object containing the API URL to fail the delivery. |
| URL (Fail) | API endpoint URL for failing the delivery. |
| Send succeeded at | Timestamp when the delivery was successfully sent. |
| Send failed at | Timestamp when the delivery failed to send. |
| Last confirmed at | Timestamp when the delivery was last confirmed. |

---
