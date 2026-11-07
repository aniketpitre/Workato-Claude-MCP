---
url: 'https://docs.workato.com/en/connectors/greenhouse/create-object-v3.md'
description: The Create object (v3) action creates objects in Greenhouse using the v3 API.
---

# Greenhouse - Create object (v3) action

The **Create object (v3)** action creates objects in Greenhouse using the v3 API.

This action is available for OAuth 2.0 connections only.

## Input

Input fields are dynamically generated based on the selected object. The following field is required for all object types:

| Input field | Description |
| --- | --- |
| Object | Select the object type to create. For example, **Candidate** or **Job**. |

Additional input fields appear based on the selected object. For example, selecting **Candidate** displays fields such as **First name** and **Last name**.

Refer to the [Greenhouse v3 object coverage guide](/en/connectors/greenhouse/object-coverage#create-object-v3) for supported objects and field-level details.

## Output

Output fields are dynamically generated based on the object you select. For example, selecting **Candidate** returns the following output fields:

| Output field | Description |
| --- | --- |
| Candidate | The created candidate object. |
| Application | The associated application object, if applicable. |

Other object types return their corresponding resource data.

---
