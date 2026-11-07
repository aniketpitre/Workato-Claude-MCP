---
url: 'https://docs.workato.com/en/connectors/bynder/action-download-asset.md'
description: >-
  The Download asset action in the Bynder connector downloads the contents of an
  asset so you can stream the file into other applications in your recipe.
---

# Bynder - Download asset action

Download contents of an asset. File contents can be used in subsequent steps of the recipe to upload the file into other applications.

In the example below, we use Content datapill from Bynder's Download asset action and provide that to Box's Upload file action.

![Upload file from Bynder to Box](/assets/bynder_connection_3.CrbTtqJS.png)

## Input

| Field name | Description |
| --- | --- |
| Asset ID **Required** | Asset ID to retrieve. ID can be found at the end of the URL. |
| Version | Provide version if you wish to download the old version of an asset.You can provide either version of a file or a type of file to download. Leave blank to download the latest version of the asset. |
| Type of file to download | For image file types, Bynder generates multiple additional files such as `thumbnail`, `small`, `online` etc of various file sizes. Note that when multiple additional files are available only the download url of the latest one will be returned. |
| Chunk size | File contents will be [streamed](/en/features/file-streaming) in chunks of this size. Enter the size with the unit, Eg. 50KB. Valid units are 'B', 'KB', 'MB'. Default chunk size is 10MB. Minimum is 32KB and maximum is 10MB. Use this when you want to optimize throughput. Bigger chunk size will increase throughput, but may exceed API quotas. |

  

## Output

| Field name | Description |
| --- | --- |
| Content | Binary contents of the file. When you upload this file contents to other applications, [streaming](/en/features/file-streaming) will be used. |

---
