---
url: 'https://docs.workato.com/en/connectors/google-vault/get-record-by-id-action.md'
description: The get record by ID action enables you to get a record in Google Vault.
---

# Google Vault - Get record by ID action

The **Get record by ID** action enables you to retrieve a record in Google Vault.

![Google Vault Get record by ID action](/assets/google-vault-get-record-by-id-action.1Z6Oc-I3.png)_Google Vault **Get record by ID** action_

## Input

| Input Field | Description |
| --- | --- |
| Object | Specify the object you plan to retrieve. Fields dynamically load based on the selected object. |

## Output

The output fields are determined by the object you select in the input. Map the relevant datapills from the data tree for downstream steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-vault/remove-accounts-from-hold-action.md
description: >-
  The remove accounts from hold action enables you to remove accounts from an
  accounts-based hold in Google Vault.
---

# Google Vault - Remove accounts from hold action

The **Remove accounts from hold** action enables you to remove accounts from an account-based hold in Google Vault.

![Google Vault Remove accounts from hold action](/assets/google-vault-remove-accounts-from-hold-action.FPsCrGbL.png)_Google Vault **Remove accounts from hold** action_

## Input

| Input Field | Description |
| --- | --- |
| Hold ID | Use the **Hold ID** drop-down menu to select a hold from Google Vault, or enter the ID manually. |
| Matter ID | Use the **Matter ID** drop-down menu to select a hold from Google Vault, or enter the ID manually. |
| Account IDs | Enter a comma-separated list of account email addresses to remove from the hold. |
| Details output field | Describe custom output fields present in the details of the output schema |

## Output

| Output Field | Description |
| --- | --- |
| Code | The HTTP response status code. |
| Message | A developer-facing error message, if any. |
| Details | A list of messages that contain additional error details, if applicable. |

---
