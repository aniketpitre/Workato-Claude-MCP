---
url: 'https://docs.workato.com/en/control-plane/collaborators.md'
description: Manage collaborators who help govern workspaces within your Control plane.
---

# Collaborators

Administrators can invite and manage collaborators who help govern workspaces within the Control plane. Control plane collaborators are separate from workspace collaborators. Linking a workspace to your Control plane doesn't automatically add collaborators within that workspace to the Control plane.

## Collaborator roles

Each collaborator has one role. Control plane provides the following roles:

- **Admin**: Full administrative access to the Control plane, including linking and unlinking workspaces.
- **Policy admin**: Read-only access to the Control plane. Policy admins can't access Activity audit.
- **Auditor**: Read-only access to the Control plane, including the list of linked workspaces.

Role changes and collaborator removals take effect within 60 seconds.

> **AT LEAST ONE ADMIN REQUIRED**
> 
> Control plane must always have at least one collaborator with the **Admin** role. You can't remove the last Admin or change their role. Assign the **Admin** role to another collaborator first.

The following table lists the access each role has to Control plane features:

| Feature | Admin | Policy admin | Auditor |
| --- | --- | --- | --- |
| [AI usage dashboard](/en/control-plane/ai-usage) | View | View | View |
| [AI registry asset catalog](/en/control-plane/ai-registry#asset-catalog) | View, manage visibility | View | View |
| [AI registry User portal settings](/en/control-plane/ai-registry#configure-user-portal-settings) | View, edit | View | View |
| [Workspaces](/en/control-plane/manage-workspaces) | View, link and unlink, resend and cancel requests | View | View |
| [End users](/en/control-plane/add-end-users) | View, create, edit, delete, resend invitation, log out | View | View |
| [End-user groups](/en/control-plane/user-groups) | View, create, edit, delete | View | View |
| [SAML identity providers](/en/control-plane/user-groups#user-group-authentication) | View, create, edit, delete | View | View |
| Collaborators | View, invite, edit, delete, resend invitation | View | View |
| [Authentication](/en/control-plane/authentication) | View, edit | View | View |
| [Subdomain](/en/control-plane/configure-subdomain) | View, edit | View | View |
| [Activity audit](/en/control-plane/activity-audit) | View, export | No access | View, export |

## Invite a collaborator

Complete the following steps to invite a collaborator to your control plane:

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**. Control plane opens in a new tab by default.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Control plane settings > Collaborators**.
   
6. Click **\+ Invite collaborator**. The **Invite collaborator to control plane** modal displays.
   
7. Provide a name in the **Name** field.
   
   ![Invite a collaborator](/assets/invite-collaborator.BPQFiNeE.png)_Invite a collaborator_
   
8. Enter the email address in the **Email address** field.
   
9. Use the **Role** drop-down menu to select the role you plan to grant the collaborator.
   
10. Click **Invite**. The invited user is listed on the **Collaborators** page with an **Invited** label.
    

## Resend a collaborator invitation

Complete the following steps to resend a collaborator invitation to your control plane:

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Go to **Enterprise controls** and click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Settings > Collaborators**.
   
6. Click the **...** (ellipsis) option menu of the invited user you plan to send another invitation.
   
7. Click **Resend Invitation**.
   
   ![Click Resend Invitation](/assets/resend-collaborator-invitation.Cb8UaWP-.png)_Click **Resend Invitation**_
   

## Edit a collaborator role

You can only edit a collaborator's role. You can't edit a collaborator's name or email address.

Complete the following steps to edit a collaborator's role:

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Go to **Enterprise controls** and click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Settings > Collaborators**.
   
6. Click the **...** (ellipsis) option menu of the user you plan to edit.
   
7. Click **Edit**.
   
8. Use the **Role** drop-down menu to select the role you plan to grant the collaborator.
   
   ![Collaborator roles](/assets/collaborator-roles.nmaVTdmg.png)_Collaborator roles_
   
9. Click **Save changes**.
   

## Remove a collaborator

Complete the following steps to remove a collaborator from your control plane:

1. Sign in to your Workato account.
   
2. Expand the workspaces menu.
   
3. Go to **Enterprise controls** and click **Control plane**.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Go to **Settings > Collaborators**.
   
6. Click the **...** (ellipsis) option menu of the user you plan to remove.
   
7. Click **Remove**.
   
8. Click **Remove** in the **Remove collaborator?** modal.
   

## Accept a collaborator invitation

Complete the following steps to accept an invitation to a control plane:

1. Go to your email account.
   
2. Locate the email invitation in your inbox.
   
3. Click **Get started** in the body of the email to set up your control plane account.
   
4. Enter your name in the **Name** field.
   
5. Enter your email address in the **Email address** field.
   
6. Enter a password in the **New password** field.
   
7. Re-enter the password in the **Confirm password** field.
   
8. Click **Continue**.

---
