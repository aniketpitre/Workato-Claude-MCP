---
url: 'https://docs.workato.com/en/connectors/ukg-pro-soap.md'
description: >-
  The UKG Pro (SOAP) connector enables you to add or update data in UKG Pro
  using the SOAP API.
---

# UKG Pro (SOAP)

[UKG Pro](https://www.ultimatesoftware.com/hcm-solutions) is a Human Capital Management (HCM) tool that helps enterprises manage the entire employee life cycle. This connector allows you to automate the recruitment, employee onboarding, and employee offboarding processes.

The UKG Pro SOAP connector allows you to add or update data in UltiPro. Use the [UKG Pro connector](/en/connectors/ukg-pro/overview) to retrieve data.

## Prerequisites

Workato recommends using an Integration System User (ISU), such as a dedicated service account, for integration with Workato. This ensures that permissions are consistent and all operations are logged on a single account.

Ensure you have an active UKG Pro account with the **View** and **Personal Integration** permissions at a minimum. If permissions are not configured correctly, actions may not work as intended, even if the connection is successful.

To use employee objects, Workato recommends enabling the following view, add, and edit permissions:

- Personnel Integration
- Employee global new hire
- Employee new hire
- Employee contacts
- Employee job
- Employee compensation
- Employee employment information
- Employee person
- Employee address
- Employee phone information
- Employee User Defined Fields
- Employee Termination

Refer to the [UKG Pro service account documentation](https://learningcenter.ultimatesoftware.com/a/179488) for more information about creating a UKG Pro (SOAP) service account and configuring permissions.

## How to connect to UKG Pro (SOAP)

Complete the following steps to connect Workato to UKG Pro (SOAP):

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **UKG Pro (SOAP)** as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your **User name**. Refer to the [UKG Pro service account documentation](https://learningcenter.ultimatesoftware.com/a/179488) for more information about creating a UKG Pro (SOAP) service account.
   
6. Enter your **Password**.
   
7. Enter your base **API URL**. For example, if the login endpoint is `http://service.ultipro.com/services/LoginService`, the base API URL is `http://service.ultipro.com`.
   
8. Enter your **Customer API key** for the master company.
   
9. Enter your **User API key** for the service account.
   
10. Select the **Service** you plan to use from the drop-down menu.
    
11. Click **Connect** to establish the connection.
    
    ![UKG Pro (SOAP) connection](/assets/connection.BWugjDJf.png)_Create a UKG Pro (SOAP) connection_
    

## Permissions

Ensure that your API credential has the necessary permissions. If permissions are not configured correctly, actions may not work as intended, even if the connection is successful.

To use employee objects, Workato recommends enabling the following view, add, and edit permissions:

- Personnel Integration
- Employee global new hire
- Employee new hire
- Employee contacts
- Employee job
- Employee compensation
- Employee employment information
- Employee person
- Employee address
- Employee phone information
- Employee User Defined Fields
- Employee Termination

---
