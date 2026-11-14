---
url: 'https://docs.workato.com/en/wel/errors.md'
description: >-
  Learn what a WEL error code means, whether it's catchable, and how to
  troubleshoot it.
---

# WEL error codes

WEL errors include a stable code. The code remains the same when the error message changes or is translated. Use the code to search for an error, configure alerts, or include it in a support request.

`_` is the input your expression receives in these examples. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

Error codes are organized into the following categories:

| Category | Range | Description |
| --- | --- | --- |
| [Parse and static analysis](#parse-errors) | `E001`–`E027` | The expression itself is malformed. Not catchable. |
| [Type errors](#type-errors) | `E100`–`E108` | A value isn't the type an operation needs. Catchable. |
| [Runtime errors](#runtime-errors) | `E200`–`E230` | The data is wrong, missing, or out of range. Catchable. |
| [Host errors](#host-errors) | `E300`–`E301` | An explicit `HostFx` call was unresolved or failed. Catchable. |
| [Stops](#stop-errors) | `E400`–`E401`, `E450` | The host stops the whole operation. Not catchable. |
| [Schema errors](#schema-errors) | `E500`–`E503` | The expression's output doesn't match the schema the host declared for it. Not caught by `|?`, since it runs after the expression evaluates. |

## Identify the family

The error family identifies the source of the error.

- `E0xx`: The expression is wrong for every input, and it can't be caught, because nothing can recover from a script that won't parse. These surface as you write the expression, not in production.
  
- `E1xx` and `E2xx`: The expression is valid, but this particular record doesn't have the shape it expected, such as a missing field or a string where a number belongs. These are the errors most likely to surface in production, often partway through a batch that otherwise runs cleanly. They are catchable, so you can decide what should happen.
  
- `E3xx`: The expression is valid, but an explicit `HostFx` call either wasn't resolved or failed. Both are catchable, so you can decide what should happen when a host integration doesn't supply what the expression asked for.
  
- `E4xx`: The host stopped the operation because a limit was reached or the host service failed. None of these errors are catchable.
  
- `E5xx`: The host declared a schema that the expression's result failed to follow. These errors occur after the expression runs and checks the result against the schema, so `|?` doesn't catch them. Refer to [Schema errors](#schema-errors).
  

## Catchability

The try-fallback operator `|?` catches a catchable error and returns a fallback instead. A non-catchable error propagates.

```wel
_.customer.email |? 'unknown'
Integer(_.qty) |? 0
```

### Compare `|?` and `|`

The distinction between `|?` and `|` matters most of all, and a mix-up here is a common source of confusion.

| Operator | Handles | Doesn't handle |
| --- | --- | --- |
| `|` | A `null` value | An error |
| `|?` | An error | N/A |

Reading a field that doesn't exist raises `E104`. It doesn't produce `null`, so `|` won't save you:

```wel
_.customer.nickname | 'none'      // still raises E104
_.customer.nickname |? 'none'     // returns 'none'
```

Use `|` when the key exists and its value may be `null` or blank, usually with [presence](/en/wel/stdlib/common), which normalizes every kind of absence to `null`:

```wel
presence(_.display_name) | 'Unknown'
```

Use `|?` when the shape itself may differ.

> **A FALLBACK IS A DECISION, NOT A FIX**
> 
> `|? 0` on a currency field means a malformed amount silently becomes zero, and the job reports success. That is sometimes right and sometimes an invoice that quietly goes out wrong.
> 
> Use a fallback when the absence is expected and the default is genuinely correct. Let the error propagate when it isn't. A failed job is visible, and a wrong number isn't.

## Parse and static analysis errors

WEL raises these errors before evaluation begins. They occur for every input and aren't catchable.

| Code | Message | Resolution |
| --- | --- | --- |
| `E001` | Script requires a newer WEL version than the runtime supports | The expression uses a feature this engine doesn't have. Check the engine version. |
| `E002` | Unexpected token | A caret (`^`) in the message points at the offending token. Fix the syntax error at that point. |
| `E003` | Unterminated string literal | Close the quote (`'` or `"`), escape an apostrophe with `\'` or switch to double quotes, or use `\n`/`\r` or a triple-quoted form (`'''...'''` or `"""..."""`) to include a line break directly. |
| `E004` | Invalid number literal | Check for a stray separator or a malformed exponent. |
| `E005` | Invalid binary literal | Keep a `0x"..."` literal to hex digits only. |
| `E006` | Unexpected end of input | Check for a missing close: A bracket (`[`), a parenthesis (`(`), or a `do` with no body. |
| `E007` | Invalid regular expression | Ensure the pattern follows ECMAScript regular expression syntax. This error is for patterns written directly in the expression. Refer to `E213` when the pattern is built from data at runtime. |
| `E008` | `Binary()` can't contain non-ASCII characters | Use [encode\_string](/en/wel/stdlib/encoding) with an explicit encoding instead. |
| `E009` | Variable is already defined | Rename the inner binding. WEL doesn't allow shadowing. |
| `E010` | Undefined variable | Check for a typo, or a name used outside the `let` that binds it. |
| `E011` | Undefined function | Check the [standard library](/en/wel/stdlib) for the function name, or correct the typo. |
| `E012` | Wrong number of arguments | Check the signature on the function's reference entry. |
| `E013` | Invalid locale configuration | Check the locale settings on the action. |
| `E014` | Expression nesting too deep | Break the expression into `let` bindings. |
| `E015` | Identifier too long | Shorten the name to 64 Unicode scalar values or fewer after NFC normalization. |
| `E016` | Invalid format specification | Check the format string in an f-string or format function. |
| `E017` | Invalid hostfx reference | Check the host function reference syntax. |
| `E018` | HostFx namespace isn't allowed | Check which namespaces are permitted in this context. |
| `E019` | Number literal too long | Reduce the digits, or read the value as a `String` and convert it. |
| `E020` | Invalid constant for constructor | Match the literal to what the constructor accepts. For example, `Duration('P1D')` raises this because `Duration` takes clock durations such as `PT24H`. This is also raised when an `Integer` or `Decimal` literal or constant exceeds the 1024-byte magnitude limit. Refer to [Data types](/en/wel/language/data-types) for more information. |
| `E021` | Expression is too large | Split the expression across additional steps. |
| `E022` | Key collision in a literal | Remove or rename the duplicate key. |
| `E023` | `Skip` can't be called or piped into | Write `Skip`, not `Skip()`, and don't use it as the left side of `|`, `|?`, or `>>`. |
| `E024` | Character isn't allowed at this identifier position | Check for a stray symbol or a character copied from outside the editor. |

`E025`, `E026`, and `E027` are **warnings**. They report alongside the result rather than stopping the expression:

| Code | Message | Resolution |
| --- | --- | --- |
| `E025` | Identifier contains an uncommon character | The name includes a zero-width character (such as ZWNJ/ZWJ) or a compatibility character changed by NFKC normalization, such as full width or mathematical-bold letters. Rename using plain letters, digits, and underscores to silence the warning. |
| `E026` | Identifier contains a mixed-script confusable | The name mixes letters from scripts that look alike, such as Latin and Cyrillic, using a curated confusable character (for example, Cyrillic `а` in `аdmin`). Keep a single script per identifier. |
| `E027` | Identifiers are visually confusable | Names active in the same scope share a curated visual skeleton, such as Latin `a` and Cyrillic `а`. Rename them so they're visually distinct. |

## Type errors

WEL raises these errors when a value isn't the type an operation needs. All type errors are catchable.

WEL doesn't automatically coerce arguments to satisfy a function or operator. Convert values explicitly when their input type doesn't match the required type. Refer to [Conversion functions](/en/wel/stdlib/conversion) for details.

| Code | Message | Resolution |
| --- | --- | --- |
| `E100` | Type mismatch: expected one type, got another | Convert the type explicitly, or ensure `and`, `or`, `not`, and an `if` condition only receive `Bool` (or `Null`/`Skip`). |
| `E101` | Operator isn't supported for these types | Check both operands and convert one of them. |
| `E102` | Cannot cast one type to another | The value isn't in a format the constructor accepts. Clean the value, or use `|?` to supply a default. |
| `E103` | Mixed precision between `Decimal` and `Float` | Make both sides the same type. Refer to [Data types](/en/wel/language/data-types) for more information. |
| `E104` | Cannot access field on this type | The field is missing, or the value isn't a `Map`. Use [has\_key?](/en/wel/stdlib/map#has-key), or `|?` for a default. |
| `E105` | Lambda expects a different number of arguments | Check the lambda's parameters against what the higher-order function passes it. For example, [filter\_by](/en/wel/stdlib/list#filter-by) on a `Map` passes two arguments, the key and the value, not one. |
| `E106` | Function expects a different number of arguments | Check the signature. |
| `E107` | Lambda can't be used as a value here | Pass the lambda to a function that takes one. The lambda is only valid as an argument, not a standalone value. |
| `E108` | Operator isn't supported for this type | Remove the operator, or convert the operand to a type it supports. |

### `E103` is about money

`Decimal` and `Float` won't mix. A silent mix would destroy the exactness that makes `Decimal` worth using. The result is approximate when a `Float` enters the calculation, and nothing downstream can tell.

The fix is typically to make the other operand a `Decimal` rather than to convert the `Decimal` to a `Float` when you hit `E103` on a total.

> **RECIPES ENABLE MIXED PRECISION BY DEFAULT**
> 
> The [Transform data](/en/wel/workato-expression-language-connector) action has a **Mixed precision** field which configures whether `Decimal` and `Float` can mix. This field defaults to `allow`, which means `E103` doesn't raise for recipe actions unless you set the field to `deny`.

## Runtime errors

WEL raises these errors during evaluation when an input value can't be processed. All runtime errors are catchable.

### Data shape and access

The following errors occur when the data doesn't have the shape or value an operation expects:

| Code | Message | Resolution |
| --- | --- | --- |
| `E200` | Undefined or indeterminate arithmetic result | Guard the divisor to prevent dividing by zero or a similarly undefined operation. |
| `E201` | Index out of bounds | The list is shorter than expected. Use [first](/en/wel/stdlib/list#first), [last](/en/wel/stdlib/list#last), or `|?`. |
| `E202` | Cannot access property of null | A parent field is `null`. Use `|?` or check with [present?](/en/wel/stdlib/common#present). |
| `E203` | Guard condition failed | Check the guard-site variables and values the message lists to see what was rejected, then fix the input or the condition. |
| `E204` | `one!` expects exactly one element | Use a different function, such as [first](/en/wel/stdlib/list#first), [last](/en/wel/stdlib/list#last), or `|?`, if zero or multiple matches is a valid outcome. `one!` is strict by design. It raises this instead of silently picking one record when the lookup matches zero or several. |
| `E205` | Cannot concatenate with null | Wrap the value: `presence(x) | ''`. |
| `E207` | Cannot compute on an empty list | Ensure the list isn't empty. [avg](/en/wel/stdlib/list#avg) of nothing has no answer. |
| `E224` | Undefined name | Check for a typo, or a name used before it's bound. |
| `E225` | Invalid value: expected one of a set | Use one of the allowed option tokens listed by the error message. |

### Parsing and formats

The following errors occur when a value can't be parsed as, or converted to, the expected format:

| Code | Message | Resolution |
| --- | --- | --- |
| `E206` | Invalid or unsupported encoding | Check the name against [encodings()](/en/wel/stdlib/encoding). |
| `E208` | Invalid URL | Check that the value is a well-formed URL. |
| `E209` | JSON parse error | Check the line and column the message gives. The input text isn't valid JSON. A structurally valid object with a duplicate key raises `E223` instead. |
| `E210` | JSON serialize error | Convert the value to a JSON-representable type before serializing it. |
| `E212` | Temporal constraint violation | The date, time, or duration components are each individually valid but don't fit together. For example, a month has too many days or an offset doesn't match the named time zone. A component that's invalid on its own, such as `hour: 200`, raises `E211` instead. |
| `E213` | Invalid regular expression | Use [escape\_for\_regex](/en/wel/stdlib/escape) on interpolated values. Unlike `E007`'s static pattern, this one is built at runtime, such as with an f-string or concatenation, so an unescaped special character in the data can break the pattern for some records and not others. |
| `E214` | Invalid timezone | Use an IANA name such as `Europe/London`. |
| `E215` | Ambiguous or non-existent datetime | Set `on_gap` or `on_fold` to resolve the ambiguity. The datetime falls on a daylight-saving boundary. |
| `E226` | Invalid data for the encoding | Check that the bytes are valid in the encoding the message names. |
| `E227` | Character can't be encoded | Check with [convertible\_to\_encoding?](/en/wel/stdlib/encoding#convertible-to-encoding) whether the target encoding can represent the character. |
| `E228` | Rounding required but mode is `exact` | Accept a rounding mode, or treat it as bad data. The value doesn't fit the requested places. |

### Options, paths, and limits

The following errors occur when an options map, a path expression, or a size limit rejects the input:

| Code | Message | Resolution |
| --- | --- | --- |
| `E211` | Value out of range | Check the message for the permitted range. For example, `^` with a negative exponent on an `Integer` or `Decimal` base, or an `Integer`/`Decimal` magnitude over 1024 bytes computed at runtime. |
| `E218` | Invalid map field | A recognized key in an options map holds a value of the wrong type or shape. Check the message for the field name and the type it expects. An unrecognized key raises `E225` instead. |
| `E219` | Invalid JSONPath expression | Check the path syntax. |
| `E220` | Unsupported JSONPath feature | Filters, unions, and function extensions are outside the supported subset. Use [deep\_collect\_by](/en/wel/stdlib/deep-map) instead. |
| `E221` | Result too large | An operation would produce more elements than the limit allows. Filter before expanding. |
| `E222` | Value nesting too deep | Flatten the value before processing it further. |
| `E223` | Key collision | Remove or rename the duplicate key in the source data. The message names the function that found two entries for the same key while building a `Map` or parsing an object. |
| `E229` | Invalid JSON Pointer syntax | Check the pointer against [RFC 6901](https://www.rfc-editor.org/rfc/rfc6901) syntax. The pointer must start with a leading `/`, encode a literal `/` as `~1` and `~` as `~0` within a token, and use non-negative list indices with no leading zeros. |
| `E230` | JSON Pointer resolution failed | The pointer is well-formed, but the path doesn't exist. This can be caused by a missing key, an out-of-bounds index, or a segment that walks into a non-container value. Use [json\_pointer](/en/wel/stdlib/json#json-pointer)'s `|?` support for an optional path. |

### Cryptography and other

| Code | Message | Resolution |
| --- | --- | --- |
| `E216` | Cryptographic operation failed | This is often caused by a key that's shorter than the algorithm requires: `HS256` needs at least 32 bytes, `HS384` at least 48, `HS512` at least 64. Check the message for the exact cause. |
| `E217` | A general error | This is a generic failure code, check the message for details. |

## Host errors

WEL raises these errors when an explicit `HostFx` call either wasn't resolved or failed. Both are catchable.

| Code | Message | Resolution |
| --- | --- | --- |
| `E300` | Unresolved hostfx | A host value wasn't supplied for the namespace and key the expression referenced. Use `|?` to supply a fallback. |
| `E301` | HostFx call failed | The host attempted the call and it failed in a way the expression can recover from. Use `|?` to supply a fallback, or check the host integration's configuration. |

## Stops

WEL raises these errors when the host stops the whole operation rather than letting the expression continue. None of these are catchable: There's nothing left of the evaluation to recover into.

| Code | Message | Resolution |
| --- | --- | --- |
| `E400` | Evaluation depth exceeded | Flatten the expression, or break it into `let` bindings across more than one step. |
| `E401` | Memory limit exceeded | Process the data in smaller batches. |
| `E450` | Host function failed | The host itself failed in a way the expression can't recover from, as opposed to `E301`'s recoverable call failure. Check the host integration or connection. |

## Schema errors

A host can declare a schema for the expression's result, such as the [Transform data](/en/wel/workato-expression-language-connector) action's **Output schema**. Schema validation runs after the expression evaluates, checking the result against that schema. Because it's a separate step from evaluation, `|?` doesn't see these errors. They don't propagate through the expression at all.

| Code | Message | Resolution |
| --- | --- | --- |
| `E500` | Required field is missing or blank | A required schema field received no value, `null`, `Skip`, or a blank value with no default. Supply the field, or mark it optional in the schema. |
| `E501` | Value cannot be coerced to the field's declared type | The expression's output doesn't match the schema's declared type for that field, and WEL couldn't convert it. Check the field's actual type against the schema. |
| `E502` | A schema assertion failed or couldn't be evaluated | Check the `wel_assertions` entry on the schema. |
| `E503` | Schema definition nests deeper than the limit | Flatten the schema definition. |

## Common errors

The following errors commonly result from input that doesn't match the type or shape expected by an expression:

| Code | Usually means |
| --- | --- |
| `E100` | A field arrived as a `String` and is being used as a number, or the reverse. |
| `E104` | An optional field is absent from this record. |
| `E102` | A value won't convert, such as an empty string where a number was expected. |
| `E103` | A `Decimal` amount met a `Float` somewhere in the arithmetic. |

Reduce these errors by converting input fields to their expected types at the start of a transformation and handling optional values explicitly. Use `presence(...) | default` for fields that are genuinely optional. Refer to [Conversion functions](/en/wel/stdlib/conversion) and [Common functions](/en/wel/stdlib/common) for details.

## Related

- [Data types](/en/wel/language/data-types): The data types relevant to these errors.
- [Operators](/en/wel/language/operators): More information about `|` and `|?`.
- [Conversion functions](/en/wel/stdlib/conversion): How to construct each data type.
- [Transform data](/en/wel/workato-expression-language-connector): The action where a failing expression runs, including the **Output schema** it uses for schema validation.

---
