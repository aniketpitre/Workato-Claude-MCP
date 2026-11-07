---
url: 'https://docs.workato.com/en/connectors/tableau.md'
description: >-
  The Tableau connector lets you automate analytics workflows: refresh
  workbooks, run extract refresh tasks, download views, and search views and
  workbooks.
---

# Tableau

[Tableau](https://www.tableau.com) is a business intelligence and data visualization tool that helps users analyze data to solve problems. It uses visualizations such as charts, graphs, and maps to make data easier to understand. Tableau helps people and organizations be more data-driven.

## Prerequisites

Before using the Tableau connector in Workato, ensure you have an active Tableau account with appropriate permissions to access APIs, then complete the following prerequisite steps:

1. [Access Tableau server administration](#admin)
2. [Add a local user](#local-user)
3. [Authenticate with the REST API](#rest-api)
4. [Create a personal access token](#access-token)

### Access Tableau server administration

Complete the following steps to access Tableau server administration:

1. Sign in to Tableau Server as an administrator.
   
2. If applicable, select the site for which you plan to manage users.
   

### Add a local user

Complete the following steps to add a local user to your Tableau server:

1. Select the site in which you plan to add the user and go to the **Users** section.
   
2. Click **Add Users**, then **Create new user**.
   
3. Enter a **Username** to use as the API user ID.
   
4. Select a site role, such as: **Explorer**, **Viewer**, or **Content Manager**.
   
5. Click **Create User**.
   
6. Set a full name, password, and email address for the user.
   

### Authenticate with the REST API

Complete the following steps to authenticate with the Tableau REST API:

1. Make a [Sign In API request](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_authentication.htm#sign_in) to Tableau's Server REST API. Include the `username` (user ID) and `password` for your [local user](#local-user) in the request body, along with the site content URL (if applicable).
   
2. Include the credentials token returned by the call in subsequent API requests for authentication.
   

### Create a personal access token

Complete the following steps to generate a Tableau personal access token:

1. Go to **Tableau Server Settings > Personal Access Tokens**.
   
2. Enter a descriptive name for your token in the **Token Name** field under **Personal Access Tokens**, then click **Create Token**.
   
3. Click **Copy Secret** in the **Personal Access Token** dialog box.
   
4. Paste the secret to a file and store the file in a safe location.
   
5. Click **Close** when finished.
   

> **PAT LIMITS**
> 
> If you use Tableau Server, you can have up to 10 PATs by default. If you use Tableau Cloud, you can have up to 104 PATs. Refer to the [Personal access token](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-a-personal-access-token) page for more information.

## How to connect to Tableau on Workato

Complete the following steps to establish a connection to Tableau:

1. Click **Create** > **Connection**.
   
2. Search for and select **Tableau** as your connection in the New connection page.
   
3. Provide a name for your connection in the **Connection name** field. ![Tableau connection](/assets/connection.CU9m3Ln0.png)_Tableau connection fields_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select either **Cloud** or **On-prem group** as your **Connection type**.
   
6. Select the **Authentication type** from the drop-down list.
   
7. **Basic authentication**
   
   Enter your Tableau **User name** and **Password**.
   
   **Personal access token authentication**
   
   Enter the **Personal access token name** and **Personal access token secret**.
   
8. Provide the **Server name**. You can find the server name in the Tableau site URL. For example, a server with the name `company.online.tableau.com` will have the URL `https://company.online.tableau.com/#/site/workato/`.
   
9. Enter the **Site name**. You can find the site name in the Tableau site URL. For example, a site with the name `workato` will have the URL `https://company.online.tableau.com/#/site/workato/`.
   
10. Enter the Tableau **API version**.
    
11. Click **Connect** to establish the connection.

---
