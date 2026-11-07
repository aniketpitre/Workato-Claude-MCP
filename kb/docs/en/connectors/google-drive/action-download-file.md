---
url: 'https://docs.workato.com/en/connectors/google-drive/action-download-file.md'
description: Downloads the content of a file in Google Drive.
---

# Google Drive - Download file action

This action downloads the content of a file in Google Drive. You can use downloaded content in subsequent steps of the recipe, such as uploading the content into other applications.

There is no fixed limit on file size. Maximum file size depends on whether the download can finish within the [job timeout limit](/en/recipes/jobs#timeouts).

Note that you can only download binary files. Attempting to download a folder or Google Docs file results in an error. You must use a custom export API action to export binary files to `csv` or `xlsx` file formats.

![Google Drive Download file action](/assets/google-drive-download-file.hVhneBms.png) _Google Drive Download file action_

## Input

| Input field | Description |
| --- | --- |
| File | Select a file or enter the ID of the file. You can find the file ID in the output of other Google Drive triggers or actions, or in the file's shareable link. To get the shareable link, right-click the file in Google Drive and select **Share > Copy link**. For example, if the shareable link is `https://drive.google.com/file/d/123nyR2IjW_Rq84d3qEYRoq1/view`, the file ID is `123nyR2IjW_Rq84d3qEYRoq1`. |
| Chunk size (KB) | Configure this to optimize throughput. Larger chunk size increases throughput, but may hit API quotas. Defaults to 1024 KB. Refer to [File streaming](/en/features/file-streaming) for more details. |
| Encoding of the file content | Specify the file encoding to set it explicitly. By default, encoding is set to `UTF-8`. [Learn more](https://en.wikibooks.org/wiki/Ruby_Programming/Encoding) about supported encodings. |

## Output

| Output field | Description |
| --- | --- |
| File contents | The full content of the file as a [streaming object](/en/features/file-streaming). You can use file content in the **Upload file** actions of other connectors, such as Box, Dropbox, Amazon S3, and more to upload the file content into those applications. |
| Size | Size of the file in bytes. |

---
