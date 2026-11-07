---
url: 'https://docs.workato.com/en/connectors/google_cloud_storage/list-objects.md'
description: >-
  The List objects action in the Google Cloud Storage connector lets you list
  the details of all objects within a bucket, with folder and offset filters.
---

# Google Cloud Storage - List objects action

This action will list the details of all objects within a bucket in the Google cloud storage system.

## Input

| Field | Description |
| --- | --- |
| Bucket name **Required** | The name of the bucket. |
| Folder path | List files and folders in a particular folder. If blank, it will list all objects in the selected bucket. Define the full path, for example `folder_1/subfolder_1`. |
| Delimiter | Default Delimiter is set to “/”. If you have a customized delimiter, please add it here. |
| Start offset | Filter results to objects at or after startOffset. If endOffset is also set, the objects listed have names between startOffset (inclusive) and endOffset (exclusive). |
| End offset | Filter results to objects before endOffset. If startOffset is also set, the objects listed have names between startOffset (inclusive) and endOffset (exclusive). |
| Projection | Set of properties to return. Defaults to No ACL. |
| Max results | Maximum results to be returned from API. Default value and maximum allowed value is 200 |
| Page token | Token to specify the next page in a query. This can be found from the output of an earlier List buckets action. If the page token is null, there are no more pages. |
| Versions | If ‘Yes’, lists all versions of an object as distinct results in order of increasing generation number. Set as ‘No’ by default. |

## Output

Object specific output fields will be dynamically rendered base on the objects you select.

---
