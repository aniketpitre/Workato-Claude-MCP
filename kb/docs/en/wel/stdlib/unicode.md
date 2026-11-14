---
url: 'https://docs.workato.com/en/wel/stdlib/unicode.md'
description: >-
  Use WEL Unicode functions to handle text by grapheme, normalize Unicode text,
  detect deceptive text, and convert Japanese kana and width.
---

# Unicode functions

Unicode functions handle text based on how readers perceive it rather than how systems store it. Use these functions for non-English text, strings that look identical but aren’t equal, and potentially deceptive text from external sources.

## Grapheme clusters

**Grapheme clusters** represent user-perceived characters rather than individual code points. A family emoji displays as one character but consists of several code points. An accented letter can be stored as one code point or as a letter and a combining mark.

| Formula | Result |
| --- | --- |
| `grapheme_length('👨‍👩‍👧')` | `1` |
| `length('👨‍👩‍👧')` | `5` |

Use grapheme functions for displays and human-facing character counts, such as when truncating text or enforcing a character limit on an input field.

### `grapheme_length`

Counts user-perceived characters (grapheme clusters).

```wel
grapheme_length(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to measure. |

Count grapheme clusters in a family emoji

The following example counts the grapheme clusters in a family emoji made of several code points:

**Formula**

```wel
grapheme_length('👨‍👩‍👧')
```

**Output**

```wel
1
```

### `grapheme_substring`

Extracts text by grapheme-cluster index without splitting characters that contain multiple code points.

```wel
grapheme_substring(text, start, length)
```

| Parameter | Description |
| --- | --- |
| text | The string to extract from. |
| start | Zero-based grapheme index. Negative counts from the end. A start exactly at the end returns an empty string. Any other out-of-range start raises `E201`. |
| length | Optional number of grapheme clusters. A negative `length` raises `E211`. |

Extract a substring by grapheme index

The following example extracts a two-grapheme substring from an accented word:

**Formula**

```wel
grapheme_substring('héllo', 0, 2)
```

**Output**

```text
hé
```

### `grapheme_reverse`

Reverses a string by grapheme clusters.

```wel
grapheme_reverse(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to reverse. |

Reverse a string by grapheme clusters

The following example reverses a string by grapheme clusters:

**Formula**

```wel
grapheme_reverse('abc')
```

**Output**

```text
cba
```

### `grapheme_lpad` and `grapheme_rpad`

Pad a string to a width measured in grapheme clusters.

Use these rather than [lpad](/en/wel/stdlib/string#lpad) and [rpad](/en/wel/stdlib/string#rpad) for fixed-width output containing non-ASCII text, so the columns line up for a reader.

```wel
grapheme_lpad(text, width, pad)
grapheme_rpad(text, width, pad)
```

| Parameter | Description |
| --- | --- |
| text | The string to pad. |
| width | Target width in grapheme clusters. Negative values and values over 10,000,000 raise `E211`. |
| pad | The padding string. Padding repeats and truncates as needed to reach the correct `width`. |

Pad a string on the left

The following example pads a string on the left to a width of 5 grapheme clusters:

**Formula**

```wel
grapheme_lpad('42', 5, '0')
```

**Output**

```wel
00042
```

Pad a string on the right

The following example pads a string on the right to a width of 5 grapheme clusters:

**Formula**

```wel
grapheme_rpad('42', 5, '0')
```

**Output**

```wel
42000
```

## Normalization

Systems can store the same visible text in different ways. For example, `café` can contain a single `é` or an `e` followed by a combining accent. These representations look identical but aren't equal. This difference can cause a lookup to fail for an existing record.

Normalization converts text to a canonical form so comparisons between different systems evaluate correctly.

| Form | What it does |
| --- | --- |
| `nfc` | Compose: Combine marks into single characters. `nfc` is the usual choice for storage. |
| `nfd` | Decompose: Split characters into base characters and combining marks. |
| `nfkc` | Compose, and fold compatibility variants such as full-width to half-width. |
| `nfkd` | Decompose, and fold compatibility variants. |

Normalize to `nfc` when data arrives, and comparisons downstream behave. An unrecognized `form` raises `E206`.

### `unicode_normalize`

Converts a string to the normalization form you specify.

```wel
unicode_normalize(text, form)
```

| Parameter | Description |
| --- | --- |
| text | The string to normalize. |
| form | The normalization form to convert to: `nfc`, `nfd`, `nfkc`, or `nfkd`. Any other value raises `E225`. |

Length of the composed form

The following example measures the length of the composed form:

**Formula**

```wel
length('café')
```

**Output**

```wel
4
```

Length of the decomposed form

The following example measures the length after converting the string to NFD:

**Formula**

```wel
length(unicode_normalize('café', 'nfd'))
```

**Output**

```wel
5
```

The decomposed form is one unit longer because the accent becomes a separate combining mark. The two forms appear identical on screen.

### `unicode_normalized?`

Returns `true` if the string is already in a form you specify.

```wel
unicode_normalized?(text, form)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |
| form | The normalization form to test against: `nfc`, `nfd`, `nfkc`, or `nfkd`. Any other value raises `E225`. |

A composed string is already NFC

The following example tests a composed string against the NFC form:

**Formula**

```wel
unicode_normalized?('café', 'nfc')
```

**Output**

```wel
true
```

A decomposed string isn't NFC

The following example tests a decomposed string against the NFC form:

**Formula**

```wel
unicode_normalized?(unicode_normalize('café', 'nfd'), 'nfc')
```

**Output**

```wel
false
```

### `unicode_compare`

Compares the numeric value of Unicode code points in two strings after normalization.

```wel
unicode_compare(first, second, form)
```

| Parameter | Description |
| --- | --- |
| first | The first string. |
| second | The second string. |
| form | Optional normalization form: `nfc`, `nfd`, `nfkc`, or `nfkd`. Defaults to `nfc`. Any other value raises `E225`. |

Returns one of the following values:

- `-1`: `first` sorts before `second`
- `0`: Both are equal
- `1`: `first` sorts after `second`.

Compare a composed and a decomposed string

The following example compares a composed string against its decomposed form:

**Formula**

```wel
unicode_compare('café', unicode_normalize('café', 'nfd'))
```

**Output**

```wel
0
```

## Detect deceptive text

Text arriving from outside can be built to mislead a person reading it. These functions surface that intent.

### `unicode_contains_suspicious?`

Detects text designed to deceive, such as bidirectional overrides, zero-width characters, confusable lookalike characters, Zalgo stacking, or private-use code points.

```wel
unicode_contains_suspicious?(text)
unicode_contains_suspicious?(text, options)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |
| options | Optional map of `Boolean` switches, one per check. `bidi_overrides`: Bidirectional overrides.; `zero_width`: Zero-width characters.; `controls`: Control characters.; `noncharacters`: Unicode non-character code points.; `replacement`: The Unicode replacement character.; `private_use`: Private-use code points.; `confusables`: Confusable lookalike characters.; `zalgo`: Zalgo stacking.; `zalgo_threshold`: An `Integer` threshold for Zalgo detection, rather than a `Boolean` switch. Defaults to `4`. A negative value raises `E211`. An unrecognized key raises `E225`. |

A plain domain isn't suspicious

The following example tests a domain made entirely of Latin characters:

**Formula**

```wel
unicode_contains_suspicious?('paypal.com')
```

**Output**

```wel
false
```

A lookalike domain is suspicious

The following example tests a domain containing a Cyrillic lookalike character:

**Formula**

```wel
unicode_contains_suspicious?('pаypal.com')
```

**Output**

```wel
true
```

> **THOSE TWO STRINGS AREN'T THE SAME**
> 
> The second contains a Cyrillic **а** in place of the Latin **a**. It renders identically in most fonts, and a person approving it can't tell the difference.
> 
> Run this check on text from untrusted sources before a person acts on it, such as supplier names in payments, domains in notifications, or display names in approval requests.

### `unicode_contains_bidi?`

Detects right-to-left characters by checking for Unicode Bidi\_Class values of `R` (right-to-left) and `AL` (Arabic letter). Arabic-Indic digits, punctuation, and combining marks return `false`.

Right-to-left characters are legitimate in Arabic and Hebrew text. They are also the mechanism behind attacks that make a string display in a different order from how it's stored, so treat a `true` result as a signal to look rather than an error on its own.

```wel
unicode_contains_bidi?(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |

Plain ASCII text has no bidirectional characters

The following example tests plain ASCII text:

**Formula**

```wel
unicode_contains_bidi?('hello')
```

**Output**

```wel
false
```

### `unicode_contains_emoji?`

Detects emoji by checking for the Unicode Emoji\_Presentation property. A character that defaults to text presentation (`❤`) only counts when it's followed by the `U+FE0F` variation selector that requests emoji presentation (`❤️`).

```wel
unicode_contains_emoji?(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |

Text containing an emoji

The following example tests a string containing an emoji:

**Formula**

```wel
unicode_contains_emoji?('ok 👍')
```

**Output**

```wel
true
```

Text without an emoji

The following example tests a string with no emoji:

**Formula**

```wel
unicode_contains_emoji?('plain')
```

**Output**

```wel
false
```

## Japanese text

Japanese systems distinguish two kana scripts and two character widths, and often require a specific combination. These six functions convert between them.

### `hiragana_to_katakana` and `katakana_to_hiragana`

Convert between the two kana scripts. Conversion covers small kana, `ゔ`/`ヴ`, and the kana iteration marks. The long vowel mark `ー` stays unchanged, because it's shared by both scripts.

```wel
hiragana_to_katakana(text)
katakana_to_hiragana(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to convert. |

Convert hiragana to katakana

The following example converts hiragana to katakana:

**Formula**

```wel
hiragana_to_katakana('ひらがな')
```

**Output**

```text
ヒラガナ
```

Convert katakana to hiragana

The following example converts katakana to hiragana:

**Formula**

```wel
katakana_to_hiragana('カタカナ')
```

**Output**

```text
かたかな
```

### `to_fullwidth_ascii` and `to_halfwidth_ascii`

Convert ASCII characters between full-width and half-width forms.

```wel
to_fullwidth_ascii(text)
to_halfwidth_ascii(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to convert. |

Convert ASCII to full-width

The following example converts ASCII characters to their full-width form:

**Formula**

```wel
to_fullwidth_ascii('AB1')
```

**Output**

```text
ＡＢ１
```

Convert ASCII to half-width

The following example converts full-width characters back to their half-width ASCII form:

**Formula**

```wel
to_halfwidth_ascii('ＡＢ１')
```

**Output**

```text
AB1
```

### `to_fullwidth_katakana` and `to_halfwidth_katakana`

Convert katakana between full-width and half-width forms. `to_halfwidth_katakana` splits a voiced or semi-voiced katakana character into a base character and a separate mark, and `to_fullwidth_katakana` merges them back. `ヰ`, `ヱ`, and the small `ヮ` have no half-width form, so `to_halfwidth_katakana` leaves them unchanged.

```wel
to_fullwidth_katakana(text)
to_halfwidth_katakana(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to convert. |

Convert katakana to full-width

The following example converts half-width katakana to its full-width form:

**Formula**

```wel
to_fullwidth_katakana('ｶﾀｶﾅ')
```

**Output**

```text
カタカナ
```

Convert katakana to half-width

The following example converts full-width katakana to its half-width form:

**Formula**

```wel
to_halfwidth_katakana('カタカナ')
```

**Output**

```text
ｶﾀｶﾅ
```

### Use case: Normalize names before matching across systems

Two systems hold the same customer, but one stored the name decomposed. Use Unicode functions to normalize both names so the match succeeds, and flag anything that shouldn't be matched automatically:

**Input**

```json
{
  "crm_name": "café",
  "erp_name": "café"
}
```

**Formula**

```wel
{
  equal_as_stored: _.crm_name == _.erp_name,
  equal_normalized: unicode_compare(_.crm_name, _.erp_name) == 0,
  needs_review: unicode_contains_suspicious?(_.erp_name)
}
```

**Output**

```json
{
  "equal_as_stored": false,
  "equal_normalized": true,
  "needs_review": false
}
```

The two names in the input are _not the same bytes_. The CRM stored `é` as one character and the ERP stored it as `e` and a combining accent. They render identically, and no amount of looking at them will reveal the difference.

A plain `==` therefore says these are different customers. That incorrect result is the bug, because it creates a duplicate record that then diverges.

## Related

- [String functions](/en/wel/stdlib/string): `length`, `substring`, `lpad` and their byte-oriented behavior.
- [Encoding functions](/en/wel/stdlib/encoding): Convert text to bytes in a named encoding.
- [Common functions](/en/wel/stdlib/common): Information about `length` across data types.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E201`.

---
