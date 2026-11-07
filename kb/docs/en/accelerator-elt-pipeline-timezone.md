---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-timezone.md'
description: >-
  Learn how the ELT Pipeline accelerator uses the Workato account timezone and
  why you must reference it when scheduling pipeline start times.
---

# Pipeline timezone

The recipes in this accelerator run on the provisioned Workato workspace. Because of this, they use the Workato account's timezone as the point of reference. When you create pipelines, you must reference the Workato account's timezone, as using a different timezone may cause unintended behaviors. For example, consider a situation with the following conditions:

- User's date-time: 2022-02-04 T 07:40:00-01:00
- User timezone: UTC-1
- Workato account timezone: UTC-8
- Pipeline start time, as selected with the bot based on user timezone: 2022-02-04 10:00
- Actual pipeline start time: 2022-02-04T10:00:00-08:00 or 2022-02-04T17:00:00-01:00

In this scenario, the pipeline starts seven hours later than the user intended. Thus, you must consider the Workato account where the accelerator is installed when you select a start time.

---
