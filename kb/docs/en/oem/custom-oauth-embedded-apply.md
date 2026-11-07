---
url: 'https://docs.workato.com/en/oem/custom-oauth-embedded-apply.md'
description: >-
  Apply a custom OAuth profile from your Embedded Admin workspace to specific
  customer workspaces, replacing the default profile.
---

# Apply a custom OAuth profile to customer workspaces

After you create a custom OAuth profile and register an application in your Admin workspace, you can apply this OAuth profile to specific customer workspaces. When applied at the Admin level, this profile replaces the OAuth profile for the same application by default in customer workspaces.

> **PREREQUISITES**
> 
> You must [create a custom OAuth profile](/en/oem/custom-oauth-embedded-create) for your application before you can apply a profile to a customer workspace.

## OAuth assignment process

You must apply an OAuth profile to each individual customer workspace.

To apply an OAuth profile:

1. Navigate to the **Admin console > Customer settings**.
   
2. Select the customer you plan to assign an OAuth profile to.
   
3. Navigate to the customer's **Settings > Custom OAuth profiles** interface.
   
   ![Assign a profile](/assets/custom-oauth-embedded-assign-step1.olLwuVq3.png)_Custom OAuth profiles interface_
   
4. Click **Assign a profile**.
   
5. In the **Assign an OAuth profile** interface select an app and profile to assign to the customer.
   
   You can only have one OAuth profile for each application.
   
   ![Assign a profile](/assets/custom-oauth-embedded-assign-step2.BnP-3aG7.png)_Assign a profile_
   
6. Click **Confirm**.
   

## Important considerations

After you share a custom OAuth profile with a customer, that profile is automatically adopted for that connector and the customer cannot switch to another connector.

When a user in a customer workspace makes a connection to an app that has a shared custom OAuth profile from the admin workspace, the Custom OAuth profile drop-down is disabled. For example, in the following screenshot, the Custom OAuth field is grayed out.

![Disabled field](/assets/custom-oauth-embedded-assign-field.Cwn_jkEQ.png)_Disabled custom OAuth field_

> **HIDE CUSTOM OAUTH PROFILE FIELD**
> 
> You can hide the **Custom OAuth profile field** if you do not want it to be visible to customers. You can hide this field through the customer workspace plan. This field is only visible if the customer workspace plan includes access to the Custom OAuth profiles feature. If an admin sets a custom OAuth profile for this customer, the customer can use it even if they do not have access to the Custom OAuth feature.

You can only set one custom OAuth profile for an application for each customer. If you want to change to a different OAuth profile and have active connections in that customer workspace, Workato displays the following warning message.

![Warning message](/assets/custom-oauth-embedded-assign-warning.BuvOLC6i.png)_Warning message_

Workato displays a similar warning when you delete an OAuth profile from the customer workspace.

## Example user flow

1. An Embedded partner registers a Hubspot custom OAuth profile in the Admin account.
2. The partner enables the profile in the **Admin console > Customers > Settings > Custom OAuth profiles**.
3. Anyone in that customer workspace that creates a connection to Hubspot immediately uses the custom OAuth profile created at the partner account level when they try to connect to Hubspot. The customer cannot select anything in the **Custom OAuth profile** field.

---
