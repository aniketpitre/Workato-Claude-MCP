---
url: 'https://docs.workato.com/en/projects.md'
description: >-
  Learn how to create and manage projects in Workato. Use projects to organize
  your integration assets by department, use case, or application.
---

# Projects

A project is a container for your integration assets in Workato, such as recipes, connections, genies, and more. Projects can be further organized into folders and are typically grouped by department, use case, or application.

Admins control access by assigning collaborators a project role, such as **Project admin** or **Builder**, that defines what they can create, edit, view, or delete within that project.

## Create a project

Complete the following steps to create a project:

1. Sign in to Workato.
   
2. Go to **Projects**.
   
   ![The Projects page](/assets/projects-page.CgXt349P.png)_The **Projects** page_
   
3. Create a project using one of the following methods:
   
   - Select **Create > Project**.
   - Press C+P.
   - Click the **+** icon next to the search bar in the sidebar.
4. Enter a name for your project in the **Project name** field.
   
   ![Enter project name](/assets/create-project-name.DJ9CcZ8d.png)_Enter a project name_
   
5. Select a starting point for your project:
   
   - Choose **Build a recipe** to create a project with a [recipe](/en/recipes) as your first asset.
   - Choose **Build a genie** to create a project with a [genie](/en/agentic/workato-genies) as your first asset.
   - Choose **Build an MCP server** to create a project with an [MCP server](/en/mcp) as your first asset.
   - Choose **Build an app** to create a project with a [workflow app](/en/workflow-apps) as your first asset.
   - Choose **Start from scratch** to create a blank project.
   
   These options determine your starting point only. You can add recipes, genies, MCP servers, workflow apps, and other assets to your project after it's created.
   
6. Click **Create project**. The new project appears in the **Projects** menu.
   
   If you selected an option other than **Start from scratch**, a creation wizard opens to help you set up your first asset. Refer to the following guides to complete the wizard:
   
   - [Build a recipe](/en/getting-started/build-first-recipe#step-1-create-a-new-recipe)
   - [Build a genie](/en/agentic/agent-studio/create-a-genie)
   - [Build an MCP server](/en/mcp/mcp-servers#create-an-mcp-server)
   - [Build an app](/en/workflow-apps/getting-started#app-create)

## Customize a project

By default, a project displays the first letter of its name as its icon. Complete the following steps to customize a project:

1. Click the **Customize project** icon next to the project name, or select **Customize** from the **...** menu next to the project in the sidebar.
   
   **Project page**
   
   ![Customize project icon](/assets/customize-project.ID77A3jP.png)_Click the **Customize project** icon_
   
   **Sidebar**
   
   ![Customize project sidebar](/assets/customize-project-1.CU3xHoLh.png)_Select **Customize** from the **...** menu next to the project_
   
2. Customize the project's name, **Color**, and icon. The icon options are organized into two tabs:
   
   - **Icon**: Choose from a set of preset icons.
   - **Emoji**: Choose an emoji to represent the project.
   
   ![Customize the project.](/assets/customize-project-menu.Cw0LNCs4.png)_Customize the project._
   
3. Click **Save**.
   

## Reorder project tabs

The project detail page includes the following tabs: **Canvas** (if available in your workspace), **Workflow app**, **Assets**, **Deployments**, and **Settings**. You can drag and drop tabs to reorder them for any project.

Tab order is saved per user and per environment, so changes you make only apply to you and don't affect other collaborators. Tab order is also configured per project, so if you want a consistent order across all your projects, you need to update each one individually.

![Reorder project tabs](/assets/reorder-tabs.CDzqyt0t.gif)_Reorder project tabs_

## Create a folder

Complete the following steps to create a folder:

1. Create a folder using one of the following methods:
   
   - Select **Create > Folder**.
   - Press C+F.
   - Select **Create folder** from the **...** menu next to a project in the sidebar.
   
   ![Create folder](/assets/create-folder-new.C9xd1IEJ.png)_Create folder_
   
2. Enter a name in the **Folder name** field. The folder name must be unique within its parent folder.
   
   ![Enter folder name](/assets/create-folder-name.CASsujcp.png)_Enter a folder name_
   
3. Use the **Location** drop-down menu to select the project where you plan to create the folder.
   
4. Click **Create folder**. The new folder appears as a sub-folder within the project.
   

## Manage projects and permissions

Project roles control a collaborator's permissions to create, edit, view, or delete content within specific projects. You can assign collaborators a project role, such as **Project admin**, **Builder**, or a [custom project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#create-a-custom-project-role), to define their level of access.

> **PROJECT ACCESS**
> 
> You can't share an individual project directly outside your workspace. [Invite collaborators to the workspace](/en/user-accounts-and-teams/role-based-access/managing-team-collaborators#invite-and-manage-workspace-collaborators) and assign them a project role for each project where they need access.

## Smart folders

Smart folders provide a cross-project view of all your recipes and connections. You can filter by active or inactive recipes, and connected or disconnected connections.

![Smart folders](/assets/smart-folder-assets.BqNt_j2q.png)_Smart folders_

## Assets page

The **Assets** page provides the following filters:

![Filter assets page](/assets/assets-page-filters.ituRsh8J.png)_Assets page filters_

- All assets
  
- Filter by all types of assets, including recipes, connections, pages, genies, skills, knowledge bases, and event streams.
  
- App
  
- Select one or more apps. Only assets with the apps you select display in the results.
  
- Edited by
  
- Filter by the user who edited the assets. Choose **Me** to view assets you edited, or **Others** to select and view assets edited by specific collaborators within the workspace. Not all users can view assets edited by other collaborators.
  
- Tag
  
- Filter by [tags](/en/recipes/tags) applied to assets.
  

These filter options provide additional [sub-filters](#asset-sub-filters) for granular search results.

### Assets tab

The **Assets** tab allows you to filter and manage assets specific to the selected project. It provides the same filters and sub-filters as the [Assets page](#assets-page), but only applies to assets within the current project.

![filter assets tab](/assets/asset-filter-tab.CEkSyBoM.png)_Assets tab filters_

### Asset sub-filters

The **Assets** page and **Assets** tab both provide sub-filters for managing assets.

![Sub-filter assets page](/assets/recipe-sub-filter.BoiCS95m.png)_Filter by assets_

Recipes

| Sub-filter | Description |
| --- | --- |
| Status | Filter by **Active** or **Inactive** status. All statuses are shown by default. |
| App | Select multiple apps to filter recipes associated with those apps. |
| Recipe trigger | Choose one trigger option from an app, as each recipe can only have a single trigger. |
| Edited by | Filter by the user who edited the recipes. Choose **Me** to view recipes you edited, or **Others** to select and view recipes edited by specific collaborators within the workspace. Not all users can view recipes edited by other collaborators. |
| Tag | Filter recipes by tags. |

Connections

| Sub-filter | Description |
| --- | --- |
| Status | Filter by **Connected** or **Disconnected** status. All statuses are shown by default. |
| App | Choose one app to filter connections associated with that app. |
| Edited by | Filter by the user who edited the connections. Choose **Me** to view connections you edited, or **Others** to select and view connections edited by specific collaborators within the workspace. Not all users can view connections edited by other collaborators. |
| Tag | Filter connections by tags. |

Pages

| Sub-filter | Description |
| --- | --- |
| Edited by | Filter by the user who edited the pages. Choose **Me** to view pages you edited, or **Others** to select and view pages edited by specific collaborators within the workspace. Not all users can view pages edited by other collaborators. |
| Tag | Filter pages by tags. |

Genies

| Sub-filter | Description |
| --- | --- |
| Edited by | Filter by the user who edited the genie. |
| Tag | Filter genies by tags. |

Skills

| Sub-filter | Description |
| --- | --- |
| Edited by | Filter by the user who edited the skill. |
| Tag | Filter skills by tags. |

Knowledge bases

| Sub-filter | Description |
| --- | --- |
| Edited by | Filter by the user who edited the knowledge base. |
| Tag | Filter knowledge bases by tags. |

MCP servers

| Sub-filter | Description |
| --- | --- |
| Edited by | Filter by the user who edited the MCP server. |
| Tag | Filter MCP servers by tags. |

Decision models

| Sub-filter | Description |
| --- | --- |
| Edited by | Filter by the user who edited the decision model. |
| Tag | Filter decision models by tags. |

Event streams

| Sub-filter | Description |
| --- | --- |
| Edited by | Filter by the user who edited the event stream. |
| Tag | Filter event streams by tags. |

### Search assets

You can search for assets by name, description, app, or action from the **Assets** page.

![Search assets](/assets/assets-page-search.wOiBEvhV.png)_Search assets_

> **SORT SEARCH RESULTS**
> 
> Search results are sorted by relevance by default. You can change the sorting order, which remains in effect until you reset the search.

## Move assets

You can move assets using the Workato UI, the Developer API, or the Embedded API. Dependencies are automatically updated when you move an asset.

**In-app**

You can drag and drop an asset into a different project to move it. ![Drag and drop an asset](/assets/drag-and-drop-assets.PIcJzi6i.gif)_Drag and drop an asset_

Alternatively, you can complete the following steps to move an asset using a modal:

1. Click the **...** (ellipsis) next to the asset, then click **Move**. ![\_Click the ... (ellipsis), then click Move](/assets/click-move.TPQIqm1C.png)_Click the **...** (ellipsis), then click **Move**_
   
2. Select a new storage **Location** for the asset from the drop-down menu, then click **Move**. ![Select a new storage Location](/assets/select-location.DXlBK6ui.png)_Select a new storage **Location**_
   

**Developer API**

You can use the following endpoints to move assets using the Developer API:

- Move connections using the [Update a connection](/en/workato-api/connections#update-a-connection) endpoint.
  
- Move recipes using the [Update a recipe](/en/workato-api/recipes#update-a-recipe) endpoint.
  
- Move assets as a package using the [Import a package into a folder](/en/workato-api/recipe-lifecycle-management#import-package-into-a-folder) endpoint.
  

**Embedded API**

You can use the following endpoints to move assets using the Embedded API:

- Move connections using the [Update a connection](/en/oem/oem-api/connections#update-a-connection) endpoint.
  
- Move recipes using the [Update recipe in a customer workspace](/en/oem/oem-api/recipes#update-a-recipe) endpoint.
  
- Move assets as a package using the [Import package into a customer workspace](/en/oem/oem-api/recipe-lifecycle-management#package-import) endpoint.
  

## Tags for assets

Tags are labels you apply to assets to add context and group them across projects. You can filter and search by tag to find assets that share an attribute.

![Tags for assets](/assets/asset-tags.DiTviNCI.png)_Tags for assets_

Refer to [Tags for assets](/en/recipes/tags) for more information.

## Delete a project

Deleting a project permanently removes it. Connections are deleted and recipes are moved to the trash, where you can restore or permanently delete them.

![Restore deleted recipe](/assets/restore-deleted-recipe.Bq_k3UEa.png)_Restore deleted recipe_

Deleting a shared connection removes it from every project where it is used, which may break recipes or workflows that rely on it.

> **PROJECTS WITH ACTIVE ASSETS CAN'T BE DELETED**
> 
> You can't delete a project with active assets.

You can delete a project from the **Projects** page in two ways:

- Drag the project to the **Trash** folder in the **Projects** menu.

![Delete by dragging the project](/assets/delete-drag.B_Ej8Th8.gif)_Delete by dragging the project_

- Click the **...** (ellipsis) next to the project, then click **Delete**.

![Delete by clicking delete](/assets/delete-click.CI22Llp1.gif)_Click Delete_

## Best practices

- **Organize projects** by department, use case, or project type to create a clear, logical structure. This enables you to efficiently locate and manage related assets.
  
- **Create the target project before importing across workspaces**. Give it the same name as the source project for consistency. Importing a project into **All projects** converts each folder into a separate project.
  

## Home assets project

The **Home assets** project contains assets that were previously stored in your workspace's root folder. It functions just like any other project.

### Home assets project name

Your workspace's **Home assets** project may have one of the following names:

- **Home assets**: your workspace didn't have an existing project with that name.
- **Home assets (migrated)**: your workspace already had a project named **Home assets**, so Workato used this name to avoid a conflict. Collaborator access was preserved without changes.

### API requirements

You must specify a folder when importing or creating assets. Assets can no longer be stored in the root folder.

**Developer API**

- The `folder_id_for_home_assets` parameter is required for the [Import a package into a folder](/en/workato-api/recipe-lifecycle-management#import-package-into-a-folder) endpoint if the target workspace's **Home assets** folder has been converted to a project or the target package contains root folder assets.
  
- The `folder_id` parameter is required for the [Create a connection](/en/workato-api/connections#connections-create), [Create a recipe](/en/workato-api/recipes#create-a-recipe), and [Copy a recipe](/en/workato-api/recipes#copy-a-recipe) endpoints if the target workspace's **Home assets** folder has been converted to a project.
  

**Embedded API**

- The `folder_id_for_home_assets` parameter is required for the [Import package into a customer workspace](/en/oem/oem-api/recipe-lifecycle-management#package-import) endpoint if the target workspace's **Home assets** folder has been converted to a project or the target package contains root folder assets.
  
- The `folder_id` parameter is required for the [Create a connection](/en/oem/oem-api/connections#create-a-connection), [Create recipe in a customer workspace](/en/oem/oem-api/recipes#create-a-recipe), and [Copy recipe in a customer workspace](/en/oem/oem-api/recipes#copy-recipe-in-a-customer-account) endpoints if the target workspace's **Home assets** folder has been converted to a project.

---
