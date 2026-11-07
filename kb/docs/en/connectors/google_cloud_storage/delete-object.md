---
url: 'https://docs.workato.com/en/connectors/google_cloud_storage/delete-object.md'
description: >-
  The Delete object action in the Google Cloud Storage connector lets you delete
  an object and its metadata from a bucket, with generation conditions.
---

# Google Cloud Storage - Delete object action

This action will delete an object from a bucket in your Google cloud storage instance. It will delete the object and its metadata in the Google Cloud Storage system. Deletions are permanent if versioning is not enabled for the bucket.

## Input

| Field | Description |
| --- | --- |
| Bucket name **Required** | The name of the bucket to be deleted. |
| Object name **Required** | The name of the object to be deleted. |
| Generation | If present, permanently deletes a specific revision of this object (as opposed to the latest version by default). |
| If generation matches | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. |
| If generation does not match | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. |
| If Meta generation matches | Makes the operation conditional on whether the object's current metageneration matches the given value. |
| If Meta generation does not match | Makes the operation conditional on whether the object's current metageneration does not match the given value. |

## Output

| Field | Description |
| --- | --- |
| Successfully deleted | Whether the object was deleted. |

---
