---
url: 'https://docs.workato.com/en/connectors/pgp-by-workato/decrypt-data-action.md'
description: This action decrypts content using a private key and passphrase.
---

# PGP tools by Workato - Decrypt data action

The **Decrypt data** action decrypts encrypted file content using the private key and passphrase provided in the connection.

## Input

| Input field | Description |
| --- | --- |
| Encrypted content | Provide the encrypted content to decrypt. Map a File content datapill or paste the encrypted string directly. |
| Use public key from connection? | Select **Yes** to use the public key from the connection for signature verification. |
| Verification public key | Provide a public key to verify the signature of the encrypted content. This field generates when you set **Use public key from connection?** field to **No**. |
| Ignore MDC error | Select **Yes** to skip MDC (Modification Detection Code) errors when decrypting. |

## Output

| Output field | Description |
| --- | --- |
| Decrypted contents | The decrypted contents of the file. |

---
