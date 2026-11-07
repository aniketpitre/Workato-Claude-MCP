---
url: 'https://docs.workato.com/en/features/handling-binary-files.md'
description: >-
  Learn how to move binary files across apps in Workato recipes using a public
  URL or by downloading and uploading file content.
---

# Handling binary files

Binary files are files that are in a non-text format. Binary files are not written in human-readable language and use more complex storage configurations than text files. Using Workato, you can sync such files across your business systems with recipes.

Workato provides two options for moving files across apps. Both options are applicable for text and binary files.

1. [Moving files using a public URL](#moving-files-using-a-public-url):
   
   Obtain a public URL for the specified file and pass it to the destination app. This moves the file directly to the destination app without moving the file through Workato. The URL must be publicly accessible for the duration of the job.
   
2. [Moving files using file content](#moving-files-using-file-content):
   
   Download the file content to Workato and then upload the content to the destination app. Using this option, you can read and perform transformations on the file data.
   
   We recommend moving very large files using a public URL, because moving large files using file content can slow the job's processing speed.
   

## Moving files using a public URL

To move files using a public URL:

1. Find and save the public URL of the file you plan to move.
   
2. Pass the file's public URL to the destination app.
   

The following example demonstrates how to move a file from Dropbox to Box. Refer to the [sample recipe](https://www.workato.com/recipes/485735) for a working example.

![Moves files from Dropbox to Box via public URLs](/assets/file-url-recipe.rVRDqWA7.png)_Moves files from Dropbox to Box via public URLs_

The recipe retrieves the public URL from the **New file** trigger. Next, it checks if the file already exists in Box. If the file does not exist in Box, the recipe passes the URL to the **Upload file via URL** action.

> **GENERATE A PUBLIC URL**
> 
> When configuring the **New file** trigger, remember to mark `Yes` for the **Obtain a direct URL to file** field to generate a public URL.

## Moving files using file content

To move files using file content:

1. Download the file content from the file you plan to move.
   
2. Upload the file to the target system.
   

You can use the [File tools by Workato](/en/features/file-tools-by-workato) connector to move files using file content. This native application allows you to perform a variety of file-related actions.

The following example demonstrates how to move an attachment from Gmail to Box. Refer to the [sample recipe](https://www.workato.com/recipes/485773) for a working example.

![Download attachments from Gmail and upload to Box](/assets/download-file-recipe.D37fjKAf.png)_Download attachments from Gmail and upload to Box_

The Gmail **New email** trigger output can contain a list of attachments. This recipe checks if the email has attachments. If the email has attachments, the recipe runs a **Download attachment** action. Then, the recipe loads the file to Box through the **Upload file using file contents** action.

The `For each` recipe step (Step 2) is an action that repeats the download and upload steps for every attachment in the email.

> **USING FILE CONTENT**
> 
> The preceding example used file content to move the Gmail attachment because Gmail does not provide public URLs for attachments. [Moving files using public URLs](#moving-files-using-a-public-url) is more recipe efficient if the file has a public URL.

## Download file content from public URL

If the source app provides only a public URL and the destination app requires file content, use the [Get file from URL](/en/features/get-file-from-url) action from [File tools by Workato](/en/features/file-tools-by-workato). This action retrieves the file content from the public URL.

In the following example, the recipe uploads and associates new files created in a shared Box folder to a Salesforce account.

![Example recipe - using tools to download file](/assets/utilities-download-file.Dmv6gz7e.png)_Recipe that uses Tools to download file content. [Example recipe](https://www.workato.com/recipes/1006009-new-file-in-box-will-download-file-from-url#recipe)._

The recipe uses the Box file's public URL to download the file content. Then, the file content is then uploaded into Salesforce as a new attachment associated to a specific Salesforce account. In this case, the Salesforce account ID is hardcoded within the recipe.

![Upload file to Salesforce](/assets/upload-file-to-salesforce.C6BE69iC.gif)_Download file using the Box URL, then upload file content to Salesforce. [Example recipe](https://www.workato.com/recipes/1006009-new-file-in-box-will-download-file-from-url#recipe)._

## Base64 encoding

Base64 encoding is a format for converting binary content into a set of standard characters for sending over networks. Certain apps only allow Base64-encoded file uploads, and those apps often produce Base64-encoded file content when their files are downloaded.

Workato supports the ability to encode or decode Base64 content using [Formulas](/en/formulas/formula-mode).

To Base64 encode binary content and upload it into such apps:

![Encode file content](/assets/encode-file.ah2234bN.png)_Formula for encoding file content_

To decode Base64 content to binary content from such apps:

![Decode file content](/assets/decode-file.CRl1GMFp.png)_Formula for decoding file content_

---
