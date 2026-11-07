---
url: 'https://docs.workato.com/en/connectors/pgp-by-workato/sign-message-action.md'
description: >-
  This action signs data using the private key and passphrase from the
  connection.
---

# PGP tools by Workato - Sign a message action

The **Sign a message** action signs text or file content using the private key and passphrase provided in the connection. You can also sign a message as part of the **Encrypt data** action.

## Input

| Input field | Description |
| --- | --- |
| File content | Provide the content to sign. Map a File content datapill or enter plain text directly. |
| ASCII armor | Optional. Select **Yes** to generate the signature as ASCII characters. Use this for standard text formats such as email or messaging. |

## Output

| Output field | Description |
| --- | --- |
| PGP signature | The signed message. |

---
