---
url: 'https://docs.workato.com/en/saml-role-sync-cyberark-idaptive.md'
description: >-
  Configure CyberArk Identity to sync Workato roles through SAML SSO so user
  roles update across DEV, PROD, and TEST environments at login.
---

# CyberArk Identity SAML role sync configuration

Integrate Workato with CyberArk Identity to manage SAML role synchronization and ensure that your users' roles are updated when they log in through SAML SSO.

Set up role sync for standard Workato environments: DEV (default), PROD, and TEST, as we recommend this for consistent role management.

## Prerequisites

1. Ensure that you have successfully configured the SAML SSO within your CyberArk Identity platform. For guidance, go to the [CyberArk Identity SAML Documentation](https://docs.cyberark.com/Idaptive/Latest/en/Content/Applications/AppsCustom/AddConfigSAML.htm).
   
2. Ensure that you enabled [just-in-time provisioning](/en/user-accounts-and-teams/just-in-time-provisioning#team-collaboration-just-in-time-provisioning) in Workato.
   
3. Ensure that you use [SAML SSO enforcement](/en/user-accounts-and-teams/single-sign-on#cyberark-idaptive-single-sign-on) for your team or organization.
   
4. Ensure that you enabled [role syncing](/en/user-accounts-and-teams/saml-role-sync#enable) in Workato.
   
   ![Enable role sync](/assets/saml-role-sync-enable-2.DmsuWraI.png)_Enable role sync in Workato_
   

## Configure custom user attributes in CyberArk Identity

To set up custom user attributes for Workato environments within CyberArk Identity, follow these steps:

1. Log in to your CyberArk Identity admin console.
   
2. Navigate to **Settings > Customization** in your CyberArk Identity admin portal.
   
3. Click **Additional Attributes** to manage custom attributes.
   
   ![Custom user attributes](/assets/custom-user-attributes.DlbuUDZQ.png)_Create custom user attributes for SAML role sync_
   
4. Select **Add** to create a new attribute.
   
5. Define the attributes for various Workato environments by adding the following:
   
   - `workato_role`: This attribute maps to the DEV environment.
   - `workato_role_test`: This attribute maps to the TEST environment.
   - `workato_role_prod`: This attribute maps to the PROD environment.
6. Select the attribute type as **Text** from the drop-down menu. Repeat this for each attribute.
   
7. Ensure the **User Editable** box is unchecked, unless you intend for users to modify this attribute from their portal.
   
8. Click **Add** to save each attribute.
   
9. Configure the values for each user based on the roles you plan to assign within each Workato environment.
   
   > **ROLE MAPPINGS**
   > 
   > How Workato interprets these values depends on your workspace model:
   > 
   > - **Legacy permissions model**: Values map to legacy collaborator roles such as **Admin**, **Analyst**, **Operator**, or custom roles.
   > - **New permissions model**: Values map to environment roles such as **Environment admin**, **Environment manager**, **Member**, or custom environment roles.
   
   ![Specify Attributes](/assets/specify-user-attributes.2pURLluA.png)_Define attribute types and role values_
   

By completing these steps, you'll have successfully configured custom user attributes in CyberArk Identity, which can be utilized for SAML role synchronization with Workato.

## Configure Workato roles in the CyberArk Identity portal

The following steps show you how to set up the necessary SAML response attributes for role synchronization in Workato:

1. Log in to CyberArk and navigate to **Apps & Widgets > Apps**.
   
2. Select the Workato SAML app from the list to configure it.
   
3. Click **SAML response** to set up the attributes that Workato receives during SSO.
   
   ![SAML Response app](/assets/saml-response-select.wY54a_HK.png)_Set up SAML response attributes_
   
4. Click **Add** to create new attribute statements.
   
5. Specify the attribute names and values based on the custom user attributes you defined earlier. Refer to the following table:
   
   | Attribute Name | Attribute Value |
   | --- | --- |
   | `workato_role` | `LoginUser.Get('workato_role')` |
   | `workato_role_prod` | `LoginUser.Get('workato_role_prod')` |
   | `workato_role_test` | `LoginUser.Get('workato_role_test')` |
   
6. Ensure that you **Save** your settings to apply the changes.
   

> **CUSTOM ROLES IN WORKATO**
> 
> Ensure any custom roles are already defined in Workato before you sync them with SAML assertions. If you reference a role that isn’t defined, users default to **Operator** in workspaces using the legacy permissions model, or **Member** in workspaces using the new permissions model. Role names are case-sensitive.

## Change roles in the CyberArk Identity portal

To change a user's Workato role:

1. Log in to your CyberArk Identity admin console.
   
2. Select the user and the environment you plan to change.
   
3. Enter the new role value and click **Save**.
   
   ![Enter role value](/assets/new-role-value.Cv98evRo.png)_Update user roles in CyberArk Identity_
   

You can verify the user’s updated role privileges from the **Activity Audit** tab on Workato.

![Verify role privileges](/assets/verify-role-privilege.Gg7yLuWc.png)_Confirm role updates in Workato's activity audit_

## Verify with the SAML tracer extension

Use the SAML Tracer browser extension to verify the values passed in SAML assertions. You should see the `workato_role`, `workato_role_test`, and `workato_role_prod` attributes successfully passed.

![Verify SAML Tracer](/assets/verify-saml-extension.Cceqzmw-.png)_Check SAML assertion values with SAML tracer extension_

* * *

---
