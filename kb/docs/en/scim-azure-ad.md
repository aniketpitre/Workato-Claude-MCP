---
url: 'https://docs.workato.com/en/scim-azure-ad.md'
description: >-
  Configure SCIM 2.0 in Microsoft Entra ID to automate user provisioning,
  deprovisioning, and attribute mapping with Workato.
---

# Configure SCIM in Microsoft Entra ID

Workato supports the System for Cross-domain Identity Management (SCIM 2.0) protocol with the Microsoft Entra ID identity provider.

> **NEW NAME FOR AZURE AD**
> 
> Microsoft has renamed Azure Active Directory to [Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/new-name). You may see either name in the Azure Portal during the transition period.

Configuring SCIM for Microsoft Entra ID involves the following steps:

- [Prerequisites](#prerequisites)
- [Step 1: Configure custom extension attributes](#step-1-extension-attributes)
- [Step 2: Configure automatic provisioning on Microsoft Entra ID](#step-2-auto-provisioning)
- [Step 3: Configure attribute mappings between Microsoft Entra ID and Workato](#step-3-attribute-mappings)
- [Step 4: Provision users](#step-4-provision)

> **HYBRID MODEL**
> 
> Workato’s new permission model uses a hybrid approach:
> 
> - SCIM provisions and deprovisions user accounts, and syncs core profile attributes such as userName, email, and, active.
> - SAML assigns environment roles and collaborator group memberships dynamically at login.
> 
> While Microsoft Entra ID supports extension attributes for role values through SCIM, Workato recommends that you manage role and group assignments through SAML attribute mappings and group claims.

* * *

## Prerequisites

**In Workato:**

- You must be a workspace admin.
- Your organization must have the **Data Monitoring/Advanced Security & Compliance** capability.
- You must have [SAML SSO](/en/user-accounts-and-teams/single-sign-on) successfully set up with your identity provider.
- You must have already [configured SCIM in Workato](/en/scim-workato#configure-workato).

**In Microsoft Entra ID:**

- You must be able to access the [Microsoft Graph](https://developer.microsoft.com/en-us/graph/graph-explorer) API.
- You must have access to Microsoft Entra ID with sufficient permissions.

* * *

## Step 1: Configure custom extension attributes

By default, Workato roles and collaborator groups aren't provisioned through SCIM. These are assigned dynamically through SAML attribute mappings and group claims.

You may extend the Microsoft Entra ID user schema to include a custom attribute specifying the user's Workato role.

> **RECOMMENDATION**
> 
> Workato recommends using SAML attribute mappings and group claims for role assignment. SCIM should remain focused on user lifecycle management.

If you plan to create [extension attributes](https://learn.microsoft.com/en-us/azure/active-directory/app-provisioning/user-provisioning-sync-attributes-for-mapping#create-an-extension-attribute-for-cloud-only-users-using-microsoft-graph), complete the following steps.

1. Navigate to [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer).
   
2. Run a Microsoft Graph query to list your Azure tenant's applications:
   
   - Select **GET** from the HTTP verb drop-down menu.
   - Enter `https://graph.microsoft.com/v1.0/applications` in the query box.
   - Select **Run query**.
   
   ![Example request to list applications using Microsoft Graph Explorer](/assets/scim-azure-ad-list-apps.Dz9pzBGO.png) _Example request to list applications using Microsoft Graph Explorer_
   
3. Find your application's `id` field in the output.
   
   ![Find the id field](/assets/scim-azure-ad-get-app-id.DrncdzWP.png) _Find the `id` field_
   
   > **ID FIELD**
   > 
   > The `id` field is distinct from the `appId` field. Do not use `appId`.
   
4. Create an extension attribute called `workato_role`. In a later step, you will use this attribute to assign each user's role in your workspace. Note that in workspaces with the [Environments](/en/features/environments) feature enabled, `workato_role` is used to assign a role for the default DEV environment.
   
   - Select **POST** from the HTTP verb drop-down menu.
     
   - Enter the following URL in the query box and replace `{id}` with your application's ID:
     
     ```
     https://graph.microsoft.com/v1.0/applications/{id}/extensionProperties
     ```
     
   - Paste the following JSON in the **Request body** field:
     
     ```json
     {
       "name": "workato_role",
       "dataType": "string",
       "targetObjects": [
         "User"
       ]
     }
     ```
     
   - Select **Run query**.
     
   
   ![Example request to create an extension attribute in Microsoft Graph Explorer](/assets/scim-azure-ad-create-extension-request.BXdhYI9p.png) _Example request to create an extension attribute in Microsoft Graph Explorer_
   
5. Locate the `name` field in the output and copy its value. It will look something like this:
   
   ```
   extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role
   ```
   
   ![Find the name field in the output](/assets/scim-azure-ad-create-extension-response.BBUYo-Si.png) _Find the `name` field in the output_
   
6. **If your organization has the [Environments](/en/features/environments) feature in Workato:** Repeat the preceding two steps using the example request bodies below. Send one request to create an extension attribute for the PROD environment, and another request for the TEST environment:
   
   ```json
   {
     "name": "workato_role_prod",
     "dataType": "string",
     "targetObjects": [
       "User"
     ]
   }
   ```
   
   ```json
   {
     "name": "workato_role_test",
     "dataType": "string",
     "targetObjects": [
       "User"
     ]
   }
   ```
   
   Ensure that you copy the value of the `name` field in each response.
   
7. Find the ID of the user you want to provision to Workato:
   
   - Select **GET** from the HTTP verb drop-down menu.
   - Enter `https://graph.microsoft.com/v1.0/users` in the query box.
   - Select **Run query**.
   - Look for the user in the output and copy the value of their `id` attribute.
8. Assign the extension attribute(s) and the desired role to the user:
   
   - Select **PATCH** from the HTTP verb drop-down menu.
     
   - Enter the following URL in the query box and replace `{id}` with the user's ID:
     
     ```
     https://graph.microsoft.com/v1.0/users/{id}
     ```
     
   - Create a request body based on the following JSON, substituting the appropriate values, and paste it in the **Request body** field:
     
     ```json
     {
       "{extension attribute name}": "{system role or custom role to assign the user}"
     }
     ```
     
     EXAMPLE REQUEST BODY WITHOUT ENVIRONMENTS
     
     The following example assigns the user an **Admin** role in a workspace without the [Environments](/en/features/environments) feature enabled:
     
     ```json
     {
       "extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role": "Admin"
     }
     ```
     
     EXAMPLE REQUEST BODY WITH ENVIRONMENTS
     
     The following example assigns the user a different system role for each environment:
     
     ```json
     {
       "extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role": "Admin",
       "extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role_prod": "Operator",
       "extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role_test": "Analyst"
     }
     ```
     
   - Select **Run query**.
     
   
   If the request is successful, the response is simply `{}`.
   
   ![Successful role assignment](/assets/scim-azure-ad-assign-extension-to-user.DkfdpUgg.png) _Successful role assignment_
   
9. Confirm that the extension has been assigned to the user:
   
   - Select **GET** from the HTTP verb drop-down menu.
     
   - Enter the following URL into the search box, replacing `{id}` with the user's ID and `{extension attribute name}` with the extension name you want to confirm:
     
     ```
     https://graph.microsoft.com/v1.0/users/{id}?$select={extension attribute name}
     ```
     
     For example:
     
     ```
     https://graph.microsoft.com/v1.0/users/4a5b1db8-415b-4207-ab8d-1a2b3c4d5e6f?$select=extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role
     ```
     
   - Select **Run query**.
     
   - Check the response to confirm that the user has an extension attribute with the desired role. You should see output like this:
     
     ```json
     {
       "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users(extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role)/$entity",
       "extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role": "Admin"
     }
     ```
     

## Step 2: Configure automatic provisioning on Microsoft Entra ID

After you extend the Microsoft Entra ID user schema, you must configure automatic provisioning on Microsoft Entra ID.

1. Navigate to the Workato SAML application you created in Microsoft Entra ID.
   
   > **CONFIGURE SAML SSO**
   > 
   > If you have not yet configured SAML SSO for your Workato application, set up a [non-gallery SAML application in Microsoft Entra ID](/en/user-accounts-and-teams/single-sign-on#azure-ad-single-sign-on) to access your Workato workspace.
   
2. Navigate to **Manage > Provisioning**.
   
3. Select **Automatic** from the **Provisioning Mode** drop-down menu.
   
4. In the **Admin Credentials** section, enter the **Tenant URL** and **Secret Token** fields using the base URL and SCIM token you generated when you [configured SCIM in Workato](/en/scim-workato#configure-workato).
   
   ![Configure automatic provisioning](/assets/scim-azure-ad-enable-automatic-provisioning.BNTwhx1q.png) _Configure automatic provisioning_
   
5. Select **Test Connection**. If the test is successful, Azure will display the message "The supplied credentials are authorized to enable provisioning":
   
   ![Successful test connection](/assets/scim-azure-ad-test-connection.Cc0fJsPk.png) _Successful test connection_
   
6. Disable group provisioning. Microsoft Entra ID enables this option by default, but Workato SCIM only supports user-level provisioning.
   
   ![Disable group provisioning](/assets/disable-group-provision.DtPN2Tic.png)_Disable group provisioning_
   
7. Select **Save**.
   

## Step 3: Configure attribute mappings between Microsoft Entra ID and Workato

You must configure which Microsoft Entra ID attributes are passed into Workato through SCIM.

> **REQUIRED MAPPINGS**
> 
> At minimum, map only the core attributes needed for lifecycle management. Don't map environment roles or collaborator groups through SCIM. These are managed by SAML at log in to ensure dynamic evaluation of group claims.
> 
> If your organization requires role assignment through SCIM, you can map extension attributes (for example, `workato_role_test` or `workato_role_prod`). However, Workato recommends using SAML for role and group assignments to ensure dynamic evaluation.

1. Navigate to your Workato SAML application in Microsoft Entra ID.
   
2. Expand the **Mappings** section and select **Provision Microsoft Entra ID Users**.
   
3. Ensure **Enabled** is set to **Yes**.
   
4. In the **Target Object Actions** section, check the boxes for **Create** and **Update**.
   
5. At the bottom of the page, select the **Show advanced options** checkbox.
   
6. Select **Edit attribute list for customappsso**.
   
7. At the bottom of the **customappsso User Attributes** list, add the following attribute name in the **Name** field and set **Type** to **String**:
   
   ```
   urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole:workato_role
   ```
   
8. **If your organization has the [Environments](/en/features/environments) feature in Workato:** Repeat the previous step to add the extension attributes for the TEST and PROD environments, using each of the following attribute names with **Type** set to **String**:
   
   ```
   urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole:workato_role_test
   ```
   
   ```
   urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole:workato_role_prod
   ```
   
   ![Extension attributes for an organization with the Environments feature enabled](/assets/scim-azure-ad-edit-attribute-list.BRH4IiBL.png) _Extension attributes for an organization with the Environments feature enabled_
   
9. Select **Save** and then **Yes** to confirm that you want to make the changes. You are returned to the **Attribute Mapping** page.
   
10. Select **Add New Mapping**.
    
11. In the **Mapping type** field, select **Direct**.
    
12. In the **Source attribute** field, select the `workato_role` extension attribute you configured previously, as shown in the following example:
    
    ```
    workato_role (extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role)
    ```
    
13. In the **Target attribute** field, select the corresponding attribute you configured, as shown in the following example:
    
    ```
    urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole:workato_role
    ```
    
14. Select **Always** from the **Apply this mapping** drop-down menu if it is not already selected.
    
    ![Edit attribute mapping for workato\_role](/assets/scim-azure-ad-edit-attribute-mapping.DkMvK0kG.png) _Edit attribute mapping for `workato_role`_
    
15. Select **OK**.
    
16. **If your organization has the [Environments](/en/features/environments) feature in Workato:** Select **Add New Mapping** and repeat the previous steps to map the extension attributes for the TEST and PROD environments:
    
    MAP EXTENSION ATTRIBUTES FOR TEST ENVIRONMENT
    
    Example source attribute:
    
    ```
    workato_role (extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role_test)
    ```
    
    Example target attribute:
    
    ```
    urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole:workato_role_test
    ```
    
    MAP EXTENSION ATTRIBUTES FOR PROD ENVIRONMENT
    
    Example source attribute:
    
    ```
    workato_role (extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role_prod)
    ```
    
    Example target attribute:
    
    ```
    urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole:workato_role_prod
    ```
    
    The **Attribute Mapping** page should then look like the following image:
    
    ![Mapped extension attributes for a workspace with the Environments feature enabled](/assets/scim-azure-ad-mapped-extension-attributes-environments.DfERgu_o.png) _Mapped extension attributes for a workspace with the Environments feature enabled_
    
17. Select **Save** and then **Yes** to confirm you want to save your changes.
    

## Step 4: Provision users

After you configure automatic provisioning, you can assign Microsoft Entra ID users and groups to your Workato application and then provision them.

1. Navigate to your Workato SAML application's overview in Microsoft Entra ID.
   
2. Select **Users and groups**.
   
3. Select **Add user/group**.
   
4. Select **None selected** and search for the user or group you want to provision to Workato.
   
5. Select the user or group and click **Select**.
   
6. Select **Assign**.
   
7. In the sidebar, select **Provisioning**.
   
8. Choose whether to provision users automatically or on demand:
   
   PROVISIONING USERS AUTOMATICALLY
   
   To run a cycle that automatically provisions users once every 40 minutes, select **Start provisioning**.
   
   Between cycles, you can trigger a provisioning request immediately by selecting **Stop provisioning** and then **Start provisioning**.
   
   PROVISIONING USERS ON DEMAND
   
   To provision users on demand:
   
   1. Select **Provision on demand**.
      
   2. Search for the user you want to provision and select their name.
      
   3. Select **Provision**.
      
   
   If provisioning is successful, you'll see the following confirmation:
   
   ![Successful user provisioning](/assets/scim-azure-ad-successful-provisioning.Ebqy4xQB.png) _Successful user provisioning_
   
9. Workato sends an email invitation to the selected users. Ask the user to verify their email address by clicking on the link in the email:
   
   ![Email invitation to join a workspace](/assets/scim-azure-ad-email-notification.kjKQFcUM.png) _Email invitation to join a workspace_
   
   The collaborator can then sign in to the assigned workspace with the role(s) you configured.
   
   > **TROUBLESHOOTING**
   > 
   > If clicking on the invitation email redirects you to the Workato login page instead of your organization’s workspace, it is likely that you already have a Workato account associated with the same email. If you have forgotten your login credentials, reset your password.
   
10. You may optionally verify that the user has been added from the Workato [activity audit log](/en/features/activity-audit-log):
    
    ![Activity audit log showing that a user has accepted an invitation](/assets/scim-azure-ad-audit-log.CNCV_sJm.png) _Activity audit log showing that a user has accepted an invitation_
    

## Update users

To update a user's Workato role(s) from Microsoft Entra ID, you must update their custom attributes.

1. Navigate to [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer).
   
2. Run a Microsoft Graph query to update the desired user's custom attributes:
   
   - Select **PATCH** from the HTTP verb drop-down menu.
     
   - Enter the following URL in the query box and replace `{id}` with the user's ID:
     
     ```
     https://graph.microsoft.com/v1.0/users/{id}
     ```
     
   - Paste the following JSON in the **Request body** field, substituting the appropriate values:
     
     ```json
     {
       "{extension attribute name}": "{system role or custom role to assign the user}"
     }
     ```
     
     For example, the following request body updates a user's role to `NoAccess` in the PROD environment of a workspace with the [Environments](/en/features/environments) feature enabled:
     
     ```json
     {
       "extension_ae58e98b4abd4da58d00abcd1234abcd_workato_role_prod": "NoAccess"
     }
     ```
     
   - Select **Run query**.
     
   
   If the request is successful, the response is simply `{}`.
   
   ![Updating a user's attributes using Microsoft Graph Explorer](/assets/scim-azure-ad-update-user-attributes.BVz0Xbn-.png) _Updating a user's attributes using Microsoft Graph Explorer_
   
3. Run a [provisioning cycle](#step-4-provision) on demand in Microsoft Entra ID or wait for the next scheduled cycle.
   

## Deprovision users

There are two ways to deprovision a user:

- [App assignment removal](#app-assignment-removal)
- [User deletion (soft)](#user-deletion-soft)

Either way, the deprovisioned user is no longer able to access the Workato workspace. However, their recipes and connections remain available to the rest of the team.

> **DEPROVISIONING DURING AN ACTIVE SESSION**
> 
> If users are deprovisioned during an active session, their next action locks them out from the workspace. Their data, such as recipes and connections, remain accessible to other users in the workspace.

### App assignment removal

1. In Microsoft Entra ID, navigate to **Users**.
   
2. Select the user you want to deactivate.
   
3. Select the Workato SAML application from the **Applications** section.
   
4. Select **Remove**.
   

### User deletion (soft)

Soft deletions allow you to recover user accounts if needed.

1. In Microsoft Entra ID, navigate to **Users**.
   
2. Select the user you want to deactivate.
   
3. Select **Delete**.
   
4. Select **Delete** again.
   

## Disable SCIM

To disable SCIM from within Microsoft Entra ID:

1. In Microsoft Entra ID, navigate to the Workato application.
   
2. In the **Provisioning** interface, change the provisioning method from **Automatic** to **Manual**.
   
   This action breaks your SCIM connection. User data cannot be synced between Microsoft Entra ID and Workato.
   

You can also disable SCIM from within Workato. See [Disabling SCIM](/en/scim-workato#disable).

---
