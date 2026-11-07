---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/search-record-batch.md'
description: >-
  The Search record batch action in the HubSpot connector retrieves multiple
  records of a selected object that match the given search criteria.
---

# HubSpot - Search record action (batch)

The **Search record** batch action retrieves multiple records of an object you specify that match the given search criteria. To configure this action, first select the object to search.

This action supports the following objects:

- Contact
- Company
- Deal
- Product
- Ticket
- Line Item
- Quote
- Custom Objects

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to trigger jobs off. |
| Fields to retrieve | If not configured, Workato returns the default set of properties for each record type. You can pull in custom sets of properties by configuring this input. Custom fields are supported. |
| Filter Groups | Use filters to search records that meet your filter criteria. When multiple filter groups are provided, they are combined using a logical \`OR\` operator. You can have a maximum of three filter groups and each filter group can have a maximum of three sub filters. Each sub filter within a filter group is joined using a logical AND operator. For example, filter group 1 with sub filter A and sub filter B, alongside filter group 2 with sub filter C and sub filter D are joined into a query as - (A **AND** B) **OR** (C **AND** D). |
| Quota | Maximum number of rows to return. Minimum is 1 and maximum is 100. Defaults to 100. Not all rows are returned as a single response in the output. The user must paginate to obtain all the requisite records. |
| Offset | Number of rows to skip. For example, 100. Defaults to 0. Use this input to paginate and retrieve more rows. |

## Output

Workato returns a set of records matching the filters defined in the action. The properties selected in **Fields to retrieve** are returned as datapills. If left blank, only the default fields are returned. A paging object is returned as well to allow the user to paginate and obtain more records if present. The total records are indicated along with the current offset.

---
