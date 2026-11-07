---
url: 'https://docs.workato.com/en/wel/stdlib/unicode.md'
description: >-
  WEL Unicode functions for grapheme-aware text handling, Unicode normalization,
  detecting deceptive text, and Japanese kana and width conversion.
---

# Unicode functions

Unicode functions handle text based on how readers perceive it rather than how systems store it. Use these functions for non-English text, strings that look identical but aren’t equal, and potentially deceptive text from external sources.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Grapheme clusters

**Grapheme clusters** represent user-perceived characters rather than individual code points. A family emoji displays as one character but consists of several code points. An accented letter can be stored as one code point or as a letter and a combining mark.

| Formula | Result |
| --- | --- |
| `grapheme_length('👨‍👩‍👧')` | `1` |
| `length('👨‍👩‍👧')` | `5` |

Use grapheme functions for displays and human-facing character counts, such as when truncating text or enforcing a character limit on an input field.

### `grapheme_length`

Counts user-perceived characters (grapheme clusters).

```text
grapheme_length(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to measure. |

Count grapheme clusters in a family emoji

The following example counts the grapheme clusters in a family emoji made of several code points:

**Formula**

```text
grapheme_length('👨‍👩‍👧')
```

**Output**

```text
1
```

### `grapheme_substring`

Extracts text by grapheme-cluster index without splitting characters that contain multiple code points.

A negative start counts from the end. A start exactly at the end returns an empty string. Any other out-of-range start raises `E201`.

```text
grapheme_substring(text, start, length)
```

| Parameter | Description |
| --- | --- |
| text | The string to extract from. |
| start | Zero-based grapheme index. Negative counts from the end. |
| length | Optional number of grapheme clusters. |

Extract a substring by grapheme index

The following example extracts a two-grapheme substring from an accented word:

**Formula**

```text
grapheme_substring('héllo', 0, 2)
```

**Output**

```text
hé
```

### `grapheme_reverse`

Reverses a string by grapheme clusters.

```text
grapheme_reverse(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to reverse. |

Reverse a string by grapheme clusters

The following example reverses a string by grapheme clusters:

**Formula**

```text
grapheme_reverse('abc')
```

**Output**

```text
cba
```

### `grapheme_lpad` and `grapheme_rpad`

Pad a string to a width measured in grapheme clusters.

Use these rather than [lpad](/en/wel/stdlib/string#lpad) and [rpad](/en/wel/stdlib/string#rpad) for fixed-width output containing non-ASCII text, so the columns line up for a reader.

```text
grapheme_lpad(text, width, pad)
grapheme_rpad(text, width, pad)
```

| Parameter | Description |
| --- | --- |
| text | The string to pad. |
| width | Target width in grapheme clusters. |
| pad | The padding string. |

Pad a string on the left

The following example pads a string on the left to a width of 5 grapheme clusters:

**Formula**

```text
grapheme_lpad('42', 5, '0')
```

**Output**

```text
00042
```

Pad a string on the right

The following example pads a string on the right to a width of 5 grapheme clusters:

**Formula**

```text
grapheme_rpad('42', 5, '0')
```

**Output**

```text
42000
```

## Normalization

Systems can store the same visible text in different ways. For example, `café` can contain a single `é` or an `e` followed by a combining accent. These representations look identical but aren't equal. This difference can cause a lookup to fail for an existing record.

Normalization converts text to a canonical form so comparisons work.

| Form | What it does |
| --- | --- |
| `nfc` | Compose: combine marks into single characters. The usual choice for storage. |
| `nfd` | Decompose: split characters into base characters and combining marks. |
| `nfkc` | Compose, and fold compatibility variants such as full-width to half-width. |
| `nfkd` | Decompose, and fold compatibility variants. |

Normalize to `nfc` when data arrives, and comparisons downstream behave.

### `unicode_normalize`

Converts a string to the given normalization form.

```text
unicode_normalize(text, form)
```

| Parameter | Description |
| --- | --- |
| text | The string to normalize. |
| form | `nfc`, `nfd`, `nfkc`, or `nfkd`. |

Length of the composed form

The following example measures the length of the composed form:

**Formula**

```text
length('café')
```

**Output**

```text
4
```

Length of the decomposed form

The following example measures the length after converting the string to NFD:

**Formula**

```text
length(unicode_normalize('café', 'nfd'))
```

**Output**

```text
5
```

The decomposed form is one unit longer because the accent becomes a separate combining mark. The two forms appear identical on screen.

### `unicode_normalized?`

Returns `true` if the string is already in the given form.

```text
unicode_normalized?(text, form)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |
| form | `nfc`, `nfd`, `nfkc`, or `nfkd`. |

A composed string is already NFC

The following example tests a composed string against the NFC form:

**Formula**

```text
unicode_normalized?('café', 'nfc')
```

**Output**

```text
true
```

A decomposed string isn't NFC

The following example tests a decomposed string against the NFC form:

**Formula**

```text
unicode_normalized?(unicode_normalize('café', 'nfd'), 'nfc')
```

**Output**

```text
false
```

### `unicode_compare`

Compares two strings after normalizing both, returning `-1`, `0`, or `1`.

`unicode_compare` is the reliable way to compare text from two different systems. Plain `==` compares what is stored. `unicode_compare` compares what is written.

```text
unicode_compare(first, second, form)
```

| Parameter | Description |
| --- | --- |
| first | The first string. |
| second | The second string. |
| form | Optional normalization form. Defaults to `nfc`. |

Compare a composed and a decomposed string

The following example compares a composed string against its decomposed form:

**Formula**

```text
unicode_compare('café', unicode_normalize('café', 'nfd'))
```

**Output**

```text
0
```

The two arguments are stored differently and compare as equal, which is the entire point.

## Detect deceptive text

Text arriving from outside can be built to mislead a person reading it. These functions surface that intent.

### `unicode_contains_suspicious?`

Detects text designed to deceive, such as bidirectional overrides, zero-width characters, confusable lookalike characters, Zalgo stacking, or private-use code points.

```text
unicode_contains_suspicious?(text)
unicode_contains_suspicious?(text, options)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |
| options | Optional map of `Boolean` switches, one per check. `bidi_overrides`: Bidirectional overrides.; `zero_width`: Zero-width characters.; `controls`: Control characters.; `noncharacters`: Unicode non-character code points.; `replacement`: The Unicode replacement character.; `private_use`: Private-use code points.; `confusables`: Confusable lookalike characters.; `zalgo`: Zalgo stacking.; `zalgo_threshold`: An `Integer` threshold for Zalgo detection, rather than a `Boolean` switch. |

A plain domain isn't suspicious

The following example tests a domain made entirely of Latin characters:

**Formula**

```text
unicode_contains_suspicious?('paypal.com')
```

**Output**

```text
false
```

A lookalike domain is suspicious

The following example tests a domain containing a Cyrillic lookalike character:

**Formula**

```text
unicode_contains_suspicious?('pаypal.com')
```

**Output**

```text
true
```

> **THOSE TWO STRINGS AREN'T THE SAME**
> 
> The second contains a Cyrillic **а** in place of the Latin **a**. It renders identically in most fonts, and a person approving it can't tell the difference.
> 
> Run this check on text from untrusted sources before a person acts on it, such as supplier names in payments, domains in notifications, or display names in approval requests.

### `unicode_contains_bidi?`

Detects right-to-left characters.

Right-to-left characters are legitimate in Arabic and Hebrew text. They are also the mechanism behind attacks that make a string display in a different order from how it's stored, so treat a `true` result as a signal to look rather than an error on its own.

```text
unicode_contains_bidi?(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |

Plain ASCII text has no bidirectional characters

The following example tests plain ASCII text:

**Formula**

```text
unicode_contains_bidi?('hello')
```

**Output**

```text
false
```

### `unicode_contains_emoji?`

Detects emoji.

```text
unicode_contains_emoji?(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to test. |

Text containing an emoji

The following example tests a string containing an emoji:

**Formula**

```text
unicode_contains_emoji?('ok 👍')
```

**Output**

```text
true
```

Text without an emoji

The following example tests a string with no emoji:

**Formula**

```text
unicode_contains_emoji?('plain')
```

**Output**

```text
false
```

## Japanese text

Japanese systems distinguish two kana scripts and two character widths, and often require a specific combination. These six functions convert between them.

### `hiragana_to_katakana` and `katakana_to_hiragana`

Convert between the two kana scripts.

```text
hiragana_to_katakana(text)
katakana_to_hiragana(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to convert. |

Convert hiragana to katakana

The following example converts hiragana to katakana:

**Formula**

```text
hiragana_to_katakana('ひらがな')
```

**Output**

```text
ヒラガナ
```

Convert katakana to hiragana

The following example converts katakana to hiragana:

**Formula**

```text
katakana_to_hiragana('カタカナ')
```

**Output**

```text
かたかな
```

### `to_fullwidth_ascii` and `to_halfwidth_ascii`

Convert ASCII characters between full-width and half-width forms.

```text
to_fullwidth_ascii(text)
to_halfwidth_ascii(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to convert. |

Convert ASCII to full-width

The following example converts ASCII characters to their full-width form:

**Formula**

```text
to_fullwidth_ascii('AB1')
```

**Output**

```text
ＡＢ１
```

Convert ASCII to half-width

The following example converts full-width characters back to their half-width ASCII form:

**Formula**

```text
to_halfwidth_ascii('ＡＢ１')
```

**Output**

```text
AB1
```

### `to_fullwidth_katakana` and `to_halfwidth_katakana`

Convert katakana between full-width and half-width forms.

```text
to_fullwidth_katakana(text)
to_halfwidth_katakana(text)
```

| Parameter | Description |
| --- | --- |
| text | The string to convert. |

Convert katakana to full-width

The following example converts half-width katakana to its full-width form:

**Formula**

```text
to_fullwidth_katakana('ｶﾀｶﾅ')
```

**Output**

```text
カタカナ
```

Convert katakana to half-width

The following example converts full-width katakana to its half-width form:

**Formula**

```text
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

```text
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
