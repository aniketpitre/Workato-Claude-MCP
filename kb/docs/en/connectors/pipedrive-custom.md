---
url: 'https://docs.workato.com/en/connectors/pipedrive-custom.md'
description: Use the Pipedrive connector to automate and manage sales processes.
---

# Pipedrive

[Pipedrive](https://www.pipedrive.com/) is sales CRM and pipeline management software that helps small sales teams manage intricate or lengthy sales processes. It is built to be simple and easy to use, yet powerful.

## Create a Pipedrive app

A Pipedrive app is required to set up a connection in Workato. Complete the following steps to create a Pipedrive app:

1. On your Pipedrive dashboard, click on your profile icon, then on the **Developer hub**.
   
2. Click **Create an app**.
   
3. Select **Private app**.
   
4. Name your app and enter the Workato callback URL: `https://www.workato.com/oauth/callback`
   
5. Click **Save**.
   
6. Toggle all the required **API scopes**.
   
7. Copy the **Client ID** and **Client Secret** and store them securely. These values are required to establish the connection in Workato.
   
8. Click **Save**, then **Change to Live**.
   

## Connection setup

1. Click **Create > Connection** or press C+C.
   
2. Search for and select **Pipedrive** as your connection on the **New Connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
4. Select the project where you plan to store the connection from the **Location** drop-down menu.
   
5. Enter the **Client ID** and **Client secret** for the Pipedrive app you created in the previous steps.
   
6. Enter the **Company domain** of your Pipedrive instance.
   
7. Click **Connect** to complete the setup.
   

> **PREREQUISITES**
> 
> A Pipedrive app is required to set up a connection in Workato. Refer to the [Create a Pipedrive app](#creating-an-app) section to create an app in Pipedrive.

---

---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/new-or-updated-record-trigger.md
description: >-
  The New/updated record trigger monitors Pipedrive for newly created or updated
  records.
---

# Pipedrive - New/updated record trigger

The **New/updated record trigger** monitors Pipedrive for newly created or updated records.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to monitor for new or updated instances. |
| Trigger poll interval | Select how frequently to check for new objects. |
| When first started, this recipe should pick up events from | Select a start date and time to retrieve trigger events. This enables your recipe to capture past events. This value cannot be changed after the recipe has been run or tested. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The **New/updated record** trigger's output fields vary based on your selected **Object** type. The following output table uses a **User** object as an example:

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the object. |
| Name | The name of the object. |
| Default currency | The default currency for the object. |
| Locale | The language locale for the object. |
| Language | The language for the object. |
| Email | The object's attached email. |
| Phone | The object's attached phone number. |
| Activated | Indicates whether the object is active or not. |
| Last login | A timestamp indicating the user's last login time. |
| Created | A timestamp indicating the creation date of the object. |
| Modified | A timestamp indicating the time the object was last modified. |
| Has created company | Indicates whether this user has created a company. |
| Access | The access roles set for this user. |
| Active flag | Indicates whether the user is active in real-time on the platform. |
| Timezone | The timezone where the user is located. |
| Timezone offset | Difference between the GMT and the user’s timezone. |
| Role ID | A unique identifier for the primary role of this user. |
| Is admin | Indicates whether the user is an admin. |
| Icon URL | The URL of the icon set for this user. |
| Is you | Indicates whether the API requester and the user who caused the trigger event are the same. |
| Is deleted | Indicates whether this object was deleted. |

---
