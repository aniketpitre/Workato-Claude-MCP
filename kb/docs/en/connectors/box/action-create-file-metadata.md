---
url: 'https://docs.workato.com/en/connectors/box/action-create-file-metadata.md'
description: >-
  The Create file metadata action creates standard or custom metadata on a file
  in Box.
---

# Box - Create file metadata action

The **Create file metadata** action creates metadata on a file in Box. You can apply either a standard template or custom metadata. An enterprise account is required to create metadata templates. You can't add custom metadata if it already exists on the file. When you plan to use a standard template, select one from the template list. For custom metadata, you can either provide the ID of a sample file that already contains the metadata or enter new metadata values directly. Note that metadata names can't include special characters.

## Input

| Input field | Description |
| --- | --- |
| File ID | Enter the ID of the file where you plan to create metadata. |
| Metadata template | Select a metadata template to apply to the file. |
| Sample file ID with custom metadata | Enter the ID of a file with custom metadata. Use this to create new custom metadata. |

## Output

This action doesn't return output fields.

---
