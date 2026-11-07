---
url: 'https://docs.workato.com/en/connectors/pgp-by-workato/verify-signed-message.md'
description: This action verifies signed data using a public key.
---

# PGP tools by Workato – Verify a signed message action

The **Verify a signed message** action checks the authenticity of signed content using a public key.

## Input

| Input field | Description |
| --- | --- |
| Signed document | Provide the signed content to verify. Map a File content datapill or enter the signed string directly. |
| Use public key from connection? | Optional. Select **Yes** to use the public key stored in the connection. |
| Verification public key | Provide a public key to verify the signature. This field generates when you set **Use public key from connection?** to **No**. |

## Output

This action doesn't return any output fields.

---
