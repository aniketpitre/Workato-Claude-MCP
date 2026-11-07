---
url: 'https://docs.workato.com/en/formulas/array-list-formulas.md'
description: >-
  Learn how to use Workato list and hash formulas to work with arrays, hashes,
  and lists of hashes when transforming complex data.
---

# List and Hash formulas

In addition to the basic data types (for example, string and integer), you may encounter more complex data structures that contain information about multiple items or multiple pieces of information about a single item.

You may encounter these data structures:

- [Lists](#lists-arrays) (also known as arrays)
- [Hashes](#hashes)
- [List of hashes](#lists-of-hashes)

Formulas in Workato are added to allowlists for Ruby methods. Only allowlisted Ruby methods are supported. Contact your Customer Success Manager to request new formulas for the allowlist.

* * *

## Lists (arrays)

Arrays are ordered, integer-indexed collections of any object. List indexing starts at 0. Lists and arrays refer to the same data structure.

In the example below, a list of integers is expressed as:

```ruby
number_list = [100, 101, 102, 103, 104]
```

As lists are ordered, we can use the following formula to get the values. Workato only supports retrieving up to the fifth item using this syntax.

| Formula | Result |
| --- | --- |
| number\_list.first | 100 |
| number\_list.second | 101 |
| number\_list.third | 102 |
| number\_list.fourth | 103 |
| number\_list.fifth | 104 |
| number\_list.last | 104 |

We can also use indexes to get corresponding values. Remember, indexes start at 0:

| Formula | Result |
| --- | --- |
| number\_list\[0\] | 100 |
| number\_list\[1\] | 101 |
| number\_list\[2\] | 102 |
| number\_list\[3\] | 103 |

Lists in Ruby supports negative indexes.

| Formula | Result |
| --- | --- |
| number\_list\[-1\] | 104 |
| number\_list\[-2\] | 103 |
| number\_list\[-3\] | 102 |
| number\_list\[-4\] | 101 |

Lists also support ranges as indexes. This returns another list, instead of returning only a value.

| Formula | Result |
| --- | --- |
| number\_list\[0..2\] | \[100, 101, 102\] |
| number\_list\[-3..-1\] | \[102, 103, 104\] |
| number\_list\[0..-2\] | \[100, 101, 102, 103\] |

* * *

## Hashes

A hash is a dictionary-like collection of unique keys and their values. They are similar to Lists, but where a List uses integers as its index, a Hash allows you to use any object type. Hashes enumerate their values in the order that the corresponding keys were inserted.

Let's take the example of a hash with 2 values, with `'Acme widgets'` and `10` as the values of item\_name and item\_quantity respectively.

```ruby
line_item = { 'item_name' => 'Acme widgets', 'item_qty' => 10 }
```

| Formula | Result |
| --- | --- |
| line\_item\["item\_name"\] | "Acme widgets" |
| line\_item\["item\_qty"\] | 10 |

* * *

## Lists of hashes

Here is an example of an invoice which has multiple line items. It is represented as a list of hashes.

```ruby
line_items = [
  { 'item_no': 1, 'item_name' => 'Acme widgets', 'item_qty' => 10 },
  { 'item_no': 2, 'item_name' => 'RR bearings',  'item_qty' => 99 },
  { 'item_no': 3, 'item_name' => 'Coyote tyres', 'item_qty' => 7 }
]
```

* * *

### Example list of hashes

The following is an example of a list of hashes called **Contacts**.

This is the Contacts list in a table form:

| name | email | state | company | company\_rev |
| --- | --- | --- | --- | --- |
| Joe | [joe@abc.om](mailto:joe@abc.om) | CA | ABC | 1000 |
| Jill | [jill@nbc.com](mailto:jill@nbc.com) | MA | NBC | 1000 |
| Joan | [joan@nbc.com](mailto:joan@nbc.com) | MA | NBC | 10000 |
| Jack | [jack@hbo.com](mailto:jack@hbo.com) | CA | HBO | 30000 |

This is the Contacts list in a list of hashes form.

```ruby
[
  {
    'name' => 'Joe',
    'email' => 'joe@abc.com',
    'state' => 'CA',
    'company' => 'ABC',
    'company_rev' => 1000,
    'description' => { 'summary' => 'First time buyer', 'estimated_value' => 300 }
  },
  {
    'name' => 'Jill',
    'email' => 'jill@nbc.com',
    'state' => 'MA',
    'company' => 'NBC',
    'company_rev' => 1000,
    'description' => { 'summary' => 'Referral', 'estimated_value' => 500 }
  },
  {
    'name' => 'Joan',
    'email' => 'joan@nbc.com',
    'state' => 'MA',
    'company' => 'NBC',
    'company_rev' => 10000,
    'description' => { 'summary' => 'Recurring customer', 'estimated_value' => 900 }
  },
  {
    'name' => 'Jack',
    'email' => 'jack@hbo.com',
    'state' => 'CA',
    'company' => 'HBO',
    'company_rev' => 30000,
    'description' => { 'summary' => 'Recurring customer', 'estimated_value' => 1000 }
  }
]
```

* * *

## List formulas

* * *

### `first`

This formula returns the first item in a list.

It can also be used to return the first _n_ items in a list. In this case, the output will be formatted as a list.

#### Syntax

List.first(number)

- List - An input list.
- number - (optional) The number of items to retrieve from the list. If not specified, the formula will return only _one_ item.

#### Sample usage

| Formula | Result |
| --- | --- |
| \["One","Two","Three","Four","Five"\].first() | "One" |
| \["One","Two","Three","Four","Five"\].first(2) | \["One","Two"\] |
| \[1,2,3,4,5\].first() | 1 |
| \[1,2,3,4,5\].first(3) | \[1,2,3\] |

#### How it works

This formula returns the first _n_ items from a list. If _n_ is greater than one, the output is formatted as a list.

> **Output datatype**
> 
> If you are returning a single item (i.e. no arguments provided). The output will be formatted according to the item's datatype.
> 
> If you are returning more than _one_ item. The output will be formatted as a list datatype.

#### See also

- [last](/en/formulas/array-list-formulas#last): Returns the last _n_ items in a list.
- [where](/en/formulas/array-list-formulas#where): Returns a subset of list items that meet a certain condition.

* * *

### `last`

This formula returns the last item in a list.

It can also be used to return the last _n_ items in a list. In this case, the output will be formatted as a list.

#### Syntax

List.last(number)

- List - An input list.
- number - (optional) The number of items to retrieve from the list. If not specified, the formula will return only _one_ item.

#### Sample usage

| Formula | Result |
| --- | --- |
| \["One","Two","Three","Four","Five"\].last() | "Five" |
| \["One","Two","Three","Four","Five"\].last(2) | \["Four","Five"\] |
| \[1,2,3,4,5\].last() | 5 |
| \[1,2,3,4,5\].last(3) | \[3,4,5\] |

#### How it works

This formula returns the last _n_ items from a list. If _n_ is greater than one, the output is formatted as a list.

> **Output datatype**
> 
> If you are returning a single item (i.e. no arguments provided). The output will be formatted according to the item's datatype.
> 
> If you are returning more than _one_ item. The output will be formatted as a list datatype.

#### See also

- [first](/en/formulas/array-list-formulas#first): Returns the first _n_ items in a list.
- [where](/en/formulas/array-list-formulas#where): Returns a subset of list items that meet a certain condition.

* * *

### `index`

Returns the index of the first item matching the given value. Returns `nil` if no matching items are found.

#### Syntax

Input.index(value)

- Input - An input list.
- value - The value to search for in the list.

#### Sample usage

| Formula | Result |
| --- | --- |
| \[4, 5, 6, 7\].index(6) | 2 |
| \[4, 5, 6, 7\].index(8) | nil |

* * *

### `count`

Returns the number of items in a list.

#### Syntax

`List`.count

- `List` - An input of list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| `["Hello", "World", "Cat", "Dog"]`.count | 4 |
| `["Hello", "World", ["Sub-array", "Here"]]`.count | 3 |
| `["Hello", "World", nil, ["Sub-array", "Here"]]`.count | 4 |

* * *

### `where`

Retrieves only the rows (hashes) which satisfy the specified WHERE condition. This formula accepts a single argument in the form of a hash with one or more key-value pairs.

The default operand for the condition is **equal to** (`==`). This formula also supports the following operands. Operands should be added to the end of key separated by a space.

| Name | Notation | Example |
| --- | --- | --- |
| Equal to (default) | \== | leads.where('state': 'CA') |
| More than | \> | leads.where('company\_revenue >': 10000) |
| More than or equal to | \>= | leads.where('company\_revenue >=': 10000) |
| Less than | < | leads.where('company\_revenue <': 10000) |
| Less than or equal to | <= | leads.where('company\_revenue <=': 10000) |
| Not equal to | != | leads.where('state !=': 'CA') |

> **Use datapills as the conditional argument**
> 
> Instead of using a static value (for example, `'CA'`), you can use a datapill as the conditional argument. The value of the datapill will be processed at run-time.
> 
> `contacts.where(state:` datapill `)`

#### Sample usage

Example of a single where condition

`contacts.where('state': 'CA')` returns the following rows:

| name | email | state | company | company\_rev |
| --- | --- | --- | --- | --- |
| Joe | [joe@abc.om](mailto:joe@abc.om) | CA | ABC | 1000 |
| Jack | [jack@hbo.com](mailto:jack@hbo.com) | CA | HBO | 30000 |

These rows will be expressed as a list of hashes:

```ruby
[
  {
    'name' => 'Joe',
    'email' => 'joe@abc.com',
    'state' => 'CA',
    'company' => 'ABC',
    'company_rev' => 1000
  },
  {
    'name' => 'Jack',
    'email' => 'jack@hbo.com',
    'state' => 'CA',
    'company' => 'HBO',
    'company_rev' => 30000
  }
]
```

Example of compound where formula

A compound WHERE formula will retrieve only the rows that matches all the conditions.

`contacts.where('state': 'CA', 'company_revenue >=': 10000)`

Returns the following rows:

| name | email | state | company | company\_rev |
| --- | --- | --- | --- | --- |
| Jack | [jack@hbo.com](mailto:jack@hbo.com) | CA | HBO | 30000 |

These rows will be expressed as a list of hashes:

```ruby
[
  {
    'name' => 'Jack',
    'email' => 'jack@hbo.com',
    'state' => 'CA',
    'company' => 'HBO',
    'company_rev' => 30000
  }
]
```

* * *

> **Warning - MULTIPLE CONDITIONS IN A SINGLE KEY**
> 
> Only the last condition is considered when you apply multiple conditions to the same key in a compound WHERE formula. This overrides previous conditions, and can lead to unexpected outcomes.
> 
> The following example shows that applying multiple conditions for `state`, returns only rows that contain the second `MA` key:
> 
> `contacts.where('state': 'CA', 'state': 'MA')`
> 
> returns only rows with states that are `MA`:
> 
> | name | email | state | company | company\_rev |
> | --- | --- | --- | --- | --- |
> | Jill | [jill@nbc.com](mailto:jill@nbc.com) | MA | NBC | 1000 |
> | Joan | [joan@nbc.com](mailto:joan@nbc.com) | MA | NBC | 10000 |
> 
> These rows will be returned as a list of hashes.
> 
> ```ruby
> [
>   {
>     'name' => 'Jill',
>     'email' => 'jill@nbc.com',
>     'state' => 'MA',
>     'company' => 'NBC',
>     'company_rev' => 1000
>   },
>   {
>     'name' => 'Joan',
>     'email' => 'joan@nbc.com',
>     'state' => 'MA',
>     'company' => 'NBC',
>     'company_rev' => 10000
>   }
> ]
> ```

Example of multiple matches

You can filter out records based on a particular field against more than 1 value. This is done by passing an array value in the WHERE condition.

`contacts.where('company': ['ABC','HBO'])`

This WHERE condition will return rows where the company is either **ABC** or **HBO**:

| name | email | state | company | company\_rev |
| --- | --- | --- | --- | --- |
| Joe | [joe@abc.om](mailto:joe@abc.om) | CA | ABC | 1000 |
| Jack | [jack@hbo.com](mailto:jack@hbo.com) | CA | HBO | 30000 |

These rows will be returned as a list of hashes.

```ruby
[
  {
    'name' => 'Joe',
    'email' => 'joe@abc.com',
    'state' => 'CA',
    'company' => 'ABC',
    'company_rev' => 1000
  },
  {
    'name' => 'Jack',
    'email' => 'jack@hbo.com',
    'state' => 'CA',
    'company' => 'HBO',
    'company_rev' => 30000
  }
]
```

Example where condition with pattern matching

You can also filter out records using regex. This is done by passing a regex instead of a string.

`contacts.where('name': /^Jo/)`

This WHERE condition will return rows where the name starts with **Jo**:

| name | email | state | company | company\_rev |
| --- | --- | --- | --- | --- |
| Joe | [joe@abc.om](mailto:joe@abc.om) | CA | ABC | 1000 |
| Joan | [joan@nbc.com](mailto:joan@nbc.com) | MA | NBC | 10000 |

These rows will be expressed as a list of hashes:

```ruby
[
  {
    'name' => 'Joe',
    'email' => 'joe@abc.com',
    'state' => 'CA',
    'company' => 'ABC',
    'company_rev' => 1000
  },
  {
    'name' => 'Joan',
    'email' => 'joan@nbc.com',
    'state' => 'MA',
    'company' => 'NBC',
    'company_rev' => 10000
  }
]
```

Example where condition with pattern matching (using datapills)

You may use datapills within a regex pattern to dynamically change the string that you are matching. However, using variables in a regex pattern requires escaping within the regex expression.

For example: `contacts.where(state: /#{` datapill `}/)`

The image below shows the method used to obtain all the 'Emails' in lookup table where the value in the 'State' column contains the string in the datapill from Salesforce, State (Step 2).

![Datapill in regex expression](/assets/regex-datapill.ClBzfqZA.png)_Using datapills in regex expressions_

**Note:** All regex metacharacters will need to be escaped if they should not be interpreted as metacharacters.

Example of chaining where conditions

If a series of WHERE conditions are chained, the formula evaluates each where condition in series.

`contacts.where('state': 'CA').where('company_revenue >=': 10000)` returns the following rows, which is the same as the compound where formula:

| name | email | state | company | company\_rev |
| --- | --- | --- | --- | --- |
| Jack | [jack@hbo.com](mailto:jack@hbo.com) | CA | HBO | 30000 |

In this case, however, the chaining will result in an intermediary array:

`contacts.where('state': 'CA')` first returns:

| name | email | state | company | company\_rev |
| --- | --- | --- | --- | --- |
| Joe | [joe@abc.om](mailto:joe@abc.om) | CA | ABC | 1000 |
| Jack | [jack@hbo.com](mailto:jack@hbo.com) | CA | HBO | 30000 |

And `.where('company_revenue >=': 10000)` filters this intermediary array further to return only:

| name | email | state | company | company\_rev |
| --- | --- | --- | --- | --- |
| Jack | [jack@hbo.com](mailto:jack@hbo.com) | CA | HBO | 30000 |

Results will be expressed as a list of hashes:

```ruby
[
  {
    'name' => 'Jack',
    'email' => 'jack@hbo.com',
    'state' => 'CA',
    'company' => 'HBO',
    'company_rev' => '30000'
  }
]
```

Example of chaining not operator

You can use the WHERE formula to find the difference between two arrays by chaining a not operator. This is useful if you have two lists, an original list and an updated list, and plan to compare the two to ensure the updated list contains all values from the original list.

For example: `contacts.where.not("id":updated_contacts.pluck('id'))` identifies any values that are present in the original list (`contacts`) and missing from the updated list (`updated_contacts`).

* * *

### `except`

Returns a hash that includes everything except given keys.

```ruby
hash = { a: true, b: false, c: nil }
hash.except(:c)     # => { a: true, b: false }
hash.except(:a, :b) # => { c: nil }
hash                # => { a: true, b: false, c: nil }
```

* * *

### `pluck`

Retrieves only the columns which have been specified.

#### Sample usage

Example of a single column output

`contacts.pluck("email")` returns

| email |
| --- |
| [joe@abc.com](mailto:joe@abc.com) |
| [jill@nbc.com](mailto:jill@nbc.com) |
| [joan@nbc.com](mailto:joan@nbc.com) |
| [jack@hbo.com](mailto:jack@hbo.com) |

If a single column, results will be returned as an array:

```ruby
["joe@abc.com", "jill@nbc.com", "joan@nbc.com", "jack@hbo.com"]
```

Example of a multiple column dataset

`contacts.where("state ==": "CA").pluck("email", "company")` returns

| email | company |
| --- | --- |
| [joe@abc.com](mailto:joe@abc.com) | ABC |
| [jill@nbc.com](mailto:jill@nbc.com) | NBC |
| [joan@nbc.com](mailto:joan@nbc.com) | NBC |
| [jack@hbo.com](mailto:jack@hbo.com) | HBO |

Results are returned as a list of a list:

```ruby
[["joe@abc.com", "ABC"], ["jill@nbc.com", "NBC"], ["joan@nbc.com", "NBC"], ["jack@hbo.com", "HBO"]]
```

Example of retrieving nested fields

This method can be used to extract nested fields. Use the `[<1st-level field>,<2nd-level field>...]` format to define which fields to retrieve.

`contacts.pluck("email", ["description", "summary"])` returns

| email | summary |
| --- | --- |
| [joe@abc.com](mailto:joe@abc.com) | First time buyer |
| [jill@nbc.com](mailto:jill@nbc.com) | Referral |
| [joan@nbc.com](mailto:joan@nbc.com) | Recurring customer |
| [jack@hbo.com](mailto:jack@hbo.com) | Recurring customer |

Results are returned as a list of lists:

```ruby
[
  ["joe@abc.com", "First time buyer"],
  ["jill@nbc.com", "Referral"],
  ["joan@nbc.com", "Recurring customer"],
  ["jack@hbo.com", "Recurring customer"]
]
```

* * *

### `format_map`

Creates a new array of strings by applying a format to each item in the input array. You can reference input values in the format string using `%{field_name}` for hashes, or `%s` for sub-arrays and scalar values.

#### Sample usage

Array of hashes

You can use `format_map` on an array of hashes. For example:

```ruby
[
  { name: 'Alex',  email: 'alex@example.com',  company: 'ACME' },
  { name: 'Hao',   email: 'hao@example.com',   company: 'ACME' },
  { name: 'Kai',   email: 'kai@example.com',   company: 'STARK' },
  { name: 'Sasha', email: 'sasha@example.com', company: 'ACME' }
].format_map('Name: %{name}, Email: %{email}, Company: %{company}')
```

This outputs an array containing a formatted string for each hash in the input:

```ruby
[
  'Name: Alex, Email: alex@example.com, Company: ACME',
  'Name: Hao, Email: hao@example.com, Company: ACME',
  'Name: Kai, Email: kai@example.com, Company: STARK',
  'Name: Sasha, Email: sasha@example.com, Company: ACME',
]
```

Nested array

You can use `format_map` on a nested array. For example:

```ruby
[
  ['Alex', 'alex@example.com', 'ACME'],
  ['Hao', 'hao@example.com', 'ACME'],
  ['Kai', 'kai@example.com', 'STARK'],
  ['Sasha', 'sasha@example.com', 'ACME']
].format_map('Name: %s, Email: %s, Company: %s')
```

This outputs an array containing a formatted string for each sub-array in the input:

```ruby
[
  'Name: Alex, Email: alex@example.com, Company: ACME',
  'Name: Hao, Email: hao@example.com, Company: ACME',
  'Name: Kai, Email: kai@example.com, Company: STARK',
  'Name: Sasha, Email: sasha@example.com, Company: ACME'
]
```

Array of scalar values

You can use `format_map` on an array of scalar values, such as strings, integers, dates, and booleans. For example:

```ruby
['Alex', 'Hao', 'Kai'].format_map('Name: %s')
```

This outputs an array containing a formatted string for each scalar value in the input:

```ruby
[
  'Name: Alex',
  'Name: Hao',
  'Name: Kai'
]
```

* * *

### `join`

Combines all items in a list into a text string. A separator is placed between each item.

#### Syntax

List.join(separator)

- List - An input of list datatype.
- separator - The character to add between items when they are joined. If no separator is specified, the list items will be joined together.

#### Sample usage

| Formula | Result |
| --- | --- |
| \["Ms", "Jean", "Marie"\].join("-") | "Ms-Jean-Marie" |
| \[1,2,3\].join("--") | "1--2--3" |
| \["ab", "cd", "ef"\].join | "abcdef" |

#### How it works

The list items are combined into a single text string. The separator characters is added between each item.

> **Separator character**
> 
> You can use a string of characters together as the separator argument (for example, `", "`).
> 
> \["Open","Pending","Closed"\].join(", ") returns `"Open, Pending, Closed"`.

#### See also

- [split](/en/formulas/string-formulas#split): Divides a string around a specified character and returns an array of strings.

* * *

### `smart_join`

Joins list elements into a string. Removes empty and nil values and trims any white space before joining.

#### Syntax

List.smart\_join(separator)

- List - An input of list datatype.
- separator - The character to add between items when they are joined. If no separator is specified, a blank space will be used as the joining character.

#### Sample usage

| Formula | Result |
| --- | --- |
| \[nil, "", "Hello", " ", "World"\].smart\_join(" ") | "Hello World" |
| \["111 Vinewood Drive", "", "San Francisco", "CA", "95050"\].smart\_join(",") | "111 Vinewood Drive, San Francisco, CA, 95050" |

* * *

### `concat`

Concatenates 2 lists into a single list. Nested lists will NOT be flattened.

#### Syntax

List.concat(list\_to\_be\_joined)

- List - An input of list datatype.
- list\_to\_be\_joined - The other list to be concatenated with the original list input.

#### Sample usage

| Formula | Result |
| --- | --- |
| \["Hello", "World"\].concat(\["Workato", "Rocks"\]) | \["Hello", "World", "Workato", "Rocks"\] |
| \["Hello", "World", \["Sub-array", "Here"\]\].concat(\["Workato", "Rocks"\]) | \["Hello", "World", \["Sub-array", "Here"\], "Workato", "Rocks"\] |
| \["Hello", "World", nil, \["Sub-array", "Here"\]\].concat(\["Workato", "Rocks"\]) | \["Hello", "World", nil, \["Sub-array", "Here"\], "Workato", "Rocks"\] |

* * *

### `reverse`

Reverses the order of a list.

#### Syntax

List.reverse

- List - An input of list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| \["Joe", "Jill", "Joan", "Jack"\].reverse | \["Jack", "Joan", "Jill", "Joe"\] |
| \[100, 101, 102, 103\].reverse | \[103, 102, 101, 100\] |

* * *

### `sum`

For integers and decimals, the numbers will be added together and the total sum obtained. For strings, the strings will be concatenated together to form a longer string.

#### Syntax

List.sum

- List - An input of list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| \[1, 2, 3\].sum | 6 |
| \[1.5, 2.5, 3\].sum | 7.0 |
| \["abc", "xyz"\].sum | "abcxyz" |

* * *

### `uniq`

Returns a list containing unique items.

#### Syntax

List.uniq

- List - An input of list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| \["joe", "jack", "jill", "joe", "jack"\].uniq | \["joe","jack", "jill"\] |
| \[1, 2, 3, 1, 1, 3\].uniq | \[1, 2, 3\] |
| \[1.0, 1.5, 1.0\].uniq | \[1.0, 1.5\] |

* * *

### `flatten`

Flattens a multi-dimensional array (i.e. array of arrays) to a single dimension array.

#### Syntax

List.flatten

- List - An input of list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| \[\[1, 2, 3\], \[4, 5, 6\]\].flatten | \[1, 2, 3, 4, 5, 6\] |
| \[\[1, \[2, 3\], 3\], \[4, 5, 6\]\].flatten | \[1, 2, 3, 3, 4, 5, 6\] |
| \[\[1, \[2, 3\], 9\], \[9, 8, 7\]\].flatten | \[1, 2, 3, 9, 9, 8, 7\] |

* * *

### `length`

Returns the number of elements in self. Returns 0 if the list is empty.

#### Syntax

List.length

- List - An input of list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| \[ 1, 2, 3, 4, 5 \].length | 5 |
| \[{..}, {..}, {..}\].length | 3 |
| \[" ", nil, "", nil\].length | 4 |
| \[\].length | 0 |

* * *

### `max`

Returns largest value in an array. When comparing numbers, the largest number is returned. When comparing strings, the string with the largest ASCII value is returned.

#### Syntax

List.max

- List - An input of list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| \[-5, 0, 1, 2, 3, 4, 5\].max | 5 |
| \[-1.5, 1.5, 2, 3, 3.5\].max | 3.5 |
| \["cat", "dog", "rat"\].max | "rat" |

* * *

### `min`

Returns smallest value in an array. When comparing numbers, the smallest number is returned. When comparing strings, the string with the smallest ASCII value is returned.

#### Syntax

List.min

- List - An input of list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| \[-5, 0, 1, 2, 3, 4, 5\].min | \-5 |
| \[-1.5, 1.5, 2, 3, 3.5\].min | \-1.5 |
| \["cat", "dog", "rat"\].min | "cat" |

* * *

### `compact`

Removes nil values from array and hash.

#### Sample usage

| Formula | Result |
| --- | --- |
| \["foo", nil, "bar"\].compact | \["foo", "bar"\] |
| { foo: 1, bar: nil, baz: 2 }.compact | { foo: 1, baz: 2 } |

* * *

## Conditionals

* * *

### `blank?`

Checks whether the input is considered blank according to Ruby conventions. This includes:

- Null values
- Empty inputs
- False booleans
- Strings containing only whitespace
- Non-value numbers, sometimes referred to as NaN (not a number). This is an undefined value or value that cannot be represented. For example, the result of division by zero, or a missing value.

#### Syntax

Input.blank?

- Input - An input datapill. It can be a string, number, date, datetime, boolean, array, or object datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Any Value".blank? | false |
| 123.blank? | false |
| 0.blank? | false |
| "".blank? | true |
| ' '.blank? | true |
| nil.blank? | true |
| false.blank? | true |
| true.blank? | false |
| \[\].blank? | true |
| {}.blank? | true |

#### How it works

If the input is considered blank according to Ruby conventions, the formula returns true. For any other data, it returns false.

#### See also

- [presence](/en/formulas/string-formulas#presence): Returns the data if it exists, returns nil if it does not.
- [present?](/en/formulas/string-formulas#present): Returns true if there is a valid input.

* * *

### `include?`

Checks if the string contains a specific substring, or if a list contains an element. Returns true if it does.

#### Syntax

Input.include?(substring)

- Input - A string or list input.
- substring\_or\_element - The substring or element to check for.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Partner account".include?("Partner") | true |
| "Partner account".include?("partner") | false |
| \["Hello", "World", \["Sub-array","Here"\]"\].include?("Hello") | true |
| \["Hello", "World", \["Sub-array","Here"\]"\].include?(\["Sub-array","Here"\]) | true |

#### How it works

This formula check is the string contains a specific substring, or if a list contains a specific element. Returns true if it does, otherwise, returns false. The substring comparison is case sensitive, and the element comparison is exact match.

This function acts in an opposite manner from [exclude?](#exclude). The latter will return true only if the input string/list does NOT contain the stated keyword/element.

#### See also

- [exclude?](#exclude): Checks if the string contains a specific substring, or if a list contains an element. Returns false if it does.

* * *

### `exclude?`

Checks if the string contains a specific substring, or if a list contains an element. Returns false if it does.

#### Syntax

Input.exclude?(substring)

- Input - A string or list input.
- substring\_or\_element - The substring or element to check for.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Partner account".exclude?("Partner") | false |
| "Partner account".exclude?("partner") | true |
| \["Hello", "World", \["Sub-array","Here"\]"\].include?("Hello") | false |
| \["Hello", "World", \["Sub-array","Here"\]"\].include?(\["Sub-array","Here"\]) | false |

#### How it works

This formula check is the string contains a specific substring, or if a list contains a specific element. Returns false if it does, otherwise, returns true. The substring comparison is case sensitive, and the element comparison is exact match.

This function acts in an opposite manner from [include?](#include). The latter will return true only if the input string/list contains the stated keyword/element.

#### See also

- [include?](#include): Checks if the string contains a specific substring, or if a list contains an element. Returns true if it does.

* * *

### `present?`

This formula will check the input and if there is a value present, it will return true. If the input is nil, boolean false, an empty string, or an empty list, the formula will return false.

#### Syntax

Input.present?

- Input - An input datapill. It can be a string, number, date, or list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| "Any Value".present? | true |
| 123.present? | true |
| 0.present? | true |
| "2017-04-02T12:30:00.000000-07:00".present? | true |
| nil.present? | false |
| "".present? | false |
| \[\].present? | false |

#### How it works

If the input is null, an empty string or an empty list, the formula will return false. For any other data, it returns true.

> **Evaluating a list with nil values**
> 
> - Only an empty list will return false.
> 
> \[\].present? returns false.
> 
> - A list with nil and empty string will return true.
> 
> \[nil,""\].present? returns true.

#### See also

- [presence](/en/formulas/array-list-formulas#presence): Returns the data if it exists, returns nil if it does not.
- [blank?](/en/formulas/array-list-formulas#blank): Returns nil if the data does not exist or if the string consist of only white spaces.

* * *

### `presence`

Returns the data if it exists, returns nil if it does not.

#### Syntax

Input.presence

- Input - An input datapill. It can be a string, number, date, or datetime datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| nil.presence | nil |
| "".presence | nil |
| "Any Value".presence | "Any Value" |
| 45.0.presence | 45.0 |
| 0.presence | 0 |

#### How it works

If the input is null or an empty string, the formula will return nil. For any other data, it returns the original input data.

#### See also

- [blank?](/en/formulas/array-list-formulas#blank): Returns nil if the data does not exist or if the string consist of only white spaces.
- [present?](/en/formulas/array-list-formulas#present): Returns true if there is a valid input.

* * *

## Conversion

* * *

The following formulas allows you to convert data from arrays to other data types

* * *

### `to_csv`

Generates CSV line from an array. This handles escaping. Nil values and empty strings will also be expressed within the csv line.

#### Syntax

Input.to\_csv

- Input - An input of list datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| \["John Smith", "No-Email", " ", nil, "555-1212"\].to\_csv | "John Smith,No-Email, ,,555-1212" |
| \["John Smith", "No-Email", " ", nil, 1212\].to\_csv | "John Smith,No-Email, ,,1212" |

* * *

### `to_json`

Converts hash or array to JSON string.

#### Syntax

Input.to\_json

- Input - An input datapill. It can be a list or hash datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| {"pet" => "cat", "color" => "gray"}.to\_json | {"pet":"cat","color":"gray"} |
| \["1","2","3"\].to\_json | \["1", "2", "3"\] |

* * *

### `to_xml`

Converts hash or array into XML string.

#### Syntax

Input.to\_xml

- Input - An input datapill. It can be a list or hash datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| {"name" => "Ken"}.to\_xml(root: "user") | <user><name>Ken</name></user> |
| \[{"name" => "Ken"}\].to\_xml(root: "users") | <users><user><name>Ken</name></user></users> |

* * *

### `from_xml`

Converts XML string to hash.

#### Syntax

Input.from\_xml

- Input - Input XML data.

#### Sample usage

Converting XML string to hash

This XML string:

`<?xml version=\"1.0\" encoding=\"UTF-8\" ?> <hash><foo type="integer">123</foo></hash>`

represents the following XML data.

```xml
<?xml version=\"1.0\" encoding=\"UTF-8\" ?>

<hash>
  <foo type="integer">123</foo>
</hash>
```

XML string.from\_xml will return the following hash.

```ruby
{ "hash":
  [ "foo":
    [
      { "@type": "integer",
        "content!": "1"
      }
    ]
  ]
}
```

* * *

### `encode_www_form`

Join hash into url-encoded string of parameters.

#### Syntax

Input.encode\_www\_form

- Input - An input of hash datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| {"apple" => "red green", "2" => "3"}.encode\_www\_form | "apple=red+green&2=3" |

* * *

### `to_param`

Returns a string representation for use as a URL query string.

#### Syntax

Input.to\_param

- Input - An input of hash datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| {name: 'Jake', age: '22'}.to\_param | "name=Jake&age=22" |

* * *

### `keys`

Returns an array of keys from the input hash.

#### Syntax

Input.keys

- Input - An input of hash datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| {"name" => 'Jake', "age" => '22'}.keys | \["name", "age"\] |

* * *

### `values`

Returns an array of values from the input hash.

#### Syntax

Input.values

- Input - An input of hash datatype.

#### Sample usage

| Formula | Result |
| --- | --- |
| {"name" => 'Jake', "age" => '22'}.values | \["Jake", "22"\] |

* * *

## List operands

### Difference (`-`)

Returns the difference between two arrays, meaning a new array that is a copy of the first array without any of the items also present in the second array.

#### Syntax

`list` - `updated_list`

- `-` the difference/subtract operand
- `list` - the original list
- `updated_list` - an updated list

#### Sample usage

Let's say you have two arrays, `contacts` and `updated_contacts`:

`contacts = ["Ariel", "Max", "Kai", "Noam", "Tal"]`

`updated_contacts = ["Ariel", "Max", "Kai", "Lee", "Quinn"]`

| Formula | Result |
| --- | --- |
| `contacts - updated_contacts` | \["Noam", "Tal"\] |
| `updated_contacts - contacts` | \["Lee", "Quinn"\] |

#### How it works

This operand creates an array that is the difference between the two arrays. The first example, `contacts - updated_contacts`, returns an array of items present in `contacts` but not present in `updated_contacts`. It's important to note that this does not simply remove duplicate items; if we reverse the order of operations, we obtain different results. For example, when we find the difference between `updated_contacts` and `contacts`, the new array contains items that are present in `updated_contacts`, and not present in `contacts`.

#### See also

- [where](/en/formulas/array-list-formulas#where): Returns a subset of list items that meet a certain condition. Reference the example on chaining not operands to use `where` to compare two lists.

* * *

### Union (`&`)

While Workato does not support the union (`&`) operand to manipulate arrays directly, you can achieve a similar result by combining the [concat](#concat) and [uniq](#uniq) formulas.

#### Syntax

`list.concat(updated_list).uniq`

- `list` - a list
- `concat` - concatenates two lists into a single list
- `updated_list` - an updated list
- `uniq` - returns a list containing unique values

#### Sample usage

| Formula | Result |
| --- | --- |
| `contacts.concat(updated_contacts).uniq` | \["Ariel", "Kai", "Lee", "Max", "Noam", "Quinn", "Tal"\] |

#### How it works

`concat` concatenates two lists into a single list, and `uniq` returns a list containing unique items. You can combine two lists and remove any duplicate items that may appear by combining the two formulas.

---
