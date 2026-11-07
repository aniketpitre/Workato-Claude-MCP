---
url: >-
  https://docs.workato.com/en/connectors/linkedin/search-advertising-form-responses.md
description: >-
  The Search lead gen form responses action in the LinkedIn connector lets you
  search responses, filtered by campaign, form, and creative.
---

# LinkedIn - Search lead gen form responses action

Use this action to search for all lead gen form responses.

![Search lead gen form response](/assets/search-advertising-response.CIIXcOfU.png)_Search lead gen form responses by campaign, form, and creative_

## Input

| Input field | Description |
| --- | --- |
| Advertising account | The advertising account where the form is coming from. You can't map a datapill to this field. |
| Form | The form to which this lead gen response belongs. This is required for Workato to identify the custom questions within this lead gen form. |
| Pull reports within a specified time range | Specify the date range for the reports you plan to retrieve. The start date must be a maximum of 90 days in the past. |
| Offset | Used for pagination. |
| Limit | Limit the number of leads this action can pull. |
| Campaign | Limit responses to a specific campaign. |
| Creative | Limit responses to a specific creative. |

## Output

The output of this action contains all information relevant to leads based on your search filters.
