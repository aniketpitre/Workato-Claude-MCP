---
url: 'https://docs.workato.com/en/connectors/jira/create-issue-action.md'
description: This action creates a new issue in Jira.
---

# Jira - Create issue action

The **Create issue** action creates a new issue in Jira.

## Input

| Input field | Description |
| --- | --- |
| Project issue type | Select the project and issue type of the issue. Alternatively, you can use the **Select from list** drop-down menu to select **Enter project and issue type**, then use the following format to dynamically generate the project issue type: Key`--`Name. Note that this prevents Workato from generating input fields for the issue at design-time unless you use the **Sample project issue type** field. |
| Sample project issue type | Select the project and issue type to retrieve custom fields from. Use this field when dynamically creating issues across multiple projects or issue types. |
| Summary | Enter a summary for the issue. This field may be required, depending on your Jira field configuration. |
| Reporter account ID | Enter the ID of the account to assign as the issue's reporter. |
| Description | Enter a description for the issue. |
| Issue priority | Select a priority level for the issue. |
| Assignee account ID | Enter the ID of the account to assign the issue to. |

Additional fields load dynamically based on your **Project issue type** and **Sample project issue type** selections. Use these inputs to configure values for the issue fields.

## Output

| Output field | Description |
| --- | --- |
| ID | The numeric Jira identifier for the new issue. |
| Key | The human-readable Jira identifier for the new issue. |
| Self | The API URL of the new issue. |

## Troubleshooting

Ensure the connected Jira account has sufficient permissions to view projects, issues, and fields if you encounter difficulties with this action.

Additionally, check Jira to ensure that fields are associated with the correct issue type, and that the issue type scheme is associated with the correct project.

Refer to the [Jira connector permissions guide](/en/connectors/jira#jira-permissions-helper) or the Jira [Permissions helper](https://confluence.atlassian.com/adminjiracloud/using-the-permission-helper-868982879) documentation for more details.

---
