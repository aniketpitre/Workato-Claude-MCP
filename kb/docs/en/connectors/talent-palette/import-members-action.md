---
url: 'https://docs.workato.com/en/connectors/talent-palette/import-members-action.md'
description: The import members action imports members in bulk in Talent Palette.
---

# Talent Palette - Import members action

The **Import members** action imports members in bulk in Talent Palette.

## Input

| Input field | Description |
| --- | --- |
| File | Provide the CSV file to import. |
| Header line number | Specify the line number of the header in the file. |
| Type | Select the operation type from the drop-down menu. |
| Update key names | Provide an array of strings specifying the keys used for the update operation. |
| Not update key names | Provide an array of strings specifying attributes that should not be updated. |
| Account column | Specify the column to import as the account. |
| Retirement date column | Specify the header linked to `retirement date`, if the file does not include such a column. |
| Convert CSV header merge data setting | Provide an array of `convertCsvHeaderMergeDataSetting` objects specifying header merge settings. |
| Import except master name | Specify the master name to exclude from the import process. |
| Convert data library setting | Provide an array of `convertDataLibrarySetting` objects specifying attributes to replace using a master library. |
| Convert add string setting | Provide an array of `convertAddStringSetting` objects specifying attribute value string addition settings. |
| Code page | Specify the file's character encoding. |
| Processing rule set | Specify the data processing rule set name to apply. |

## Output

| Output field | Description |
| --- | --- |
| Job ID | The Talent Palette ID of the registered job. |

---

---
url: >-
  https://docs.workato.com/en/connectors/talent-palette/import-organizations-action.md
description: >-
  The import organizations action imports organizations in bulk in Talent
  Palette.
---

# Talent Palette - Import organizations action

The **Import organizations** action imports organizations in bulk in Talent Palette.

## Input

| Input field | Description |
| --- | --- |
| File | Provide the CSV file to import. |
| Type | Select the operation type from the drop-down menu. |
| Update key names | Select the master key from the drop-down menu. This field is dynamically loaded when `Update history` is selected as `Type`. |
| Update sub key names | Select the sub key from the drop-down menu. This field will be dynamically loaded when `Update history` is selected as `Type`. |
| Code page | Specify the file's character encoding. |
| Processing rule set | Specify the data processing rule set name to apply. |

## Output

| Output field | Description |
| --- | --- |
| Job ID | The Talent Palette ID of the registered job. |

---
