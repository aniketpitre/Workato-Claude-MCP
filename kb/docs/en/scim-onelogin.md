---
url: 'https://docs.workato.com/en/scim-onelogin.md'
description: >-
  Configure SCIM 2.0 in OneLogin to automate user provisioning and
  deprovisioning for your Workato workspace.
---

# Configure SCIM in OneLogin

Workato supports the SCIM 2.0 protocol with the OneLogin identity provider.

* * *

## Prerequisites

- Your organization must have the **Data Monitoring/Advanced Security & Compliance** capability.
- You must have [SAML SSO](/en/user-accounts-and-teams/single-sign-on) successfully set up with your identity provider.
- You already [configured SCIM in Workato](/en/scim-workato#configure-workato).

* * *

## Configure for generic SAML applications

If you are using a generic SAML application without provisioning on OneLogin, you must first add a new application that supports provisioning from the OneLogin app catalog.

> **RECOMMENDATION**
> 
> We recommend that you also configure SAML SSO for the application, and then proceed to configure SCIM.

Follow these steps:

1. Log into **OneLogin**.
   
2. Navigate to **Apps > Add App**.
   
3. Search for “SCIM”, and select the \*\*SAML with SCIM Provisioner (core user 2.0)\*\*option.
   
4. Add the application.
   

## Configure SCIM

1. Navigate to the **Provisioning** interface, and select the following options:
   
   <dl><dt>Enable provisioning</dt><dd>Select this option.</dd><dt>When users are deleted...</dt><dd>Choose .</dd><dt>When user accounts are suspended...</dt><dd>Choose .</dd></dl>
   
   _Enable provisioning_
   
2. Navigate to the **Configuration** interface, and add values to the following fields:
   
   <dl><dt>SCIM Base URL</dt><dd>This is the <a href="/en/scim-workato.html#base_url">Base URL</a> of the Workato SCIM API endpoint, that you copied when configuring SCIM in Workato.</dd><dt>SCIM Bearer Token</dt><dd>This is the <a href="/en/scim#parameters">SCIM token</a> you copied when configuring SCIM in Workato.</dd></dl>
   
   _Supply Base URL and SCIM token from Workato_
   
3. To update Workato user roles from OneLogin through SCIM provisioning, you must configure the standard JSON schema in OneLogin.
   
   Expand the SCIM JSON template and add in the following:
   
   - As part of "schemas", add `urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole`
   - After emails, within the rest of the schema, add the following code:
   
   ```
     "urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole": {
     "workato_role": "{$user.custom_fields.workato_role}",
     "workato_role_test": "{$user.custom_fields.workato_role_test}",
     "workato_role_prod": "{$user.custom_fields.workato_role_prod}"
     }
   ```
   
   _Update Workato user roles_
   
4. If you did not configure the custom user fields for updating Workato roles through SAML Roles Sync, complete the configuration of custom user attributes like “workato\_role”, “workato\_role\_test”, and “workato\_role\_prod” before moving on to the next step. See [SAML role sync](/en/saml-role-sync-onelogin#onelogin-create-roles).
   
5. Configure the parameters to reference these role attributes.
   
   Navigate to the **Parameters** interface, and edit the `workato_role` by adding the following fields to reference the `workato_role` attribute values:
   
   - Select the **+** (plus) icon, under **Field name**, ensuring that the value corresponds to the **short name** that you configured for the custom user attributes.
   - Select the **Include in SAML Assertion** option.
   - Select the **Include in User Provisioning** option.
   
   Click **Save**.
   
   _Configure role attribute parameters_
   
   If your organization has the **Environment** feature in Workato, repeat this step for all environment-specific roles, such as `workato_role_prod`, `workato_role_test`, and for any additional custom roles.
   
6. After you finish configuring the parameters, your interface should appear similar to this example:
   
   _Parameters_
   
7. Again, navigate back to the **Configuration** interface.
   
   Under **API connection**, select **Enable**.
   
   _Enable API connection_
   

## Provision users

If you already have users assigned to your Workato application for SAML SSO, you can trigger a provisioning job to sync your existing users between OneLogin and Workato. This ensures that you don't unintentionally create duplicate accounts on your Workato workspace.

1. In OneLogin, find the Workato application.
   
2. Navigate to **Users**, select **Apply to all**, then choose **Reapply Mappings**, and confirm by clicking **Approve**.
   
   _Provision users_
   
   This action triggers a bulk sync between Workato and OneLogin, and ensures that all existing collaborators are now managed through SCIM.
   
3. Navigate to the **Users** interface to see the **Provisioning State** for all users.
   
   _Updated provisioning state for users_
   
4. When assigning new users to Workato, you can either assign the application to them, or assign a OneLogin Role with the necessary access policy.
   
5. Workato sends an email invitation to the selected users. Instruct users to click the link in the email to verify their email address:
   
   ![Email invitation to join a workspace](/assets/scim-azure-ad-email-notification.kjKQFcUM.png) _Email invitation to join a workspace_
   
   The collaborator can then sign in to the assigned workspace with the role(s) you configured.
   
   > **TROUBLESHOOTING**
   > 
   > If clicking on the invitation email redirects you to the Workato login page instead of your organization’s workspace, it is likely that you already have a Workato account associated with the same email. If you have forgotten your login credentials, reset your password.
   
6. You can check the Workato [activity audit log](/en/features/activity-audit-log) to confirm the addition of the user:
   
   ![Activity audit log showing that a user has accepted an invitation](/assets/scim-azure-ad-audit-log.CNCV_sJm.png) _Activity audit log showing that a user has accepted an invitation_
   

## Update users

To update Workato roles from OneLogin, you must update the user’s custom attributes.

1. In OneLogin, navigate to the **Users** interface.
   
2. Select the user that you plan to update.
   
3. Enter the name of the role you plan to provision.
   
   > **TIP**
   > 
   > Role names are case-sensitive.
   
4. Click **Save**.
   
5. To verify role changes on Workato, you can examine the activity-audit logs dashboard.
   
   We denote changes made through SCIM as `scim_auto_sync`.
   
   _Confirming role change through SCIM_
   

## Deprovision users

To deprovision users, you can use one of the three (3) available methods, depending on the circumstances and use case. In all these situations, the user cannot access the Workato workspace. The user’s recipes and connections remain available to the rest of the team.

Each of these scenarios on OneLogin trigger a deprovisioning event on Workato:

<dl><dt>Remove App access</dt><dd><ol><li>In OneLogin, navigate to the Workato application.</li><li>Select <strong>Users</strong>.</li><li>Find the user that you plan to deprovision.</li><li>Click <strong>Delete</strong>.</li><li>Confirm.</li></ol></dd><dt>Deactivate the user</dt><dd><ol><li>In OneLogin, navigate to the <strong>Users</strong> interface.</li><li>Select the user that you plan to deactivate.</li><li>Toggle the <strong>Active</strong> switch to <strong>Inactive</strong>.</li><li>Click <strong>Save</strong>.</li></ol></dd><dt>Delete the user</dt><dd><ol><li>In OneLogin, navigate to the <strong>Users</strong> interface.</li><li>Select the user you plan to delete.</li><li>Click <strong>More Actions</strong> and select <strong>Delete</strong>.</li><li>Click <strong>Save</strong>.</li></ol></dd></dl>

> **INFO**
> 
> If users are deprovisioned during an active session, their next action locks them out from the workspace. Their data, such as recipes and connections, remain accessible to other users in the workspace.

## Disable SCIM

To disable SCIM, follow these steps in OneLogin. Alternatively, you can disable SCIM in [Workato](/en/scim-workato#disable).:

1. In OneLogin, find the Workato application.
   
2. In the **Provisioning** interface, deselect the **Enable provisioning** option.
   
3. Disable SCIM by unselecting the **Enable SCIM provisioning** option, and then **Save** your action.
   
   This action breaks your SCIM connection. User data cannot be synced between OneLogin and Workato.
   

_Disabling SCIM_

---
