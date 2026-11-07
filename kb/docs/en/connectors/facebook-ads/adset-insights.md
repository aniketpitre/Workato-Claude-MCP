---
url: 'https://docs.workato.com/en/connectors/facebook-ads/adset-insights.md'
description: >-
  The Get Adset insights action in the Facebook Lead Ads connector retrieves
  advertising performance metrics for a given ad set by adset ID.
---

# Facebook Lead Ads - Get Adset insights action

The **Get Adset insights** action retrieves advertising performance metrics in Facebook by adset ID. This action allows you to deduplicate metrics across child objects, sort metrics, and conduct asynchronous reporting to enhance your advertising strategy.

![Get Adset insights action](/assets/get-adset-action.B4T8wpw-.png)_Facebook Lead Ads - Get Adset insights action_

### Input

| Field | Description |
| --- | --- |
| Adset ID | Enter the unique identifier for the ad set you plan to analyze. An ad set groups ads with shared budgets, schedules, bid strategies, and targeting data. |
| Time range | Define the time range to retrieve ad performance data. The time range fields do not support UNIX timestamps. |
| Since | Specify the start date to begin data collection. |
| Until | Specify the end date to conclude data collection. |

### Output

| Field | Description |
| --- | --- |
| Account ID | The unique identifier for the advertising account. |
| Campaign ID | The identifier for the associated campaign. |
| Date start | The start date of the data retrieval range. |
| Date stop | The end date of the data retrieval range. |
| Impressions | The total number of times ads were shown. |
| Spend | The total amount of money spent on the ads. |
| Campaign name | The name of the campaign. |
| Adset objective | The objective set for the ad set. |
| Created time | The time when the ad set was created. |
| Adset ID | The unique identifier for the ad set. |
| Adset name | The name of the ad set. |
| List size | The total number of items in the list. |
| List index | The index of the item within the list. |

---
