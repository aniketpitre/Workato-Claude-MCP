---
url: 'https://docs.workato.com/en/recipes/tags.md'
description: >-
  Learn how tags in Workato categorize assets to organize and filter them across
  projects.
---

# Tags for assets

Tags are labels you apply to assets to add context and group them across projects. You can filter and search by tag to find assets that share an attribute.

> **TAG LIMITS**
> 
> Tags are subject to the following quotas:
> 
> | Description | Quota |
> | --- | --- |
> | Maximum number of tags in a workspace | 1,000 |

![Tags for assets](/assets/asset-tags.DiTviNCI.png)_Tags for assets_

## How tags improve asset management

Tags enhance asset organization by offering flexibility in categorization and search capabilities, by providing the following workflow enhancements:

- Organize assets across projects
  
- Group assets based on shared attributes, enabling effective management across project boundaries.
  
- Streamline search and filtering
  
- Locate assets by filtering based on tags, simplifying the search process.
  
- Provide better context
  
- Add context, clarifying the purpose or category of an asset at a glance and improving workspace organization.
  

## Tag management permissions

Tag management is controlled through workspace settings. Collaborators with the [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role, a custom environment role with the [Workspace access privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#workspace-access), or the legacy [Admin system role](/en/roles#system-roles) can configure which users can create, edit, and delete tags. The following permissions apply based on your configuration:

- **View tags**: Any user in the workspace can view tags.
- **Manage tags**: Admins and users with WS permissions can create, edit, and delete all tags across the workspace.
- **Create and manage personal tags**: Any user can create, edit, or delete their own tags if the **Restrict tag management** toggle is disabled. If enabled, only admins and users with WS permissions can manage tags.
- **Apply or remove tags**: Users with asset edit permissions can apply or remove tags on assets they can edit.

Ensure the appropriate permissions are set to allow the necessary users to manage tags effectively.

### Configure tag management permissions

Complete the following steps to configure tag management permissions:

1. Navigate to **Workspace admin > Settings > Workspace > Tags**.
   
   ![Manage tag permissions](/assets/tag-permissions.inQA8l9I.png)_Manage tag permissions_
   
2. Configure the **Restrict tag management** toggle. This setting controls who can manage tags in your workspace:
   
   - **OFF**: Allows all users to create, edit, or delete their own tags. Admins and users with workspace settings (WS) permissions can manage all tags, including those created by other users.
   - **ON**: Only admins or users with WS permissions can create, edit, or delete tags. Users with asset edit permissions can apply or remove tags on assets they can edit but cannot create, update, or delete tags.
3. Click **Save** to apply your configuration. The permissions are now set according to your selection.
   

## Create and apply tags

Ensure you have the necessary [permissions](#tag-management-permissions) before creating or applying tags across your assets. You can apply tags to assets using two primary methods:

**Apply tags from the assets or project page**

Complete the following steps to apply or create tags for an asset from the **Assets** or **Projects** page:

1. Navigate to the **Assets**, **Projects**, or mixed assets page.
   
2. Locate the asset for which you plan to apply or create a tag.
   
3. Click **Apply tags** next to the asset.
   
   ![Apply tags](/assets/apply-tags.CpRIiEwc.png)_Apply tags_
   
4. Select multiple tags from the list of existing tags, or type a new tag name. If no matching tag is found, click **Create** to add the new tag. You can add multiple tags to the asset.
   
   ![Create a new tag](/assets/create-tag.nclc3TbG.png)_Create a new tag_
   
5. Alternatively, click the `+` (plus) button to open a dialog for creating a new tag with a name, description, and color.
   
   ![Create a new detailed tag](/assets/create-detailed-tag.CG24sKny.png)_Create a new detailed tag_
   

**Apply tags from the asset’s detailed view**

Complete the following steps to apply or create tags from the detailed view of an asset:

1. Go to the **Assets**, **Projects**, or mixed assets page.
   
2. Locate the asset for which you plan to apply or create a tag.
   
3. Click the asset to open its detailed view.
   
4. Go to the **Tags** section on the sidebar.
   
5. Click **Apply tags** next to the asset.
   
   ![Apply tags](/assets/apply-tags-view.deaJqSeT.png)_Apply tags_
   
6. Select multiple tags from the list of existing tags, or type a new tag name. If no matching tag is found, click **Create** to add the new tag. You can add multiple tags to the asset.
   
   ![Create a new tag](/assets/create-tag.nclc3TbG.png)_Create a new tag_
   
7. Alternatively, click the `+` (plus) button to open a dialog for creating one or more new tags with a name, description, and color.
   
   ![Create a new detailed tag](/assets/create-detailed-tag.CG24sKny.png)_Create a new detailed tag_
   

## Edit tags on an asset

Ensure you have the necessary [permissions](#tag-management-permissions) before editing tags across your assets. You can edit existing tags for a selected asset by adding, removing, or modifying them using two primary methods:

**Edit tags from the assets or project page**

Complete the following steps to edit tags for an asset from the **Assets** or **Projects** page:

1. Go to the **Assets**, **Projects**, or mixed assets page.
   
2. Locate the asset for which you plan to edit tags.
   
3. Click the asset card's tags section to enter edit mode.
   
   ![Edit tags](/assets/modify-tags._rwQxs4z.png)_Edit tags_
   
4. Review the list of tags applied to the asset.
   
   ![Review tags](/assets/review-tags.BJg71Yqc.png)_Review tags_
   
5. Choose from the following options:
   
   - Select additional tags from the list to assign to the asset.
   - Deselect tags to remove them from the asset.
   - Search for or create new tags as needed.

**Edit tags from the asset’s detailed view**

Complete the following steps to edit tags from the detailed view of an asset:

1. Go to the **Assets**, **Projects**, or mixed assets page.
   
2. Locate the asset for which you plan to edit tags.
   
3. Click the asset to open its detailed view.
   
4. Go to the **Tags** section on the sidebar.
   
5. Click **Edit** tags to manage the existing tags.
   
   ![Edit tags](/assets/modify-tags-view.CcG99KwD.png)_Edit tags_
   
6. Review the list of tags applied to the asset.
   
   ![Review tags](/assets/review-tags-view.ByA1p1et.png)_Review tags_
   
7. Choose from the following options:
   
   - Select additional tags from the list to assign to the asset.
   - Deselect tags to remove them from the asset.
   - Search for or create new tags as needed.

## Manage tags

Ensure you have the necessary [permissions](#tag-management-permissions) before managing tags. Complete the following steps to manage your tags:

1. Navigate to **Workspace admin > Settings > Workspace > Tags**.
   
2. Click **Manage tags** to open the tag management page.
   
   > **WORKSPACE-LEVEL TAGS**
   > 
   > Tags are managed at the workspace level and are consistent across all workspaces within the organization.
   
   ![Manage tags setting](/assets/manage-settings.DB_g_BPG.png)_Manage tags setting_
   
3. Create new tags, edit existing ones, or delete tags as needed.
   
   > **SOFT DELETED RECIPES**
   > 
   > Recipes use a soft delete strategy, allowing you to restore deleted recipes. When a recipe is deleted, its tags are not removed and are automatically restored with the recipe.
   
   ![Manage tags](/assets/manage-tags.DteuAdAO.png)_Manage tags_
   

## Manage tags directly from assets

You can also manage tags from specific assets using the following methods:

**Manage tags from the asset card**

You can access the **Manage tags** settings from the asset card on the mixed asset or project page.

![Manage tags](/assets/manage-tags-card.Cxy1-EyF.png)_Manage tags from the asset card_

**Manage tags from the detailed asset page**

You can access the **Manage tags** settings from the detailed view of a recipe or connection.

![Manage tags](/assets/manage-tags-detailed.CHtmU9Wz.png)_Manage tags from the detailed asset page_

## Filter by tags

Tags organize assets into categories, enhancing search and filtering capabilities. Complete the following steps to filter assets by tags:

1. Navigate to the **Assets** or **Projects** page.
   
2. Locate the **Tags** filter.
   
3. Select one or more tags from the multi-select menu.
   
   ![Select tags](/assets/select-tags.AuHJDz6T.png)_Select tags_
   
4. Click **Apply** to filter the assets by the selected tags.
   
5. Alternatively, use the keyboard shortcut Command (Mac) or Ctrl (Windows) and click a tag to filter assets for the selected tag.
   

The page automatically updates to display assets that match the selected tags.

![Filter tags](/assets/filter-tags.DMlqoinH.png)_Filter tags_

---
