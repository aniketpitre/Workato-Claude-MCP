---
url: 'https://docs.workato.com/en/wel/stdlib/binary.md'
description: >-
  WEL binary functions for base64, hex, and quoted-printable conversion,
  measuring byte length, and slicing raw byte data from files and digests.
---

# Binary functions

`Binary` is the WEL type for raw bytes. It appears when you handle file content, when a crypto function returns a digest, and when a system sends data base64-encoded inside a JSON field.

Binary functions convert bytes to JSON-safe text representations. They also measure and slice raw bytes.

> **BYTES AREN'T TEXT**
> 
> `Binary` and `String` are different types, and WEL won't convert between them implicitly. `String()` rejects a `Binary` outright.
> 
> Specify which character encoding the bytes are in to convert them to readable text, using [decode\_string](/en/wel/stdlib/encoding). Use `encode_base64` or `encode_hex_string` to go from bytes to text that is safe to put in a JSON field.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Base64

Base64 is the standard way to embed raw bytes in a JSON field or a URL.

### `encode_base64`

Encodes bytes as a base64 string.

```text
encode_base64(binary, mode)
```

| Parameter | Description |
| --- | --- |
| binary | The bytes to encode. |
| mode | Optional. `'url'` for URL-safe output, `'no_pad'` to omit padding, `'url_no_pad'` for both. |

Encode bytes as base64

The following example encodes bytes as a base64 string:

**Formula**

```text
encode_base64(Binary('ABC'))
```

**Output**

```text
QUJD
```

> **USE URL MODE FOR TOKENS IN A URL**
> 
> Standard base64 contains `+` and `/`, which can have special meaning in URLs and filenames. The `'url'` mode replaces them with `-` and `_`. Use this mode for tokens in query strings or URL paths.

### `decode_base64`

Decodes a base64 string to bytes. Tolerates missing padding.

```text
decode_base64(text, mode)
```

| Parameter | Description |
| --- | --- |
| text | The base64 string to decode. |
| mode | Optional. `'url'` for URL-safe input. |

Decode a base64 string to bytes

The following example decodes a base64 string to bytes:

**Formula**

```text
decode_base64('QUJD')
```

**Output**

```text
0x"414243"
```

## Hexadecimal

Hex represents each byte as two characters, trading size for human readability.

### `encode_hex_string`

Converts bytes to a hexadecimal string, two characters per byte.

Hex requires more space than base64 but provides a human-readable representation. Checksums and digests commonly use this format.

```text
encode_hex_string(binary, mode)
```

| Parameter | Description |
| --- | --- |
| binary | The bytes to encode. |
| mode | Optional. `'upper'` for uppercase output. |

Encode bytes as a hex string

The following example encodes bytes as a hexadecimal string:

**Formula**

```text
encode_hex_string(Binary('ABC'))
```

**Output**

```text
414243
```

### `decode_hex_string`

Converts a hexadecimal string to bytes. Strips a leading `0x` or a trailing `h` unless the mode is `'strict'`.

```text
decode_hex_string(text, mode)
```

| Parameter | Description |
| --- | --- |
| text | The hex string to decode. |
| mode | Optional. `'strict'` to reject prefixes and suffixes. |

Decode a hex string to bytes

The following example decodes a hexadecimal string to bytes:

**Formula**

```text
decode_hex_string('414243')
```

**Output**

```text
0x"414243"
```

## Quoted-printable

Quoted-printable is a MIME encoding for mostly-ASCII text, such as an email body.

### `encode_quoted_printable`

Encodes bytes as MIME quoted-printable, as defined in RFC 2045, with 76-column soft line breaks.

Email bodies use quoted-printable when the content consists mostly of ASCII and readability matters more than compactness.

```text
encode_quoted_printable(binary)
```

| Parameter | Description |
| --- | --- |
| binary | The bytes to encode. |

Encode bytes as quoted-printable

The following example encodes bytes containing an equals sign as quoted-printable:

**Formula**

```text
encode_quoted_printable(Binary('a=b'))
```

**Output**

```text
a=3Db
```

### `decode_quoted_printable`

Decodes MIME quoted-printable text to bytes.

```text
decode_quoted_printable(text)
```

| Parameter | Description |
| --- | --- |
| text | The quoted-printable string to decode. |

Decode a quoted-printable string to bytes

The following example decodes a quoted-printable string back to bytes:

**Formula**

```text
decode_quoted_printable('a=3Db')
```

**Output**

```text
0x"613D62"
```

## Measure and slice

The following functions measure and extract raw byte ranges directly, without any text interpretation:

### `byte_length`

Returns the number of bytes.

`byte_length` returns a byte count, not a character count. `length` counts code points in text, and [grapheme\_length](/en/wel/stdlib/unicode#grapheme-length) counts user-perceived characters (grapheme clusters) instead. The three can differ for anything outside ASCII.

```text
byte_length(binary)
```

| Parameter | Description |
| --- | --- |
| binary | The bytes to measure. |

Measure the byte length of a string

The following example measures the byte length of an ASCII string:

**Formula**

```text
byte_length(Binary('ABC'))
```

**Output**

```text
3
```

### `byte_slice`

Extracts a run of bytes by offset and length.

```text
byte_slice(binary, offset, length)
```

| Parameter | Description |
| --- | --- |
| binary | The bytes to slice. |
| offset | Zero-based starting byte. |
| length | How many bytes to take. |

Extract a range of bytes

The following example extracts 3 bytes starting at offset 1:

**Formula**

```text
byte_slice(Binary('ABCDEF'), 1, 3)
```

**Output**

```text
0x"424344"
```

> **SLICING BYTES CAN SPLIT A CHARACTER**
> 
> A non-ASCII character can occupy multiple bytes in UTF-8. A byte slice can split one of these characters and produce an invalid byte sequence.
> 
> Slice it as text with [substring](/en/wel/stdlib/string) or [grapheme\_substring](/en/wel/stdlib/unicode) when the data is text.

### Use case: Attach a file and record its checksum

A destination expects base64-encoded file content in a JSON field and a SHA-256 checksum in hexadecimal format. Use binary functions to encode the file and compute the checksum:

**Input**

```json
{
  "filename": "note.txt",
  "content": "ABC"
}
```

**Formula**

```text
let bytes = Binary(_.content)
do {
  filename: _.filename,
  size_bytes: byte_length(bytes),
  content_base64: encode_base64(bytes),
  sha256: hex_sha256(bytes)
}
```

**Output**

```json
{
  "filename": "note.txt",
  "size_bytes": 3,
  "content_base64": "QUJD",
  "sha256": "b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78"
}
```

`let … do` converts the content to bytes once, and the three derived fields all read the same value.

## Related

- [Encoding functions](/en/wel/stdlib/encoding): Turn bytes into text with a named character encoding.
- [Crypto functions](/en/wel/stdlib/crypto): Produce digests and HMAC values, which return `Binary`.
- [Random functions](/en/wel/stdlib/random): Generate `random_bytes` for salts.
- [Data types](/en/wel/language/data-types): More information about the `Binary` type.

---
