---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/download-file-from-library-action.md
description: >-
  The download file action in the SharePoint connector lets you download a file
  from a library you specify.
---

# SharePoint - Download file from SharePoint library action (file)

This action downloads a file from a SharePoint library you specify.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Folder relative URL | Provide the relative URL of the folder. For example, if you have not specified the **Site name**, enter `/documentlibraryname/foldername`.If you have provided the **Site name**, enter `/sites/sitename/documentlibrary/foldername`. |
| File path | Provide a direct path to the file. For example, `/sites/sitename/documentlibrary/foldername/filename.txt`. |
| File name | Provide the name of the file you plan to download. |
| Encoding of the file content | Specify the encoding of the file to set it explicitly. By default, Workato sets the encoding to UTF-8 if left blank. Learn more about the [encodings Workato supports](https://en.wikibooks.org/wiki/Ruby_Programming/Encoding). |

## Output

The output datatree contains the content of the downloaded file.

| Field | Description |
| --- | --- |
| Content | The content of the downloaded file. |
