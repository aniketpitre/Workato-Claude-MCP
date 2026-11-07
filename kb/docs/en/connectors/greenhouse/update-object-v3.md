---
url: 'https://docs.workato.com/en/connectors/greenhouse/update-object-v3.md'
description: The Update object (v3) action updates objects in Greenhouse using the v3 API.
---

# Greenhouse - Update object (v3) action

The **Update object (v3)** action updates objects in Greenhouse using the v3 API.

This action is available for OAuth 2.0 connections only.

## Input

Input fields are dynamically generated based on the selected object type. The following fields are required for all object types:

| Input field | Description |
| --- | --- |
| Object | Select the object type to update. For example, **Candidate** or **Job**. |
| ID | Enter the ID of the object to update. |

Additional input fields appear based on the selected object type. For example, selecting **Candidate** displays fields such as **First name** and **Last name**.

Refer to the [Greenhouse v3 object coverage guide](/en/connectors/greenhouse/object-coverage#create-object-v3) for supported objects and field-level details.

## Output

Output fields are dynamically generated based on the selected object type.

For example, selecting **Candidate** returns the following output fields:

| Output field | Description |
| --- | --- |
| ID | ID of the updated object. |
| First name | Updated first name of the candidate. |
| Last name | Updated last name of the candidate. |
| Updated | Indicates whether the object was successfully updated. |

Other object types return their corresponding resource data.

---
