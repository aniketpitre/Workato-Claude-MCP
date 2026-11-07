---
url: 'https://docs.workato.com/en/wel/stdlib/temporal.md'
description: >-
  WEL temporal functions for reading date and time components, calendar and
  clock arithmetic, period boundaries, time zones, and durations, with examples.
---

# Temporal functions

Temporal functions read, calculate with, and move between dates, times, instants, and durations. This is the largest category in the standard library. It's also where the most integration bugs live, such as a report that is off by one day, an SLA that fires an hour late twice a year, or a date that changes when it crosses a system boundary.

> **FEATURE AVAILABILITY**
> 
> WEL is currently available to select customers. Contact your Customer Success Representative to confirm whether it is available in your workspace.

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

```text
year(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the year from a calendar date

The following example returns the year from a calendar date:

**Formula**

```text
year(PlainDate('2026-03-15'))
```

**Output**

```text
2026
```

### `month`

Returns the month as a number from 1 to 12.

```text
month(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the month number from a calendar date

The following example returns the month number from a calendar date:

**Formula**

```text
month(PlainDate('2026-03-15'))
```

**Output**

```text
3
```

### `day`

Returns the day of the month, from 1 to 31.

```text
day(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the day of the month from a calendar date

The following example returns the day of the month from a calendar date:

**Formula**

```text
day(PlainDate('2026-03-15'))
```

**Output**

```text
15
```

### `quarter`

Returns the calendar quarter, from 1 to 4.

```text
quarter(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the calendar quarter from a date

The following example returns the calendar quarter from a date:

**Formula**

```text
quarter(PlainDate('2026-03-15'))
```

**Output**

```text
1
```

### `day_of_year`

Returns the day of the year, from 1 to 366.

```text
day_of_year(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the day number within the year

The following example returns the day number within the year:

**Formula**

```text
day_of_year(PlainDate('2026-03-15'))
```

**Output**

```text
74
```

### `day_of_week`

Returns the day of the week from 1 to 7, where 1 is the _locale's_ first day of the week.

That makes the number locale-dependent: the same date is `1` where the week starts on Sunday and `7` where it starts on Monday. Prefer an explicit comparison against `day_of_week_name`, or confirm the recipe's locale, when the number is going into a destination system.

```text
day_of_week(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the day of the week as a locale-dependent number

The following example returns the day of the week as a locale-dependent number:

**Formula**

```text
day_of_week(PlainDate('2026-03-15'))
```

**Output**

```text
1
```

### `day_of_week_name`

Returns the localized name of the day.

```text
day_of_week_name(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the localized name of the day

The following example returns the localized name of the day:

**Formula**

```text
day_of_week_name(PlainDate('2026-03-15'))
```

**Output**

```text
Sunday
```

### `month_name`

Returns the localized name of the month.

```text
month_name(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, or `PlainDateTime`. |

Return the localized name of the month

The following example returns the localized name of the month:

**Formula**

```text
month_name(PlainDate('2026-03-15'))
```

**Output**

```text
March
```

### `hour`

Returns the hour, from 0 to 23.

```text
hour(value)
```

| Parameter | Description |
| --- | --- |
| value | A `DateTime`, `PlainDateTime`, or `PlainTime`. |

Return the hour from a timestamp

The following example returns the hour from a timestamp:

**Formula**

```text
hour(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```text
9
```

### `minute`

Returns the minute, from 0 to 59.

```text
minute(value)
```

| Parameter | Description |
| --- | --- |
| value | A `DateTime`, `PlainDateTime`, or `PlainTime`. |

Return the minute from a timestamp

The following example returns the minute from a timestamp:

**Formula**

```text
minute(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```text
30
```

### `second`

Returns the second as a `Decimal`, so fractional precision is preserved.

```text
second(value)
```

| Parameter | Description |
| --- | --- |
| value | A `DateTime`, `PlainDateTime`, or `PlainTime`. |

Return the second from a timestamp

The following example returns the second from a timestamp:

**Formula**

```text
second(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```text
45
```

### `time`

Returns the wall-clock time as a `PlainTime`. With a time zone argument, it returns the local time in that zone instead.

```text
time(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | A `DateTime` or `PlainDateTime`. |
| timezone | Optional IANA time zone name. |

Return the wall-clock time with no time zone given

The following example returns the wall-clock time with no time zone given:

**Formula**

```text
time(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```text
09:30:45
```

Return the wall-clock time as read in Tokyo

The following example returns the wall-clock time as read in Tokyo:

**Formula**

```text
time(DateTime('2026-03-15T09:30:45Z'), 'Asia/Tokyo')
```

**Output**

```text
18:30:45
```

### `to_map`

Decomposes any temporal value, including `Duration`, into a map of its components.

```text
to_map(value)
```

| Parameter | Description |
| --- | --- |
| value | A `PlainDate`, `DateTime`, `PlainDateTime`, `PlainTime`, or `Duration`. |

Decompose a calendar date into its components

The following example decomposes a calendar date into its components:

**Formula**

```text
to_map(PlainDate('2026-03-15'))
```

**Output**

```text
{year: 2026, month: 3, day: 15}
```

Decompose a duration into its components

The following example decomposes a duration into its components:

**Formula**

```text
to_map(Duration('PT2H30M'))
```

**Output**

```text
{hours: 2, minutes: 30, seconds: 0}
```

## Calendar arithmetic

A calendar month and 30 days aren't the same increment. The difference shows up at the end of the month. These two functions handle that case differently.

### `add_months`

Adds a number of months, _clamping_ to the end of the month when the target has fewer days. Equivalent to the `EDATE` function in Excel.

January 31 plus one month is February 28, or 29 in a leap year. Use this when a business rule means "the same date next month, or the last day if there isn't one," which describes most billing and subscription rules.

```text
add_months(date, months)
```

| Parameter | Description |
| --- | --- |
| date | The `PlainDate` to advance. |
| months | The number of months to add. A negative value moves the date backward instead. |

Clamp to the last day of a shorter month

The following example clamps to the last day of a shorter month:

**Formula**

```text
add_months(PlainDate('2026-01-31'), 1)
```

**Output**

```text
2026-02-28
```

Move a date backward with a negative months value

The following example moves a date backward using a negative number of months:

**Formula**

```text
add_months(PlainDate('2026-03-15'), -2)
```

**Output**

```text
2026-01-15
```

### `advance_date`

Advances a `PlainDate` by any combination of years, months, and days.

`advance_date` _raises an error_ rather than clamping when the result wouldn't be a real date, unlike `add_months`. Use it when an impossible date means the input was wrong and you would rather the job fail than silently move the day.

```text
advance_date(date, delta)
```

| Parameter | Description |
| --- | --- |
| date | The `PlainDate` to advance. |
| delta | A map with any of `years`, `months`, `days`. An unrecognized key raises `E222`. |

Advance a date by a number of days

The following example advances a date by a number of days:

**Formula**

```text
advance_date(PlainDate('2026-03-15'), {days: 10})
```

**Output**

```text
2026-03-25
```

Advance a date by years and months together

The following example advances a date by years and months together:

**Formula**

```text
advance_date(PlainDate('2026-03-15'), {years: 1, months: 2})
```

**Output**

```text
2027-05-15
```

### `date_diff`

Decomposes the gap between two dates into years, months, and days.

`date_diff` measures _from the first date to the second_, so a second date that is earlier gives negative components.

```text
date_diff(from, to)
```

| Parameter | Description |
| --- | --- |
| from | The starting `PlainDate`. |
| to | The ending `PlainDate`. |

Measure the gap from an earlier date to a later one

The following example measures the gap from an earlier date to a later one:

**Formula**

```text
date_diff(PlainDate('2025-01-10'), PlainDate('2026-03-15'))
```

**Output**

```text
{years: 1, months: 2, days: 5}
```

Measure the gap from a later date to an earlier one

The following example measures the gap from a later date to an earlier one, which gives negative components:

**Formula**

```text
date_diff(PlainDate('2026-03-15'), PlainDate('2025-01-10'))
```

**Output**

```text
{years: -1, months: -2, days: -5}
```

### `advance_datetime`

Advances a `DateTime` by years, months, days, hours, minutes, or seconds, in a given time zone.

```text
advance_datetime(datetime, delta, timezone, on_gap, on_fold)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to advance. |
| delta | A map with any of `years`, `months`, `days`, `hours`, `minutes`, `seconds`. An unrecognized key raises `E222`. |
| timezone | Optional IANA time zone in which to do the calendar arithmetic. |
| on\_gap | Optional. How to resolve a local time that a daylight-saving change skipped. |
| on\_fold | Optional. How to resolve a local time that a daylight-saving change repeated. |

Advance a datetime by hours

The following example advances a datetime by hours:

**Formula**

```text
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

```text
datetime_add_duration(datetime, duration, timezone, on_gap, on_fold)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to advance. |
| duration | An ISO 8601 duration string. |
| timezone | Optional IANA time zone. |
| on\_gap, on\_fold | Optional daylight-saving resolution. |

Add a clock duration to a datetime

The following example adds a clock duration to a datetime:

**Formula**

```text
datetime_add_duration(DateTime('2026-03-15T09:30:00Z'), 'PT2H')
```

**Output**

```text
2026-03-15T11:30:00Z
```

### `datetime_sub_duration`

Subtracts a duration from a `DateTime`. Takes the same arguments as `datetime_add_duration`.

```text
datetime_sub_duration(datetime, duration, timezone, on_gap, on_fold)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to move back. |
| duration | An ISO 8601 duration string. |
| timezone | Optional IANA time zone. |
| on\_gap, on\_fold | Optional daylight-saving resolution. |

Subtract a calendar duration from a datetime

The following example subtracts a calendar duration from a datetime:

**Formula**

```text
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

```text
until(from, to)
```

| Parameter | Description |
| --- | --- |
| from | The starting `DateTime`. |
| to | The ending `DateTime`. |

Measure the duration from an earlier instant to a later one

The following example measures the duration from an earlier instant to a later one:

**Formula**

```text
until(DateTime('2026-03-15T09:00:00Z'), DateTime('2026-03-15T11:30:00Z'))
```

**Output**

```text
PT2H30M
```

### `since`

Returns the signed duration between two instants, taking the _second from the first_, the opposite argument order to `until`.

`since(now(), created_at)` matches how the question is normally phrased: "how long since it was created?"

```text
since(later, earlier)
```

| Parameter | Description |
| --- | --- |
| later | The `DateTime` to measure from. |
| earlier | The `DateTime` to measure to. |

Measure how long has passed since an earlier instant

The following example measures how long has passed since an earlier instant:

**Formula**

```text
since(DateTime('2026-03-15T11:30:00Z'), DateTime('2026-03-15T09:00:00Z'))
```

**Output**

```text
PT2H30M
```

### `in_hours`, `in_minutes`, `in_seconds`, `in_days`

Convert a `Duration` to a whole number of the named unit, truncating rather than rounding. `PT150M` is `2` hours, not `3`.

```text
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

```text
in_hours(Duration('PT150M'))
```

**Output**

```text
2
```

Convert a duration to whole minutes

The following example converts a duration to whole minutes:

**Formula**

```text
in_minutes(Duration('PT2H30M'))
```

**Output**

```text
150
```

Convert a duration to whole seconds

The following example converts a duration to whole seconds:

**Formula**

```text
in_seconds(Duration('PT1M30S'))
```

**Output**

```text
90
```

Convert a duration to whole days

The following example converts a duration to whole days:

**Formula**

```text
in_days(Duration('PT72H'))
```

**Output**

```text
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

```text
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

Each accepts no arguments for the current instant in UTC, one argument for a supplied value, or two for a `DateTime` and a time zone.

### `start_of_day` and `end_of_day`

Return the first and last instant of the calendar day.

```text
start_of_day(datetime)
end_of_day(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | Optional `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone. |

Find the first instant of the day

The following example finds the first instant of the day:

**Formula**

```text
start_of_day(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
2026-03-15T00:00:00Z
```

Find the last instant of the day

The following example finds the last instant of the day:

**Formula**

```text
end_of_day(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
2026-03-15T23:59:59.999999999Z
```

`end_of_day` is the last representable instant of the day, not the following midnight, so a `<=` comparison against it includes the whole day without also catching the next one.

### `start_of_hour`

Returns the first instant of the hour.

```text
start_of_hour(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | Optional `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone. |

Find the first instant of the hour

The following example finds the first instant of the hour:

**Formula**

```text
start_of_hour(DateTime('2026-03-15T09:30:45Z'))
```

**Output**

```text
2026-03-15T09:00:00Z
```

### `start_of_week` and `end_of_week`

These functions are locale-aware. Which day the week starts on depends on the recipe's locale.

```text
start_of_week(value)
end_of_week(value, timezone)
```

| Parameter | Description |
| --- | --- |
| value | Optional `PlainDate` or `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone, when the value is a `DateTime`. |

Find the first day of the week

The following example finds the first day of the week:

**Formula**

```text
start_of_week(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-15
```

Find the last day of the week

The following example finds the last day of the week:

**Formula**

```text
end_of_week(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-21
```

### `start_of_month` and `end_of_month`

Return the first and last day of the calendar month.

```text
start_of_month(value)
end_of_month(value, timezone)
```

| Parameter | Description |
| --- | --- |
| value | Optional `PlainDate` or `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone, when the value is a `DateTime`. |

Find the first day of the month

The following example finds the first day of the month:

**Formula**

```text
start_of_month(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-01
```

Find the last day of the month

The following example finds the last day of the month:

**Formula**

```text
end_of_month(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-31
```

### `start_of_quarter` and `end_of_quarter`

Return the first and last day of the calendar quarter.

```text
start_of_quarter(value)
end_of_quarter(value, timezone)
```

| Parameter | Description |
| --- | --- |
| value | Optional `PlainDate` or `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone, when the value is a `DateTime`. |

Find the first day of the quarter

The following example finds the first day of the quarter:

**Formula**

```text
start_of_quarter(PlainDate('2026-03-15'))
```

**Output**

```text
2026-01-01
```

Find the last day of the quarter

The following example finds the last day of the quarter:

**Formula**

```text
end_of_quarter(PlainDate('2026-03-15'))
```

**Output**

```text
2026-03-31
```

### `start_of_year` and `end_of_year`

Return the first and last day of the calendar year.

```text
start_of_year(value)
end_of_year(value, timezone)
```

| Parameter | Description |
| --- | --- |
| value | Optional `PlainDate` or `DateTime`. Defaults to now, in UTC. |
| timezone | Optional IANA time zone, when the value is a `DateTime`. |

Find the first day of the year

The following example finds the first day of the year:

**Formula**

```text
start_of_year(PlainDate('2026-03-15'))
```

**Output**

```text
2026-01-01
```

Find the last day of the year

The following example finds the last day of the year:

**Formula**

```text
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

```text
{
  from: start_of_month(PlainDate(now())),
  to: end_of_month(PlainDate(now()))
}
```

**Output**

```json
{"from": "2026-07-01", "to": "2026-07-31"}
```

This example uses `now()` at `2026-07-12T12:34:56.789Z`. Convert to `PlainDate` first: reporting APIs expect calendar dates, and an instant's day depends on the reader's zone.

## Time zones

The following functions convert a `DateTime` between time zones and inspect its offset:

### `in_tz`

Re-renders the same instant in another time zone. The instant doesn't change, only how it reads.

```text
in_tz(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to re-render. |
| timezone | An IANA time zone name, such as `Asia/Tokyo`. |

Re-render an instant in another time zone

The following example re-renders an instant in another time zone:

**Formula**

```text
in_tz(DateTime('2026-03-15T09:30:00Z'), 'Asia/Tokyo')
```

**Output**

```text
2026-03-15T18:30:00+09:00
```

### `assume_tz`

Interprets a `PlainDateTime`'s wall-clock reading as occurring in a given time zone, producing a `DateTime`.

`assume_tz` is the opposite direction to `in_tz`. `in_tz` keeps the instant and changes the reading. `assume_tz` keeps the reading and determines the instant. Use it when a source system sends a local time and tells you the zone separately.

```text
assume_tz(plain_datetime, timezone, on_gap, on_fold)
```

| Parameter | Description |
| --- | --- |
| plain\_datetime | The reading, with no zone. |
| timezone | An IANA time zone name. |
| on\_gap | Optional. How to resolve a time that a daylight-saving change skipped. |
| on\_fold | Optional. How to resolve a time that a daylight-saving change repeated. |

Interpret a wall-clock reading as occurring in a given time zone

The following example interprets a wall-clock reading as occurring in a given time zone:

**Formula**

```text
assume_tz(PlainDateTime('2026-03-15T09:30:00'), 'Europe/London')
```

**Output**

```text
2026-03-15T09:30:00Z
```

### `utc_offset`

Returns the offset from UTC as a canonical string: `Z`, or a signed offset such as `+02:00`.

```text
utc_offset(datetime)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to inspect. |

Get the offset for an instant in UTC

The following example gets the offset for an instant in UTC:

**Formula**

```text
utc_offset(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
Z
```

Get the offset after converting to another time zone

The following example gets the offset after converting to another time zone:

**Formula**

```text
utc_offset(in_tz(DateTime('2026-07-15T09:30:00Z'), 'Asia/Tokyo'))
```

**Output**

```text
+09:00
```

### `is_dst?`

Returns `true` if daylight saving time is in effect at that instant in that zone.

```text
is_dst?(datetime, timezone)
```

| Parameter | Description |
| --- | --- |
| datetime | The instant to test. |
| timezone | An IANA time zone name. |

Detect daylight saving time in effect

The following example detects daylight saving time in effect during summer in London:

**Formula**

```text
is_dst?(DateTime('2026-07-15T09:30:00Z'), 'Europe/London')
```

**Output**

```text
true
```

Detect standard time with no daylight saving in effect

The following example detects standard time in London during winter, with no daylight saving in effect:

**Formula**

```text
is_dst?(DateTime('2026-01-15T09:30:00Z'), 'Europe/London')
```

**Output**

```text
false
```

### `observes_dst?`

Returns `true` if the time zone observes daylight saving at all, in a given year.

```text
observes_dst?(timezone)
observes_dst?(timezone, year)
```

| Parameter | Description |
| --- | --- |
| timezone | An IANA time zone name. |
| year | Optional year. Defaults to the current year. |

Check a time zone that observes daylight saving

The following example checks a time zone that observes daylight saving:

**Formula**

```text
observes_dst?('Europe/London')
```

**Output**

```text
true
```

Check a time zone that doesn't observe daylight saving

The following example checks a time zone that doesn't observe daylight saving:

**Formula**

```text
observes_dst?('Asia/Tokyo')
```

**Output**

```text
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

```text
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

```text
now()
```

### `epoch`

Builds a `DateTime` from Unix epoch seconds.

```text
epoch(seconds)
```

| Parameter | Description |
| --- | --- |
| seconds | Unix epoch seconds. |

Build a datetime from Unix epoch seconds

The following example builds a datetime from Unix epoch seconds:

**Formula**

```text
epoch(1773567000)
```

**Output**

```text
2026-03-15T09:30:00Z
```

### `to_epoch`

Converts a `DateTime` to Unix epoch seconds, as a `Decimal` so nanosecond precision survives.

```text
to_epoch(datetime)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to convert. |

Convert a datetime to Unix epoch seconds

The following example converts a datetime to Unix epoch seconds:

**Formula**

```text
to_epoch(DateTime('2026-03-15T09:30:00Z'))
```

**Output**

```text
1773567000
```

### `to_iso8601`

Formats a `DateTime` as ISO 8601 with its offset.

```text
to_iso8601(datetime)
```

| Parameter | Description |
| --- | --- |
| datetime | The `DateTime` to format. |

Format a datetime as ISO 8601

The following example formats a datetime as ISO 8601:

**Formula**

```text
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
- [Error codes](/en/wel/errors): Troubleshoot job failures such as `E020` and `E222`.

---
