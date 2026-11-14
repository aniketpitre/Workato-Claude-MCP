---
url: 'https://docs.workato.com/en/wel/stdlib/temporal.md'
description: >-
  Use WEL temporal functions to read date and time components, perform calendar
  and clock arithmetic, find period boundaries, and handle time zones and
  durations, with examples.
---

# Temporal functions

Temporal functions read, calculate with, and move between dates, times, instants, and durations. This is the largest category in the standard library. It's also where the most integration bugs live, such as a report that is off by one day, an SLA that fires an hour late twice a year, or a date that changes when it crosses a system boundary.

## Pick the right type first

Most temporal bugs are a type choice, not a function choice. WEL separates an instant from a wall-clock reading, and the separation is what prevents the classic errors.

| Type | Use case | Literal |
| --- | --- | --- |
| `DateTime` | Record the specific time of an event with a timezone, such as the time something was created, shipped, or logged. | `DateTime('2026-03-15T09:30:00Z')` |
| `PlainDate` | Record a calendar date without a timezone that's the same for everyone looking at it, such as an invoice date, a birth date, or a contract start date. | `PlainDate('2026-03-15')` |
| `PlainTime` | Record a time of day with no date attached and no timezone, such as a store's opening time or a daily cutoff. | `PlainTime('09:30:00')` |
| `PlainDateTime` | Record a wall-clock reading before its time zone is known, such as a local time a source system sends with the zone supplied separately. | `PlainDateTime('2026-03-15T09:30:00')` |
| `Duration` | Record a length of time, such as an age, an elapsed interval between two events, or a timeout. | `Duration('PT2H30M')` |

> **USE PLAINDATE TO IGNORE TIMEZONES**
> 
> The same point in time can have different dates across timezones. For example, `2026-03-15T00:00:00Z` is the 15th at 9am in Tokyo and the _14th_ at 5pm in Los Angeles.
> 
> A `PlainDate` has no timezone, so it reads as the same date for everyone. Storing an invoice date as a `DateTime` instead of a `PlainDate` is the most common source of off-by-one-day errors.

> **NOW() IS FIXED FOR THE WHOLE STEP**
> 
> `now()` returns the same instant everywhere in one Transform Data step, however many times you call it. An expression can't see the clock advance partway through, so two fields computed from `now()` are consistent with each other.

## Read a component

These take a `PlainDate`, `DateTime`, or `PlainDateTime` and return one part of it.

### `year`

Returns the year.

```wel
year(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the year from a calendar date

The following example returns the year from a calendar date:

**Formula**

```wel
year(PlainDate('2026-03-15'))
```

**Output**

```wel
2026
```

### `month`

Returns the month as a number from 1 to 12.

```wel
month(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the month number from a calendar date

The following example returns the month number from a calendar date:

**Formula**

```wel
month(PlainDate('2026-03-15'))
```

**Output**

```wel
3
```

### `day`

Returns the day of the month, from 1 to 31.

```wel
day(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the day of the month from a calendar date

The following example returns the day of the month from a calendar date:

**Formula**

```wel
day(PlainDate('2026-03-15'))
```

**Output**

```wel
15
```

### `quarter`

Returns the calendar quarter, from 1 to 4.

```wel
quarter(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the calendar quarter from a date

The following example returns the calendar quarter from a date:

**Formula**

```wel
quarter(PlainDate('2026-03-15'))
```

**Output**

```wel
1
```

### `day_of_year`

Returns the day of the year, from 1 to 366.

```wel
day_of_year(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the day number within the year

The following example returns the day number within the year:

**Formula**

```wel
day_of_year(PlainDate('2026-03-15'))
```

**Output**

```wel
74
```

### `day_of_week`

Returns the day of the week from 1 to 7, where 1 is the _locale's_ first day of the week.

That makes the number locale-dependent: The same date is `1` where the week starts on Sunday and `7` where it starts on Monday. Prefer an explicit comparison against `day_of_week_name`, or confirm the recipe's locale, when the number is going into a destination system.

```wel
day_of_week(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the day of the week as a locale-dependent number

The following example returns the day of the week as a locale-dependent number:

**Formula**

```wel
day_of_week(PlainDate('2026-03-15'))
```

**Output**

```wel
1
```

### `day_of_week_name`

Returns the localized name of the day.

```wel
day_of_week_name(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the localized name of the day

The following example returns the localized name of the day:

**Formula**

```wel
day_of_week_name(PlainDate('2026-03-15'))
```

**Output**

```text
Sunday
```

### `month_name`

Returns the localized name of the month.

```wel
month_name(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the localized name of the month

The following example returns the localized name of the month:

**Formula**

```wel
month_name(PlainDate('2026-03-15'))
```

**Output**

```text
March
```

### `hour`

Returns the hour, from 0 to 23.

```wel
hour(value)
```

| Parameter | Description |
| --- | --- |
| value | A `DateTime`, `PlainDateTime`, or `PlainTime`. A `PlainDate`, which has no time component, raises `E100`. |

Return the hour from a timestamp

The following example returns the hour from a timestamp:

**Formula**

```wel
hour(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```wel
9
```

### `minute`

Returns the minute, from 0 to 59.

```wel
minute(value)
```

| Parameter | Description |
| --- | --- |
| value | A `DateTime`, `PlainDateTime`, or `PlainTime`. A `PlainDate`, which has no time component, raises `E100`. |

Return the minute from a timestamp

The following example returns the minute from a timestamp:

**Formula**

```wel
minute(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```wel
30
```

### `second`

Returns the second as a `Decimal`, so fractional precision is preserved.

```wel
second(value)
```

| Parameter | Description |
| --- | --- |
| value | A `DateTime`, `PlainDateTime`, or `PlainTime`. A `PlainDate`, which has no time component, raises `E100`. |

Return the second from a timestamp

The following example returns the second from a timestamp:

**Formula**

```wel
second(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```wel
45
```

### `time`

Returns the wall-clock time as a `PlainTime`. With a time zone argument, it returns the local time in that zone instead.

```wel
time(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | A `DateTime` or `PlainDateTime`. A `PlainDate`, which has no time component, raises `E100`. |
| timezone | Optional IANA time zone name. Only applies to a `DateTime`. Passing `timezone` with a `PlainDateTime` raises `E100`. An unrecognized zone raises `E214`. |

Return the wall-clock time with no time zone given

The following example returns the wall-clock time with no time zone given:

**Formula**

```wel
time(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```text
09:30:45
```

Return the wall-clock time as read in Tokyo

The following example returns the wall-clock time as read in Tokyo:

**Formula**

```wel
time(DateTime('2026-03-15T09:30:45Z'), 'Asia/Tokyo')
```

**Output**

```text
18:30:45
```

### `to_map`

Decomposes any temporal value, including `Duration`, into a map of its components. A `DateTime`'s map also includes an `offset` key. A `Duration`'s `hours` component isn't capped at 24, so a 30-hour duration reports `hours: 30` rather than rolling over into days.

```wel
to_map(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, `PlainDateTime`, `PlainTime`, or `Duration`. |

Decompose a calendar date into its components

The following example decomposes a calendar date into its components:

**Formula**

```wel
to_map(PlainDate('2026-03-15'))
```

**Output**

```wel
{year: 2026, month: 3, day: 15}
```

Decompose a duration into its components

The following example decomposes a duration into its components:

**Formula**

```wel
to_map(Duration('PT2H30M'))
```

**Output**

```wel
{hours: 2, minutes: 30, seconds: 0}
```

## Calendar arithmetic

A calendar month and 30 days aren't the same increment. The difference shows up at the end of the month. These two functions handle that case differently.

### `add_months`

Adds a number of months, _clamping_ to the end of the month when the target has fewer days. Equivalent to the `EDATE` function in Excel.

January 31 plus one month is February 28, or 29 in a leap year. Use this when a business rule means "the same date next month, or the last day if there isn't one," which describes most billing and subscription rules.

```wel
add_months(date, months)
```

| Parameter | Description |
| --- | --- |
| date | The `PlainDate` to advance. |
| months | The number of months to add. A negative value moves the date backward instead. |

A result outside the years 1 to 9999 raises catchable `E211`.

Clamp to the last day of a shorter month

The following example clamps to the last day of a shorter month:

**Formula**

```wel
add_months(PlainDate('2026-01-31'), 1)
```

**Output**

```text
2026-02-28
```

Move a date backward with a negative months value

The following example moves a date backward using a negative number of months:

**Formula**

```wel
add_months(PlainDate('2026-03-15'), -2)
```

**Output**

```text
2026-01-15
```

### `advance_date`

Advances a `PlainDate` by any combination of years, months, and days.

`advance_date` raises catchable `E212` rather than clamping when the result wouldn't be a real date, unlike `add_months`. Use it when an impossible date means the input was wrong. A result outside the years 1 to 9999 raises `E211` instead.

```wel
advance_date(date, delta)
```

| Parameter | Description |
| --- | --- |
| date | The `PlainDate` to advance. |
| delta | A map with any of `years`, `months`, `days`. An unrecognized key raises `E225`. A non-integer data type raises `E218`. |

Advance a date by a number of days

The following example advances a date by a number of days:

**Formula**

```wel
advance_date(PlainDate('2026-03-15'), {days: 10})
```

**Output**

```text
2026-03-25
```

Advance a date by years and months together

The following example advances a date by years and months together:

**Formula**

```wel
advance_date(PlainDate('2026-03-15'), {years: 1, months: 2})
```

**Output**

```text
2027-05-15
```

### `date_diff`

Decomposes the gap between two dates into years, months, and days.

`date_diff` measures _from the first date to the second_, so a second date that is earlier gives negative components.

```wel
date_diff(from, to)
```

| Parameter | Description |
| --- | --- |
| from | The starting `PlainDate`. |
| to | The ending `PlainDate`. |

Measure the gap from an earlier date to a later one

The following example measures the gap from an earlier date to a later one:

**Formula**

```wel
date_diff(PlainDate('2025-01-10'), PlainDate('2026-03-15'))
```

**Output**

```wel
{years: 1, months: 2, days: 5}
```

Measure the gap from a later date to an earlier one

The following example measures the gap from a later date to an earlier one, which gives negative components:

**Formula**

```wel
date_diff(PlainDate('2026-03-15'), PlainDate('2025-01-10'))
```

**Output**

```wel
{years: -1, months: -2, days: -5}
```

### `advance_datetime`

Advances a `DateTime` by years, months, days, hours, minutes, or seconds, in a given time zone.

```wel
advance_datetime(datetime, delta, timezone, on_gap, on_fold)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to advance. |
| delta | A map with any of `years`, `months`, `days`, `hours`, `minutes`, `seconds`. An unrecognized key raises `E225`. A non-integer data type raises `E218`. |
| timezone | Optional IANA time zone in which to do the calendar arithmetic. An unrecognized zone raises `E214`. |
| on\_gap | Optional. How to resolve a local time that a daylight-saving change skipped. |
| on\_fold | Optional. How to resolve a local time that a daylight-saving change repeated. |

A result whose calendar date is out of range raises catchable `E212`.

Advance a datetime by hours

The following example advances a datetime by hours:

**Formula**

```wel
advance_datetime(DateTime('2026-03-15T09:30:00Z'), {hours: 5})
```

**Output**

```text
2026-03-15T14:30:00Z
```

## Duration arithmetic

The following functions add or subtract an ISO 8601 duration from a `DateTime`:

### `datetime_add_duration`

Adds a duration, written as an ISO 8601 string, to a `DateTime`.

Clock-only durations such as `PT2H` preserve the offset. Calendar durations such as `P1D` apply in the given time zone, or the locale's, so that "one day later" stays the same wall-clock time across a daylight-saving change.

```wel
datetime_add_duration(datetime, duration, timezone, on_gap, on_fold)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to advance. |
| duration | An ISO 8601 duration string. A malformed string raises catchable `E102`. |
| timezone | Optional IANA time zone. An unrecognized zone raises `E214`. |
| on\_gap, on\_fold | Optional daylight-saving resolution. |

A result whose calendar date is out of range raises catchable `E212`.

Add a clock duration to a datetime

The following example adds a clock duration to a datetime:

**Formula**

```wel
datetime_add_duration(DateTime('2026-03-15T09:30:00Z'), 'PT2H')
```

**Output**

```text
2026-03-15T11:30:00Z
```

### `datetime_sub_duration`

Subtracts a duration from a `DateTime`.

```wel
datetime_sub_duration(datetime, duration, timezone, on_gap, on_fold)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to advance. |
| duration | An ISO 8601 duration string. A malformed string raises catchable `E102`. |
| timezone | Optional IANA time zone. An unrecognized zone raises `E214`. |
| on\_gap, on\_fold | Optional daylight-saving resolution. |

Subtract a calendar duration from a datetime

The following example subtracts a calendar duration from a datetime:

**Formula**

```wel
datetime_sub_duration(DateTime('2026-03-15T09:30:00Z'), 'P1D')
```

**Output**

```text
2026-03-14T09:30:00Z
```

## Measure an interval

The following functions measure the interval between two instants, as a `Duration`:

### `until`

Returns the signed duration from the first instant to the second.

```wel
until(from, to)
```

| Parameter | Description |
| --- | --- |
| from | The starting `DateTime`. |
| to | The ending `DateTime`. |

Measure the duration from an earlier instant to a later one

The following example measures the duration from an earlier instant to a later one:

**Formula**

```wel
until(DateTime('2026-03-15T09:00:00Z'), DateTime('2026-03-15T11:30:00Z'))
```

**Output**

```text
PT2H30M
```

### `since`

Returns the signed duration between two instants, taking the _second from the first_, the opposite argument order to `until`.

`since(now(), created_at)` matches how the question is normally phrased: "how long since it was created?"

```wel
since(later, earlier)
```

| Parameter | Description |
| --- | --- |
| later | The `DateTime` to measure from. |
| earlier | The `DateTime` to measure to. |

Measure how long has passed since an earlier instant

The following example measures how long has passed since an earlier instant:

**Formula**

```wel
since(DateTime('2026-03-15T11:30:00Z'), DateTime('2026-03-15T09:00:00Z'))
```

**Output**

```text
PT2H30M
```

### `in_hours`, `in_minutes`, `in_seconds`, `in_days`

Convert a `Duration` to a whole number of the named unit, truncating rather than rounding. `PT150M` is `2` hours, not `3`.

```wel
in_days(duration)
in_hours(duration)
in_minutes(duration)
in_seconds(duration)
```

| Parameter | Description |
| --- | --- |
| duration | The `Duration` to convert. |

Convert a duration to whole hours, truncated

The following example converts a duration to whole hours, truncating the remainder:

**Formula**

```wel
in_hours(Duration('PT150M'))
```

**Output**

```wel
2
```

Convert a duration to whole minutes

The following example converts a duration to whole minutes:

**Formula**

```wel
in_minutes(Duration('PT2H30M'))
```

**Output**

```wel
150
```

Convert a duration to whole seconds

The following example converts a duration to whole seconds:

**Formula**

```wel
in_seconds(Duration('PT1M30S'))
```

**Output**

```wel
90
```

Convert a duration to whole days

The following example converts a duration to whole days:

**Formula**

```wel
in_days(Duration('PT72H'))
```

**Output**

```wel
3
```

> **DURATION() TAKES CLOCK DURATIONS ONLY**
> 
> The `Duration` constructor accepts the time part of an ISO 8601 duration: `PT2H`, `PT30M`, `PT72H`. It rejects calendar forms such as `P1D` and `P3DT12H` with `E020`. Write three days as `PT72H`.
> 
> `until` and `since` return clock durations for the same reason, so a two-week interval comes back as `PT336H`. Use `date_diff` on `PlainDate` values instead to express a gap in calendar terms.
> 
> The `datetime_add_duration` and `datetime_sub_duration` functions do accept calendar duration _strings_, because they apply them in a time zone.

### Use case: Flag tickets past their SLA

A support queue needs tickets flagged once they've been open too long. Measure each ticket's age against `now()` and mark the ones over 48 hours:

**Input**

```json
{
  "tickets": [
    {"id": "T-1", "created_at": "2026-07-09T08:00:00Z"},
    {"id": "T-2", "created_at": "2026-07-12T06:00:00Z"}
  ]
}
```

**Formula**

```wel
_.tickets >> map_by(t ~> {
  id: t.id,
  age_hours: in_hours(since(now(), DateTime(t.created_at))),
  breached: in_hours(since(now(), DateTime(t.created_at))) > 48
})
```

**Output**

```json
[
  {"id": "T-1", "age_hours": 76, "breached": true},
  {"id": "T-2", "age_hours": 6, "breached": false}
]
```

This example uses `now()` at `2026-07-12T12:34:56.789Z`. This formula computes `age_hours` and `breached` from the same instant, so they can't disagree, because `now()` is fixed for the whole step.

## Period boundaries

These snap a value to the start or end of a period, the usual way to build a reporting window or bucket records by month.

Each accepts no arguments for the current instant in UTC, one argument for a supplied value, or two for a `DateTime` and a time zone. Passing a time zone with a `PlainDate`, which carries no instant to convert, raises `E100`. A result outside the years 1 to 9999 raises `E211`.

### `start_of_day` and `end_of_day`

Return the first and last instant of the calendar day.

```wel
start_of_day(datetime)
end_of_day(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | Optional `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone. An unrecognized time zone raises `E214`. |

Find the first instant of the day

The following example finds the first instant of the day:

**Formula**

```wel
start_of_day(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
2026-03-15T00:00:00Z
```

Find the last instant of the day

The following example finds the last instant of the day:

**Formula**

```wel
end_of_day(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
2026-03-15T23:59:59.999999999Z
```

`end_of_day` is the last representable instant of the day, not the following midnight, so a `<=` comparison against it includes the whole day without also catching the next one.

### `start_of_hour`

Returns the first instant of the hour.

```wel
start_of_hour(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | Optional `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone. An unrecognized time zone raises `E214`. |

Find the first instant of the hour

The following example finds the first instant of the hour:

**Formula**

```wel
start_of_hour(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```text
2026-03-15T09:00:00Z
```

### `start_of_week` and `end_of_week`

These functions are locale-aware. Which day the week starts on depends on the recipe's locale.

```wel
start_of_week(value)
end_of_week(value, timezone)
```

| Parameter | Description |
| --- | --- |
| value | Optional `PlainDate` or `DateTime`. Defaults to now, in UTC. A result outside the years 1 to 9999 raises catchable `E211`. |
| timezone | Optional IANA time zone, when the value is a `DateTime`. An unrecognized time zone raises `E214`. |

Find the first day of the week

The following example finds the first day of the week:

**Formula**

```wel
start_of_week(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-15
```

Find the last day of the week

The following example finds the last day of the week:

**Formula**

```wel
end_of_week(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-21
```

### `start_of_month` and `end_of_month`

Return the first and last day of the calendar month.

```wel
start_of_month(value)
end_of_month(value, timezone)
```

| Parameter | Description |
| --- | --- |
| value | Optional `PlainDate` or `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone, when the value is a `DateTime`. An unrecognized time zone raises `E214`. |

Find the first day of the month

The following example finds the first day of the month:

**Formula**

```wel
start_of_month(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-01
```

Find the last day of the month

The following example finds the last day of the month:

**Formula**

```wel
end_of_month(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-31
```

### `start_of_quarter` and `end_of_quarter`

Return the first and last day of the calendar quarter.

```wel
start_of_quarter(value)
end_of_quarter(value, timezone)
```

| Parameter | Description |
| --- | --- |
| value | Optional `PlainDate` or `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone, when the value is a `DateTime`. An unrecognized time zone raises `E214`. |

Find the first day of the quarter

The following example finds the first day of the quarter:

**Formula**

```wel
start_of_quarter(PlainDate('2026-03-15'))
```

**Output**

```text
2026-01-01
```

Find the last day of the quarter

The following example finds the last day of the quarter:

**Formula**

```wel
end_of_quarter(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-31
```

### `start_of_year` and `end_of_year`

Return the first and last day of the calendar year.

```wel
start_of_year(value)
end_of_year(value, timezone)
```

| Parameter | Description |
| --- | --- |
| value | Optional `PlainDate` or `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone, when the value is a `DateTime`. An unrecognized time zone raises `E214`. |

Find the first day of the year

The following example finds the first day of the year:

**Formula**

```wel
start_of_year(PlainDate('2026-03-15'))
```

**Output**

```text
2026-01-01
```

Find the last day of the year

The following example finds the last day of the year:

**Formula**

```wel
end_of_year(PlainDate('2026-03-15'))
```

**Output**

```text
2026-12-31
```

### Use case: Build the current month's reporting window

A report needs the first and last day of the current calendar month. Build both from `now()` with `start_of_month` and `end_of_month`:

**Input**

```json
{}
```

**Formula**

```wel
{
  from: start_of_month(PlainDate(now())),
  to: end_of_month(PlainDate(now()))
}
```

**Output**

```json
{"from": "2026-07-01", "to": "2026-07-31"}
```

This example uses `now()` at `2026-07-12T12:34:56.789Z`. Convert to `PlainDate` first: Reporting APIs expect calendar dates, and an instant's day depends on the reader's zone.

## Time zones

The following functions convert a `DateTime` between time zones and inspect its offset:

### `in_tz`

Re-renders the same instant in another time zone. The instant doesn't change, only how it reads.

```wel
in_tz(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to re-render. A `PlainDateTime`, which carries no instant to re-render, raises `E100`. |
| timezone | An IANA time zone name, such as `Asia/Tokyo`. The match is case-insensitive. A fixed-offset or unrecognized name raises `E214`. |

Re-render an instant in another time zone

The following example re-renders an instant in another time zone:

**Formula**

```wel
in_tz(DateTime('2026-03-15T09:30:00Z'), 'Asia/Tokyo')
```

**Output**

```text
2026-03-15T18:30:00+09:00
```

### `assume_tz`

Interprets a `PlainDateTime`'s wall-clock reading as occurring in a given time zone, producing a `DateTime`.

`assume_tz` is the opposite direction to `in_tz`. `in_tz` keeps the instant and changes the reading. `assume_tz` keeps the reading and determines the instant. Use it when a source system sends a local time and tells you the zone separately.

```wel
assume_tz(plain_datetime, timezone, on_gap, on_fold)
```

| Parameter | Description |
| --- | --- |
| plain\_datetime | The reading, with no zone. A `DateTime`, which already carries a zone, raises `E100`. |
| timezone | An IANA time zone name. An unrecognized zone raises `E214`. |
| on\_gap | Optional. How to resolve a time that a daylight-saving change skipped. |
| on\_fold | Optional. How to resolve a time that a daylight-saving change repeated. |

Interpret a wall-clock reading as occurring in a given time zone

The following example interprets a wall-clock reading as occurring in a given time zone:

**Formula**

```wel
assume_tz(PlainDateTime('2026-03-15T09:30:00'), 'Europe/London')
```

**Output**

```text
2026-03-15T09:30:00Z
```

### `utc_offset`

Returns the offset from UTC as a canonical string: `Z`, or a signed offset such as `+02:00`. A historical offset that carries seconds prints as `+HH:MM:SS` instead.

```wel
utc_offset(datetime)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to inspect. |

Get the offset for an instant in UTC

The following example gets the offset for an instant in UTC:

**Formula**

```wel
utc_offset(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
Z
```

Get the offset after converting to another time zone

The following example gets the offset after converting to another time zone:

**Formula**

```wel
utc_offset(in_tz(DateTime('2026-07-15T09:30:00Z'), 'Asia/Tokyo'))
```

**Output**

```text
+09:00
```

### `is_dst?`

Returns `true` if daylight saving time is in effect at that instant in that zone.

```wel
is_dst?(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | The instant to test. Any offset the `DateTime` itself carries is ignored in favor of `timezone`. |
| timezone | An IANA time zone name. An unrecognized zone raises `E214`. |

Detect daylight saving time in effect

The following example detects daylight saving time in effect during summer in London:

**Formula**

```wel
is_dst?(DateTime('2026-07-15T09:30:00Z'), 'Europe/London')
```

**Output**

```wel
true
```

Detect standard time with no daylight saving in effect

The following example detects standard time in London during winter, with no daylight saving in effect:

**Formula**

```wel
is_dst?(DateTime('2026-01-15T09:30:00Z'), 'Europe/London')
```

**Output**

```wel
false
```

### `observes_dst?`

Returns `true` if the time zone observes daylight saving at all, in a given year. A one-time change to a zone's standard-time offset, such as a country abandoning daylight saving entirely, doesn't count as observing it.

```wel
observes_dst?(timezone)
observes_dst?(timezone, year)
```

| Parameter | Description |
| --- | --- |
| timezone | An IANA time zone name. An unrecognized zone raises `E214`. |
| year | Optional year. Defaults to the current year. A year outside the range 1 to 9999 raises `E211`. |

Check a time zone that observes daylight saving

The following example checks a time zone that observes daylight saving:

**Formula**

```wel
observes_dst?('Europe/London')
```

**Output**

```wel
true
```

Check a time zone that doesn't observe daylight saving

The following example checks a time zone that doesn't observe daylight saving:

**Formula**

```wel
observes_dst?('Asia/Tokyo')
```

**Output**

```wel
false
```

A one-time standard-time change doesn't count as observing daylight saving

Russia abandoned daylight saving permanently in 2014, shifting its standard-time offset instead. The following example confirms that one-time change doesn't count as observing daylight saving that year:

**Formula**

observes\_dst?('Europe/Moscow', 2014)

```

**Output**

false
```

### Use case: Report events on the local business date

Two events on the same UTC day fall on different calendar dates in Tokyo. Convert to the local zone before taking the date, or the daily report will be wrong for everything after 15:00 UTC:

**Input**

```json
{
  "events": [
    {"id": "E-1", "at": "2026-03-15T16:30:00Z"},
    {"id": "E-2", "at": "2026-03-15T09:30:00Z"}
  ]
}
```

**Formula**

```wel
_.events >> map_by(e ~> {
  id: e.id,
  tokyo_date: PlainDate(in_tz(DateTime(e.at), 'Asia/Tokyo'))
})
```

**Output**

```json
[
  {"id": "E-1", "tokyo_date": "2026-03-16"},
  {"id": "E-2", "tokyo_date": "2026-03-15"}
]
```

`E-1` moves to the 16th because 16:30 UTC is 01:30 the next morning in Tokyo. The raw UTC value's `PlainDate` would have reported both on the 15th instead.

## Current instant and epoch time

The following functions read the current instant, or convert to and from Unix epoch seconds:

### `now`

Returns the current instant with a UTC offset that's fixed for the whole step. It takes no arguments.

```wel
now()
```

### `epoch`

Builds a `DateTime` from Unix epoch seconds.

```wel
epoch(seconds)
```

| Parameter | Description |
| --- | --- |
| seconds | Unix epoch seconds, as an `Integer`, `Float`, or `Decimal`. Nanoseconds beyond `Decimal` precision are rounded. A result outside the years 1 to 9999 raises catchable `E211`. |

Build a datetime from Unix epoch seconds

The following example builds a datetime from Unix epoch seconds:

**Formula**

```wel
epoch(1773567000)
```

**Output**

```text
2026-03-15T09:30:00Z
```

### `to_epoch`

Converts a `DateTime` to Unix epoch seconds, as a `Decimal` so nanosecond precision survives.

```wel
to_epoch(datetime)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to convert. |

Convert a datetime to Unix epoch seconds

The following example converts a datetime to Unix epoch seconds:

**Formula**

```wel
to_epoch(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```wel
1773567000
```

### `to_iso8601`

Formats a `DateTime` as ISO 8601 with its offset. A fractional-second component prints with no trailing zeros.

```wel
to_iso8601(datetime)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to format. |

Format a datetime as ISO 8601

The following example formats a datetime as ISO 8601:

**Formula**

```wel
to_iso8601(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
2026-03-15T09:30:00Z
```

## Related

- [Conversion functions](/en/wel/stdlib/conversion): How to construct each data type, such as `DateTime`, `PlainDate`, and `Duration`.
- [Formatting functions](/en/wel/stdlib/formatting): `format_date`, `parse_datetime`, `to_rfc3339`.
- [Data types](/en/wel/language/data-types): More information about the temporal types.
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E020` and `E218`.

---
