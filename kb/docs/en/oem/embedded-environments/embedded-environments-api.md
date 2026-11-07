---
url: >-
  https://docs.workato.com/en/oem/embedded-environments/embedded-environments-api.md
description: >-
  Use Embedded APIs with Environments by targeting the Development, Test, or
  Production workspace ID for each managed customer.
---

# Embedded Environments APIs

[Embedded APIs](/en/oem/oem-api) are fully compatible with Embedded Environments. You can continue to use the same Embedded API across all environments by targeting the appropriate workspace ID. When provisioning Environments for an existing Embedded Customer, their original workspace ID becomes the Development workspace ID, and two new IDs are generated for the TEST and PROD Environments.

## Embedded APIs with and without Environments

The base URL for all Embedded API interactions is:

`.../api/managed_users/`

Append the `managed_user_id` to this base URL to interact with a specific customer. This allows you to manage each environment for customers with Environments provisioned by pointing to each workspace ID. If the customer doesn't have Environments provisioned, you can use the URL `/api/managed_users/:managed_user_id` to interact with a specific customer.

> **WORKSPACE ID REPRESENTATION FOR PROVISIONED AND NON-PROVISIONED ENVIRONMENTS**
> 
> The `managed_user_id` represents the Workspace ID when Environments is not provisioned. The `managed_user_id` represents each environment ID (Development, Test, or Production) when Environments is provisioned. To find the `managed_user_id`: click **Workspace Admin > Settings > Workspace ID**.
> 
> Use the following API endpoints to target a specific environment within a customer's account:
> 
> - **Development environment:**`/api/managed_users/:managed_user_id_dev`
>   
> - **Test environment:** `/api/managed_users/:managed_user_id_test`
>   
> - **Production environment:** `/api/managed_users/:managed_user_id_prod`
>   
> 
> When you provision Environments for an existing customer, their original `:managed_user_id` is designated for the Development environment (`:managed_user_id_dev`). New unique identifiers are generated for the Test and Production environments (`:managed_user_id_test` and `:managed_user_id_prod`, respectively). This ensures that each environment is independently accessible and manageable through the API, providing precise control over the deployment and operation of integrations across different development stages.

## Provision Environments programmatically

You can provision the Environments feature programmatically for new and existing managed customers. Refer to the [Embedded APIs Environments](/en/oem/oem-api/managed-users#provision-environments) section for more information.

## How to get the correct ID

You can retrieve the IDs for your customers' environments using the [Get List Of Customers API](/en/oem/oem-api/managed-users#get-list-of-customer-accounts).

When listing your customers, those with Environments provisioned return the new property `environments` with the PROD and TEST environments IDs.

### Sample request

```shell
curl  -X GET https://app.workato.com/api/managed_users \
      -H 'Authorization: Bearer <api_token>'
```

### Response

```json
{
        {
            "id": 29727, //this is the used_id for a customer without ENVs
            "external_id": null,
            "name": "new",
            "environments": [],
            "notification_email": "virginia2@workato.com",
            ...
        },
        {
            "id": 29833, //this is the used_id_dev for a customer with ENVs
            "external_id": null,
            "name": "Alex",
            "environments": [
                {
                    "id": 29835, //this is the used_id_prod for a customer with ENVs
                    "environment_type": "prod"
                },
                {
                    "id": 29834, //this is the used_id_test for a customer with ENVs
                    "environment_type": "test"
                }
            ],
            "notification_email": "alex@workato.com",
           ...
        },
}
```

## External IDs for environments

You can also specify unique external IDs for each of your customers' environments. External IDs enable you to manage customers programmatically in the same way as you do for customers without Environments.

To add an external ID, you can either [Update the customer through the API](/en/oem/oem-api/managed-users#update-customer-account-member) or add it through the UI:

1. Navigate to **Manage customers**.
   
2. Click **Settings > External IDs**.
   

## Exclusive development environment access

Certain API endpoints, designed for development activities like collaborator management, are exclusively accessible within the Development environment. An error displays if you try to access these endpoints from your TEST or PROD environments.

For example:

### Sample request

```shell
curl  -X POST https://app.workato.com/api/managed_users/:managed_user_id_test \
      -H 'Authorization: Bearer <api_token>'
```

### Response

```json
{
    "message": "Not Available for Environment"
}
```
