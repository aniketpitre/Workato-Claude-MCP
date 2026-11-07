---
url: 'https://docs.workato.com/en/resources/resource-management.md'
description: >-
  Upload, view, update, download, delete, move, and version Workato resources
  using the Workato UI.
---

# Resource management

Refer to the following sections to manage resources in Workato:

- [Upload resources](#upload-resources)
- [View a resource](#view-a-resource)
- [Update a resource](#update-a-resource)
- [Download a resource](#download-a-resource)
- [Delete a resource](#delete-a-resource)
- [Move a resource](#move-a-resource)
- [Version management](#versioning)
  - [Restore a resource version](#restore-a-resource-version)

> **RESOURCES API**
> 
> Refer to the [Resources API](/en/workato-api/static-assets) guide to manage resources programmatically.

## Upload resources

Complete the following steps to upload resources using the Workato UI:

1. Go to the project where you plan to store the resource. Alternatively, go to **Assets > Resources**.
   
2. Click **Create > Resource**.
   
   ![Click Create > Resource](/assets/create-resource.C_QWtdki.png)_Click **Create > Resource**_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the resource.
   
   ![Select a Location for the resource](/assets/upload-resource.BsTGQEfi.png)_Select a **Location** for the resource_
   
4. Drag and drop files, or click **Upload from device** to select files.
   
   > **FILE LIMITATIONS**
   > 
   > Resources have a maximum size of 50 MB and must be one of the following file types:
   > 
   > - `.xsd`
   > - `.xslt`
   > - `.wsdl`
   > - `.rb`
   > - `.js`
   > - `.py`
   > - `.wel`
   
   Upload errors
   
   Workato stops the upload and displays an error in the following scenarios:
   
   - A resource with the same file name already exists in this folder.
   - The file exceeds the maximum allowed size of 50 MB.
   - The file has an unsupported extension.
   - The file was selected multiple times in this upload batch.
   
5. Click **Done**. Workato stores the files as resources and scans them for threats. You can't view or interact with a resource until the scan is complete.
   

Workato marks a file as **Malicious** if it detects a threat. Workato blocks malicious files from view, download, and use in recipes. [Delete](#delete-a-resource) the file or [upload a new version](#update-a-resource) to proceed.

Resources [are available in recipes](/en/resources/recipe-integration) after they pass the security check.

## View a resource

You can select a resource to view its **Contents** tab.

![Resource Contents tab](/assets/contents-tab.BkkonucW.png)_Resource **Contents** tab_

The **Contents** tab contains the following information:

- A preview of the file's content.
- **Version**: The numerical identifier for the version and its security scan status.
- **Type**: The resource's file type.
- **Updated**: Timestamp when the resource was last updated.
- **Tags**: Organizational tags applied to the resource. Click **Apply tags** to add tags.
- **Latest activity**: Recent changes to the resource.

Refer to the [Version management](#versioning) section for information about the **Versions** tab.

## Update a resource

Complete the following steps to upload a new version of an existing resource:

1. Go to the project that contains the resource or go to **Assets > Resources**.
   
2. Select the resource, then click **Upload new version**.
   
   ![Upload a new version](/assets/upload-new-version.CB1igteX.png)_Upload a new version._
   
3. Drag and drop files or click **Upload from device** and select files to upload.
   
   > **FILE LIMITATIONS**
   > 
   > Resources have a maximum size of 50 MB and must be one of the following file types:
   > 
   > - `.xsd`
   > - `.xslt`
   > - `.wsdl`
   > - `.rb`
   > - `.js`
   > - `.py`
   > - `.wel`
   
4. Click **Done** to upload the file.
   
   Workato stores the new file and scans it for threats. You can't view or interact with the new version until the scan is complete, but the last resource version remains available.
   

Workato marks a file as **Malicious** if it detects a threat. Malicious files are blocked from view, download, and use in recipes. Resources continue using the latest safe version until a new version passes the security check.

## Download a resource

Complete the following steps to download a resource using the Workato UI:

1. Go to the project that contains the resource or go to **Assets > Resources**.
   
2. Select the resource to download.
   
3. Optionally, go to the **Versions** tab and select a previous version to download.
   
   ![Resource Versions tab](/assets/versions-tab.DLFKEMKX.png)_Resource **Versions** tab_
   
4. Click **Download**.
   
   ![Click Download.](/assets/download-resource.7nVS0kbH.png)_Click **Download**._
   

## Delete a resource

Complete the following steps to delete a resource using the Workato UI:

> **REMOVE DEPENDENCIES FIRST**
> 
> Remove all references to a resource before deleting it to prevent job failures.

1. Go to the project that contains the resource or go to **Assets > Resources**.
   
2. Select the resource to delete.
   
3. Click **Delete** (trash icon). A confirmation modal displays the recipes that reference this resource. Remove these references before you delete the resource to avoid job failures.
   
   ![Click Delete.](/assets/delete-resource.CvYZmj4z.png)_Click **Delete**_
   
4. Click **Delete resource** to confirm the deletion.
   
   ![Click Delete resource.](/assets/delete-confirmation.BwlqQVN0.png)_Click **Delete resource**._
   

## Move a resource

Complete the following steps to move a resource:

> **UPDATE RESOURCE REFERENCES**
> 
> Resource references store static paths to the file and resolve the paths at runtime. These paths don't update automatically when you move a resource. Update references with the new path to prevent job failures.

1. Go to the project that contains the resource. Alternatively, go to **Assets > Resources**.
   
2. Select the **...** (ellipsis) on the resource you plan to move, then click **Move**.
   
   ![Click Move.](/assets/context-menu-move.Cxj5k_Xw.png)_Click **...** (ellipsis), then click **Move**._
   
3. Use the **Location** drop-down menu to select the project where you plan to store the resource.
   
4. Click **Move**. A confirmation modal displays the recipes that reference this resource. Update these references with the new resource path to avoid job failures.
   

## Version management

Workato maintains the last 100 versions of a resource. Go to a resource's **Versions** tab to view its history.

![Resource Versions tab](/assets/versions-tab.DLFKEMKX.png)_Resource **Versions** tab_

The **Versions** tab contains the following information for each version:

- **Version**: The numerical identifier for the version.
- **Current**: A badge indicating the latest safe version. Recipes use this version at runtime.
- **Uploaded on**: The date and time the version was uploaded.
- **Modified by**: The user that last modified the version.
- **Comments**: The comment attached to the version. Click **Add comment** to attach a comment.
- **Status**: The results of the security scan.

Select a specific version to see a preview of its contents.

> **VERSION UPDATES**
> 
> Resource references use the latest safe version at runtime. You can't prevent a reference from updating. Refer to [Restore a resource version](/en/resources/resource-management#restore-a-resource-version) to restore a resource to a previous version.

### Restore a resource version

[Download](#download-a-resource) the version you plan to restore, then [upload it as a new version](#update-a-resource) to restore a resource to a previous version.

---
