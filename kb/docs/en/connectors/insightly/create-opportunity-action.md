---
url: 'https://docs.workato.com/en/connectors/insightly/create-opportunity-action.md'
description: >-
  The Create opportunity action in the Insightly connector lets you create a new
  opportunity with state, value, pipeline, and stage details.
---

# Insightly - Create opportunity action

This action creates a new opportunity in your Insightly instance.

## Input

| Field | Description |
| --- | --- |
| Opportunity name | The name of the opportunity. |
| Opportunity state | The state of the opportunity. |
| Opportunity details | The details of the opportunity. |
| Probability | The percentage probability of winning the opportunity. |
| Forecast close date | The forecast close date of the opportunity. |
| Category ID | The category ID of the opportunity. |
| Responsible user ID | The responsible user ID of the opportunity. |
| Owner user ID | The owner user ID of the opportunity. |
| Bid currency | The bid currency of the opportunity. |
| Value | The value of the opportunity. |
| Bid type | The bid type of the opportunity. |
| Visible to | The visibility of the opportunity. |
| Visible user IDs | The visible user IDs of the opportunity. |
| Pipeline ID | The pipeline ID of the opportunity. |
| Stage name | The stage name of the opportunity. |

## Output

The output of this action is a datatree that contains information about the [opportunity](https://api.insightly.com/v3.1/Help#!/Opportunities/GetEntities) created.

---
