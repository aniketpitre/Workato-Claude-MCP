---
url: 'https://docs.workato.com/en/wel/stdlib/string.md'
description: >-
  WEL string functions check, clean, extract, and replace text in recipe data,
  including case conversion, padding, and regular expression matching.
---

# String functions

String functions read and reshape text. Use them to clean inbound payloads, extract identifiers, normalize values before they reach a destination system, and build the exact string format a target expects.

`_` is the input your expression receives in these examples. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Call a string function

Call a function directly, or pipe a value into it with `>>`:

```text
upper(_.status)
_.status >> upper
```

The pipe form reads left to right, which makes it the better choice when you chain several steps:

```text
_.email >> trim >> lower
```

The piped value fills the function's first argument. Write any other arguments normally:

```text
_.order_id >> starts_with?('SO-')
```

> **STRINGS DON'T CONVERT AUTOMATICALLY**
> 
> String functions require a `String`. Passing a number or a date raises `E100`. Wrap the value in `String(...)` first. Refer to the [Data types](/en/wel/language/data-types) documentation for details.

## Check a string

The following functions return a `Boolean`. Use them in conditions, in `filter_by`, and to guard a step before it runs.

### `blank?`

Returns `true` if the string is empty or contains only whitespace.

```text
blank?(string)
```

| Parameter | Description |
| --- | --- |
| string | The string to test. |

A whitespace-only string is blank

The following example tests a whitespace-only string:

**Formula**

```text
blank?('   ')
```

**Output**

```text
true
```

A non-empty string isn't blank

The following example tests a non-empty string:

**Formula**

```text
blank?('SO-1001')
```

**Output**

```text
false
```

### `empty?`

Returns `true` if the value has no content. It works on a `String`, `List`, `Map`, or `Binary` value, and unlike `blank?`, it returns `true` for `null`.

```text
empty?(value)
```

| Parameter | Description |
| --- | --- |
| value | A string, list, map, binary value, or null. |

An empty string is empty

The following example tests an empty string:

**Formula**

```text
empty?('')
```

**Output**

```text
true
```

Null is empty

The following example tests a `null` value:

**Formula**

```text
empty?(null)
```

**Output**

```text
true
```

> **BLANK? OR EMPTY?**
> 
> Use `empty?` when the field may be missing entirely, because it accepts `null`. Use `blank?` when the field is present but may contain only spaces. `blank?(null)` raises an error.

### `contains?`

Returns `true` if the string contains the substring, using a case-sensitive comparison.

```text
contains?(string, substring)
```

| Parameter | Description |
| --- | --- |
| string | The string to search. |
| substring | The value to look for. |

A matching substring, same case

The following example tests a substring that matches case exactly:

**Formula**

```text
contains?('Partner account', 'Partner')
```

**Output**

```text
true
```

A matching substring, different case

The following example tests a substring that matches except for case:

**Formula**

```text
contains?('Partner account', 'partner')
```

**Output**

```text
false
```

### `starts_with?`

Returns `true` if the string begins with the prefix.

```text
starts_with?(string, prefix)
```

| Parameter | Description |
| --- | --- |
| string | The string to test. |
| prefix | The prefix to look for. |

A string starting with the given prefix

The following example tests a string that starts with the given prefix:

**Formula**

```text
starts_with?('SO-1001', 'SO-')
```

**Output**

```text
true
```

### `ends_with?`

Returns `true` if the string ends with the suffix.

```text
ends_with?(string, suffix)
```

| Parameter | Description |
| --- | --- |
| string | The string to test. |
| suffix | The suffix to look for. |

A string ending with the given suffix

The following example tests a string that ends with the given suffix:

**Formula**

```text
ends_with?('invoice.pdf', '.pdf')
```

**Output**

```text
true
```

### `valid_email?`

Returns `true` if the string is a valid email address, as defined in RFC 5321 and RFC 5322.

```text
valid_email?(string)
```

| Parameter | Description |
| --- | --- |
| string | The address to validate. |

A valid email address

The following example tests a valid email address:

**Formula**

```text
valid_email?('nur@example.com')
```

**Output**

```text
true
```

An address with a doubled @ is invalid

The following example tests an address with a doubled `@`:

**Formula**

```text
valid_email?('nur@@example.com')
```

**Output**

```text
false
```

### `valid_url?`

Returns `true` if the string is a valid URL. Pass a list of schemes to restrict which are accepted.

```text
valid_url?(string)
valid_url?(string, schemes)
```

| Parameter | Description |
| --- | --- |
| string | The URL to validate. |
| schemes | Optional. A list of allowed schemes. |

A valid URL with no scheme restriction

The following example tests a valid URL with no scheme restriction:

**Formula**

```text
valid_url?('https://example.com/orders')
```

**Output**

```text
true
```

A URL whose scheme isn't in the allowed list

The following example tests a URL whose scheme isn't in the allowed list:

**Formula**

```text
valid_url?('ftp://example.com', ['http', 'https'])
```

**Output**

```text
false
```

### `match?`

Returns `true` if the string matches a regular expression. WEL uses ECMAScript regular expression syntax.

```text
match?(string, pattern)
```

| Parameter | Description |
| --- | --- |
| string | The string to test. |
| pattern | A regular expression. |

A string matching the pattern

The following example tests a string against a pattern it matches:

**Formula**

```text
match?('SO-1001', '^SO-\d+$')
```

**Output**

```text
true
```

### Use case: Filter a delimited recipient list

A webhook delivers recipients as one comma-separated string with inconsistent spacing, casing, and malformed entries. Use string functions to split it, normalize each address, then keep only the valid ones:

**Input**

```json
{
  "recipients": "a@example.com, B@Example.com ,,not-an-address"
}
```

**Formula**

```text
_.recipients
  >> split(',')
  >> map_by(e ~> trim(e) >> lower)
  >> filter_by(e ~> valid_email?(e))
```

**Output**

```json
["a@example.com", "b@example.com"]
```

`split` produces four entries, including one empty string. `trim` and `lower` normalize each one. `valid_email?` discards both the empty entry and `not-an-address`.

## Change case

The following functions change the case of a string's characters:

### `upper`

Converts the string to uppercase.

```text
upper(string)
```

| Parameter | Description |
| --- | --- |
| string | The string to convert. |

Convert a string to uppercase

The following example converts a string to uppercase:

**Formula**

```text
upper('acme corp')
```

**Output**

```text
ACME CORP
```

### `lower`

Converts the string to lowercase. Use it to normalize email addresses and codes before comparing or deduplicating them.

```text
lower(string)
```

| Parameter | Description |
| --- | --- |
| string | The string to convert. |

Convert a string to lowercase

The following example converts a string to lowercase:

**Formula**

```text
lower('ACME Corp')
```

**Output**

```text
acme corp
```

### `capitalize`

Converts the first character to uppercase and the rest to lowercase.

```text
capitalize(string)
```

| Parameter | Description |
| --- | --- |
| string | The string to convert. |

Capitalize a lowercase word

The following example capitalizes a lowercase word:

**Formula**

```text
capitalize('acme')
```

**Output**

```text
Acme
```

### `titleize`

Converts the first character of each whitespace-separated word to uppercase and the rest to lowercase.

```text
titleize(string)
```

| Parameter | Description |
| --- | --- |
| string | The string to convert. |

Title-case a lowercase phrase

The following example title-cases a lowercase phrase:

**Formula**

```text
titleize('acme widgets inc')
```

**Output**

```text
Acme Widgets Inc
```

## Clean and pad

The following functions remove whitespace or pad a string to a fixed width:

### `trim`

Removes leading and trailing whitespace.

```text
trim(string)
```

| Parameter | Description |
| --- | --- |
| string | The string to trim. |

Trim whitespace from both ends

The following example trims whitespace from both ends of a string:

**Formula**

```text
trim('  SO-1001  ')
```

**Output**

```text
SO-1001
```

### `ltrim`

Removes leading whitespace.

```text
ltrim(string)
```

| Parameter | Description |
| --- | --- |
| string | The string to trim. |

Trim whitespace from the start

The following example trims whitespace from the start of a string:

**Formula**

```text
ltrim('  SO-1001')
```

**Output**

```text
SO-1001
```

### `rtrim`

Removes trailing whitespace.

```text
rtrim(string)
```

| Parameter | Description |
| --- | --- |
| string | The string to trim. |

Trim whitespace from the end

The following example trims whitespace from the end of a string:

**Formula**

```text
rtrim('SO-1001  ')
```

**Output**

```text
SO-1001
```

### `lpad`

Pads the start of the string until it reaches the given width. Use it for zero-padded reference numbers and fixed-width records.

```text
lpad(string, width, pad)
```

| Parameter | Description |
| --- | --- |
| string | The string to pad. |
| width | The target width. |
| pad | The padding string. |

Zero-pad a number to a fixed width

The following example zero-pads a number to a fixed width:

**Formula**

```text
lpad('42', 8, '0')
```

**Output**

```text
00000042
```

### `rpad`

Pads the end of the string until it reaches the given width.

```text
rpad(string, width, pad)
```

| Parameter | Description |
| --- | --- |
| string | The string to pad. |
| width | The target width. |
| pad | The padding string. |

Space-pad a string to a fixed width

The following example space-pads a string to a fixed width:

**Formula**

```text
rpad('A-100', 8, ' ')
```

**Output**

```text
"A-100   "
```

Padded to 8 characters.

### `normalize_newlines`

Rewrites CRLF, CR, and LF line terminators to a single convention. Defaults to LF.

```text
normalize_newlines(string, terminator)
```

| Parameter | Description |
| --- | --- |
| string | The string to normalize. |
| terminator | Optional. The target line terminator. |

Normalize mixed line terminators to LF

The following example normalizes mixed line terminators to LF:

**Formula**

```text
normalize_newlines("a\r\nb\rc")
```

**Output**

```text
"a\nb\nc"
```

### Use case: Build a fixed-width record

Many ERP and mainframe systems accept fixed-width records rather than JSON. Use string functions to pad each field to its column width, then concatenate them:

**Input**

```json
{
  "sku": "A-100",
  "qty": 2
}
```

**Formula**

```text
rpad(_.sku, 10, ' ') ++ lpad(String(_.qty), 5, '0')
```

**Output**

```json
"A-100     00002"
```

The SKU occupies a 10-character column padded on the right. The quantity occupies a 5-character column zero-padded on the left. `qty` is an `Integer`, so `String(...)` converts it before padding.

## Extract part of a string

The following functions read or extract part of a string without changing the rest of it:

### `substring`

Extracts part of a string by code-point index. A negative start counts back from the end.

```text
substring(string, start, length)
```

| Parameter | Description |
| --- | --- |
| string | The source string. |
| start | The zero-based start index. |
| length | Optional. The number of code points to take. |

Extract from a start index to the end

The following example extracts from a start index to the end of the string:

**Formula**

```text
substring('SO-1001', 3)
```

**Output**

```text
1001
```

Extract a fixed-length substring

The following example extracts a fixed-length substring:

**Formula**

```text
substring('SO-1001', 0, 2)
```

**Output**

```text
SO
```

Extract using a negative start index

The following example extracts using a negative start index counting back from the end:

**Formula**

```text
substring('SO-1001', -4)
```

**Output**

```text
1001
```

> **OUT-OF-RANGE STARTS RAISE E201**
> 
> WEL clamps a `length` longer than the remaining string. A `start` past the end of the string raises `E201`. Check the length first when the start position isn't `0`.

### `index_of`

Returns the zero-based index of the first occurrence of a substring, or `-1` if it isn't found.

```text
index_of(string, substring)
```

| Parameter | Description |
| --- | --- |
| string | The string to search. |
| substring | The value to find. |

Find the index of a substring

The following example finds the index of a substring:

**Formula**

```text
index_of('orders/SO-1001', '/')
```

**Output**

```text
6
```

### `split`

Splits a string into a list on a literal separator.

```text
split(string, separator)
```

| Parameter | Description |
| --- | --- |
| string | The string to split. |
| separator | The literal separator. |

Split a string on a literal separator

The following example splits a string on a literal separator:

**Formula**

```text
split('a@example.com,b@example.com', ',')
```

**Output**

```text
["a@example.com", "b@example.com"]
```

### `split_regex`

Splits a string into a list on a regular expression. Use it when the delimiter varies.

```text
split_regex(string, pattern)
```

| Parameter | Description |
| --- | --- |
| string | The string to split. |
| pattern | A regular expression matching the separator. |

Split a string on a varying delimiter

The following example splits a string on a delimiter that varies between entries:

**Formula**

```text
split_regex('A-100; B-220,C-050', '[;,]\s*')
```

**Output**

```text
["A-100", "B-220", "C-050"]
```

### `match`

Returns the first regular expression match as a map, or `null` if there is no match. Key `0` is the full match, numeric keys hold each capture group, and named captures are also available by name.

```text
match(string, pattern)
```

| Parameter | Description |
| --- | --- |
| string | The string to search. |
| pattern | A regular expression. |

Match a pattern with named capture groups

The following example matches a pattern with named capture groups:

**Formula**

```text
match('SO-1001', '^(?<prefix>[A-Z]+)-(?<number>\d+)$')
```

**Output**

```text
{"0": "SO-1001", "1": "SO", "2": "1001", prefix: "SO", number: "1001"}
```

> **NAME YOUR CAPTURE GROUPS**
> 
> Named captures make a formula readable and keep it working when you add a group. Read the result as `match(...).number` rather than `match(...)['2']`.

### `match_all`

Returns every regular expression match as a list of maps, using the same key structure as `match`.

```text
match_all(string, pattern)
```

| Parameter | Description |
| --- | --- |
| string | The string to search. |
| pattern | A regular expression. |

Match every occurrence of a pattern

The following example matches every occurrence of a pattern:

**Formula**

```text
match_all('A-100 B-220', '[A-Z]-\d+')
```

**Output**

```text
[{"0": "A-100"}, {"0": "B-220"}]
```

### `parse_url`

Parses a URL into its components.

```text
parse_url(string)
```

| Parameter | Description |
| --- | --- |
| string | The URL to parse. |

Parse a URL into its components

The following example parses a URL into its components:

**Formula**

```text
parse_url('https://api.example.com:8443/v2/orders?status=open#top')
```

**Output**

```text
{scheme: "https", host: "api.example.com", port: 8443, path: "/v2/orders", query: "status=open", fragment: "top"}
```

### Use case: Extract an identifier from a callback path

An inbound callback carries the order number inside a URL path. Use a named capture group to pull it out, without depending on the position of the segment:

**Input**

```json
{
  "path": "/orders/SO-1001/lines"
}
```

**Formula**

```text
match(_.path, '/orders/(?<order>[A-Z]{2}-\d+)/').order
```

**Output**

```json
"SO-1001"
```

`match` returns a map, so the formula reads the `order` key directly. `match` returns `null` if the path can't match, and reading the key then fails as a result. Add a fallback with `|?` when the source data varies. Refer to the [Operators](/en/wel/language/operators#error-fallback) documentation for details.

## Replace part of a string

WEL has separate functions for literal and regular expression matching. Each comes in a first-match and an all-matches form.

| Function | Matches | Replaces |
| --- | --- | --- |
| `replace_first` | Literal text | First occurrence |
| `replace_all` | Literal text | All occurrences |
| `replace_first_regex`, `sub` | Regular expression | First match |
| `replace_all_regex`, `gsub` | Regular expression | All matches |

### `replace_all`

Replaces every occurrence of a literal substring.

```text
replace_all(string, pattern, replacement)
```

| Parameter | Description |
| --- | --- |
| string | The source string. |
| pattern | The literal text to find. |
| replacement | The replacement text. |

Remove every occurrence of a literal substring

The following example removes every occurrence of a literal substring:

**Formula**

```text
replace_all('A-100-X', '-', '')
```

**Output**

```text
A100X
```

### `replace_first`

Replaces the first occurrence of a literal substring.

```text
replace_first(string, pattern, replacement)
```

| Parameter | Description |
| --- | --- |
| string | The source string. |
| pattern | The literal text to find. |
| replacement | The replacement text. |

Remove the first occurrence of a literal substring

The following example removes the first occurrence of a literal substring:

**Formula**

```text
replace_first('A-100-X', '-', '')
```

**Output**

```text
A100-X
```

### `replace_all_regex`

Replaces every regular expression match. `gsub` is an alias.

```text
replace_all_regex(string, pattern, replacement)
```

| Parameter | Description |
| --- | --- |
| string | The source string. |
| pattern | A regular expression. |
| replacement | The replacement text. |

Collapse repeated whitespace to a single space

The following example collapses repeated whitespace into a single space:

**Formula**

```text
replace_all_regex('SO 1001  extra', '\s+', ' ')
```

**Output**

```text
SO 1001 extra
```

Strip non-digit characters using the gsub alias

The following example strips every non-digit character using the `gsub` alias:

**Formula**

```text
gsub('(555) 123-4567', '[^0-9]', '')
```

**Output**

```text
5551234567
```

### `replace_first_regex`

Replaces the first regular expression match. `sub` is an alias.

```text
replace_first_regex(string, pattern, replacement)
```

| Parameter | Description |
| --- | --- |
| string | The source string. |
| pattern | A regular expression. |
| replacement | The replacement text. |

Replace the first regex match using the sub alias

The following example replaces the first regular expression match using the `sub` alias:

**Formula**

```text
sub('SO-1001', '^SO', 'PO')
```

**Output**

```text
PO-1001
```

### `concat`

Joins two strings. Use `++` or string interpolation to join more than two, or to mix in other types.

```text
concat(first, second)
```

| Parameter | Description |
| --- | --- |
| first | The first string. |
| second | The second string. |

Join two strings

The following example joins two strings:

**Formula**

```text
concat('Josh', ' Ito')
```

**Output**

```text
Josh Ito
```

> **CONCAT TAKES EXACTLY TWO ARGUMENTS**
> 
> `concat` isn't variadic. Use `++` to join several values, or interpolation to embed them in a template:
> 
> ```text
> _.first_name ++ ' ' ++ _.last_name
> "Order ${_.order_id} for ${_.customer}"
> ```
> 
> Interpolation converts values to strings automatically. `++` doesn't. Refer to the [Strings and formatting](/en/wel/language/strings) documentation for details.

### Use case: Normalize an inbound contact

A signup webhook delivers names with inconsistent spacing and casing, and an email address that a downstream CRM treats as case-sensitive. Use string functions to normalize all three fields before the record is created:

**Input**

```json
{
  "first_name": "  josh ",
  "last_name": "ITO",
  "email": " Josh@Example.COM "
}
```

**Formula**

```text
{
  full_name: titleize(trim(_.first_name) ++ ' ' ++ trim(_.last_name)),
  email: lower(trim(_.email))
}
```

**Output**

```json
{
  "full_name": "Josh Ito",
  "email": "josh@example.com"
}
```

`trim` removes whitespace from each field before `++` joins them, so the joining space is the only space between the names. `titleize` then fixes the casing of both names at once. `lower` normalizes the address so it matches an existing CRM record regardless of how it was typed.

## Related

- [Data types](/en/wel/language/data-types): Why string functions require a `String`.
- [Strings and formatting](/en/wel/language/strings): Information about interpolation, f-strings, and format specs.
- [Operators](/en/wel/language/operators): Information about `++`, the pipe `>>`, and the fallback operators.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E100` and `E201`.

---
