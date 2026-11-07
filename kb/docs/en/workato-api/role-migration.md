---
url: 'https://docs.workato.com/en/workato-api/role-migration.md'
description: >-
  Reference for the Workato role migration API to convert legacy system and
  custom roles into environment and project roles.
---

# Developer API - Role migration

Use the following endpoints to convert legacy roles into [environment and project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#key-roles). Alternatively, you can use the [in-app migration wizard](/en/user-accounts-and-teams/role-based-access/migrate-roles).

> **RBAC 2.0 MIGRATION**
> 
> These endpoints are deprecated after your workspace migrates to the new role-based access control model, since a migrated workspace has no remaining legacy roles to migrate. Refer to [RBAC 2.0 migration - Developer and Embedded API changes](/en/user-accounts-and-teams/role-based-access/rbac2-migration-api-changes) for details.

## Rate limits

The role migration resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All[](/en/workato-api/role-migration.html) | All [Role migration](/en/workato-api/role-migration.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/roles\_migration/system\_roles](#migrate-system-roles) | Migrate system roles. |
| POST | [/api/roles\_migration/custom\_role](#migrate-a-custom-role) | Migrate a custom role. |

## Migrate system roles

Converts legacy system roles into [environment and project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#key-roles). You can also use the in-app migration wizard to [migrate system roles](/en/user-accounts-and-teams/role-based-access/migrate-roles#migrate-system-roles).

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/roles_migration/system_roles
```

</api-code>

### Request body

| Name | Type | Description |
| --- | --- | --- |
| dry\_run | **boolean** _optional_ | Returns a JSON response without migrating roles when set to `true`. The default value is `false`. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/roles_migration/system_roles' \
  -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "data": {
    "environment_roles": [
      {
        "name": "EnvironmentAdmin",
        "config": { /* Environment admin permissions */ }
      },
      {
        "name": "EnvironmentManager",
        "config": { /* Environment manager permissions */ }
      },
      {
        "name": "Member",
        "config": { /* Member permissions */ }
      }
    ],
    "project_roles": [
      {
        "name": "ProjectAdmin",
        "config": { /* Project admin permissions */ }
      },
      {
        "name": "AdvancedBuilder",
        "config": { /* Advanced builder permissions */ }
      },
      {
       "name": "ProjectOperator",
        "config": { /* Project operator permissions */ }
      }
    ],
    "collaborators": [
      {
        "user_id": 1,
        "email": "kim@example.com",
        "name": "Kim",
        "roles": [
          { "environment": "dev", "name": "EnvironmentAdmin" },
          { "environment": "prod", "name": "EnvironmentManager" },
          { "environment": "test", "name": "Member" }
        ]
      }
    ],
    "projects": [
      {
        "id": 101,
        "name": "Dev Project",
        "environment": "dev",
        "collaborators": [
          {
            "user_id": 1,
            "email": "izumi@example.com",
            "name": "Izumi",
            "project_role": "ProjectAdmin"
          }
        ]
      }
    ],
    "moderators": [
      {
        "user_id": 201,
        "email": "sasha@example.com",
        "name": "Sasha",
        "environment_role": "EnvironmentAdmin",
        "project_role": "ProjectAdmin"
      }
    ]
  }
}
```

Config objects

`Config` objects contain the permissions configured for a role. For example, the following is the `Config` object for the environment admin role:

```json
"config": {
          "personalization": {"privileges": "all"},
          "topic": {"privileges": "all"},
          "lookup_table": {"privileges": "all"},
          "people_task": {"privileges": "all"},
          "manage_projects": {"privileges": "all"},
          "custom_adapter_sdk": {"privileges": "all"},
          "custom_adapter_use_in_recipes": {"privileges": "all"},
          "opa": {"privileges": "all"},
          "connection_opa_files": {"privileges": "all"},
          "connection_opa_cmd_scripts": {"privileges": "all"},
          "api_key": {"privileges": "all"},
          "service_console": {"privileges": "all"},
          "api_platform_dashboard": {"privileges": "all"},
          "api_platform_endpoints": {"privileges": "all"},
          "api_platform_clients": {"privileges": "all"},
          "api_platform_policies": {"privileges": "all"},
          "api_platform_settings": {"privileges": "all"},
          "apim_proxy_transformation": {"privileges": "all"},
          "workato_schema": {"privileges": "all"},
          "custom_oauth_key": {"privileges": "all"},
          "workato_template": {"privileges": "all"},
          "workbot": {"privileges": "all"},
          "enterprise_workbot": {"privileges": "all"},
          "group_recommendations": {"privileges": "all"},
          "job_history_search": {"privileges": "all"},
          "action_timeout": {"privileges": "all"},
          "data_masking": {"privileges": "all"},
          "identity_service_settings": {"privileges": ["read", "update"]},
          "identity_service_users_and_groups": {"privileges": ["read", "create", "update", "delete"]},
          "lcap_portal_settings": {"privileges": ["read", "update"]},
          "lcap_portal_user_groups": {"privileges": ["read", "create", "update", "delete"]},
          "lcap_public_pages": {"privileges": "all"},
          "lcap_app_functions": {"privileges": ["read", "create", "update", "delete"]},
          "lcap_page_actions": {"privileges": "all"},
          "lcap_custom_domains": {"privileges": "all"},
          "lcap_insights": {"privileges": "all"},
          "file_storage": {"privileges": "all"},
          "account_property": {"privileges": "all"},
          "data_mapper": {"privileges": "all"},
          "audit_log_replication": {"privileges": "all"},
          "apim_log_replication": {"privileges": "all"},
          "activity_logs": {"privileges": "all"},
          "saml": {"privileges": "all"},
          "team": {"privileges": "all"},
          "package": {"privileges": "all"},
          "custom_roles": {"privileges": "all"},
          "api_clients": {"privileges": "all"},
          "oem_vendor": {"privileges": "all"},
          "workspace_settings": {"privileges": "all", "enable_for": "non_oem"},
          "environment_settings": {"privileges": "all", "enable_for": "non_oem"},
          "oem_admin_settings": {"privileges": "all", "enable_for": "org_admin_with_settings"},
          "oem_customer_settings": {"privileges": "all", "enable_for": "org_customer_with_settings"},
          "logging_service": {"privileges": "all"},
          "general_provisioning": {"privileges": "all"},
          "account_deletion": {"privileges": "all"},
          "disable_two_fa": {"privileges": "all"},
          "configurable_data_retention": {"privileges": "all"},
          "extended_60_days_data_retention": {"privileges": "all"},
          "extended_data_retention": {"privileges": "all"},
          "cmk_management": {"privileges": "all"},
          "external_secret_sources": {"privileges": "all"},
          "federation_management": {"privileges": "all", "enable_for": "federation"},
          "scim": {"privileges": "all"},
          "oem_ac_customers": {"privileges": "all", "enable_for": "oem_admin"},
          "oem_ac_automations": {"privileges": "all", "enable_for": "oem_admin"},
          "oem_ac_analytics": {"privileges": "all", "enable_for": "oem_admin"},
          "usage_insights": {"privileges": ["read", "create", "update", "delete"]},
          "usage_dashboard": {"privileges": ["read"]},
          "cbp_usage_dashboard": {"privileges": ["read"]}
        }
```

## Migrate a custom role

Converts legacy custom roles into [environment and project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#key-roles). Alternatively, you can use the in-app migration wizard to [migrate custom roles](/en/user-accounts-and-teams/role-based-access/migrate-roles#migrate-custom-roles).

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/roles_migration/custom_role
```

</api-code>

### Request body

| Name | Type | Description |
| --- | --- | --- |
| privilege\_group\_id | **integer** _required_ | The ID of the role to convert. |
| environment\_role | **object** _required_ | Defines the environment role to create. |
| environment\_role\[name\] | **string** _required_ | The name of the new environment role. |
| environment\_role\[additional\_permissions\] | **object** _optional_ | Specifies additional permissions for the new environment role. |
| project\_role | **object** _required_ | Defines the project role to create. |
| project\_role\[name\] | **string** _required_ | The name of the new project role. |
| project\_role\[additional\_permissions\] | **object** _optional_ | Specifies additional permissions for the new project role. |
| dry\_run | **boolean** _optional_ | Returns a JSON response without migrating roles when set to `true`. The default value is `false`. |

### Sample request

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/roles_migration/custom_role' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <api_token>" \
  -d '{
        "privilege_group_id": :privilege_group_id_value,
        "environment_role": {
          "name": ":environment_role_name",
          "additional_permissions": :environment_additional_permissions
        },
        "project_role": {
          "name": ":project_role_name",
          "additional_permissions": :project_additional_permissions
        }
      }'
```

</api-code>

### Response

```json
{
  "data": {
    "environment_roles": [
      {
        "name": "New Environment role",
        "config": {
          "lookup_table": {
            "privileges": ["read"]
          },
          "manage_projects": {
            "privileges": ["create", "access_control"]
          }
        }
      }
    ],
    "project_roles": [
      {
        "name": "New project role",
        "config": {
          "recipe": {
            "privileges": ["read"]
          },
          "project_administration": {
            "privileges": ["access_control"]
          }
        }
      }
    ],
    "collaborators": [
      {
        "user_id": 1,
        "email": "yuri@example.com",
        "name": "Yuri",
        "roles": [
          { "environment": "dev", "name": "New Environment role" },
          { "environment": "prod", "name": "New Environment role" },
          { "environment": "test", "name": "New Environment role" }
        ]
      }
    ],
    "projects": [
      {
        "id": 1,
        "name": "Dev Project",
        "environment": "dev",
        "collaborators": [
          {
            "user_id": 1,
            "email": "hao@example.com",
            "name": "Hao",
            "project_role": "New project role"
          }
        ]
      }
    ],
    "moderators": [
      {
        "user_id": 1,
        "email": "lucian@example.com",
        "name": "Lucian",
        "environment_role": "New Environment role",
        "project_role": "New project role"
      }
    ]
  }
}
```

---
