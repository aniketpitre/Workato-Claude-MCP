---
url: 'https://docs.workato.com/en/data-types/duration-data-type.md'
description: The duration data type converts duration to a number (in seconds).
---

# Duration data type

The `Duration` data type converts duration to a number. `Duration` values are serialized as integers in seconds.

Example `Duration` values:

- `3.seconds`
- `5.minutes`
- `7.days`
- `12.months`
- `2.years`

## Syntax

now.to\_i + 1.minute

## Sample usage

| Formula | Result |
| --- | --- |
| now.to\_i + 1.6 | current time + 96 seconds |
| now.to\_i + 24.hours | current time + 86400 |

---
