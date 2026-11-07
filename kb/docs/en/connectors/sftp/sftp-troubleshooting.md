---
url: 'https://docs.workato.com/en/connectors/sftp/sftp-troubleshooting.md'
description: >-
  Troubleshoot common SFTP connection and runtime errors in Workato, including
  the password must not be longer than 1024 bytes connection failure.
---

# SFTP troubleshooting guide

Use this guide to troubleshoot issues when you set up or run recipes with the SFTP connector.

## Connection fails with “password must not be longer than 1024 bytes”

You may see the following error when you create an SFTP connection:

![SFTP connection failed error](/assets/sftp-connection-failed.DKLMInDn.png)_SFTP connection failed error_

### Why it happens

This error occurs when the **Private key passphrase** field contains a value longer than 1024 characters. In some cases, the field auto-fills incorrectly with the private key itself. The encryption library Workato uses enforces a 1024-byte quota on passphrase length, which causes the connection to fail.

### How to troubleshoot

Complete the following steps to resolve the issue:

1. Create a new SFTP connection in Workato.
   
2. Leave the **Private key passphrase** field blank if your SSH key doesn't use a passphrase. If your key uses a passphrase, enter it manually and ensure it's under 1024 characters.
   
3. Save and test the new connection.
   

## SFTP upload fails with close stream error

You may see a `closed stream` error when you run an **Upload file to SFTP server** action.

### Why it happens

This error can occur for the following reasons:

- The target SFTP server has intermittent network connectivity.
- The SFTP connection uses a small transfer buffer size.
- The connection logs lack sufficient detail for large file uploads.

### How to troubleshoot

Complete the following steps to resolve the issue:

1. Increase the transfer buffer size in your SFTP connection settings. The default and minimum transfer buffer size is 32768 bytes (32 KB), and the maximum is 327680 bytes (320 KB).
   
2. Verify that the SFTP server is stable and reachable during large file transfers.
   

## No such file error in new/updated file in directory trigger

The job may fail with the following error when you use the **New/updated file in directory** trigger:

```text
SFTP error 2 : no such file
```

### Why it happens

This error can occur for the following reasons:

- The external SFTP server removes a file after a download attempt.
- The file becomes corrupted during upload.
- Network instability interrupts file access during polling.

### How to troubleshoot

Complete the following steps to resolve the issue:

1. Ensure that your SFTP server retains files in the monitored directory until the trigger downloads them.
   
2. Confirm that uploaded files are complete and not corrupted.
   
3. Check for intermittent network issues between Workato and the SFTP host.
   

## No such file error in new/updated CSV file in directory trigger

You may see a `No such file` error when you use the **New/updated CSV file in directory** trigger. The error persists even after you restart the recipe, while other recipes that use the same directory continue to work.

### Why it happens

This error occurs when the trigger starts to download a file that the SFTP server deletes or moves during the download. The trigger continues to fail because its cursor references the deleted file.

### How to troubleshoot

Complete the following steps to resolve the issue:

1. Set **Ignore Missing Files?** to **true** in the trigger settings. This option allows the trigger to skip missing files and continue to detect new ones.
   
2. Alternatively, if the issue persists, clone the affected recipe, set **Ignore Missing Files?** to **true** in the clone, then stop the original recipe and start the cloned one.

---
