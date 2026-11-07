---
url: >-
  https://docs.workato.com/en/recipe-development-lifecycle/compare-versions-with-recipe-diff.md
description: >-
  Learn how the Workato Recipe Diff feature visually compares two recipe or
  skill versions so you can review changes side by side.
---

# Using a recipe diff to compare recipe changes

Workato tracks all changes made to recipes and skills. A new version of the skill or recipe is created when the skill or recipe is saved.

The Recipe Diff feature enables you to visually compare two skill or recipe versions and review the changes.

In this guide, we'll cover:

- [How the Recipe Diff feature works](#how-it-works)
- [The types of changes included in Recipe Diffs](#change-types)
- [How to access and use Recipe Diffs](#usage)

* * *

## How it works

Check out this video guide

[Video](https://www.youtube.com/embed/HNKKbPnwg9o)

The Recipe Diff (or difference) feature visually compares any two skill or recipe versions and highlights their differences.

In tools like GitHub, the diff feature shows a text comparison. For example:

![Example of a diff in GitHub](/assets/github-diff.HkViAs-G.png)

In Workato, the Recipe Diff feature shows a visual difference between two skill or recipe versions. Recipe Diffs make it easier to review the changes and discuss them as part of the recipe development lifecycle. For example:

![The Workato Recipe Diff page](/assets/compare-version-screen.BOEfWw_s.png)

How changes are displayed depends on the [type of change](#change-types).

* * *

## Change types

The Recipe Diff feature tracks the following types of recipe changes:

- [Adding a step](#add-step-change-type)
- [Deleting a step](#remove-step-change-type)
- [Moving a step](#move-step-change-type)
- [Nesting or unnesting a step](#nest-unnest-step-change-type)
- [Updating a step's configuration](#updated-step-config-change-type)
- [Skipping or unskipping a step](#skip-unskip-step-change-type)

**Note**: Any combination of the following changes can happen in a single step. For example, a step's position or configuration can change, along with being (un)skipped or (un)nested.

### Adding a step

When a new step is added to a skill or recipe version, the step is highlighted in green:

![Adding a step](/assets/add-step.B7zaIduk.png)

### Deleting a step

When a step is deleted from a skill or recipe version, the step is highlighted in red:

![Deleting a step](/assets/remove-step.CxVk39hy.png)

### Moving a step

When a step is moved in a skill or recipe version, the step is highlighted in blue and a label describing the movement will display:

![Moving a step](/assets/moved-step.C6g039sV.png)

### Nesting or unnesting a step

When a step is nested or unnested in a skill or recipe version, the step is highlighted in blue and a **Nested** or **Unnested** label will display:

![Unnesting a step](/assets/unnested-step.BAbD9lff.png)

### Updating a step's configuration

When a step's configuration is changed, the step is highlighted in blue and an **Updated config** label displays. Furthermore, within the step configuration, field addition, removal, and updates will be displayed.

![Updating a step's configuration](/assets/updated-step-config.B_0452Yy.png)

> **Viewing step-level changes**
> 
> Field updates and datapill changes will display in the diff.
> 
> - Field addition (green)
> - Field removal (red)
> - Field updates (grey) - this includes switching datapills and formulas

### Skipping or unskipping a step

When [a step is skipped or unskipped](/en/recipes/steps/skip-step) in a skill or recipe version, the step is highlighted in blue and a **Skipped** or **Unskipped** label displays:

![Skipping a step](/assets/skipped-step.A8gM-VWK.png)

* * *

## Using diffs

1. Sign in to your Workato account.
   
2. Open a recipe.
   
3. Click the **Versions** tab.
   
4. You can access the Recipe Diff feature in the following ways:
   
   From the Version history page:
   
   1. Check the **checkboxes** of the versions you want to compare:
      
      ![Checking boxes next to versions to compare](/assets/version-checkboxes.DbMGZOZI.png)
      
   2. Click the **Compare VXX and VXX** button:
      
      ![Highlighted compare versions button](/assets/compare-versions-button.DsyYHGAG.png)
      
   
   From the Version details page:
   
   1. Click a skill or recipe version.
      
   2. On the **Version details** page, click **Compare to current version** near the top right corner of the page:
      
      ![Highlighted compare current version button](/assets/compare-current-version-button.C4SlGR01.png)
      
      If you're viewing the current version of the skill or recipe, the button will read **Compare to the previous version**.
      
   
5. The Recipe Diff page will display:
   
   ![The Recipe Diff page](/assets/compare-version-screen.BOEfWw_s.png)
   
   Changes between the versions will be highlighted [depending on their type](#change-types).
   
   You can also use interactions like **Zoom** by right-clicking or using keyboard shortcuts:
   
   ![User interactions in the Recipe Diff page](/assets/user-interactions.iV_s3jyP.gif)
   
6. **To change the versions you're comparing**, use the **Compare from** and **Compare to** menus:
   
   ![The version comparison menus in the Recipe Diff page](/assets/change-versions.CnWw53la.gif)
   
   The comparison views will automatically update with the selected version(s).
