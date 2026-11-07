---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/create-user.md
description: >-
  The Create user action creates a user in Oracle Fusion Cloud using HCM Data
  Loader.
---

# Oracle Fusion Cloud - Create user action

The **Create user** action creates a user in Oracle Fusion Cloud using the HCM Data Loader process.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Web key | Provide the authentication key for Oracle WebCenter Content service. |
| IDC service | Set to `CHECKIN_UNIVERSAL` for uploading HCM Data Loader files to create users. |
| User | Optional container for user-specific metadata configuration. |
| Fields (User) | Configure user-specific metadata fields and their values as needed. |
| Result set (User) | Optional result set configuration for user data. |
| Option list (User) | Optional option list configuration for user data. |
| Document | Container for the HCM Data Loader ZIP file and its metadata. |
| Fields (Documents) | Configure document metadata as key-value pairs: **dDocTitle**: Document title; **dDocType**: Document type (usually `Document`); **dDocAuthor**: Document author (your HCM username); **dSecurityGroup**: Security group (usually `FAFusionImportExport`); **dDocAccount**: Document account (usually `hcm$/dataloader$/import$`); **dDocName**: Content ID (optional, for versioning) |
| Result set (Documents) | Optional result set configuration for document data. |
| Option list (Documents) | Optional option list configuration for document data. |
| File (Documents) | Configure the HCM Data Loader file upload: **href**: File reference, **name**: File name (usually `primaryFile`), **Contents**: Base64 encoded ZIP file content containing the user.dat file |

### User.dat file format

Create a `user.dat` file with the following structure:

```text
METADATA|User|UserName|PersonNumber|StartDate|Active|EmailAddress
MERGE|User1|1001|2025/09/03|Y|<user1@example.com>
```

Convert the `user.dat` file to a ZIP file, then encode the ZIP file as Base64 before entering it in the **File (Documents) > Contents** field.

Refer to the [Oracle Fusion Cloud documentation](https://docs.oracle.com/en/solutions/load-data-into-hcm-cloud/use-webcenter-content-generic-soap-web-service-upload-hcm-data-loader-zip-file1.html#GUID-D2C49B89-5973-4971-977B-CC5D9CBBED7E) for more information.

## Output

| Output field | Description |
| --- | --- |
| IDC service | WebCenter Content service used. |
| User | User metadata response. |
| Fields (User) | User field responses. |
| Result set (User) | User result set data. |
| Option list (User) | User option list data. |
| Document | Document metadata response. |
| Fields (Document) | Document field responses. |
| Result set (Document) | Document result set data. |
| Option list (Document) | Document option list data. |
| File (Document) | File upload response details. |
