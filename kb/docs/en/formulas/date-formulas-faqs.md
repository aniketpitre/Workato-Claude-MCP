---
url: 'https://docs.workato.com/en/formulas/date-formulas-faqs.md'
description: >-
  Find answers to common questions about date and datetime formulas in Workato,
  including arithmetic, from_now, and wday.
---

# Date formulas FAQs

Get answers to frequently asked questions (FAQs) about date formulas.

## What are date and datetime formulas used for?

View answer

[Date and datetime formulas](/en/formulas/date-formulas#date-formulas) allow you to work with date and time datapills. These formulas are used to manipulate and perform calculations on date and time data in Workato.

## Are all Ruby methods supported by date formulas?

View answer

No, not all Ruby methods are supported. Contact your Customer Success Manager to request new formulas for the allowlist. Refer to the [Date formulas](/en/formulas/date-formulas) documentation for more information.

## How can I perform arithmetic with date and datetime data?

View answer

You can use [arithmetic](/en/formulas/date-formulas#date-arithmetic) keywords like `seconds`, `minutes`, `days`, `months`, and `years` in combination with date and datetime formulas to perform addition and subtraction operations.

## What units can I use with the from\_now formula, and how does it work?

View answer

The [**from\_now** formula](/en/formulas/date-formulas#from-now) returns a future timestamp by a specified time duration. It calculates the timestamp at runtime.

You can use units like seconds, minutes, hours, days, months, or years with the **from\_now** formula to calculate future timestamps. It calculates the current timestamp and offsets it by the specified time duration.

## What does the wday formula return?

View answer

The [**wday** formula](/en/formulas/date-formulas#wday) returns the day of the week, with Sunday represented as `0` , Monday as `1`, and so on for each day of the week.

## How can I convert a string into a date datatype?

View answer

You can use the [**to\_date** formula](/en/formulas/date-formulas#to-date) to convert a string into a date datatype. This formula allows you to specify the date format if necessary.

## What does the strftime formula do, and how can I use it?

View answer

The [**strftime** formula](/en/formulas/date-formulas#strftime) allows you to format a datetime input as a user-defined string. You can customize the output format using various codes, as specified in the parameters.

## How can I convert a string into an ISO timestamp?

View answer

You can use the [**to\_time** formula](/en/formulas/date-formulas#to-time) to convert a string into an ISO timestamp, and it will use the UTC timezone.

## How can I convert a date or datetime to a different timezone?

View answer

The [**in\_time\_zone** formula](/en/formulas/date-formulas#in-time-zone) can be used to convert a date or datetime to a different timezone using timezone names from the IANA time zone database.

You can use the list of timezone names to determine which timezone to use.

## How do I determine if a datetime is within Daylight Savings Time (DST)?

View answer

You can use the [**dst?** formula](/en/formulas/date-formulas#dst) to check if a datetime is within Daylight Savings Time.

---
