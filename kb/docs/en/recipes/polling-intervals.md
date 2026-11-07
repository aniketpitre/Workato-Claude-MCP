---
url: 'https://docs.workato.com/en/recipes/polling-intervals.md'
description: >-
  Learn how Workato poll-based triggers check apps for new and updated records,
  default polling intervals by plan, and how to change them.
---

# Polling intervals

Most Workato triggers are poll-based triggers. This means that it checks the trigger application for the trigger events it is monitoring, at regular intervals, for example, every 5 minutes.

## Polling intervals explained

For recipes on a polling interval, Workato uses two date/time fields (i.e. **Created Date** and **Last Modified** ) in the object records to determine if the record was newly created or updated.

When checking for **newly created** records, recipes are triggered if two conditions are met:

- The record was created since the time you specified. Is the "created date" since the "since" parameter?
- The record was not already processed by Workato. Has this triggered the recipe already?

Similarly, when checking for **updated** records, recipes are triggered if two conditions are met on any record:

- The record was updated since the time you specified. Is the "last modified date" after both the "since" and "created date" parameters?
- The record was not already processed by Workato. Has this triggered the recipe already?

> **INFO**
> 
> Select **Test recipe** or **Start recipe** then **Stop recipe** to poll the app for new trigger events immediately.
> 
> Alternatively, you can use [Webhooks](/en/connectors/workato-webhooks) to pick up trigger events as soon as they occur.

## How long are polling intervals?

Polling intervals are determined by the tier of Workato plan you are subscribed to.

- **Community** and **Base** plan subscribers have a default of 10 minute polling interval
- **Professional and above** plans have a default of 5 minute polling interval

## How can I change the polling interval?

For poll-based triggers, the **Trigger Poll Interval** field is available as an optional configuration in the trigger setup. This field allows a user to either choose from a set of options, for example, every 6 hours / 1 day / 30 days, or define your own poll interval in number of minutes.

The minimum polling interval allowed is determined by the tier of Workato plan you are subscribed to. This value is also shown to you in the **Trigger Poll Interval** field's hint.

![configure polling interval](/assets/configure-polling-interval.CHLDsZa6.gif)

## I want my jobs to trigger the recipe instantly

For jobs to be picked up immediately, Webhooks have to be used instead. Some applications on Workato support Webhooks and you will see a `REAL TIME` indication in the trigger.

![real time](/assets/real-time.CmleXd6L.jpg)

Webhooks have to be configured and set-up before use. It is also possible to build a webhooks connection with the HTTP application.

---
