---
url: 'https://docs.workato.com/en/wel/language/expressions.md'
description: >-
  How a WEL expression is built, covering the input variable, field access,
  conditionals, let bindings, guards, lambdas, and named functions in a step.
---

# Expressions

A WEL step is one expression, with no statements, no assignments, and no return. The expression produces a single value, and that value is the output.

This isn't restrictive, because every construct in WEL produces a value. A conditional produces a value, and a `let` binding produces a value. Each composes anywhere a value is allowed, including inside a [map literal](#build-the-output).

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Input variables

The underscore (`_`) is the **input variable**. It holds the input fields you declared in the [Transform data](/en/wel/workato-expression-language-connector) action.

A period (`.`) reads a field from `_`:

```text
_                    // the whole input
_.order_id           // the order_id field
_.customer.email     // email, inside the customer field
_.line_items         // the whole list
```

`_.order_id` is two parts, not one. `_` names the input, and `.order_id` reads a field from `_`. WEL has no `_.` operator.

Refer to the [Transform data](/en/wel/workato-expression-language-connector) action for how input fields become keys on `_`.

## Access fields

Use a period (`.`) for a plain name, and brackets (`[]`) when the key is computed or isn't a bare identifier:

```text
_.customer.email
_.customer['email']
_['order-id']
```

Reading a key that doesn't exist raises `E104` rather than producing `null`. This prevents a typo in a field name from silently propagating a missing value. Use `|?` to mark a field as genuinely optional:

```text
_.customer.nickname |? 'none'
```

Refer to [Operators](/en/wel/language/operators) for the difference between `|`, which handles null values, and `|?`, which catches errors.

## Build the output

Most transformations are a map literal whose values are expressions:

```text
{
  order_id: upper(_.order_id),
  email: lower(trim(_.customer.email)),
  item_count: count(_.line_items)
}
```

Write keys as bare identifiers. Values can be anything, such as a field, a call, a pipeline, a conditional, or a nested map.

## Conditionals

`if ... then ... else ...` produces a value.

| Formula | Result |
| --- | --- |
| `if 5 > 3 then 'yes' else 'no'` | `yes` |
| `if 1 > 2 then 'a' else if 3 > 2 then 'b' else 'c'` | `b` |

Use `else if` to chain more than two branches. The whole conditional is a value, so it goes directly into the output:

```text
{
  tier: if _.total > 1000 then 'gold'
        else if _.total > 100 then 'silver'
        else 'standard'
}
```

## Name intermediate values

`let name = value do body` binds a name for use in the body.

| Formula | Result |
| --- | --- |
| `let x = 10 do x * 2` | `20` |
| `let a = 1, b = 2 do a + b` | `3` |

Separate several bindings with commas. Later bindings can use earlier ones.

Use `let` to reuse a value more than once:

```text
let parts = _.results >> partition_by(r ~> r.status == 'ok')
do {
  succeeded: parts >> at(0),
  failed: parts >> at(1)
}
```

`let` also helps when an expression has grown too long to read. A named step in the middle of a pipeline is often clearer than a single unbroken chain, and the same technique fixes `E014` (nesting too deep).

> **WEL DOESN'T ALLOW SHADOWING**
> 
> Re-binding a name that is already in scope raises `E009`. This prevents an inner binding from silently capturing an outer one. Use a different name to resolve the error.

## Guards

A guard tests a condition and raises `E203` when the condition is false.

```text
let total = _.total
guard total > 0
do total
```

An optional `else` supplies a custom message:

```text
let total = _.total
guard total > 0 else 'total must be positive'
do total
```

Guards are for input you are unwilling to process. A negative total isn't something to default away. It means the payload is wrong, and a job that fails loudly is better than an invoice that goes out wrong. Compare with `|?`, which is for absences you expect.

## Lambdas

A lambda is an inline function, written with `~>`. The higher-order [list functions](/en/wel/stdlib/list) take lambdas as arguments.

| Formula | Result |
| --- | --- |
| `[1,2,3] >> map_by(x ~> x * 2)` | `[2, 4, 6]` |
| `[1,2,3] >> map_with_index_by((x, i) ~> x + i)` | `[1, 3, 5]` |

Choose any name for the parameter before `~>`. Wrap two or more parameters in parentheses (`()`).

A lambda is only valid as an argument to a function that takes one. Using it as a standalone value raises `E107`.

> **\-> AND => ARE NOT LAMBDA ARROWS**
> 
> WEL exclusively uses `~>` for lambdas. Writing `x -> x * 2` or `x => x * 2` raises a parse error. This is the most common mistake for people and AI more familiar with other languages, which often use `->` or `=>` for lambdas. Refer to the [WEL kit](/en/wel/quickstart#start-with-ai) to provide an AI agent the necessary context to work with WEL.

## Named functions

`fun name = lambda do body` binds a lambda to a name, so you can reuse the same logic in several places without writing it out again.

| Formula | Result |
| --- | --- |
| `fun double = x ~> x * 2 do double(21)` | `42` |

Pass a named function to a higher-order function like any other lambda:

| Formula | Result |
| --- | --- |
| `fun is_open = o ~> o.status == 'open' do [{status: 'open'}, {status: 'closed'}] >> filter_by(is_open)` | `[{status: "open"}]` |

Each `fun` has its own `do`, and later definitions can call earlier ones:

```text
fun net = li ~> Decimal(li.unit_price) * li.qty do
fun taxed = li ~> net(li) * Decimal('1.20') do
_.line_items >> map_by(taxed) >> sum
```

Use `fun` when a rule appears more than once.

## Put it together

```text
let items = _.line_items
guard count(items) > 0 else 'order has no line items'
do {
  order_id: upper(_.order_id),
  item_count: count(items),
  total: items >> map_by(li ~> Decimal(li.unit_price) * li.qty) >> sum,
  tier: if count(items) > 10 then 'bulk' else 'standard'
}
```

The preceding block is one expression. A binding, a guard, a map literal, a pipeline, and a conditional each produce a value, and those values compose into the value the step returns.

## Related

- [Operators](/en/wel/language/operators): Precedence, pipelines, and fallback operators.
- [Data types](/en/wel/language/data-types): The data types these expressions produce.
- [Standard library](/en/wel/stdlib): Every WEL function.
- [Error codes](/en/wel/errors): Troubleshoot errors such as `E009`, `E014`, `E104`, `E107`, and `E203`.

---
