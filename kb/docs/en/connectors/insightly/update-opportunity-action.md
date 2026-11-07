---
url: 'https://docs.workato.com/en/connectors/insightly/update-opportunity-action.md'
description: >-
  The Update opportunity action in the Insightly connector lets you update an
  existing opportunity by ID, including its state, value, and stage.
---

# Insightly - Update opportunity action

This action updates an opportunity in your Insightly instance.

## Input

| Input field | Description |
| --- | --- |
| Opportunity ID | The ID of the opportunity to be updated. |
| Opportunity name | The name of the opportunity. |
| Opportunity state | The state of the opportunity. |
| Opportunity details | The details of the opportunity. |
| Probability | The percentage probability of winning the opportunity. |
| Forecast close date | The forecast close date of the opportunity. |
| Category | The category of the opportunity. |
| Responsible user ID | The responsible user ID of the opportunity. |
| Owner user ID | The owner user ID of the opportunity. |
| Bid currency | The bid currency of the opportunity. |
| Value | The value of the opportunity. |
| Bid type | The bid type of the opportunity. |
| Visible to | The visibility of the opportunity. |
| Visible user IDs | The visible user IDs of the opportunity. |
| Pipeline ID | The pipeline ID of the opportunity. |
| Stage name | The stage name associated with the selected pipeline. |

## Output

The output of this action is a datatree that contains information about the updated [opportunity](https://api.insightly.com/v3.1/Help#!/Opportunities/GetEntities).

---
