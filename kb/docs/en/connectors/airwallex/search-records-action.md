---
url: 'https://docs.workato.com/en/connectors/airwallex/search-records-action.md'
description: >-
  The Search records action enables you to search and retrieve a list of records
  for an object in Airwallex.
---

# Airwallex - Search records action

The **Search records** action enables you to search and retrieve a list of records for an object in Airwallex.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to search and retrieve the list of records. Fields load dynamically based on the selected object. |

Refer to the following example input schema for the **Refunds** object:

| Input field | Description |
| --- | --- |
| Currency | Enter the currency of the refund. |
| Payment attempt ID | Select the payment attempt ID of the refund. |
| Payment intent ID | Select the payment intent ID of the refund. |
| Status | Select the refund status. |
| From created at | Enter the date and time to start searching from. |
| Page number | Enter the page number to search for. |
| Page size | Enter the page size to search for. |
| To created at | Enter the date and time to end the search. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. Refer to the following example output fields for the **Refunds** object:

| Output field | Description |
| --- | --- |
| Has more | Whether more pages are available. |
| Items | List of all refunds, including the following properties. |
| Acquirer reference number | Reference number provided by the acquirer for the refund. |
| Amount | Amount that has been refunded. |
| Created at | Date and time when the refund was created. |
| Currency | Currency in which the refund was processed. |
| ID | Unique identifier for the refund. |
| Metadata | A set of key-value pairs attached to the refund. |
| Key | Metadata key. |
| Value | Metadata value. |
| List size | Total number of metadata entries. |
| List index | Position of the metadata entry in the list. |
| Payment attempt ID | ID of the payment attempt against which this refund was created. |
| Payment intent ID | ID of the payment intent against which this refund was created. |
| Reason | Reason provided for the refund. |
| Request ID | Unique identifier for the refund request. |
| Status | Current status of the refund. For example: `ACCEPTED`. |
| Updated at | Date and time when the refund was updated. |

---
