---
url: 'https://docs.workato.com/en/saml-role-sync-onelogin.md'
description: >-
  Configure OneLogin to sync Workato role assignments for users and groups
  through SAML across DEV, PROD, and TEST environments.
---

# OneLogin SAML role sync configuration

When using OneLogin IdP, you can sync role configurations both for users and for groups.

Here, we configure role sync for basic Workato environments: DEV (default), PROD, and TEST.

## Prerequisites

1. Ensure that you configured the SAML SSO for your OneLogin organization.
2. Ensure that you enabled just-in-time provisioning in the Workato UI.
3. Ensure that you use SAML SSO enforcement for your team or organization.

## Add custom Workato role attributes to your user profile on OneLogin

To begin, you must create the necessary Workato role attributes inside your identity provider, OneLogin.

1. In OneLogin, navigate to **Users >> More Actions >> Custom User Fields >> New User Field**.
   
2. In the **Custom User Fields** interface, specify the new role using these fields:
   
   <dl><dt>Name</dt><dd>Use <code>appuser.workato_role</code>. This sets up the default user role for Workato, for the DEV environment.</dd><dt>Short name</dt><dd>Use <code>workato_role</code>.</dd></dl>
   
   Similarly, specify the roles for the other Workato environments, if you use them:
   
   - **Name** `appuser.workato_role_prod` with **Short name** `workato_role_prod` for the PROD environment
   - **Name** `appuser.workato_role_test` with **Short name** `workato_role_test` for the TEST environment
   
   _Add Workato custom role in OneLogin_
   
3. If you use additional environments in Workato, add more custom user fields.
   

## Configure SAML attribute statements

To include `workato_role` attribute values each time a users signs into Workato through SAML SSO, you must configure the SAML attribute statements.

1. In OneLogin, navigate to **Applications >> Workato >> Parameters >> Create new field** by clicking the **+** (plus) icon.
   
2. In the **New Field** interface, add the **Short name** of the role, which you specified in the [user profile](#onelogin-create-roles).
   
   Here, we are adding the field name for `workato_role_prod`, the Workato role for the PROD environment.
   
   _Add new Workato role to SAML attribute statements in OneLogin_
   
3. Select the option **Include in SAML assertion**.
   
4. Click **Save**.
   
5. Open the field you just created to edit it. Here, we are editing **workato\_role\_prod**.
   
6. In the **Edit Field workato\_role\_prod** interface, select the **Value** `appuser.workato_role_prod (Custom)` from the drop-down.
   
   _Adding Workato roles in SAML attribute statements in OneLogin_
   
7. Click **Save**.
   
8. Similarly, specify the values for the other Workato environments:
   
   - **Name** `workato_role` with **Value** `appuser.workato_role (Custom)` for the DEV environment
   - **Name** `workato_role_test` with **Value** `appuser.workato_role_test (Custom)` for the TEST environment
9. Repeat these steps if you use environments in Workato.
   

After adding the necessary SAML statements, your custom fields for Workato may resemble the following screenshot:

_List of SAML custom fields for Workato_

## Assign the Workato app to users

Here, we demonstrate how to assign the app to users and update the `workato_role` parameter.

1. Navigate to **Users** in OneLogin.
   
2. Select the user to assign to Workato.
   
   Here, we assign the Workato app to the user **Gregory**.
   
3. In the **Edit SAML Custom Connector ...** interface, specify the level of permissions for each environment-based role.
   
4. Select the **Allow the user to sign in** option, if not turned on already.
   
5. Enter role values for the user's environment attributes.
   
   > **ROLE MAPPINGS**
   > 
   > How Workato interprets these values depends on your workspace configuration:
   > 
   > - **Legacy permissions model**: Use workspace-level system roles such as **Admin**, **Analyst**, **Operator**, or custom roles (for example, **DevOps\_Admin**).
   > - **New permissions model**: Use environment roles such as **Environment admin**, **Environment manager**, **Member**, or custom environment roles.
   > 
   > Role names are case-sensitive and must match the roles defined in Workato.
   
   For example, in the screenshot below we assign **Gregory** the legacy collaborator **Analyst** role in the PROD environment, and the legacy collaborator **Admin** role in the DEV and TEST environments.
   
   _Assign user to Workato app, and specify permissions_
   
   > **Recommendation**
   > 
   > Workato recommends that you update a users `workato_role` attribute value at the user or group level in the identity provider **_only_**. After you enable role sync, Workato overwrites all manual role changes that you make in the Workato UI when the user subsequently logs in through SAML SSO.
   
6. Click **Save**.
   

## Assign the Workato app to groups

Start by creating a new group, and assign users to that group in OneLogin.

You must then create and configure a new rule, and then set `workato_role` values based on group membership.

1. Navigate to **Users >> Groups**, click **New Group**, and create a new group.
   
   Here, we create the group **Workato DevOps Admins**.
   
2. In **Users >> Select User >> Authentication**, click **Add membership to groups**.
   
   Add individual users as members to the new group, **Workato DevOps Admins**.
   
3. Navigate to **Applications >> Workato >> Rules**, and click **Create new rule**.
   
4. In the **New mapping** interface, specify rule mappings based on group membership. Here, we assign to the members of the **Workato\_DevOps\_Admins** group the **DevOps\_Admin** role in the various Workato environments by mapping the values of the roles to the Macro **DevOps\_Admin**.
   
   1. Make sure to select the correct group.
      
      Here, under **Conditions**, we construct the statement by setting **Group is Workato\_DevOps\_Admin**.
      
   2. Under **Actions**, select one of the previously defined roles.
      
   3. For each role, select the **Map from OneLogin** option.
      
   4. Under **Set workato_role_ to**, select **Macro**.
      
   5. Make sure to use the group you created to complete the mapping. Here, we use **DevOps\_Admin**.
      
   
   _Assign the group to Workato app, and specify permissions_
   
5. Make sure to complete the mappings for all workato environments:
   
   - DEV: workato\_role
   - PROD: workato\_role\_prod
   - TEST: workato\_role\_test
   - any additional custom environments that you use is Workato

## Change assignment for user management at group level

To include previously-configured users under group management rules, complete these steps:

1. Navigate to **Users** in OneLogin.
   
2. Select the user to assign to Workato.
   
   Here, we change the Workato app assignment of the user **Gregory** to be managed at group level.
   
3. In the **Edit SAML Custom Connector ...** interface, make the changes to the necessary Workato role attributes.
   
   Here, we are changing the fields **workato\_role\_test** and **workato\_role** (for TEST and DEV environments, respectively) to group **DevOps\_Admin**.
   
   _Workato field definition, SAML assertion_
   
4. Click **Reset login**. This action remaps the login for the user at the application level by applying the new rule. You only need to do this for users who were previously configured as individuals.
   
5. Click **Save**.
   

## Verify role changes

If your organization uses Workato's Activity Audit Logs feature, you can verify the automatic role sync when the user logs in through SAML SSO.

Role changes triggered by SAML assertions appear under the **Source** attribute, with the value `saml_auto_sync`.

Manual role changes made in Workato UI have the value `user`.

You can also see the **New Role** and **Previous Role** values.

_SAML roles sync activity audit log_

---
