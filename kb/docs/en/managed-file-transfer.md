---
url: 'https://docs.workato.com/en/managed-file-transfer.md'
description: >-
  Workato Managed File Transfer (MFT) provides secure, automated, scalable file
  transfers with encryption, scheduling, monitoring, and SFTP and FTP(s)
  servers.
---

# Managed File Transfer

Workato Managed File Transfer (MFT) is a standards-based, enterprise-grade solution for secure, automated, and scalable file transfers. MFT includes built-in encryption, scheduling, monitoring, and embedded SFTP and FTP(s) servers.

## Transfer orchestration

File transfers automate file exchanges with built-in processing, scheduling, and error handling. Refer to the following documentation for more information:

[File transfers](/en/managed-file-transfer/transfer-flows): Define where to pick up and deliver files.

[Source file handling](/en/managed-file-transfer/transfer-flows#add-a-source): Configure what happens to source files after a successful transfer, including archiving to a folder or deletion.

[Processing actions](/en/managed-file-transfer/transfer-flows#processing-actions): Configure processing steps such as file renaming, encryption and decryption with PGP, and compression and decompression.

[Schedule transfers](/en/managed-file-transfer/transfer-flows#schedule-transfers): Configure time-based schedules for file transfers using intervals or cron expressions.

[Error handling and retries](/en/managed-file-transfer/error-handling-and-retries): Configure automatic retry behavior, including maximum retry duration and transfer auto-stop behavior.

[Monitor transfer activity](/en/managed-file-transfer/alerts-and-monitoring#run-history-and-analytics): View run history and per-file status.

[Workato Logs](/en/managed-file-transfer/alerts-and-monitoring#workato-logs): View file transfer events across all file transfers.

[Triggers](/en/managed-file-transfer/alerts-and-monitoring#notifications): React to file transfer events, such as failed or successful transfer runs, using MFTOps recipe triggers.

## File servers

File servers provide managed SFTP and FTP(s) endpoints for secure file exchange with partners and systems. Refer to the following documentation for more information:

[Workato SFTP server](/en/managed-file-transfer/file-servers#sftp-server): Connect to encrypted file transfer endpoints at `sftp.workato.com`. You can create accounts, set folder permissions, and configure authentication with SSH keys or passwords.

[Workato FTP(s) server](/en/managed-file-transfer/file-servers#ftps-server): Connect to systems that require FTP-based file transfer.

[Monitor server activity](/en/managed-file-transfer/file-servers#server-logs): Track connection attempts, authentication events, file operations, and user activity.

> **FEATURE AVAILABILITY**
> 
> Contact your Customer Success Manager for information about access to Workato MFT.

---
