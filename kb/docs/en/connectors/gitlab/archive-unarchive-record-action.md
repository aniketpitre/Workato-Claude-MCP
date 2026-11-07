---
url: >-
  https://docs.workato.com/en/connectors/gitlab/archive-unarchive-record-action.md
description: The Archive/Unarchive record action archives or unarchives a record in GitLab.
---

# GitLab - Archive/Unarchive record action

The **Archive/Unarchive record** action archives or unarchives a record in GitLab.

## Input

| Input field | Description |
| --- | --- |
| Object | Select an object from the drop-down menu. |
| Object ID | Enter the object ID. |
| Operation | Select the operation from the drop-down menu or enter the value. The options are `Archive` or `Unarchive`. |

## Output

| Output field | Description |
| --- | --- |
| ID | The record ID. |
| Description | The record description. |
| Name | The record name. |
| Name with namespace | A string value that combines the project readable title with the name of the group, subgroup, or personal user space that contains it. The format is: `[Namespace Name] / [Project Name]`. For example, `MyCompany Group / Web App Project`. |
| Path | The specific location of the record. It's a string representing the ID or URL-encoded path of the project or branch. |
| Created At | A standard timestamp that indicates the exact date and time the record was initially generated. |
| Default Branch | The primary branch of a repository. For example, `main` or `master`. |
| Tag List | An array of strings (comma-separated or in a list format) that displays all the topic tags associated with the record. |
| Topics | An array of strings that contains the descriptive labels or tags assigned to a record. |
| Visibility | Indicates who can access and view the record. The options are: `public`, `internal`, and `private`. |
