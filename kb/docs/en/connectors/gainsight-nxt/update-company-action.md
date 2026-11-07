---
url: 'https://docs.workato.com/en/connectors/gainsight-nxt/update-company-action.md'
description: >-
  The Update company record/s action updates up to 50 records in the Company
  object in Gainsight NXT.
---

# Gainsight NXT - Update company record/s action

The **Update company record/s** action updates up to 50 records in the Company object in `Gainsight NXT`. You can apply an import lookup configuration to populate GSIDs into a field by referencing it from the same object or a different object.

## Input

| Input field | Description |
| --- | --- |
| Object fields | Select a maximum of three fields to identify the existing records to update. |
| Companies | A list of up to 50 company records to update. Each record accepts the writable fields of the **Company** object, such as `Name`, `Industry`, `Average recurring revenue`, `Number of employees`, `Stage`, `Status`, and `Tags`. |

Refer to the [Gainsight NXT API](https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation) documentation for additional input fields.

## Output

This action has multiple output fields. Refer to the [Gainsight NXT API](https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Company_and_Relationship_API/Company_API_Documentation) documentation for a complete list of output fields.

---
