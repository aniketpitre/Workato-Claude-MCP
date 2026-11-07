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
