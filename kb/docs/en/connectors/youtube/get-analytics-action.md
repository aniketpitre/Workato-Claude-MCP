---
url: 'https://docs.workato.com/en/connectors/youtube/get-analytics-action.md'
description: >-
  The Get analytics action retrieves analytics data for a date range you specify
  in YouTube.
---

# YouTube - Get analytics action

The **Get analytics** action retrieves analytics data for a date range you specify in YouTube.

> **PREREQUISITES**
> 
> This action requires OAuth 2.0 authentication and returns data only for the channel associated with the connected account. It also calls the **YouTube Analytics API**, a separate API from YouTube Data API v3 that the rest of this connector uses. Enable **YouTube Analytics API** for your project in the [Google Cloud Console](https://console.cloud.google.com/apis/library/youtubeanalytics.googleapis.com) in addition to YouTube Data API v3. Your OAuth connection also needs a scope that grants YouTube Analytics access: **YouTube Analytics reports** for standard metrics, or **YouTube Analytics monetary reports** for revenue and ad performance metrics, such as `estimatedRevenue`. The general **Read-only access** scope doesn't grant access to the YouTube Analytics API.

## Input

| Field | Description |
| --- | --- |
| Start date | Select or enter the start date for the analytics data. |
| End date | Select or enter the end date for the analytics data. |
| Metrics | Select the metrics to retrieve, such as `views`, `estimatedMinutesWatched`, `likes`, `comments`, `subscribersGained`, and `estimatedRevenue`. Leave blank for default metrics. |
| Dimensions | Select the dimensions for grouping data, such as `day`, `month`, `country`, `ageGroup`, `gender`, `deviceType`, `video`, and `playlist`. |
| Filters | Enter the filters parameter, for example `video==videoID;country==IN`. |
| Sort | Enter the sort parameter, for example `-views` for descending views or `day` for ascending by day. |
| Max results | Enter the maximum number of results to return. Valid values are 1-50. Default is 25. |

## Output

| Field | Description |
| --- | --- |
| Kind | The API resource type, for example `youtubeAnalytics#resultTable`. |
| Column headers | An array describing each column in `Rows`. Each entry contains a `Name`, `Column type`, and `Data type`. |
| Rows | An array of result rows. Each row contains one value per column, in the order defined by `Column headers`. |

---
