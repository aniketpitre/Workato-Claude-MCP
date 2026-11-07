---
url: 'https://docs.workato.com/en/features/data-masking.md'
description: >-
  Learn how data masking in Workato hides sensitive trigger and step data so
  collaborators cannot view it in job history or audit logs.
---

# Data masking

Workato stores [job history details](/en/security/data-protection/data-retention/#job-history-details) data for every recipe step according to your [data retention policy](/en/security/data-protection/data-retention/#what-is-it). However, in some cases, you may prefer to restrict other workspace collaborators with privileges to access job history data from viewing sensitive information, such as employee SSNs or birth dates.

**Data masking** enables you to hide sensitive data at the trigger and step levels, ensuring better control over job history visibility.

> **FEATURE AVAILABILITY**
> 
> Data masking is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

## How does data masking affect data storage?

- [Trigger and action steps](#trigger-and-action-steps)
- [Activity audit log](#activity-audit-log)

### Trigger and action steps

When you enable data masking for a trigger or action step, Workato doesn't store or display input and output data for that step.

However, trigger event data, which is used to repeat jobs, is still stored. This data is separate from job history data.

### Activity audit log

Workato excludes masked input and output data from the [activity audit log](/en/features/activity-audit-log) and doesn't stream it to your [audit log streaming destination](/en/features/activity-audit-log-streaming-destinations) when data masking is enabled.

Instead, Workato replaces the step data with a `"masked"` placeholder in the activity audit log:

```json
"lines": [
    {
        "input": {"data": "masked"},
        "output": {"data": "masked"},
        "adapter_name": "timer",
        "adapter_operation": "trigger_event",
        "line_stat": {
            "details": [
                {
                    "name": "execution_time",
                    "average": 0.002,
                    "total": 0.002,
                    "min": 0.002,
                    "max": 0.002,
                    "count": 1
                }
            ],
            "total": 0.002
        },
        "recipe_line_number": 1,
        "mask_data": true
    }
]
```

## Enable data masking

You can mask data for individual recipe steps. Workato hides both input and output data from the job history.

Complete the following steps to enable data masking:

1. Open a recipe in the recipe editor.
   
2. Hover over the trigger or recipe step and click the **•••** (ellipsis).
   
3. Click the **Mask data** toggle to enable data masking for that specific step.
   
   ![Enable data masking](/assets/enabling-data-masking.CouC11vm.png)_Enable data masking_
   

## Example

In the following [example recipe](https://www.workato.com/recipes/480360), data masking is enabled for the Salesforce **New/updated account** trigger:

![Recipe with data masking enabled](/assets/recipe.vqA288tv.png)_Recipe with data masking enabled_

Before enabling data masking, the trigger's input and output data appears on the job details page:

![Job details before masking](/assets/job-details-before-masking.DH4K5apu.gif)_Job details before masking_

However, after enabling data masking, the trigger's input and output data is hidden:

![Job details after masking](/assets/job-details-after-masking.DTFRyEX3.gif)_Job details after masking_

---
