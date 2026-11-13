---
url: 'https://docs.workato.com/en/wel/cookbook.md'
description: >-
  Worked WEL examples of common integration problems - joins, grouping,
  deduplication, CSV and JWT generation, and error-tolerant batch processing.
---

# WEL cookbook

This page contains 26 worked examples of common integration problems, grouped by theme. Each example is self-contained, so you can paste it into the [`wel` binary](/en/wel/quickstart#start-with-the-binary) and run it as-is.

## Reshape and extract

The following solutions reshape payloads and extract values from nested structures:

### Normalize contact names from a CRM

A CRM sends names with inconsistent spacing and casing. Clean each field, then build a display name from the cleaned values.

**Formula**

```text
let raw = {first: '  dana ', last: ' SMITH  '}
do {
  first: raw.first >> trim >> capitalize,
  last: raw.last >> trim >> capitalize,
  full: trim(raw.first) ++ ' ' ++ trim(raw.last) >> titleize
}
```

**Output**

```json
{"first": "Dana", "last": "Smith", "full": "Dana Smith"}
```

[trim](/en/wel/stdlib/string#trim) clears the stray whitespace, then [capitalize](/en/wel/stdlib/string#capitalize) and [titleize](/en/wel/stdlib/string#titleize) fix the casing, so all three fields come out clean regardless of how the source formatted them.

### Extract fields safely, with fallbacks

Two optional fields are missing. Supply a default for each rather than passing `null` through to the destination.

**Formula**

```text
let contact = {name: 'Kai', email: null, phone: null}
do {
  name: contact.name,
  email: contact.email | 'no-reply@example.com',
  phone: contact.phone | 'N/A'
}
```

**Output**

```json
{"name": "Kai", "email": "no-reply@example.com", "phone": "N/A"}
```

The [fallback operator](/en/wel/language/operators#null-value-fallback) (`|`) only replaces a `null` value, so `name` remains unchanged while the two missing fields get their defaults.

### Extract identifiers from a deeply nested response

An API response contains the same field name at several levels. Extract every occurrence without specifying each path.

**Formula**

```text
let api_response = {
  data: {
    users: [
      {profile: {Name: 'Dana'}, orders: [{Name: 'Order-1'}]},
      {profile: {Name: 'Kai'}, orders: [{Name: 'Order-2'}, {Name: 'Order-3'}]}
    ]
  }
}
do deep_collect(api_response, 'Name')
```

**Output**

```json
["Dana", "Order-1", "Kai", "Order-2", "Order-3"]
```

[deep\_collect](/en/wel/stdlib/deep-map#deep-collect) walks every level of the structure, so it finds a `Name` field whether it belongs to a profile or an order, without naming either path.

### Transform values inside a deeply nested structure

A document carries file attachments at an unpredictable depth. Encode every binary value in place and leave everything else untouched.

**Formula**

```text
let doc = {
  title: 'Report',
  attachments: [
    {name: 'logo', data: Binary('PNG')},
    {name: 'csv', data: Binary('CSV')}
  ]
}
do deep_map_values_by(
  doc,
  v ~> encode_base64(v),
  v ~> type_of(v) == 'Binary'
)
```

**Output**

```json
{"title": "Report", "attachments": [{"name": "logo", "data": "UE5H"}, {"name": "csv", "data": "Q1NW"}]}
```

The condition lambda is what makes this safe. [deep\_map\_values\_by](/en/wel/stdlib/deep-map#deep-map-values-by) only applies the transform to values where `type_of(v) == 'Binary'`, so `title` and `name` pass through as they are.

## Lists and aggregation

The following solutions combine, reduce, or reorganize a list of records into the shape a destination expects:

### Flatten nested order line items

Orders arrive with their line items nested underneath them. Produce one flat row per line item, carrying the parent order ID along.

**Formula**

```text
let orders = [
  {id: 'A1', items: [{sku: 'X', qty: 2}, {sku: 'Y', qty: 1}]},
  {id: 'A2', items: [{sku: 'Z', qty: 5}]}
]
do orders
  >> map_by(o ~> o.items >> map_by(i ~> {order_id: o.id, sku: i.sku, qty: i.qty}))
  >> flatten
```

**Output**

```json
[
  {"order_id": "A1", "sku": "X", "qty": 2},
  {"order_id": "A1", "sku": "Y", "qty": 1},
  {"order_id": "A2", "sku": "Z", "qty": 5}
]
```

The inner [map\_by](/en/wel/stdlib/list#map-by) produces one list of line items for each order. [flatten](/en/wel/stdlib/list#flatten) combines those lists into one flat list.

### Group line items by SKU across orders

The same SKU appears across several orders. Total the quantity for each one.

**Formula**

```text
let lines = [
  {sku: 'X', qty: 2}, {sku: 'Y', qty: 1},
  {sku: 'X', qty: 3}, {sku: 'Y', qty: 4}
]
do lines
  >> group_by(l ~> l.sku)
  >> entries
  >> map_by(e ~> {sku: e.key, total: e.value >> map_by(row ~> row.qty) >> sum})
```

**Output**

```json
[{"sku": "X", "total": 5}, {"sku": "Y", "total": 5}]
```

[group\_by](/en/wel/stdlib/list#group-by) produces a `Map` keyed by SKU. [entries](/en/wel/stdlib/map#entries) converts the map to a list, and [sum](/en/wel/stdlib/list#sum) calculates the total quantity for each group.

### Deduplicate records, keeping the most recent

The same record ID appears multiple times with different timestamps. Keep only the most recent version of each record.

**Formula**

```text
let events = [
  {id: 'a', ts: 1, status: 'pending'},
  {id: 'b', ts: 2, status: 'active'},
  {id: 'a', ts: 3, status: 'active'}
]
do events
  >> group_by(e ~> e.id)
  >> values
  >> map_by(group ~> group >> sort_by(e ~> e.ts) >> last)
```

**Output**

```json
[{"id": "a", "ts": 3, "status": "active"}, {"id": "b", "ts": 2, "status": "active"}]
```

A group-by on ID collects every version of a record together. Within each group, a sort by timestamp followed by [last](/en/wel/stdlib/list#last) then keeps only the most recent version.

### Pivot rows into columns

A metrics API returns one row per metric. Reshape it into a single record with one field per metric.

**Formula**

```text
let rows = [
  {metric: 'cpu', value: 72},
  {metric: 'mem', value: 85},
  {metric: 'disk', value: 40}
]
do rows
  >> map_by(r ~> {key: r.metric, value: r.value})
  >> from_entries
```

**Output**

```json
{"cpu": 72, "mem": 85, "disk": 40}
```

[from\_entries](/en/wel/stdlib/map#from-entries) is the inverse of [entries](/en/wel/stdlib/map#entries): It takes a list of `{key, value}` pairs and rebuilds them into a single `Map`. This operation turns rows into columns.

### Partition records into success and failure buckets

A batch job needs to route successes and failures differently. Split a mixed list of results into the two groups.

**Formula**

```text
let results = [
  {id: 1, status: 'ok'}, {id: 2, status: 'error'},
  {id: 3, status: 'ok'}, {id: 4, status: 'error'}
]
do let parts = partition_by(results, r ~> r.status == 'ok')
do {
  succeeded: parts[0] >> map_by(r ~> r.id),
  failed: parts[1] >> map_by(r ~> r.id)
}
```

**Output**

```json
{"succeeded": [1, 3], "failed": [2, 4]}
```

[partition\_by](/en/wel/stdlib/list#partition-by) returns a two-element list. The first element contains matching records, and the second contains the remaining records. In this example, `parts[0]` contains successes and `parts[1]` contains failures.

## Join data sources

The following solutions combine records from two separate lists by a shared key:

### Join two lists on a shared key

Two lists share a key. Return only records with a match in both lists.

**Formula**

```text
let users = [{id: 1, name: 'Dana'}, {id: 2, name: 'Kai'}],
    orders = [{user_id: 1, item: 'Book'}, {user_id: 1, item: 'Pen'}, {user_id: 3, item: 'Tape'}]
do users
  >> map_by(u ~> orders
      >> filter_by(o ~> o.user_id == u.id)
      >> map_by(o ~> {name: u.name, item: o.item}))
  >> flatten
```

**Output**

```json
[{"name": "Dana", "item": "Book"}, {"name": "Dana", "item": "Pen"}]
```

[filter\_by](/en/wel/stdlib/list#filter-by) keeps only the orders matching each user's ID. Users without matching orders produce empty lists, which `flatten` removes from the result. This behavior creates an inner join.

### Keep every record in a left join, even without a match

Every record on the left side of a join must appear in the result, matched or not, unlike an inner join.

**Formula**

```text
let users = [{id: 1, name: 'Dana'}, {id: 2, name: 'Kai'}],
    orders = [{user_id: 1, item: 'Book'}]
do users
  >> map_by(u ~>
      let matches = orders >> filter_by(o ~> o.user_id == u.id)
      do if length(matches) > 0
         then matches >> map_by(o ~> {name: u.name, item: o.item})
         else [{name: u.name, item: null}])
  >> flatten
```

**Output**

```json
[{"name": "Dana", "item": "Book"}, {"name": "Kai", "item": null}]
```

The `else` branch supplies a single-element list with `item: null` instead of an empty one when no order matches a user, so that user still contributes a row after `flatten`.

### Merge and reconcile two data sources

The same entity exists in two systems, sometimes only in one of them. Combine both into a single record per ID, noting which system each one came from.

**Formula**

```text
let crm = [{id: '1', name: 'Dana', source: 'crm'}, {id: '2', name: 'Kai', source: 'crm'}],
    erp = [{id: '2', name: 'Lucian', source: 'erp'}, {id: '3', name: 'Sasha', source: 'erp'}]
do let all_ids = (crm ++ erp) >> map_by(r ~> r.id) >> unique
do all_ids >> map_by(id ~>
    let from_crm = crm >> find_by(r ~> r.id == id),
        from_erp = erp >> find_by(r ~> r.id == id)
    do {
      id: id,
      name: if from_crm != null then from_crm.name else from_erp.name,
      in_crm: from_crm != null,
      in_erp: from_erp != null
    })
```

**Output**

```json
[
  {"id": "1", "name": "Dana", "in_crm": true, "in_erp": false},
  {"id": "2", "name": "Kai", "in_crm": true, "in_erp": true},
  {"id": "3", "name": "Sasha", "in_crm": false, "in_erp": true}
]
```

This collects every ID from both lists first, before looking either system up, so a record from only one source still appears in the result.

## Numbers and money

The following solutions keep a number exact through arithmetic and parsing, where approximation would be a real bug:

### Convert currency without losing precision

An invoice amount needs converting to another currency. Round the result to cents for display, without losing the exact source amount.

**Formula**

```text
let invoice = {amount: Decimal('1234.56'), rate: Decimal('0.85')}
do let converted = invoice.amount * invoice.rate
do {
  original: invoice.amount,
  eur: round_places(converted, 2),
  label: String(round_places(converted, 2)) ++ ' EUR'
}
```

**Output**

```json
{"original": 1234.56, "eur": 1049.38, "label": "1049.38 EUR"}
```

Both `amount` and `rate` are `Decimal` from the start, so the multiplication is exact and [round\_places](/en/wel/stdlib/numeric#round-places) is the only place any precision is lost, and only for display.

### Parse large integers and decimals from JSON without losing precision

Most languages silently lose precision parsing large integers or decimals from JSON. A JavaScript `JSON.parse`, for example, truncates `9999999999999999999` to `10000000000000000000`.

**Formula**

```text
let json = '{"tx_id": 9999999999999999999, "balance": 1234567890.1234567890}'
do let data = parse_json(json, {numbers: 'decimal'})
do {
  tx_id: data.tx_id,
  balance: data.balance,
  balance_type: type_of(data.balance),
  cents: data.balance * 100
}
```

**Output**

```json
{"tx_id": 9999999999999999999, "balance": 1234567890.1234567890, "balance_type": "Decimal", "cents": 123456789012.3456789000}
```

`Integer` isn't limited to 64 bits, so `tx_id` survives intact. The `{numbers: 'decimal'}` option keeps `balance` as an exact `Decimal` instead of an approximate `Float`. Without it, fractional numbers parse using standard `Integer`/`Float` rules.

## Dates

The following solution derives several routing facts from a single date at once:

### Route a record by its date

A record requires routing based on whether its date falls on a weekend, the number of days until month end, and its quarter.

**Formula**

```text
let event_date = PlainDate('2025-03-15')
do let dow = day_of_week(event_date)
do let month_end = end_of_month(event_date)
do {
  is_weekend: dow == 6 or dow == 7,
  days_until_month_end: month_end - event_date,
  quarter: ceil(month(event_date) / 3.0)
}
```

**Output**

```json
{"is_weekend": true, "days_until_month_end": 16, "quarter": 1}
```

A `PlainDate` subtraction gives a day count directly, so `days_until_month_end` needs no separate duration handling. Refer to [day\_of\_week](/en/wel/stdlib/temporal#day-of-week) for what the numbering depends on.

## Validation and errors

The following solutions reject or route invalid data before it reaches downstream steps:

### Validate an incoming webhook payload

A webhook delivers its body as a JSON string. Parse it, then reject the payload immediately if the amount it carries isn't usable.

**Formula**

```text
let payload = '{"amount": "42.50", "currency": "USD"}'
do let data = parse_json(payload)
do let amount = Decimal(data.amount)
guard amount > 0 else 'amount must be positive'
do {amount: amount, currency: data.currency}
```

**Output**

```json
{"amount": 42.50, "currency": "USD"}
```

The [guard](/en/wel/language/expressions#guards) stops a zero, negative, or unparseable amount from reaching the rest of the transformation, rather than letting a bad value flow through silently.

### Filter and summarize API error responses

A batch of API responses mixes successes and failures. Report how many of each, with the failure details.

**Formula**

```text
let responses = [
  {code: 200, body: 'ok'},
  {code: 422, body: 'validation failed'},
  {code: 200, body: 'ok'},
  {code: 500, body: 'internal error'}
]
do let failures = responses >> filter_by(r ~> r.code >= 400)
do {
  total: length(responses),
  failed: length(failures),
  errors: failures >> map_by(r ~> String(r.code) ++ ': ' ++ r.body)
}
```

**Output**

```json
{"total": 4, "failed": 2, "errors": ["422: validation failed", "500: internal error"]}
```

The `let` binding for `failures` filters the failed responses a single time, reusing the result for both the count and the error list, rather than filtering twice.

### Clean and validate a batch of email addresses

A batch of email addresses arrives with inconsistent casing, stray whitespace, blanks, and at least one malformed entry. Keep only the ones that are actually usable.

**Formula**

```text
let raw = ['dana@co.com', 'bad-email', '  KAI@CO.COM  ', '', 'sasha@co.com']
do raw
  >> map_by(e ~> trim(e) >> lower)
  >> filter_by(e ~> not blank?(e))
  >> filter_by(e ~> valid_email?(e))
```

**Output**

```json
["dana@co.com", "kai@co.com", "sasha@co.com"]
```

The normalization step runs before validation, so it treats `KAI@CO.COM` and `kai@co.com` as the same address, and [valid\_email?](/en/wel/stdlib/string#valid-email) removes `bad-email`, which wasn't a valid address.

### Guard a multi-step calculation against bad input

A tax calculation depends on a rate that arrives as a string and must fall within a sane range before anything downstream trusts it.

**Formula**

```text
let payload = {items: [{price: 10, qty: 2}, {price: 25, qty: 1}], tax_rate: '0.08'}
do let tax = Decimal(payload.tax_rate)
guard tax >= 0 and tax < 1 else 'invalid tax rate'
do let subtotal = payload.items >> map_by(i ~> i.price * i.qty) >> sum
do {
  subtotal: subtotal,
  tax: round_places(Decimal(subtotal) * tax, 2),
  total: round_places(Decimal(subtotal) * (1 + tax), 2)
}
```

**Output**

```json
{"subtotal": 45, "tax": 3.60, "total": 48.60}
```

The guard runs immediately after converting `tax`, before any of the arithmetic that depends on it, so an out-of-range rate fails the job instead of producing a silently wrong total.

### Process a batch without failing the whole job on one bad record

A batch of values needs converting to `Integer`, but some of them aren't valid numbers. One bad record shouldn't fail the rest of the batch.

**Formula**

```text
let inputs = ['42', 'bad', '100', '', '7.5']
do inputs >> map_by(v ~> {
  raw: v,
  parsed: Integer(v) |? null,
  ok: (Integer(v) |? null) != null
})
```

**Output**

```json
[
  {"raw": "42", "parsed": 42, "ok": true},
  {"raw": "bad", "parsed": null, "ok": false},
  {"raw": "100", "parsed": 100, "ok": true},
  {"raw": "", "parsed": null, "ok": false},
  {"raw": "7.5", "parsed": null, "ok": false}
]
```

The try-fallback operator [|?](/en/wel/language/operators#error-fallback) catches the conversion error per element, so one unparseable value produces a `null` for that record instead of stopping the whole batch.

## Generate output formats

The following solutions safely build a string in a format another system expects:

### Build a SOQL query without breaking on special characters

A search term entered by a user can contain characters that would otherwise break out of the query's string literal.

**Formula**

```text
let search = "O'Brien & Sons"
do "SELECT Id, Name FROM Account WHERE Name = '" ++ escape_for_soql(search) ++ "'"
```

**Output**

```text
SELECT Id, Name FROM Account WHERE Name = 'O\'Brien & Sons'
```

[escape\_for\_soql](/en/wel/stdlib/escape#escape-for-soql) escapes only the search value and preserves the surrounding query syntax. The escaped apostrophe can't terminate the string literal.

### Build CSV rows from structured data

A destination expects a CSV file, and some field values contain commas. Escape these values so the commas don't act as column separators.

**Formula**

```text
let records = [
  {name: 'Dana', email: 'dana@co.com', amount: 100},
  {name: 'Kai, Jr.', email: 'kai@co.com', amount: 250}
]
do let header = 'Name,Email,Amount'
do let rows = records
    >> map_by(r ~> escape_for_csv(r.name) ++ ',' ++ r.email ++ ',' ++ String(r.amount))
do [header] ++ rows >> join_to_string('\n')
```

**Output**

```text
Name,Email,Amount
Dana,dana@co.com,100
"Kai, Jr.",kai@co.com,250
```

[escape\_for\_csv](/en/wel/stdlib/escape#escape-for-csv) quotes only the field containing a comma, `"Kai, Jr."`, so it survives as one column instead of splitting into two.

### Issue a JWT for API authentication

An outbound API call needs a signed, time-limited token proving who issued it.

**Formula**

```text
let issued_at = now() >> to_epoch >> floor,
    key = '0123456789abcdef0123456789abcdef'
do let payload = {sub: 'service-account', iat: issued_at, exp: issued_at + 3600}
do let token = jwt_encode(payload, key, 'HS256')
do {
  authorization: 'Bearer ' ++ token,
  decoded: jwt_decode(token, key, 'HS256')
}
```

**Output**

```text
{
  authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  decoded: {header: {alg: "HS256", typ: "JWT"}, payload: {sub: "service-account", iat: ..., exp: ...}}
}
```

Use at least 32 random bytes from a secure secret store for the key in production. Refer to [jwt\_encode](/en/wel/stdlib/crypto#jwt-encode) for why `HS256` enforces that minimum.

### Generate a numbered list of items

A list of items needs rendering as numbered, uppercased lines for a plain-text report.

**Formula**

```text
let items = ['alpha', 'beta', 'gamma', 'delta']
do items
  >> map_with_index_by((item, i) ~> String(i + 1) ++ '. ' ++ upper(item))
  >> join_to_string('\n')
```

**Output**

```text
1. ALPHA
2. BETA
3. GAMMA
4. DELTA
```

[map\_with\_index\_by](/en/wel/stdlib/list#map-with-index-by) supplies the zero-based position alongside each element, deriving the line number instead of tracking it separately.

## Structure expressions

The following solutions use WEL's own constructs, `Skip` and `fun`, to keep an expression clean:

### Map fields conditionally, omitting some with Skip

An outbound record should omit a field entirely when it's blank, and not forward an internal field at all.

**Formula**

```text
let src = {name: 'Dana', nickname: '', age: 30, internal_id: 'x-123'}
do {
  name: src.name,
  nickname: if not blank?(src.nickname) then src.nickname else Skip,
  age: src.age,
  internal_id: Skip
}
```

**Output**

```json
{"name": "Dana", "age": 30}
```

[Skip](/en/wel/language/data-types#null-and-skip) removes a key from the result entirely, which is why `nickname` and `internal_id` are both absent rather than present as `null`.

### Reuse logic with a named function

The same masking rule applies to more than one field. Name it once instead of writing the same lambda out repeatedly.

**Formula**

```text
fun mask = s ~>
  if length(s) > 4
  then substring(s, 0, 2) ++ '***' ++ substring(s, length(s) - 2, 2)
  else '****'
do let records = [{name: 'Dana', ssn: '123-45-6789'}, {name: 'Kai', ssn: '987-65-4321'}]
do records >> map_by(r ~> {name: r.name, ssn: mask(r.ssn)})
```

**Output**

```json
[{"name": "Dana", "ssn": "12***89"}, {"name": "Kai", "ssn": "98***21"}]
```

[fun](/en/wel/language/expressions#fun) binds the masking rule to a name once, so both records apply the same logic instead of writing it twice.

## Related

- [Quickstart](/en/wel/quickstart): An example showing different WEL workflows.
- [Standard library](/en/wel/stdlib): More information about every function used on this page.
- [Data types](/en/wel/language/data-types): The data types these solutions convert between.
- [Error codes](/en/wel/errors): Troubleshoot a failing expression.

---
