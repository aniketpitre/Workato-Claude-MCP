---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/create-document-relationship-action.md
description: >-
  The Create document relationship action links a source document version to a
  target document in Veeva Vault.
---

# Veeva Vault - Create document relationship action

The **Create document relationship** action creates a relationship on a source document version, linking it to a target document, in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| Source document type | Select the source document type. This list is populated dynamically from your Vault. Select this first, since it determines the available **Relationship type** options. |
| Relationship type | Select the relationship type. Options depend on the **Source document type** you select. This list is populated dynamically from your Vault. Standard system types, such as **Based On**, might not be creatable through the API. |
| Source document ID | Enter the internal Vault document ID of the source document, for example `776`. |
| Source major version | Enter the major version of the source document, for example `0`. |
| Source minor version | Enter the minor version of the source document, for example `1`. |
| Target document ID | Enter the internal Vault document ID of the target document. |
| Target major version | Optional. Enter the major version of the target document. Required for target version-specific relationship types. |
| Target minor version | Optional. Enter the minor version of the target document. Required for target version-specific relationship types. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the relationship creation operation. |
| Response message | A message describing the result of the operation. |
| Relationship ID | The ID of the created relationship. If the relationship already exists, Vault returns `0`, which is expected and not a failure. |
