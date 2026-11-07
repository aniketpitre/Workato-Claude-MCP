---
url: 'https://docs.workato.com/en/oem/oem-api/team.md'
description: >-
  Reference for the Embedded API endpoint that invites a collaborator to a
  customer workspace and assigns environment or legacy roles.
---

# Embedded API - Customer workspace collaborators

This API enables you to [manage collaborators](/en/user-accounts-and-teams/team-collaboration) in a customer workspace. To work with collaborators in an admin workspace, refer to the Developer API documentation for [workspace collaborators](/en/workato-api/team).

> **RBAC 2.0 MIGRATION**
> 
> This endpoint's payload and response change after the customer workspace migrates to the new role-based access control model. Refer to [RBAC 2.0 migration - Developer and Embedded API changes](/en/user-accounts-and-teams/role-based-access/rbac2-migration-api-changes) for details.

## Rate limits

Customer workspace collaborator resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Customer workspace collaborators](/en/oem/oem-api/team.html) endpoints | 60 requests per minute. Additionally, you can send one request per user and workspace ID every 20 minutes to the **Invite collaborator to managed customer workspace** endpoint. |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users/:id/member\_invitations](#invite-collaborator-to-managed-customer-account) | Invites a collaborator to a customer workspace. |

## Invite a collaborator to a customer workspace

Invite a [collaborator](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) to an Embedded customer workspace. The API sends an email invitation if the email you provide doesn't belong to an existing user. Collaborators can join the workspace after they create a Workato account. You can invite a specific email and workspace combination once every twenty minutes. Alternatively, you can use the [Add collaborator](/en/oem/oem-api/managed-users#add-member-to-customer-account) endpoint to add a collaborator directly.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:id/member_invitations
```

</api-code>

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The Embedded customer ID or external ID. External IDs must be URL encoded and prefixed with an `E`, for example: `EA2300`. |

### Request body

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | The name of the collaborator. |
| email | **string** _required_ | The email of the collaborator. |
| env\_roles | **object** _conditional_ | Configures the collaborator's environment roles. **Required** if `role_name` is not provided. |
| env\_roles\[environment\_type\] | **string** _conditional_ | The type of environment in the workspace where you plan to invite the collaborator. **Required** if `role_name` is not provided. Use `dev` for single-environment workspaces. |
| env\_roles\[name\] | **string** _conditional_ | The role to assign the collaborator for the specific environment. **Required** if `role_name` is not provided. |
| env\_roles\[role\_type\] | **string** _optional_ | The type of role to assign the collaborator. Accepted values include `privilege_group` and `environment`. The default value is `privilege_group`. |
| role\_name | **string** _conditional_ | The role to assign the collaborator. **Required** if `env_roles` is not provided. |
| user\_group\_ids | **array of strings** _optional_ | The IDs of collaborator groups to assign. |

> **SPECIFY ROLES FOR DIFFERENT ENVIRONMENTS**
> 
> You must provide either `role_name` or `env_roles` in the payload:
> 
> \-`role_name` assigns a role in the `dev` environment only. -`env_roles` lets you specify roles for different environments.
> 
> You can't combine `role_name` and `env_roles` in the same request. If both are included, Workato assigns only the roles in `env_roles` and ignores `role_name`.

### Sample request

This example request creates an invitation for the `dev` environment that assigns the collaborator an `Admin` role.

<api-code>

```shell
curl -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/member_invitations' \
  -H 'Authorization: Bearer <api_token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": ":name",
        "email": ":email",
        "user_group_ids": [
          ":user_group_id_1",
          ":user_group_id_2"
        ],
        "env_roles": [
          {
            "environment_type": ":environment_type",
            "name": ":role_name",
            "role_type": ":role_type"
          }
        ]
      }'
```

</api-code>

### Response

```json
{
    "result": "ok"
}
```

---
