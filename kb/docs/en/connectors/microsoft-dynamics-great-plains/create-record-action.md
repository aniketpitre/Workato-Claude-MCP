---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/create-record-action.md
description: The Create record action creates a new record in Microsoft Dynamics GP.
---

# Microsoft Dynamics Great Plains - Create record action

The **Create record** action creates a new record in Microsoft Dynamics GP. Select the object to create to generate the relevant fields for that object. For example, the following are the input and output schemas if you select **Post bank deposit** as the object:

## Input

| Input field | Description |
| --- | --- |
| DB connection string | Enter the database connection string to use for the action. |
| Checkbook ID | Provide the ID of the checkbook for the bank deposit. |
| Deposit number | Provide the deposit number for posting. |
| Requester transaction | Select whether to populate the requester shadow table. |
| User ID for posting | Provide the user ID for posting. |
| User-defined fields 1-5 | Provide additional information in these fields, which are for developer use only. |

## Output

| Output field | Description |
| --- | --- |
| Create entity result | The status of the **Create record** action. |
