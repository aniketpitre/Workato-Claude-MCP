---
url: 'https://docs.workato.com/en/connectors/oracle-object-storage.md'
description: >-
  The Oracle Object Storage connector lets you upload and download objects,
  including streams, and create, get, search, and delete stored records.
---

# Oracle Object Storage

[Oracle Object Storage](https://www.oracle.com/cloud/storage/object-storage/) is a cloud-based object storage service that provides a scalable, secure, and cost-effective way to store and access data.

## Prerequisites

Before you can establish an Oracle Object Storage connection in Workato, you must configure authentication and access permissions in Oracle Cloud. Complete the following prerequisite steps:

1. [Create an Oracle Identity Cloud group](#oracle-cloud-identity-group)
2. [Create an Oracle Identity Cloud policy](#oracle-cloud-identity-policy)
3. [Create an API key](#creating-an-api-key)

### Create an Oracle Identity Cloud group

Complete the following steps to create a user group:

1. Sign in to your **Oracle Cloud** and go to **Identity and Security**.
   
2. Go to **Domains**, then select **OracleIdentityCloudService** or any other domain of your choice.
   
3. Go to **User management > Groups** and click **Create group**.
   
4. Enter a name for the group, such as **Oracle Object Storage Group**.
   
5. Select the user to add to this new group. This is the user who will be accessing Oracle Object Storage using Workato.
   
6. Click **Create**.
   

### Create an Oracle Identity Cloud policy

Complete the following steps to create a policy that grants access permissions to Oracle Object Storage:

1. In **Identity and Security**, go to **Policies**.
   
2. Click **Create Policy**.
   
3. Enter a **Name** and **Description** for your policy.
   
4. Under **Policy builder**, select **Show manual editor**.
   
5. Enter the following policy: `Allow group '<DOMAIN>'/'<GROUP>' to manage object-family in tenancy`
   
   For example: `Allow group 'OracleIdentityCloudService'/'Oracle Object Storage Group' to manage object-family in tenancy`
   
6. Click **Create**.
   

### Create an API key

Complete the following steps to generate an API key for authentication:

1. In **Identity and Security**, go to **My profile**.
   
2. Go to **Token and keys**, then click **Add API key**.
   
3. Retrieve your RSA key pair:
   
   - Download the auto-generated key pair (provides private key in PEM format), or
   - Upload your own public key or paste its contents
   
   Store the private key securely.
   
4. Click **Add**.
   
5. Retrieve details for your API key, including the **User OCID**, **Tenant OCID**, **Fingerprint**, and **Region**. Save these details in a safe location.
   

## How to connect to Oracle Object Storage

Complete the following steps to establish an Oracle Object Storage connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Oracle Object Storage** as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
   ![Connect to Oracle Object Storage](/assets/oracle-object-storage-connection.CoAHg1wL.png)_Connect to Oracle Object Storage_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to save your connection.
   
5. Fill in the required fields:
   
   - **Region**
   - **Tenancy OCID**
   - **User OCID**
   - **Fingerprint**
   - **Private key** (paste in PEM format)
6. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/create-record-action.md
description: The Create record action creates a new record in Oracle Object Storage.
---

# Oracle Object Storage - Create record action

The **Create record** action creates a new record in Oracle Object Storage.

## Input

| Input field | Description |
| --- | --- |
| Record type | Specify the record type to create. Fields load dynamically based on the selected record type. |

For example, if the selected record type is **Bucket**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Bucket name | Enter the name of the new bucket. |
| Auto tiering | Choose between standard and infrequent access modes for your objects. |
| Compartment ID | Enter the compartment's Oracle Cloud ID (OCID) to create the bucket. |
| Defined tags | Define a list of defined tags for the bucket. |
| Freeform tags | Define a list of freeform tags for the bucket. |
| KMS key ID | Enter the Oracle Cloud ID (OCID) of the master key used to generate or encrypt data keys via the Key Management service. |
| Metadata | Define key-value pairs of user-defined metadata. |
| Object events enabled | Select whether to allow events for objects inside the bucket. |
| Public access type | Choose the level of public access to the bucket. |
| Storage tier | Choose the storage tier to use for the bucket. |
| Versioning | Select whether to enable versioning for the bucket. |
| Headers | Specify custom request headers to send with the request. Includes client request ID. |

## Output

The output fields are determined by the record type selected in the input. Map the relevant datapill from the datatree to subsequent steps. For example, selecting **Bucket** as the record type returns the following output fields:

| Output field | Description |
| --- | --- |
| Headers | Response headers. |
| Approximate count | The approximate number of objects in the bucket. |
| Approximate size | The approximate total size in bytes of all objects in the bucket. |
| Approximate size multipart uploads | The approximate size of multipart uploads in the bucket. |
| Auto tiering | The auto tiering status on the bucket. |
| Compartment ID | The compartment ID is the one for which the bucket is authorized. |
| Created by | The Oracle Cloud ID (OCID) of the bucket user created. |
| Defined tags | Defined tags for this resource. |
| Entity tag | The entity tag (ETag) for the bucket. |
| Freeform tags | Free-form tags for this resource. |
| ID | The Oracle Cloud ID (OCID) of the bucket. |
| Is read only | Whether or not this bucket is read-only. |
| KMS Key ID | The Oracle Cloud ID (OCID) of a master encryption key is used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key. |
| Metadata | Arbitrary string keys and values for user-defined metadata. |
| Bucket name | The name of the bucket. |
| Namespace | The Object Storage namespace is where the bucket resides. |
| Object events enabled | Whether or not events are emitted for object state changes in this bucket. |
| Object level audit mode | Audit mode of the objects in this bucket. |
| Object lifecycle policy ETag | The entity tag (ETag) for the live object lifecycle policy on the bucket. |
| Public access type | The type of public access enabled on this bucket. |
| Replication enabled | Whether or not this bucket is a replication source. |
| Storage tier | The storage tier type assigned to the bucket. |
| Time created | The date and time the bucket was created, as described in RFC 2616. |
| Versioning | The versioning status on the bucket. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/delete-record-action.md
description: The Delete record action deletes a record from Oracle Object Storage.
---

# Oracle Object Storage - Delete record action

The **Delete record** action deletes a record from Oracle Object Storage.

## Input

| Input field | Description |
| --- | --- |
| Record type | Specify the record type to delete. Fields load dynamically based on the selected record type. |

For example, if the selected record type is **Bucket**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Bucket name | Enter the name of the bucket to delete. |
| Headers | Specify custom request headers to send with the request. Includes client request ID and if match. |

## Output

The output fields are determined by the record type selected in the input. Map the relevant datapill from the datatree to subsequent steps. For example, selecting **Bucket** as the record type returns the following output fields:

| Output field | Description |
| --- | --- |
| Headers | Response headers. Includes client request ID and request ID. |
| Success | Whether the delete operation was successful or not. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/download-object-action.md
description: The Download object action downloads an object from Oracle Object Storage.
---

# Oracle Object Storage - Download object action

The **Download object** action downloads an object from Oracle Object Storage. This action is recommended for small files up to 100 MiB. For larger files, use the [Download object (stream) action](/en/connectors/oracle-object-storage/download-object-stream-action).

## Input

| Input field | Description |
| --- | --- |
| Bucket name | Select or enter the name of the bucket to download from. |
| Object name | Select or enter the name of the object to download. |
| Version ID | Enter a version ID to specify a version of the object. |
| HTTP response content disposition | Specify the value of content disposition. |
| HTTP response cache control | Specify the value of cache control to override it in the response headers. |
| HTTP response content type | Specify the value of content type to override it in the response headers. |
| HTTP response content language | Specify the value of content language to override it in the response headers. |
| HTTP response content encoding | Specify the value of content encoding to override it in the response headers. |
| HTTP response expires | Specify the value of expires to override it in the response headers. |
| Headers | Specify custom request headers to send with the request. Includes if, if none match, client request ID, SSE customer algorithm, SSE customer key, SSE customer key SHA256. |

## Output

| Output field | Description |
| --- | --- |
| Headers | Response headers. Includes entity tag (ETag), archival state, cache control, content disposition, content encoding, content language, content length, content MD5, content range, content type, expires, last modified, client request ID, multirt MD5, request ID, storage tier, time of archival and version ID. |
| Contents | File contents. |
| Name | Name of the object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/download-object-stream-action.md
description: >-
  The Download object (stream) action downloads an object from Oracle Object
  Storage.
---

# Oracle Object Storage - Download object (stream) action

The **Download object (stream)** action downloads an object from Oracle Object Storage. Subsequent recipe steps can use the file contents to upload the file into another app.

There is no fixed limit on file size. The maximum file size depends on whether the download can finish within the [job timeout limit](/en/recipes/jobs#timeouts).

## Input

| Input field | Description |
| --- | --- |
| Bucket name | Select or enter the name of the bucket to download from. |
| Object name | Select or enter the name of the object to download. |
| Version ID | Enter a version ID to specify a version of the object. |
| HTTP response content disposition | Specify the value of content disposition. |
| HTTP response cache control | Specify the value of cache control to override it in the response headers. |
| HTTP response content type | Specify the value of content type to override it in the response headers. |
| HTTP response content language | Specify the value of content language to override it in the response headers. |
| HTTP response content encoding | Specify the value of content encoding to override it in the response headers. |
| HTTP response expires | Specify the value of expires to override it in the response headers. |
| Headers | Specify custom request headers to send with the request. Includes if, if none match, client request ID, SSE customer algorithm, SSE customer key, SSE customer key SHA256. |

## Output

| Output field | Description |
| --- | --- |
| Headers | Response headers. Includes entity tag (ETag), archival state, cache control, content disposition, content encoding, content language, content length, content MD5, content range, content type, expires, last modified, client request ID, multirt MD5, request ID, storage tier, time of archival and version ID. |
| Contents | File contents. |
| Name | Name of the object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/get-record-action.md
description: >-
  The Get record action retrieves details about a record from Oracle Object
  Storage.
---

# Oracle Object Storage - Get record action

The **Get record** action retrieves details about a record from Oracle Object Storage.

## Input

| Input field | Description |
| --- | --- |
| Record type | Specify the record type to get. Fields load dynamically based on the selected record type. |

For example, if the selected record type is **Bucket**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Bucket name | Enter the name of the bucket. |
| Headers | Specify custom request headers to send with the request. Includes if match, if none match and client request ID. |
| Fields | Select additional fields to return. |

## Output

The output fields are determined by the record type selected in the input. Map the relevant datapill from the datatree to subsequent steps. For example, selecting **Bucket** as the record type returns the following output fields:

| Output field | Description |
| --- | --- |
| Headers | Response headers. Includes entity tag (ETag), client request ID, and request ID. |
| Approximate count | The approximate number of objects in the bucket. |
| Approximate size | The approximate total size in bytes of all objects in the bucket. |
| Approximate size multipart uploads | The approximate size of multipart uploads in the bucket. |
| Auto tiering | The auto tiering status on the bucket. |
| Compartment ID | The compartment ID is the one for which the bucket is authorized. |
| Created by | The Oracle Cloud ID (OCID) of the bucket user created. |
| Defined tags | Defined tags for this resource. |
| Entity tag | The entity tag (ETag) for the bucket. |
| Freeform tags | Free-form tags for this resource. |
| ID | The Oracle Cloud ID (OCID) of the bucket. |
| Is read only | Whether or not this bucket is read-only. |
| KMS Key ID | The Oracle Cloud ID (OCID) of a master encryption key is used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key. |
| Metadata | Arbitrary string keys and values for user-defined metadata. |
| Bucket name | The name of the bucket. |
| Namespace | The Object Storage namespace is where the bucket resides. |
| Object events enabled | Whether or not events are emitted for object state changes in this bucket. |
| Object level audit mode | Audit mode of the objects in this bucket. |
| Object lifecycle policy ETag | The entity tag (ETag) for the live object lifecycle policy on the bucket. |
| Public access type | The type of public access enabled on this bucket. |
| Replication enabled | Whether or not this bucket is a replication source. |
| Storage tier | The storage tier type assigned to the bucket. |
| Time created | The date and time the bucket was created, as described in RFC 2616. |
| Versioning | The versioning status on the bucket. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/search-records-action.md
description: >-
  The Search records action retrieves a list of records for an object in Oracle
  Object Storage that match your search criteria.
---

# Oracle Object Storage - Search records action

The **Search records** action retrieves a list of records for an object in Oracle Object Storage that match your search criteria.

## Input

| Input field | Description |
| --- | --- |
| Record type | Specify the record type to search. Fields load dynamically based on the selected record type. |

For example, if the selected record type is **Bucket**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Compartment ID | Enter the compartment's Oracle Cloud ID (OCID) to search buckets. |
| Limit | Specify the quota for list—the maximum number of results per page. |
| Page | Specify the page number for list pagination, which is the value of the opc-next-page response header from the previous call. |
| Headers | Specify custom request headers to send with the request. Includes client request ID. |
| Fields | Select additional fields to return. |

## Output

The output fields are determined by the record type selected in the input. Map the relevant datapill from the datatree to subsequent steps. For example, selecting **Bucket** as the record type returns the following output fields:

| Output field | Description |
| --- | --- |
| Headers | Response headers. This includes the next page, client request ID, and request ID. |
| Buckets | List of buckets which match the search criteria with the following properties. |
| Compartment ID | The compartment ID is the one for which the bucket is authorized. |
| Created by | The Oracle Cloud ID (OCID) of the bucket user created. |
| Defined tags | Defined tags for this resource. |
| Entity tag | The entity tag (ETag) for the bucket. |
| Freeform tags | Free-form tags for this resource. |
| Bucket name | The name of the bucket. |
| Namespace | The Object Storage namespace is where the bucket resides. |
| Time created | The date and time the bucket was created, as described in RFC 2616. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/upload-object-action.md
description: The Upload object action uploads an object to Oracle Object Storage.
---

# Oracle Object Storage - Upload object action

The **Upload object** action uploads an object to Oracle Object Storage. This action is recommended for small files up to 100 MiB. For larger files, use the [Upload object (stream) action](/en/connectors/oracle-object-storage/upload-object-stream-action).

## Input

| Input field | Description |
| --- | --- |
| Bucket name | Select or enter the name of the bucket. |
| Object name | Select or enter the name of the object to upload. |
| Contents | Specify a binary string of the object to upload to the object store. |
| Headers | Specify custom request headers to send with the request. Includes if match, if none match, client request ID, content length, content MD5, content type, content language, content encoding, content disposition, cache control, SSE customer algorithm, SSE customer key, SSE customer key SHA256, KMS key OCID and storage tier. |

## Output

| Output field | Description |
| --- | --- |
| Headers | Response headers. This includes the entity tag (ETag), last modified, client request ID, multipart MD5, request ID and version ID. |
| Status | Whether the file was uploaded successfully or not. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/upload-object-stream-action.md
description: The Upload object (stream) action uploads an object to Oracle Object Storage.
---

# Oracle Object Storage - Upload object (stream) action

The **Upload object (stream)** action uploads an object to Oracle Object Storage. The minimum file size is 64 MiB.

There is no fixed limit on maximum file size. The maximum file size depends on whether the upload can finish within the [job timeout limit](/en/recipes/jobs#timeouts).

## Input

| Input field | Description |
| --- | --- |
| Bucket name | Enter the name of the bucket to upload to. |
| Object name | Enter the name of the object to upload. |
| Contents | Specify a binary string of the object to upload to the object store. |

## Output

| Output field | Description |
| --- | --- |
| Success | Whether the file was uploaded successfully or not. |
| Object name | Name of the object. |
| Upload ID | ID of the upload operation. |
| Parts uploaded | Number of parts uploaded to complete the multipart file upload. |
| Total bytes uploaded | Size of the uploaded files in bytes. |

---
