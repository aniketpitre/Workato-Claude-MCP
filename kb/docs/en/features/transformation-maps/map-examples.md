---
url: 'https://docs.workato.com/en/features/transformation-maps/map-examples.md'
description: >-
  Example transformation maps that reshape a list, aggregate a list by a key,
  chain formulas, flatten a nested array, and join two arrays.
---

# Example transformation maps

The following examples show complete transformation maps for common integration patterns. Add null handling to these examples for production data that may contain missing fields.

- [Reshape a list](#reshape-a-list): Change the shape of items in a list.
- [Aggregate with group-by](#aggregate-with-group-by): Group a list by a key and compute a count or total for each group instead of copying each row.
- [Chain a transformation with filter and sort](#chain-a-transformation-with-filter-and-sort): Break a multi-stage transformation into separate nodes.
- [Flatten a nested array](#flatten-a-nested-array): Produce one row for each element of an array nested inside another array.
- [Join two arrays](#join-two-arrays): Correlate two lists on a shared key.

## Reshape a list

Use this pattern when an inbound system sends a list of items in one shape and the target system requires each item in a different shape, such as different field names and a computed value.

In this example, an e-commerce order webhook sends order lines with `sku`, `qty`, and `unit_price`. The ERP requires items with `product_code`, `quantity`, and a per-line `amount`.

![Reshape a list](/assets/example-1-reshape-a-list.bOyipLJ8.png)_Reshape a list_

**Input schema**

This example uses the following JSON sample to generate an input schema:

```json
{
  "order_id": "SO-1001",
  "lines": [
    { "sku": "A-100", "qty": 2, "unit_price": 9.5 },
    { "sku": "B-220", "qty": 1, "unit_price": 40 }
  ]
}
```

**Output schema**

This example uses the following JSON sample to generate an output schema:

```json
{
  "order_number": "SO-1001",
  "items": [
    { "product_code": "A-100", "quantity": 2, "amount": 19.0 },
    { "product_code": "B-220", "quantity": 1, "amount": 40.0 }
  ]
}
```

**total**

The `total` node uses the following formula:

```text
_.unit_price * _.qty
```

This reshape doesn't require a formula for the whole list. `order_id`, `sku`, and `qty` pass through unchanged under new names, so only the computed `amount` field needs a formula.

The `total` node multiplies the quantity by the unit price to produce the per-line total. It returns a single scalar value, so the node doesn't require an output schema. An `Integer` multiplied by a `Number` returns a `Number`.

## Aggregate with group-by

Use this pattern when you require a summary rather than a row-for-row copy, such as grouping a list by a key and computing a count or total for each group.

In this example, the same order lines carry a `category`. The target requires one row for each category with the number of lines and the summed amount.

![Aggregate with group-by](/assets/example-2-aggregate-with-group-by.CK7qv3SK.png)_Aggregate with group-by_

**Input schema**

This example uses the following JSON sample to generate an input schema:

```json
{
  "order_id": "SO-1001",
  "lines": [
    { "sku": "A-100", "category": "hardware", "qty": 2, "unit_price": 9.5 },
    { "sku": "B-220", "category": "hardware", "qty": 1, "unit_price": 40 },
    { "sku": "C-050", "category": "service", "qty": 3, "unit_price": 15 }
  ]
}
```

**Output schema**

This example uses the following JSON sample to generate an output schema:

```json
{
  "order_number": "SO-1001",
  "totals_by_category": [
    { "category": "hardware", "line_count": 2, "total_amount": 59.0 },
    { "category": "service", "line_count": 1, "total_amount": 45.0 }
  ]
}
```

**summarize by category**

The `summarize by category` node uses the following formula:

```text
{
  totals_by_category: _.lines
    >> group_by(line ~> line.category)
    >> entries
    >> map_by(g ~> {
         category: g.key,
         line_count: count(g.value),
         total_amount: g.value >> map_by(l ~> l.qty * l.unit_price) >> sum
       })
}
```

`order_id` connects directly to `order_number` unchanged, the same as a one-to-one rename. Only `lines` feeds the `summarize by category` node, since it's the only field the aggregation needs.

The `summarize by category` node does the aggregation in three stages. `group_by` collects the lines into one bucket for each category, which produces a map rather than a list. `entries` restates that map as a list of key and value pairs so you can iterate over it. `map_by` then returns one object for each pair, containing the category name, the number of lines in the group, and the sum of the line totals.

The node returns a list of objects, so it requires an output schema. Refer to [When to define an output schema](/en/features/transformation-maps/create-map#when-to-define-an-output-schema).

## Chain a transformation with filter and sort

Use this pattern when a transformation runs in stages. Chaining keeps each stage in its own node, so you can read the transformation from the canvas and test each stage on its own.

In this example, order lines carry a `sku`, `qty`, and `unit_price`. The map computes a per-line total, filters out lines below a threshold, and sorts what remains by total, each stage in its own node.

![Chain a transformation with filter and sort](/assets/example-3-chain-aggregate-filter-sort.oklgwVPZ.png)_Chain a transformation with filter and sort_

**Input schema**

This example uses the following JSON sample to generate an input schema:

```json
{
  "order_id": "SO-1001",
  "lines": [
    { "sku": "A-100", "qty": 2, "unit_price": 9.5 },
    { "sku": "B-220", "qty": 1, "unit_price": 40 },
    { "sku": "C-050", "qty": 3, "unit_price": 15 },
    { "sku": "D-410", "qty": 2, "unit_price": 60 }
  ]
}
```

**Output schema**

This example uses the following JSON sample to generate an output schema:

```json
{
  "high_value_lines": [
    { "sku": "D-410", "amount": 120.0 },
    { "sku": "C-050", "amount": 45.0 },
    { "sku": "B-220", "amount": 40.0 }
  ]
}
```

**line totals**

The `line_totals` node uses the following formula:

```text
{
  lines: _.lines
  >> map_by(l ~> {
   sku: l.sku,
   amount: l.qty * l.unit_price
  })
}
```

**filter**

The `filter` node uses the following formula:

```text
{
  filtered: _.line_totals_lines >> filter_by(t ~> t.amount >= 20)
}
```

**sort**

The `sort` node uses the following formula:

```text
{
  high_value_lines: _.filter_filtered >> sort_by(f ~> 0 - f.amount)
}
```

The map uses three nodes, each handling one stage:

- `line_totals` computes a per-line total by multiplying `qty` by `unit_price`.
- `filter` keeps only lines with a total of 20 or more.
- `sort` orders the remaining lines from highest to lowest total.

Each node references the previous node's output by the upstream formula name, such as `_.line_totals_lines` and `_.filter_filtered`. Every node in the chain returns a list, so each one requires its own output schema. Refer to [When to define an output schema](/en/features/transformation-maps/create-map#when-to-define-an-output-schema).

Four lines produce four totals, the filter drops `A-100` at 19, and the sort puts `D-410` at 120 ahead of `C-050` at 45 and `B-220` at 40.

You can write all three stages as a single formula in one node, which produces the same result and requires only one output schema. Chain the stages instead to test each one on its own, or when a single formula becomes difficult to read.

## Flatten a nested array

Use this pattern when the values you need are in an array nested inside another array. You can't access inner arrays directly, so the transformation starts at the top-level array and flattens down to the inner elements. Refer to [Arrays](/en/features/transformation-maps/create-map#arrays) for more information.

In this example, `lines` is a list of objects, and each line carries its own `units` list of objects. The target requires one row for each unit, with the `sku` of the line it came from.

![Flatten a nested array](/assets/example-4-flatten-a-nested-array.DNKsN3iA.png)_Flatten a nested array_

**Input schema**

This example uses the following JSON sample to generate an input schema:

```json
{
  "order_id": "SO-1001",
  "lines": [
    {
      "sku": "A-100",
      "units": [
        { "serial_number": "SN-1", "condition": "new" },
        { "serial_number": "SN-2", "condition": "refurbished" }
      ]
    },
    {
      "sku": "B-220",
      "units": [
        { "serial_number": "SN-3", "condition": "new" }
      ]
    }
  ]
}
```

**Output schema**

This example uses the following JSON sample to generate an output schema:

```json
{
  "units": [
    { "sku": "A-100", "serial_number": "SN-1", "condition": "new" },
    { "sku": "A-100", "serial_number": "SN-2", "condition": "refurbished" },
    { "sku": "B-220", "serial_number": "SN-3", "condition": "new" }
  ]
}
```

**flatten units**

The `flatten units` node uses the following formula:

```text
{
  units: _.lines
    >> map_by(l ~> l.units >> map_by(u ~> {
         sku: l.sku,
         serial_number: u.serial_number,
         condition: u.condition
       }))
    >> flatten
}
```

The `flatten units` node walks each line, then walks that line's `units` list, and flattens the result into a single list. Two lines containing three units in total produce three rows.

The formula reads `sku` from the parent line while it processes each unit, which is how every row keeps a value from the line it came from. Without this, the node still flattens, but the result contains only the unit fields, with no indication of which line each unit came from.

The node returns a list of objects, so it requires an output schema. Refer to [When to define an output schema](/en/features/transformation-maps/create-map#when-to-define-an-output-schema).

## Join two arrays

Use this pattern when the payload contains two lists that you must correlate on a shared key, such as order lines and a product catalog.

In this example, `lines` carries a `sku` and a quantity, and `products` carries the name and price for each `sku`. The target requires one enriched item for each line.

![Join two arrays](/assets/example-5-join-two-arrays.CV6F-c0Z.png)_Join two arrays_

**Input schema**

This example uses the following JSON sample to generate an input schema:

```json
{
  "lines": [
    { "sku": "A-100", "qty": 2 },
    { "sku": "B-220", "qty": 1 }
  ],
  "products": [
    { "sku": "A-100", "name": "Widget", "unit_price": 9.5 },
    { "sku": "B-220", "name": "Gadget", "unit_price": 40 }
  ]
}
```

**Output schema**

This example uses the following JSON sample to generate an output schema:

```json
{
  "items": [
    { "sku": "A-100", "name": "Widget", "qty": 2, "amount": 19.0 },
    { "sku": "B-220", "name": "Gadget", "qty": 1, "amount": 40.0 }
  ]
}
```

**join products**

The `join products` node uses the following formula:

```text
let catalog = _.products >> map_by(p ~> [p.sku, p]) >> from_pairs do

{
  items: _.lines >> map_by(l ~>
    let p = catalog[l.sku] do
      {
        sku: l.sku,
        name: p.name,
        qty: l.qty,
        amount: l.qty * p.unit_price
      })
}
```

The `join products` node builds a lookup from `products` once, keyed by `sku`, before it processes any lines. Each line then reads its product directly from that lookup, rather than searching the product list again for every line. The node returns one item for each line, combining the quantity from the line with the name of the matched product and an amount computed from its price.

The node returns a list of objects, so it requires an output schema. Refer to [When to define an output schema](/en/features/transformation-maps/create-map#when-to-define-an-output-schema).

Every `sku` in `lines` must exist in `products`. The mapping fails with a `Cannot access field` error when it looks up a key that doesn't exist, so add a fallback if the source data can contain unmatched keys. If `products` can contain the same `sku` more than once, the lookup keeps the last entry for that key and discards the earlier ones.

---
