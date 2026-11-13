---
url: 'https://docs.workato.com/en/managed-file-transfer/transfer-flows.md'
description: >-
  Configure file transfers to automate file movement between systems, including
  detection, validation, transformation, and delivery.
---

# Transfer orchestration

File transfers automate the movement of files between systems. Each transfer manages the full lifecycle, including detection, validation, transformation, delivery, and deletion. Transfers include built-in scheduling, processing, and error handling.

![A configured file transfer](/assets/transfer-flow.CvXJy7Eh.png)_A configured file transfer_

- **Source**: Monitors a location for new files and picks them up based on a schedule.
  
- **Target:** File transfers upload files to a target location after processing.
  

## Supported endpoint types

File transfers support the following connections as a source or target:

- [Workato FileStorage](/en/features/filestorage/filestorage-console)
- External SFTP server

Workato plans to support the following additional connections:

- Amazon S3
- Azure Blob Storage
- Sharepoint
- HTTPS

Refer to the [Add a source](#add-a-source) and [Add a target](#add-a-target) sections for more information about connections.

> **ON-PREMISES ENDPOINTS**
> 
> Use the Workato OPA for dedicated MFT use cases such as transferring files directly between two on-premises SFTP servers without routing file payloads through the Workato Cloud.

## Configure a file transfer

Each file transfer supports one source and one target. Complete the following steps to create a new file transfer that automates file movement between systems:

1. Click **Create > File transfer**. The **Create a file transfer** modal displays.
   
   ![The Create a file transfer modal](/assets/create-file-transfer.DHizzDBT.png)_The **Create a file transfer** modal_
   
2. Enter a descriptive **Transfer name**. For example: `Partner Orders Import` or `Daily Report to S3`. Names must be unique within a project.
   
3. Optional. Enter a **Description** of what the transfer does. This field has a maximum of 350 characters.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the file transfer.
   
5. Click **Start building**. The file transfer is created in an **Inactive** state and the **Transfer** page displays.
   
6. Refer to [Add a source](#add-a-source) and [Add a target](#add-a-target) to complete the remaining set up steps.
   

### Add a source

Sources define where to pick up files, when to check for new files, and how to handle source files after a successful transfer.

Complete the following steps to add a source to your file transfer:

1. Select the **File transfer** asset you plan to configure.
   
2. Click **\+ Add source**. The **Add source** setup wizard displays.
   
   ![The Add source setup wizard](/assets/add-source.27HRMRXM.png)_The **Add source** setup wizard_
   
3. Enter a descriptive name in the **Source name** field. For example: `Partner SFTP` or `Bank Reports`. This name appears in logs and monitoring.
   
4. Use the **Source type** drop-down menu to select a connection type. Workato supports the following connections:
   
   - [Workato FileStorage](/en/features/filestorage/filestorage-console)
   - External SFTP server
   
   Workato plans to support the following additional connections:
   
   - Amazon S3
   - Azure Blob Storage
   - Sharepoint
   - HTTPS
5. Connections are reusable across all flow assets including file transfers. Use the **Connection** drop-down menu to select a connection if your **Source type** is **External SFTP**. You can also click **Create new connection**, then click **Refresh** to update the list.
   
6. Enter the folder path to retrieve files from in the **Source directory path** field. Ensure the source connection has permission to download from this path.
   
7. Use the **Only transfer files with a successful virus scan** toggle to set the transfer's security scan behavior if your **Source type** is **FileStorage**. FileStorage automatically scans files up to 100 MB.
   
8. Enter a pattern to filter files by in the **File name filter** field. Use the drop-down menu to select a pattern type. Select **Wildcard** for simple patterns or [Regex](/en/regex) for advanced matching.
   
   Wildcards
   
   Wild card patterns use the following format:
   
   - Single character wildcard `?`
     
   - Represents one instance of any character. For example, `Report_draft_?.pdf` can represent `Report_draft_1.pdf`, `Report_draft_2.pdf` or `Report_draft_3.pdf`.
     
   - Multiple character wildcard `*`
     
   - Represents zero or more instances of any character. For example, `Report_draft*.pdf` can represent `Report_draft.pdf`, `Report_draft_1.pdf`, `Report_draft_2.pdf` or `Report_draft_3.pdf`.
     
   
9. Use the **Source file handling** to configure what happens to files at the source after a successful transfer:
   
   - **Keep at source** (default): Files remain at the source directory.
   - **Archive**: Moves the file to a configured archive subfolder. Requires write and delete permission at the source. Archived files can't be retried from the UI.
   - **Delete**: Permanently deletes the file. Requires delete permission at the source. Deleted files can't be retried from the UI.
10. Click **Next**, then refer to the [Schedule transfers](#schedule-transfers) section to configure the transfer schedule.
    

#### Schedule transfers

Complete the following steps to schedule file transfers after you [add a source](#add-a-source):

**Intervals**

1. Use the **Time unit** drop-down menu to select the scale for your schedule, such as `Minutes`, `Hours`, or `Days`.
   
   ![The Schedule transfer page](/assets/schedule.6qZfYvxP.png)_The **Schedule transfer** page_
   
2. Enter an interval in the **Trigger every** field based on the selected time unit.
   
   For example, select **Hours** and enter **12** to trigger the transfer every 12 hours. The minimum interval you can set is 5 minutes.
   
3. Select a **Timezone** for the schedule. This field defaults to your workspace's timezone when left blank.
   
4. Enter a start date and time in the **Start after** field or leave it blank to start after activation.
   
5. Click **Add** to add the source, then continue to [Add a target](#add-a-target) to configure where to deliver files and what processing actions to perform on files before delivery.
   

**Custom schedule (Cron expressions)**

1. Use the **Time unit** drop-down menu to select **Custom schedule**. This allows you to define scheduling with a cron expression.
   
2. Enter a schedule in the **Cron expression** field using the following format:
   
   ```text
   [minute] [hour] [day of month] [month] [day of week]
   ```
   
   - `*`: Any value
   - `,`: Value list separator
   - `-`: Value range
   - `/`: Step values
   
   For example, enter `0 8 * * *` to sync every day at 8:00 AM.
   
3. Optional. Select a **Timezone** for the cron expression. This field defaults to your workspace's timezone when left blank.
   
4. Optional. Select a date and time to start the transfer in the **When first started, this transfer should pick up records from** field or leave it blank to start immediately.
   
   You can't change this value after you run the transfer. Refer to the [When first started, this recipe should pick up events from](/en/recipes/triggers#since-from) section for more information.
   
5. Click **Add** to add the source, then continue to [Add a target](#add-a-target) to configure where to deliver files and what processing actions to perform on files before delivery.
   

### Add a target

Targets define where to deliver files and what processing actions to perform on files before delivery.

Complete the following steps to add a target to your file transfer:

1. Select the **File transfer** asset you plan to configure.
   
2. Click **\+ Add target**. The **Add target** setup wizard displays.
   
   ![The Add target setup wizard](/assets/add-target.Cv4ndcY7.png)_The **Add target** setup wizard_
   
3. Enter a descriptive name for the target in the **Target name** field. This name appears in logs and monitoring.
   
4. Use the **Target type** drop-down menu to select a connection type. Workato supports the following connections:
   
   - [Workato FileStorage](/en/features/filestorage/filestorage-console)
   - External SFTP server
   
   Workato plans to support the following additional connections:
   
   - Amazon S3
   - Azure Blob Storage
   - Sharepoint
   - HTTPS
5. Use the **Connection** drop-down menu to select a connection if your **Target type** is **External SFTP**. Connections are reusable across all flow assets including file transfers. You can also click **Create new connection**, then click **Refresh** to update the list.
   
6. Enter the folder path to deliver files to in the **Target directory path** field. Ensure the target connection has the permission to upload to this path.
   
7. Use the **When a file already exists at destination** field to configure conflict resolution:
   
   - **Skip** (default): Doesn't transfer the file and logs the event as **Skipped**. Note that skipped files are considered successful runs, so the source-file handling rule configured in **Set up source** still applies.
   - **Overwrite**: Replaces the existing file at the destination. The original file is permanently replaced and can't be recovered.
8. Click **Next**, then continue to [Processing actions](#processing-actions).
   

#### Processing actions

Processing actions are performed on files after pickup from the source and before delivery to the target. Workato MFT supports the following processing actions:

| Action | Description |
| --- | --- |
| PGP encryption | Encrypt files using a PGP public key. Create and select a connection to the [PGP tools by Workato](/en/connectors/pgp-by-workato#set-up-pgp-tools-by-workato) connector to define your PGP keys for this transfer. |
| PGP decryption | Decrypt files using a PGP private key. Create and select a connection to the [PGP tools by Workato](/en/connectors/pgp-by-workato#set-up-pgp-tools-by-workato) connector to define your PGP keys for this transfer. |
| Rename | Rename files dynamically using functions and the following variables: **Original file name:** The source file name without an extension., **Original file extension:** The file extension. For example: `.csv` |
| Compression | Compress files into ZIP, TAR, or GZIP format. |
| Decompression | Decompress ZIP, TAR, or GZIP formatted files. The archive must contain only one file. |

Complete the following steps to define processing actions after you [add a target](#add-a-target):

1. Select the **File transfer** asset you plan to configure.
   
2. Click **...** (ellipsis) on the target.
   
3. Click **Edit processing actions**.
   
4. Click **\+ Add action** to add a new processing action.
   
5. Configure the action, then click **Save**.
   

### Configure settings

The **Settings** page allows you to configure the following aspects of your file transfer:

**Retry settings**

Workato uses exponential backoff with jitter for optimal retry behavior.

Configure the retry behavior for failed runs using the following settings:

- **Maximum retry duration**: Set a maximum duration for retry attempts. The minimum value is `5 minutes`, the maximum is `24 hours`, and the default is `1 hour`. Individual attempts have a quota of 8 hours, regardless of your selection.
  
- **Maximum retry attempts**: Enter a quota for the number of retry attempts. The maximum value is `10` and the default is `3`.
  

Workato stops retrying a run when either the duration or the attempt quota is reached, whichever comes first. For example, a **Maximum retry attempts** value of `3` allows 1 original attempt and 3 automatic retries for a total of 4 attempts per run.

Refer to the [Error handling and retries](/en/managed-file-transfer/error-handling-and-retries) documentation for more information.

**Concurrency**

Use the **Concurrency limit** setting to configure the number of runs the file transfer processes simultaneously. Select a higher number for high volume transactions.

**Auto-stop on errors**

Use the **Consecutive run error threshold** setting to configure the number of consecutive runs that must exhaust their retry attempts and fail before Workato stops the transfer. The minimum value is `1`. This setting applies per transfer and can't be disabled.

Refer to [Transfer auto-stop](/en/managed-file-transfer/error-handling-and-retries#transfer-auto-stop) for more information.

## Start a transfer

Complete the following steps to start a file transfer after adding a [source](#add-a-source) and a [target](#add-a-target):

1. Select the **File transfer** asset you plan to start.
   
2. Click **Start transfer**. The status changes from **Inactive** to **Active**. Transfers begin based on the schedule and **Start after** time configured during [source setup](#add-a-source). Restarting a stopped transfer doesn't trigger an immediate poll; it waits until the next scheduled poll time.
   

## Check for files now

Complete the following steps to poll a file transfer immediately, without waiting for its next scheduled poll:

1. Select the **File transfer** asset you plan to poll.
   
2. Go to the **Runs** tab.
   
   ![The Runs tab](/assets/runs-tab.BCeepQik.png)_The **Runs** tab_
   
3. Click **Check for files now**.
   
   The transfer checks for new files and reschedules the next poll based on the current time and the configured poll interval.
   

## Stop a transfer

Complete the following steps to stop a file transfer:

1. Select the **File transfer** asset you plan to stop.
   
2. Click **Stop transfer**. The status changes from **Active** to **Inactive**.
   
   Scheduled runs pause and in-progress file transfers complete. Transfers you [resume](#start-a-transfer) continue processing files from the poll event where they stopped.
   

## Quotas

File transfers have the following quotas:

| Description | Quota |
| --- | --- |
| Maximum file size for a file transfer | No limit |
| Maximum duration of a single transfer attempt | 8 hours |

> **FEATURE AVAILABILITY**
> 
> Contact your Customer Success Manager for information about access to Workato MFT.

---

---
url: >-
  https://docs.workato.com/en/managed-file-transfer/error-handling-and-retries.md
description: >-
  Configure automatic retry and error handling for file transfers to recover
  from transient failures and ensure reliable delivery.
---

# Error handling and retries

File transfers include built-in error handling to ensure reliable file delivery. Select a run in the transfer's **Runs** tab to see its [attempt history](/en/managed-file-transfer/alerts-and-monitoring#attempt-history), including the status of each retry and error details.

![Attempt history](/assets/attempt-history.DQ1pt4MK.png)_Attempt history_

## Automatic retry

File transfers automatically retry failed runs. Workato doesn't classify failures by error type or distinguish transient from permanent issues. The same retry settings apply to every failure.

For example, an attempt fails if it exceeds the maximum attempt duration of 8 hours. The failure automatically triggers another attempt, unless the run has reached the maximum retry duration, maximum retry attempts, or consecutive run error threshold.

Workato uses exponential backoff with jitter between attempts, increasing the delay between each retry to reduce load on a struggling endpoint.

### Automatic retry settings

Complete the following steps to configure automatic retry settings:

1. Select the **File transfer** asset that you plan to configure.
   
2. Go to **Settings > Retry settings**.
   
   ![Retry settings](/assets/retry-settings.NRwPU3Nz.png)_Retry settings_
   
3. Configure the retry behavior for failed runs using the following settings:
   
   - **Maximum retry duration**: Set a maximum duration for retry attempts. The minimum value is `5 minutes`, the maximum is `24 hours`, and the default is `1 hour`. Individual attempts have a quota of 8 hours, regardless of your selection.
     
   - **Maximum retry attempts**: Enter a quota for the number of retry attempts. The maximum value is `10` and the default is `3`.
     
   
   Workato stops retrying a run when either the duration or the attempt quota is reached, whichever comes first. For example, a **Maximum retry attempts** value of `3` allows 1 original attempt and 3 automatic retries for a total of 4 attempts per run.
   
4. Click **Save**.
   

## Manual retry

Complete the following steps to manually retry a transfer run. Manual retries don't count toward the transfer's [consecutive run error threshold](#transfer-auto-stop).

1. Select the **File transfer** asset that you plan to retry.
   
2. Go to the **Runs** tab.
   
3. Select rows, then click **Retry runs**. You can retry both successful and failed runs.
   
   ![Manual retry](/assets/retry-transfer.DK255WDS.png)_Manual retry_
   

## Transfer auto-stop

Workato tracks how many consecutive runs have exhausted their automatic retry attempts and automatically stops the transfer when this count reaches the **Consecutive run error threshold**.

When a transfer auto-stops:

- The transfer's status changes to **Inactive**.
- An error banner displays on the file transfer page with the reason for the stop.
- Workato sends a notification to the MFTOps [Transfer stopped](/en/connectors/mftops/triggers/transfer-stopped) trigger.

Auto-stop also affects files based on their state at the time of the stop:

| File state | Resulting status |
| --- | --- |
| The file whose run triggered the auto-stop | **Failed** |
| Files queued but not yet picked up | **Stopped** |
| Files already in-flight | Continue running normally; unaffected by the stop |

Investigate and resolve the underlying issue, then manually reactivate the transfer. Refer to [Start a transfer](/en/managed-file-transfer/transfer-flows#start-a-transfer) for activation steps.

### Auto-stop settings

Complete the following steps to configure auto-stop settings:

1. Select the **File transfer** asset that you plan to configure.
   
2. Go to **Settings > Auto-stop on errors**.
   
   ![Auto-stop settings](/assets/auto-stop-settings.sRCToe34.png)_Auto-stop settings_
   
3. Set a **Consecutive run error threshold** that configures the number of consecutive runs that must exhaust their retry attempts and fail for Workato to stop the transfer. The minimum value is `1`. This setting applies per transfer and can't be disabled.
   
   Refer to [Transfer auto-stop](#transfer-auto-stop) for more information.
   
4. Click **Save**.
   

> **FEATURE AVAILABILITY**
> 
> Contact your Customer Success Manager for information about access to Workato MFT.

---
