---
url: 'https://docs.workato.com/en/features/workato-filestorage.md'
description: >-
  Workato FileStorage lets you create, store, append to, and retrieve files
  within Workato recipes, and organize them into directories.
---

# Workato FileStorage

Workato FileStorage helps you store and make use of files within Workato. With Workato FileStorage, you can now do the following file operations with ease, all within Workato:

- Create and store data created in the recipes as files
- Get contents of a stored file and use the content in Workato recipes
- Append more content to an existing file
- Create directories to classify and store groups of files

You can use Workato FileStorage to effectively store files that must be processed in Workato recipes, and delete the files after the job completes successfully.

> **FEATURE AVAILABILITY**
> 
> Workato FileStorage is available on specific pricing plans. Refer to your pricing plan and contract to learn more.

* * *

## Usage inspiration

Using Workato FileStorage, you can perform the following tasks:

- Receive any file from any connector, and store it in Workato FileStorage.
- Receive data as a bulk CSV stream from Salesforce actions, and store it as a CSV file in Workato FileStorage.
- Get lead data as JSON in smaller chunks from Hubspot, convert to CSV format, and append it to an existing file in Workato FileStorage, before pushing it (in bulk) to a downstream app.
- Persist and fetch static files that are frequently required in the recipes: product information, price information, zipcode data, standard codes, and so on.
- Perform transformations on CSV data existing within Workato FileStorage by pairing it with the SQL transformation utility connector.

* * *

> **HOW TO GET ACCESS TO WORKATO FILESTORAGE**
> 
> You can access Workato FileStorage by using the Workato FileStorage connector or FileStorage UI, both of which are currently available in limited access. Reach out to your Customer Success representative to enable these features.

* * *

## Setup

Workato FileStorage supports both workspace-level and tenant-level access. There are two ways to access FileStorage system:

- [Through the FileStorage connector](#connector-access)
- [Through the FileStorage UI](#ui-access)

### FileStorage connector

The Workato FileStorage [connector](/en/features/filestorage/filestorage-connector) does not restrict access based on role. All users in a workspace can access all FileStorage files and directories in the workspace using the connector.

There are no separate setup requirements in the connector, and you can use it directly to perform file-related operations.

![Workato FileStorage connector](/assets/connector-setup.4ATnghKN.png)_Workato FileStorage connector_

### FileStorage UI

The Workato FileStorage [UI](/en/features/filestorage/filestorage-console) restricts access based on role. See [Role-based access control in the FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

You can access Workato FileStorage through the Workato FileStorage connector in the recipe editor, or through the FileStorage UI in **Tools > FileStorage**.

The FileStorage UI allows you to browse the FileStorage system and perform certain file-related operations. No separate setup is required.

![Workato FileStorage UI](/assets/filestorage-ui-nav.CjsbBXg9.png)_The Workato FileStorage UI_

* * *

## FileStorage quotas

Workato FileStorage has the following quotas:

| Description | Quota |
| --- | --- |
| Maximum file size | 10 GB |
| Maximum storage capacity available to a workspace's environment for direct customers | 100 GB |
| Maximum storage capacity available to an environment for Embedded customers | 100 GB |

* * *

## Encryption

Workato FileStorage is built on an encrypted file storage system. In addition to this, each account's data is encrypted using an account specific key that rotates every month.

Additionally, Workato FileStorage is also included as part of Workato's [BYOK](/en/security/data-protection/encryption-key-management/#encryption-key-management) initiative.

* * *

## Data retention

Workato does not delete files available in FileStorage automatically and they are stored as long as the you wish to persist them in the system. If you want to delete this data you must do so manually using the FileStorage delete action.

* * *

## Storing sensitive data

Caution should be taken when storing sensitive data in Workato FileStorage, including personal data that would fall under privacy laws and regulations, financial data, and/or healthcare data. While Workato protects such data at rest and in transit through encryption, customers are responsible for assessing whether storage of such data is appropriate and allowable given their own policies and legal/regulatory requirements, as well as applying appropriate access controls.

* * *

## Things to know

- Streaming - A mechanism to transfer large files between two different entities by moving the files in smaller parts called chunks. This allows us to transfer large files without worrying about limitations in sending or receiving ends. All file adapters and bulk actions in Workato support streaming today and are capable of transferring large volumes of data. See [File Streaming](/en/features/file-streaming#file-streaming) for more information.

---
