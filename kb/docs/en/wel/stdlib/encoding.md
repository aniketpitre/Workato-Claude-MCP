---
url: 'https://docs.workato.com/en/wel/stdlib/encoding.md'
description: >-
  Use WEL encoding functions to convert between text and bytes in a named
  character encoding, check convertibility, and encode MIME email headers.
---

# Encoding functions

Encoding functions convert between text and bytes using a named character encoding, and handle the encoded-word form used in email headers.

These functions matter when a system doesn't speak UTF-8, such as a mainframe export in Shift\_JIS, a legacy CSV in Windows-1252, or an email header carrying an accented name. A wrong encoding produces the garbled text that shows up as `Ã©` where an `é` should be.

> **ENCODING ISN'T ESCAPING**
> 
> Encoding is about which bytes represent a character. [Escaping](/en/wel/stdlib/escape) is about which characters are safe inside a format. An accented name sent to a CSV needs both, and neither substitutes for the other.

## Text to bytes and back

The following functions convert between text and bytes with a specified character encoding:

### `encode_string`

Converts a string to `Binary` using a named encoding.

Use `encode_string` instead of `Binary()` when text can contain non-ASCII characters. `Binary()` raises `E008` for non-ASCII input instead of selecting an encoding.

```text
encode_string(text, encoding)
```

| Parameter | Description |
| --- | --- |
| text | The string to encode. |
| encoding | An encoding name, such as `UTF-8` or `Shift_JIS`. A name suffixed with `-BOM`, such as `UTF-8-BOM`, prepends a byte-order mark. A name suffixed with `-NFC`, `-NFD`, `-NFKC`, or `-NFKD`, such as `UTF-8-NFC`, normalizes the text to that form before encoding. An unrecognized name raises `E206`. A character the target encoding can't represent raises `E227`. |

Encode an accented string as UTF-8

The following example encodes an accented string as UTF-8 bytes:

**Formula**

```text
encode_string('café', 'UTF-8')
```

**Output**

```text
0x"636166C3A9"
```

The `é` occupies two bytes, `C3A9`, so the 4-code-point string `café` encodes to 5 bytes. [length](/en/wel/stdlib/common#length) counts code points, [grapheme\_length](/en/wel/stdlib/unicode#grapheme-length) counts user-perceived characters, and [byte\_length](/en/wel/stdlib/binary#byte-length) counts bytes. The three can differ for anything outside ASCII.

### `decode_string`

Converts `Binary` to a string using a named encoding. This conversion strips leading byte-order marks.

```text
decode_string(binary, encoding, options)
```

| Parameter | Description |
| --- | --- |
| binary | The bytes to decode. Data types other than `Binary` raise `E100`. |
| encoding | The encoding the bytes are in. An unrecognized name raises `E206`. |
| options | Optional map to control how invalid sequences are handled. `invalid`: `'replace'` substitutes a replacement character, or `'skip'` drops them. Other `invalid` values raise `E225`. An unrecognized key in `options` raises `E225`. |

An invalid sequence raises an error by default. Silently replacing bytes instead would turn a data problem into a corrupted record that nobody notices.

Decode UTF-8 bytes back to a string

The following example decodes UTF-8 bytes back to the original string:

**Formula**

```text
decode_string(encode_string('café', 'UTF-8'), 'UTF-8')
```

**Output**

```text
café
```

### `decode_string_by_content_type`

Decodes bytes using the charset named in an HTTP `Content-Type` header, rather than one you supply.

Use it when handling an HTTP response whose encoding you don't control.

```text
decode_string_by_content_type(binary, content_type, options)
```

| Parameter | Description |
| --- | --- |
| binary | The bytes to decode. Data types other than `Binary` raise `E100`. |
| content\_type | The `Content-Type` header value. |
| options | Optional map specifying a `fallback` encoding to use when the header names none. An unrecognized key in `options` raises `E225`. |

## Check before converting

The following functions test whether text or bytes support a specified encoding:

### `ascii_string?`

Returns `true` if the string contains only ASCII characters.

```text
ascii_string?(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |

A plain string is ASCII

The following example tests a plain ASCII string:

**Formula**

```text
ascii_string?('plain')
```

**Output**

```text
true
```

An accented string isn't ASCII

The following example tests a string containing an accented character:

**Formula**

```text
ascii_string?('café')
```

**Output**

```text
false
```

### `convertible_to_encoding?`

Returns `true` if the given encoding can represent the string without losing anything.

Check convertibility before sending text to a system with a restricted character set. It's better to reject a record here than to deliver one with characters silently replaced.

```text
convertible_to_encoding?(text, encoding)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |
| encoding | The target encoding. An unrecognized encoding raises `E206`. |

Test whether an accented string fits ASCII

The following example tests whether an accented string can convert to ASCII without loss:

**Formula**

```text
convertible_to_encoding?('café', 'ASCII')
```

**Output**

```text
false
```

### `valid_string?`

Returns `true` if the bytes are valid in the given encoding and can be decoded.

```text
valid_string?(binary, encoding)
```

| Parameter | Description |
| --- | --- |
| binary | The bytes to test. Data types other than `Binary` raise `E100`. |
| encoding | The encoding to test against. An unrecognized encoding raises `E206`. |

Valid UTF-8 bytes

The following example tests bytes that are valid UTF-8:

**Formula**

```text
valid_string?(Binary('AB'), 'UTF-8')
```

**Output**

```text
true
```

### `encodings`

Lists the encoding types that other encoding functions accept. Encoding names are case-insensitive.

```text
encodings(include_synonyms)
```

| Parameter | Description |
| --- | --- |
| include\_synonyms | Optional boolean flag. Controls whether the response contains accepted synonyms in addition to the canonical names of each encoding type, such as `utf8` as a synonym to `UTF-8`. Defaults to `false`. Non-boolean data types raise `E100`. |

## Email headers

An email header can only carry ASCII. RFC 2047 wraps anything outside that range in encoded-words that look like `=?UTF-8?B?...?=`.

### `encode_mime_header`

Encodes text as RFC 2047 encoded-words for an email header.

```text
encode_mime_header(text, encoding, mode)
```

| Parameter | Description |
| --- | --- |
| text | The header text to encode. |
| encoding | The character encoding to use. An unrecognized encoding raises `E206`. A character the encoding can't represent raises `E227`. |
| mode | Optional encoding mode. Defaults to `'B'` (base64). An unrecognized mode raises `E225`. |

The result splits the output into multiple encoded-words when one word would exceed the 75 character limit RFC 2047 sets for encoded words.

Encode an accented name for a header

The following example encodes an accented string as an RFC 2047 encoded-word:

**Formula**

```text
encode_mime_header('café', 'UTF-8')
```

**Output**

```text
=?UTF-8?B?Y2Fmw6k=?=
```

### `decode_mime_header`

Decodes RFC 2047 encoded-words in an email header back to text. `decode_mime_header` drops whitespace between adjacent encoded-words. Adjacent words can use different charsets.

```text
decode_mime_header(text)
```

| Parameter | Description |
| --- | --- |
| text | The header value to decode. A malformed encoded word raises `E226`. An unrecognized charset raises `E206`. |

Decode an RFC 2047 encoded-word

The following example decodes an RFC 2047 encoded-word back to text:

**Formula**

```text
decode_mime_header('=?UTF-8?B?SGVsbG8=?=')
```

**Output**

```text
Hello
```

### Use case: Prepare a name for a legacy ASCII-only system

The destination exclusively accepts ASCII. Use `convertible_to_encoding?` to check each name before sending, and route the ones that won't fit rather than delivering corrupted text:

**Input**

```json
{
  "names": ["Kalani Park", "Noam Gupta", "José Álvarez"]
}
```

**Formula**

```text
let parts = _.names >> partition_by(n ~> convertible_to_encoding?(n, 'ASCII'))
do {
  send: parts >> at(0),
  needs_review: parts >> at(1)
}
```

**Output**

```json
{
  "send": ["Kalani Park", "Noam Gupta"],
  "needs_review": ["José Álvarez"]
}
```

Check convertibility before transmission so a person can correct the record instead of receiving corrupted text such as `Jos? lvarez`.

## Related

- [Binary functions](/en/wel/stdlib/binary): Base64 and hex, which need no character encoding.
- [Unicode functions](/en/wel/stdlib/unicode): Normalization and grapheme-aware text handling.
- [Escape functions](/en/wel/stdlib/escape): Make a value safe inside another format.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E008`.

---
