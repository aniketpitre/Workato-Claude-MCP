---
url: 'https://docs.workato.com/en/wel/stdlib/list.md'
description: >-
  Use WEL list functions to select, transform, order, group, and aggregate
  collections of records in recipe data, with syntax and examples for each.
---

# List functions

List functions work on ordered collections. Most integration work is list work. A webhook delivers an array of records, an API returns pages of results, and a destination system expects a different shape, a different order, or a single aggregated number.

`_` is the input your expression receives in these examples. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

## Call a list function

Call a function directly, or pipe a value into it with `>>`:

```wel
count(_.line_items)
_.line_items >> count
```

List functions chain well, and the pipe form is what makes a multi-step transformation readable:

```wel
_.orders >> filter_by(o ~> o.status == 'open') >> map_by(o ~> o.id)
```

### Lambdas

Many list functions take a lambda, a small inline function written with `~>`:

```wel
_.orders >> filter_by(order ~> order.total > 100)
```

Choose any name for the parameter before `~>`. It refers to one element at a time. Wrap two or more parameters in parentheses (`()`):

```wel
_.items >> map_with_index_by((item, index) ~> f"{index + 1}. {item.name}")
```

> **\-> AND => ARE NOT LAMBDA ARROWS**
> 
> WEL exclusively uses `~>` for lambdas. Writing `x -> x * 2` or `x => x * 2` raises a parse error. This is the most common mistake for people and AI more familiar with other languages, which often use `->` or `=>` for lambdas. Refer to the [WEL kit](/en/wel/quickstart#start-with-ai) to provide an AI agent the necessary context to work with WEL.

A predicate lambda, such as the one `filter_by` or `find_by` takes, must return a `Boolean`, `null`, or `Skip`. `null` and `Skip` count as false. Any other return type raises `E100`.

## Inspect a list

The following functions read a list without changing it:

### `count`

Returns the number of elements. Raises `E100` for a `String` or `Map`. Use [length](/en/wel/stdlib/common#length) for those instead.

```wel
count(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to measure. |

Count the elements of a non-empty list

The following example counts the elements of a non-empty list:

**Formula**

```wel
count(['SO-1', 'SO-2', 'SO-3'])
```

**Output**

```wel
3
```

Count the elements of an empty list

The following example counts the elements of an empty list:

**Formula**

```wel
count([])
```

**Output**

```wel
0
```

### `first`

Returns the first element, or `null` if the list is empty.

```wel
first(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |

Get the first element of a list

The following example gets the first element of a list:

**Formula**

```wel
first(['pending', 'shipped'])
```

**Output**

```text
pending
```

An empty list has no first element

The following example returns `null` for an empty list:

**Formula**

```wel
first([])
```

**Output**

```wel
null
```

### `last`

Returns the last element, or `null` if the list is empty.

```wel
last(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |

Get the last element of a list

The following example gets the last element of a list:

**Formula**

```wel
last(['pending', 'shipped'])
```

**Output**

```text
shipped
```

### `at`

Returns the element at a zero-based index. A negative index counts back from the end. `at` also works on a [Map](/en/wel/stdlib/map#at), where it takes a `String` key instead of an index.

An index outside the list raises `E201`. Use `first` or `last` for just an end. Use `find_by` to search for an element rather than a position.

```wel
at(list, index)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |
| index | Zero-based position. Negative counts from the end. |

Get the element at a positive index

The following example gets the element at index 0:

**Formula**

```wel
at(['pending', 'shipped', 'closed'], 0)
```

**Output**

```text
pending
```

Get the element at a negative index

The following example gets the last element using a negative index:

**Formula**

```wel
at(['pending', 'shipped', 'closed'], -1)
```

**Output**

```text
closed
```

### `one!`

Returns the single element of a one-element list, and raises `E204` for any other length.

Use it as an assertion. `one!` turns "zero or many" into a job that fails loudly instead of a transformation that quietly proceeds with the wrong record when a lookup must match exactly one record.

```wel
one!(list)
```

| Parameter | Description |
| --- | --- |
| list | A list expected to hold exactly one element. |

Extract the single element of a one-element list

The following example extracts the single element of a one-element list:

**Formula**

```wel
one!(['SO-1001'])
```

**Output**

```text
SO-1001
```

## Test a list

The following functions answer a question about a list rather than returning a new one:

### `all?`

Returns `true` if every element satisfies the predicate. An empty list returns `true`.

```wel
all?(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to test. |
| predicate | A lambda returning a `Boolean` for each element. |

Test whether every element matches a predicate

The following example tests whether every element is `'open'`:

**Formula**

```wel
['open', 'open'] >> all?(s ~> s == 'open')
```

**Output**

```wel
true
```

### `any?`

Returns `true` if at least one element satisfies the predicate.

```wel
any?(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to test. |
| predicate | A lambda returning a `Boolean` for each element. |

Test whether any element exceeds a threshold

The following example tests whether any element is greater than 100:

**Formula**

```wel
[199, 42, 8] >> any?(n ~> n > 100)
```

**Output**

```wel
true
```

### `find_by`

Returns the first element satisfying the predicate, or `null` if none does.

```wel
find_by(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to search. |
| predicate | A lambda returning a `Boolean` for each element. |

Find a record by a field value

The following example finds the first record whose SKU matches:

**Formula**

```wel
[{id: 1, sku: 'WID-1'}, {id: 2, sku: 'GAD-7'}] >> find_by(r ~> r.sku == 'GAD-7')
```

**Output**

```wel
{id: 2, sku: "GAD-7"}
```

### `find_first_index`

Returns the zero-based index of the first element satisfying the predicate, or `-1` if none does.

```wel
find_first_index(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to search. |
| predicate | A lambda returning a `Boolean` for each element. |

Find the index of a matching element

The following example finds the index of the element equal to `'c'`:

**Formula**

```wel
['a', 'b', 'c'] >> find_first_index(s ~> s == 'c')
```

**Output**

```wel
2
```

No element matches the predicate

The following example returns `-1` when no element matches:

**Formula**

```wel
['a', 'b'] >> find_first_index(s ~> s == 'z')
```

**Output**

```wel
-1
```

## Select elements

The following functions return a shorter list built from the original:

### `filter_by`

Keeps the elements for which the predicate returns `true`.

Also accepts a `Map`, in which case the lambda receives two parameters, the key and the value. The result is a `Map` too.

```wel
filter_by(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list or map to filter. |
| predicate | A lambda returning a `Boolean`. |

Filter a list to values above a threshold

The following example keeps only the elements greater than 2:

**Formula**

```wel
[1, 2, 3, 4] >> filter_by(n ~> n > 2)
```

**Output**

```wel
[3, 4]
```

### `take`

Returns the first `count` elements, or the last `count` elements if `count` is negative. A request for more than the list holds returns the whole list rather than raising an error.

```wel
take(list, count)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |
| count | The number of elements to return. Negative takes from the end. Raises `E211` if `count` is outside the 64-bit integer range. |

Take elements from the start

The following example takes the first 2 elements:

**Formula**

```wel
take(['a', 'b', 'c', 'd'], 2)
```

**Output**

```wel
["a", "b"]
```

Take elements from the end

The following example takes the last 2 elements using a negative count:

**Formula**

```wel
take(['a', 'b', 'c', 'd'], -2)
```

**Output**

```wel
["c", "d"]
```

### `drop`

Removes the first `count` elements, or the last `count` elements if `count` is negative.

```wel
drop(list, count)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |
| count | The number of elements to remove. Negative removes from the end. Raises `E211` if `count` is outside the 64-bit integer range. |

Remove elements from the start

The following example removes the first 2 elements:

**Formula**

```wel
drop(['a', 'b', 'c', 'd'], 2)
```

**Output**

```wel
["c", "d"]
```

### `compact`

Removes `null` values.

Useful directly after a `map_by` that produces a value only for some elements, and for cleaning optional fields out of an inbound payload.

```wel
compact(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to clean. |

Remove null values from a list

The following example removes the `null` value from a list:

**Formula**

```wel
compact(['a', null, 'b'])
```

**Output**

```wel
["a", "b"]
```

### `unique`

Removes duplicates, keeping the first occurrence of each value in its original position. Elements count as duplicates when WEL's [comparison](/en/wel/language/operators#comparison) rules treat them as equal:

| Behavior | Example |
| --- | --- |
| Numbers and strings don't equate. | `1 == '1'` returns `false`. |
| `Integer` compares across type with `Float` and `Decimal`. `Float` and `Decimal` don't mix. | `1 == 1.0` and `1 == Decimal('1')` return `true`. `1.5 == Decimal('1.5')` raises `E103`. |
| Comparison examines value, not construction. | `[1, 2] == range(1, 2)` returns `true`. `{a: 1} == from_entries([{key: 'a', value: 1}])` returns `true`. |
| Strings that [normalize](/en/wel/stdlib/unicode#unicode-normalize) differently aren't equal. | `é` stored as one character and `e` followed by a combining accent render identically but aren't equal. Use [unicode\_compare](/en/wel/stdlib/unicode) to compare text from different systems. |
| String comparison is case-sensitive. | `'A' == 'a'` returns `false`. |

```wel
unique(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to deduplicate. Raises `E103` if `list` mixes `Float` and `Decimal` elements. |

Remove duplicate values from a list

The following example removes the duplicate value while keeping the first occurrence:

**Formula**

```wel
unique(['WID-1', 'GAD-7', 'WID-1'])
```

**Output**

```wel
["WID-1", "GAD-7"]
```

### `unique_by`

Removes duplicates by a key function, keeping the first element for each key.

Use it with records, where two entries are "the same" because they share an identifier even though the whole objects differ.

```wel
unique_by(list, key)
```

| Parameter | Description |
| --- | --- |
| list | The list to deduplicate. |
| key | A lambda returning the value to compare on. Raises `E100` if the lambda returns `Skip` for an element. |

Deduplicate records by a key field

The following example keeps the first record for each SKU:

**Formula**

```wel
[{sku: 'WID-1'}, {sku: 'WID-1'}] >> unique_by(r ~> r.sku)
```

**Output**

```wel
[{sku: "WID-1"}]
```

### Use case: Keep the valid records from a webhook batch

A webhook delivers a batch in which some records are missing an email address and one identifier repeats. Use list functions to keep one record per identifier and drop the ones with no email to deliver to:

**Input**

```json
{
  "contacts": [
    {"id": "C-1", "email": "nur@example.com"},
    {"id": "C-2", "email": null},
    {"id": "C-1", "email": "nur@example.com"},
    {"id": "C-3", "email": "dana@example.com"}
  ]
}
```

**Formula**

```wel
_.contacts
  >> unique_by(c ~> c.id)
  >> filter_by(c ~> present?(c.email))
  >> map_by(c ~> c.email)
```

**Output**

```json
["nur@example.com", "dana@example.com"]
```

`unique_by` runs before `filter_by` so the duplicate is removed on identity, not on whether it happened to have an email address.

## Transform elements

The following functions return a list of the same length, or reshape the structure:

### `map_by`

Applies a lambda to every element and returns the results. `map_by` omits elements that return `Skip`, so the function can filter and transform in the same pass.

```wel
map_by(list, transform)
```

| Parameter | Description |
| --- | --- |
| list | The list to transform. `map_by` only accepts a `List`. A `Map` input raises `E100`. |
| transform | A lambda returning the new value for each element. |

Double each element of a list

The following example doubles each element of a list:

**Formula**

```wel
[1, 2, 3] >> map_by(n ~> n * 2)
```

**Output**

```wel
[2, 4, 6]
```

### `map_with_index_by`

Applies a two-parameter lambda receiving the element and its zero-based index. `map_with_index_by` omits elements that return `Skip`, so the function can filter and transform in the same pass.

```wel
map_with_index_by(list, transform)
```

| Parameter | Description |
| --- | --- |
| list | The list to transform. |
| transform | A lambda taking `(element, index)`. |

Number each element of a list

The following example numbers each element using its index:

**Formula**

```wel
['a', 'b'] >> map_with_index_by((s, i) ~> f"{i + 1}. {s}")
```

**Output**

```wel
["1. a", "2. b"]
```

### `flatten`

Flattens one level of nesting, and only one level. A list nested two deep keeps its inner list, so call `flatten` again to go further.

```wel
flatten(list)
```

| Parameter | Description |
| --- | --- |
| list | The list of lists to flatten. |

Flatten a list of lists

The following example flattens a list of lists by one level:

**Formula**

```wel
flatten([[1, 2], [3]])
```

**Output**

```wel
[1, 2, 3]
```

Flatten only removes one level of nesting

The following example shows that a list nested two levels deep keeps its inner list:

**Formula**

```wel
[[1, 2], [3, [4]]] >> flatten
```

**Output**

```wel
[1, 2, 3, [4]]
```

### `zip`

Pairs elements from two lists into two-element lists. The shorter list determines the length.

```wel
zip(first, second)
```

| Parameter | Description |
| --- | --- |
| first | The first list. |
| second | The second list. |

Pair two lists of equal length

The following example pairs two lists of equal length:

**Formula**

```wel
zip(['sku', 'qty'], ['WID-1', 3])
```

**Output**

```wel
[["sku", "WID-1"], ["qty", 3]]
```

The shorter list determines the result length

The following example shows the shorter list determining the result length:

**Formula**

```wel
zip(['a', 'b', 'c'], [1])
```

**Output**

```wel
[["a", 1]]
```

### `reverse`

Reverses the order of elements.

```wel
reverse(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to reverse. |

Reverse the order of a list

The following example reverses the order of a list:

**Formula**

```wel
reverse(['a', 'b', 'c'])
```

**Output**

```wel
["c", "b", "a"]
```

## Order a list

The following functions sort a list, ascending and stable:

### `sort`

Sorts in ascending order. The sort is stable, so elements that compare equal keep their original relative order. Compares strings by code point, not locale rules.

```wel
sort(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to sort. Raises `E101` if the list contains elements of incomparable types, such as a number and a string, or a `null` element. Raises `E103` if the list mixes `Float` and `Decimal` elements. |

Sort a list in ascending order

The following example sorts a list in ascending order:

**Formula**

```wel
sort([3, 1, 2])
```

**Output**

```wel
[1, 2, 3]
```

Sort in descending order by reversing after sort

The following example sorts ascending, then reverses to get descending order:

**Formula**

```wel
[3, 1, 2] >> sort >> reverse
```

**Output**

```wel
[3, 2, 1]
```

### `sort_by`

Sorts by a key function, ascending and stable.

There is no descending variant. Pipe the result into `reverse` for descending order.

```wel
sort_by(list, key)
```

| Parameter | Description |
| --- | --- |
| list | The list to sort. |
| key | A lambda returning the value to sort on. Comparing incomparable types, such as a number and a string, or a `null` value, raises `E101`. Mixing `Float` and `Decimal` values raises `E103`. |

Sort records by a field

The following example sorts records by their `n` field:

**Formula**

```wel
[{n: 'b'}, {n: 'a'}] >> sort_by(r ~> r.n)
```

**Output**

```wel
[{n: "a"}, {n: "b"}]
```

### Use case: Take the three largest orders

A report needs the three largest orders pulled from a batch. Sort ascending, reverse, then take from the top:

**Input**

```json
{
  "orders": [
    {"id": "SO-1", "amount": 120},
    {"id": "SO-2", "amount": 940},
    {"id": "SO-3", "amount": 310},
    {"id": "SO-4", "amount": 75}
  ]
}
```

**Formula**

```wel
_.orders
  >> sort_by(o ~> o.amount)
  >> reverse
  >> take(3)
  >> map_by(o ~> o.id)
```

**Output**

```json
["SO-2", "SO-3", "SO-1"]
```

## Group and split

The following functions divide a list into groups or two buckets, based on a key or a predicate:

### `group_by`

Groups elements into a `Map` keyed by the result of the key function. Each value is the list of elements sharing that key.

```wel
group_by(list, key)
```

| Parameter | Description |
| --- | --- |
| list | The list to group. |
| key | A lambda returning the grouping key. Must return a `String`, `Integer`, or `Bool`. Any other type, including `null`, raises `E100`. Keys that stringify the same, such as `1` and `'1'`, collide into a single group. |

Group records by a key field

The following example groups records by their SKU:

**Formula**

```wel
[{sku: 'WID-1', q: 1}, {sku: 'GAD-7', q: 2}, {sku: 'WID-1', q: 5}] >> group_by(r ~> r.sku)
```

**Output**

```wel
{"WID-1": [{sku: "WID-1", q: 1}, {sku: "WID-1", q: 5}], "GAD-7": [{sku: "GAD-7", q: 2}]}
```

### `partition_by`

Partitions a list into two nested lists. Index `0` contains a list of elements that match the predicate, and index `1` contains a list of elements that don't. Read the two inner lists with `at(0)` and `at(1)`.

```wel
partition_by(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to split. |
| predicate | A lambda returning a `Boolean`. |

Split a list by a predicate

The following example splits a list into matching and non-matching elements:

**Formula**

```wel
[1, 2, 3, 4] >> partition_by(n ~> n > 2)
```

**Output**

```wel
[[3, 4], [1, 2]]
```

Read the matching elements from the result

The following example reads only the matching elements from the partitioned result:

**Formula**

```wel
[1, 2, 3, 4] >> partition_by(n ~> n > 2) >> at(0)
```

**Output**

```wel
[3, 4]
```

### Use case: Split a batch result into succeeded and failed

A bulk API returns one record per row with a per-row status. Use `partition_by` to split them, so the failures can be routed to a retry path while the successes continue:

**Input**

```json
{
  "results": [
    {"id": "A", "status": "ok"},
    {"id": "B", "status": "error"},
    {"id": "C", "status": "ok"}
  ]
}
```

**Formula**

```wel
let parts = _.results >> partition_by(r ~> r.status == 'ok')
do {
  succeeded: parts >> at(0) >> map_by(r ~> r.id),
  failed: parts >> at(1) >> map_by(r ~> r.id)
}
```

**Output**

```json
{"succeeded": ["A", "C"], "failed": ["B"]}
```

`let … do` binds the split once so the list is partitioned a single time rather than twice.

## Aggregate

The following functions reduce a list to one value.

Null handling for `sum`, `avg`, `min`, and `max` depends on the **Nulls in aggregates** flag:

- Off (the default): A `null` element raises `E101`.
- On: `null` elements are skipped. A list of only `null` values is then treated the same as an empty list.

### `sum`

Adds the numeric elements. An empty list sums to `0`. A non-numeric element raises `E101`. Raises `E103` if the list mixes `Float` and `Decimal` elements.

```wel
sum(list)
```

| Parameter | Description |
| --- | --- |
| list | A list of numbers. |

Sum a list of floats

The following example sums a list of floats:

**Formula**

```wel
sum([12.50, 99.00])
```

**Output**

```wel
111.5
```

Sum a list of decimals to preserve scale

The following example sums a list of `Decimal` values, preserving the original scale:

**Formula**

```wel
sum([Decimal('12.50'), Decimal('99.00')])
```

**Output**

```wel
111.50
```

An empty list sums to zero

The following example sums an empty list:

**Formula**

```wel
sum([])
```

**Output**

```wel
0
```

> **SUM MONEY AS DECIMAL, NOT AS FLOAT**
> 
> The `sum([12.50, 99.00])` and `sum([Decimal('12.50'), Decimal('99.00')])` examples run the same arithmetic on different types. `12.50` is a `Float`, so the total is `111.5` and the scale is gone. `Decimal('12.50')` is exact, so the total is `111.50`. It stays a currency amount through every later step.
> 
> Schema inference in the Transform Data action doesn't produce `Decimal` for money. Refer to the [Transform data](/en/wel/workato-expression-language-connector) action for how to declare it.

### `avg`

Returns the mean of the numeric elements. A non-numeric element raises `E101`. An empty list raises `E207`, because there is no meaningful average of nothing.

```wel
avg(list)
```

| Parameter | Description |
| --- | --- |
| list | A list of numbers. |

Average a list of numbers

The following example averages a list of numbers:

**Formula**

```wel
avg([10, 20, 30])
```

**Output**

```wel
20
```

### `min`

Returns the smallest element. Works on strings as well as numbers. `min` returns the first tied element when more than one shares the smallest value. An empty list raises `E207`.

```wel
min(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to reduce. Comparing elements of incomparable types, such as a string and a number, raises `E101`. Mixing `Float` and `Decimal` elements raises `E103`. |

Find the smallest number in a list

The following example finds the smallest number in a list:

**Formula**

```wel
min([5, 2, 9])
```

**Output**

```wel
2
```

### `max`

Returns the largest element. Works on strings as well as numbers. `max` returns the first tied element when more than one shares the largest value. An empty list raises `E207`.

```wel
max(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to reduce. Comparing elements of incomparable types, such as a string and a number, raises `E101`. Mixing `Float` and `Decimal` elements raises `E103`. |

Find the largest number in a list

The following example finds the largest number in a list:

**Formula**

```wel
max([5, 2, 9])
```

**Output**

```wel
9
```

Find the largest string in a list

The following example finds the largest string in a list:

**Formula**

```wel
max(['apple', 'pear'])
```

**Output**

```text
pear
```

### `reduce_by`

Folds a list into a single value using an accumulator.

Use it when the result isn't a plain total, such as building a `Map`, concatenating, or carrying state across elements. Use `sum` and `avg` instead for a straight sum or average, because their names say what they mean.

```wel
reduce_by(list, initial, accumulate)
```

| Parameter | Description |
| --- | --- |
| list | The list to fold. |
| initial | The starting value of the accumulator. |
| accumulate | A lambda taking `(accumulator, element)` and returning the new accumulator. Raises `E100` if it returns `Skip`. |

Fold a list into a total

The following example folds a list into a running total:

**Formula**

```wel
[1, 2, 3] >> reduce_by(0, (acc, n) ~> acc + n)
```

**Output**

```wel
6
```

### Use case: Total an order by SKU

Line items arrive one row per shipment, so the same SKU appears more than once. Use list functions to group them and total the quantity for each:

**Input**

```json
{
  "line_items": [
    {"sku": "WID-1", "qty": 3},
    {"sku": "GAD-7", "qty": 1},
    {"sku": "WID-1", "qty": 2}
  ]
}
```

**Formula**

```wel
_.line_items
  >> group_by(li ~> li.sku)
  >> entries
  >> map_by(e ~> {key: e.key, value: e.value >> map_by(r ~> r.qty) >> sum})
  >> from_entries
```

**Output**

```json
{"WID-1": 5, "GAD-7": 1}
```

`group_by` produces a `Map` of lists. `entries` turns it into a list of `{key, value}` pairs so each group can be summed. `from_entries` then puts it back together. Refer to [Map functions](/en/wel/stdlib/map) for both.

## Generate a list

The following functions produce a new list rather than transforming an existing one:

### `range`

Builds a list of integers from start to end, inclusive. The list descends when start is greater than end. Raises `E211` if the range would hold more than 10,000,000 elements, and `E100` if `start` or `end` isn't an `Integer`.

```wel
range(start, end)
```

| Parameter | Description |
| --- | --- |
| start | First integer, included. |
| end | Last integer, included. |

Build an ascending range

The following example builds an ascending range of integers:

**Formula**

```wel
range(1, 5)
```

**Output**

```wel
[1, 2, 3, 4, 5]
```

Build a descending range

The following example builds a descending range when the start is greater than the end:

**Formula**

```wel
range(5, 1)
```

**Output**

```wel
[5, 4, 3, 2, 1]
```

### `random_choice`

Returns one randomly selected element.

The result differs on every evaluation, so don't use it for anything a later step must reproduce. Refer to [Random functions](/en/wel/stdlib/random) for other ways to generate a value that doesn't need to repeat.

```wel
random_choice(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to pick from. Raises `E207` for an empty list. |

## Related

- [Map functions](/en/wel/stdlib/map): Work with the `Map` that `group_by` returns.
- [Deep map functions](/en/wel/stdlib/deep-map): Reach through deeply nested structures.
- [Operators](/en/wel/language/operators): More information about the pipeline family of operators.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E101`, `E201`, `E204`, and `E207`.

---
