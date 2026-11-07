---
url: 'https://docs.workato.com/en/formulas/date-formulas.md'
description: >-
  Learn how to use Workato date and datetime formulas to manipulate dates and
  perform date arithmetic with days, months, and years.
---

# Date formulas

Video guide: Learn how to transform dates with formula mode

[Video](https://www.youtube.com/embed/Saq5ybJauVM)

Workato supports a variety of date and datetime formulas.

Formulas in Workato are allowlisted Ruby methods. Syntax and functionality for these formulas are generally unchanged. Most formulas return an error and stop the job if the formula operates on nulls (expressed as `nil` in Ruby), except for `present?`, `presence`, and `blank?`.

You can refer to the Ruby documentation on [time](http://ruby-doc.org/core-2.3.3/Time.html) for more information. However, only allowlisted Ruby methods are supported. Contact your Customer Success Manager to request new formulas for the allowlist.

## Date arithmetic

Use the following keywords to perform arithmetic with date and datetime data:

- `seconds`
- `minutes`
- `days`
- `months`
- `years`

When combined with a formula, you can perform addition and subtraction.

### Sample usage

| Date Arithmetic | Output |
| --- | --- |
| "2020-01-01".to\_date + 2.days | "2020-01-03" |
| "2020-01-01".to\_date - 2.days | "2019-12-30" |
| "2020-01-01".to\_date + 2.months | "2020-03-01" |
| "2020-01-01".to\_date - 2.months | "2019-11-01" |
| "2020-01-01".to\_date + 2.years | "2022-01-01" |
| "2020-01-01".to\_date - 2.years | "2018-01-01" |

* * *

## `now`

Returns the time and date at runtime in US Pacific Time Zone (PST).

### Sample usage

| Formula | Result |
| --- | --- |
| now | "2022-02-01T07:00:00.000000-08:00" |
| now + 8.hours | "2022-02-01T15:00:00.000000-08:00" |
| now + 2.days | "2022-02-03T07:00:00.000000-08:00" |

### How it works

The formula calculates the timestamp when the job is processed. Each step using this formula returns the timestamp at which the step runs.

> **Output datapill**
> 
> If you only want the date without the time, try using the [today](/en/formulas/date-formulas#today) formula instead.

### See also

- [today](/en/formulas/date-formulas#today): Returns the date at runtime.
- [in\_time\_zone](/en/formulas/date-formulas#in-time-zone): Converts a time value to a different time zone.

* * *

## `today`

Returns the date at runtime in US Pacific Time Zone.

### Sample usage

| Formula | Result |
| --- | --- |
| today | "2022-02-01" |
| today + 8.hours | "2022-02-01T15:00:00.000000-08:00" |
| today + 2.days | "2022-02-03" |

### How it works

The formula calculates the timestamp when the job is processed. Each step using this formula returns the date at which the step runs.

> **Output datapill**
> 
> If you want the date and time, try using the [now](/en/formulas/date-formulas#now) formula instead.

### See also

- [now](/en/formulas/date-formulas#now): Returns the time and date at runtime.
- [in\_time\_zone](/en/formulas/date-formulas#in-time-zone): Converts a time value to a different time zone.

* * *

## `from_now`

Returns a future timestamp by a specified time duration. The timestamp is calculated at runtime.

### Syntax

Unit.from\_now

- Unit - A time value to offset.

### Sample usage

| Formula | Result |
| --- | --- |
| 30.seconds.from\_now | "2022-02-01T07:00:30.000000-08:00" |
| 2.months.from\_now | "2022-04-01T07:00:00.000000-08:00" |
| 3.days.from\_now | "2022-02-04T07:00:00.000000-08:00" |

### How it works

The formula calculates the current timestamp and offsets by a specified time duration. This timestamp is calculated when the job is processed. Each step using this formula returns a timestamp.

> **UNITS**
> 
> You can use any of the following units: `seconds`, `minutes`, `hours`, `days`, `months`, or `years`.

### See also

- [ago](/en/formulas/date-formulas#ago): Returns an earlier timestamp by a specified time duration.
- [now](/en/formulas/date-formulas#now): Returns the time and date at runtime.
- [today](/en/formulas/date-formulas#today): Returns the date at runtime.

* * *

## `ago`

Returns an earlier timestamp by a specified time duration. The timestamp is calculated at runtime.

### Syntax

Unit.ago

- Unit - A time value to offset.

### Sample usage

| Formula | Result |
| --- | --- |
| 2.months.ago | "2020-10-04 14:45:29 -0700" |
| 3.days.ago | "2020-12-01 14:45:29 -0700" |
| 30.seconds.ago | "2020-12-04 14:15:29 -0700" |

### How it works

The formula calculates the current timestamp and offsets by a specified time duration. This timestamp is calculated when the job is processed. Each step using this formula returns a timestamp for each step that runs.

> **Units**
> 
> You can use any of the following units: `seconds`, `minutes`, `hours`, `days`, `months`, or `years`.

### See also

- [from\_now](/en/formulas/date-formulas#from-now): Returns a future timestamp by a specified time duration.
- [now](/en/formulas/date-formulas#now): Returns the time and date at runtime.
- [today](/en/formulas/date-formulas#today): Returns the date at runtime.

* * *

## `wday`

Returns day of the week. Sunday returns 0, Monday returns 1.

### Syntax

Date.wday

- Date - A date or datetime datatype.

### Sample usage

| Example | Result |
| --- | --- |
| today.wday | 4 |
| "01/12/2020".to\_date(format:"DD/MM/YYYY").wday | 2 |

### How it works

The formula calculates the current day when the job is processed. The day of the week is converted into an integer output. Sunday = 0, Monday = 1.

> **Quicktip: Convert to date datatype**
> 
> This formula only works with date or datetime datatype. Use [to\_date](/en/formulas/date-formulas#to-date) to convert a string into a date datatype.

### See also

- [yday](/en/formulas/date-formulas#yday): Returns the day number of the year.
- [yweek](/en/formulas/date-formulas#yweek): Returns the week number of the year.

* * *

## `yday`

Returns day number of the year.

### Syntax

Date.yday

- Date - A date or datetime datatype.

### Sample usage

| Example | Result |
| --- | --- |
| today.yday | 338 |
| "2020-01-01".to\_date(format:"YYYY-MM-DD").yday | 1 |
| "2020-02-01".to\_date(format:"YYYY-MM-DD").yday | 32 |

### How it works

The formula calculates the current day when the job is processed. The day of the year is converted to an integer output.

> **Quicktip: Convert to date datatype**
> 
> This formula only works with date or datetime datatype. Use [to\_date](/en/formulas/date-formulas#to-date) to convert a string into a date datatype.

### See also

- [wday](/en/formulas/date-formulas#wday): Returns the day number of the week.
- [yweek](/en/formulas/date-formulas#yweek): Returns the week number of the year.

* * *

## `yweek`

Returns week number of the year.

### Syntax

Date.yweek

- Date - A date or datetime datatype.

### Sample usage

| Example | Result |
| --- | --- |
| today.yweek | 49 |
| "2020-01-01".to\_date(format:"YYYY-MM-DD").yweek | 1 |
| "2020-02-01".to\_date(format:"YYYY-MM-DD").yweek | 5 |

### How it works

The formula calculates the current day when the job is processed. The week of the year is converted to an integer output.

> **Quicktip: Convert to date datatype**
> 
> This formula only works with date or datetime datatype. Use [to\_date](/en/formulas/date-formulas#to-date) to convert a string into a date datatype.

### See also

- [wday](/en/formulas/date-formulas#wday): Returns the day number of the week.
- [yday](/en/formulas/date-formulas#yday): Returns the day number of the year.

* * *

## `beginning_of_hour`

Returns datetime for top-of-the-hour for a given datetime.

### Syntax

Datetime.beginning\_of\_hour

- Datetime - An input datetime.

### Sample usage

| Formula | Result |
| --- | --- |
| today.to\_time.beginning\_of\_hour | "2020-12-02T16:00:00.000000-07:00" |
| "2020-06-01T01:30:45.000000+00:00".to\_time.beginning\_of\_hour | "2020-06-01T01:00:00.000000+00:00" |
| "2020-06-01".to\_time.beginning\_of\_hour | "2020-06-01T00:00:00.000000+00:00" |

* * *

## `beginning_of_day`

Returns datetime for midnight on date of a given date/datetime.

### Syntax

Date.beginning\_of\_day

- Date - An input date or datetime.

### Sample usage

| Formula | Result |
| --- | --- |
| today.beginning\_of\_day | "2020-12-02T00:00:00.000000-07:00" |
| "2020-06-01".to\_date.beginning\_of\_day | "2020-06-01T00:00:00.000000+00:00" |
| "2020-06-01T01:30:45.000000+00:00".beginning\_of\_day | "2020-06-01T00:00:00.000000+00:00" |

* * *

## `beginning_of_week`

Returns date for the start of the week (Monday) for a given date/timestamp.

### Syntax

Date.beginning\_of\_week

- Date - An input date or datetime.

### Sample usage

| Formula | Result |
| --- | --- |
| today.beginning\_of\_week | "2020-11-30T00:00:00.000000+00:00" |
| "2020-06-01".to\_date.beginning\_of\_week | "2020-06-01T00:00:00.000000+00:00" |
| "2020-06-01T01:30:45.000000+00:00".beginning\_of\_week | "2020-06-01T00:00:00.000000+00:00" |

* * *

## `beginning_of_month`

Returns first day of the month for a given date/datetime.

### Syntax

Date.beginning\_of\_month

- Date - An input date or datetime.

### Sample usage

| Formula | Result |
| --- | --- |
| today.beginning\_of\_month | "2020-12-01T00:00:00.000000+00:00" |
| "2020-06-01".to\_date.beginning\_of\_month | "2020-06-01T00:00:00.000000+00:00" |
| "2020-06-01T01:30:45.000000+00:00".beginning\_of\_month | "2020-06-01T00:00:00.000000+00:00" |

* * *

## `beginning_of_year`

Returns first day of the year for a given date/datetime.

### Syntax

Date.beginning\_of\_year

- Date - An input date or datetime.

### Sample usage

| Formula | Result |
| --- | --- |
| today.beginning\_of\_year | "2020-01-01T00:00:00.000000+00:00" |
| "2020-06-01".to\_date.beginning\_of\_year | "2020-01-01T00:00:00.000000+00:00" |
| "2020-06-01T01:30:45.000000+00:00".beginning\_of\_year | "2020-01-01T00:00:00.000000+00:00" |

* * *

## `end_of_month`

Returns last day of the month for a given date/datetime. This formula will return a date or datetime based on the input data.

### Syntax

Date.end\_of\_month

- Date - An input date or datetime.

### Sample usage

| Formula | Result |
| --- | --- |
| today.end\_of\_month | "2020-12-31" |
| "2020-06-01".to\_date.end\_of\_month | "2020-06-30" |
| "2020-06-01T01:30:45.000000+00:00".to\_time.end\_of\_month | "2020-06-30T23:59:59.999999+00:00" |

* * *

## `strftime`

Returns a datetime input as a user-defined string.

### Syntax

Date.strftime(format)

- Date - An input date or datetime.
- format - The format of the user-defined datetime written as a string.

### Sample usage

| Formula | Result |
| --- | --- |
| "2020-06-05T17:13:27.000000-07:00".to\_date.strftime("%Y/%m/%d") | "2020/06/05" |
| "2020-06-05T17:13:27.000000-07:00".strftime("%Y-%m-%dT%H:%M:%S%z") | "2020-06-05T17:13:27-0700" |
| "2020-06-05T17:13:27.000000-07:00".strftime("%B %e, %l:%M%p") | "June 5, 5:13 pm" |
| "2020-06-05T17:13:27.000000-07:00".strftime("%A, %d %B %Y %k:%M") | "Friday, 05 June 2020 0:00" |

### Parameters

As previously shown, each code (`%B`, `%e`, `%I`, for example) refers to a specific element of `datetime`. You can also add static text and punctuation, such as commas (`,`), slashes (`/`), and colons (`:`). Refer to the following list of frequently used codes:

| Code | Meaning | Example (2020-06-05T17:13:27.000000-07:00) |
| --- | --- | --- |
| %Y | Year with century | 2020 |
| %m | Month with zero-prefix | 06 |
| %B | Full month name | June |
| %b | Abbreviated month name | Jun |
| %d | Day of the month with zero-prefix | 05 |
| %e | Day of the month without zero-prefix | 5 |
| %H | Hour of the day (24-hour) | 17 |
| %k | Hour of day without 0 prefix (24-hour) | 17 |
| %I (capital i) | Hour of the day (12-hour) | 05 |
| %l (lowercase L) | Hour of day without 0 prefix (12-hour) | 5 |
| %p | AM or PM | PM |
| %M | Minute of the hour | 13 |
| %S | Second of the minute | 27 |
| %L | Millisecond of the second | 000 |
| %z | Time zone offset from UTC | \-0700 |
| %:z | Time zone formatted offset from UTC | \-07:00 |
| %Z | Time zone abbrev. name | UTC |
| %A | Full day name | Friday |

To access the full list, check out the [Ruby documentation](http://ruby-doc.org/core-2.3.3/Time.html#method-i-strftime)

### How it works

Allows the user to define a datetime format. Returns the datetime input in the specified format.

> **Input datatype**
> 
> The input must be a date or datetime datatype. You can use the [to\_date](/en/formulas/date-formulas#to-date) formula to convert a string into a date datatype.

### See also

- [to\_date](/en/formulas/date-formulas#to-date): Returns a date in date datatype.

* * *

## `in_time_zone`

Converts a date or datetime to a different time zone using [IANA time zone names](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Returns a datetime.

### Syntax

Date.in\_time\_zone(timezone)

- Date - An input date or datetime.
- timezone - The target timezone name (optional). Refer to [Regions reference](/en/formulas/date-formulas#regions-reference) for valid timezone names.

### Behavior

The formula behaves differently depending on how you call it:

- **No argument** - Returns Pacific Time: `now.in_time_zone`
- **Timezone specified** - Converts to the specified timezone: `now.in_time_zone("America/New_York")`
- **Explicit nil** - Returns UTC timezone: `now.in_time_zone(nil)`

### Sample usage

| Formula | Result |
| --- | --- |
| today.in\_time\_zone("America/New\_York") | "2020-12-01T00:00:00.000000-05:00" |
| today.to\_time.in\_time\_zone("America/New\_York") | "2020-11-30T19:00:00.000000-05:00" |
| "2020-06-01".to\_time.in\_time\_zone | "2020-05-31T17:00:00.000000-07:00" |
| "2020-06-01T01:30:45.000000+00:00".in\_time\_zone | "2020-05-31T18:30:45.000000-07:00" |
| "2020-06-01T01:30:45.000000-07:00".in\_time\_zone(nil) | "2020-06-01T08:30:45.000000+00:00" |

* * *

## `dst?`

Returns true if the input datetime is within Daylight Savings Time.

### Syntax

Datetime.dst?

- Datetime - An input date or datetime.

### Sample usage

| Formula | Result |
| --- | --- |
| today.to\_time.dst? | false |
| today.in\_time\_zone("America/New\_York").dst? | true |
| "2020-06-01".in\_time\_zone("America/New\_York").dst? | true |
| "2020-09-06T18:30:15.671720-05:00".to\_time.dst? | false |

### Regions reference

Refer to the following table for the timezone name to use in the formula.

| Region | Timezone to use in formula | UTC zone | DST offset? |
| --- | --- | --- | --- |
| International Date Line West | Pacific/Midway | UTC-11 |  |
| Midway Island | Pacific/Midway | UTC-11 |  |
| American Samoa | Pacific/Pago\_Pago | UTC-11 |  |
| Hawaii | Pacific/Honolulu | UTC-10 |  |
| Alaska | America/Juneau | UTC-9 | :white\_check\_mark: |
| Pacific Time (US & Canada) | America/Los\_Angeles | UTC-8 | :white\_check\_mark: |
| Tijuana | America/Tijuana | UTC-8 | :white\_check\_mark: |
| Mountain Time (US & Canada) | America/Denver | UTC-7 | :white\_check\_mark: |
| Arizona | America/Phoenix | UTC-7 |  |
| Chihuahua | America/Chihuahua | UTC-7 | :white\_check\_mark: |
| Mazatlan | America/Mazatlan | UTC-7 | :white\_check\_mark: |
| Central Time (US & Canada) | America/Chicago | UTC-6 | :white\_check\_mark: |
| Saskatchewan | America/Regina | UTC-6 |  |
| Guadalajara | America/Mexico\_City | UTC-6 | :white\_check\_mark: |
| Mexico City | America/Mexico\_City | UTC-6 | :white\_check\_mark: |
| Monterrey | America/Monterrey | UTC-6 | :white\_check\_mark: |
| Central America | America/Guatemala | UTC-6 |  |
| Eastern Time (US & Canada) | America/New\_York | UTC-5 | :white\_check\_mark: |
| Indiana (East) | America/Indiana/Indianapolis | UTC-5 | :white\_check\_mark: |
| Bogota | America/Bogota | UTC-5 |  |
| Lima | America/Lima | UTC-5 |  |
| Quito | America/Lima | UTC-5 |  |
| Atlantic Time (Canada) | America/Halifax | UTC-4 | :white\_check\_mark: |
| Caracas | America/Caracas | UTC-4 |  |
| La Paz | America/La\_Paz | UTC-4 |  |
| Santiago | America/Santiago | UTC-4 | :white\_check\_mark: |
| Georgetown | America/Guyana | UTC-4 |  |
| Newfoundland | America/St\_Johns | UTC-3:30 | :white\_check\_mark: |
| Brasilia | America/Sao\_Paulo | UTC-3 |  |
| Buenos Aires | America/Argentina/Buenos\_Aires | UTC-3 |  |
| Montevideo | America/Montevideo | UTC-3 |  |
| Greenland | America/Godthab | UTC-3 | :white\_check\_mark: |
| Mid-Atlantic | Atlantic/South\_Georgia | UTC-2 |  |
| Azores | Atlantic/Azores | UTC-1 | :white\_check\_mark: |
| Cape Verde Is. | Atlantic/Cape\_Verde | UTC-1 |  |
| Dublin | Europe/Dublin | UTC-1 | :white\_check\_mark: |
| Lisbon | Europe/Lisbon | UTC+0 | :white\_check\_mark: |
| Edinburgh | Europe/London | UTC+0 | :white\_check\_mark: |
| London | Europe/London | UTC+0 | :white\_check\_mark: |
| Monrovia | Africa/Monrovia | UTC+0 |  |
| UTC | Etc/UTC | UTC+0 |  |
| Casablanca | Africa/Casablanca | UTC+1 |  |
| Belgrade | Europe/Belgrade | UTC+1 | :white\_check\_mark: |
| Bratislava | Europe/Bratislava | UTC+1 | :white\_check\_mark: |
| Budapest | Europe/Budapest | UTC+1 | :white\_check\_mark: |
| Ljubljana | Europe/Ljubljana | UTC+1 | :white\_check\_mark: |
| Prague | Europe/Prague | UTC+1 | :white\_check\_mark: |
| Sarajevo | Europe/Sarajevo | UTC+1 | :white\_check\_mark: |
| Skopje | Europe/Skopje | UTC+1 | :white\_check\_mark: |
| Warsaw | Europe/Warsaw | UTC+1 | :white\_check\_mark: |
| Zagreb | Europe/Zagreb | UTC+1 | :white\_check\_mark: |
| Brussels | Europe/Brussels | UTC+1 | :white\_check\_mark: |
| Copenhagen | Europe/Copenhagen | UTC+1 | :white\_check\_mark: |
| Madrid | Europe/Madrid | UTC+1 | :white\_check\_mark: |
| Paris | Europe/Paris | UTC+1 | :white\_check\_mark: |
| Amsterdam | Europe/Amsterdam | UTC+1 | :white\_check\_mark: |
| Berlin | Europe/Berlin | UTC+1 | :white\_check\_mark: |
| Bern | Europe/Zurich | UTC+1 | :white\_check\_mark: |
| Zurich | Europe/Zurich | UTC+1 | :white\_check\_mark: |
| Rome | Europe/Rome | UTC+1 | :white\_check\_mark: |
| Stockholm | Europe/Stockholm | UTC+1 | :white\_check\_mark: |
| Vienna | Europe/Vienna | UTC+1 | :white\_check\_mark: |
| West Central Africa | Africa/Algiers | UTC+1 |  |
| Bucharest | Europe/Bucharest | UTC+2 | :white\_check\_mark: |
| Cairo | Africa/Cairo | UTC+2 |  |
| Helsinki | Europe/Helsinki | UTC+2 | :white\_check\_mark: |
| Kyiv | Europe/Kiev | UTC+2 | :white\_check\_mark: |
| Riga | Europe/Riga | UTC+2 | :white\_check\_mark: |
| Sofia | Europe/Sofia | UTC+2 | :white\_check\_mark: |
| Tallinn | Europe/Tallinn | UTC+2 | :white\_check\_mark: |
| Vilnius | Europe/Vilnius | UTC+2 | :white\_check\_mark: |
| Athens | Europe/Athens | UTC+2 | :white\_check\_mark: |
| Jerusalem | Asia/Jerusalem | UTC+2 | :white\_check\_mark: |
| Harare | Africa/Harare | UTC+2 |  |
| Pretoria | Africa/Johannesburg | UTC+2 |  |
| Kaliningrad | Europe/Kaliningrad | UTC+2 |  |
| Istanbul | Europe/Istanbul | UTC+3 |  |
| Minsk | Europe/Minsk | UTC+3 |  |
| Moscow | Europe/Moscow | UTC+3 |  |
| St. Petersburg | Europe/Moscow | UTC+3 |  |
| Kuwait | Asia/Kuwait | UTC+3 |  |
| Riyadh | Asia/Riyadh | UTC+3 |  |
| Nairobi | Africa/Nairobi | UTC+3 |  |
| Baghdad | Asia/Baghdad | UTC+3 |  |
| Tehran | Asia/Tehran | UTC+3:30 | :white\_check\_mark: |
| Volgograd | Europe/Volgograd | UTC+4 |  |
| Samara | Europe/Samara | UTC+4 |  |
| Abu Dhabi | Asia/Muscat | UTC+4 |  |
| Muscat | Asia/Muscat | UTC+4 |  |
| Baku | Asia/Baku | UTC+4 |  |
| Tbilisi | Asia/Tbilisi | UTC+4 |  |
| Yerevan | Asia/Yerevan | UTC+4 |  |
| Kabul | Asia/Kabul | UTC+4:30 | :white\_check\_mark: |
| Ekaterinburg | Asia/Yekaterinburg | UTC+5 |  |
| Islamabad | Asia/Karachi | UTC+5 |  |
| Karachi | Asia/Karachi | UTC+5 |  |
| Tashkent | Asia/Tashkent | UTC+5 |  |
| Sri Jayawardenepura | Asia/Colombo | UTC+5:30 | :white\_check\_mark: |
| Chennai | Asia/Kolkata | UTC+5:30 | :white\_check\_mark: |
| Kolkata | Asia/Kolkata | UTC+5:30 | :white\_check\_mark: |
| Mumbai | Asia/Kolkata | UTC+5:30 | :white\_check\_mark: |
| New Delhi | Asia/Kolkata | UTC+5:30 | :white\_check\_mark: |
| Kathmandu | Asia/Kathmandu | UTC+5:45 | :white\_check\_mark: |
| Astana | Asia/Dhaka | UTC+6 |  |
| Dhaka | Asia/Dhaka | UTC+6 |  |
| Almaty | Asia/Almaty | UTC+6 |  |
| Urumqi | Asia/Urumqi | UTC+6 |  |
| Rangoon | Asia/Rangoon | UTC+6:30 | :white\_check\_mark: |
| Novosibirsk | Asia/Novosibirsk | UTC+7 |  |
| Bangkok | Asia/Bangkok | UTC+7 |  |
| Hanoi | Asia/Bangkok | UTC+7 |  |
| Jakarta | Asia/Jakarta | UTC+7 |  |
| Krasnoyarsk | Asia/Krasnoyarsk | UTC+7 |  |
| Beijing | Asia/Shanghai | UTC+8 |  |
| Chongqing | Asia/Chongqing | UTC+8 |  |
| Hong Kong | Asia/Hong\_Kong | UTC+8 |  |
| Kuala Lumpur | Asia/Kuala\_Lumpur | UTC+8 |  |
| Singapore | Asia/Singapore | UTC+8 |  |
| Taipei | Asia/Taipei | UTC+8 |  |
| Perth | Australia/Perth | UTC+8 |  |
| Irkutsk | Asia/Irkutsk | UTC+8 |  |
| Ulaanbaatar | Asia/Ulaanbaatar | UTC+8 |  |
| Seoul | Asia/Seoul | UTC+9 |  |
| Osaka | Asia/Tokyo | UTC+9 |  |
| Sapporo | Asia/Tokyo | UTC+9 |  |
| Tokyo | Asia/Tokyo | UTC+9 |  |
| Yakutsk | Asia/Yakutsk | UTC+9 |  |
| Darwin | Australia/Darwin | UTC+9:30 |  |
| Adelaide | Australia/Adelaide | UTC+9:30 | :white\_check\_mark: |
| Canberra | Australia/Melbourne | UTC+10 | :white\_check\_mark: |
| Melbourne | Australia/Melbourne | UTC+10 | :white\_check\_mark: |
| Sydney | Australia/Sydney | UTC+10 | :white\_check\_mark: |
| Brisbane | Australia/Brisbane | UTC+10 |  |
| Hobart | Australia/Hobart | UTC+10 | :white\_check\_mark: |
| Vladivostok | Asia/Vladivostok | UTC+10 |  |
| Guam | Pacific/Guam | UTC+10 |  |
| Port Moresby | Pacific/Port\_Moresby | UTC+10 |  |
| Magadan | Asia/Magadan | UTC+11 |  |
| Srednekolymsk | Asia/Srednekolymsk | UTC+11 |  |
| Solomon Is. | Pacific/Guadalcanal | UTC+11 |  |
| New Caledonia | Pacific/Noumea | UTC+11 |  |
| Fiji | Pacific/Fiji | UTC+12 | :white\_check\_mark: |
| Kamchatka | Asia/Kamchatka | UTC+12 |  |
| Marshall Is. | Pacific/Majuro | UTC+12 |  |
| Auckland | Pacific/Auckland | UTC+12 | :white\_check\_mark: |
| Wellington | Pacific/Auckland | UTC+12 | :white\_check\_mark: |
| Nuku'alofa | Pacific/Tongatapu | UTC+13 |  |
| Tokelau Is. | Pacific/Fakaofo | UTC+13 |  |
| Samoa | Pacific/Apia | UTC+13 |  |
| Chatham Is. | Pacific/Chatham | UTC+13:45 | :white\_check\_mark: |

* * *

## `to_date`

This formula converts input data into a date and returns the date formatted as `YYYY-MM-DD`.

### Syntax

String.to\_date(format: format)

- String - A string input that describes a date or datetime.
- format - (optional) The format of the input date string. If not specified, Workato parses the input string automatically.

> **FORMAT PARAMETER DOESN'T AFFECT OUTPUT FORMAT**
> 
> The `format` parameter defines only the input format. It does not affect the output format, which is returned as `YYYY-MM-DD`.

### Sample usage

| Formula | Result |
| --- | --- |
| "23-01-2020 10:30 pm".to\_date(format: "DD-MM-YYYY") | "2020-01-23" |
| "01-23-2020 10:30 pm".to\_date(format: "MM-DD-YYYY") | "2020-01-23" |
| "2020/01/23".to\_date(format: "YYYY/MM/DD") | "2020-01-23" |
| "06/27/25".to\_date(format: "%m/%d/%y") | "2025-06-27" |

### How it works

Converts the input data into a date datatype.

> **INPUT DATA BEST PRACTICE**
> 
> We recommend that you specify the input data format. If you don't specify the input data format, Workato parses the input string automatically.
> 
> The input string must resemble a date for this formula to work.

### See also

- [strftime](/en/formulas/date-formulas#strftime): Returns datetime is a custom format.
- [to\_time](/en/formulas/date-formulas#to-time): Converts a string to an ISO timestamp.

* * *

## `to_time`

Converts a string to an ISO timestamp. The response will use the UTC timezone (+00:00).

### Syntax

String.to\_time(format: format)

- String - An input string that describes a date or datetime.
- format - (optional) The format of the user-defined datetime written as a string.

### Sample usage

| Formula | Result |
| --- | --- |
| "2020-04-02T12:30:30.462659-07:00".to\_time(format: "%Y-%m-%dT%H:%M:%S") | "2020-04-02T19:30:30.000+00:00" |
| "2020-04-02".to\_time | "2020-04-02T00:00:00.000+00:00" |

### How it works

Converts the input string into a datetime datatype. The output datetime will be converted to the UTC timezone (+00:00).

> **Autofill time**
> 
> If the input data does not include the time, the output will default to `00:00:00.000000 +00:00`.

### See also

- [strftime](/en/formulas/date-formulas#strftime): Returns datetime is a custom format.
- [to\_date](/en/formulas/date-formulas#to-date): This formula converts the date-like input into a date. Returns the date formatted as YYYY-MM-DD.

### Parameters

As previously shown, each code (`%B`, `%e`, `%I`, for example) refers to a specific element of `datetime`. You can also add static text and punctuation, such as commas (`,`), slashes (`/`), and colons (`:`). Refer to the following list of frequently used codes:

| Code | Meaning | Example (2020-06-05T17:13:27.000000-07:00) |
| --- | --- | --- |
| %Y | Year with century | 2020 |
| %m | Month with zero-prefix | 06 |
| %B | Full month name | June |
| %b | Abbreviated month name | Jun |
| %d | Day of the month with zero-prefix | 05 |
| %e | Day of the month without zero-prefix | 5 |
| %H | Hour of the day (24-hour) | 17 |
| %k | Hour of day without 0 prefix (24-hour) | 17 |
| %I (capital i) | Hour of the day (12-hour) | 05 |
| %l (lowercase L) | Hour of day without 0 prefix (12-hour) | 5 |
| %p | AM or PM | PM |
| %M | Minute of the hour | 13 |
| %S | Second of the minute | 27 |
| %L | Millisecond of the second | 000 |
| %z | Time zone offset from UTC | \-0700 |
| %:z | Time zone formatted offset from UTC | \-07:00 |
| %Z | Time zone abbrev. name | UTC |
| %A | Full day name | Friday |

To access the full list, check out the [Ruby documentation](http://ruby-doc.org/core-2.3.3/Time.html#method-i-strftime)

* * *

## `to_i`

Convert datetime into epoch time. Returns an epoch time in UTC (+00:00).

### Syntax

Datetime.to\_i

- Datetime - An input datetime.

### Sample usage

| Formula | Result |
| --- | --- |
| today.to\_time.to\_i | 1645660800 |
| now.to\_i | 1645714000 |

### How it works

Converts the input datetime into an integer, it will return epoch time in seconds, not milliseconds. The output datetime will be converted to the UTC timezone (+00:00).

> **Converting between Epoch time to datetime**
> 
> Convert time formats easily with Workato formulas.
> 
> #### How to convert human readable time to epoch time
> 
> Use `to_i` to convert a datetime datapill to epoch time (in UTC). Learn more about [how it works](/en/formulas/date-formulas#to-i).
> 
> #### How to convert epoch time to human-readable time
> 
> Use the following formula to convert an epoch time to human-readable datetime.
> 
> Note that the output will be in UTC timezone (+00:00).
> 
> `"1970-01-01".to_time +` Epoch time`.seconds`
> 
> If you plan to convert epoch time to a specific timezone, you must specify it with [in\_time\_zone](/en/formulas/date-formulas#in-time-zone).
> 
> `"1970-01-01".to_time.in_time_zone("US/Pacific") +` Epoch time`.seconds`

> **Wrong datatype: undefined method to\_i**
> 
> Epoch time requires a datetime datapill. If you are using a date datapill, it will cause an error.
> 
> Use [to\_time](/en/formulas/date-formulas#to-time) to convert a date into a datetime before converting to epoch time.

### See also

- [to\_time](/en/formulas/date-formulas#to-time): Converts a string to an ISO timestamp.
- [to\_date](/en/formulas/date-formulas#to-date): This formula converts the date-like input into a date. Returns the date formatted as YYYY-MM-DD.
- [in\_time\_zone](/en/formulas/date-formulas#in-time-zone): Converts a time value to a different time zone.

---
