---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/initialize-record-action.md
description: >-
  The Initialize record action retrieves a pre-filled record without creating it
  in NetSuite REST.
---

# NetSuite REST - Initialize record action

The **Initialize record** action retrieves a pre-filled record without creating it in NetSuite REST.

The action populates a target record with data from an existing reference record and returns it without saving it in NetSuite, so you can inspect or modify the values before you create the record.

Use the [Transform record](/en/connectors/netsuite-rest/transform-record-action) action to create a record from an existing source instead of filling and retrieving it.

The **Record** and **Reference record** types must form a supported transformation pair. Refer to the [Supported transformation types](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4267258715.html#bridgehead_4327469981) for valid source-to-target combinations. For setup requirements, see [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html).

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to initialize. The action returns a pre-filled record of this type. |
| Reference record | Select the NetSuite record type of the existing reference record. The action uses data from this record to pre-fill the target record. |
| Reference record ID | Enter the internal ID of the existing reference record instance. |

## Output

The output is the pre-filled target record. The output schema reflects the record type you select in the **Record** field, including its standard fields and any custom fields configured in NetSuite. The available output fields vary by record type because the schema is dynamic. After you select a record type, the recipe editor displays the output fields for that record.
