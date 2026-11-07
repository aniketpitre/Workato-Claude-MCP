---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/update-record-action.md
description: The Update record action updates a new record in Microsoft Dynamics GP.
---

# Microsoft Dynamics Great Plains - Update record action

The **Update record** action updates a new record in Microsoft Dynamics GP. Select the object to update to generate the relevant fields for that object. For example, the following are the input and output schemas if you select **Country code** as the object:

## Input

| Input field | Description |
| --- | --- |
| DB connection string | Enter the database connection string to use for the action. |
| Country code | Enter the standard country code representing the country. |
| Country code description | Provide a short description or name of the country corresponding to the country code. |
| EU member | Indicate whether the country is a member of the European Union. |
| Update if exists | Indicate whether to update the existing record if the provided country code is already in use. |
| Requester transaction | Select whether to populate the requester shadow table. |
| User-defined field 1-5 | Use these fields to capture any additional custom information needed for your use case. |

## Output

| Output field | Description |
| --- | --- |
| Update entity result | The status of the **Update record** action. |
