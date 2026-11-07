---
url: 'https://docs.workato.com/en/connectors/xero/search-credit-notes.md'
description: >-
  The Search credit notes batch action in the Xero connector lets you find
  credit notes using criteria such as the credit note ID.
---

# Xero - Search credit notes batch action

The **Search credit notes** batch action allows you to find credit notes using specific criteria, such as the credit note ID. You must provide at least one search field.

![Search accounts action](/assets/search-credit-notes-action.BeSoZ19w.png)_Xero - Search credit notes batch action_

## Input

| Input field | Description |
| --- | --- |
| Credit note ID | Enter the Xero internal ID of the credit note you plan to search for. This ID is typically found at the end of the credit note's URL. |
| Type | Specify the type of credit note. |
| Date | Select a date to find credit notes created after this specific date. |
| Status | Enter the status to filter credit notes. Valid values include `DRAFT`, `SUBMITTED`, `DELETED`, `AUTHORISED`, `PAID`, and `VOIDED`. |
| Line amount types | Input the line amount type you plan to filter. |
| Credit note number | Provide the credit note number. |
| Reference | Input a reference number associated with the credit note for your search. |

## Output

| Output field | Description |
| --- | --- |
| Credit notes | Details about the credit note records. |

---
