---
url: 'https://docs.workato.com/en/oem/oem-api/jwt-direct-link-configurations.md'
description: >-
  Reference for the Embedded API endpoint to update the JWT signature
  verification key used for JWT direct linking.
---

# Embedded API - JWT direct link configurations

Use the following endpoint to manage the [JWT direct link configurations](/en/oem/jwt-direct-linking) programmatically.

## Rate limits

The JWT public key resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [JWT public key](/en/oem/oem-api/jwt-direct-link-configurations.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| PUT | [/api/account/signature\_verification\_key](/en/oem/oem-api/jwt-direct-link-configurations#update-jwt-signature-verification-key) | Update JWT signature verification key |

## Update JWT signature verification key

Updates the public key used for verifying the JWT signature. Returns `Embedded Vendor ID`, used for generating the JWT token.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/account/signature_verification_key
```

</api-code>

### Body Parameters

| Name | Type | Description |
| --- | --- | --- |
| key | **string** | The public key in PEM format, using the RS256 algorithm and the [PKCS#1](/en/oem/jwt-direct-linking#prerequisites) or [PKCS#8](/en/oem/jwt-direct-linking#prerequisites) format. Note that the PKCS#1 or PKCS#8 format affects only the private key. The public key you send in the request to Workato is the same. |

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/account/signature_verification_key' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{"key":":key"}'
```

</api-code>

### Response

```json
{
  "vendor_id": "we9898zgsgsgw38394",
  "success": true
}
```

---
