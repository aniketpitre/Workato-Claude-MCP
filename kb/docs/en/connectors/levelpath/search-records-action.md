---
url: 'https://docs.workato.com/en/connectors/levelpath/search-records-action.md'
description: >-
  The Search records action searches for existing records in LevelPath based on
  object type and filter criteria.
---

# LevelPath - Search records action

The **Search records** action searches for existing records in LevelPath based on the selected object type and criteria.

## Input

| Input field | Description |
| --- | --- |
| Object type | Required. Select the LevelPath object to search. |

Additional input fields appear based on the object type you select. These fields define search filters for the record query.

## Output

The output fields vary depending on the selected object type. For example, if you select **Supplier** as the **Object type**, the output may include the following fields:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the supplier. |
| External ID | External reference ID. |
| Corpus ID | Corpus record identifier. |
| Name | Supplier name. |
| Website | Supplier website URL. |
| Employee ID number | Identifier for the supplier’s employee. |
| Description | Description of the supplier. |
| Primary category ID | ID of the primary category. |
| Ticker | Public stock ticker symbol. |
| Stock exchange | Stock exchange where the supplier is listed. |
| Fiscal year end | Month and day the fiscal year ends. |
| Domain | Email or web domain of the supplier. |
| Status | Current status of the supplier. |
| Notes | Notes about the supplier. |
| Is customer | Indicates if the supplier is also a customer. |
| Is preferred | Indicates if the supplier is preferred. |

---
