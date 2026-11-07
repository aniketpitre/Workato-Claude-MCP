---
url: 'https://docs.workato.com/en/connectors/wrike/get-record-id-action.md'
description: >-
  The Get record ID action in the Wrike connector converts a legacy record ID to
  its API v4 format for use in other Wrike actions.
---

# Wrike - Get record ID action

The **Get record ID** action converts a legacy record ID in Wrike to its API v4 format. You can use the API v4 in actions such as [Get task by ID](/en/connectors/wrike/get-task-by-id-action), [Get folder by ID](/en/connectors/wrike/get-folder-by-id-action), and [Get attachment metadata](/en/connectors/wrike/get-attachment-meta-action).

## Input

| Input field | Description |
| --- | --- |
| Record type | Select the type of record to convert to API v4 format. |
| Record IDs | Enter one or more legacy record IDs. You can find these IDs at the end of the URL when you access the record in the Wrike web interface. For example, in the permalink `https://files.wrike.com/123456/123456789`, the last 9 digits (`123456789`) represent the legacy record ID. Example input: `123456789, 987654321`. |

## Output

| Output field | Description |
| --- | --- |
| ID mappings | List of ID mappings between API v4 and legacy formats. |
| API v4 ID | The converted API v4 format ID. |
| Legacy ID | The original legacy format ID. |
| List size | Total number of records in the batch. |
| List index | Position of the current record in the batch. |

---
