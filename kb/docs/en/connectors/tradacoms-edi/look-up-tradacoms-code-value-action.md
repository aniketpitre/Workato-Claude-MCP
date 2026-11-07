---
url: >-
  https://docs.workato.com/en/connectors/tradacoms-edi/look-up-tradacoms-code-value-action.md
description: >-
  Translate a standard TRADACOMS ANA code, such as a transaction code or VAT
  category, into its meaning.
---

# TRADACOMS EDI - Look up TRADACOMS code value action

The **Look up TRADACOMS code value** action translates a standard Article Numbering Association (ANA) code, for example a transaction code, VAT category, or priority, into its meaning in TRADACOMS EDI.

## Input

| Input field | Description |
| --- | --- |
| Code list | Select the ANA code list to use, or enter an element code, for example `TCDE` or `VATC`. |
| Code | Enter the code value to look up, for example `0430` or `S`. The action keeps leading zeros on numeric codes, so enter `0430` instead of `430`. |

## Output

| Output field | Description |
| --- | --- |
| Code | The matched code. Returns the code you entered if the action finds no match. |
| Found | A boolean value (`true` or `false`) that indicates whether the action found the code in the selected code list. |
| Meaning | The code's meaning, for example `New orders`. Empty if the action finds no match. |
| List name | The selected code list's full name, for example `VAT rate category code (ANA List 12)`. |
| Entries | Every code in the selected code list. |
| Code (Entries) | The entry's code. |
| Meaning (Entries) | The entry's meaning. |
