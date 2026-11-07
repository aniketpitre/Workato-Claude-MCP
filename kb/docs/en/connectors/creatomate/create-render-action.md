---
url: 'https://docs.workato.com/en/connectors/creatomate/create-render-action.md'
description: >-
  The Create render action enables you to create a render from a template or
  RenderScript and wait for it to complete in Creatomate.
---

# Creatomate - Create render action

The **Create render** action creates a render from a template or from RenderScript, and waits until the render succeeds or fails in Creatomate. The action times out if the render doesn't finish in 60 minutes. Queued renders keep running and can be checked afterward with the [Get render status action](/en/connectors/creatomate/get-render-status-action).

## Input

Input fields are dynamically generated based on the object you select. The following input field is common to all objects. Refer to the [Creatomate](https://creatomate.com/docs/api/reference/introduction) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object | Select the object type you plan to update. For example, `Template` or `RenderScript`. |

## Output

Output fields are dynamically generated based on the object you select. Refer to the [Creatomate](https://creatomate.com/docs/api/reference/introduction) documentation for more information on available output fields.

---
