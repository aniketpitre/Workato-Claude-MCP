---
url: 'https://docs.workato.com/en/connectors/active_directory/search_entries.md'
description: >-
  The Search entries batch action in the Active Directory connector retrieves
  entries matching your criteria and processes them in batches.
---

# Active Directory - Search entries action (Batch)

The **Search entries** batch action retrieves a list of Active Directory entries matching the criteria you specify and processes them in batches.

## Input

| Input field | Description |
| --- | --- |
| Sample entry DN | Specify the distinguished name (DN) of a reference entry. The action uses this entry’s attributes as a template to define sub-fields in the **Search entries by** field and retrieve values from matching entries. |
| Limit | Enter the maximum number of entries you plan to retrieve for each action. The maximum is 1,000 entries. |
| Batch size | Optional. Enter the maximum number of entries to return in each batch. Defaults to `1000`. |
| Batch cookie | Optional. Enter the `Batch cookie` from a previous iteration of this action to retrieve the next batch of results. Leave this field blank to retrieve the first batch. |
| Search entries by | Enter values for each attribute you plan to filter by. Only entries that match all the provided values are processed. This field includes sub-fields for each attribute of the reference entry. |
| Advanced search filter | Enter [LDAP filters](https://ldap.com/ldap-filters/) to define search conditions. For example, enter `(ou=Dev)(objectClass=Person)` to retrieve only `Person` entries from the `Dev` organization unit. |

## Output

| Output field | Description |
| --- | --- |
| Batch cookie | A pagination token for the next batch of results. |
| Entries | Returns the entries that match your search criteria, including values for each attribute defined by the sample entry. |

---
