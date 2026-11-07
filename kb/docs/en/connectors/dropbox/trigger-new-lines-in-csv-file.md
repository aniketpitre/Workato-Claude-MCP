---
url: >-
  https://docs.workato.com/en/connectors/dropbox/trigger-new-lines-in-csv-file.md
description: >-
  The new lines in CSV file triggers in the Dropbox connector process existing
  CSV rows on recipe start in real-time or batch mode.
---

# Dropbox - New and new/updated lines in CSV file triggers

## New lines in CSV file trigger (real-time)

On recipe start, trigger will pick up all existing lines in the CSV file. Individual jobs will be processed for each new line updated. Trigger will not pick up lines subsequently added to the file.

![New lines in CSV file trigger](/assets/new-lines-csv-rt-trigger.CsagwrFB.png)_New lines in CSV file real-time trigger_

### Input

| Field name | Description |
| --- | --- |
| File / File path | The CSV file to monitor for new lines. |
| Column separator | The delimiter separating the values. |

### Output

The output fields of this trigger correspond to the values of updated columns of the chosen CSV file.

## New lines in CSV file trigger (batch)

On recipe start, trigger will pick up all existing lines in the CSV file. Each batch of new lines will be processed as a single trigger event. Trigger will not pick up lines subsequently added to the file.

![New lines in CSV file batch trigger](/assets/new-lines-csv-b-trigger.DI19_aZi.png)_New lines in CSV file batch trigger_

### Input

| Field name | Description |
| --- | --- |
| File / File path | The CSV file to monitor for new lines. |
| Column separator | The delimiter separating the values. |
| Batch | Number of CSV lines to be picked up in a single job. Defaults to 100. |
| File encoding type | Default encoding type is set to UTF-8, typically doesn't need to be changed. |

### Output

The output fields of this trigger correspond to the values of updated columns of the chosen CSV file trigger and will output them as an array of rows. The Batch datapill indicates that the output is a list containing data for each row in that batch.

![Batch datapill](/assets/batch-datapill.CqpEZ5EW.png)_Batch datapill_

## New/Updated lines in CSV file trigger (real-time)

CSV file must have a column containing datetime that line was updated (create counts as an update). When recipe is first started, lines updated after the From datetime will be picked up. Subsequently, any line with an updated datetime will be picked up.

![New/Updated lines in CSV file trigger](/assets/updated-lines-csv-rt-trigger.Cnle81cN.png)_New/Updated lines in CSV file real-time trigger_

### Input

| Field name | Description |
| --- | --- |
| File / File path | The CSV file to monitor for new lines. |
| Column separator | The delimiter separating the values. |
| From | New/updated lines after this time will be processed by the recipe. If left blank, the default date will be set to **one day** before the recipe is first started. |

### Output

The output fields of this trigger correspond to the values of updated columns of the chosen CSV file.
