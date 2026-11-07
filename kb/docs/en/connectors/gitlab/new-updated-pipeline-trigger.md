---
url: 'https://docs.workato.com/en/connectors/gitlab/new-updated-pipeline-trigger.md'
description: >-
  The New/updated pipeline trigger monitors GitLab and triggers when a pipeline
  is created or updated.
---

# GitLab - New/updated pipeline trigger

The **New/updated pipeline** trigger monitors GitLab for a new or updated pipeline.

## Input

| Input field | Description |
| --- | --- |
| Project or Project ID | Select a project from the drop-down menu or enter the ID. |

## Output

| Output field | Description |
| --- | --- |
| ID | The pipeline ID. |
| Internal ID | The internal ID that resets or counts sequentially per project. |
| Project ID | The ID assigned to every repository and project upon creation. |
| SHA | The Secure Hash Algorithm is a 40-character alphanumeric string that acts as an immutable fingerprint for a specific state of your repository files and history. |
| Reference | Values can be a semantic version (`1.0`), a partial version (`latest`), a branch name, or a specific commit SHA. |
| Status | The lifecycle phase of a specific build or process. Options include `pending`, `running`, `success`, `failed`, `canceled`, `skipped`, and `manual`. |
| Source | The origin or the event that caused the pipeline to run. Options include `push`, `merge_request_event`, `trigger`, `pipeline`, `schedule`, and `web`. |
| Created At | A standard timestamp that indicates the exact date and time an object was initially generated. |
| Updated At | A standard timestamp that indicates the exact date and time an object or record was last modified. |
| Web URL | The direct, human-readable HTTPS address to view a specific resource (such as a project, commit, or merge request) in a web browser. |
| Name | The pipeline name. |

---

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

---
