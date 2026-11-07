---
url: 'https://docs.workato.com/en/connectors/sms-by-workato.md'
description: >-
  SMS by Workato is a utility connector that sends low-volume SMS messages for
  recipe alerts, debugging, and testing before moving to a production provider.
---

# SMS by Workato

SMS by Workato is designed to allow users to easily send SMS for low volume use cases around critical recipe alerts, debugging, or testing. You can use this connector to quickly build proof of concepts before migrating to a production-ready SMS service provider.

> **DEPRECATION NOTICE**
> 
> Workato will deprecate the SMS by Workato connector on **February 1, 2025**.
> 
> After this date, SMS by Workato will no longer be available for selection when building or editing recipes. However, all existing recipes that use SMS by Workato will continue to work for the foreseeable future as long as you don't remove or edit any existing SMS by Workato actions.
> 
> The end-of-support date for this feature will be announced in the future.

> **FEATURE AVAILABILITY**
> 
> SMS by Workato is only available in US and SG data centers. All messages sent are appended with `- via workato.com` and the recipient sees the sender as "Workato". Therefore, for production use cases, Workato recommends using other SMS providers such as Twilio or Vonage.

## Send SMS action

### Input

| Output | Description |
| --- | --- |
| Phone | Enter a US or SG phone number prepended with '+' and the country code. For example: +16505551212. |
| Message | The message you plan to send, limited to 142 GSM-7 characters (or 52 UCS-2 characters). You can use this [segment calculator](https://twiliodeved.github.io/message-segment-calculator/) to check your message length. |

### Output

| Output | Description |
| --- | --- |
| Remaining calls | The number of remaining calls Workato can execute out of the overall daily quota (25 calls). |
| Consumed calls | The number of actions completed out of the overall daily quota (25 calls). |
| Reset time | The time the daily quota resets. |

## Quotas

SMS by Workato is subject to the following rate limits:

- 25 SMS for each workspace in a 24-hour period

If you exceed this rate limit, Workato throws an error and fails the job. If you need to send SMS at scale we recommend using your own SMS provider like Twilio or Vonage. To help you keep track of your usage, Workato supplies output datapills corresponding to your current consumed calls and reset time for the quotas.

---
