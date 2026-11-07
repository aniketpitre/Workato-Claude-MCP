---
url: 'https://docs.workato.com/en/recipe-development-lifecycle/import.md'
description: >-
  Import a package of exported recipes and dependencies to deploy them into a
  Workato workspace using the package import UI or deployment APIs.
---

# Importing: Deployment

Importing a package is the final step in the recipe development lifecycle, where finished recipes are deployed in a Workato instance. You must have a package containing [exported](/en/recipe-development-lifecycle/export) assets to import recipes and dependencies into a Workato workspace.

You can deploy a tested package to a new environment in multiple ways:

- Package import UI A package zip file can be deployed manually using package import UI.
- Deployment APIs A package zip file can be deployed using Workato [platform APIs](/en/workato-api/recipe-lifecycle-management). For example, you can initiate the deployment from your CI/CD server using a cURL request.

> **EXPLORE ENVIRONMENTS FOR ENHANCED FUNCTIONALITY**
> 
> Enhance your recipe development experience by integrating Recipe Lifecycle Management (RLCM) with Environments.
> 
> Environments are built on the same principles as RLCM and offer a seamless deployment experience across unified workspaces. Refer to [Environments](/en/features/environments) for more information.

* * *

## Contents

This section covers how Workato recipes and dependencies are deployed (imported) into your target workspace. If you have already imported a package, you may move on to the last section on working with external source control systems:

- [Planning for lifecycle management](/en/recipe-development-lifecycle/export)
- [Exporting: Packaging recipes and dependencies](/en/recipe-development-lifecycle/export)
- **Importing: Deployment** _(current)_
- [Working with external source control systems](/en/recipe-development-lifecycle/rdlc-guide-source-control)

* * *

## Import quotas

The maximum allowable size for imported packages is 100 MB. You can import one package at a time.

* * *

## Import a package

Complete the following steps to import a package into Workato:

> **CREATE PROJECTS PRIVILEGE REQUIREMENT**
> 
> You must have the **create projects** privilege to import `All projects`.

> **PROJECT NAMES MUST MATCH**
> 
> The name of the project in the destination workspace where you import a Workflow app must match the name of the project being imported.

1. Sign in to your Workato account.
   
2. Go to **Tools > Recipe lifecycle management** in the sidebar navigation.
   
3. Select the **Import** tab.
   
   ![Select import tab](/assets/select-import-tab.C_o2LftU.png)_Select import tab_
   
4. Drag and drop the `.zip` file containing the package you plan to import into the **Select zip file** field, or click **upload from device**.
   
   ![Select zip file](/assets/select-zip-file.CbtU0UYa.png)_Select `.zip` file_
   
5. Choose a **Target folder** for the import. This folder must already exist in your workspace. If the required folder or project is not listed, select **New project** to create one.
   
6. Enable the **Import all tags** toggle to include tags associated with your assets during import. When enabled, all tags associated with the imported assets are included in the process.
   
7. Click **Next** to proceed. The wizard reads the package contents, loads its data, and compares it with existing recipes and dependencies in your account.
   

## Sort manifests

Workato provides sorting options for export and import manifests. You can sort manifests by **Latest activity** or **Name (A -> Z)** to organize your content efficiently.

![Sort manifests](/assets/sort-manifests-import.CADOn9X-.png)_Sort manifests_

* * *

## Import status tags

On the import preview screen, each item is assigned a tag that will inform the user of its import status.

### Recipes

![Import preview](/assets/import-tags.8sYKofwe.png)_Example status tags for recipes and assets that will be imported_

- Recipes that don't exist in the target folder are tagged with "Add".
- Recipes that exist and weren't changed are tagged with "No change".
- Recipes that exist and have been edited are tagged with "Update recipe logic".
- If a running recipe needs to be updated, it is tagged with "Update running logic". The recipes are stopped, updated, and then automatically restarted.

#### Updating a running recipe

![Warning overwriting running recipes](/assets/overwrite-running-recipe-warning.rmUgbvIu.png)_Running recipes will be stopped and then automatically restarted_

If there are running recipes that must be updated, Workato displays a warning after the review process. In this situation, recipes with pending jobs cannot be stopped.

##### Event handling during deployment

The behavior during deployment depends on what changes you're making:

**Webhook recipes**:

- **Trigger condition changes only**: No downtime occurs. The current recipe continues processing events, and once deployment succeeds, the updated version processes new events with the new trigger condition. This ensures zero event loss.
- **Other webhook trigger configuration changes**: Brief downtime may occur (such as 404 responses) as the recipe restarts with the new configuration.

**All other recipe types**:

- **Any trigger changes**: Recipe downtime occurs as the recipe must restart in the backend.

Recipes imported successfully will restart automatically and continue running seamlessly. Any errors in restarting the recipes must be fixed manually. Once the process is completed, the new/updated recipes and dependencies should be successfully imported and restarted.

If errors occur with starting a recipe after the import process, you should select the link to the recipe, resolve any errors and restart the recipe manually.

Running recipes need to be restarted in the following scenarios:

1. When the recipe's trigger or trigger input has been changed (except webhook trigger condition changes)
2. When the trigger connection has been switched to another

### Connections

One of the main advantages of separate accounts for the different lifecycle phases is that each can have its own set of connections, and these can be different: for example, a development account can use an application sandbox account for its recipes, while a production account uses the production application account with live data.

For security reasons, exporting a package does not export any credentials, keys, or other private data needed to make a connection to applications. Those are kept private. Only the connection name, application type and other non-sensitive information will be exported. Here, a placeholder connection is created. This placeholder contains only the application and name of the connection. **Authentication to this placeholder is required after import**.

When importing a package, Workato will attempt to automatically fill in connection details with existing connections in the importing account. Workato checks that this **connection type exists** and that there are **no multiple connections** of that type (for example, multiple Gmail accounts). If these conditions are met, the connections required in the imported recipes will be configured automatically. If this is not possible, then you may need to manually re-establish connections needed by the recipes after import.

### Lookup tables

Lookup tables in the zip file contains schema data (name and column names) but may or may not contain data. During import, users can specify if the table data should be or overwritten or ignored.

If the lookup table contains no data, it will be created/updated with only column names. If the lookup table contains data, use the radio buttons to select if the data should be overwritten or ignored.

![RLM in tools gif](/assets/import-assets.Rf4iY2B9.png)_'Import data' or 'Ignore data' on individual lookup tables to be imported_

‘Overwrite’ will cause all table data to be overwritten and all data in the table to be replaced permanently. ‘Ignore’ will disregard all table data even though the table was exported with data.

Workato recommends you establish rules and procedures for the use of these options. The simplest approach is to use the defaults: “include data” on export and “overwrite data” on import. This assumes, however, that the lookup table in the importing account can be safely overwritten, without affecting recipes that are not part of the package being imported.

### Other dependencies

Other recipe dependencies will have the following tags according to their statuses.

1. A new recipe/dependency will be added (Creates a new dependency)
2. If there are no detected changes, the asset will be tagged with a **‘No change’** tag
3. The current recipe/dependency will be overwritten with the changes in the import (Overwrites dependency)

* * *

## Packages import behavior

The following table details how an imported package's assets are moved into your Workato account.

| Dependency type | What Workato does when package is imported | Location |
| --- | --- | --- |
| Recipes | **Overwrites** recipe if a recipe with the same name exists in the folder. **Creates** new recipe if no recipe with the same name exists in the folder. | Selected folder |
| Custom connectors | Overwrites existing custom connector if connector with same name already exists in the Workato account. Creates new connector if no connector with the same name exists in the Workato account. | Connector SDK |
| Connections | Creates a connection placeholder. The user should connect the application after importing. Nothing is done if a connection with the same name already exists. | App Connections |
| Lookup tables | Creates a lookup table with the header rows. Imports the lookup table data if selected during export and import. | Lookup table |
| Environment properties | Adds properties to existing properties in the Workato account. Does nothing if a property with the same name already exists. | Environment properties |
| Project properties | Adds properties scoped to the project level to the target folder you specify. Workato does not support importing packages containing project properties into the root folder (All projects) and displays an error message if you attempt to do so. | Selected folder |
| Common data models | Adds the schema to existing shared schemas in the Workato account or updates it if a schema with the same name already exists. | Common data models |
| Message templates | Adds the message template to existing templates in the Workato account or updates it if a template with the same name already exists. | Message templates |
| Event streams | Places the imported event stream into a folder or project. Event streams without folder information during the [transition period](/en/event-streams#event-streams-as-project-assets) are placed into the default **Event Streams** project, which Workato creates the first time it's needed. Imported packages must include folder information for each event stream after the transition period. Workato retains the [retention period](/en/connectors/pubsub/pubsub-retention) settings of the original event stream. | Selected folder / Event Streams project |

---

---
url: >-
  https://docs.workato.com/en/recipe-development-lifecycle/rdlc-guide-source-control.md
description: >-
  Learn how to store exported Workato recipes in external source control like
  git, mapping projects to repositories and managing pull requests.
---

# Working with external source control systems

One reason to export recipes from Workato is to enable storage in a centralized version control system. This is a standard practice at many companies that do development; but whether you do this or not may depend on whether you have staff who normally do software development work on Workato recipes, or whether you have less technical staff doing that task who aren’t accustomed to using source control for their work.

The following discussion assumes that your version control system is “git,” although the same general principles could be used with other systems.

In general, Workato recommends that you use external version control primarily for maintaining a set of snapshots of the code and as a staging area for teams to deliver and pick up code. That still has some value, because git will have a coherent history spanning the different Workato environments and everyone with a git account can see that. It also ensures that recipes can be backed up securely in the git repository.

However, it isn’t recommended that you make changes to the recipe files while they reside outside of Workato in an external source control system. That could be risky because you don’t have the checking and validation Workato will do when changes are made in the Workato environment. Also, changes made in this way will not show in the version history visible in Workato.

## Contents

- [Planning for lifecycle management](/en/recipe-development-lifecycle/rdlc-guide-planning)
- [Exporting: Packaging recipes and dependencies](/en/recipe-development-lifecycle/export)
- [Importing: Deployment](/en/recipe-development-lifecycle/import)
- **Working with external source control systems** _(current)_

## Workato project to GitHub repository mapping

Workato packages can be mapped directly to a Git repository. A single account can have multiple projects and each project is bundled using a package.

In the example below, the Acme Workato workspace contains three projects and they map onto three repositories in Acme’s GitHub account.

![GitHub workato packages](/assets/source-control.DcyuGzcW.png)_Mapping Workato packages to GitHub repos_

## Pull requests (PRs)

### Creation

Each new feature development starts in the Workato development account. After feature completion, the recipe developer should build a package based on the latest version of the recipes. The package should be extracted to the local Git repository directory for the project and unzipped. Then the changes should be committed to a feature branch, and pushed to a central GitHub repository.

![Create PR](/assets/pr-creation.WlAhgIHC.png)_Commit latest package to existing GitHub repository_

Once the feature branch exists in GitHub, the developer can submit a pull request (PR) for review.

![Created PR](/assets/pr-created.B92-ftIJ.png)_Create PR in GitHub_

### Review

One or more reviewers can examine the new code in GitHub and add comments. The developer should address the review comments and update the PR with the fixed code. As mentioned earlier, it is recommended that changes be made first in Workato, tested, then re-exported.

![Review PR](/assets/pr-review.B8gt0Nvz.png)_Viewing recipe changes (against previous version) in GitHub_

### Merge and promotion across environments

After all PR comments are resolved, the feature branch can be merged into the master branch. At this point, the code for recipes and other artifacts can be imported into a different Workato account corresponding to the next lifecycle stage. This can be done either by export followed by import directly on Workato's UI or by a script that zips the GitHub code back into a Workato package which will be used for import.

---
