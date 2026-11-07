---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/execute-restlet-script-action.md
description: >-
  The Execute RESTlet script action in the NetSuite REST connector lets you
  import or export data by calling a RESTlet script and deployment ID.
---

# NetSuite REST - Execute RESTlet script action

Use this action to export or import data in NetSuite.

Learn more about [NetSuite RESTlet](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4387799403.html#SuiteScript-2.x-RESTlet-Script-Type).

## Input

| Input field | Description |
| --- | --- |
| Operation | Select a RESTlet operation to perform from the picklist. Available operations include **Import** and **Export**. **Export** operations use **GET** methods and **Import** use **POST** HTTP methods to interact with RESTlet APIs. |
| Script ID | Provide the RESTlet script ID to perform the operation. You can get the script ID from within your NetSuite instance in **Customization > Scripting > Scripts > NetSuite script record**. |
| Deployment ID | Provide the RESTlet script deployment ID to perform the operation. Obtain the deployment ID from your NetSuite instance in **Customization > Scripting > Scripts > NetSuite script record > Deployments**. |
| Request URL parameters | Determine what the URL parameters should be and assign values to them. You can set up these parameters in Workato's graphical UI by clicking **Add URL parameter**. Then, provide a **Label**, **Data type**, and **Hint** (optional) in the **Add new field modal**. Alternatively, you can add the request URL parameters manually by providing a JSON description of your schema. |
| Request body parameters | This input field is only available when you perform an **Import** operation. Click **Use JSON** to describe your request body parameters in JSON, or click **add fields manually** to fill out the **Add new field** modal, determining the **Name**, **Label**, **Data type**, whether the parameter is **Optional**, and the **Hint** for each of your parameters. |
| Response type | Determine a response type. You can choose between JSON and plain text. |
| Output schema | Click **Use JSON** to describe all fields in your response using JSON, or click **add fields manually** to fill out the **Add new field** modal, determining the **Name**, **Label**, **Data type**, whether the parameter is **Optional**, and the **Hint** for each of your parameters. |

## Output

This action does not generate any output data for use in downstream recipe steps.
