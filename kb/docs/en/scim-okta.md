---
url: 'https://docs.workato.com/en/scim-okta.md'
description: >-
  Configure SCIM 2.0 in Okta to automate Workato user lifecycle management while
  SAML handles roles and group assignments.
---

# Configure SCIM in Okta

Workato supports the SCIM 2.0 protocol with the Okta identity provider:

- SCIM handles user lifecycle management (create, update, deactivate).
- SAML handles roles and group assignments (environment roles and collaborator groups).

> **SUPPORTED CONFIGURATIONS**
> 
> Workato's new permission model supports two valid configurations:
> 
> - **Hybrid**: SCIM handles user lifecycle management (create, update, deactivate), and SAML handles roles and group assignments dynamically at login.
> - **SCIM-only role provisioning**: Some organizations continue to provision environment roles through SCIM. To support this, include the **External Namespace** value `urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole` when you configure environment role attributes such as `workato_role`, `workato_role_test`, or `workato_role_prod`.

## Prerequisites

- Your organization must have the **Data Monitoring/Advanced Security & Compliance** capability.
- You must have [SAML SSO](/en/user-accounts-and-teams/single-sign-on) successfully set up with your identity provider.
- You must have already [configured SCIM in Workato](/en/scim-workato#configure-workato).

* * *

## Configure SCIM

1. Log in to your **Okta admin** dashboard.
   
2. If you have already configured your Workato SAML app on Okta, locate the **Workato SAML Application**, and navigate there.
   
   If you have not configured your Workato SAML app on Okta yet, [create a new SAML 2.0 app](/en/user-accounts-and-teams/single-sign-on#okta-single-sign-on) before proceeding.
   
3. In the **General** tab, under **App Settings**, find the **Provisioning** field.
   
4. Select **Enable SCIM Provisioning**, and Save.
   
   _Enable SCIM provisioning_
   
5. You can now see the new **Provisioning** tab on Okta.
   
6. In the **SCIM Connection** interface, specify the following:
   
   <dl><dt>SCIM connector base URL</dt><dd>This is the <a href="/en/scim-workato.html#base_url">Base URL</a> of the Workato SCIM API endpoint, that you copied when configuring SCIM in Workato.</dd><dd>In this example, we use <code>https://workato.com/scim/v2</code>.</dd><dt>Unique identifier field for users</dt><dd>This is how we identify users both in Workato and in Okta.</dd><dd>Here, we set the <code>userName</code> in Okta to contain the user’s email.</dd><dt>Supported provisioning actions</dt><dd>Select the following actions:<ul><li>Import New Users and Profile Updates</li><li>Push New Users</li><li>Push Profile Updates</li></ul></dd><dt>Authentication Mode</dt><dd>Select HTTP Header.</dd><dt>Authorization</dt><dd>Set the <strong>Bearer</strong> field by pasting the <a href="/en/scim#parameters">SCIM token</a> you copied when configuring SCIM in Workato.</dd></dl>
   
   _SCIM setup details_
   
7. Click **Test Connector Configuration** to determine if your setup is correct.
   
8. When the test runs successfully, Okta displays the status of the connection and the supported SCIM provisioning actions.
   
   _Successful SCIM setup in Okta_
   

### Configure SCIM attribute mappings

You can configure attribute mappings after you successfully configure and test the SCIM connection.

Complete the following steps to set up attribute mappings:

1. Go to **Provisioning > To App > Attribute Mappings**. ![SCIM provisioning setup in Okta](/assets/scim-okta-attribute-mapping.V8rWkczk.png)_SCIM provisioning setup in Okta_
   
2. Use the following configuration:
   
   | Workato attribute | Okta value | Applies on |
   | --- | --- | --- |
   | `userName` | Configured in **Sign On settings** | N/A |
   | `givenName` | `user.firstName` | Create and update |
   | `familyName` | `user.lastName` | Create and update |
   | `email` | `user.email` | Create and update |
   | `displayName` | `user.displayName` | Create and update |
   
   You don't need to create custom SCIM attributes for this step. These mappings define how Okta passes user profile values to Workato during provisioning.
   
   > **ENVIRONMENT ROLES AND GROUP MANAGEMENT**
   > 
   > We recommend mapping environment role attributes (`workato_role`, `workato_role_test`, `workato_role_prod`) through SCIM and managing collaborator groups (`workato_user_groups`) through SAML.
   > 
   > This allows you to provision and deprovision users with SCIM while dynamically assigning them to groups during SAML authentication.
   

## Configure Workato role attributes for SCIM

Workato's hybrid integration with Okta uses SCIM for user lifecycle management and SAML for role and group assignments. However, some organizations choose to provision environment roles (such as `workato_role`, `workato_role_test`, and `workato_role_prod`) through SCIM. This configuration remains supported but requires the correct **External Namespace** setting.

Use this configuration if your organization provisions environment roles through SCIM instead of SAML. If you rely on SAML for role assignment, you can skip this section.

1. Go to your **Workato application > Provisioning > To App** tab in the Okta Admin Console.
   
2. Enable the following SCIM actions so that Okta can create and update user attributes in Workato:
   
   - **Create Users**
   - **Update User Attributes**
   - **Deactivate Users**
   
   _To App actions_
   
3. Go to **Directory > Profile Editor > Workato App User Profile > + Add Attribute**.
   
   If your organization already has existing `workato_role`, `workato_role_test`, or `workato_role_prod` attributes from a previous configuration, edit them instead of creating new ones. Ensure that each includes the required **External Namespace** setting so Okta can continue to update these attributes through SCIM.
   
4. Set the following values for each environment role attribute you plan to provision through SCIM:
   
   | Field | Value |
   | --- | --- |
   | Data type | `String` |
   | Display name | `workato_role` (or environment-specific equivalent, for example `workato_role_test`, `workato_role_prod`) |
   | Variable name | Same as the display name |
   | External name | Same as the display name |
   | External namespace | `urn:ietf:params:scim:schemas:workato:1.0:WorkatoRole` |
   
   This ensures that Okta correctly passes these environment role attributes through SCIM.
   
5. Select the **Define enumerated list of values** checkbox and add your environment role values under **Attribute members**:
   
   | Display name | Value |
   | --- | --- |
   | Environment admin | Environment admin |
   | Environment manager | Environment manager |
   | Member | Member |
   | NoAccess | NoAccess |
   
   Values are case sensitive.
   
6. Click **Save**. Your configuration should resemble the following example:
   
   _Complete configuration_
   

## Provision users

If you already assigned users to your Workato application for SAML SSO, you can trigger a provisioning job to sync your existing users between Okta and Workato. This ensures that you don't unintentionally create duplicate accounts on your Workato workspace.

Users provisioned through SCIM exist in Workato immediately, but they don’t receive roles or collaborator group memberships until they log in through SAML.

> **SCIM USERS ARE HIDDEN UNTIL EMAIL VERIFICATION**
> 
> SCIM-provisioned users don't appear on collaborator management screens until they accept a verification email from Workato. Unverified users are excluded from the collaborators list, the pending invitations screen, and group member lists and member counts. As a result, the collaborator count in Workato may be lower than the number of users provisioned in Okta if those users haven't verified their email addresses.

1. In the **Assignments** interface, Okta denotes the users that existed before you configured SCIM with a red exclamation mark icon.
   
   _Existing users are not provisioned by SCIM_
   
2. Click **Provision User** to sync users. Okta displays a notification that it will provision the user to Workato.
   
3. Click **OK**.
   
   _Confirm provisioning_
   
4. Go to **Groups > Application > Assign Workato**.
   
   _Configure groups_
   
5. Assign the Workato application to individuals or groups in Okta for new users. SCIM provisions the account in Workato, while environment roles and collaborator group memberships are evaluated dynamically through SAML at login.
   
6. Workato sends an email invitation to provisioned users. Instruct them to click the link in the email to verify their email address.
   
   ![Email invitation to join a workspace](/assets/scim-azure-ad-email-notification.kjKQFcUM.png) _Email invitation to join a workspace_
   
   After verification, users can sign in with the environment roles and collaborator groups assigned through SAML.
   
   > **TROUBLESHOOTING**
   > 
   > If clicking on the invitation email redirects you to the Workato login page instead of your organization’s workspace, it is likely that you already have a Workato account associated with the same email. If you have forgotten your login credentials, reset your password.
   
7. You can check the Workato [activity audit log](/en/features/activity-audit-log) to confirm the addition of the user:
   
   ![Activity audit log showing that a user has accepted an invitation](/assets/scim-azure-ad-audit-log.CNCV_sJm.png) _Activity audit log showing that a user has accepted an invitation_
   

## Convert user assignments to group assignments

If you previously assigned users directly to the Workato application, you can convert them to group-based assignments. Group assignments ensure environment roles and collaborator groups are evaluated dynamically through SAML at login.

1. Go to **Applications > Workato > Assignments** and go to the Workato application.
   
2. Select **Convert Assignments**.
   
   _Convert assignments from user to group_
   
3. Select the individual user that you plan to convert from user to group management in the **Select assignments to convert** interface.
   
   _Select the user to convert to group management_
   
4. Click **Convert selected**.
   
5. Okta displays a successful conversion message when the conversion completes. The user is now managed through group assignment. Environment roles and collaborator group memberships apply dynamically through SAML at login.
   

## Update users

SCIM provisions lifecycle changes such as user profile updates, status changes, or deactivation. Environment roles and collaborator group memberships are managed through SAML and take effect the next time the user signs in.

1. Update user attributes such as email, display name, or status, and click **Save**. This action triggers a user update call to Workato through SCIM and immediately updates the user in Workato.
   
2. Click **Save**. This action triggers a user update call to Workato through SCIM.
   
3. Examine the activity-audit logs dashboard to verify provisioning.
   
   We denote changes made through SCIM as `scim_auto_sync`.
   

## Deprovision users

You can deprovision users directly in the **Okta admin** dashboard.

In **Okta**, a deprovisioning event can be any of the following actions:

- User suspension
- User deactivation
- App access removed

In **Workato**, a user is deprovisioned from your Workato workspace in any of the following scenarios:

- User is suspended in Okta
- User is deactivated in Okta
- Workato app is removed from the user

In all these situations, the user cannot access the Workato workspace. The user’s recipes and connections remain available to the rest of the team.

The user may be re-provisioned from Okta at a later time, and would retain their earlier privileges.

## Disable SCIM

To disable SCIM, follow these steps in Okta. Alternatively, you can disable SCIM in [Workato](/en/scim-workato#disable).:

1. In Okta, find the Workato application.
   
2. Navigate to **General**.
   
3. Disable SCIM by unselecting the **Enable SCIM provisioning** option, and then **Confirm** your action.
   
   This action breaks your SCIM connection. User data cannot be synced between Okta and Workato.

---
