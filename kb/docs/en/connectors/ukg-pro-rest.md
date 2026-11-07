---
url: 'https://docs.workato.com/en/connectors/ukg-pro-rest.md'
description: >-
  Connect UKG Pro to Workato to automate HCM workflows, retrieving HR, payroll,
  talent, and workforce management data across the employee lifecycle.
---

# UKG Pro

[UKG Pro](https://www.ukg.com/solutions/human-capital-management) is a comprehensive Human Capital Management (HCM) platform that offers a single suite for managing HR, payroll, talent, and workforce management, designed to support employee engagement and streamline the entire employee lifecycle across businesses of all sizes.

The UKG Pro connector retrieves data from UKG Pro. Use the [UKG Pro SOAP](/en/connectors/ukg-pro-soap) connector to add or update data in UltiPro.

## Prerequisites

Establishing a connection to UKG Pro in Workato requires the **API base URL** and **Customer API Key** of a UKG Pro service account. Complete the following steps to retrieve your **API base URL** and **Customer API Key**:

1. Go to **Menu > System Configuration > Security > Service Account Administration** in UKG Pro.
   
2. **Add a new service account**
   
   1. Click **Add**.
      
   2. Enter a **Unique user name** that's distinct from any existing user accounts used for portal access.
      
   3. Provide an **Email address** for the service account.
      
   4. The **Generate New Password** option is automatically selected. Click **Save** to generate a random password.
      
   5. Copy and store the password securely.
      
   
   **Modify an existing service account**
   
   1. Click the **User Name** for the service account you plan to modify.
      
   2. Update the account's information as needed.
      
   
3. Specify the account's access levels for each Web Service, such as **Add**, **Delete**, **View**, and **Edit**.
   
4. Go to **System Configuration > Web Services**, then copy and save the **API base URL**.
   
5. Go to **System Configuration > Service Account Administration**, then copy and save the **Customer API Key**.
   

## How to connect to UKG Pro

Complete the following steps to establish a UKG Pro connection:

1. Click **Create** > **Connection**.
   
2. Search for and select **UKG Pro** as your connection in the New connection page.
   
3. Provide a name for your connection in the **Connection name** field. ![UKG Pro connection setup](/assets/connection-setup.B9ZQD7yA.png)_UKG Pro connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your UKG Pro username in the **User name** field.
   
6. Enter your UKG Pro **Password**.
   
7. Enter your base **API URL**. Refer to [Prerequisites](#prerequisites) to generate this URL.
   
8. Enter your **Customer API key**. Refer to [Prerequisites](#prerequisites) to generate this key.
   
9. Click **Connect** to complete the connection.

---
