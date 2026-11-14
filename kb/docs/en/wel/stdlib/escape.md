---
url: 'https://docs.workato.com/en/wel/stdlib/escape.md'
description: >-
  Use WEL escape functions to safely embed values in CSV, HTML, XML, JSON,
  JavaScript, URLs, SOQL, OData, and regular expressions without breaking
  syntax.
---

# Escape functions

Escape functions make values safe to embed in specific formats, such as queries, URLs, markup documents, and CSV rows.

> **ESCAPE THE VALUE, NOT THE WHOLE STRING**
> 
> Escape each value before you insert it. Don't escape the completed string. Escaping the completed string can alter valid syntax, while skipping escaping can allow injection.
> 
> ```wel
> f"SELECT Id FROM Account WHERE Name = '{escape_for_soql(_.name)}'"
> ```
> 
> The quotes form part of the query syntax. Escape only the value between them.

## Query languages

Inbound data inserted directly into a query can introduce unintended syntax. The following functions escape values so the query engine treats them as data instead of code.

### `escape_for_soql`

Escapes a value for a SOQL string literal in Salesforce. Escapes `'` and `\`. Doesn't escape `%` and `_` wildcards.

```wel
escape_for_soql(value)
```

| Parameter | Description |
| --- | --- |
| value | The value to escape. Raises `E100` for a `List`, `Map`, or `Binary` value. |

Escape an apostrophe for SOQL

The following example escapes an apostrophe for a SOQL string literal:

**Formula**

```wel
escape_for_soql("O'Brien")
```

**Output**

```text
O\'Brien
```

### `escape_for_odata`

Escapes a value for an OData filter string literal by doubling each single quote. OData expects a doubled quote instead of a backslash escape.

```wel
escape_for_odata(value)
```

| Parameter | Description |
| --- | --- |
| value | The value to escape. |

Escape an apostrophe for OData

The following example escapes an apostrophe for an OData filter string literal:

**Formula**

```wel
escape_for_odata("O'Brien")
```

**Output**

```text
O''Brien
```

### `escape_for_regex`

Escapes regular-expression metacharacters so the pattern matches the string literally. Syntax characters get a preceding backslash, and punctuation becomes a `\xHH` escape.

```wel
escape_for_regex(value)
```

| Parameter | Description |
| --- | --- |
| value | The value to escape. Raises `E100` for a `List`, `Map`, or `Binary` value. |

Escape regex metacharacters

The following example escapes the regex metacharacters in a string:

**Formula**

```wel
escape_for_regex('a.b*c')
```

**Output**

```text
a\.b\*c
```

## Markup

The following functions escape a value for HTML or XML markup:

### `escape_for_html`

Escapes a value for HTML text or a quoted attribute value. Escapes `&`, `<`, `>`, `"`, `'`, and `/`.

The result isn't safe inside a `<script>` or `<style>` element, or inside an unquoted attribute. Use `escape_for_javascript` first, then `escape_for_html` for JavaScript in an event-handler attribute.

```wel
escape_for_html(value)
```

| Parameter | Description |
| --- | --- |
| value | The value to escape. Raises `E100` for a `List`, `Map`, or `Binary` value. |

Escape HTML markup characters

The following example escapes the markup characters in an HTML string:

**Formula**

```wel
escape_for_html('<b>Tom & Jerry</b>')
```

**Output**

```text
&lt;b&gt;Tom &amp; Jerry&lt;&#x2F;b&gt;
```

### `escape_for_xml`

Escapes a value for XML text or an attribute, and strips code points that are illegal in XML 1.0.

Removing these code points prevents source-system control characters from producing XML that a parser can't process.

```wel
escape_for_xml(value)
```

| Parameter | Description |
| --- | --- |
| value | The value to escape. |

Escape XML markup characters

The following example escapes the markup characters in an XML string:

**Formula**

```wel
escape_for_xml('<tag> & more')
```

**Output**

```text
&lt;tag&gt; &amp; more
```

## Data formats

The following functions escape a value for a specific data or code format:

### `escape_for_csv`

Escapes a value for a CSV field, following RFC 4180 by quoting the field and doubling internal quotes when needed.

Pass `'safe_formulas'` to prevent **CSV formula injection**. Spreadsheet applications otherwise treat a field beginning with a tab, a carriage return, a line feed, a negative number, `=`, `+`, `-`, `@`, or a full-width equivalent as a formula, so a value from an untrusted source can run when someone opens the file. `'safe_formulas'` prefixes potentially dangerous fields with an apostrophe (`'`).

```wel
escape_for_csv(value, 'safe_formulas')
```

| Parameter | Description |
| --- | --- |
| value | The value to escape. Raises `E100` for a `List`, `Map`, or `Binary` value. |
| 'safe\_formulas' | Optional. Pass this parameter to also neutralize leading formula characters. Raises `E225` for an unrecognized mode. |

Quote a field containing a comma

The following example quotes a CSV field containing a comma:

**Formula**

```wel
escape_for_csv('Smith, Josh')
```

**Output**

```wel
"Smith, Josh"
```

Neutralize a leading formula character

The following example neutralizes a leading formula character with `'safe_formulas'`:

**Formula**

```wel
escape_for_csv('=1+1', 'safe_formulas')
```

**Output**

```wel
"'=1+1"
```

> **USE SAFE\_FORMULAS FOR ANYTHING A PERSON OPENS**
> 
> Pass `'safe_formulas'` when a person opens the CSV in a spreadsheet application. This option isn't necessary for machine-to-machine processing that doesn't evaluate spreadsheet formulas.

### `escape_for_json_string`

Escapes a value to embed inside a JSON string, without adding the surrounding quotes. It escapes only `"`, `\`, and control characters, leaving `/` and non-ASCII characters unchanged.

Use this when assembling JSON text by hand. Use [to\_json](/en/wel/stdlib/json), which handles escaping throughout, to serialize a whole value instead.

```wel
escape_for_json_string(value)
```

| Parameter | Description |
| --- | --- |
| value | The value to escape. Raises `E100` for a `List`, `Map`, or `Binary` value. |

Escape a quote for a JSON string

The following example escapes a double quote for embedding inside a JSON string:

**Formula**

```wel
escape_for_json_string('He said "hi"')
```

**Output**

```text
He said \"hi\"
```

### `escape_for_javascript`

Escapes a value for use inside a single or double-quoted JavaScript string literal, without adding the quotes.

| Character | Result |
| --- | --- |
| `'`, `"`, `\`, `/` | Gains a preceding backslash |
| `<`, `>` | `\x3C`, `\x3E` |
| Newline, CR, tab, backspace, form feed | Becomes `\n`, `\r`, `\t`, `\b`, `\f` |
| `U+2028`, `U+2029` | Becomes `\u2028`, `\u2029` |
| Other control characters | Becomes `\uXXXX` |

Escaping `<` and `>` means the result can't close a `<script>` element. Backticks and `${` aren't escaped, so don't put the result in a template literal.

```wel
escape_for_javascript(value)
```

| Parameter | Description |
| --- | --- |
| value | Any scalar value. A number, `Boolean`, temporal value, or `null` is first converted to text by the [String](/en/wel/stdlib/conversion#string) rules, and `null` becomes `'null'`. Raises `E100` for a `List`, `Map`, or `Binary` value. |

Escape an apostrophe for JavaScript

The following example escapes an apostrophe for a JavaScript string literal:

**Formula**

```wel
escape_for_javascript("O'Brien")
```

**Output**

```text
O\'Brien
```

## URLs and query strings

These three related functions handle spaces differently. Choose the function that matches the required URL format:

| Function | Space becomes | Use for |
| --- | --- | --- |
| `escape_for_url` | `%20` | A whole string, as defined in RFC 3986 |
| `uri_encode_www_form_component` | `%20` | One component of a URL |
| `uri_encode_www_form` | `+` | A whole form-encoded query string |

### `escape_for_url`

Percent-encodes a string as defined in RFC 3986.

```wel
escape_for_url(value)
```

| Parameter | Description |
| --- | --- |
| value | The value to encode. |

Percent-encode a whole string

The following example percent-encodes a whole string as defined in RFC 3986:

**Formula**

```wel
escape_for_url('name=Kalani Park&x=1')
```

**Output**

```text
name%3DKalani%20Park%26x%3D1
```

### `uri_encode_www_form_component`

Percent-encodes a single URI component. Unreserved characters pass through unchanged.

```wel
uri_encode_www_form_component(value)
```

| Parameter | Description |
| --- | --- |
| value | The component to encode. |

Percent-encode a single component

The following example percent-encodes a single URI component:

**Formula**

```wel
uri_encode_www_form_component('Kalani Park')
```

**Output**

```text
Kalani%20Park
```

### `uri_decode_www_form_component`

Decodes a percent-encoded URI component. A `+` passes through unchanged rather than becoming a space.

```wel
uri_decode_www_form_component(value)
```

| Parameter | Description |
| --- | --- |
| value | The component to decode. Malformed percent-encoding raises `E226`. |

Decode a percent-encoded component

The following example decodes a percent-encoded URI component:

**Formula**

```wel
uri_decode_www_form_component('Kalani%20Park')
```

**Output**

```text
Kalani Park
```

### `uri_encode_www_form`

Encodes a `Map` as an `application/x-www-form-urlencoded` query string, with pairs joined by `&` in the map's order.

Keys and values use the WHATWG form rules: A space becomes `+`, ASCII letters, digits, and `*`, `-`, `.`, `_` pass through unchanged, and every other byte becomes `%XX`. A `String` value is written as is. Any other scalar value is written in its canonical text form, so `true` becomes `true`, `null` becomes `null`, and a date becomes its ISO form.

```wel
uri_encode_www_form(map, options)
```

| Parameter | Description |
| --- | --- |
| map | The map of parameters. A `List` value writes one pair for each item. An empty `List` raises `E218`. A `Map`, `Binary`, or nested `List` value raises `E100`. |
| options | Optional map specifying the `dialect`. `'whatwg'` (default) repeats the key for each `List` item. `'rack'` writes `key[]` for each item, and raises `E218` for a key containing `[` or `]`. An unrecognized option key raises `E225`. An unrecognized `dialect` value raises `E225`. |

Encode a map as a query string

The following example encodes a map as a form-urlencoded query string:

**Formula**

```wel
uri_encode_www_form({status: 'open', q: 'blue widget'})
```

**Output**

```text
status=open&q=blue+widget
```

### `uri_decode_www_form`

Decodes a query string into a `Map`. The function decodes `+` to a space, skips empty pairs, decodes a pair with no `=` sign to an empty value, and keeps a leading `?` literally as part of the first key.

```wel
uri_decode_www_form(text, options)
```

| Parameter | Description |
| --- | --- |
| text | The query string to decode. Malformed percent-encoding raises `E226`. |
| options | Optional map to control decoding. `collect_duplicates`: Makes repeated keys collect into a list. A duplicate key without `collect_duplicates` raises `E223`., `dialect`: `'rack'` reads `key[]` arrays. `'whatwg'` treats keys as opaque. An invalid `dialect` value raises `E225`. An unrecognized option key raises `E225`. |

Decode a query string into a map

The following example decodes a form-urlencoded query string into a map:

**Formula**

```wel
uri_decode_www_form('status=open&q=blue+widget')
```

**Output**

```wel
{status: "open", q: "blue widget"}
```

### Use case: Build a filtered API request

Search terms from inbound data can contain spaces and punctuation. Encode the parameters as a map instead of concatenating strings to escape each value and preserve the separators:

**Input**

```json
{
  "status": "open",
  "search": "blue widget & more"
}
```

**Formula**

```wel
f"/api/v2/orders?{uri_encode_www_form({status: _.status, q: _.search})}"
```

**Output**

```json
"/api/v2/orders?status=open&q=blue+widget+%26+more"
```

`uri_encode_www_form` encodes the `&` inside the search term as `%26` so it isn't mistaken for a parameter separator, and leaves the `&` that genuinely separates the two parameters untouched.

## Related

- [JSON functions](/en/wel/stdlib/json): Use `to_json` to serialize a whole value.
- [String functions](/en/wel/stdlib/string): Regular-expression matching and replacement.
- [Encoding functions](/en/wel/stdlib/encoding): Character encodings, not escaping.
- [Strings and formatting](/en/wel/language/strings): More information about f-strings.

---
