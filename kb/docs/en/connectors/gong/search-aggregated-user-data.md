---
url: 'https://docs.workato.com/en/connectors/gong/search-aggregated-user-data.md'
description: >-
  The Search aggregated user data action in the Gong connector lists activity
  statistics for multiple users across time periods in a date range.
---

# Gong - Search aggregated user data action

This action will search aggregated user data in Gong. Lists the aggregated activity of multiple users within the Gong system for each time period within the defined date range. This endpoint returns multiple records, one for each user. For each user there are items for every time period in the date range, including statistics about the user's activity. Records are returned only for users with activity in the range.

## Input

| Field | Description |
| --- | --- |
| Aggregation period **Required** | Choose from \['Day', 'Week', 'Month', 'Quarter', 'Year', 'No aggregation'\]. Calendar time period for aggregating data. First day of the week is Monday. Select No aggregation to return user data aggregated by the date range you provide. |

Upon selection of an aggregation period you will have to provide the start date (which is inclusive) and end date (which is exclusive and not exceed the current day). You can also choose to provide a list of User IDs to obtain information just about them. If this is left blank then all users are returned.

## Output

| Field | Description |
| --- | --- |
| Users aggregate activity _A list of following details for each user_ | User Aggregate Activity | The aggregate details of a single user is contained within this list object. |
| User Email Address | Email address of the user whose information is at the corresponding index. |
| User ID | Gong User ID for the specific user. |
| List Size | The list size of the users aggregate activity. |
| List Index | An index for each item in the list of users aggregate activity. |
| Records _Metadata of the response_ | Current page number | Necessary for repeat requests to ensure pagination. |
| Current page size | Number of records on the current page. |
| Cursor | UUID necessary for pagination. |
| Total Records | Total number of records that can be queried. |

---
