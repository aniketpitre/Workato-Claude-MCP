---
url: 'https://docs.workato.com/en/connectors/hibob.md'
description: >-
  The HiBob connector lets you automate HR workflows: create, update, search,
  and delete records, manage employees, and trigger on new events.
---

# HiBob

[HiBob](https://www.hibob.com/) is a people management platform that offers fast-growing companies powerful tools to manage a modern workforce, increase productivity, and improve employee experience.

## Prerequisites

You must have the following information to establish a connection to HiBob in Workato:

- Service User ID
- Service User Token You must be an **Admin** or have the following privileges to create service users: **Features > Integrations > Automation > Create/update/delete the integration.**

Complete the following steps to generate credentials for connection setup between Workato and HiBob:

1. Click **Bob products > System settings** to add a new service user.
   
2. Select **Integrations** in the side navigation menu.
   
3. Use the **All categories** drop-down menu to select **Automation**.
   
4. Go to the **Service users** tile and click **Manage**.
   
5. Click **\+ New service user**.
   
6. Enter a name in the **Display name** field and optionally provide a description in the **Description** field. ![HiBob Service User](/assets/service-user.SnHyEXLc.png)_HiBob Service User_
   
7. Click **Next**. The Service user info modal displays with the new API service user's ID and token.
   
8. Go to **Credentials** and copy the **ID** and **Token** values. Save the values in a file or a safe place in your environment. ![HiBob Service User info](/assets/service-user-info.2m-lqUlS.png)_HiBob Service User info_
   
9. Go to **Permissions > permission groups** to [create a service user permission group](https://help.hibob.com/hc/en-us/articles/27875098648465-Manage-service-users#h_01JB9DYK9SNFAABHWCDBCNTJSQ) and assign it to the service user you created in the preceding steps.
   
10. Click **Done**.
    
11. Follow the [HiBob instructions to set the permissions](https://apidocs.hibob.com/docs/api-service-users#step-3-set-permissions) for the user.
    

> **HIBOB ADMIN ACCESS**
> 
> Ask a Bob Admin to generate credentials for you if you don't have direct access.

## How to connect to HiBob

Complete the following steps to establish a connection with HiBob:

1. Click **Create** > **Connection**.
   
2. Search for and select **HiBob** as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field. ![HiBob Connection](/assets/connection.DM1EQgqq.png)_HiBob Connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Provide the **Service user ID** and **Service user token** in the respective fields, generated in the previous steps.
   
6. Select the suitable **Environment** from the drop-down menu.
   
7. Provide the Partner token in the respective field if you have a partner account. You can obtain the Partner token by logging in to your **Partner Stack account** and going to **HiBob Program > My Profile > Partner-Token.**
   
8. Click the **Connect** button to establish the connection.

---
