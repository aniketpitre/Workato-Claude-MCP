---
url: 'https://docs.workato.com/en/workato-api/users.md'
description: >-
  Reference for the Developer API workspace details resource, with the GET
  /api/users/me endpoint that returns details about your workspace.
---

# Developer API - Workspace details

Use this API to get details about your workspace.

> **ENDPOINT ACCESS**
> 
> Your [API client](/en/workato-api/api-clients#api-client-benefits) must be assigned privilege for the **Get details** endpoint. This privilege is determined by your [API client role](/en/workato-api/api-clients#create-a-client-role).
> 
> Additionally, if your workspace uses [environments](/en/features/environments), this privilege is only available to API clients with `DEV` access.
> 
> To enable endpoint access:
> 
> You can enable access to this endpoint by editing an existing API client role or by creating a new API client role:
> 
> 1. Navigate to **Workspace admin > API clients > Client roles**.
>    
>    Select the role you plan to edit.
>    
>    Alternatively, click **\+ Add client role** to create a new API client role.
>    
> 2. Select **Admin** and navigate to **Workspace details > Workspace details**.
>    
> 3. Select the checkbox next to the **Get details** `GET /api/users/me` endpoint.
>    
>    ![Select the endpoint you plan to enable](/assets/api-client-user-privileges-workspace-details.BR5yPeJ-.png)_Select the endpoint you plan to enable_
>    

## Rate limits

Workspace details resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Workspace details](/en/workato-api/users.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/users/me](/en/workato-api/users#auth-user-details-get) | Get details. |

## Get details

Get details of the authenticated user.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/users/me
```

</api-code>

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/users/me \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "id": 17293,
    "name": "Jane Doe",
    "created_at": "2025-06-19T19:53:16.886-07:00",
    "avatar_url": "https://workato-assets.s3.amazonaws.com/profiles/avatars/000/089/005/large/logo.png?1562399288",
    "recipes_count": 49,
    "interested_applications": [],
    "last_seen": "2026-08-11T23:22:24.329-07:00",
    "contact_phone": null,
    "email": "jane.doe@example.com",
    "phone": "xxxxxxxxxx",
    "active_recipes_count": 1,
    "root_folder_id": 10294,
    "plan_id":"cbp_v1_workato_one",
    "current_billing_period_start": "2026-08-01T19:15:11.372-07:00",
    "current_billing_period_end": "2026-09-01T19:15:11.372-07:00",
    "team_name": "ACME Corp",
    "environment_name": "Development"
}
```

---
