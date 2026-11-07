---
url: 'https://docs.workato.com/en/connectors/facebook-ads/campaign-insights.md'
description: >-
  The Get campaign insights action in the Facebook Lead Ads connector retrieves
  aggregate metrics across all ads and ad sets by campaign ID.
---

# Facebook Lead Ads - Get campaign insights action

The **Get campaign insights** action allows you to retrieve aggregate information across all ads and ad sets in Facebook by campaign ID.

![Get Adset insights action](/assets/get-campaign-action.CqETOZh2.png)_Facebook Lead Ads - Get campaign insights action_

## Input

| Field | Description |
| --- | --- |
| Campaign ID | Enter the unique identifier of the Facebook campaign you plan to analyze. |
| Time range | Define the time range to retrieve campaign performance data. The time range fields do not support UNIX timestamps. |
| Since | Specify the start date for the data collection period. |
| Until | Specify the end date to conclude data collection. |

## Output

| Field | Description |
| --- | --- |
| Account ID | The unique identifier for the advertising account. |
| Campaign ID | The identifier for the campaign. |
| Date start | The start date of the data retrieval period. |
| Date stop | The end date of the data retrieval period. |
| Impressions | The total number of times ads were displayed. |
| Spend | The total amount spent on the campaign. |
| Campaign name | The name of the campaign. |
| Campaign objective | The objective set for the campaign. |
| Created time | The time when the campaign was created. |
| Adset ID | The unique identifier for the ad set. |
| Adset name | The name of the ad set. |
| List size | The total number of items in the list. |
| List index | The index of the item within the list. |

---
