---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-troubleshoot-runtime.md
description: Troubleshoot errors that occur when you use Workflow apps.
---

# Troubleshoot Workflow apps errors

Use this guide to troubleshoot errors that occur when you use Workflow apps.

## Error on import of Workflow apps project

The browser console displays the following error when you can't import a Workflow apps project from one workspace to another:

```bash
"error": "App configuration can be imported only into project"
```

This error occurs if the destination workspace doesn't have the same name as the project you're trying to import, or if you select the wrong folder as the import destination.

Complete the [Import a package](/en/recipe-development-lifecycle/import#import-a-package) procedure. Ensure that the destination project name matches the name of the project in the source workspace.
