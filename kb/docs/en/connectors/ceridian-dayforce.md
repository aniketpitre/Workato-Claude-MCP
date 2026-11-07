---
url: 'https://docs.workato.com/en/connectors/ceridian-dayforce.md'
description: ' Ceridian Dayforce is a global human capital management (HCM) platform that combines payroll, HR, benefits, talent, and workforce management in a single application.'
---

# Ceridian Dayforce

[Ceridian Dayforce](https://www.dayforce.com/) is a global human capital management (HCM) platform that combines payroll, HR, benefits, talent, and workforce management in a single application.

## Install Ceridian Dayforce from the community library

Complete the following steps to install the Ceridian Dayforce connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Ceridian Dayforce connector supports the following authentication types:

- [Basic authentication](#basic-auth)
- [Token-based authentication](#token-auth)

### Basic authentication

Use basic authentication when developing lightweight integrations, testing API endpoints, or performing server-to-server data transfers in Ceridian Dayforce.

#### Ceridian Dayforce setup

Complete the following steps to set up Ceridian Dayforce for basic authentication:

1. Enable web services for Ceridian Dayforce.
   
   1. Go to **System Admin > Roles**.
      
   2. Select the role associated with your Ceridian Dayforce user account.
      
   3. Go to **Features > HCM Anywhere > Web Services**.
      
   4. Select the checkboxes to enable **Web Services**, and minimally, **Read Data**.
      
   5. Click **Save**, and then **Refresh**.
      
2. Retrieve your company short name from Ceridian Dayforce.
   
   1. Log in to your Ceridian Dayforce account.
      
   2. Go to **Company > Settings > General**.
      
   3. Get your company short name from the **Client namespace** field.
      

## How to connect to Ceridian Dayforce

Complete the following steps to establish a Ceridian Dayforce connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Ceridian Dayforce** as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Select the **Basic authentication** from the **Authentication type** drop-down menu.
   
6. Enter the sub domain of your Dayforce account in the **sub domain** field. For example, if your Dayforce account URL is `sandbox.dayforcehcm.com`, the sub domain is `sandbox`.
   
7. Enter your client namespace in the **Client namespace** field.
   
8. Select the version of Ceridian Dayforce you plan to use in the **Version** field.
   
9. Select the time zone for the Dayforce application in the **Dayforce time zone** field.
   
10. Enter your Ceridian Dayforce web services account user name in the **User name** field.
    
11. Enter your Ceridian Dayforce web services account password in the **Password** field.
    
12. Click **Connect**.
    

### {Authentication method 2 name} authentication

Use token-based authentication when authenticating API integrations, setting up automated data transfers, or allowing third-party applications to access system data in Ceridian Dayforce.

#### Ceridian Dayforce setup

Complete the following steps to set up Ceridian Dayforce for token-based authentication:

1. Enable web services for Ceridian Dayforce.
   
   1. Go to **System Admin > Roles**.
      
   2. Select the role associated with your Ceridian Dayforce user account.
      
   3. Go to **Features > HCM Anywhere > Web Services**.
      
   4. Select the checkboxes to enable **Web Services**, and minimally, **Read Data**.
      
   5. Click **Save**, and then **Refresh**.
      
2. Identify your client namespace. The client namespace is the identifier associated with your organization in your Ceridian Dayforce login URL.
   
3. Determine your identity/token endpoint. The endpoint is different for production and test environments.
   
   - Production: [https://dfid.dayforcehcm.com/connect/token](https://dfid.dayforcehcm.com/connect/token)
   - Test: [https://dfidtst.np.dayforcehcm.com/connect/token](https://dfidtst.np.dayforcehcm.com/connect/token)

---

---
url: >-
  https://docs.workato.com/en/connectors/ceridian-dayforce/new-updated-employee-trigger.md
description: >-
  The New/updated employee trigger activates when an employee is created or
  updated in Ceridian Dayforce.
---

# Ceridian Dayforce - New/updated employee trigger

The **New/updated employee** trigger activates when an employee is created or updated in Ceridian Dayforce.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for new events. Defaults to minutes if left blank. Minimum value allowed is minutes. Refer to [Polling intervals](https://docs.workato.com/en/recipes/polling-intervals.html) for more information. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| XRefCode | The external reference codes for the new/updated employees returned in your search. |

---

---
url: >-
  https://docs.workato.com/en/connectors/ceridian-dayforce/get-employee-action.md
description: >-
  The Get employee action retrieves the HR details of a specified employee in
  Ceridian Dayforce.
---

# Ceridian Dayforce - Get employee action

The **Get employee** action retrieves the HR details of a specified employee in Ceridian Dayforce.

## Input

| Input field | Description |
| --- | --- |
| Employee XRefCode | Enter the unique identifier of the employee to retrieved. The value must match exactly. |
| Context date | Select the date and time to retrieve employees. |
| Sub entities | Select relevant sub entities to improve performance. All sub entities are returned if left blank. |
| Context date range from | Select the date and time to start retrieving employees from. Defaults to null if left blank. |
| Context date range to | Select the date and time to stop retrieving employees from. Defaults to null if left blank. |

## Output

This action has many output fields. Refer to the [Ceridian Dayforce](https://developers.dayforce.com/Special-Pages/Welcome-Page.aspx) documentation for a complete list of output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/ceridian-dayforce/search-employees-action.md
description: >-
  The Search employees action returns a list of employees that match your search
  criteria in Ceridian Dayforce.
---

# Ceridian Dayforce - Search employees action

The **Search employees** action returns a list of employees that match your search criteria in Ceridian Dayforce. Use the start date and end date input fields together for hired, updated and, terminated employees.

## Input

| Input field | Description |
| --- | --- |
| Employee number | Enter the ID of the employee you plan to search for. You can use a partial employee ID value for a broader search. |
| Display name | Enter the employee name you plan to search for. |

This action has many input fields. Refer to the [Ceridian Dayforce](https://developers.dayforce.com/Special-Pages/Welcome-Page.aspx) documentation for a complete list of input fields.

## Output

| Output field | Description |
| --- | --- |
| XRefCodes | The external reference codes for the employees returned in your search. |

---
