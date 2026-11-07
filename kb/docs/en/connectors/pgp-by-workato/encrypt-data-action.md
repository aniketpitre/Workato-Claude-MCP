---
url: 'https://docs.workato.com/en/connectors/pgp-by-workato/encrypt-data-action.md'
description: This action encrypts data using a public key.
---

# PGP tools by Workato - Encrypt data action

The **Encrypt data** action encrypts text or file content using a public key. Use this action to protect sensitive information before you transfer or store it.

## Input

| Input field | Description |
| --- | --- |
| File content | Provide the content to encrypt. Map a File content datapill or enter plain text directly. |
| Public key | Provide a public key for encryption. Leave blank to use the key set in the connection. |
| Sign | Select **Yes** to sign the content using the private key and passphrase in the connection. You can also sign a message using the **Sign a message** action. |
| File name | Enter the original name of the input file. If left blank, Workato generates a file name automatically. |
| ASCII armor | Select **Yes** to output the encrypted content as ASCII characters. Use this for email or message transfer. |

## Output

| Output field | Description |
| --- | --- |
| Encrypted contents | The encrypted contents of the file. |
| File name | The name of the encrypted file. |

---
