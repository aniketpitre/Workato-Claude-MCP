---
url: 'https://docs.workato.com/en/connectors/onedrive/download-file-action.md'
description: >-
  The Download file or folder action in the OneDrive connector downloads the
  contents of a file from Microsoft OneDrive for use in later recipe steps.
---

# OneDrive - Download file or folder action (file)

The **Download file or folder** action downloads the contents of a file in Microsoft OneDrive. You can use the downloaded file contents in subsequent recipe steps to upload the file to another app.

There is no fixed file size limit. The maximum size depends on whether the download finishes within the [job timeout limit](/en/recipes/jobs#job-errors).

Downloading a folder results in an error. To download a file from a shared folder, enter the folder ID in the **Drive ID** field. You can find this field in the optional input section.

## Input

| Input fields | Description |
| --- | --- |
| Drive ID | Provide the drive ID from which you plan to download the file. The **Drive ID** appears in the CID parameter of the OneDrive URL. For example, in `https://onedrive.live.com/?id=244DDFC44A57%21103&cid=24C9A8FC44A57` `24C9A8FC44A57` is the drive ID. |
| File ID | Provide the file ID. For example, `01G65C3RKY7QJD67NCMVAYKVFGW3KBGK75`. |
| Chunk size | Configure the chunk size to optimize throughput. A larger value increases throughput but may exceed API quotas. The value entered in this field is multiplied by `320`KB. The default is `5` (`1600`KB). |

## Output

| Output fields | Description |
| --- | --- |
| File content | The content of the downloaded file. |
| File size | The size of the downloaded file in bytes. |
| File name | The name of the downloaded file. |
| File path | The path of the downloaded file. |

---
