---
url: 'https://docs.workato.com/en/workflow-apps/app-user-groups.md'
description: >-
  Manage Workflow apps users and groups: invite app-users, provision with SSO
  JIT, and assign roles from the Workflow apps portal.
---

# App-user and group management

You can manage app-users and groups in **Platform > Workflow apps portal > Users and groups**.

![Manage users and groups](/assets/users-manage.Ciu6sT6e.png)_Manage users and groups_

* * *

## Add users

You have multiple options to add app-users to the **Workflow apps portal**. You can add app-users to the **Workflow apps portal** by sending individual invitations, or [SSO JIT (Just-in-time) provisioning](/en/user-accounts-and-teams/just-in-time-provisioning). The first option enables you to invite external users and requires users to accept the invitation, while SSO JIT (Just-in-time) provisioning is only for your internal users.

Your third option is to invite users programmatically using the [Invite user action](/en/workflow-apps/workflow-apps-connector/invite-user-action).

* * *

> **WORKFLOW APPS SEATS**
> 
> The number of end users allowed to interact with Workflow apps depends on your platform plan and any additional capacity you've purchased.
> 
> Go to **Platform > Workflow apps portal** or use the [Usage dashboard](/en/pricing/usage) to track the number of authorized end users.
> 
> Note that this is separate from the number of builders you can have or the apps you can create, as there are no limits on either.

### Individual invitations

Complete the following steps to send an individual invitation:

1. Sign in to Workato.
   
2. Go to **Platform > Workflow apps portal > Users and groups**.
   
3. Select **Invite user**.
   
4. Enter the **Name** and **Email address** of the user you plan to invite.
   
5. Click **Add user**.
   
6. New users appear in the **Users and groups** interface.
   

_Invite an individual user to the Workflow apps portal_

* * *

### Resend invitations

You can manually resend invitations to the Workflow apps portal to individual users if their original invitations have expired.

Complete the following steps to resend an invitation:

1. Sign in to your Workato account.
   
2. Go to **Platform > Workflow apps portal > Users and groups**.
   
3. Select the user whose invitation has expired.
   
4. Click the **...** (ellipses) and select **Resend invite**.
   
   ![Resend invitation](/assets/resend-invitation.GHENtJIE.png)_Resend invitation_
   

A new invitation to the Workflow apps portal is sent to the user's email inbox.

## Organize users and groups

You can organize app-users into user groups. This enables you to apply permissions using [role-based access controls](/en/workflow-apps/setup-and-access#app-access-manage), and assign workflow tasks to specific groups.

By default, Workato places every user into the **Everyone group**.

* * *

### Create a group

To create additional groups:

1. Click the **+** (plus).
   
2. Name the group.
   
3. Click the **✓** (checkmark) to save.
   

* * *

### Add users to the group

Select **Add users to this group** to add existing users to this group.

Alternatively, you can invite new users into this group directly by clicking **Invite user**.

![Add users to a group](/assets/users-add.D8M17rlT.png)_Add users to a group_

* * *

### Edit/delete a user

This interface enables you to edit a user's name and the groups to which they belong.

You can also delete users. Deleted users lose access to the Workflow apps portal.

To edit a user:

1. Click the user name you plan to edit.
   
2. Make the necessary changes.
   
3. Select **Save changes**.
   

To delete a user:

1. Click the user name you plan to delete.
   
   Alternatively, click the **☑** (checkbox) to the left of the user name.
   
2. Click **Delete user**.
   

> **FURTHER READING**
> 
> - [Learn how to set up the Workflow apps portal](/en/workflow-apps/portal-settings)

---
