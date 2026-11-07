---
url: >-
  https://docs.workato.com/en/connectors/azure-ad/search-transitive-group-member-action.md
description: Get a list of the group's transitive members using search filters.
---

# Microsoft Entra ID - Search transitive group members action

The **Search transitive group members** action retrieves a list of the group's transitive members using search filters. A group can include users, devices, service principals, and other groups as members.

Refer to the [Group membership](https://learn.microsoft.com/en-us/graph/api/resources/groups-overview?view=graph-rest-1.0#group-membership) section for supported member types. If the number of records exceeds the limit, this action paginates through the remaining records.

## Input

| Input field | Description |
| --- | --- |
| Group | Choose a group from the drop-down. Alternatively, enter a custom value if the group is not listed. |
| Fields | Choose the fields to include in the output. |
| Additional fields | Define additional fields using the schema designer. |
| Search | Filter results using search keywords. For example,`mail:user@microsoft.com`. [Learn more](https://learn.microsoft.com/en-us/graph/search-query-parameter?tabs=http). |
| Filter | Apply query parameters to filter results. For example, `startsWith(givenName, ‘J’)`. [Learn more](https://learn.microsoft.com/en-us/graph/filter-query-parameter?tabs=http). |
| Next page cursor | Retrieve this value from the output if additional records exist. |
| Page size | Set the maximum number of records to return. Defaults to 100 if blank. Note that the action may fail due to rate limits. Refer to [Microsoft Graph service-specific throttling quota](https://learn.microsoft.com/en-us/graph/throttling-limits) for more information. |

## Output

Refer to the [User schema](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0#properties) for field definitions.
