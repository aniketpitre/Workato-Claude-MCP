---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/new-classification-record-trigger.md
description: >-
  The New classification record trigger detects new classification records in
  NetSuite REST.
---

# NetSuite REST - New classification record trigger

The **New classification record** trigger detects new classification records in NetSuite REST. Use this trigger to monitor classification records that don't include created or modified date fields. The trigger uses internal ID for polling.

## Input

| Input field | Description |
| --- | --- |
| Record type | Select the NetSuite classification record type to monitor. |
| When first started, this recipe should pick up events from ID | Enter the internal ID to start polling from. The trigger processes records with IDs greater than this value. Leave empty to start from ID 0. |
| Search query | Enter a search query to filter records. For example, `name CONTAIN test`. Don't filter by internal ID. |
| Search settings | Configure how the trigger retrieves and filters records. Refer to [Record Collection Filtering](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1545222128.html) for more information. |

Additional fields appear based on the selected **Record type**. These fields update dynamically to match the record you select.

## Output

The output fields vary based on the selected **Record type**. The trigger returns fields that correspond to the classification record you select.

For example, if you select **Analytical impact**, the output includes the following fields:

| Output field | Description |
| --- | --- |
| Acquisition Month End Date | The end date of the acquisition month associated with the analytical impact record. |
| Analytical impact event | The event type recorded for the analytical impact. |
| Analytical impact link | The reference link associated with the analytical impact record. |
