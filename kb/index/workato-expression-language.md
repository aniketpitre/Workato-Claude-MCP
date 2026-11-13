# Workato Expression Language

26 pages. Paths are relative to the repository root.


## Workato Expression Language

- **Workato Expression Language** - `kb/docs/en/wel.md` - WEL is Workato's transformation language - 245 built-in functions, 16 data types, and exact decimal arithmetic, running natively alongside your recipe.
- **WEL cookbook** - `kb/docs/en/wel/cookbook.md` - Worked WEL examples of common integration problems - joins, grouping, deduplication, CSV and JWT generation, and error-tolerant batch processing.
- **WEL error codes** - `kb/docs/en/wel/errors.md` - Learn what a WEL error code means, whether it's catchable, and how to troubleshoot it.
- **WEL language guide** - `kb/docs/en/wel/language.md` - The syntax and rules behind every WEL expression, the 16 data types, operators and precedence, how expressions are structured, and string formatting.
- **WEL quickstart** - `kb/docs/en/wel/quickstart.md` - Get started with WEL three ways - in the Transform Data action, with an external AI client, or with the wel command-line binary for fast local iteration.
- **WEL standard library** - `kb/docs/en/wel/stdlib.md` - The 245 built-in functions in WEL, spanning 16 categories - strings, lists, maps, temporal, numeric, crypto, encoding, escaping, and conversion.

## Language guide

- **Data types** - `kb/docs/en/wel/language/data-types.md` - The 16 WEL data types, including numbers, text, temporal types, collections, and the Skip marker, and how to choose the right one for each field.
- **Expressions** - `kb/docs/en/wel/language/expressions.md` - How a WEL expression is built, covering the input variable, field access, conditionals, let bindings, guards, lambdas, and named functions in a step.
- **Operators** - `kb/docs/en/wel/language/operators.md` - WEL operators for arithmetic, comparison, logic, concatenation, the pipeline operator, and the two fallback operators, with their precedence.
- **Strings and formatting** - `kb/docs/en/wel/language/strings.md` - WEL string literals, f-string interpolation, and format specifications for controlling padding, alignment, and decimal places in output text.

## Standard library

- **Binary functions** - `kb/docs/en/wel/stdlib/binary.md` - Use WEL binary functions to convert bytes to and from base64, hex, and quoted-printable text, measure byte length, and slice raw byte data from files and digests.
- **Common functions** - `kb/docs/en/wel/stdlib/common.md` - Use WEL common functions to read an element by index or key, measure length, test presence, and inspect a value's type.
- **Conversion functions** - `kb/docs/en/wel/stdlib/conversion.md` - Use WEL conversion functions to cast values to Integer, Decimal, Float, String, Bool, Binary, temporal types, and the Null and Skip sentinels.
- **Crypto functions** - `kb/docs/en/wel/stdlib/crypto.md` - Use WEL crypto functions to hash data, create and verify HMAC signatures, encode and verify JWTs, derive keys with PBKDF2, and encrypt and decrypt data with AES.
- **Deep map functions** - `kb/docs/en/wel/stdlib/deep-map.md` - Use WEL deep map functions to collect values and transform leaf values anywhere inside a deeply nested API response, regardless of depth.
- **Encoding functions** - `kb/docs/en/wel/stdlib/encoding.md` - Use WEL encoding functions to convert between text and bytes in a named character encoding, check convertibility, and encode MIME email headers.
- **Escape functions** - `kb/docs/en/wel/stdlib/escape.md` - Use WEL escape functions to safely embed values in CSV, HTML, XML, JSON, JavaScript, URLs, SOQL, OData, and regular expressions without breaking syntax.
- **Formatting functions** - `kb/docs/en/wel/stdlib/formatting.md` - Use WEL formatting functions to render dates, times, numbers, and currency as display strings, parse datetimes, join lists, and serialize values to WEL.
- **JSON functions** - `kb/docs/en/wel/stdlib/json.md` - Use WEL JSON functions to parse JSON strings into WEL values, serialize WEL values back to JSON text, and query a structure with JSONPath.
- **List functions** - `kb/docs/en/wel/stdlib/list.md` - Use WEL list functions to select, transform, order, group, and aggregate collections of records in recipe data, with syntax and examples for each.
- **Map functions** - `kb/docs/en/wel/stdlib/map.md` - Use WEL map functions to read keys and values, merge maps, pick and remove fields, and flatten nested objects into a single level.
- **Numeric functions** - `kb/docs/en/wel/stdlib/numeric.md` - Use WEL numeric functions to round to integers and decimal places, take absolute values, and test for finite, infinite, or NaN numbers.
- **Random functions** - `kb/docs/en/wel/stdlib/random.md` - Use WEL random functions to generate UUIDs, random integers, floats, hexadecimal strings, and raw bytes for identifiers and idempotency keys.
- **String functions** - `kb/docs/en/wel/stdlib/string.md` - Use WEL string functions to check, clean, extract, and replace text in recipe data, including case conversion, padding, and regular expression matching.
- **Temporal functions** - `kb/docs/en/wel/stdlib/temporal.md` - Use WEL temporal functions to read date and time components, perform calendar and clock arithmetic, find period boundaries, and handle time zones and durations, with examples.
- **Unicode functions** - `kb/docs/en/wel/stdlib/unicode.md` - Use WEL Unicode functions to handle text by grapheme, normalize Unicode text, detect deceptive text, and convert Japanese kana and width.
