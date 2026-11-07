---
url: 'https://docs.workato.com/en/connectors/workato-edi/send-transaction-file.md'
description: >-
  Use the Send transaction file action to send a file as an Any File transaction
  to a trading partner through Workato EDI.
---

# Workato EDI - Send transaction file action

Use the **Send transaction file** action to send a file as an **Any File** transaction to a trading partner through Workato EDI. **Any File** transactions contain arbitrary file payloads that fall outside standard EDI message formats, such as XML or flat positional files with custom structure and syntax.

Refer to the Orderful [outbound **Any File** transactions](https://docs.orderful.com/docs/outbound-mft-create-and-send-any-file) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| File contents | Use a datapill from an upstream action, such as generating an XML file, to specify the file contents to send as a transaction. You can also paste the contents directly. |
| Content type | Select the content type of the file. Available options include `JSON`, `XML`, `CSV`, `PDF`, and `JPEG`. Alternatively, select **Use custom value** to enter a MIME type string, such as `application/pdf`, `application/xml`, `text/csv`, `application/json`, or `image/jpeg`. |
| Sender ISA ID | Select an ISA ID from your organization's EDI accounts. |
| Receiver ISA ID | Enter the trading partner's ISA ID. This identifies the organization you're sending the transaction to. |
| Transaction type | Select an **Any File** transaction type from the list of available types configured for your Orderful instance. **Any File** transaction types follow the `RAW_*` naming convention, such as `RAW_ORDER` or `RAW_INVOICE`. Refer to the Orderful [**Any File** transaction types](https://docs.orderful.com/reference/available-transaction-types#any-file-transaction-types) documentation for more information. |
| Stream | Specify the stream that the transaction belongs to. Select `TEST` for your testing environment or `LIVE` for your production environment. |
| Business number | A business reference number for the transaction. |

## Output

| Output field | Description |
| --- | --- |
| Transaction ID | Unique identifier of the transaction created in Orderful. |

---
