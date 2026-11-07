# Workato Expression Language

26 pages. Paths are relative to the repository root.


## Workato Expression Language

- **Workato Expression Language** - `kb/docs/en/wel.md` - WEL is Workato's transformation language - 245 built-in functions, 16 data types, and exact decimal arithmetic, running natively alongside your recipe.
- **WEL cookbook** - `kb/docs/en/wel/cookbook.md` - Worked WEL examples of common integration problems - joins, grouping, deduplication, CSV and JWT generation, and error-tolerant batch processing.
- **WEL error codes** - `kb/docs/en/wel/errors.md` - Every WEL error code, what it means, whether you can catch it, and what to do about it, covering all 72 codes across four error families in WEL.
- **WEL language guide** - `kb/docs/en/wel/language.md` - The syntax and rules behind every WEL expression, the 16 data types, operators and precedence, how expressions are structured, and string formatting.
- **WEL quickstart** - `kb/docs/en/wel/quickstart.md` - Get started with WEL three ways - in the Transform Data action, with an external AI client, or with the wel command-line binary for fast local iteration.
- **WEL standard library** - `kb/docs/en/wel/stdlib.md` - The 245 built-in functions in WEL, spanning 16 categories - strings, lists, maps, temporal, numeric, crypto, encoding, escaping, and conversion.

## Language guide

- **Data types** - `kb/docs/en/wel/language/data-types.md` - The 16 WEL data types, including numbers, text, temporal types, collections, and the Skip marker, and how to choose the right one for each field.
- **Expressions** - `kb/docs/en/wel/language/expressions.md` - How a WEL expression is built, covering the input variable, field access, conditionals, let bindings, guards, lambdas, and named functions in a step.
- **Operators** - `kb/docs/en/wel/language/operators.md` - WEL operators for arithmetic, comparison, logic, concatenation, the pipeline operator, and the two fallback operators, with their precedence.
- **Strings and formatting** - `kb/docs/en/wel/language/strings.md` - WEL string literals, f-string interpolation, and format specifications for controlling padding, alignment, and decimal places in output text.

## Standard library

- **Binary functions** - `kb/docs/en/wel/stdlib/binary.md` - WEL binary functions for base64, hex, and quoted-printable conversion, measuring byte length, and slicing raw byte data from files and digests.
- **Common functions** - `kb/docs/en/wel/stdlib/common.md` - WEL common functions for measuring length, testing whether a value is present, providing a fallback when it isn't, and inspecting a value's type.
- **Conversion functions** - `kb/docs/en/wel/stdlib/conversion.md` - WEL conversion functions for casting values to Integer, Decimal, Float, String, Bool, Binary, temporal types, and the Null and Skip sentinels.
- **Crypto functions** - `kb/docs/en/wel/stdlib/crypto.md` - WEL crypto functions for hashing, HMAC signatures, JWT encoding and verification, PBKDF2 key derivation, and AES encryption and decryption of data.
- **Deep map functions** - `kb/docs/en/wel/stdlib/deep-map.md` - WEL deep map functions for collecting values and transforming leaf values anywhere inside a deeply nested API response, regardless of depth.
- **Encoding functions** - `kb/docs/en/wel/stdlib/encoding.md` - WEL encoding functions for converting between text and bytes in a named character encoding, checking convertibility, and encoding MIME email headers.
- **Escape functions** - `kb/docs/en/wel/stdlib/escape.md` - WEL escape functions for safely embedding values in CSV, HTML, XML, JSON, JavaScript, URLs, SOQL, OData, and regular expressions without breaking syntax.
- **Formatting functions** - `kb/docs/en/wel/stdlib/formatting.md` - WEL formatting functions for rendering dates, times, numbers, and currency as display strings, parsing datetimes, joining lists, and serializing values to WEL.
- **JSON functions** - `kb/docs/en/wel/stdlib/json.md` - WEL JSON functions for parsing JSON strings into WEL values, serializing WEL values back to JSON text, and querying a structure with JSONPath.
- **List functions** - `kb/docs/en/wel/stdlib/list.md` - WEL list functions for selecting, transforming, ordering, grouping, and aggregating collections of records in recipe data, with syntax and examples for each.
- **Map functions** - `kb/docs/en/wel/stdlib/map.md` - WEL map functions for reading keys and values, merging maps, picking and removing fields, and flattening nested objects into a single level.
- **Numeric functions** - `kb/docs/en/wel/stdlib/numeric.md` - WEL numeric functions for rounding to integers and decimal places, taking absolute values, and testing for finite, infinite, or NaN numbers.
- **Random functions** - `kb/docs/en/wel/stdlib/random.md` - WEL random functions for generating UUIDs, random integers, floats, hexadecimal strings, and raw bytes for identifiers and idempotency keys.
- **String functions** - `kb/docs/en/wel/stdlib/string.md` - WEL string functions check, clean, extract, and replace text in recipe data, including case conversion, padding, and regular expression matching.
- **Temporal functions** - `kb/docs/en/wel/stdlib/temporal.md` - WEL temporal functions for reading date and time components, calendar and clock arithmetic, period boundaries, time zones, and durations, with examples.
- **Unicode functions** - `kb/docs/en/wel/stdlib/unicode.md` - WEL Unicode functions for grapheme-aware text handling, Unicode normalization, detecting deceptive text, and Japanese kana and width conversion.
