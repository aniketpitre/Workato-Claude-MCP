---
url: 'https://docs.workato.com/en/connectors/stacklet/mutate-records-action.md'
description: >-
  The Mutate records action creates, updates, or deletes one or more records in
  Stacklet.
---

# Stacklet - Mutate records action

The **Mutate records** action creates, updates, or deletes one or more records in Stacklet.

## Input

Input fields load dynamically based on the object you select. For example, if you select **Update current user**, the following input fields are available.

| Input field | Description |
| --- | --- |
| Mutation | Select the mutation operation to perform. |
| Input | Enter the input for the selected object, such as **Display name**. |
| Fields to retrieve | Select the fields to retrieve in the mutate records action. Retrieving specific fields improves performance. All fields are returned if left blank. |
| Sub queries | Select sub query records to retrieve. |
| Permissions | Enter additional permissions for the selected object, such as **Fields to retrieve**. |

## Output

The output fields load dynamically based on the object you select. For example, if you select **Update current user**, the following output fields are available.

| Output field | Description |
| --- | --- |
| Name | The name of the updated user. |
| Display name | The name of the updated user that is displayed. |
| Email | The email associated with the updated user. |
| Role assignment principal | The role assignment principal for the updated user. |
| Permissions | The user's permissions. |

---
