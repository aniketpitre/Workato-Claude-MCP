---
url: 'https://docs.workato.com/en/oem/oem-api/folders.md'
description: >-
  Reference for the Embedded API folders resource to manage folders and projects
  within customer workspaces programmatically.
---

# Embedded API - Folders

Use the following endpoints to manage folders and projects (top-level folders) in customer workspaces.

> **ENDPOINT ACCESS**
> 
> To access these endpoints, your [API client](/en/workato-api/api-clients#api-client-benefits) must have the appropriate privileges. This is determined by the [role](/en/workato-api/api-clients#create-a-client-role) assigned to your API client.
> 
> To enable endpoint access:
> 
> You can enable access to these endpoints by editing an existing API client role, or by creating a new API client role:
> 
> 1. Navigate to **Workspace admin > API clients > Client roles**.
>    
>    Select the role you plan to edit.
>    
>    Alternatively, click **\+ Add client role** to create a new API client role.
>    
> 2. Navigate to **Customer workspaces > Projects > Project assets > Projects & folders**.
>    
> 3. Select the checkboxes next to the endpoints you plan to enable for this role. The following options are available:
>    
>    - **Projects & folders**
>      - Select this option to enable all endpoints for this role.
>    - **List folders** `GET /api/managed_users/:managed_user_id/folders`
>    - **List projects** `GET /api/managed_users/:managed_user_id/projects`
>    - **Create folder** `POST /api/managed_users/:managed_user_id/folders`
>    - **Delete folder** `DELETE /api/managed_users/:managed_user_id/folders   /:folder_id`
>    - **Update folder** `PUT /api/managed_users/:managed_user_id/folders   /:folder_id`
>    - **Delete project** `DELETE /api/managed_users/:managed_user_id/projects   /:project_id`
>    - **Update project** `PUT /api/managed_users/:managed_user_id/projects   /:project_id`
>    
>    ![Select the endpoints you plan to enable](/assets/project-api-embed-customers-enable.DoJIed0C.png)_Select the endpoints you plan to enable_
>    

## Rate limits

Folder resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Folders](/en/oem/oem-api/folders.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/folders](/en/oem/oem-api/folders#list-folders) | List folders in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/folders](/en/oem/oem-api/folders#create-folder) | Create a folder in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/folders/:folder\_id](/en/oem/oem-api/folders#update-folder) | Update a folder in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/folders/:folder\_id](/en/oem/oem-api/folders#delete-folder) | Delete a folder in a customer workspace. |

## List folders

Lists all folders in a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/folders
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| parent\_id | **string** _optional_ | Parent folder ID. Defaults to Home folder. |
| page | **integer** _optional_ | Page number. Defaults to 1. |
| per\_page | **integer** _optional_ | Page size. Defaults to 100. The maximum is 100. |
| with\_nested\_folders | **boolean** _optional_ | If false, returns all immediate child folders under root, excluding root. The default is false. |
| updated\_after | **string** _optional_ | Filter the list of folders to include only those updated after the date and time you specify. The date and time must be provided in ISO 8601 format according to the following pattern: `YYYY-MM-DDTHH:MM:SSZ`. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/folders?parent_id=:parent_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
{
    "result": [
        {
            "id": 1789,
            "name": "Netsuite production",
            "parent_id": 12323,
            "created_at": "2020-07-16T10:49:53.337-07:00",
            "updated_at": "2020-07-16T10:49:53.347-07:00"
        }
    ],
    "count": 1,
    "page": 1,
    "per_page": 100
}
```

## Create a folder

Creates a new folder in the specified parent folder. If you don't specify a parent folder ID, the system creates the folder as a top-level folder in the home folder.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/folders
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the folder. |
| parent\_id | **string** _optional_ | Parent folder ID. Defaults to Home folder. |

#### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/folders \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d  '{
            "name": ":name"
           }'
```

</api-code>

### Response

```json
{
  "id": 3498583,
}
```

## Update a folder

Use this endpoint to update a folder name or move it to a different folder within a customer workspace. You can change the folder's name and update its `parent_id` if the folder is not a project. If the folder is a project, you can only change the project name using this endpoint.

Refer to the [Update a project](/en/oem/oem-api/project-properties#update-project) endpoint documentation for additional options in the request payload for projects.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/folders/:folder_id
```

</api-code>

  

> **FOLDER AND PROJECT CONVERSION**
> 
> You can't use this endpoint to convert a folder into a project or a project into a folder.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| folder\_id | **string** _required_ | The ID of the folder you plan to update. You can retrieve a list of folder IDs by calling the [List folders](#list-folders) endpoint. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | The new name for the folder. |
| parent\_id | **string** _optional_ | The ID of the parent folder to which you plan to move the folder. |

> **FOLDER NAME**
> 
> The folder name cannot include the `/` or `\` characters.

### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/folders/:folder_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "parent_id": :parent_id
          }'
```

</api-code>

### Responses

Successful response

```json
{
    "id": 12345,
    "name": "My updated folder name",
    "parent_id": 67890,
    "created_at": "2024-08-02T13:35:11.691-07:00",
    "updated_at": "2024-08-02T14:26:30.365-07:00"
}
```

Unsuccessful responses

#### Changing the parent folder of a project

Projects are top-level folders. Attempting to change the parent folder of a project returns the following error:

```json
{
    "message": "Parent can't be changed for project folder"
}
```

Refer to the [Update a project](/en/oem/oem-api/project-properties#update-project) endpoint documentation for the available options for the request payload.

#### Invalid characters in folder name

Attempting to update a folder name to include the `/` or `\` characters returns the following error:

```json
{
    "message": "Folder name can't contain the folder path"
}
```

## Delete a folder

Delete a folder in a customer workspace.

> **FOLDER DELETION INCLUDES RECIPES AND CONNECTIONS**
> 
> This action deletes a folder and all of its contents (recipes and connections).

To use this endpoint, your API client role must have the [Delete folder](#folders) privilege.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/folders/:folder_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| folder\_id | **string** _required_ | The ID of the folder you plan to delete. You can retrieve a list of folder IDs by calling the [list folders](#list-folders) endpoint. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| force | **boolean** _optional_ | Set this parameter to `true` to delete a folder that is not empty. When `true`, the folder you specify using the `folder_id` parameter, and its contents (all recipes and connections) within the folder are deleted. If set to `false`, this action can only delete an empty folder. |

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/folders/:folder_id?force=:true_or_false' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

Successful response

```json
{
    "success": "true"
}
```

Unsuccessful response

If you attempt to delete a folder that isn't empty, but do not set the `force` parameter to `true` Workato cannot delete the folder you've specified.

If the folder contains a connection, Workato provides the following response:

```json
{
    "message": "can't remove a folder with connections"
}
```

If the folder contains a recipe, Workato provides the following response:

```json
{
    "message": "can't remove a folder with recipe"
}
```

---
