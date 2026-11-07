---
url: 'https://docs.workato.com/en/wel/errors.md'
description: >-
  Every WEL error code, what it means, whether you can catch it, and what to do
  about it, covering all 72 codes across four error families in WEL.
---

# WEL error codes

Every WEL error includes a stable code. The code remains the same when the error message changes or is translated. Use the code to search for an error, configure alerts, or include it in a support request.

`_` is the input your expression receives in these examples. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

Error codes are organized into the following categories:

| Category | Range | Description |
| --- | --- | --- |
| [Parse and static analysis](#parse-errors) | `E001`–`E021` | The expression itself is malformed. Not catchable. |
| [Type errors](#type-errors) | `E100`–`E107` | A value isn't the type an operation needs. Catchable. |
| [Runtime errors](#runtime-errors) | `E200`–`E238` | The data is wrong, missing, or out of range. Catchable. |
| [Host errors](#host-errors) | `E300`–`E303` | Something outside the expression failed. Mostly not catchable. |

## Identify the family

The error family identifies the source of the error.

- `E0xx`: The expression is wrong for every input, and it can't be caught, because nothing can recover from a script that won't parse. These surface as you write the expression, not in production.
  
- `E1xx` and `E2xx`: The expression itself is fine, but this particular record doesn't have the shape it expected, such as a missing field or a string where a number belongs. These are the errors most likely to surface in production, often partway through a batch that otherwise runs cleanly. They are catchable, so you can decide what should happen.
  
- `E3xx`: The expression itself is fine, but a host function or another dependency it relies on didn't behave as expected. Catchability differs by code. `E300` is catchable, because a missing optional host value is recoverable. `E301`–`E303` isn't catchable, because the host itself failed.
  

## Catchability

The try-fallback operator `|?` catches a catchable error and returns a fallback instead. A non-catchable error propagates.

```text
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

```text
_.customer.nickname | 'none'      // still raises E104
_.customer.nickname |? 'none'     // returns 'none'
```

Use `|` when the key exists and its value may be `null` or blank, usually with [presence](/en/wel/stdlib/common), which normalizes every kind of absence to `null`:

```text
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
| `E002` | Unexpected token | A syntax error. The caret (`^`) in the message points at the offending token. |
| `E003` | Unterminated string literal | A quote (`'` or `"`) isn't closed. Apostrophes use the same character as single quotes (`'`), so an apostrophe inside a single-quoted string closes it early. |
| `E004` | Invalid number literal | Check for a stray separator or a malformed exponent. |
| `E005` | Invalid binary literal | A `0x"..."` literal contains something other than hex digits. |
| `E006` | Unexpected end of input | Something isn't closed: a bracket (`[`), a parenthesis (`(`), or a `do` with no body. |
| `E007` | Invalid regular expression | The pattern doesn't compile. |
| `E008` | `Binary()` can't contain non-ASCII characters | Use [encode\_string](/en/wel/stdlib/encoding) with an explicit encoding instead. |
| `E009` | Variable is already defined | Rename the inner binding. WEL doesn't allow shadowing. |
| `E010` | Undefined variable | A typo, or a name used outside the `let` that binds it. |
| `E011` | Undefined function | A typo, or a function that doesn't exist. Check the [standard library](/en/wel/stdlib). |
| `E012` | Wrong number of arguments | Check the signature on the function's reference entry. |
| `E013` | Invalid locale configuration | Check the locale settings on the action. |
| `E014` | Expression nesting too deep | Break the expression into `let` bindings. |
| `E015` | Identifier too long | Shorten the name. |
| `E016` | Invalid format specification | Check the format string in an f-string or format function. |
| `E017` | Invalid hostfx reference | Check the host function reference syntax. |
| `E018` | HostFx namespace isn't allowed | The namespace isn't permitted in this context. |
| `E019` | Number literal too long | Reduce the digits, or read the value as a `String` and convert it. |
| `E020` | Invalid constant for constructor | The literal doesn't fit the constructor. `Duration('P1D')` raises this. `Duration` takes clock durations such as `PT24H`. |
| `E021` | Expression is too large | Split the transformation across more than one step. |

## Type errors

WEL raises these errors when a value isn't the type an operation needs. All type errors are catchable.

WEL doesn't automatically coerce arguments to satisfy a function or operator. Convert values explicitly when their input type doesn't match the required type. Refer to [Conversion functions](/en/wel/stdlib/conversion) for details.

| Code | Message | Resolution |
| --- | --- | --- |
| `E100` | Type mismatch: expected one type, got another | Convert explicitly: `String(...)`, `Integer(...)`, `Decimal(...)`. The most common error in WEL. |
| `E101` | Operator isn't supported for these types | Check both operands. A `String` plus a number raises this. Convert one of them. |
| `E102` | Cannot cast one type to another | For example, `Integer('3 items')` won't convert. Clean the value first, or use `|?` to supply a default. |
| `E103` | Mixed precision between `Decimal` and `Float` | Make both sides the same type. Make both `Decimal` for money. Refer to [Data types](/en/wel/language/data-types) for details. |
| `E104` | Cannot access field on this type | The field is missing, or the value isn't a `Map`. Use [has\_key?](/en/wel/stdlib/map#has-key), or `|?` for a default. |
| `E105` | Lambda expects a different number of arguments | Check the lambda's parameters. [filter\_by](/en/wel/stdlib/list#filter-by) on a `Map` passes two, not one. |
| `E106` | Function expects a different number of arguments | Check the signature. |
| `E107` | Lambda can't be used as a value here | A lambda is only valid as an argument to a function that takes one. |

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
| `E202` | Cannot access property of null | A parent field is `null`. Use `|?` or check with [present?](/en/wel/stdlib/common#present). Also raised by an aggregate function when the **Nulls in aggregates** flag is off and the list contains `null`. |
| `E203` | Guard condition failed | A `let ... guard` rejected the input. The message names the condition. |
| `E204` | `one!` expects exactly one element | A lookup matched zero or several records. This error is the function doing its job. Decide which case you have. |
| `E205` | Cannot concatenate with null | Wrap the value: `presence(x) | ''`. |
| `E207` | Cannot compute on an empty list | [avg](/en/wel/stdlib/list#avg) of nothing has no answer. Check the list is non-empty first. |
| `E211` | Value out of range | The message gives the permitted range. |
| `E217` | Required field is missing or blank | Supply the field, or handle its absence. |
| `E231` | Undefined name | The name isn't bound at this point. |
| `E232` | Invalid value: expected one of a set | An option token isn't in the allowed set. The message lists what is allowed. |

### Parsing and conversion

The following errors occur when a value can't be parsed as, or converted to, the expected format:

| Code | Message | Resolution |
| --- | --- | --- |
| `E206` | Invalid or unsupported encoding | Check the name against [encodings()](/en/wel/stdlib/encoding). |
| `E208` | Invalid URL | The value isn't a well-formed URL. |
| `E209` | JSON parse error | The input isn't valid JSON. The message gives the line and column. |
| `E210` | JSON serialize error | The value can't be represented in JSON. |
| `E212` | Invalid date value | The value isn't a date the parser accepts. Supply a `format` option. |
| `E213` | Invalid duration value | Check the ISO 8601 duration form. |
| `E214` | Invalid regular expression | The pattern was built at runtime and doesn't compile. Use [escape\_for\_regex](/en/wel/stdlib/escape) on interpolated values. |
| `E215` | Invalid timezone | Use an IANA name such as `Europe/London`. |
| `E216` | Ambiguous or non-existent datetime | The datetime falls on a daylight-saving boundary. Set `on_gap` or `on_fold` to resolve the ambiguity. |
| `E230` | Invalid time value | The value isn't a time the parser accepts. |
| `E233` | Invalid data for the encoding | The bytes aren't valid in the encoding named. |
| `E234` | Character can't be encoded | The target encoding can't represent this character. Check first with [convertible\_to\_encoding?](/en/wel/stdlib/encoding#convertible-to-encoding). |
| `E235` | Rounding required but mode is `exact` | The value doesn't fit the requested places. Either accept a rounding mode or treat it as bad data. |

### Schema and structure

The following errors occur when a value's structure doesn't match a declared schema, options map, or path expression:

| Code | Message | Resolution |
| --- | --- | --- |
| `E218` | Schema type mismatch on a field | The output doesn't match the declared Output schema. |
| `E219` | Schema assertion failed on a field | A declared constraint wasn't met. |
| `E222` | Invalid map field | An unrecognized key in an options map, usually a typo. WEL validates options rather than ignoring them, so the typo surfaces here instead of silently changing behavior. |
| `E223` | Invalid JSONPath expression | Check the path syntax. |
| `E224` | Unsupported JSONPath feature | Filters, unions, and function extensions are outside the supported subset. Use [deep\_collect\_by](/en/wel/stdlib/deep-map) instead. |
| `E229` | Key collision | Two source keys produced the same output key. Last write wins. This error warns you it happened. |

### Limits

The following errors occur when an expression, name, literal, or the data it processes has exceeded a size limit:

| Code | Message | Resolution |
| --- | --- | --- |
| `E225` | Result too large | An operation would produce more elements than the limit allows. Filter before expanding. |
| `E226` | Recursion limit exceeded | Flatten the expression. |
| `E227` | Memory limit exceeded | Process the data in smaller batches. |
| `E228` | Value nesting too deep | The structure is nested past the limit. Flatten the value before processing it further. |

### Serialization

The following errors occur when a value can't be serialized to a WEL literal:

| Code | Message | Resolution |
| --- | --- | --- |
| `E236` | HostFx values can't be serialized to a WEL literal | Resolve the value before serializing. |
| `E237` | `NaN` can't be serialized to a WEL literal | Filter it out. [present?](/en/wel/stdlib/common#present) treats `NaN` as absent. |
| `E238` | `Skip` inside a `Map` can't be serialized to a WEL literal | Remove the `Skip` before serializing. |

### Other

| Code | Message | Resolution |
| --- | --- | --- |
| `E220` | Cryptographic operation failed | The message gives the cause. A common one is a key shorter than the algorithm requires. `HS256` needs at least 32 bytes. |
| `E221` | A general error | The message carries the detail. |

## Host errors

WEL raises these errors outside the expression.

| Code | Message | Catchable | Resolution |
| --- | --- | --- | --- |
| `E300` | Unresolved hostfx | Yes | A host value wasn't supplied. Catchable, because a missing optional value is recoverable. |
| `E301` | Host function failed | No | The host itself failed, and the failure isn't recoverable inside the expression. |
| `E302` | Invalid hostfx field | No | A field in the host function configuration is invalid. Check the configuration. |
| `E303` | TLV serialize error | No | The value couldn't be serialized to the host's TLV format. |

## Common errors

The following errors commonly result from input that doesn't match the type or shape expected by an expression:

| Code | Usually means |
| --- | --- |
| `E100` | A field arrived as a `String` and is being used as a number, or the reverse |
| `E104` | An optional field is absent from this record |
| `E102` | A value won't convert: an empty string where a number was expected |
| `E103` | A `Decimal` amount met a `Float` somewhere in the arithmetic |

Reduce these errors by converting input fields to their expected types at the start of a transformation and handling optional values explicitly. Use `presence(...) | default` for fields that are genuinely optional. Refer to [Conversion functions](/en/wel/stdlib/conversion) and [Common functions](/en/wel/stdlib/common) for details.

## Related

- [Data types](/en/wel/language/data-types): The data types relevant to these errors.
- [Operators](/en/wel/language/operators): More information about `|` and `|?`.
- [Conversion functions](/en/wel/stdlib/conversion): How to construct each data type.
- [Transform data](/en/wel/workato-expression-language-connector): The action where a failing expression runs.

---
