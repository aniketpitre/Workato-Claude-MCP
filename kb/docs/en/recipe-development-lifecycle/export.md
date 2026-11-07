---
url: 'https://docs.workato.com/en/recipe-development-lifecycle/export.md'
description: >-
  Export Workato recipes and their dependencies into package zip files to move
  assets between environments or store them in version control.
---

# Export: Packaging recipes and dependencies

You can export packages to create distributable files containing related recipes and their dependencies. This step in recipe lifecycle management typically follows the completion of recipe and asset development, or when business process changes require recipe edits. Workato packages these recipes and assets into zip files, containing JSON file representations of each exported item. You can use packages to:

- Move recipes between environments, transitioning from development to test, and then to production.
- Store recipes in traditional version control systems like git.

After completing the export process, you can [import](/en/recipe-development-lifecycle/import) the package in another Workato instance to apply the changes.

> **EXPLORE ENVIRONMENTS FOR ENHANCED FUNCTIONALITY**
> 
> Enhance your recipe development experience by integrating Recipe Lifecycle Management (RLCM) with Environments.
> 
> Environments are built on the same principles as RLCM and offer a seamless deployment experience across unified workspaces. Refer to [Environments](/en/features/environments) for more information.

* * *

## Contents

This section covers how to convert Workato recipes and dependencies into shareable assets, known as packages. If you have already exported a package, you may move on to our other sections:

- [Planning for lifecycle management](/en/recipe-development-lifecycle/rdlc-guide-planning)
- **Exporting: Packaging recipes and dependencies** _(current)_
- [Importing: Deployment](/en/recipe-development-lifecycle/import)
- [Working with external source control systems](/en/recipe-development-lifecycle/rdlc-guide-source-control)

* * *

## Export manifests

To export a package, you must define an export manifest. A manifest is a record of all the recipes and dependencies that you select for export and re-export. You can edit the manifest at any time after its initial creation and first export.

> **CREATE PROJECTS PRIVILEGE REQUIREMENT**
> 
> You must have the **create projects** privilege to export `All projects`.

Reuse an existing manifest if you've updated recipes and plan to export the same set of objects again.

You can modify the manifest to reflect changes in your designated export folder, such as adding new assets or removing ones that are no longer necessary. If you plan on excluding certain recipes from the export, you can make these adjustments during the editing process.

* * *

## Create a manifest

Complete the following steps to create a manifest in Workato:

1. Enter a **Manifest name** to identify your content within Workato.
   
   ![Create manifest](/assets/create-manifest.DQxvF3ZR.png)_Provide the manifest name and source folder_
   
2. Choose the **Source folder** for your manifest and click **Next**. Workato automatically adds all recipes and dependent assets from the chosen folder and its subfolders to your manifest.
   
   ![Example manifest](/assets/manifest-assets.jeLcNAc4.png)_Example manifest with recipes and dependencies_
   
3. Select the **Select all assets** checkbox to include all available assets in your export manifest, or clear it to choose specific assets individually. This option allows you to customize which connections, custom connectors, lookup tables, recipe functions, and other assets are part of the manifest. All environment properties within your Workato account are displayed on this page.
   
4. Select the **Include tags** checkbox to include tags associated with your assets in the manifest. When selected, all tags related to the chosen assets are included in the export.
   

### Dependencies from other projects

When selecting assets for your manifest, Workato alerts you if any assets are located outside of the chosen folder. For instance, if a required connection is not in the folder:

- Navigate to the app connections page.
- Relocate the connection to the appropriate folder. Note that connections stored in the home folder are shared and can be exported from any folder. You can ignore orange warning messages if you plan to proceed with the export without dependent assets.

![Connection in different folder](/assets/dependent-asset-not-found.BH9-Ob9o.png)_Warning for a connection in a different folder_

Workato displays an orange warning if you deselect dependencies while configuring your manifest, indicating potential missing dependencies in the final exported package. Expand each recipe line to re-select any assets you deselected. You can ignore this warning if the deselected dependency is not required in your exported package.

![Warnings when deselecting objects](/assets/deselect-object.CuOPVefB.png)_Warnings when deselecting objects_

We recommend that you place connections that are shared between different accounts in the root or `Home` folder. This enables you to export your connections, regardless of the source folder you select.

You can choose to export data in individual lookup tables. For each table, select **Include data** to export every row or **Ignore data** to export only the headers. This setting defaults to **Ignore data**.

![Ignore data or include data on each lookup table](/assets/lookup-tables-properties.CGj8O0PO.png)_**Ignore data** or **Include data** on each lookup table_

After configuring your manifest, save it. Workato stores saved manifests in the **Export** tab of the Recipe lifecycle management interface. You can reuse this manifest to create additional packages.

* * *

> **ASSETS FROM DIFFERENT PROJECTS**
> 
> Assets from different projects are not automatically included in a manifest. If your recipes call [recipe functions](/en/connectors/recipe-functions) from other projects, you must reorganize these recipes into the same [project](/en/projects) to include them in the manifest.

## Sort manifests

Workato provides sorting options for export and import manifests. You can sort manifests by **Latest activity** or **Name (A -> Z)** to organize your content efficiently.

![Sort manifests](/assets/sort-manifests.DQhyJGez.png)_Sort manifests_

* * *

## Export a manifest as a package

After creating a manifest, you can export it as a package by clicking the **Build and export package** button.

Clicking on this button creates a .zip file package and opens a pop-up displaying the export status. After the .zip file finishes building, you can download it.

![Download package](/assets/download-package.B86Ap8la.png)_Download the zip file after export_

Workato records all export-related activities in the **Export history** tab of the manifest. To download a previous version of the package, click the **Download zip file** button in the last column of the history table. The package version corresponds to the state of the manifest at the time of your export. Each package is available for the duration of the [data retention](/en/security/data-protection/data-retention/) period set in your workspace. Go to **Workspace admin > Settings > Data retention** to find the data retention period of your workspace.

![Export history](/assets/export-history.Bnzpmc1C.png)_Review past exports in the export history tab_

* * *

## Troubleshoot manifest export errors

You may encounter the following error message when exporting a manifest:

![Manifest error](/assets/manifest-error.BniQJxGS.png)_Manifest export error_

This error indicates that some assets referenced in the manifest are missing. These assets may have been deleted or moved to a different folder after you created the manifest. Complete the following steps to resolve this error:

1. Click the **Review missing assets** button in the error message popup. This action displays a list of the missing assets. Alternatively, you can click **Edit manifest** to access the same list.
   
   ![Manifest error](/assets/review-assets.Bu5rBP3y.png)_Review missing assets_
   
2. Ensure that the assets listed in the manifest are still present in their original locations. Missing assets are marked as **Not found**.
   
3. Restore moved assets to their original locations or update the manifest to reflect their new locations.
   
4. Deselect or remove any unavailable assets, and then click **Update manifest** to save your changes.
   
   ![Manifest error](/assets/edit-manifest.D0KG47Tf.png)_Edit manifest_
   
5. Click the **Build and export package** button to retry the export process after addressing the missing assets.
   

* * *

## Returning to an existing manifest

When you continue developing recipes in the same folder, you may need to return to an existing manifest to re-export its contents. During this process, the following changes may occur:

- Assets were deleted
- Assets were moved to a different folder/sub-folder
- Assets were renamed
- Assets were edited
- Assets were added

### Deleted, moved, or renamed assets

Workato automatically performs checks to ensure cross-compatibility and synchronization across instances before exporting a manifest. Changes such as deleting, moving, or renaming assets affect the structure of your manifest. When Workato detects these changes, it highlights them and prompts your review.

To continue with the export, you must review the manifest and decide whether to remove references to deleted files or confirm the changes made.

![Warnings for deselected objects](/assets/missing-connection.D-NxlLx3.png)_Warnings for deselected objects_

### Edited assets

When you edit assets in a manifest, such as recipe actions, mappings, or lookup table additions, they are highlighted with a blue **Updated** tag.

If these edits don't impact your export objectives, you have the option to ignore them by clicking on **Ignore changes and build package**. This allows you to create the package to include the latest version of each asset while maintaining the existing structure of your manifest.

![Example of an edited recipe and a new recipe](/assets/new-changed-asset.C8jeYF1q.png)_Example of an edited recipe and a new recipe_

### New assets

When you add a new recipe or dependency to a folder, Workato detects this change and highlights it with a green **Added** tag. Complete the following steps to include the new asset in the manifest:

1. Click **Review manifest changes** in the **Manifest content** tab.
   
2. Find the asset marked with the green **Added** tag and select the checkbox next to it.
   
3. Click **Update manifest**. This action updates the manifest with the new asset and saves it as part of the latest manifest version.
   

### Navigate assets with hyperlinks

Workato's manifest interface includes hyperlinks for each asset, providing you a direct way to navigate through manifests. You can click on hyperlinked asset names within the manifest to open their detailed pages in new tabs, instead of manually searching for your assets. This provides you immediate access to the latest information for each asset, ensuring a more efficient review process.

![Asset hyperlinks](/assets/manifest-hyperlinks.C_Z2nPzS.png)_Navigate assets with hyperlinks_

---
