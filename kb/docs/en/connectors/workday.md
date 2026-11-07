---
url: 'https://docs.workato.com/en/connectors/workday.md'
description: >-
  The Workday connector lets you automate HR and finance workflows: read and
  update business and custom objects, run reports, and trigger on object
  changes.
---

# Workday

[Workday](https://www.workday.com/) offers cloud-based financial management and human capital management software. It combines finance and HR functionalities, enhancing business performance and providing deeper insights into organizational data.

Workday provides three primary types of services for data orchestration:

- Workday Web Services
  
- Provides a set of Simple Object Access Protocol (SOAP) APIs that enable users to read and write data in and out of Workday.
  
- Workday REST
  
- Offers REST APIs primarily used for manipulating custom objects.
  
- Workday Report-as-a-Service (RaaS)
  
- Allows you to extract data from custom reports that are web service enabled.
  

Workato uses these services to create powerful integration scenarios and sync data between your Workday instance and other cloud applications.

## Workday Approved

![Workday Approved Badge](/assets/workday-approved-badge.Cs5G6TSu.png)_Workday Approved Badge_

Our Workday connector is **Workday Approved** for all HR Onboarding/HCM use cases.

## Use cases

Integrate Workday with your business applications to automate HR processes and improve workforce management. You can sync employee data, streamline user provisioning, secure access management, and ensure efficient data handling. Explore our [use cases](/en/getting-started/workato-use-cases) to discover how you can optimize your Workday workflows:

- [Provision Jira and Okta users](/en/getting-started/use-cases/workday-jira-okta) for new employees in Workday.
- [Export Workday workers to CSV](/en/getting-started/use-cases/workday-python-google-drive) with Python and upload the file to Google Drive.

## API version

Workato supports the following versions for each of Workday's services:

### Workday Web Services

#### Supported versions

- v46.1
- v45.1
- v44.1
- v42.1

#### Version support policy

- Workato primarily supports even-numbered major version releases (for example, 42 and 44), following Workday's schedule of releasing one major version every six months. However, Workato may support odd-numbered versions when critical functionality isn't available in even-numbered releases. For example, Workday API v45 is supported to enable multiple concurrent jobs for contingent workers.
- Workato generally supports up to three API versions at any given time. In some cases, additional versions may be temporarily supported to accommodate customer requirements or ensure a smooth transition between releases. All connections using removed versions are automatically upgraded to the oldest available version. For example, if versions 42, 44, and 45 are supported and version 46 is added, version 42 may be removed, leaving 44, 45, and 46.
- Workato applies enhancements and bug fixes only to the latest supported version. Previous versions are offered as-is and don't receive updates.
- Workato intends to follow this approach but may adjust support coverage if the annual release cycle doesn't align with customer needs.

### Workday REST

- v1

### Workday Report-as-a-Service (RaaS)

There are no versions associated with the Workday RaaS.

## How to connect to Workday on Workato

### Before connecting to Workday

We recommend that you create an [Integration System User (ISU)](/en/connectors/workday#register-integration-system-user-isu-in-workday) before you integrate your Workday with Workato. An ISU ensures that all integration operations are logged under a designated user, separate from regular workflow processes. This is essential as changes to a regular worker’s security profile or their termination could disrupt integrations reliant on their account. Limit each ISU to a single integration system, such as Workato, for enhanced security.

The Workday REST API requires authentication through an OAuth client setup. You must register a Workday [API client](#register-api-client) if your integration includes Workday **custom objects**.

### Register Integration System User (ISU) in Workday

Your Integration System User (ISU) must be assigned the required permissions to create a successful integration. You may receive a `403` error if your ISU has insufficient permissions.

![403 error](/assets/permission-error-updated.DU_qX7h4.png)_Error message when ISU doesn't have enough permissions_

A `403` error may indicate that the ISU lacks the required domain-level permissions. Refer to the [Grant domain access to security group](#grant-domain-access-to-security-group) section to ensure that your ISU is granted the appropriate permissions.

#### Create an Integration System User (ISU)

Complete the following steps to create an ISU in Workday:

1. Type **Create Integration System User** into Workday's search bar and select the task from the results.
   
   ![Search for Create Integration System User task in Workday](/assets/search-isu-task.CvD1cTHm.png)_Search for **Create Integration System User** task in Workday_
   
2. Enter a username and set a password in the **Create Integration System User** task.
   
   > **ISU USERNAMES**
   > 
   > Spaces in Workday ISU usernames can cause encoding and formatting issues. We strongly recommend that you use underscores (`_`) or hyphens (`-`) instead of spaces.
   
   ![Create integration system user](/assets/create-isu.COdXMj8O.png)_Create Integration System User_
   
3. Set **Session Timeout Minutes** to `0` to prevent the ISU from timing out.
   
4. Ensure that the **Do Not Allow UI Sessions** checkbox isn't selected.
   
5. Go to the **Maintain Password Rules** task.
   
6. Exempt the integration system user from password expiration by adding them to the **System Users exempt from password expiration** field.
   
   ![Exempt ISU user from password expiration](/assets/exempt-isu-user.B7qOvBPQ.png)_Exempt ISU from password expiration_
   

#### Create an integration security group

Complete the following steps to create either an unconstrained or constrained integration system security group and then assign your newly created ISU:

1. Search for **Create Security Group** in Workday and select the corresponding task.
   
   ![Select the Create Security Group task in Workday](/assets/create-security-task.YeKadzO7.png)_Select the **Create Security Group** task in Workday_
   
2. Locate the **Type of Tenanted Security Group** field, and select and name your security group. Workday offers two types of integration system security groups:
   
   - **Integration System Security Group (Unconstrained)**: Allows group members to access all data instances secured by the group.
     
   - **Integration System Security Group (Constrained)**: Grants access to a subset of data instances based on context.
     
   
   ![Choose the security group type in Workday](/assets/create-security-group.PkL3Olo0.png)_Choose the security group type_
   
   Contact your Workday integration partner before selecting an option to ensure that the appropriate security group type is used for your integration.
   
3. Assign members to your newly created security group. You must add the ISU you registered in the preceding steps. You must also specify the organization scope if you plan to use a constrained group.
   
   ![Add ISU to the security group](/assets/edit-security-group.DTIauGb-.png)_Add ISU to the security group_
   
4. Select **Done** to save all changes.
   

#### Grant domain access to security group

Complete the following steps to grant your security group access to the domains required for your integration:

1. Search for **Maintain Permissions for Security Group** in Workday and select the task.
   
   ![Select the Maintain Permissions for Security Group task](/assets/select-permissions-task.BTgc81hJ.png)_Select the **Maintain Permissions for Security Group** task_
   
2. Choose the security group you created from the **Source Security Group** list to modify the permissions.
   
   ![Choose the created security group](/assets/select-security-group.C0SR91o_.png)_Select the created security group_
   
3. Click **OK** to confirm your selection.
   
4. Go to the **Maintain Permissions for Security Group > Domain Security Policy Permissions** tab and assign the necessary permissions for each domain, such as `GET` and `PUT` operations.
   
   ![Assign perissions for each domain](/assets/grant-security-permissions.CT-ho8YI.png)_Assign permissions for each domain_
   
5. Ensure the security group has `GET` permissions for the following domain security policies:
   
   - Integration Process
   - Integration Debug
   - Worker Data: Current Staffing Information
   - Worker Data: Public Worker Reports
6. Click **OK** to apply the permissions.
   
7. Click **Done** to save your changes.
   

#### Activate security policy changes

You must activate permissions you assign to your policy.

Complete the following steps to activate security policy changes:

1. Type **Activate Pending Security Policy Changes** into Workday's search box and select the task.
   
   ![Search for the Activate Pending Security Policy Changes task in Workday](/assets/search-pending-task.DdQWe9jN.png)_Search for the **Activate Pending Security Policy Changes** task_
   
2. Start the **Activate Pending Security Policy Changes** task by entering a reason for your audit in the comment field, then click **OK**.
   
   ![Enter a comment](/assets/enter-comment.Xy_4AYnb.png)_Enter a comment for audit purposes_
   
3. Select the **Confirm** checkbox to complete the task and click **OK**.
   
   ![Create integration system user](/assets/activate-policy-changes.Dlc9M6zj.png)_Activate the policy changes_
   

#### Register a new API client for integrations

This step is required only if you plan to work with custom objects in Workday.

Ensure you meet the following prerequisites before you begin registering a new API client for integrations in Workday:

- You have admin access to your company’s Workday account.
- You are logged in to Workday with your admin credentials.
- You have [authenticated the Integration System User (ISU)](#register-integration-system-user-isu-in-workday) and enabled both GET and View access in Workday.

Complete the following steps to register an API client for integrations in Workday:

1. Search for **Register API Client for Integrations** in Workday's search field.
   
   ![Select the Register API client for integrations task](/assets/search-api-task.B5dZMe78.png)_Select the **Register API client for Integrations** task_
   
2. Select the **Register API Client for integrations** task to access the registration page.
   
   ![Register API client for integrations](/assets/select-api-task.C8wiEHh_.png)_Register API client for integrations_
   
3. Enter a name for your API client in the **Client Name** field.
   
4. Select the **Non-Expiring Refresh Tokens** option.
   
5. Specify the scope of access for the API client. Ensure to include the `Integration` scope, which covers essential domain security policies such as `Integration Build`, `Integration Debug`, `Integration Process`, and `Integration Event`. Including this scope is a minimum requirement for establishing a connection with Workday, in addition to any specific call operations required for your integration.
   
6. Click **OK** to generate the **Client ID** and **Client Secret**.
   
   ![Generate API client credentials](/assets/generate-client._M_58o0v.png)_Generate API client credentials_
   
7. Save the **Client Secret** and **Client ID**.
   
8. Click **Done**.
   

#### Generate a non-expiring refresh token

Complete the following steps to create a non-expiring refresh token for your API client:

1. Type **View API Clients** in the search field in Workday.
   
2. Open the **View API Clients** report from the search results.
   
   ![Access the report](/assets/select-client-report.Bx3EeGJP.png)_Access the **View API Clients** report_
   
3. Go to the **API Clients for Integrations** tab.
   
4. Select the API client you registered in the preceding steps.
   
5. Click the ellipsis (...) next to the client name and choose **API Client > Manage Refresh Tokens for Integrations** for token management.
   
   ![Select the option to manage refresh tokens](/assets/select-refresh-tokens.D4juyDGq.png)_Manage refresh tokens for the API client_
   
6. Input the Workday account of a user authorized to access the custom report in the **Workday Account** field.
   
   ![Input an authorized Workday account](/assets/enter-workday-account.C0JVnxwc.png)_Enter an authorized Workday account_
   
7. Click **OK**.
   
8. Go to the **Delete or Regenerate Refresh Token** page and select the **Generate New Refresh Token** option.
   
   ![Generate a new refresh token](/assets/select-token-option.CwGIcYjE.png)_Generate a new refresh token_
   
9. Click **OK**.
   
10. Copy the refresh token from the **Successfully Regenerated Refresh Token** page.
    
    ![Copy the generated refresh token](/assets/copy-token.CcZ3RE6F.png)_Copy the generated refresh token_
    
11. Click **Done** to complete the process.
    

#### Find your token endpoint URL

Complete the following steps to find your token endpoint URL in Workday:

1. Enter **View API Clients** into the search field in Workday.
   
2. Access the **View API Clients** report from the search results.
   
3. Save the URLs listed in the **Token Endpoint** and **Authorization Endpoint** fields. These URLs are required for the OAuth 2.0 connection.
   
   ![Save the token endpoint and authorization endpoint URLs](/assets/save-url.BkmumQyc.png)_Save the token endpoint and authorization endpoint URLs_
   

### Setting up the connection to Workday

The Workato Workday connector is categorized into three distinct types: the main Workday connector, the Workday Web Services connector, and the Workday REST connector. Each type follows a similar authentication pattern but differs slightly in support capabilities and functionalities.

#### Connection setup using OAuth 2.0 authentication

Complete the following steps to configure your Workday connection in Workato using OAuth 2.0 authentication:

OAuth 2.0 authentication is required if you plan to work with the Workday REST API or custom objects. We recommend that you avoid using the deprecated **Hybrid** authentication method.

1. Enter a unique **Connection name** to identify your Workday account in Workato.
   
   ![Workday connection](/assets/workday-connection-setup-oauth.rU2iQ_Y6.png)_Label your connection_
   
2. Use the **Location** drop-down to select the project or folder to store this connection.
   
3. Choose **OAuth 2.0** as the **Authentication type**. This method is required for working with custom objects and for querying data using Workday Query Language (WQL) with the Workday REST API.
   
4. Select the **Workday web services version** appropriate for your Workday tenant. We recommend choosing the newest version available for access to the latest features and updates.
   
5. Locate and enter your **Tenant ID**. You can find your tenant ID in your Workday URL. For example, your tenant ID is `sample_company` if your URL is `https://impl.workday.com/sample_company/d/home.htmld`.
   
6. Provide the **WSDL URL** associated with your Workday services.
   
7. Enter the **Client ID** and **Client Secret** from your API client settings.
   
8. Provide your **Refresh token** if using an API client for integrations.
   
9. Enter your **Authorization endpoint** and **Token endpoint** from your API Client settings to complete the OAuth flow.
   
10. Select the **Workday tenant timezone** that matches your Workday tenant's settings. Workday uses Pacific Standard Time (PST) by default.
    
11. Click **Advanced settings** to configure the **Advanced XML payload for multiple ID values**.
    
    Workato wraps each value in fields with multiple values within its own container by default when constructing the XML from your input.
    
    For example:
    
    ```
    <languages><language>english</language></languages><languages><language>chinese</language></languages>
    ```
    
    Workato unwraps these values and presents them in a single container if you set the value to **Yes**:
    
    ```
    <languages><language>english</language><language>chinese</language></languages>
    ```
    
    Consider enabling this when you encounter invalid payload errors.
    
12. Review the information you entered to ensure it is correct.
    
13. Click **Connect** to initiate the authorization process and complete the connection setup.
    

#### Connection setup using basic authentication

Complete the following steps to set up your Workday connection in Workato with basic authentication:

1. Enter a unique **Connection name** to identify your Workday account in Workato.
   
   ![Workday connection](/assets/workday-connection-setup-basic-updated.B1rcozBp.png)_Label your connection_
   
2. Use the **Location** drop-down to select the project or folder to store this connection.
   
3. Select **Basic** as the **Authentication type**. This method uses your Workday username and password for integration.
   
4. Locate and enter your **Tenant ID**. You can find your tenant ID in your Workday URL. For example, your tenant ID is `sample_company` if your URL is `https://impl.workday.com/sample_company/d/home.htmld`.
   
5. Provide the **WSDL URL** associated with your Workday services.
   
6. Provide your Workday **Login name** and **Password**.
   
7. Select your **Workday tenant timezone** that matches your Workday tenant's settings. Workday uses Pacific Standard Time (PST) by default.
   
8. Click **Advanced settings** to configure the **Advanced XML payload for multiple ID values** if required. Fields with multiple values are wrapped within a container by default. Set this option to `yes` to unwrap the values.
   
9. Review the information you entered to ensure it's correct.
   
10. Click **Connect** to initiate the authorization process and complete the connection setup.
    

## What's next

More details on the capabilities of the Workday connector can be found in the following sections:

### Triggers

- [New/updated business object trigger](/en/connectors/workday/new_updated_object)
- [New/updated business object batch trigger](/en/connectors/workday/new_updated_object_batch)
- [Scheduled report trigger](/en/connectors/workday/scheduled_report)
- [Scheduled report using WQL trigger](/en/connectors/workday/scheduled_report_using_wql)

### Actions

- [Call operation action](/en/connectors/workday/call_operation)
- [Get custom object action](/en/connectors/workday/get-custom-objects)
- [Get report action](/en/connectors/workday/get_report)
- [Get report using WQL action](/en/connectors/workday/get_report_using_wql)
- [List custom object definitions action](/en/connectors/workday/list-custom-object-definitions)
- [Create/update custom object action](/en/connectors/workday/create-update-custom-objects)
- [Search business objects batch action](/en/connectors/workday/search-business-objects)

### Wiki

- [Workday Reports-as-a-Service (RaaS)](/en/connectors/workday/workday_raas)

---
