---
url: >-
  https://docs.workato.com/en/connectors/bim360/download-cost-document-in-a-project-action.md
description: >-
  The download cost document in a project action retrieves the file content of a
  BIM 360 cost document you specify.
---

# BIM 360 - Download cost document in a project action

The **Download cost document in a project** action retrieves the file content of a BIM 360 cost document you specify.

## Input

| Input fields | Description |
| --- | --- |
| Hub | Select the hub that contains the cost document you plan to retrieve. |
| Project | Select the project that contains the cost document you plan to retrieve. |
| File URN | Provide the URN of the cost document you plan to download. You can retrieve the URN from the [Get object in a project](/en/connectors/bim360/get-object-in-a-project-action) action's output. |

## Output

| Output fields | Description |
| --- | --- |
| Content | The cost document's file content. |
