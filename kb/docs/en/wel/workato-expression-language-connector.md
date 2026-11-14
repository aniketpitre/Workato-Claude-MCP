---
url: 'https://docs.workato.com/en/wel/workato-expression-language-connector.md'
description: Use WEL in recipes to reshape data for downstream recipe steps.
---

# Workato Expression Language connector - Transform data action

The **Transform data (code)** action runs a [WEL](/en/wel) expression inside a recipe to reshape data for downstream recipe steps. The **Workato Expression Language** connector provides only this one recipe step.

## Input

| Input field | Description |
| --- | --- |
| Name | Enter a human-readable label for the WEL expression. This label only shows in the recipe editor. |
| Input fields | Define the schema for the data the expression consumes. Add fields manually, or generate them automatically using a JSON sample. |
| Output schema | Define the schema for the data the expression produces. Add fields manually, or generate them automatically using a JSON sample. This schema determines the datapills that appear in downstream steps. |
| WEL snippet source | Select **Define manually** to write the expression directly in this action, or **Use a resource** to reference a snippet file managed in your Workato project. |
| Code | Enter the WEL expression to run using the input data. |
| Locale | Optional. Select the locale to use for engine error messages (the control-plane locale). Defaults to `EN`. |
| Data plane locale | Optional. Use the fields in this section to override the currency, number, and date formatting to use for functions such as `to_local_string`, `to_local_currency`, and `format_date`. This section contains the following input fields: **Currency code**: Enter the ISO 4217 currency code. Defaults to `USD`.; **Currency symbol**: Enter the currency symbol, such as `$`, `€`, or `¥`. Defaults to `$`.; **Decimal separator**: Enter the decimal mark character. Defaults to `.`.; **Thousands separator**: Enter the thousands grouping character. Defaults to `,`.; **List separator**: Enter the separator to use when joining lists to strings. Defaults to `,` .; **Date format**: Enter the `strftime` format for `PlainDate`. Defaults to `%Y-%m-%d`.; **Datetime format**: Enter the `strftime` format for `DateTime`. Defaults to `%Y-%m-%dT%H:%M:%SZ`.; **Plain datetime format**: Enter the `strftime` format for `PlainDateTime`. Defaults to `%Y-%m-%dT%H:%M:%S`.; **Plain time format**: Enter the `strftime` format for `PlainTime`. Defaults to `%H:%M:%S%.f`. These fields are validated as a set rather than accepted as-is: **Currency code** must be a three-letter ISO 4217 code, and **Decimal separator** and **Thousands separator** must differ from each other. |
| Flags | Optional. Use the fields in this section to override engine behavior for this step. This section contains the following input fields: **Mixed precision**: Select how to handle mixed `Decimal` and `Float` arithmetic. `allow` permits it silently, `warn` emits a diagnostic, and `deny` raises `E103`. Defaults to `allow`.; **Stdlib shadowing**: Select how to handle `let` or `fun` shadowing a standard library name. `allow` permits it silently, `warn` emits a diagnostic, and `deny` raises `E009`. Defaults to `warn`.; **Concat with null**: Select whether concatenating with `null` raises an error. `x ++ null` and `concat(x, null)` return `x` when this is `true`, or raise `E205` when it's `false`. Defaults to `false`.; **Nulls in aggregates**: Select whether an aggregate function skips `null` elements. Aggregate functions skip `null` elements when this is `true`, or raise `E101` when it's `false`, the same as any other non-numeric or incomparable element. Defaults to `false`.; **Report all assertion failures in schema guards**: Select whether schema validation reports every failed assertion. Schema validation runs every assertion and reports every failure when this is `true`, or stops at the first failure when it's `false`. Defaults to `false`.; **Number literals as decimal**: Select how the engine types numeric literals and JSON numbers. Every float literal and JSON number becomes a `Decimal` for exact arithmetic when this is `true`, or a `Float` (IEEE 754) when it's `false`. Defaults to `false`. |

> **MIXED PRECISION COERCES BY DEFAULT**
> 
> **Mixed precision** defaults to `allow`, which permits `Decimal` to mix silently with `Float`. Set **Mixed precision** to `deny` to instead raise a catchable `E103` on that arithmetic, which fails the expression unless you catch it with `\|?`.

### How the expression sees your input

The underscore (`_`) is the variable that contains the expression's input values. Each top-level field in **Input fields** becomes a top-level key on `_`. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

The following formulas use input fields `name` (string), `quantity` (integer), and `items` (list of objects):

```wel
_.name           // The value mapped into the name input field
_.quantity * 2   // Double the value of quantity. Arithmetic works directly on integers.
_.items          // The whole list
```

### Configure schemas from sample JSON

Both schema designers can infer a schema from a pasted sample JSON document, which is the recommended way to configure them. Paste a representative sample, let the designer build the field list, then adjust what inference can't see.

Inference gets structure right, such as nesting, lists of objects, and field names. It also correctly tells string, number, and boolean values apart, but it can't express everything the declared schema controls.

> **WHAT SCHEMA INFERENCE GETS WRONG**
> 
> - **Numeric precision**: A sample `19.99` infers a floating-point number, not a Decimal. Set the type to Decimal manually for money and other precision-sensitive fields. The declared type is what the expression receives, and Decimal and Float don't mix in arithmetic (`E103`).
> - **Dates and datetimes**: JSON has no temporal types, so a sample `"2024-01-15"` infers a plain string. Set that type in the designer if the field should reach the expression as a WEL date or timestamp. Otherwise the expression must parse the string itself.
> - **Optional fields**: The designer infers every field present in the sample as a regular field. Mark optional fields yourself. An unmapped optional input field reaches the expression as `null`. A required output field the expression fails to produce raises `E500`.
> - **Empty and null values**: The designer can't infer an item type from an empty list (`[]`) or a field type from `null`. Use a sample with at least one populated element and real values throughout.

You can use the same sample document to test the expression locally. Refer to the [quickstart](/en/wel/quickstart#start-with-the-binary) for details.

### Types aren't converted implicitly

WEL doesn't implicitly convert between types. Operators and functions check operand types and raise an error (typically `E100`, `E101`, or `E102`) when they don't line up. The fix is an explicit type constructor.

A common case is mixing a number into a string with `++`:

```wel
// Error E101: ++ requires both sides to be String
"Age: " ++ _.age

// Fix: Convert the integer first
"Age: " ++ String(_.age) ++ " years"
```

String interpolation is the one place conversion is automatic, other than with the [Mixed precision flag](#input). WEL coerces expressions interpolated inside `"..."` and `"""..."""` to String for you:

```wel
"Order ${_.order_id} has ${length(_.items)} items"
```

> **WEL TRADES BREVITY FOR CERTAINTY**
> 
> Implicit conversion is a common source of hard-to-find bugs in integration scripting. A script can look like it worked while it silently coerced a value into the wrong type. WEL trades some extra verbosity at the boundary for reliable output.

## Output

A WEL formula evaluates to a single value, even when it's built from a chain of `let` bindings and `guard` clauses. Whatever the final `do` produces becomes the action output. WEL has no `return` statement and no implicit wrapping.

This action returns the expression's output value as datapills according to the declared **Output schema**. The shape you declare determines the shape the expression must return:

| Output schema declares | Expression must return |
| --- | --- |
| Multiple named fields, such as `total` and `currency` | A `Map` with `total` and `currency` as keys |
| A list of objects | A `List` of `Map`s, each matching the object's fields |
| A single scalar field | A single scalar value |

A common shaping pattern is to derive a result, then return a map literal whose keys match the output schema:

```wel
let items = _.order.items
              >> filter_by(i ~> i.qty * i.unit_price > 50) do
{
  order_id: _.order.id,
  line_count: length(items),
  total: items >> map_by(i ~> i.qty * i.unit_price) >> sum,
  currency: _.order.currency
}
```

All four become datapills in downstream steps if the output schema declares `order_id`, `line_count`, `total`, and `currency`.

### Matching rules

Workato applies the following rules when matching the expression's result to the output schema:

- **Field names must match exactly**: A schema field `lineCount` isn't the same datapill as an expression key `line_count`. Workato doesn't expose keys present in the result but not in the schema as datapills. They still appear in the raw action output, but downstream steps can't reference them. Keys declared in the schema but missing from the result surface as `null` datapills.
- **Types should match the schema**: Workato attempts standard coercion, such as `Integer` to `String` for a string field, when the result type differs from the declared type. Type-incompatible shapes (a map where the schema expects a list, or the reverse) produce runtime errors. Keep the result shape identical to the schema where you can.
- **The schema is the source of truth for downstream datapills, not for what WEL produces**: WEL evaluates the expression and hands the value back. You are responsible for matching the result to the schema.

### Omit a field with `Skip`

Use `Skip` to omit an optional field from the output entirely rather than emitting it as `null`. WEL strips `Skip` from the result before returning it:

```wel
{
  id: _.id,
  note: if blank?(_.note) then Skip else _.note
}
```

Use this when the field is genuinely absent, such as when omitting an optional API request parameter.

## Related

- [Workato Expression Language](/en/wel): The language this action runs.
- [Quickstart](/en/wel/quickstart): An example showing different WEL workflows.
- [Data types](/en/wel/language/data-types): The 16 WEL data types and when to use each one.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E100`, `E103`, `E202`, `E205`, `E009`, and `E500`.

---
