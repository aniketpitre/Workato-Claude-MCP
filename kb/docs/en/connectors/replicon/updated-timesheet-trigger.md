---
url: 'https://docs.workato.com/en/connectors/replicon/updated-timesheet-trigger.md'
description: >-
  The deprecated Updated timesheet trigger in the Replicon connector picks up
  timesheets updated in your Replicon instance, processing each as a job.
---

# Replicon - Updated timesheet trigger

This trigger picks up timesheets that are updated in your Replicon instance. Each updated timesheet is processed as an individual job.

> **THIS TRIGGER IS DEPRECATED**
> 
> Due to changes in the Replicon API endpoint, we are no longer able to support this trigger. Therefore, as of **February 8, 2023**, this trigger is deprecated.

![Updated timesheet trigger](/assets/updated-timesheet-trigger.B2X2jiKZ.png)_Updated timesheet trigger_

## Input

<dl id="replicon-updated-timesheet-input"><dt>Status</dt><dd>Specifies the status of the timesheet to be picked.</dd><dt>Trigger poll interval</dt><dd>Specifies how frequently Workato polls for new client(s). This is an optional parameter.</dd></dl>

## Output

The output of this trigger will be a datatree that contains information about the updated Replicon timesheet.

---
