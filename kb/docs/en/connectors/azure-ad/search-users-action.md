---
url: 'https://docs.workato.com/en/connectors/azure-ad/search-users-action.md'
description: >-
  Retrieve a list of users using search filters. If more records exceed the
  specified limit, this action will paginate through the remaining records.
---

# Microsoft Entra ID - Search users action

The **Search users** action retrieves a list of users using search filters. If the number of records exceeds the limit, this action paginates through the remaining records.

## Input

| Input field | Description |
| --- | --- |
| Fields | Choose the fields to include in the output. |
| Expand | Retrieves related resources. |
| Additional fields | Define additional fields using the schema designer. |
| Search | Filter results using search keywords. For example,`mail:user@microsoft.com`. [Learn more](https://learn.microsoft.com/en-us/graph/search-query-parameter?tabs=http). |
| Filter | Apply query parameters to filter results. For example, `startsWith(givenName, ‘J’)`. [Learn more](https://learn.microsoft.com/en-us/graph/filter-query-parameter?tabs=http). |
| Next page cursor | Retrieve this value from the output if additional records exist. |
| Page size | Set the maximum number of records to return. Defaults to 100 if blank. Note that the action may fail due to rate limits. Refer to the [Microsoft Graph service-specific throttling quota](https://learn.microsoft.com/en-us/graph/throttling-limits) section for more information. |

## Output

Refer to the [User schema](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0#properties) for field definitions.

---
