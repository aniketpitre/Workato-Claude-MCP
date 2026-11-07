---
url: >-
  https://docs.workato.com/en/oem/embedded-environments/provision-embedded-environments.md
description: >-
  Provision the Environments feature for individual Embedded customers and
  assign collaborator roles per environment in your Workato workspace.
---

# Provision Embedded Environments for customers

You must provision the Environments feature for each customer individually. You can define different roles in each environment for a single collaborator. Customer Managers have access to all environments with the same role.

> **ENVIRONMENTS PROVISIONING CANNOT BE UNDONE**
> 
> After Environments are enabled for a customer, this configuration becomes a permanent account enhancement. It is not possible to revert to a single workspace setup.

## Provision Environments for existing customers

1. Sign in to your Workato account.
   
2. Click **Manage customers** in the sidebar navigation menu.
   
3. Select the customer you plan to provision Environments for in the **Admin console** customer table.
   
4. Click **Settings > Plan**.
   
5. Click **Get started** in the **Provision environments for your customers** box. The Provision Environments pop-up box opens with an overview of the Environments feature.
   
   ![Provision an existing customer](/assets/provision-existing-customers.CyE40ILX.png)_Provision Environments to an existing customer_
   
6. Click **Provision environments** in the pop-up box to confirm your selection.
   

> **VERIFY ACCESS POST-ENVIRONMENT PROVISIONING**
> 
> After provisioning Environments for an existing customer, it is crucial to review and adjust Role-Based Access Control (RBAC) settings to ensure that your collaborators are granted the appropriate access across all environments (Development, Test, and Production).

After provisioning Environments for an existing customer, their pre-existing workspace becomes their **Production** workspace, which includes all running recipes. Additionally, empty **Development** and **Test** environments are created. Recipes don't stop running at any point during the process.

## Provision Environments for new customers

1. Sign in to your Workato account.
   
2. Click **Manage customers** in the sidebar navigation menu.
   
3. Click **Add customer**.
   
4. Enter a **Name** and **Notification email**, and select a **Plan** for the customer.
   
5. Ensure the **Provision environments** toggle is on.
   
6. Click **Add customer**.
   
   ![Provision a new customer](/assets/provision-environments-new-customer.zDzGMNiV.png)_Provision Environments to a new customer_
   

## Provision Environments programmatically

You can provision the Environments feature programmatically for managed customers by using the boolean parameter `provision_environments`. Set this parameter to `true` to provision the Environments feature for a managed customer.

### Sample request

```shell

curl -X POST 'https://app.workato.com/api/managed_users/:managed_user_id/' \
      -H 'Authorization: Bearer <api_token>'
```

**Body**

```shell
{
    "name":"Example managed customer",
    "notification_email": "TC@test.com",
    "provision_environments": true
}
```

### Sample response

```shell
{
    "id": 209,
    "external_id": null,
    "name": "Example managed customer",
    "environments": [
        {
            "id": 211,
            "environment_type": "prod",
            "external_id": null
        },
        {
            "id": 210,
            "environment_type": "test",
            "external_id": null
        },
        {
            "id": 209,
            "environment_type": "dev",
            "external_id": null
        }
    ],
    "notification_email": "TC@test.com",
    "full_embedding": null,
    "admin_notification_emails": "TC@test.com",
    "error_notification_emails": "TC@test.com",
    "plan_id": "wrike_integrate",
    "origin_url": null,
    "trial": false,
    "in_trial": false,
    "whitelisted_apps": [],
    "frame_ancestors": null,
    "created_at": "2024-05-17T00:48:23.454-07:00",
    "updated_at": "2024-05-17T00:48:23.454-07:00",
    "time_zone": "Pacific Time (US & Canada)",
    "auth_settings": {
        "type": "workato_auth"
    }
```
