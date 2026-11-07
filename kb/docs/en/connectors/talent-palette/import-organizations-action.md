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
