---
url: 'https://docs.workato.com/en/connectors/bynder/action-upload-asset.md'
description: >-
  The Upload asset action in the Bynder connector uploads file contents as a new
  asset or a new version of an existing asset by its ID.
---

# Bynder - Upload asset action

Upload an asset to Bynder by providing contents of the file. Input asset ID to save the new file to an existing asset, or leave it empty to upload the file as a new asset. When you are using this action, make sure your recipe is running for the upload to complete.

## Input

| Field name | Description |
| --- | --- |
| File name | Provide the name of the file with extension. For example, image.png |
| File contents | Contents of the file to upload. File contents can be obtained by using Download asset action, or from other actions/trigger. |
| File size | File size can be found in the output of other triggers/actions. You can also enter the value in bytes. |
| Brand | Brand to which you want to upload the asset to. |
| Asset ID | Asset Id to which you want to save the new file. When new files are uploaded to existing asset Id, new versions of the file are created. |
| Time limit | The time limit for how long the query can run in minutes. For example, 30. Default: 30 minutes. |
| Name | Name of the asset. |
| Description | Description of the asset. |
| Tags | Comma-separated list of tags of the asset. |
| Categories | Comma-separated category IDs of the asset. |
| Audit | Choose Yes if the asset should be sent to the waiting room. Otherwise, choose No. Note that in order to be able to chose whether or not the asset will be uploaded to the waiting room you'll need both the MEDIAUPLOAD and MEDIAUPLOADFORAPPROVAL security role. |

  

## Output

| Field name | Description |
| --- | --- |
| Media Id | Id of media uploaded |
| Media Items | Paths to the media uploaded |

---
