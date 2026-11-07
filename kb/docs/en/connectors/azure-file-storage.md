---
url: 'https://docs.workato.com/en/connectors/azure-file-storage.md'
description: >-
  The Azure File Storage connector lets you automate file management on cloud
  file shares: get file contents and upsert or delete files.
---

# Azure File Storage

[Azure File Storage](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction) is a fully managed cloud storage offered by Microsoft Azure for managing structured data and shared access.

## Prerequisites

Ensure you have completed the following tasks before you connect to Azure File Storage in Workato:

- [Create a storage account](#creating-storage-account)
- [Create a file share](#creating-file-share)
- [Create a Shared Access Signature (SAS) token](#creating-sas-token)

### Create a storage account

Complete the following steps to create a storage account in Azure:

1. Sign in to the [Azure portal](https://portal.azure.com).
   
2. Go to **Storage accounts** and click **Create**.
   
3. Select the appropriate **Subscription** and **Resource group** from the drop-down menu.
   
4. Enter a **Storage account name**.
   
5. Review the **Region**, **Performance**, and **Redundancy** values. Verify these settings and make changes if necessary.
   
6. Click **Review + Create**.
   
7. Click **Create**.
   

> **ADVANCED SETTINGS**
> 
> You can modify the advanced data protection, networking, and encryption settings.

### Create a file share

Complete the following steps to create a file share in your storage account.

1. Open the storage account you created.
   
2. Go to **Data storage > File shares**.
   
3. Click **\+ File share**.
   
4. Enter a **Name** for the file share.
   
5. Review other settings and make changes if necessary.
   
6. Click **Review + Create**.
   
7. Click **Create**.
   

### Create a shared access secret token

Complete the following steps to generate a shared access secret (SAS) token:

1. Go to **Storage browser > File shares** in your storage account.
   
2. Right-click your file share and select **Generate SAS**.
   
3. Select a **Signing key** and **Stored access policy** from the drop-down menu.
   
4. Go to the **Permissions** field and select the **Read**, **Write**, **List**, **Create**, and **Delete** permissions.
   
5. Set the **Start time** and **Expiry time** for the token.
   
6. Go to the **Allowed protocols** section and select **HTTPS only**.
   
7. Click **Create SAS token and URL**.
   
8. Copy the **SAS token** and store it securely.
   

## Connect to Azure File Storage

Complete the following steps to connect Workato to Azure File Storage:

1. Sign in to your Workato account and go to the project where you plan to add your Azure File Storage connection.
   
2. Click **Create > Connection** or press C twice.
   
3. Search for and select **Azure File Storage** as your connection on the **New Connection** page.
   
4. Provide a unique name for your connection in the **Connection name** field.
   
   ![Azure File Storage Connection](/assets/azure-file-storage-connection.iylmhiVQ.png)_Azure File Storage Connection_
   
5. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
6. Enter the **Storage account name**, **File share name**, and **SAS token**.
   
7. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/create-directory-action.md
description: >-
  The Create directory action creates a new directory in Azure File Storage
  under a specified share or parent directory.
---

# Azure File Storage - Create directory action

The **Create directory** action creates a new directory in Azure File Storage under a specified share or parent directory. The parent directory must already exist, and you can't create a directory hierarchy in a single action.

## Input

| Input field | Description |
| --- | --- |
| Directory path | Enter the path to the directory you plan to create. For example, `hrdata/reports/2025`. The parent directory must already exist. |
| Creation time | Enter the UTC creation time for the directory. Leave empty to use the current time. |

## Output

| Output field | Description |
| --- | --- |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including ETag, last modified, file creation time, last write time, permission key, attributes, file ID, parent ID, and request ID. |

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/delete-directory-action.md
description: >-
  The Delete directory action deletes an empty directory from Azure File
  Storage.
---

# Azure File Storage - Delete directory action

The **Delete directory** action deletes an empty directory from Azure File Storage. The directory must be empty before you can delete it.

## Input

| Input field | Description |
| --- | --- |
| Directory path | Enter the path to the directory you plan to delete. For example, `hrdata/reports/2025`. The directory must be empty. |
| Headers | Enter HTTP request headers to customize client request tracking and trailing dot behavior. |

## Output

| Output field | Description |
| --- | --- |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including content length, server, request ID, version, and date. |

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/delete-file-action.md
description: The Delete file action deletes an existing file from Azure File Storage.
---

# Azure File Storage - Delete file action

The **Delete file** action deletes an existing file from Azure File Storage.

## Input

| Input field | Description |
| --- | --- |
| File path | Enter the path to the file in the share, including the file name. For example, `hrdata/test.csv`. |
| Timeout | Enter the timeout in seconds to wait for the server to complete the operation. |
| Headers | Enter HTTP request headers to customize lease validation, request tracking, and trailing dot behavior. |

## Output

| Output field | Description |
| --- | --- |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including content length, server, request ID, version, and date. |

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/get-file-contents-action.md
description: >-
  The Get file contents action enables you to download the contents of an
  existing file from Azure File Storage.
---

# Azure File Storage - Get file contents action

The **Get file contents** action enables you to download the contents of an existing file from Azure File Storage.

## Input

| Input field | Description |
| --- | --- |
| File path | Enter the path to the file in the share, including the file name. For example, `hrdata/test.csv`. |
| Timeout | Specify the timeout in seconds to wait for the server to complete the operation. |
| Headers | Specify HTTP request headers to customize range, content integrity checks, lease validation, request tracking, and trailing dot behavior. |

## Output

| Output field | Description |
| --- | --- |
| File contents | Contents of the file. |
| Response headers | HTTP response headers including cache control, content length, content type, last modified, ETag, and request ID. |

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/rename-directory-action.md
description: >-
  The Rename directory action renames an existing directory within the same file
  share in Azure File Storage.
---

# Azure File Storage - Rename directory action

The **Rename directory** action renames an existing directory within the same file share in Azure File Storage. The source directory must exist, and the destination directory must not already exist unless you enable **Replace if exists**.

## Input

| Input field | Description |
| --- | --- |
| Source path | Enter the path of the existing directory to rename. For example, `hrdata/old_reports`. |
| Destination path | Enter the new path for the directory. For example, `hrdata/new_reports`. The destination must not already exist unless **Replace if exists** is enabled. |
| Replace if exists | Enable to overwrite the existing destination. |
| Ignore read-only | Enable to rename only if the destination has the read-only attribute. Requires **Replace if exists** to also be true. |
| Metadata | Specify key-value metadata pairs to set on the renamed directory. Each call replaces all existing metadata. Keys must follow C# identifier naming rules. |
| Headers | Specify HTTP request headers to customize file permissions, attributes, timestamps, lease validation, client request tracking, and trailing dot behavior. |

## Output

| Output field | Description |
| --- | --- |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including ETag, last modified, file creation time, last write time, permission key, attributes, file ID, parent ID, and request ID. |

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/search-files-and-directories-action.md
description: >-
  The Search files and directories action lists the files and directories under
  a directory path in Azure File Storage.
---

# Azure File Storage - Search files and directories action

The **Search files and directories** action lists the files and directories under a directory path in Azure File Storage. You can filter results by name prefix and page through large listings using the returned next page value.

## Input

| Input field | Description |
| --- | --- |
| Directory path | Enter the path to the directory you plan to list. For example, `hrdata/reports`. Leave empty to list the root of the file share. |
| Prefix | Enter a prefix the search to limit files and directories whose names begin with the specified prefix. |
| Page size | Enter the maximum number of files or directories to return. Default and maximum is `5000`. |

## Output

| Output field | Description |
| --- | --- |
| Entries | List of files and directories found under the directory path, including type, name, file ID, content length, timestamps, ETag, attributes, and permission key for each entry. |
| Directory ID | Unique identifier of the searched directory. |
| Next page | Value to use in the **Page** input field to retrieve the next page of results. |

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/upsert-file-action.md
description: >-
  The upsert file action enables you to create a new file or update an existing
  one with the specified content.
---

# Azure File Storage - Upsert file action

The **Upsert file** action creates a new file or updates an existing file with content you specify in Azure File Storage. The action searches your files and replaces your file content if it finds an existing file. The action creates a new file with the content if it doesn't find an existing file. This action supports files up to **300 MB**.

## Input

| Input field | Description |
| --- | --- |
| File path | Enter the path to the file you plan to upsert. For example, `hrdata/test.csv` |
| File contents | Enter the contents you plan to write to the file. |
| Request headers (create file) | Enter HTTP request headers for the create file operation, such as content length, content type, cache control, and metadata. |
| Request headers (put range) | Select HTTP request headers for the put range operation, such as content MD5, lease ID, file last write time. |

## Output

| Output field | Description |
| --- | --- |
| Create file response | Output of the create file operation. |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including content length, last modified, ETag, and request ID. |
| Put range response | Output of the put range operation. |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including content length, content MD5, last modified, ETag, and request ID. |

---
