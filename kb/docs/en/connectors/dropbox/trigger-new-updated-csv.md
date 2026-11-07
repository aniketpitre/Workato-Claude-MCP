---
url: 'https://docs.workato.com/en/connectors/dropbox/trigger-new-updated-csv.md'
description: >-
  The New/updated CSV file in directory trigger in the Dropbox connector fires
  when a CSV file is added or updated in a folder or subfolders.
---

# Dropbox - New/updated CSV file in directory trigger

Triggers when a new CSV file is added or existing CSV file is updated in a specified folder. New and updated CSV files in subfolders will also be picked up.

![New/updated CSV file in directory](/assets/updated-csv-trigger.C7-Wazyi.gif)_New/Updated CSV file in directory trigger_

## Input

| Field name | Description |
| --- | --- |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up CSV files modified from this specified date and time. Defaults to fetching CSV files created/updated an hour ago if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Folder / Folder path | The folder to monitor for new/updated CSV files. Sub-folders will also be monitored. |
| Column delimiter | The character used to separate column values in your CSV file. |
| Batch size | Number of CSV rows to process per batch. Instead of reading rows one by one, Workato reads a batch of CSV rows at a time to increase throughput. [Learn more about batch processing](/en/features/batch-processing). |
| Obtain a direct URL to file? | Generate a public URL that lives for 4 hours. This URL can be obtained from the URL datapill in the trigger output. |
| Add column names manually? | Set column names manually. Otherwise the first row of the latest CSV file in the selected folder will be taken to get column names. |
| Column names | Enter CSV column names, each on a new line. By default, the column names of the latest CSV file in your selected folder will be retrieved. |

## Output

| Field name | Description |
| --- | --- |
| Path | File path. |
| Bytes | File size in bytes. |
| Size | File size in string format. |
| Mime type | The Mime type of this file. |
| URL | File's public URL. Can be used to download file using the [Workato file connector](/en/features/handling-binary-files#download-file-content-from-public-url). |
| URL expires | Date/time the file's public URL will expire. |
| Rev | A unique identifier for the current revision of the file. |
| Modified | Date/time the file was last modified. |
| Client modified time | This is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not. |
| Is directory | Whether this is a directory/folder. |
| Read only | Whether this file is read only. |
| Modifier | The user who modified this file. |
| Content hash | A hash of the file content. This field can be used to verify data integrity. For more information see [Box's Content hash page](https://www.dropbox.com/developers/reference/content-hash). |
| Thumb exists | Whether thumbnail exists. |
| Icon | String contents of file icon. |
| First batch | Whether this is the first batch of CSV lines. |
| Last batch | Whether this is the first batch of CSV lines. |
| Lines | A [list datapill](/en/features/list-management) representing the list of CSV lines. Can be used with [Repeat step](/en/recipes/steps#repeat-step) to loop through the CSV lines. |
| \- Line | The CSV line number. |
| \- Columns | Contains the CSV columns' values in this CSV line. |
| \- List size | Total number of CSV lines. |

---

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

---
