---
url: 'https://docs.workato.com/en/oem/oem-api/managed-users.md'
description: >-
  Reference for the Embedded API managed users resource to programmatically
  create, manage, and update customer workspaces.
---

# Embedded API - Manage customers

The **Managed Users** resource provides the ability to programmatically manage customers.

> **EMBEDDED APIS**
> 
> The endpoints in this guide are Embedded APIs and require an Embedded workspace. Contact your Workato representative for more information.

  

> **API CLIENT ACCESS**
> 
> API clients require access to the `DEV` environment to manage [collaborators](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) in an Embedded customer workspace. Refer to [Create a client role](/en/workato-api/api-clients#create-an-api-client) to configure an API client's access.

## Rate limits

Manage customers resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Create customer: [/api/managed\_users](/en/oem/oem-api/managed-users.html#create-customer-account) | 1,000 requests per minute |
| DELETE | Remove member from customer workspace: [/api/managed\_users/:id/members /:member\_id](/en/oem/oem-api/managed-users.html#remove-member-from-customer-account) | 1,000 requests per minute |
| POST | Provision environments: [/api/managed\_users/:id/environments](/en/oem/oem-api/managed-users.html#provision-environments) | 1,000 requests per minute |
| All | All [Usage](/en/oem/oem-api/managed-users.html#get-usage-v2) endpoints | 1,000 requests per minute |
| All | All other [Members](/en/oem/oem-api/managed-users.html#get-list-of-customer-account-members) endpoints | 60 requests per minute |
| All | All other [Manage customers](/en/oem/oem-api/managed-users.html) endpoints | 60 requests per minute |

### Quick reference

The Managed Users resource contains the following endpoints:

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users](#create-customer-account) | Create a customer. |
| PUT | [/api/managed\_users/:managed\_user\_id](#update-customer-account) | Update a customer. |
| DELETE | [/api/managed\_users/:managed\_user\_id](#delete-customer-account) | Delete a customer. |
| GET | [/api/managed\_users/:managed\_user\_id](#get-customer-account) | Get a customer. |
| GET | [/api/managed\_users](#get-list-of-customer-accounts) | List all customers. |
| GET | [/api/managed\_users/:id/members](#get-list-of-customer-account-members) | Get a list of collaborators in a customer workspace. |
| GET | [/api/managed\_users/:id/members/:member\_id](#get-customer-account-member) | Get customer workspace collaborator details. |
| POST | [/api/managed\_users/:id/members](#add-member-to-customer-account) | Add collaborator to customer workspace. |
| PUT | [/api/managed\_users/:id/members/:member\_id](#update-customer-account-member) | Update a customer workspace collaborator. |
| DELETE | [/api/managed\_users/:id/members/:member\_id](#remove-member-from-customer-account) | Remove collaborator from customer workspace. |
| GET | [/api/managed\_users/:id/members/:member\_id/project\_grants](#list-project-grants) | List a customer workspace collaborator's project grants. |
| GET | [/api/managed\_users/:id/connections](#list-customer-connections) | List connections in a customer workspace. |
| GET | [/api/managed\_users/:id/members/:member\_id/privileges](#get-list-of-customer-privileges) | Get privileges from a customer workspace collaborator. |
| GET | [/api/managed\_users/:managed\_user\_id/members/:id/projects\_privileges](#get-project-privileges) | Get projects privileges from a customer workspace collaborator. |
| POST | [/api/v2/managed\_users/statistics/usage](#get-usage-v2) | Retrieve usage metrics for customer workspaces with enhanced data granularity. |
| POST | [/api/v2/managed\_users/statistics/connection\_usage](#get-connection-based-usage) | Retrieve connection-based usage metrics for specified customer workspaces. |
| GET | [/api/managed\_users/usage](#get-monthly-usage) | Get task usage of all customers by month. |
| POST | [/api/managed\_users/:managed\_user\_id/environments](#provision-environments) | Provision Environments for an existing customer. Any existing assets in the customer workspace are placed in the **Development** environment after provisioning. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/environments](#provision-environments-v2) | Provision Environments (v2) for an existing customer. Any existing assets in the customer workspace are placed in the **Production** environment after provisioning. |
| GET | [/api/v2/managed\_users/environments\_provision\_tasks/:id](#get-status-of-environment-provisioning) | Get the status of asynchronous environment provisioning. |
| GET | [/api/v2/managed\_users/customer\_categories](#get-list-of-customer-categories) | List customer categories in an Embedded partner's workspace. |
| POST | [/api/v2/managed\_users/customer\_categories](#create-a-customer-category) | Create a customer category. |
| PUT | [/api/v2/managed\_users/customer\_categories/:id](#update-a-customer-category) | Update a customer category. |
| DELETE | [/api/v2/managed\_users/customer\_categories/:id](#delete-a-customer-category) | Delete a customer category. |
| POST | [/api/v2/managed\_users/customer\_categories/:id/assign](#batch-assign-a-customer-category-to-workspaces) | Batch assign a customer category to workspaces. |
| POST | [/api/v2/managed\_users/customer\_categories/:id/unassign](#batch-unassign-a-customer-category-from-workspaces) | Batch unassign a customer category from workspaces. |
| PUT | /api/managed\_users/:managed\_user\_id/upgrade This endpoint is deprecated. Instead, make a PUT request to the [/api/managed\_users/:managed\_user\_id](#update-customer-account) endpoint and update the customer's `plan ID`. | **Deprecated.** Upgrade a customer. |
| PUT | /api/managed\_users/:managed\_user\_id/downgrade This endpoint is deprecated. Instead, make a PUT request to the [/api/managed\_users/:managed\_user\_id](#update-customer-account) endpoint and update the customer's `plan ID`. | **Deprecated.** Downgrade a customer. |
| POST | /api/managed\_users/:managed\_user\_id/member This endpoint is deprecated. Instead, make a POST request to the [/api/managed\_users/:managed\_user\_id/members](#add-member-to-customer-account) endpoint. | **Deprecated.** Add a member to a customer workspace. |
| DELETE | /api/managed\_users/:managed\_user\_id/member This endpoint is deprecated. Instead, make a DELETE request to the [/api/managed\_users/:managed\_user\_id/members/:member\_id](#remove-member-from-customer-account) endpoint. | **Deprecated.** Remove a member from a customer workspace. |

> **DEPRECATED ENDPOINTS**
> 
> The following endpoints are deprecated:
> 
> - `/api/managed_users/:managed_user_id/upgrade`
> - `/api/managed_users/:managed_user_id/downgrade`
> - `/api/managed_users/:managed_user_id/member`
> 
> You can use the fully supported endpoints listed in the following table:

## Create customer

Creates a new Embedded customer.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users
```

</api-code>

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The full name of the customer. |
| notification\_email | **string** _required_ | The email address for receiving error and administrative notifications. |
| team\_name | **string** _optional_ | The name of the customer workspace. |
| oauth\_id | **string** _optional_ | The identifier used for OAuth authentication. |
| provision\_environments | **boolean** _optional_ | Determines whether the new Embedded customer is provisioned with the Environments feature. Defaults to `false`. |
| external\_id | **string** _optional_ | An external identifier for the Embedded customer. |
| origin\_url | **string** _optional_ | Applies to Embedded account customers. Provide a value if the Embedded iframe is hosted on a non-default origin page, such as customer-specific custom domains. Defaults to the origin configured at the workspace level. |
| frame\_ancestors | **string** _optional_ | A list of comma-separated URLs used as frame ancestors in the Content-Security-Policy HTTP header. This configuration allows the rendering of Workato iframes on the domains you specify. |
| plan\_id | **string** _optional_ | The plan ID. Defaults to the standard plan if not specified. |
| custom\_credit\_limit | **integer** _optional_ | Overrides the credit limit defined in the customer's plan. Pass `0` to reset the credit limit to the plan's value. Applies only to customers whose plan uses credit-based limits. |
| time\_zone | **string** _optional_ | The timezone name. Defaults to PST if not specified. Refer to the [Timezone list](/en/oem/oem-api/timezone-list#timezone-list) for accepted values. |
| whitelisted\_apps | **array of strings** _optional_ | A list of connection [`provider`](/en/oem/oem-api/connections-parameters)s for apps the customer can access. Refer to the [App access](/en/oem/admin-console/customers#app-access) section for details. |
| full\_embedding | **boolean** _optional_ | If true, end users are directed to the customer's `origin_url`. Set to `false` to disable full embedding. Defaults to `null`, inheriting the value (`true` or `false`) from the Embedded partner's admin settings. |
| auth\_settings | **hash** _optional_ | Authentication settings for the customer workspace. |
| auth\_settings\[type\] | **string** _conditional_ | Specifies the authentication type. Accepted values include `workato_auth`, `two_fa_auth`, and `saml_sso`. |
| auth\_settings\[provider\] | **string** _conditional_ | The identity provider name. **Required** if using `saml_sso` as the `auth_settings[type]`. Accepted values include `okta`, `onelogin`, and `others`. |
| auth\_settings \[metadata\_url\] | **string** _conditional_ | The URL of the identity provider's metadata XML file for configuration details. **Required** if `auth_settings[sso_url]`, `auth_settings[saml_issuer]`, and `auth_settings[x509_cert]` are not provided. |
| auth\_settings \[sso\_url\] | **string** _conditional_ | The single sign-on URL provided by the identity provider for user authentication. **Required** if `auth_settings[metadata_url]` is not provided. |
| auth\_settings \[saml\_issuer\] | **string** _conditional_ | A unique identifier for the identity provider, often used to identify the issuer of SAML assertions. **Required** if `auth_settings[metadata_url]` is not provided. |
| auth\_settings \[x509\_cert\] | **string** _conditional_ | The X.509 certificate from the identity provider. This is used to verify SAML assertion signatures. **Required** if `auth_settings[metadata_url]` is not provided. |
| auth\_settings \[jit\_provisioning\] | **boolean** _optional_ | Choose to enable Just-in-Time (JIT) provisioning, allowing Workato to create user accounts upon first sign-in. |
| auth\_settings \[saml\_role\_updates\_allowed\] | **boolean** _optional_ | Determines if role sync with the SAML identity provider is enabled. Defaults to `true`. |
| auth\_settings \[saml\_required\] | **boolean** _optional_ | Indicates if SAML authentication is enforced for the customer. Defaults to `true`. |
| environments | **array of objects** _optional_ | An array of environment objects specifying configurations such as external IDs and error notification emails for each environment. |
| environments \[environment\_type\] | **string** _optional_ | Specifies the environment type for creating customer information. Accepted values include `dev`, `test`, and `prod`, but see the [warning](#400-bad-request) on `dev` inclusion. |
| environments \[external\_id\] | **string** _optional_ | External ID for the `test` or `prod` environments. Use `external_id` in the main request body for the `dev` environment. |
| environments \[error\_notification\_emails\] | **string** _optional_ | Error notification emails for the `test` or `prod` environments. Use `notification_email` in the main request body for the `dev` environment. |
| timeout\_id | **string** _optional_ | Timeout in seconds. The following values are accepted: - `900` (15 minutes) - `1800` (30 minutes) - `2700` (45 minutes) - `14400` (4 hours) - `28800` (8 hours) - `43200` (12 hours) - `86400` (1 day) - `172800` (2 days) - `259200` (3 days) - `604800` (7 days) - `1209600` (14 days) |

  

> **400 BAD REQUEST**
> 
> Avoid providing `environments[error_notification_emails]` and `environments[external_id]` for the `dev` environment.
> 
> If these values conflict with `notification_email` and `external_id` specified in the main request body, the API returns A `400 Bad Request` error due to conflicting assignments for the same attribute.
> 
> Instead, use `notification_email` and `external_id` for the `dev` environment and reserve `environments[error_notification_emails]` and `environments[external_id]` for the `test` and `prod` environments.

### Sample requests

- [Request with Workato authentication](#request-with-workato-authentication)
- [Request with SAML SSO and metadata URL](#request-with-saml-sso-and-metadata-url)
- [Request with SAML SSO and X509 cert](#request-with-saml-sso-and-x509-cert)

#### Request with Workato authentication

This example request creates a new Embedded customer using Workato authentication.

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "team_name": ":team_name",
            "notification_email": ":notification_email",
            "provision_environments": :true_or_false,
            "external_id": ":external_id",
            "whitelisted_apps": [":whitelisted_apps_1", ":whitelisted_apps_2"],
            "time_zone": ":time_zone",
            "auth_settings": {
                "type": "workato_auth"
            },
            "full_embedding": :true_or_false,
            "environments": [
                {
                    "environment_type": ":environment_type_1",
                    "external_id": ":external_id",
                    "error_notification_emails": ":error_notification_emails"
                },
                {
                    "environment_type": ":environment_type_2",
                    "external_id": ":external_id",
                    "error_notification_emails": ":error_notification_emails"
                }
            ]
          }'
```

</api-code>

Response: Workato authentication

```json
{
    "id": 32122,
    "external_id": "UU0239093497",
    "name": "Alex Workato",
    "environments": [
        {
            "id": 32124,
            "environment_type": "prod",
            "external_id": "UU0239093499",
            "error_notification_emails": "errors@nutech.com"
        },
        {
            "id": 32123,
            "environment_type": "test",
            "external_id": "UU0239093498",
            "error_notification_emails": "errors@nutech.com"
        },
        {
            "id": 32122,
            "environment_type": "dev",
            "external_id": "UU0239093497",
            "error_notification_emails": "admin@nutech.com"
        }
    ],
    "timeout_id":"43200",
    "notification_email": "admin@nutech.com",
    "full_embedding": false,
    "admin_notification_emails": "admin@nutech.com",
    "error_notification_emails": "admin@nutech.com",
    "plan_id": "oem_enterprise",
    "origin_url": null,
    "trial": false,
    "in_trial": false,
    "whitelisted_apps": [
        "netsuite",
        "salesforce"
    ],
    "frame_ancestors": null,
    "created_at": "2024-12-11T11:04:37.084-08:00",
    "updated_at": "2024-12-11T11:04:37.084-08:00",
    "time_zone": "Central Time (US & Canada)",
    "team_name": "Nutech",
    "auth_settings": {
        "type": "workato_auth",
    },
    "current_billing_period_start": "2024-12-11T11:04:37.084-08:00",
    "current_billing_period_end": "2025-01-11T11:04:37.084-08:00",
    "task_count": 0,
    "active_connection_limit": 0,
    "active_connection_count": 0,
    "active_recipe_count": 0
}
```

#### Request with SAML SSO and metadata URL

This example request creates a new Embedded customer using SAML SSO and the metadata URL. If using this method, the following `auth_settings` fields are required:

- `type`
- `provider`
- `metadata_url`

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "team_name": ":team_name",
            "notification_email": ":notification_email",
            "provision_environments": :true_or_false,
            "external_id": ":external_id",
            "whitelisted_apps": [":whitelisted_apps_1", ":whitelisted_apps_2"],
            "time_zone": ":time_zone",
            "auth_settings": {
                "type": "saml_sso",
                "provider": ":provider",
                "metadata_url: ":metadata_url",
                "saml_role_updates_allowed": :true_or_false,
                "saml_required": :true_or_false
            },
            "full_embedding": :true_or_false,
            "environments": [
                {
                    "environment_type": ":environment_type_1",
                    "external_id": ":external_id",
                    "error_notification_emails": ":error_notification_emails"
                },
                {
                    "environment_type": ":environment_type_2",
                    "external_id": ":external_id",
                    "error_notification_emails": ":error_notification_emails"
                }
            ]
          }'
```

</api-code>

Response: SAML SSO and metadata URL

```json
{
    "id": 32122,
    "external_id": "UU0239093497",
    "name": "Alex Workato",
    "environments": [
        {
            "id": 32124,
            "environment_type": "prod",
            "external_id": "UU0239093499",
            "error_notification_emails": "errors@nutech.com"
        },
        {
            "id": 32123,
            "environment_type": "test",
            "external_id": "UU0239093498",
            "error_notification_emails": "errors@nutech.com"
        },
        {
            "id": 32122,
            "environment_type": "dev",
            "external_id": "UU0239093497",
            "error_notification_emails": "admin@nutech.com"
        }
    ],
    "timeout_id":"43200",
    "notification_email": "admin@nutech.com",
    "full_embedding": false,
    "admin_notification_emails": "admin@nutech.com",
    "error_notification_emails": "admin@nutech.com",
    "plan_id": "oem_enterprise",
    "origin_url": null,
    "trial": false,
    "in_trial": false,
    "whitelisted_apps": [
        "netsuite",
        "salesforce"
    ],
    "frame_ancestors": null,
    "created_at": "2024-12-11T11:04:37.084-08:00",
    "updated_at": "2024-12-11T11:04:37.084-08:00",
    "time_zone": "Central Time (US & Canada)",
    "team_name": "Nutech",
    "auth_settings": {
        "type": "saml_sso",
        "provider": "okta",
        "metadata_url": "https://nutech.okta.com/app/exk29ua5yiqFVszrz0h8/sso/saml/metadata",
        "saml_role_updates_allowed": true,
        "saml_required": true
    },
    "current_billing_period_start": "2024-12-11T11:04:37.084-08:00",
    "current_billing_period_end": "2025-01-11T11:04:37.084-08:00",
    "task_count": 0,
    "active_connection_limit": 0,
    "active_connection_count": 0,
    "active_recipe_count": 0
}
```

#### Request with SAML SSO and X.509 certificate

This example request creates a new Embedded customer using SAML SSO and the X.509 certificate. If using this method, the following `auth_settings` fields are required:

- `type`
- `provider`
- `sso_url`
- `saml_issuer`
- `x509_cert`

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "team_name": ":team_name",
            "notification_email": ":notification_email",
            "provision_environments": :true_or_false,
            "external_id": ":external_id",
            "whitelisted_apps": [":whitelisted_apps_1", ":whitelisted_apps_2"],
            "time_zone": ":time_zone",
            "auth_settings": {
                "type": "saml_sso",
                "provider": ":provider",
                "sso_url": ":sso_url",
                "saml_issuer": ":saml_issuer",
                "x509_cert": ":x509_cert"
            },
            "full_embedding": :true_or_false,
            "environments": [
                {
                    "environment_type": ":environment_type_1",
                    "external_id": ":external_id",
                    "error_notification_emails": ":error_notification_emails"
                },
                {
                    "environment_type": ":environment_type_2",
                    "external_id": ":external_id",
                    "error_notification_emails": ":error_notification_emails"
                }
            ]
          }'
```

</api-code>

Response: SAML SSO and X.509 certificate

```json
{
    "id": 32122,
    "external_id": "UU0239093497",
    "name": "Alex Workato",
    "environments": [
        {
            "id": 32124,
            "environment_type": "prod",
            "external_id": "UU0239093499",
            "error_notification_emails": "errors@nutech.com"
        },
        {
            "id": 32123,
            "environment_type": "test",
            "external_id": "UU0239093498",
            "error_notification_emails": "errors@nutech.com"
        },
        {
            "id": 32122,
            "environment_type": "dev",
            "external_id": "UU0239093497",
            "error_notification_emails": "admin@nutech.com"
        }
    ],
    "timeout_id":"43200",
    "notification_email": "admin@nutech.com",
    "full_embedding": false,
    "admin_notification_emails": "admin@nutech.com",
    "error_notification_emails": "admin@nutech.com",
    "plan_id": "oem_enterprise",
    "origin_url": null,
    "trial": false,
    "in_trial": false,
    "whitelisted_apps": [
        "netsuite",
        "salesforce"
    ],
    "frame_ancestors": null,
    "created_at": "2024-12-11T11:04:37.084-08:00",
    "updated_at": "2024-12-11T11:04:37.084-08:00",
    "time_zone": "Central Time (US & Canada)",
    "team_name": "Nutech",
    "auth_settings": {
        "type": "saml_sso",
        "provider": "okta",
        "sso_url": "https://nutech.okta.com/app/nutech_1/exk21ojjvq6212R6e5d7/sso/saml",
        "saml_issuer": "http://www.okta.com/exk21ojjvq6212R6e5d7",
        "x509_cert": "-----BEGIN CERTIFICATE-----\nMIID...YOUR_CERT_DATA...IDAQAB\n-----END CERTIFICATE-----"
    },
    "current_billing_period_start": "2024-12-11T11:04:37.084-08:00",
    "current_billing_period_end": "2025-01-11T11:04:37.084-08:00",
    "task_count": 0,
    "active_connection_limit": 0,
    "active_connection_count": 0,
    "active_recipe_count": 0
}
```

## Update customer

Updates an existing Embedded customer's information. You can use this endpoint to update specific parameters, such as `external_id` and `error_notification_emails`, in both test and production environments. Include the `environments` key in the request body to specify the environment.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id
```

</api-code>

**Additional notes:**

- For customers on task-based plans, use this endpoint to update the task quota override and make a one-time adjustment.
- For Embedded partners, use this endpoint to update the custom origin URL for a specific customer.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Updated name of the customer workspace. Displays in customer profiles, collaborator views, and audit logs. |
| team\_name | **string** _optional_ | Updated name of the team workspace associated with the customer. Appears in workspace settings, customer management views, and the navigation sidebar for switching between workspaces. |
| notification\_email | **string** _optional_ | Email for error and administrative notifications. |
| error\_notification\_ emails | **string** _optional_ | Emails for error notifications, overriding the value in the `notification_email` property. This property applies specifically to the `dev` environment and differs from `environments[error_notification_emails]`. |
| admin\_notification\_emails | **string** _optional_ | Emails for administrative notifications. This property overrides what you input in notification email property. |
| external\_id | **string** _optional_ | External identifier for the Embedded customer. This field applies specifically to the `dev` environment and differs from `environments[external_id]`. |
| origin\_url | **string** _optional_ | Applies to Embedded customers. Provide a value if the embedded `iframe` is hosted on a custom domain or non-default origin page. Defaults to the origin configured at the account level. |
| frame\_ancestors | **string** _optional_ | Provide one or more comma-separated frame ancestors. These URLs are used in the Content-Security-Policy HTTP header to allow rendering of Workato IFrames. |
| plan\_id | **string** _optional_ | The ID of the plan. |
| in\_trial | **boolean** _optional_ | Switches the user between a free plan and a subscription plan. |
| task\_limit\_ adjustment | **number** _optional_ | Adjusts the task quota for the **current** accounting period. Only valid for task-based plans. This adjustment doesn't apply to subsequent periods. Make a negative adjustment by adding `-`. For example, `-5000`. |
| custom\_task\_limit | **number** _optional_ | Overrides the current plan limit. Limit override **must** result in a value greater than the current task usage. |
| custom\_credit\_ limit | **integer** _optional_ | Overrides the credit limit defined in the customer's plan. Pass `0` to reset the credit limit to the plan's value. Applies only to customers whose plan uses credit-based limits. |
| whitelisted\_apps | **array** _optional_ | A list of connection [`provider`](/en/oem/oem-api/connections-parameters#configuration-parameters-by-connector) values specifying the apps the customer can access. Refer to [Admin Console App access](/en/oem/admin-console/customers#app-access) for more information. |
| time\_zone | **string** _optional_ | Timezone name. View this [document](/en/oem/oem-api/timezone-list) for a list of timezones. Defaults to PST if not specified. |
| auth\_settings | **object** _optional_ | Authentication settings for the customer. Accepted `types` are `workato_auth` and `saml_sso`. When configuring `saml_sso`, accepted `providers` include `okta`, `onelogin`, and `others`. |
| auth\_settings \[saml\_role\_ updates\_allowed\] | **boolean** _optional_ | Determines if role sync with the SAML identity provider is enabled. Defaults to `true`. |
| auth\_settings \[saml\_required\] | **boolean** _optional_ | Indicates if SAML authentication is enforced. Defaults to `true`. |
| current\_billing\_ period\_start | **string** _optional_ | Set the current billing start date. The date should be provided in ISO 8601 format. |
| full\_embedding | **boolean** _optional_ | When set to `true`, end users are sent to the customer's `origin_url`. Set this field to `false` to disable the fully embedded redirect process at the customer workspace level. If you don't specify this value, it defaults to `null` and inherits the value (`true` or `false`) from the Embedded partner's admin settings. |
| environments | **array of objects** _optional_ | An array of environment objects specifying where to update the customer's information, including the external ID and error notification emails for each environment. |
| environments \[environment\_type\] | **string** _required_ | Specifies the environment type for updating customer information. Accepted values include `test` and `prod`. |
| environments \[external\_id\] | **string** _optional_ | The updated external ID specific to each environment (`test` or `prod`). This field differs from the `external_id` in the main request body, applying only to the specified environments. |
| environments \[error\_notification\_ emails\] | **string** _optional_ | Specifies updated error notification emails for each environment (`test` or `prod`). This field differs from `error_notification_emails` in the main request body, applying only to the specified environments. |
| timeout\_id | **string** _optional_ | Timeout in seconds. The following values are accepted: - `900` (15 minutes) - `1800` (30 minutes) - `2700` (45 minutes) - `14400` (4 hours) - `28800` (8 hours) - `43200` (12 hours) - `86400` (1 day) - `172800` (2 days) - `259200` (3 days) - `604800` (7 days) - `1209600` (14 days) |

> **PROPERTIES**
> 
> Properties update only if the payload includes the property. To clear a property’s value, set it to `null` in the payload.

### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "team_name": ":team_name",
            "notification_email": ":notification_email",
            "admin_notification_emails": ":admin_notification_emails",
            "error_notification_emails": ":error_notification_emails",
            "in_trial": :true_or_false,
            "task_limit_adjustment": :task_limit_adjustment,
            "custom_task_limit": :custom_task_limit,
            "current_billing_period_start": ":current_billing_period_start",
            "environments": [
                {
                    "environment_type": ":environment_type_1",
                    "external_id": ":external_id",
                    "error_notification_emails": ":error_notification_emails"
                },
                {
                    "environment_type": ":environment_type_2",
                    "external_id": ":external_id",
                    "error_notification_emails": ":error_notification_emails"
                }
            ],
            "external_id": ":external_id",
            "origin_url": ":origin_url",
            "frame_ancestors": ":frame_ancestors",
            "plan_id": ":plan_id",
            "time_zone": ":time_zone",
            "whitelisted_apps": [
                ":whitelisted_apps_1",
                ":whitelisted_apps_2"
            ],
            "auth_settings": {
                "type": ":type",
                "provider": ":provider",
                "metadata_url": ":metadata_url",
                "saml_role_updates_allowed": :true_or_false,
                "saml_required": :true_or_false
            },
            "full_embedding": :true_or_false
        }'
```

</api-code>

### Response

```json
{
    "id": 3498583,
    "external_id": "ext-ect-dev-13",
    "name": "Nutech",
    "environments": [
        {
            "id": 3498585,
            "environment_type": "prod",
            "external_id": "ext-ec-prod-15",
            "error_notification_emails": "errorprod15@gmail.com"
        },
        {
            "id": 3498584,
            "environment_type": "test",
            "external_id": "ext-ec-test-22",
            "error_notification_emails": "errortest22@gmail.com"
        },
        {
            "id": 3498583,
            "environment_type": "dev",
            "external_id": "ext-ect-dev-13",
            "error_notification_emails": "errordev13@gmail.com"
        }
    ],
    "timeout_id":"43200",
    "notification_email": "notifications@dev.com,errordev13@gmail.com",
    "full_embedding": true,
    "admin_notification_emails": "notifications@dev.com",
    "error_notification_emails": "errordev13@gmail.com",
    "plan_id": "oem_enterprise",
    "origin_url": "https://abc123.acme.com",
    "trial": false,
    "in_trial": false,
    "whitelisted_apps": [
        "salesforce",
        "workday"
    ],
    "frame_ancestors": "https://mysite.test.com",
    "created_at": "2024-10-30T09:56:46.060-07:00",
    "updated_at": "2024-11-13T15:27:40.360-08:00",
    "time_zone": "Amsterdam",
    "team_name": "Nutech team workspace",
    "auth_settings": {
        "type": "workato_auth"
        "provider": "okta",
        "metadata_url": "https://nutech.okta.com/sso/metadata",
        "saml_role_updates_allowed": true,
        "saml_required": true
    },
    "current_billing_period_start": "2024-11-01T00:00:00.000-07:00",
    "current_billing_period_end": "2024-11-30T23:00:00.000-08:00",
    "task_count": 0,
    "active_connection_limit": 0,
    "active_connection_count": 3,
    "active_recipe_count": 0,
    "current_billing_period_start": "2024-11-01"
}
```

## Delete customer

Deletes an Embedded customer.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id
```

</api-code>

> **ACCOUNT RECOVERABILITY**
> 
> After you delete a customer account, it can't be fully recovered. Use caution when using this endpoint.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

#### Sample request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
{
    "success": true
}
```

## Get customer

Retrieve details about an Embedded customer's account.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

#### Responses

- [Without environments](#get-customer-without-environments)
- [With environments](#get-customer-with-environments)

> **CREDIT LIMIT FIELD**
> 
> The `credit_limit` field returns the customer's credit limit if their plan uses credit-based limits. For all other customers, this field returns `null`.

#### Without environments

```json
{
    "id": 27819,
    "external_id": null,
    "name": "ACME Automations",
    "environments": [],
    "notification_email": "team@acme.com",
    "full_embedding": null,
    "admin_notification_emails": "team@acme.com",
    "error_notification_emails": "team@acme.com",
    "plan_id": "oem_enterprise",
    "origin_url": null,
    "trial": false,
    "in_trial": false,
    "whitelisted_apps": [],
    "frame_ancestors": null,
    "created_at": "2024-10-02T16:16:14.512-07:00",
    "updated_at": "2024-10-02T16:16:14.512-07:00",
    "time_zone": "Pacific Time (US & Canada)",
    "team_name": "ACME team workspace",
    "auth_settings": {
        "type": "workato_auth"
    },
    "current_billing_period_start": "2024-10-02T16:16:14.689-07:00",
    "current_billing_period_end": "2024-11-02T16:16:14.689-07:00",
    "credit_limit": null,
    "task_count": 0,
    "active_connection_limit": 0,
    "active_connection_count": 0,
    "active_recipe_count": 0
}
```

#### With environments

```json
{
    "id": 27819,
    "external_id": null,
    "name": "ACME Automations",
    "environments": [
        {
            "id": 27821,
            "environment_type": "prod",
            "external_id": null
        },
        {
            "id": 27820,
            "environment_type": "test",
            "external_id": null
        },
        {
            "id": 27819,
            "environment_type": "dev",
            "external_id": null
        }
    ],
    "notification_email": "team@acme.com",
    "full_embedding": null,
    "admin_notification_emails": "team@acme.com",
    "error_notification_emails": "team@acme.com",
    "plan_id": "oem_enterprise",
    "origin_url": null,
    "trial": false,
    "in_trial": false,
    "whitelisted_apps": [],
    "frame_ancestors": null,
    "created_at": "2024-10-02T16:16:14.512-07:00",
    "updated_at": "2024-10-02T16:16:14.512-07:00",
    "time_zone": "Pacific Time (US & Canada)",
     "team_name": "ACME team workspace",
    "auth_settings": {
        "type": "workato_auth"
    },
    "current_billing_period_start": "2024-10-02T16:16:14.689-07:00",
    "current_billing_period_end": "2024-11-02T16:16:14.689-07:00",
    "credit_limit": null,
    "task_count": 0,
    "active_connection_limit": 0,
    "active_connection_count": 0,
    "active_recipe_count": 0
}
```

## Get list of customers

Get a list of all customers. This endpoint returns the data in the [customer table of the Admin Console](/en/oem/admin-console/customers#customer-table).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **number** _optional_ | Page number. Defaults to 1. |
| per\_page | **number** _optional_ | Page size. Defaults to 100 (maximum is 100). |
| category\_id | **number** _optional_ | Filter customers by their category ID. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/ \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

- [Without environments](#get-list-of-customers-without-environments)
- [With environments](#get-list-of-customers-with-environments)

> **CREDIT LIMIT FIELD**
> 
> The `credit_limit` field in the response returns the customer's credit limit if their plan uses credit-based limits. For all other customers, this field returns `null`.

> **TASK COUNT FOR BILLING PERIOD**
> 
> The task count provided by this endpoint represents the number of tasks completed during the customer's billing period.

#### Without environments

```json
{
    "result": [
        {
            "id": 27819,
            "external_id": null,
            "name": "ACME Automations",
            "environments": [],
            "notification_email": "team@acme.com",
            "full_embedding": null,
            "admin_notification_emails": "team@acme.com",
            "error_notification_emails": "team@acme.com",
            "plan_id": "oem_enterprise",
            "origin_url": null,
            "trial": false,
            "in_trial": false,
            "whitelisted_apps": [],
            "frame_ancestors": null,
            "created_at": "2024-10-02T16:16:14.512-07:00",
            "updated_at": "2024-10-02T16:16:14.512-07:00",
            "time_zone": "Pacific Time (US & Canada)",
            "team_name": "ACME team workspace",
            "auth_settings": {
                "type": "workato_auth"
            },
            "current_billing_period_start": "2024-10-02T16:16:14.689-07:00",
            "current_billing_period_end": "2024-11-02T16:16:14.689-07:00",
            "credit_limit": null,
            "task_count": 0,
            "active_connection_limit": 0,
            "active_connection_count": 0,
            "active_recipe_count": 0
        },
        ...
    ]
}
```

#### With environments

```json
{
    "result": [
        {
            "id": 27819,
            "external_id": null,
            "name": "ACME Automations",
            "environments": [
                {
                    "id": 27821,
                    "environment_type": "prod",
                    "external_id": null
                },
                {
                    "id": 27820,
                    "environment_type": "test",
                    "external_id": null
                },
                {
                    "id": 27819,
                    "environment_type": "dev",
                    "external_id": null
                }
            ],
            "notification_email": "team@acme.com",
            "full_embedding": null,
            "admin_notification_emails": "team@acme.com",
            "error_notification_emails": "team@acme.com",
            "plan_id": "oem_enterprise",
            "origin_url": null,
            "trial": false,
            "in_trial": false,
            "whitelisted_apps": [],
            "frame_ancestors": null,
            "created_at": "2024-10-02T16:16:14.512-07:00",
            "updated_at": "2024-10-02T16:16:14.512-07:00",
            "time_zone": "Pacific Time (US & Canada)",
            "team_name": "ACME team workspace",
            "auth_settings": {
                "type": "workato_auth"
            },
            "current_billing_period_start": "2024-10-02T16:16:14.689-07:00",
            "current_billing_period_end": "2024-11-02T16:16:14.689-07:00",
            "credit_limit": null,
            "task_count": 0,
            "active_connection_limit": 0,
            "active_connection_count": 0,
            "active_recipe_count": 0
        }
        ...
    ]
}
```

## Get a list of collaborators in a customer workspace

Retrieves a list of all [collaborators](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) in an Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
[
  {
    "id": 1680,
    "grant_type": "team",
    "role_name": "Admin",
    "external_id": null,
    "name": "Rosario",
    "email": "rosario@example.com",
    "time_zone": "Pacific Time (US & Canada)",
    "user_groups": [
      {
        "id": "ug-APHDLfHB-dTXBtz",
        "name" : "All collaborators",
        "system": true
      },
      {
        "id": "ug-APHDLfHB-dTXBtg",
        "name" : "Developers",
        "system": false
      }
    ],
    "env_roles": [
      {
        "environment_type": "dev",
        "name": "Admin",
        "role_type": "privilege_group"
      }
    ]
  },
  {
    "id": 2641,
    "grant_type": "customer_manager",
    "role_name": "Admin",
    "external_id": null,
    "name": "Noam",
    "email": "noam@example.com",
    "time_zone": "Eastern Time (US & Canada)",
    "user_groups": [
      {
        "id": "ug-APHDLfHB-dTXBtz",
        "name" : "All collaborators",
        "system": true
      }
    ],
    "env_roles": [
      {
        "environment_type": "dev",
        "name": "Admin",
        "role_type": "privilege_group"
      }
    ]
  }
]
```

## Get customer workspace collaborator details

Retrieves a [collaborator](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) from an Embedded customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| member\_id | **string** _required_ | The ID of the collaborator to retrieve. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "id": 1680,
  "grant_type": "team",
  "role_name": "Admin",
  "external_id": null,
  "name": "Noam",
  "email": "noam@example.com",
  "time_zone": "Pacific Time (US & Canada)",
  "user_groups": [
    {
      "id": "ug-APHDLfHB-dTXBtz",
      "name" : "All collaborators",
      "system": true
    },
    {
      "id": "ug-APHDLfHB-dTXBtg",
      "name" : "Developers",
      "system": false
    }
  ],
  "env_roles": [
    {
      "environment_type": "dev",
      "name": "Admin",
      "role_type": "privilege_group"
    }
  ]
}
```

## Add collaborator to customer workspace

Adds a [collaborator](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) to the specified Embedded customer workspace. Alternatively, you can use the [Invite a collaborator to a managed customer workspace](/en/oem/oem-api/team#invite-collaborator-to-managed-customer-account) endpoint to invite a collaborator.

> **RBAC 2.0 MIGRATION**
> 
> This endpoint's payload and response change after the customer workspace migrates to the new role-based access control model. Refer to [RBAC 2.0 migration - Developer and Embedded API changes](/en/user-accounts-and-teams/role-based-access/rbac2-migration-api-changes) for details.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| role\_name | **string** _conditional_ | The role to assign the member. **Required** if `env_roles` is not provided. |
| name | **string** _conditional_ | The full name of the member. **Required** when creating a new user to add to an embedded workspace. |
| env\_roles | **object** _conditional_ | The environment roles object. **Required** if `role_name` is not provided. |
| env\_roles\[environment\_type\] | **string** _conditional_ | The type of environment in the customer workspace where you plan to add the member. **Required** if `role_name` is not provided. Use `dev` for single-environment workspaces. |
| env\_roles\[name\] | **string** _conditional_ | The role to assign the member for the specific environment. **Required** if `role_name` is not provided. |
| env\_roles\[role\_type\] | **string** _optional_ | The type of role to assign the collaborator. Accepted values include `privilege_group` and `environment`. The default value is `privilege_group`. |
| oauth\_id | **string** _optional_ | The identifier used for OAuth. |
| external\_id | **string** _optional_ | The external identifier for the member. |
| time\_zone | **string** _optional_ | The timezone name. Refer to the [Timezone list](/en/oem/oem-api/timezone-list#timezone-list) section for more information. Defaults to PST if not specified. |
| locale | **string** _optional_ | The locale for the member's language preference (for example, `en` for English or `de` for German). |

> **SPECIFY ROLES FOR DIFFERENT ENVIRONMENTS**
> 
> You must provide either `role_name` or `env_roles` in the request body:
> 
> - `role_name` assigns a role in the `dev` environment only.
>   
> - `env_roles` lets you specify roles for different environments.
>   
> 
> You can't combine `role_name` and `env_roles` in the same request. If both are included, Workato assigns only the roles in `env_roles` and ignores `role_name`.

  

> **ADD AN EXISTING USER**
> 
> You must provide the `oauth_id` and omit the following parameters to add an existing Workato user to an Embedded workspace:
> 
> - `role_name`
> - `external_id`
> - `time_zone`
> - `name`
> - `locale`

### Sample requests

Refer to the following sections to add collaborators to specific environments:

- [Assign the dev environment using role\_name](#role-name)
- [Assign specific environments using env\_roles](#env-roles)

#### Using role\_name

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "role_name": ":role_name",
            "external_id": ":external_id"
         }'
```

</api-code>

Response: Using role\_name

```json
{
  "data": {
    "id": 12341,
    "grant_type": "team",
    "role_name": "Admin",
    "external_id": "UU0239093499",
    "name": "Jack Smith",
    "email": "jack@example.com",
    "time_zone": "Pacific Time (US & Canada)",
    "created_at": "2024-09-13T07:26:48.779-07:00",
    "last_activity_log": null
  }
}
```

#### Using env\_roles

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "env_roles": [
                {
                  "environment_type": ":environment_type_1",
                  "name": ":role_name_1",
                  "role_type": ":role_type_1"
                },
                {
                  "environment_type": ":environment_type_2",
                  "name": ":role_name_2",
                  "role_type": ":role_type_2"
                },
                {
                  "environment_type": ":environment_type_3",
                  "name": ":role_name_3",
                  "role_type": ":role_type_3"
                }
            ],
            "external_id": ":external_id"
         }'
```

</api-code>

Response: Using env\_roles

```json
{
  "data": {
    "id": 12341,
    "grant_type": "team",
    "role_name": "Admin",
    "external_id": "UU0239093499",
    "name": "Jack Smith",
    "email": "jack@example.com",
    "time_zone": "Pacific Time (US & Canada)",
    "created_at": "2024-09-24T08:06:09.883-07:00",
    "last_activity_log": null,
    "env_roles": [
      {
        "environment_type": "dev",
        "name": "Admin",
        "role_type": "privilege_group"
      },
      {
        "environment_type": "test",
        "name": "Admin",
        "role_type": "privilege_group"
      },
      {
        "environment_type": "prod",
        "name": "Admin",
        "role_type": "privilege_group"
      }
    ]
  }
}
```

## Update customer workspace collaborator

Updates an existing collaborator and their [roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#key-roles) in an Embedded customer workspace. After migration, this endpoint's payload and response change. Refer to [RBAC 2.0 migration - Developer and Embedded API changes](/en/user-accounts-and-teams/role-based-access/rbac2-migration-api-changes) for details.

> **UPDATE MEMBER RESTRICTION**
> 
> You can update the `role_name` field for any member, whether they were added manually or through the API.
> 
> However, you can only update the following fields for collaborators who don't have their own Workato workspace:
> 
> - `oauth_id`
> - `external_id`
> - `time_zone`
> - `name`
> - `locale`
> 
> These users exist only as collaborators in Embedded customer workspaces and don't own standalone Workato accounts.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| member\_id | **string** _required_ | The member ID or external member ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | The updated full name of the member. |
| role\_name | **string** _optional_ | The updated role to assign the member. You cannot include both `role_name` and `env_roles` in the same request. |
| env\_roles | **object** _optional_ | Defines the collaborator's updated environment roles. You cannot include both `env_roles` and `role_name` in the same request. |
| env\_roles\[environment\_type\] | **string** _optional_ | The type of workspace environment where you plan to update the collaborator's roles. Use `dev` for single-environment workspaces. |
| env\_roles\[name\] | **string** _optional_ | The role to assign the collaborator for the specific environment. |
| env\_roles\[role\_type\] | **string** _optional_ | The type of role to assign the collaborator. Accepted values include `privilege_group` and `environment`. The default value is `privilege_group`. |
| oauth\_id | **string** _optional_ | The updated identifier used for OAuth. |
| external\_id | **string** _optional_ | The updated external identifier for the member. |
| time\_zone | **string** _optional_ | The updated timezone name. Refer to the [Timezone list](/en/oem/oem-api/timezone-list#timezone-list) section for more information. Defaults to PST if not specified. |
| locale | **string** _optional_ | The updated locale for the member's language preference (for example, `en` for English or `de` for German). |

> **SPECIFY ROLES FOR DIFFERENT ENVIRONMENTS**
> 
> You can't combine `role_name` and `env_roles` in the same request. If both are included, Workato assigns only the roles in `env_roles` and ignores `role_name`.
> 
> - `role_name` assigns a role in the `dev` environment only.
> - `env_roles` lets you specify roles for different environments.

### Sample requests

Refer to the following sections to add collaborators to specific environments:

- [Assign the dev environment using role\_name](#update-role-name)
- [Assign specific environments using env\_roles](#update-env-roles)

#### Using role\_name

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "role_name": ":role_name",
            "external_id": ":external_id"
         }'
```

</api-code>

Response: Using role\_name

```json
{
  "data": {
    "id": 12341,
    "grant_type": "team",
    "role_name": "Admin",
    "external_id": "UU0239093499",
    "name": "Jack Smith",
    "email": "jack@example.com",
    "time_zone": "Pacific Time (US & Canada)",
    "created_at": "2024-09-13T07:26:48.779-07:00",
    "last_activity_log": null
  }
}
```

#### Using env\_roles

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "env_roles": [
                {
                  "environment_type": ":environment_type_1",
                  "name": ":role_name_1",
                  "role_type": ":role_type_1"
                },
                {
                  "environment_type": ":environment_type_2",
                  "name": ":role_name_2",
                  "role_type": ":role_type_2"
                },
                {
                  "environment_type": ":environment_type_3",
                  "name": ":role_name_3",
                  "role_type": ":role_type_3"
                }
            ],
            "external_id": ":external_id"
         }'
```

</api-code>

Response: Using env\_roles

```json
{
  "data": {
    "id": 12341,
    "grant_type": "team",
    "role_name": "Admin",
    "external_id": "UU0239093499",
    "name": "Jack Smith",
    "email": "jack@example.com",
    "time_zone": "Pacific Time (US & Canada)",
    "created_at": "2024-09-24T08:06:09.883-07:00",
    "last_activity_log": null,
    "env_roles": [
      {
        "environment_type": "dev",
        "name": "Admin",
        "role_type": "privilege_group"
      },
      {
        "environment_type": "test",
        "name": "Admin",
        "role_type": "privilege_group"
      },
      {
        "environment_type": "prod",
        "name": "Admin",
        "role_type": "privilege_group"
      }
    ]
  }
}
```

## Remove collaborator from customer workspace

Removes a [collaborator](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) from an Embedded customer workspace. This doesn't delete the collaborator's Workato account.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| member\_id | **string** _required_ | The member ID or external member ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Sample request

<api-code>

```shell
curl -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:project_grant_id' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "id": "prjgr-AQAEnmMX-b4rPeT-CD"
    }
  ]
}
```

## List a customer workspace collaborator's project grants

Retrieves all project grants assigned to a [collaborator](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) in an Embedded customer workspace. This doesn't include project access granted through [collaborator groups](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups).

> **PROJECT GRANTS**
> 
> A project grant assigns a [project role](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) to a collaborator or group. Refer to [Project grants](/en/oem/oem-api/project-grants) to manage project grants using the Embedded API or [Manage project access and roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#manage-project-access-and-roles) to manage project grants in the UI.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id/project_grants
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| member\_id | **string** _required_ | The ID of the collaborator to retrieve project grants from. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page\[number\] | **integer** _optional_ | The page number to retrieve. The default value is `1`. |
| page\[size\] | **integer** _optional_ | The number of items per page to retrieve. The default and maximum value is `100`. |

### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id/project_grants?page[number]=:page_number_value&page[size]=:page_size_value' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "id": "prjgr-AQAEnmMX-b4rPeT-CD",
      "project": {
        "id": 178230,
        "name": "Development",
        "environment": {
          "id": 148425,
          "type": "dev"
        },
      },
      "project_role": {
        "id": "prjrl-AQAEnmK3-EQpeYM",
        "name": "Developers"
      }
    },
    {
      "id": "prjgr-AQAEnmKE-xpCFwT-CD",
      "project": {
        "id": 178230,
        "name": "Sales",
        "environment": {
          "id": 148426,
          "type": "prod"
        },
      },
      "project_role": {
        "id": "prjrl-AQAEnmK3-EQpeYM",
        "name": "Developers"
      }
    }
  ],
  "total": 2,
  "page": {
    "number": 1,
    "size": 100
  }
}
```

## List customer connections

Get a list of connections in an Embedded customer's account.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

#### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "result": [
    {
      "id": 6132,
      "name": "My Box account",
      "provider": "box",
      "authorization_status": "success",
      "authorized_at": "2019-09-10T18:20:08.854-07:00",
      "created_at": "2019-09-10T18:19:57.437-07:00",
      "updated_at": "2019-09-10T18:20:08.859-07:00"
    },
    {
      "id": 6131,
      "name": "My Salesforce account",
      "provider": "salesforce",
      "authorization_status": "success",
      "authorized_at": "2019-09-10T18:19:43.018-07:00",
      "created_at": "2019-09-10T18:19:12.902-07:00",
      "updated_at": "2019-09-10T18:19:43.021-07:00"
    }
  ]
}
```

## Get privileges from a customer workspace collaborator

Retrieves the privileges and [roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#key-roles) of a collaborator in an Embedded customer workspace. The response returns an array of roles for each [environment](/en/features/environments) (for example, `dev`, `test`, and `prod`) with the following information:

- Environment type
- User role
- All permissions assigned to the role
- Role type

The response includes roles from both the legacy model (`role_type: privilege_group`) and the new model (`role_type: environment`).

> **ENVIRONMENT PRIVILEGES ONLY**
> 
> This endpoint only returns environment-level privileges. Use it together with [Get projects privileges from a customer workspace collaborator](#get-project-privileges) to retrieve the collaborator's project-level access.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id/privileges
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| member\_id | **string** _required_ | The ID of the collaborator whose privileges you plan to retrieve. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id/privileges' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

```json
{
    "data": [
        {
            "environment_type": "dev",
            "name": "Operator",
            "role_type": "privilege_group",
            "privileges": {
                "Recipes": [
                    "read",
                    "run",
                    "read_run_history"
                ],
                "Folders": [
                    "read"
                ],
                "Projects": [
                    "read"
                ],
                "Use in recipes": [
                    "all"
                ],
                "Test automation": [
                    "read"
                ]
            }
        },
        {
            "environment_type": "test",
            "name": "Operator",
            "role_type": "privilege_group",
            "privileges": {
                "Recipes": [
                    "read",
                    "run",
                    "read_run_history"
                ],
                "Folders": [
                    "read"
                ],
                "Projects": [
                    "read"
                ],
                "Use in recipes": [
                    "all"
                ],
                "Test automation": [
                    "read"
                ]
            }
        },
        {
            "environment_type": "prod",
            "name": "Operator",
            "role_type": "privilege_group",
            "privileges": {
                "Recipes": [
                    "read",
                    "run",
                    "read_run_history"
                ],
                "Folders": [
                    "read"
                ],
                "Projects": [
                    "read"
                ],
                "Use in recipes": [
                    "all"
                ],
                "Test automation": [
                    "read"
                ]
            }
        }
    ]
}
```

## Get projects privileges from a customer workspace collaborator

Retrieves project-level access for a collaborator in an Embedded customer workspace. This includes access assigned directly or through membership in a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups). You can use this endpoint to audit project permissions.

> **PROJECT PRIVILEGES ONLY**
> 
> This endpoint only returns project-level privileges. Use it together with [Get privileges from a customer workspace collaborator](#get-list-of-customer-privileges) to retrieve the collaborator's environment-level roles and privileges.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id/projects_privileges
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |
| member\_id | **string** _required_ | The ID of the collaborator to retrieve project privileges from. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/members/:member_id/projects_privileges' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "environment": {
        "id": 123456,
        "type": "dev"
      },
      "projects": {
        "61722": {
          "Folders": ["create", "view"]
        }
      }
    },
    {
      "environment": {
        "id": 789123,
        "type": "prod"
      },
      "projects": {
        "74137": {
          "Folders": ["view"]
        }
      }
    }
  ]
}
```

## Get usage (v2)

Retrieves usage metrics for specified customer workspaces within a defined time frame, including task usage, recipe counts, and counts of successful and failed jobs. This endpoint parses and returns datetime values in the Embedded admin's workspace timezone.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/statistics/usage
```

</api-code>

  

> **QUERY USAGE FOR MULTIPLE WORKSPACES IN A SINGLE REQUEST**
> 
> We recommend querying usage for all relevant workspaces in a single request to optimize performance.

> **JOB COUNTING AND ALLOCATION**
> 
> Each unique job run is counted only once. Jobs aren't double-counted but may be allocated differently depending on the query timeframe, interval, and the most recent retry.

### Request body

| Name | Type | Description |
| --- | --- | --- |
| from | **string** _required_ | Start of the date range for retrieving usage metrics, in ISO 8601 format (`YYYY-MM-DD`). |
| to | **string** _required_ | End of the date range for retrieving usage metrics, in ISO 8601 format (`YYYY-MM-DD`). |
| interval | **string** _optional_ | Sets the time interval for aggregating results. Accepted values include `none`, `year`, `month`, `week`, `day`, and `hour`. Default is `none`. |
| workspace\_ids\[\] | **array of integers** _conditional_ | Customer workspace IDs to retrieve usage data for. **Required** if `external_ids[]` is not provided. |
| external\_ids\[\] | **array of strings** _conditional_ | Customer external IDs to retrieve usage data for. **Required** if `workspace_ids[]` is not provided. |
| folder\_ids\[\] | **array of integers** _optional_ | Filters results to the specified folder IDs, returning tasks and job outcomes within those folders. Do not provide if using `folder_name_pattern`. |
| folder\_name\_pattern | **string** _optional_ | Filters results by folders matching the specified name pattern (for example, `[PROD] Folder`). Case-sensitive. Do not provide if using `folder_ids[]`. Wildcards and regular expressions are not supported. |
| recipe\_ids\[\] | **array of integers** _optional_ | Filters results to the specified recipe IDs, returning tasks and job outcomes related to those recipes. Do not provide if using `recipe_name_pattern`. |
| recipe\_name\_pattern | **string** _optional_ | Filters results by recipes matching the specified name pattern (for example, `[TEST] Recipe`). Case-sensitive. Do not provide if using `recipe_ids[]`. Wildcards and regular expressions are not supported. |
| adapter\_names\_all\[\] | **array of strings** _optional_ | Filters results to recipes that use all of the specified connectors (for example, `["stripe", "workday", "zendesk"]`). Do not provide if using `adapter_names_any[]`. |
| adapter\_names\_any\[\] | **array of strings** _optional_ | Filters results to recipes that use any of the specified connectors (for example, `["stripe", "workday", "zendesk"]`). Do not provide if using `adapter_names_all[]`. |
| running | **boolean** _optional_ | Filters results to active (`true`) or inactive (`false`) recipes. Default is `nil`, which includes both active and inactive recipes. |
| group\_by | **string** _optional_ | Specifies how results should be grouped. Accepted values include `recipe` and `workspace`. Default is `workspace`. Can only be set to `recipe` when either `folder_ids[]`, `recipe_ids[]`, `folder_name_pattern`, or `recipe_name_pattern` are specified. |

> **INCLUDE USAGE METRICS FOR DELETED RECIPES**
> 
> To include metrics for deleted recipes in the response, provide only the following fields in the request body:
> 
> - `from`
> - `to`
> - `workspace_ids` or `external_ids`
> - `interval` (optional)
> 
> Including any additional fields limits the usage data to non-deleted recipes that match those conditions.

> **CASE-SENSITIVE FILTERS**
> 
> The `recipe_name_pattern` and `folder_name_pattern` filters are case-sensitive. These filters return any recipe or folder whose name contains the specified pattern. For example, both `DeVelopment` and `MedveDeV` would match the pattern `DeV`. The filters accept patterns with three or more characters.

### Sample request

This example request retrieves monthly usage statistics for customer workspaces with IDs `10` and `2`, from July 1, 2024, to September 26, 2024. The response is grouped by the specified recipes (IDs `100` and `200`).

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/statistics/usage' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "group_by": ":group_by",
            "interval": ":interval",
            "workspace_ids": [:workspace_ids_1, :workspace_ids_2],
            "recipe_ids": [:recipe_ids_1, :recipe_ids_2],
            "from": ":from",
            "to": ":to"
          }'
```

</api-code>

### Responses

200 OK

```json
{
    "data": [
        {
            "recipe_id": 100, // Only part of the response when grouped by 'recipe'
            "workspace_id": 10,
            "intervals": [
                {
                    "start_datetime": "2024-07-01T00:00:00.000-07:00",
                    "successful_job_count": 52,
                    "failed_job_count": 3,
                    "task_count": 110
                },
                {
                    "start_datetime": "2024-08-01T00:00:00.000-07:00",
                    "successful_job_count": 78,
                    "failed_job_count": 6,
                    "task_count": 150
                },
                {
                    "start_datetime": "2024-09-01T00:00:00.000-07:00",
                    "successful_job_count": 64,
                    "failed_job_count": 2,
                    "task_count": 130
                }
            ]
        },
        {
            "recipe_id": 200,
            "workspace_id": 2,
            "intervals": [
                {
                    "start_datetime": "2024-07-01T00:00:00.000-07:00",
                    "successful_job_count": 43,
                    "failed_job_count": 5,
                    "task_count": 95
                },
                {
                    "start_datetime": "2024-08-01T00:00:00.000-07:00",
                    "successful_job_count": 61,
                    "failed_job_count": 8,
                    "task_count": 125
                },
                {
                    "start_datetime": "2024-09-01T00:00:00.000-07:00",
                    "successful_job_count": 72,
                    "failed_job_count": 7,
                    "task_count": 140
                }
            ]
        }
    ],
    "generated_at": "2024-09-26T13:48:46.839-07:00"
}
```

400 BAD REQUEST - NO MATCHING WORKSPACES FOUND

If the workspace IDs or external IDs provided in the request do not belong to the Embedded account's list of customers, or if all non-matching workspace IDs are ignored and the resulting list is empty, the following error is returned:

```json
{
    "errors": [
        {
            "code": 400,
            "title": "No workspaces found matching the specified workspace filter conditions."
        }
    ]
}
```

400 BAD REQUEST - NO MATCHING RECIPES FOUND

If the folder IDs or recipe IDs provided in the request do not belong to the specified workspace or folder, or if all invalid folder IDs, recipe IDs, folder name patterns, and recipe name patterns are ignored and the resulting list is empty, the following error is returned:

```json
{
    "errors": [
        {
            "code": 400,
            "title": "No recipes found matching the specified filter conditions."
        }
    ]
}
```

400 BAD REQUEST - SPECIFIED ADAPTERS NOT FOUND

The following error is returned when the request includes an adapter in `adapter_names_any` or `adapter_names_all` that does not exist:

```json
{
    "errors": [
        {
            "code": 400,
            "title": "Specified adapters in the filter condition not found."
        }
    ]
}
```

## Get connection-based usage

Retrieves connection-based usage metrics for specified customer workspaces. This endpoint provides usage metrics specific to connections, distinct from the task-based metrics available through the [Get usage (v2)](#get-usage-v2) endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/statistics/connection_usage
```

</api-code>

### Request body

| Name | Type | Description |
| --- | --- | --- |
| workspace\_ids\[\] | **array of integers** _conditional_ | Customer workspace IDs used to retrieve connection-based usage data. **Required** if `external_ids[]` is not provided. |
| external\_ids\[\] | **array of strings** _conditional_ | Customer external IDs used to retrieve connection-based usage data. **Required** if `workspace_ids[]` is not provided. |
| folder\_ids\[\] | **array of integers** _optional_ | Filters results by the specified folder IDs, returning tasks and job outcomes within those folders. Do not provide if using `folder_name_pattern`. |
| folder\_name\_pattern | **string** _optional_ | Filters results by folders matching the specified name pattern (for example, `[PROD] Folder`). Case-sensitive. Do not provide if using `folder_ids[]`. Wildcards and regular expressions are not supported. |
| adapter\_names\[\] | **array of strings** _optional_ | Filters results by the specified connectors. |
| include\_runtime\_connections | **boolean** _optional_ | Specifies whether to include runtime connections data in the response. Defaults to `false`. |

### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/v2/managed_users/statistics/connection_usage' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "workspace_ids": [:workspace_ids],
            "folder_ids": [:folder_ids],
            "adapter_names": [":adapter_names_1", ":adapter_names_2", ":adapter_names_3"]
          }'
```

</api-code>

### Response

```json
{
    "data": [
        {
            "active_connections_count": 3,
            "active_connections_data": [
                {
                    "id": 15728497,
                    "name": "My Salesforce account",
                    "provider": "salesforce",
                    "authorization_status": "success",
                    "recipe_count": 5,
                    "running_recipe_count": 2,
                    "external_id": null,
                    "folder_id": 21256536,
                    "parent_account_id": null
                },
                {
                    "id": 15816920,
                    "name": "My Workday account",
                    "provider": "workday",
                    "authorization_status": "success",
                    "recipe_count": 2,
                    "running_recipe_count": 2,
                    "external_id": null,
                    "folder_id": 21256536,
                    "parent_account_id": null
                },
                {
                    "id": 15816922,
                    "name": "My Stripe account",
                    "provider": "stripe",
                    "authorization_status": "success",
                    "recipe_count": 2,
                    "running_recipe_count": 2,
                    "external_id": null,
                    "folder_id": 21256536,
                    "parent_account_id": null
                }
            ],
            "inactive_connections_count": 0,
            "inactive_connections_data": [],
            "active_opa_count": 0,
            "workspace_id": 4552523
        }
    ],
    "generated_at": "2024-10-23T08:53:05.428-07:00"
}
```

## Get monthly usage

Retrieves monthly usage metrics for all Embedded customers for the last 12 months. This endpoint returns datetime values in the Embedded admin's workspace timezone. Currently, only task data is available through this endpoint.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/usage
```

</api-code>

  

> **GET USAGE V2 API**
> 
> Use the [Get usage (v2)](#get-usage-v2) endpoint to retrieve more granular task information for a specific date range, workspace, project, or recipe.

> **TASK COUNT BY CALENDAR MONTH**
> 
> The task count by customer returned by this endpoint is the total of all tasks done in the associated **calendar month**. You can obtain the total usage across all plans using this endpoint, even if the customer's plan has changed or the billing date/usage has been reset.

#### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/usage \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

**Note**: The following response has been truncated from 12 to three months.

```json
{
   "result":{
      "data":[
         {
            "user_id": 7443,
            "intervals":[
               {
                  "start_datetime": "2019-10-01T00:00:00.000-07:00",
                  "task_count": null
               },
               {
                  "start_datetime": "2019-11-01T00:00:00.000-07:00",
                  "task_count": null
               },
               {
                  "start_datetime": "2020-10-01T00:00:00.000-07:00",
                  "task_count": 0
               }
            ]
         }
      ],
      "generated_at":"2020-10-02T05:41:29.232-07:00"
   }
}
```

* * *

## Provision Environments

Provision Environments for an existing customer. Any existing assets in the customer workspace are placed in the **Development** environment after provisioning.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/environments
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID must be URL encoded. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| environments | **array** _optional_ | A list of environment configurations. |
| environment\_type | **string** _conditional_ | Specifies the type of environment. **Required** if `environments` is present. Possible values include `dev`, `test`, and `prod`. |
| external\_id | **string** _optional_ | A unique identifier for the environment. |
| error\_notification\_emails | **string** _optional_ | Email address to receive error notifications. |

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/environments \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "environments": [
             {
               "environment_type": ":environment_type_1",
               "external_id": ":external_id",
               "error_notification_emails": ":error_notification_emails"
             },
             {
               "environment_type": ":environment_type_2",
               "external_id": ":external_id",
               "error_notification_emails": ":error_notification_emails"
             },
             {
               "environment_type": ":environment_type_3",
               "external_id": ":external_id",
               "error_notification_emails": ":error_notification_emails"
             }
           ]
         }'
```

</api-code>

### Sample response

```json
{
    "data": {
        "status": "created",
        "id": 29069,
        "external_id": null,
        "name": "Barnaby",
        "environments": [
            {
                "id": 29541,
                "environment_type": "prod"
            },
            {
                "id": 29540,
                "environment_type": "test"
            }
        ],
        "notification_email": "example-email@example.com",
        "full_embedding": true,
        "admin_notification_emails": "example-email@example.com ",
        "error_notification_emails": "example-email@example.com",
        "plan_id": "premium_quarterly",
        "origin_url": null,
        "trial": false,
        "in_trial": false,
        "whitelisted_apps": [],
        "frame_ancestors": null,
        "created_at": "2023-11-13T23:59:29.420-09:00",
        "updated_at": "2024-02-29T06:02:58.078-09:00",
        "time_zone": "Pacific Time (US & Canada)",
        "auth_settings": {
            "type": "workato_auth"
        },
        "current_billing_period_start": "2024-03-08T08:19:19.079-09:00",
        "current_billing_period_end": "2024-04-08T09:19:19.079-08:00",
        "task_count": 0,
        "active_connection_limit": 0,
        "active_connection_count": 5,
        "active_recipe_count": 5
    }
}
```

* * *

## Provision Environments (v2)

Provision Environments for an existing customer. The endpoint returns a task ID and provisioning completes asynchronously. Any existing assets in the customer workspace are placed in the **Production** environment after provisioning. Use the returned `task_id` with the [Get status of environment provisioning](#get-status-of-environment-provisioning) endpoint to track progress.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environments
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID must be URL encoded. |

### Sample request

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/environments \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json'
```

</api-code>

### Sample response

```json
{
    "data": {
        "task_id": 1392
    }
}
```

* * *

## Get status of environment provisioning

Get the status of asynchronous environment provisioning.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/environments_provision_tasks/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the environment provisioning task. |

### Sample request

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/v2/managed_users/environments_provision_tasks/:id \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

```json
{
    "data": {
        "id": 1392,
        "status": "completed",
        "source_workspace_id": 5952556,
        "target_workspace_id": 7645656,
        "name": "WFA Test"
    }
}
```

* * *

## Get list of customer categories

Retrieves a list of customer categories in an Embedded partner's workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** _optional_ | Page number of customer categories to fetch. Defaults to 1. |
| per\_page | **integer** _optional_ | Number of customer categories to return in a single page. Defaults to 100. The maximum is 100. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": [
    {
      "id": 12345,
      "name": "Enterprise"
    },
    {
      "id": 12346,
      "name": "SMB"
    }
  ]
}
```

* * *

## Create a customer category

Creates a new customer category in an Embedded partner's workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| customer\_category | **hash** _required_ | The customer category object. |
| customer\_category\[name\] | **string** _required_ | The name of the customer category. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "customer_category": {
                "name": ":name"
            }
          }'
```

</api-code>

### Response

```json
{
  "data": {
    "id": 12347,
    "name": "retail"
  }
}
```

* * *

## Update a customer category

Updates a customer category in an Embedded partner's workspace.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the customer category. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| customer\_category | **hash** _required_ | The customer category object. |
| customer\_category\[name\] | **string** _required_ | The name of the customer category. |

### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories/:id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "customer_category": {
                "name": ":name"
            }
          }'
```

</api-code>

### Response

```json
{
  "data": {
    "id": 12347,
    "name": "Retail"
  }
}
```

* * *

## Delete a customer category

Deletes a customer category in an Embedded partner's workspace.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the customer category. |

### Sample request

<api-code>

```shell
curl  -X DELETE https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": {
    "success": true
  }
}
```

* * *

## Batch assign a customer category to workspaces

Assigns a customer category to Embedded customer workspaces.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories/:id/assign
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the customer category. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories/:id/assign \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

### Response

```json
{
  "data": {
    "id": 12347,
    "name": "retail"
  }
}
```

* * *

## Batch unassign a customer category from workspaces

Unassigns a customer category from Embedded customer workspaces.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories/:id/unassign
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | ID of the customer category. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| customer\_category | **hash** _required_ | The customer category object. |
| customer\_category\[user\_ids\] | **array of integers** _optional_ | Workspace IDs to remove from this customer category. The maximum is 100. |
| customer\_category\[external\_ids\] | **array of strings** _optional_ | External workspace IDs to remove from this customer category. The maximum is 100. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/v2/managed_users/customer_categories/:id/unassign \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "customer_category": {
              "user_ids": [:user_ids_1, :user_ids_2, :user_ids_3],
              "external_ids": [":external_ids_1", ":external_ids_2"]
            }
          }'
```

</api-code>

### Response

```json
{
  "data": {
    "id": 12347,
    "name": "retail"
  }
}
```

---
