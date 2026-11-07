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
