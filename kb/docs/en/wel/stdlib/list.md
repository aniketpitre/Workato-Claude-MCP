---
url: 'https://docs.workato.com/en/wel/stdlib/list.md'
description: >-
  WEL list functions for selecting, transforming, ordering, grouping, and
  aggregating collections of records in recipe data, with syntax and examples
  for each.
---

# List functions

List functions work on ordered collections. Most integration work is list work. A webhook delivers an array of records, an API returns pages of results, and a destination system expects a different shape, a different order, or a single aggregated number.

`_` is the input your expression receives in these examples. Refer to [Input variables](/en/wel/language/expressions#input-variable) for more information.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

## Call a list function

Call a function directly, or pipe a value into it with `>>`:

```text
count(_.line_items)
_.line_items >> count
```

List functions chain well, and the pipe form is what makes a multi-step transformation readable:

```text
_.orders >> filter_by(o ~> o.status == 'open') >> map_by(o ~> o.id)
```

### Lambdas

Many list functions take a lambda, a small inline function written with `~>`:

```text
_.orders >> filter_by(order ~> order.total > 100)
```

Choose any name for the parameter before `~>`. It refers to one element at a time. Wrap two or more parameters in parentheses (`()`):

```text
_.items >> map_with_index_by((item, index) ~> f"{index + 1}. {item.name}")
```

> **\-> AND => ARE NOT LAMBDA ARROWS**
> 
> WEL exclusively uses `~>` for lambdas. Writing `x -> x * 2` or `x => x * 2` raises a parse error. This is the most common mistake for people and AI more familiar with other languages, which often use `->` or `=>` for lambdas. Refer to the [WEL kit](/en/wel/quickstart#start-with-ai) to provide an AI agent the necessary context to work with WEL.

## Inspect a list

The following functions read a list without changing it:

### `count`

Returns the number of elements.

```text
count(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to measure. |

Count the elements of a non-empty list

The following example counts the elements of a non-empty list:

**Formula**

```text
count(['SO-1', 'SO-2', 'SO-3'])
```

**Output**

```text
3
```

Count the elements of an empty list

The following example counts the elements of an empty list:

**Formula**

```text
count([])
```

**Output**

```text
0
```

### `first`

Returns the first element, or `null` if the list is empty.

```text
first(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |

Get the first element of a list

The following example gets the first element of a list:

**Formula**

```text
first(['pending', 'shipped'])
```

**Output**

```text
pending
```

An empty list has no first element

The following example returns `null` for an empty list:

**Formula**

```text
first([])
```

**Output**

```text
null
```

### `last`

Returns the last element, or `null` if the list is empty.

```text
last(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |

Get the last element of a list

The following example gets the last element of a list:

**Formula**

```text
last(['pending', 'shipped'])
```

**Output**

```text
shipped
```

### `at`

Returns the element at a zero-based index. A negative index counts back from the end.

An index outside the list raises `E201`. Use `first` or `last` for just an end. Use `find_by` to search for an element rather than a position.

```text
at(list, index)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |
| index | Zero-based position. Negative counts from the end. |

Get the element at a positive index

The following example gets the element at index 0:

**Formula**

```text
at(['pending', 'shipped', 'closed'], 0)
```

**Output**

```text
pending
```

Get the element at a negative index

The following example gets the last element using a negative index:

**Formula**

```text
at(['pending', 'shipped', 'closed'], -1)
```

**Output**

```text
closed
```

### `one!`

Returns the single element of a one-element list, and raises `E204` for any other length.

Use it as an assertion. `one!` turns "zero or many" into a job that fails loudly instead of a transformation that quietly proceeds with the wrong record when a lookup must match exactly one record.

```text
one!(list)
```

| Parameter | Description |
| --- | --- |
| list | A list expected to hold exactly one element. |

Extract the single element of a one-element list

The following example extracts the single element of a one-element list:

**Formula**

```text
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

```text
all?(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to test. |
| predicate | A lambda returning a `Boolean` for each element. |

Test whether every element matches a predicate

The following example tests whether every element is `'open'`:

**Formula**

```text
['open', 'open'] >> all?(s ~> s == 'open')
```

**Output**

```text
true
```

### `any?`

Returns `true` if at least one element satisfies the predicate.

```text
any?(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to test. |
| predicate | A lambda returning a `Boolean` for each element. |

Test whether any element exceeds a threshold

The following example tests whether any element is greater than 100:

**Formula**

```text
[199, 42, 8] >> any?(n ~> n > 100)
```

**Output**

```text
true
```

### `find_by`

Returns the first element satisfying the predicate, or `null` if none does.

```text
find_by(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to search. |
| predicate | A lambda returning a `Boolean` for each element. |

Find a record by a field value

The following example finds the first record whose SKU matches:

**Formula**

```text
[{id: 1, sku: 'WID-1'}, {id: 2, sku: 'GAD-7'}] >> find_by(r ~> r.sku == 'GAD-7')
```

**Output**

```text
{id: 2, sku: "GAD-7"}
```

### `find_first_index`

Returns the zero-based index of the first element satisfying the predicate, or `-1` if none does.

```text
find_first_index(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to search. |
| predicate | A lambda returning a `Boolean` for each element. |

Find the index of a matching element

The following example finds the index of the element equal to `'c'`:

**Formula**

```text
['a', 'b', 'c'] >> find_first_index(s ~> s == 'c')
```

**Output**

```text
2
```

No element matches the predicate

The following example returns `-1` when no element matches:

**Formula**

```text
['a', 'b'] >> find_first_index(s ~> s == 'z')
```

**Output**

```text
-1
```

## Select elements

The following functions return a shorter list built from the original:

### `filter_by`

Keeps the elements for which the predicate returns `true`.

Also accepts a `Map`, in which case the lambda receives two parameters, the key and the value. The result is a `Map` too.

```text
filter_by(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list or map to filter. |
| predicate | A lambda returning a `Boolean`. |

Filter a list to values above a threshold

The following example keeps only the elements greater than 2:

**Formula**

```text
[1, 2, 3, 4] >> filter_by(n ~> n > 2)
```

**Output**

```text
[3, 4]
```

### `take`

Returns the first `count` elements, or the last `count` elements if `count` is negative. A request for more than the list holds returns the whole list rather than raising an error.

```text
take(list, count)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |
| count | How many elements. Negative takes from the end. |

Take elements from the start

The following example takes the first 2 elements:

**Formula**

```text
take(['a', 'b', 'c', 'd'], 2)
```

**Output**

```text
["a", "b"]
```

Take elements from the end

The following example takes the last 2 elements using a negative count:

**Formula**

```text
take(['a', 'b', 'c', 'd'], -2)
```

**Output**

```text
["c", "d"]
```

### `drop`

Removes the first `count` elements, or the last `count` elements if `count` is negative.

```text
drop(list, count)
```

| Parameter | Description |
| --- | --- |
| list | The list to read from. |
| count | How many elements to remove. Negative removes from the end. |

Remove elements from the start

The following example removes the first 2 elements:

**Formula**

```text
drop(['a', 'b', 'c', 'd'], 2)
```

**Output**

```text
["c", "d"]
```

### `compact`

Removes `null` and `Skip` values.

Useful directly after a `map_by` that produces a value only for some elements, and for cleaning optional fields out of an inbound payload.

```text
compact(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to clean. |

Remove null values from a list

The following example removes the `null` value from a list:

**Formula**

```text
compact(['a', null, 'b'])
```

**Output**

```text
["a", "b"]
```

### `unique`

Removes duplicates, keeping the first occurrence of each value in its original position.

```text
unique(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to deduplicate. |

Remove duplicate values from a list

The following example removes the duplicate value while keeping the first occurrence:

**Formula**

```text
unique(['WID-1', 'GAD-7', 'WID-1'])
```

**Output**

```text
["WID-1", "GAD-7"]
```

### `unique_by`

Removes duplicates by a key function, keeping the first element for each key.

Use it with records, where two entries are "the same" because they share an identifier even though the whole objects differ.

```text
unique_by(list, key)
```

| Parameter | Description |
| --- | --- |
| list | The list to deduplicate. |
| key | A lambda returning the value to compare on. |

Deduplicate records by a key field

The following example keeps the first record for each SKU:

**Formula**

```text
[{sku: 'WID-1'}, {sku: 'WID-1'}] >> unique_by(r ~> r.sku)
```

**Output**

```text
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

```text
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

Applies a lambda to every element and returns the results.

An element whose lambda returns `Skip` is omitted, so `map_by` can filter and transform in the same pass.

```text
map_by(list, transform)
```

| Parameter | Description |
| --- | --- |
| list | The list to transform. |
| transform | A lambda returning the new value for each element. |

Double each element of a list

The following example doubles each element of a list:

**Formula**

```text
[1, 2, 3] >> map_by(n ~> n * 2)
```

**Output**

```text
[2, 4, 6]
```

### `map_with_index_by`

Applies a two-parameter lambda receiving the element and its zero-based index.

```text
map_with_index_by(list, transform)
```

| Parameter | Description |
| --- | --- |
| list | The list to transform. |
| transform | A lambda taking `(element, index)`. |

Number each element of a list

The following example numbers each element using its index:

**Formula**

```text
['a', 'b'] >> map_with_index_by((s, i) ~> f"{i + 1}. {s}")
```

**Output**

```text
["1. a", "2. b"]
```

### `flatten`

Flattens one level of nesting, and only one level. A list nested two deep keeps its inner list, so call `flatten` again to go further.

```text
flatten(list)
```

| Parameter | Description |
| --- | --- |
| list | The list of lists to flatten. |

Flatten a list of lists

The following example flattens a list of lists by one level:

**Formula**

```text
flatten([[1, 2], [3]])
```

**Output**

```text
[1, 2, 3]
```

Flatten only removes one level of nesting

The following example shows that a list nested two levels deep keeps its inner list:

**Formula**

```text
[[1, 2], [3, [4]]] >> flatten
```

**Output**

```text
[1, 2, 3, [4]]
```

### `zip`

Pairs elements from two lists into two-element lists. The shorter list determines the length.

```text
zip(first, second)
```

| Parameter | Description |
| --- | --- |
| first | The first list. |
| second | The second list. |

Pair two lists of equal length

The following example pairs two lists of equal length:

**Formula**

```text
zip(['sku', 'qty'], ['WID-1', 3])
```

**Output**

```text
[["sku", "WID-1"], ["qty", 3]]
```

The shorter list determines the result length

The following example shows the shorter list determining the result length:

**Formula**

```text
zip(['a', 'b', 'c'], [1])
```

**Output**

```text
[["a", 1]]
```

### `reverse`

Reverses the order of elements.

```text
reverse(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to reverse. |

Reverse the order of a list

The following example reverses the order of a list:

**Formula**

```text
reverse(['a', 'b', 'c'])
```

**Output**

```text
["c", "b", "a"]
```

## Order a list

The following functions sort a list, ascending and stable:

### `sort`

Sorts in ascending order. The sort is stable, so elements that compare equal keep their original relative order.

```text
sort(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to sort. |

Sort a list in ascending order

The following example sorts a list in ascending order:

**Formula**

```text
sort([3, 1, 2])
```

**Output**

```text
[1, 2, 3]
```

Sort in descending order by reversing after sort

The following example sorts ascending, then reverses to get descending order:

**Formula**

```text
[3, 1, 2] >> sort >> reverse
```

**Output**

```text
[3, 2, 1]
```

### `sort_by`

Sorts by a key function, ascending and stable.

There is no descending variant. Pipe the result into `reverse` for descending order.

```text
sort_by(list, key)
```

| Parameter | Description |
| --- | --- |
| list | The list to sort. |
| key | A lambda returning the value to sort on. |

Sort records by a field

The following example sorts records by their `n` field:

**Formula**

```text
[{n: 'b'}, {n: 'a'}] >> sort_by(r ~> r.n)
```

**Output**

```text
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

```text
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

```text
group_by(list, key)
```

| Parameter | Description |
| --- | --- |
| list | The list to group. |
| key | A lambda returning the grouping key. |

Group records by a key field

The following example groups records by their SKU:

**Formula**

```text
[{sku: 'WID-1', q: 1}, {sku: 'GAD-7', q: 2}, {sku: 'WID-1', q: 5}] >> group_by(r ~> r.sku)
```

**Output**

```text
{"WID-1": [{sku: "WID-1", q: 1}, {sku: "WID-1", q: 5}], "GAD-7": [{sku: "GAD-7", q: 2}]}
```

### `partition_by`

Splits a list into exactly two lists: the elements matching the predicate, then the elements that don't.

The result is a two-element list, so read it with `at(0)` and `at(1)`.

```text
partition_by(list, predicate)
```

| Parameter | Description |
| --- | --- |
| list | The list to split. |
| predicate | A lambda returning a `Boolean`. |

Split a list by a predicate

The following example splits a list into matching and non-matching elements:

**Formula**

```text
[1, 2, 3, 4] >> partition_by(n ~> n > 2)
```

**Output**

```text
[[3, 4], [1, 2]]
```

Read the matching elements from the result

The following example reads only the matching elements from the partitioned result:

**Formula**

```text
[1, 2, 3, 4] >> partition_by(n ~> n > 2) >> at(0)
```

**Output**

```text
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

```text
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

The following functions reduce a list to one value:

### `sum`

Adds the numeric elements. An empty list sums to `0`.

```text
sum(list)
```

| Parameter | Description |
| --- | --- |
| list | A list of numbers. |

Sum a list of floats

The following example sums a list of floats:

**Formula**

```text
sum([12.50, 99.00])
```

**Output**

```text
111.5
```

Sum a list of decimals to preserve scale

The following example sums a list of `Decimal` values, preserving the original scale:

**Formula**

```text
sum([Decimal('12.50'), Decimal('99.00')])
```

**Output**

```text
111.50
```

An empty list sums to zero

The following example sums an empty list:

**Formula**

```text
sum([])
```

**Output**

```text
0
```

> **SUM MONEY AS DECIMAL, NOT AS FLOAT**
> 
> The `sum([12.50, 99.00])` and `sum([Decimal('12.50'), Decimal('99.00')])` examples run the same arithmetic on different types. `12.50` is a `Float`, so the total is `111.5` and the scale is gone. `Decimal('12.50')` is exact, so the total is `111.50`. It stays a currency amount through every later step.
> 
> Schema inference in the Transform Data action doesn't produce `Decimal` for money. Refer to the [Transform data](/en/wel/workato-expression-language-connector) action for how to declare it.

### `avg`

Returns the mean of the numeric elements. An empty list raises `E207`, because there is no meaningful average of nothing.

```text
avg(list)
```

| Parameter | Description |
| --- | --- |
| list | A list of numbers. |

Average a list of numbers

The following example averages a list of numbers:

**Formula**

```text
avg([10, 20, 30])
```

**Output**

```text
20
```

### `min`

Returns the smallest element. Works on strings as well as numbers.

```text
min(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to reduce. |

Find the smallest number in a list

The following example finds the smallest number in a list:

**Formula**

```text
min([5, 2, 9])
```

**Output**

```text
2
```

### `max`

Returns the largest element. Works on strings as well as numbers.

```text
max(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to reduce. |

Find the largest number in a list

The following example finds the largest number in a list:

**Formula**

```text
max([5, 2, 9])
```

**Output**

```text
9
```

Find the largest string in a list

The following example finds the largest string in a list:

**Formula**

```text
max(['apple', 'pear'])
```

**Output**

```text
pear
```

### `reduce_by`

Folds a list into a single value using an accumulator.

Use it when the result isn't a plain total, such as building a `Map`, concatenating, or carrying state across elements. Use `sum` and `avg` instead for a straight sum or average, because their names say what they mean.

```text
reduce_by(list, initial, accumulate)
```

| Parameter | Description |
| --- | --- |
| list | The list to fold. |
| initial | The starting value of the accumulator. |
| accumulate | A lambda taking `(accumulator, element)` and returning the new accumulator. |

Fold a list into a total

The following example folds a list into a running total:

**Formula**

```text
[1, 2, 3] >> reduce_by(0, (acc, n) ~> acc + n)
```

**Output**

```text
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

```text
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

Builds a list of integers from start to end, inclusive. The list descends when start is greater than end.

```text
range(start, end)
```

| Parameter | Description |
| --- | --- |
| start | First integer, included. |
| end | Last integer, included. |

Build an ascending range

The following example builds an ascending range of integers:

**Formula**

```text
range(1, 5)
```

**Output**

```text
[1, 2, 3, 4, 5]
```

Build a descending range

The following example builds a descending range when the start is greater than the end:

**Formula**

```text
range(5, 1)
```

**Output**

```text
[5, 4, 3, 2, 1]
```

### `random_choice`

Returns one randomly selected element.

The result differs on every evaluation, so don't use it for anything a later step must reproduce. Refer to [Random functions](/en/wel/stdlib/random) for other ways to generate a value that doesn't need to repeat.

```text
random_choice(list)
```

| Parameter | Description |
| --- | --- |
| list | The list to pick from. |

## Related

- [Map functions](/en/wel/stdlib/map): Work with the `Map` that `group_by` returns.
- [Deep map functions](/en/wel/stdlib/deep-map): Reach through deeply nested structures.
- [Operators](/en/wel/language/operators): More information about the pipeline family of operators.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E201`, `E204`, and `E207`.

---
