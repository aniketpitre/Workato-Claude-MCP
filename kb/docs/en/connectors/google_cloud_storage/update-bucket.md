---
url: 'https://docs.workato.com/en/connectors/google_cloud_storage/update-bucket.md'
description: >-
  The Update bucket action in the Google Cloud Storage connector lets you update
  the settings of an existing bucket by bucket name.
---

# Google Cloud Storage - Update bucket action

This action will update an existing bucket in the Google cloud storage system.

## Input

| Field | Description |
| --- | --- |
| Bucket name **Required** | The name of the bucket to be updated. |

## Output

Object specific output fields will be dynamically rendered base on the objects you select.

---

---
url: >-
  https://docs.workato.com/en/connectors/google_cloud_storage/update-object-metadata.md
description: >-
  The Update object metadata action in the Google Cloud Storage connector lets
  you update an object's metadata and access controls within a bucket.
---

# Google Cloud Storage - Update object metadata action

This action updates an object’s metadata in your Google cloud storage instance.

For uploading object content and metadata use the [upload object action](/en/connectors/google_cloud_storage/upload-object-with-file-streaming).

## Input

| Field | Description |
| --- | --- |
| Bucket name **Required** | The name of the bucket to be updated. |
| Object name **Required** | The name of the object to be updated. |
| Pre-defined Access Controls | Select a pre-defined access control configuration. |
| Projection | Select the set of properties to return. Defaults to No ACL. |
| Generation | If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default). |
| If generation matches | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. |
| If generation does not match | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. |
| If Meta generation matches | Makes the operation conditional on whether the object's current metageneration matches the given value. |
| If Meta generation does not match | Makes the operation conditional on whether the object's current metageneration does not match the given value. |

> **Pre-defined access controls**
> 
> These are the accepted configurations:
> 
> - **authenticatedRead**: Object owner gets `OWNER` access, and allAuthenticatedUsers get `READER` access.
> - **bucketOwnerFullControl**: Object owner gets `OWNER` access, and project workspace admins get `OWNER` access.
> - **bucketOwnerRead**: Object owner gets `OWNER` access, and project workspace admins get `READER` access.
> - **private**: Object owner gets `OWNER` access.
> - **projectPrivate**: Object owner gets `OWNER` access, and project workspace members get access according to their roles.
> - **publicRead**: Object owner gets `OWNER` access, and allUsers get `READER` access.

## Output

Object specific output fields will be dynamically rendered base on the objects you select.

---

---
url: >-
  https://docs.workato.com/en/connectors/google_cloud_storage/upload-object-with-file-streaming.md
description: >-
  The Upload object with file streaming action in the Google Cloud Storage
  connector uploads an object to a bucket using parallel uploads for any file
  size.
---

# Google Cloud Storage - Upload object with file streaming action

This action uploads an object to your Google cloud storage instance. This action sets up parallel uploads for files of all sizes for faster uploads.

## Input

| Field | Description |
| --- | --- |
| Bucket name **Required** | The name of the bucket to upload to. |
| Name **Required** | The name of the object to be uploaded. |
| Object content **Required** | Content of object to be uploaded. |

## Output

| Field | Description |
| --- | --- |
| Location | The location of the streaming upload. |

---
