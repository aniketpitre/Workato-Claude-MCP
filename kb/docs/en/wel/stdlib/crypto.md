---
url: 'https://docs.workato.com/en/wel/stdlib/crypto.md'
description: >-
  WEL crypto functions for hashing, HMAC signatures, JWT encoding and
  verification, PBKDF2 key derivation, and AES encryption and decryption of
  data.
---

# Crypto functions

Crypto functions cover the cryptography an integration actually needs, such as proving a webhook came from the sender it claims, signing an outbound API request, generating a JWT, or computing a checksum.

> **THESE FUNCTIONS AREN'T A SECURITY DESIGN**
> 
> Crypto functions implement standard algorithms correctly, but they can't make a design secure.
> 
> - **Don't put a secret in an expression**: A key written into a recipe is visible to anyone who can view it and travels with every export. Pass secrets in as input from a secure source.
> - **Hashing isn't encryption**: A hash can't recover the original value. Use hashes for checksums and signatures, not reversible data protection.
> - **A digest of a low-entropy value is guessable**: Hashing an email address doesn't anonymize it, because an attacker can enumerate the whole space.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Choose an algorithm

Use the algorithm that fits your use case:

| Use case | Algorithm |
| --- | --- |
| Verify a webhook signature | `hmac_hex_sha256` |
| Sign an outbound request | `hmac_hex_sha256` |
| Checksum a file | `hex_sha256` |
| Match a partner's legacy scheme | `hex_md5` or `hex_sha1`, only when required |
| Derive a key from a password | `pbkdf2` |
| Issue or check a token | `jwt_encode`, `jwt_decode` |

**MD5 and SHA-1 are broken** for anything security-sensitive. WEL provides them because integrations must sometimes match a partner system that still uses them. Don't choose them for new work.

## Naming convention

Each algorithm comes in two forms, distinguished by a `hex_` prefix:

- `sha256(...)` returns a `Binary` digest: the raw bytes.
- `hex_sha256(...)` returns a `String` of hex characters.

Compare the hex form against a signature header, or put it in a JSON field. Use the `Binary` form when feeding the digest into another function.

## Hashing

All hash functions accept a `String` or a `Binary`.

### `hex_sha256` and `sha256`

SHA-256 is the default choice for new work.

```text
hex_sha256(value)
sha256(value)
```

| Parameter | Description |
| --- | --- |
| value | A `String` or `Binary` to hash. |

Hash a string with SHA-256

The following example hashes a string with SHA-256 and returns the hex digest:

**Formula**

```text
hex_sha256('acme')
```

**Output**

```text
822b33ad87c148a0a20a5ba7cd5ebcaa68d36a18e7aad165554903f52ca82757
```

Measure the byte length of a raw SHA-256 digest

The following example measures the byte length of the raw binary digest:

**Formula**

```text
byte_length(sha256('acme'))
```

**Output**

```text
32
```

### `hex_sha512` and `sha512`

SHA-512 produces a longer digest from the same family.

```text
hex_sha512(value)
sha512(value)
```

| Parameter | Description |
| --- | --- |
| value | A `String` or `Binary` to hash. |

Measure the byte length of a SHA-512 digest

The following example measures the byte length of the raw binary digest:

**Formula**

```text
byte_length(sha512('acme'))
```

**Output**

```text
64
```

### `hex_sha512_256` and `sha512_256`

SHA-512/256 produces a 256-bit digest and avoids the length-extension property of SHA-256.

Use it when hashing a secret and a message. An HMAC handles that case more directly, though, and is usually the better choice.

```text
hex_sha512_256(value)
sha512_256(value)
```

| Parameter | Description |
| --- | --- |
| value | A `String` or `Binary` to hash. |

Hash a string with SHA-512/256

The following example hashes a string with SHA-512/256 and returns the hex digest:

**Formula**

```text
hex_sha512_256('acme')
```

**Output**

```text
2e7a8d79ac01f85db494bfddf90cc808d091543addc18bb68ad643257234735a
```

### `hex_sha1` and `sha1`

SHA-1 is **legacy only**, kept for compatibility with systems that still require it.

```text
hex_sha1(value)
sha1(value)
```

| Parameter | Description |
| --- | --- |
| value | A `String` or `Binary` to hash. |

Hash a string with SHA-1

The following example hashes a string with SHA-1 and returns the hex digest:

**Formula**

```text
hex_sha1('acme')
```

**Output**

```text
293abb6b76d7791c0732cc517d38c4b5c734b87f
```

### `hex_md5` and `md5`

MD5 is **legacy only**, suitable for a non-adversarial checksum and nothing else.

```text
hex_md5(value)
md5(value)
```

| Parameter | Description |
| --- | --- |
| value | A `String` or `Binary` to hash. |

Hash a string with MD5

The following example hashes a string with MD5 and returns the hex digest:

**Formula**

```text
hex_md5('acme')
```

**Output**

```text
53bce4f1dfa0fe8e7ca126f91b35d3a6
```

## HMAC signatures

An HMAC combines a message with a shared secret to produce a signature. Webhook providers commonly use HMAC signatures to verify that requests come from a trusted sender.

Every HMAC function takes the _message first and the key second_.

### `hmac_hex` and `hmac`

Compute an HMAC with the algorithm named as an argument.

```text
hmac_hex(message, key, algorithm)
hmac(message, key, algorithm)
```

| Parameter | Description |
| --- | --- |
| message | The data to sign. |
| key | The shared secret. |
| algorithm | `sha256`, `sha384`, `sha512`, or the legacy `md5` and `sha1`. Case-insensitive. |

Compute an HMAC-SHA256 signature as hex

The following example computes an HMAC-SHA256 signature and returns it as a hex string:

**Formula**

```text
hmac_hex('payload', 'secret', 'sha256')
```

**Output**

```text
b82fcb791acec57859b989b430a826488ce2e479fdf92326bd0a2e8375a42ba4
```

Measure the byte length of a raw HMAC digest

The following example measures the byte length of the raw binary HMAC digest:

**Formula**

```text
byte_length(hmac('payload', 'secret', 'sha256'))
```

**Output**

```text
32
```

### `hmac_algos`

Lists the supported HMAC algorithms.

```text
hmac_algos()
```

List the supported HMAC algorithms

The following example lists the supported HMAC algorithms:

**Formula**

```text
hmac_algos()
```

**Output**

```text
["md5", "sha1", "sha256", "sha384", "sha512"]
```

### `hmac_hex_sha256` and `hmac_sha256`

Most webhook providers use HMAC-SHA256.

```text
hmac_hex_sha256(message, key)
hmac_sha256(message, key)
```

| Parameter | Description |
| --- | --- |
| message | The data to sign. |
| key | The shared secret. |

Compute an HMAC-SHA256 signature

The following example computes an HMAC-SHA256 signature and returns it as a hex string:

**Formula**

```text
hmac_hex_sha256('payload', 'secret')
```

**Output**

```text
b82fcb791acec57859b989b430a826488ce2e479fdf92326bd0a2e8375a42ba4
```

### `hmac_hex_sha384` and `hmac_sha384`

HMAC-SHA384 works like HMAC-SHA256, with a longer digest.

```text
hmac_hex_sha384(message, key)
hmac_sha384(message, key)
```

| Parameter | Description |
| --- | --- |
| message | The data to sign. |
| key | The shared secret. |

Measure the byte length of an HMAC-SHA384 digest

The following example measures the byte length of the raw binary HMAC digest:

**Formula**

```text
byte_length(hmac_sha384('payload', 'secret'))
```

**Output**

```text
48
```

### `hmac_hex_sha512` and `hmac_sha512`

HMAC-SHA512 works like HMAC-SHA256, with an even longer digest than HMAC-SHA384.

```text
hmac_hex_sha512(message, key)
hmac_sha512(message, key)
```

| Parameter | Description |
| --- | --- |
| message | The data to sign. |
| key | The shared secret. |

Measure the byte length of an HMAC-SHA512 digest

The following example measures the byte length of the raw binary HMAC digest:

**Formula**

```text
byte_length(hmac_sha512('payload', 'secret'))
```

**Output**

```text
64
```

### `hmac_hex_sha1` and `hmac_sha1`

HMAC-SHA1 is **legacy only**, kept for compatibility with systems that still require it.

```text
hmac_hex_sha1(message, key)
hmac_sha1(message, key)
```

| Parameter | Description |
| --- | --- |
| message | The data to sign. |
| key | The shared secret. |

Measure the byte length of an HMAC-SHA1 digest

The following example measures the byte length of the raw binary HMAC digest:

**Formula**

```text
byte_length(hmac_sha1('payload', 'secret'))
```

**Output**

```text
20
```

### `hmac_hex_md5` and `hmac_md5`

HMAC-MD5 is **legacy only**, kept for compatibility with systems that still require it.

```text
hmac_hex_md5(message, key)
hmac_md5(message, key)
```

| Parameter | Description |
| --- | --- |
| message | The data to sign. |
| key | The shared secret. |

Measure the byte length of an HMAC-MD5 digest

The following example measures the byte length of the raw binary HMAC digest:

**Formula**

```text
byte_length(hmac_md5('payload', 'secret'))
```

**Output**

```text
16
```

### Use case: Verify an inbound webhook signature

The provider signs the raw body with a shared secret and sends the result in a header. Use `hmac_hex_sha256` to recompute the signature and compare it against the header:

**Input**

```json
{
  "body": "payload",
  "secret": "secret",
  "signature_header": "b82fcb791acec57859b989b430a826488ce2e479fdf92326bd0a2e8375a42ba4"
}
```

**Formula**

```text
{
  expected: hmac_hex_sha256(_.body, _.secret),
  valid: hmac_hex_sha256(_.body, _.secret) == _.signature_header
}
```

**Output**

```json
{
  "expected": "b82fcb791acec57859b989b430a826488ce2e479fdf92326bd0a2e8375a42ba4",
  "valid": true
}
```

Sign the _raw body exactly as received_. Parsing the JSON and re-serializing it changes the bytes, including key order and whitespace. The signature won't match, even though nothing is wrong.

## JSON web tokens

WEL supports HMAC-signed JWTs: `HS256`, `HS384`, and `HS512`.

### `jwt_encode`

Builds and signs a JWT.

```text
jwt_encode(payload, key, algorithm, options)
```

| Parameter | Description |
| --- | --- |
| payload | A `Map` of claims. |
| key | The signing secret. |
| algorithm | `HS256`, `HS384`, or `HS512`. Case-insensitive. |
| options | Optional map of additional header fields. |

Encode and sign a JWT with HS256

The following example builds and signs a JWT with HS256:

**Formula**

```text
jwt_encode({sub: 'user-1'}, '0123456789abcdef0123456789abcdef', 'HS256')
```

**Output**

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyLTEifQ.FKuUN7RwYyegTHXiye1jBlIKzmjIfb39oxKzJk_Gmdo
```

> **HS256 REQUIRES A KEY OF AT LEAST 32 BYTES**
> 
> A shorter key raises `E220` rather than signing with weak material. `HS384` and `HS512` require correspondingly longer keys.
> 
> The length requirement exists because an HMAC is only as strong as its key, and a short one makes the signature easy to forge.

### `jwt_decode`

Decodes a JWT _and verifies its signature_. A token whose signature doesn't match raises an error rather than returning its contents.

```text
jwt_decode(token, key, algorithm, options)
```

| Parameter | Description |
| --- | --- |
| token | The encoded JWT. |
| key | The secret to verify against. |
| algorithm | `HS256`, `HS384`, or `HS512`. |
| options | Optional map of verification settings. |

Decode and verify a JWT

The following example decodes a JWT and verifies its signature:

**Formula**

```text
jwt_decode(jwt_encode({sub: 'user-1'}, '0123456789abcdef0123456789abcdef', 'HS256'), '0123456789abcdef0123456789abcdef', 'HS256')
```

**Output**

```text
{header: {alg: "HS256", typ: "JWT"}, payload: {sub: "user-1"}}
```

> **A JWT IS SIGNED, NOT SECRET**
> 
> Anyone holding the token can read its claims. The payload is only base64-encoded. The signature proves it wasn't altered, not that it wasn't seen. Don't put anything confidential in a JWT payload.

### `jwt_algos`

Lists the supported JWT signing algorithms.

```text
jwt_algos()
```

List the supported JWT algorithms

The following example lists the supported JWT signing algorithms:

**Formula**

```text
jwt_algos()
```

**Output**

```text
["HS256", "HS384", "HS512"]
```

## Key derivation

Key derivation turns a password into a cryptographic key suitable for encryption.

### `pbkdf2`

Derives a key from a password using PBKDF2.

A higher iteration count makes guessing the password more expensive, so use the highest value the destination system permits. Take the salt from [random\_bytes](/en/wel/stdlib/random) rather than writing a fixed one.

```text
pbkdf2(password, salt, iterations, key_length, algorithm)
```

| Parameter | Description |
| --- | --- |
| password | The password or passphrase. |
| salt | A unique salt. |
| iterations | How many rounds. |
| key\_length | Length of the derived key in bytes. |
| algorithm | The underlying hash. For example, `sha256`. Case-insensitive. |

Derive a key from a password with PBKDF2

The following example derives a key from a password and returns it as hexadecimal text. It uses 1000 iterations for demonstration purposes. Production configurations require a substantially higher iteration count.

**Formula**

```text
encode_hex_string(pbkdf2('password', 'salt', 1000, 16, 'sha256'))
```

**Output**

```text
632c2812e46d4604102ba7618e9d6d7d
```

## Encryption

The following functions encrypt and decrypt data with AES in CBC mode:

### `aes_cbc_encrypt`

Encrypts data with AES in CBC mode, applying PKCS7 padding.

```text
aes_cbc_encrypt(data, key, iv)
```

| Parameter | Description |
| --- | --- |
| data | The data to encrypt. |
| key | The encryption key. Its length selects AES-128, AES-192, or AES-256. |
| iv | A 16-byte initialization vector. |

Encrypt data with AES-CBC

The following example encrypts data with AES-CBC and renders the ciphertext as base64:

**Formula**

```text
encode_base64(aes_cbc_encrypt('secret data!!!!!', '0123456789abcdef', 'abcdef0123456789'))
```

**Output**

```text
NsFUgzVrilJO5OF/imH/gbF6NPToZkf1hbVBJkaXXoY=
```

> **A NEW INITIALIZATION VECTOR FOR EVERY MESSAGE**
> 
> Reusing an IV with the same key leaks information about the plaintext. Generate one with `random_bytes(16)` per message and transmit it alongside the ciphertext. The IV can remain public, but it must remain unpredictable and unique.
> 
> CBC doesn't provide authentication and can't detect ciphertext modification. Use an authenticated encryption mode when the destination system supports one. If the destination requires CBC, send an HMAC with the ciphertext.

### `aes_cbc_decrypt`

Decrypts AES-CBC data and removes PKCS7 padding.

```text
aes_cbc_decrypt(data, key, iv)
```

| Parameter | Description |
| --- | --- |
| data | The ciphertext. |
| key | The same key used to encrypt. |
| iv | The same initialization vector used to encrypt. |

Decrypt AES-CBC ciphertext

The following example encrypts data and then decrypts it back to the original text:

**Formula**

```text
decode_string(aes_cbc_decrypt(aes_cbc_encrypt('secret data!!!!!', '0123456789abcdef', 'abcdef0123456789'), '0123456789abcdef', 'abcdef0123456789'), 'UTF-8')
```

**Output**

```text
secret data!!!!!
```

## Related

- [Binary functions](/en/wel/stdlib/binary): More information about `encode_base64`, `encode_hex_string`, and `byte_length`.
- [Random functions](/en/wel/stdlib/random): Generate `random_bytes` for salts and initialization vectors.
- [Encoding functions](/en/wel/stdlib/encoding): Use `decode_string` to turn decrypted bytes back into text.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E220`.

---
