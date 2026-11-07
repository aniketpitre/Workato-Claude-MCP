---
url: 'https://docs.workato.com/en/connectors/active_directory/scheduled_trigger.md'
description: >-
  The Scheduled entry search batch trigger in the Active Directory connector
  searches entries on a schedule and processes matches in batches.
---

# Active Directory - Scheduled entry search trigger (Batch)

The **Scheduled entry search** batch trigger searches Active Directory entries on a schedule you specify. The trigger retrieves a list of entries matching the criteria you specify and processes them batches.

## Input

| Input field | Description |
| --- | --- |
| Sample entry DN | Specify the distinguished name (DN) of a reference entry. The trigger uses this entry’s attributes as a template to define sub-fields in the **Search by** field and retrieve values from matching entries. |
| Trigger on | Select whether to search at a **Specific interval** or **Specific date/time**. |
| Entry search filter | Enter [LDAP filters](https://ldap.com/ldap-filters/) to define search conditions. For example, enter `(ou=Dev)(objectClass=Person)` to retrieve only `Person` entries from the `Dev` organization unit. |
| Batch size | Specify the number of entries to process in each batch. The default value is 100 and the maximum is 1,000 entries. |
| Limit | Enter the maximum number of entries you plan to retrieve for each trigger event. The maximum is 1,000 entries. |
| Search by | Enter values for each attribute you plan to filter by. Only entries that match all the provided values are processed. This field includes sub-fields for each attribute of the reference entry. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Trigger on** selection. Use these fields to specify the trigger schedule.

## Output

| Input field | Description |
| --- | --- |
| Entries | A list of retrieved entries and their values for attributes defined by the reference entry. |
| First batch | Indicates whether the current batch is the first batch. |
| Last batch | Indicates whether the current batch is the last batch. |

---
