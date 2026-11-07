---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/transform-record-action.md
description: >-
  The Transform record to record action transforms an existing record into
  another record type in NetSuite REST.
---

# NetSuite REST - Transform record action

The **Transform record** action transforms an existing record into another record type in NetSuite REST.

Use this action to create a target record from an existing source record. For example, you can transform a cash sale into a return authorization when NetSuite supports that transformation pair.

The available **Transform to** options depend on the selected **Source record**. After you select **Transform to**, the action displays additional fields that match the selected target record type.

Refer to the [Supported transformation types](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4267258715.html) for valid source-to-target combinations. For setup requirements, see [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html).

## Input

| Input field | Description |
| --- | --- |
| Source record | Select the NetSuite record type to transform from. Only supported source record types appear in the list. |
| Transform to | Select the target NetSuite record type to return after the transformation. This list changes based on the selected **Source record**. |
| Internal ID | Enter the internal ID of the existing source record instance to transform. |

Additional fields appear based on the **Source record** and **Transform to** values you select. These fields update dynamically to match the selected transformation pair.

## Output

| Output field | Description |
| --- | --- |
| Location | The REST resource location of the transformed record returned by NetSuite. |
| Internal ID | The internal ID assigned to the transformed record. |
