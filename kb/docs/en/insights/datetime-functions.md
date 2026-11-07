---
url: 'https://docs.workato.com/en/insights/datetime-functions.md'
description: >-
  Use datetime functions in calculated columns to extract, modify, and calculate
  time-based values within Insights dashboards.
---

# Datetime functions

You can use the following datetime functions in [calculated columns](/en/insights/custom-columns) to extract, modify, and calculate time-based values within Insights dashboards.

> **ALIASES**
> 
> You can search for a function using its alias.
> 
> For example, if the function `date_diff` has the alias `datediff`:
> 
> - When you type `datedi`, Insights suggests the `date_diff` function.
> - When you type `datediff`, Insights rewrites it as `date_diff`.

> **NULL OPERANDS**
> 
> Insights uses the following logic for expressions that include `NULL` values:
> 
> - If the expression contains a `NULL` value, the result returned in the calculated column is also a `NULL` value.
> 
> For example, if one of the rows in the Start date column is `NULL`, then the result in the calculated column for that row is also `NULL`:
> 
> **Column expression** (required):
> 
> \= `date_diff("day",`{{Start date}}`, current_date())`

## current\_date

Returns the current date.

- **Return type**: `DATE`

```plaintext
current_date()
```

### Example

This example obtains the current date to determine the time elapsed from a project start date:

**Column expression** (required):

\= `date_diff("day",`{{Start date}}`, current_date())`

You can use this function to visualize the duration of ongoing projects.

## current\_time

Returns the current timestamp.

- **Return type**: `TIMESTAMP`
- **Aliases**: `now()`, `current_timestamp()`

```plaintext
current_time()
```

### Example

This example obtains the current timestamp to determine the time that an item has remained in cart:

**Column expression** (required):

\= `date_diff("hour",`{{Cart timestamp}}`, current_time())`

You can use this function to visualize how long an item has remained in a shopping cart.

## date\_add

Add a date or time interval to a date. Also works with timestamps.

- **Return type**: `DATE`, `TIMESTAMP`
- **Aliases**: `dateadd`, `timeadd`, `timestampadd`

```plaintext
date_add(interval_unit, interval_value, timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `interval_unit` | `VARCHAR` | The unit of the amount to add. Allowed values include `"second"`, `"minute"`, `"hour"`, `"day"`, `"month"`, and `"year"`. |
| `interval_value` | `BIGINT` | The quantity of the time to add. Use negative values to perform subtraction. |
| `timestamp` | `DATE`, `TIMESTAMP` | The date or timestamp to add to. |

### Example

This example adds contract duration to the start date to determine the contract end date:

**Column expression** (required):

\= `date_add("day", 45,`{{Contract start date}}`)`

You can use this function to visualize contract end dates.

> **HANDLING END-OF-MONTH DATES**
> 
> - **If the target month has fewer days than the original date**, the result is the last day of the target month.
>   
>   - For example, `date_add("month", 1, "2024-01-31")` returns `2024-02-29`.
> - **If the original date is the last day of the month and the target month has more days**, the result remains the last day of the target month.
>   
>   - For example, `date_add("month", 1, "2024-02-29")` returns `2024-03-31`.

## date\_diff

Returns the difference between two timestamps expressed in the specified unit.

- **Return type**: `BIGINT`
- **Aliases**: `datediff`, `timediff`, `timestampdiff`, `date_subtract`

```plaintext
date_diff(interval_unit, start, end)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `interval_unit` | `VARCHAR` | The unit to use for the difference. Allowed values include `"second"`, `"minute"`, `"hour"`, `"day"`, `"month"`, and `"year"`. |
| `start` | `DATE`, `TIMESTAMP` | The starting date or timestamp. |
| `end` | `DATE`, `TIMESTAMP` | The ending date or timestamp. |

### Example

This example finds the difference between start date and end date:

**Column expression** (required):

\= `date_diff("day",`{{Start date}}`,`{{End date}}`)`

You can use this function to visualize project durations.

## date\_trunc

Truncates a timestamp to the specified unit.

- **Return type**: `DATE`, `TIMESTAMP`
- **Alias**: `trunc`

```plaintext
date_trunc(interval_unit, timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `interval_unit` | `VARCHAR` | The smallest date part to preserve. Allowed values include `"second"`, `"minute"`, `"hour"`, `"day"`, `"month"`, `"quarter"`, and `"year"`. |
| `timestamp` | `DATE`, `TIMESTAMP` | The date or timestamp to truncate. |

### Example

This example truncates the order date to the month level:

**Column expression** (required):

\= `date_trunc("month",`{{Order date}}`)`

You can use this function to visualize monthly order volume for different years.

## date\_part

Extracts the specified date part from a timestamp.

- **Return type**: `BIGINT`
- **Alias**: `extract`

```plaintext
date_part(interval_unit, timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `interval_unit` | `VARCHAR` | The date part to extract. Allowed values include `"second"`, `"minute"`, `"hour"`, `"day"`, `"week"`, `"month"`, `"year"`, and `"day_of_week"`. If you provide `"week"`, the ISO week number (1–53) of the date is returned. A year can have 52 or 53 weeks. Each week starts on Monday and ends on Sunday. If you provide `"day_of_week"`, Monday = `1` and Sunday = `7`. |
| `timestamp` | `DATE`, `TIMESTAMP` | The date or timestamp to extract from. |

### Example

This example extracts the year from transaction timestamps:

**Column expression** (required):

\= `date_part("year",`{{Transaction date}}`)`

You can use this function to calculate the total revenue for each year.

## day\_of\_week

Returns the ISO day of the week where the value ranges from `1` (Monday) to `7` (Sunday).

- **Return type**: `BIGINT`
- **Alias**: `dayofweek`

```plaintext
day_of_week(timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `timestamp` | `DATE`, `TIMESTAMP` | The input date or timestamp. |

### Example

This example identifies the day of the week when an order was placed:

**Column expression** (required):

\= `day_of_week(`{{Order timestamp}}`)`

You can use this function to identify the day of the week with the highest order volume.

### Related to

- [`date_part("day_of_week", timestamp)`](#date-part)

## name\_of\_day

Returns the three-letter name of the weekday from the timestamp.

- **Return type**: `VARCHAR`
- **Alias**: `dayname`

```plaintext
name_of_day(timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `timestamp` | `DATE`, `TIMESTAMP` | The input date or timestamp. |

### Example

This example identifies the day of the week when an order was placed:

**Column expression** (required):

\= `name_of_day(`{{Order timestamp}}`)`

You can use this function to identify the day of the week with the highest order volume.

## name\_of\_month

Returns the three-letter name of the month from the timestamp.

- **Return type**: `VARCHAR`
- **Alias**: `monthname`

```plaintext
name_of_month(timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `timestamp` | `DATE`, `TIMESTAMP` | The input date or timestamp. |

### Example

This example identifies the month when an order was placed:

**Column expression** (required):

\= `name_of_month(`{{Order timestamp}}`)`

You can use this function to identify months with highest order volumes.

## hour

Extracts the hour from the timestamp.

- **Return type**: `BIGINT`

```plaintext
hour(timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `timestamp` | `TIMESTAMP` | The input timestamp. |

### Example

This example extracts the hour from chat timestamps:

**Column expression** (required):

\= `hour(`{{Session timestamp}}`)`

You can use this function to track peak customer support chat hours.

### Related to

- [`date_part("hour", timestamp)`](#date-part)

## day

Extracts the day of the month from the timestamp.

- **Return type**: `BIGINT`
- **Alias**: `dayofmonth`, `day_of_month`

```plaintext
day(timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `timestamp` | `DATE`, `TIMESTAMP` | The input date or timestamp. |

### Example

This example extracts the day from the visit date:

**Column expression** (required):

\= `day(`{{Visit date}}`)`

You can use this function to identify days in a month with higher traffic.

### Related to

- [`date_part("day", timestamp)`](#date-part)

## week

Extracts the ISO week of the year from the timestamp.

- **Return type**: `BIGINT`

```plaintext
week(timestamp)
```

  

> **ISO WEEK NUMBER**
> 
> The ISO week number of the date ranges from 1–53. A year can have 52 or 53 weeks. Each week starts on Monday and ends on Sunday.

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `timestamp` | `DATE`, `TIMESTAMP` | The input date or timestamp. |

### Example

This example extracts the week from timesheet submissions:

**Column expression** (required):

\= `week(`{{Work date}}`)`

You can use this function to track total work hours per week.

### Related to

- [`date_part("week", timestamp)`](#date-part)

## month

Extracts the month from the timestamp.

- **Return type**: `BIGINT`

```plaintext
month(timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `timestamp` | `DATE`, `TIMESTAMP` | The input date or timestamp. |

### Example

This example extracts the month from transaction timestamps:

**Column expression** (required):

\= `month(`{{Transaction timestamp}}`)`

You can use this function to calculate the total revenue for each month.

### Related to

- [`date_part("month", timestamp)`](#date-part)

## year

Extracts the year from the timestamp.

- **Return type**: `BIGINT`

```plaintext
year(timestamp)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `timestamp` | `DATE`, `TIMESTAMP` | The input date or timestamp. |

### Example

This example extracts the year of the enrollment date:

**Column expression** (required):

\= `year(`{{Enrollment date}}`)`

You can use this function to analyze yearly growth in students for the course.

### Related to

- [`date_part("year", timestamp)`](#date-part)

## add\_months

Adds or subtracts a specified number of months to the timestamp.

- **Return type**: `DATE`, `TIMESTAMP`

```plaintext
add_months(timestamp, num_months)
```

### Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `timestamp` | `DATE`, `TIMESTAMP` | The date or timestamp to add to. |
| `num_months` | `INTEGER` | The number of months to add. |

### Example

This example obtains the date six months after a contract start date:

**Column expression** (required):

\= `add_months(`{{Start date}}`, 6)`

You can use this function to determine and visualize contract end dates.

> **HANDLING END-OF-MONTH DATES**
> 
> - **If the target month has fewer days than the original date**, the result is the last day of the target month.
>   
>   - For example, `add_month(1, "2024-01-31")` returns `2024-02-29`.
> - **If the original date is the last day of the month and the target month has more days**, the result remains the last day of the target month.
>   
>   - For example, `add_month(1, "2024-02-29")` returns `2024-03-31`.

### Related to

- [`date_add("month", interval_value, timestamp)`](#date-add)

---
