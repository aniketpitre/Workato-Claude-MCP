---
url: 'https://docs.workato.com/en/oem/oem-api/project-properties.md'
description: >-
  Reference for Embedded API endpoints to manage projects, project properties,
  and deployments in customer workspaces.
---

# Embedded API - Projects

Use the following endpoints to manage [projects](/en/projects), [project properties](/en/features/project-properties), and [project deployments](/en/features/environments/deployment) in a customer workspace programmatically.

> **PRIVATE BETA**
> 
> The following endpoints are in private beta:
> 
> - [List eligible reviewers for a deployment](#list-eligible-reviewers-for-a-deployment)
> - [Assign reviewers to a deployment](#assign-reviewers-to-a-deployment)
> - [Submit a deployment for review](#submit-a-deployment-for-review)
> - [Deploy an approved deployment](#deploy-an-approved-deployment)
> 
> Private beta features are available in production but only to selected customers. Customers must opt in and be accepted into the beta.
> 
> During the private beta, Workato may update its functionality or change its availability without prior notice.

## Rate limits

Project resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| GET | List projects: [/api/managed\_users/:managed\_user\_id /projects](/en/oem/oem-api/project-properties.html#list-projects) | 1,000 requests per minute |
| All | All [Deployments](/en/oem/oem-api/project-properties.html#list-deployments) endpoints | 60 requests per minute |
| All | All other [Projects](/en/oem/oem-api/project-properties.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/projects](/en/oem/oem-api/project-properties#list-projects) | List projects in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/folders](/en/oem/oem-api/project-properties#create-project) | Create a project in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/projects/:project\_id](/en/oem/oem-api/project-properties#update-project) | Update a project in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/projects/:project\_id](/en/oem/oem-api/project-properties#delete-a-project) | Delete a project in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/properties](/en/oem/oem-api/project-properties#list-project-properties) | List project-level properties by prefix and project ID. |
| POST | [/api/managed\_users/:managed\_user\_id/properties](/en/oem/oem-api/project-properties#upsert-project-properties) | Upsert project-level properties. |
| GET | [/api/managed\_users/:managed\_user\_id/deployments](/en/oem/oem-api/project-properties#list-deployments) | Retrieve a list of deployments in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/deployments/:id](/en/oem/oem-api/project-properties#get-a-deployment) | Retrieve a single deployment in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/api/project\_builds/:id](/en/oem/oem-api/project-properties#get-a-downloaded-package) | Retrieve a downloaded package in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/projects/:id/build](/en/oem/oem-api/project-properties#build-a-project) | Build a project in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/project\_builds/:id/deploy](/en/oem/oem-api/project-properties#deploy-a-downloaded-package) | Deploy a downloaded package in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/projects/:project\_id/deploy](/en/oem/oem-api/project-properties#deploy-a-project) | Deploy a project in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/deployments/:id/eligible\_reviewers](/en/oem/oem-api/project-properties#list-eligible-reviewers-for-a-deployment) | Retrieve a list of eligible reviewers that can be assigned to review a deployment in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/deployments/:id/assign\_reviewers](/en/oem/oem-api/project-properties#assign-reviewers-to-a-deployment) | Assign reviewers to a deployment in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/deployments/:id/submit\_for\_review](/en/oem/oem-api/project-properties#submit-a-deployment-for-review) | Submit a deployment for review in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/deployments/:id/deploy](/en/oem/oem-api/project-properties#deploy-an-approved-deployment) | Deploy an approved deployment in a customer workspace. |

## List projects

Lists all projects. Projects are top-level folders that typically encompass a single use case.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** _optional_ | Page number. Defaults to 1. |
| per\_page | **integer** _optional_ | Page size. Defaults to 100. The maximum is 100. |
| updated\_after | **string** _optional_ | Filter the list of projects to include only those updated after the date and time you specify. The date and time must be provided in ISO 8601 format according to the following pattern: `YYYY-MM-DDTHH:MM:SSZ`. |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
```

</api-code>

### Response

```json
{
    "result": [
        {
            "id": 649122,
            "description": "Coupa to Netsuite automations",
            "folder_id": 1563029,
            "name": "Procure to Pay"
        },
        {
            "id": 604202,
            "description": "Salesforce to Netsuite automations",
            "folder_id": 1486330,
            "name": "Order to Cash"
        }
    ],
    "count": 2,
    "page": 1,
    "per_page": 100
}
```

## Create a project

To create a project within a customer workspace, use the [Create a folder](/en/oem/oem-api/folders#create-folder) endpoint and omit the `parent_id` from the request payload.

## Update a project

Update a project within a customer workspace. Projects are top-level folders that typically encompass a single use case. Use this endpoint to modify a project's name and/or description.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects/:project_id
```

</api-code>

  

> **FOLDER AND PROJECT CONVERSION**
> 
> You can't use this endpoint to convert a folder into a project or a project into a folder.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| project\_id | **string** _required_ | The ID of the project you plan to update. This is distinct from the project's `folder_id`. Retrieve a list of projects in the customer workspace by calling the [List projects](#list-projects) endpoint. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | The new name for the project. |
| description | **string** _optional_ | The new description for the project. |

> **PROJECT NAME**
> 
> The project name cannot include the `/` or `\` characters.

### Sample request

<api-code>

```shell
curl  -X PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects/:project_id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "name": ":name",
            "description": ":description"
          }'
```

</api-code>

### Responses

Successful response

```json
{
    "id": 54321,
    "description": "My updated project description",
    "folder_id": 09876,
    "name": "My updated project name"
}
```

Unsuccessful response

Attempting to update your project name to include the `/` or `\` character returns the following error:

```json
{
    "message": "Name is invalid"
}
```

## Delete a project

Delete a project within the customer workspace. Projects are top-level folders that typically encompass a single use case.

> **PROJECT DELETION INCLUDES ASSETS**
> 
> This action deletes a project and all of its contents. This includes all child folders, recipes, connections, and Workflow apps assets (if applicable) inside the project.

To use this endpoint, your API client role must have the following privilege:

- **Delete project**

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects/:project_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| project\_id | **string** _required_ | The ID of the project you plan to delete. Retrieve a list of all projects in the customer workspace by calling the [List projects](#list-projects) endpoint. |

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects/:project_id' \
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

If you attempt to delete a project and do not have the appropriate privileges, Workato returns the following response:

```json
{
    "message": "Cannot destroy folder"
}
```

## List project properties

Returns a list of project-level properties belonging to a specific project in a customer workspace that matches a `project_id` you specify. You must also include a prefix. For example, if you provide the prefix `salesforce_sync.`, any project property with a name beginning with `salesforce_sync.`, such as `salesforce_sync.admin_email`, with the `project_id` you provided is returned.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/properties
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The external ID must be prefixed with an `E` (example: `EA2300`) and the resulting ID should be URL encoded. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| prefix | **string** _required_ | Returns properties that contain the prefix you provided. For example, if the prefix is `salesforce_sync.` the property `salesforce_sync.admin_email` is returned. |
| project\_id | **string** _required_ | Returns project-level properties that match the `project_id` you specify. This is distinct from the project's `folder_id`. Retrieve a list of projects and their IDs in the customer workspace by calling the [List projects](#list-projects) endpoint. If this parameter is not present, this call returns [environment properties](/en/features/account-properties). |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/properties?prefix=:prefix_value&project_id=:project_id_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json'
```

</api-code>

### Response

```json
{
  "public_url": "https://www.example.com",
  "admin_email": "jude.feeney@example.com"
}
```

## Upsert project properties

Upserts project properties belonging to a specific project in a customer workspace that matches a `project_id` you specify. This endpoint maps to properties based on the names you provide in the request.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/properties
```

</api-code>

  

> **PROPERTY LIMITS**
> 
> Project properties have the following quotas:
> 
> | Description | Quota |
> | --- | --- |
> | Maximum number of project properties per project | 1,000 |
> | Maximum length of project property name | 100 characters |
> | Maximum length of project property value | 1,024 characters |

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The external ID must be prefixed with an `E` (example: `EA2300`) and the resulting ID should be URL encoded. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| project\_id | **string** _required_ | Provide the project ID that contains the project properties you plan to upsert. This is distinct from the project's `folder_id`. Retrieve a list of projects and their IDs in the customer workspace by calling the [List projects](#list-projects) endpoint. If this parameter is not present, this call upserts [environment properties](/en/features/account-properties). |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| properties | **Hash** _required_ | Contains the names and values of the properties you plan to upsert. |

### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/properties?project_id=:project_id_value' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{ "properties": { ":property_name": ":property_value" }}'
```

</api-code>

### Response

```json
{
  "success": true
}
```

## List deployments

Retrieves a list of deployments in a customer workspace. Use query parameters to filter results by project, folder, or date range.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| project\_id | **string** _optional_ | Retrieves deployments associated with the specified project ID. |
| folder\_id | **string** _optional_ | A folder ID, formatted as `f{:folder_id}`. For example, `f660222`. If provided, only deployments associated with the folder are included in the response. Use the [List folders](/en/oem/oem-api/folders#list-folders) endpoint to retrieve these IDs. |
| environment\_type | **string** _optional_ | An environment type. If provided, only deployments associated with the environment are included in the response. Accepted values include `test` or `prod`. |
| state | **string** _optional_ | Retrieves deployments by the specified state. Accepted values include `pending`, `success`, or `failed`. |
| from | **timestamp** _optional_ | Includes deployments created after the specified timestamp. Use the ISO 8601 format (for example, `2024-10-14T10:09:43Z`). |
| to | **timestamp** _optional_ | Includes deployments created before the specified timestamp. Use the ISO 8601 format (for example, `2024-10-15T10:09:43Z`). |

### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments' \
      -H 'Authorization: Bearer <api_token>' \
```

</api-code>

### Response

```json
{
    "items": [
        {
            "id": 6409,
            "created_at": "2024-10-14T10:09:43.890-07:00",
            "updated_at": "2024-10-14T10:10:15.370-07:00",
            "title": "Deployment",
            "description": "",
            "project_build_id": 9120,
            "environment_type": "test",
            "project_id": "39334",
            "state": "success",
            "detailed_state": "deploy_finished",
            "performed_by_name": "Alex",
            "assets": [
                {
                    "id": null,
                    "name": "My Salesforce account",
                    "type": "connection",
                    "state": "new",
                    "folder": "Sample deployment"
                },
                {
                    "id": null,
                    "name": "My Zendesk account",
                    "type": "connection",
                    "state": "new",
                    "folder": "Sample deployment"
                },
                {
                    "id": null,
                    "name": "New Salesforce account will create Zendesk organization",
                    "type": "recipe",
                    "folder": "Sample deployment"
                },
            ],
            "review_state": "review_approved",
            "reviews": [
                {
                    "status": "approved",
                    "comment": "LGTM!",
                    "reviewer_name": "Alex"
                }
            ]
        }
        ...
    ]
}
```

## Get a deployment

Retrieves a single deployment in a customer workspace by its unique ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| id | **integer** _required_ | The unique identifier of the deployment you plan to retrieve. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "id": 6409,
    "created_at": "2024-10-14T10:09:43.890-07:00",
    "updated_at": "2024-10-14T10:10:15.370-07:00",
    "title": "Deployment",
    "description": "",
    "project_build_id": 9120,
    "environment_type": "test",
    "project_id": "39334",
    "state": "success",
    "detailed_state": "deploy_finished",
    "performed_by_name": "Alex",
    "assets": [
        {
            "id": null,
            "name": "My Salesforce account",
            "type": "connection",
            "state": "new",
            "folder": "Sample deployment"
        },
        {
            "id": null,
            "name": "My Zendesk account",
            "type": "connection",
            "state": "new",
            "folder": "Sample deployment"
        },
        {
            "id": null,
            "name": "New Salesforce account will create Zendesk organization",
            "type": "recipe",
            "folder": "Sample deployment"
        },
    ],
    "review_state": "review_approved",
    "reviews": [
        {
            "status": "approved",
            "comment": "LGTM!",
            "reviewer_name": "Alex"
        }
    ]
}
```

## Get a downloaded package

Retrieves a downloaded package in a customer workspace by its unique ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/api/project_builds/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| id | **integer** _required_ | The unique identifier of the downloaded package you plan to retrieve. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/project_builds/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "id": 72,
    "created_at": "2021-12-10T11:39:15.738-08:00",
    "updated_at": "2021-12-10T11:39:16.218-08:00",
    "description": null,
    "project_id": "10416",
    "state": "success",
    "performed_by_name": "Alex",
    "download_url": "https://workato-assets.s3.us-west-2.amazonaws.com/packages/zip_files/000/714/699/original/<PROJECT_NAME_DATE>.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=<CREDENTIAL>"
}
```

## Build a project

Builds a project in a customer workspace. After building, use the [Deploy a downloaded package](#deploy-a-downloaded-package) endpoint to deploy the project to an environment.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects/:id/build
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| id | **string** _required_ | The ID of the project you plan to build. Accepts a valid `project_id` or a valid `folder_id`, formatted as `f{:folder_id}` (for example, `f660222`). Use the [List projects](#list-projects) endpoint to retrieve project IDs in the workspace. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| description | **string** _optional_ | A brief description of the build. |
| include\_test\_cases | **boolean** _optional_ | Specifies whether to include test cases in the build. |
| include\_tags | **boolean** _optional_ | Specifies whether to include tags assigned to assets in the build. Tags are excluded from the build when set to `false`. Set to `false` by default. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects/:id/build \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "description": ":description",
            "include_tags": :true_or_false
          }'
```

</api-code>

### Response

```json
{
    "id": 9121,
    "created_at": "2024-10-14T14:37:29.877-07:00",
    "updated_at": "2024-10-14T14:37:29.885-07:00",
    "description": "Fixes bugs",
    "project_id": "10416",
    "state": "pending",
    "performed_by_name": "Alex",
    "download_url": null
}
```

## Deploy a downloaded package

Deploys a downloaded package in a customer workspace to an environment. Use the [Build a project](#build-a-project) endpoint to build the project before deploying it.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/project_builds/:id/deploy
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| id | **integer** _required_ | The unique identifier of the downloaded package you plan to deploy. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| environment\_type | **string** _required_ | Specifies the environment where you plan to deploy the downloaded package. Accepted values include `test` and `prod`. |
| title | **string** _optional_ | A title for the deployment. |
| description | **string** _optional_ | A brief description of the deployment. |
| include\_tags | **boolean** _optional_ | Specifies whether to include tags assigned to assets in the deployed package. Tags exist at the workspace level but are not applied to assets in the target environment when set to `false`. This is set to `false` by default. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/project_builds/:id \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "environment_type": ":environment_type",
            "include_tags": :true_or_false
          }'
```

</api-code>

### Response

```json
{
    "id": 67,
    "created_at": "2021-12-10T11:59:03.426-08:00",
    "updated_at": "2021-12-10T11:59:03.426-08:00",
    "title": null,
    "description": null,
    "project_build_id": 9121,
    "environment_type": "test",
    "project_id": "10416",
    "state": "pending",
    "performed_by_name": "Alex",
    "assets": null
}
```

## Deploy a project

Deploys a project in a customer workspace. Specify the target environment in the payload. Projects can only be deployed from the DEV environment.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects/:project_id/deploy
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| project\_id | **string** _required_ | The unique identifier of the project you plan to deploy. Use the [List projects](#list-projects) endpoint to retrieve project IDs in the workspace. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| environment\_type | **string** _required_ | Specifies the environment where you plan to deploy the project. |
| title | **string** _required_ | The title of the deployment. |
| description | **string** _optional_ | A brief description of the deployment. |
| include\_tags | **boolean** _optional_ | Specifies whether to include tags assigned to assets in the deployment. Tags exist at the workspace level but are not applied to assets in the target environment when set to `false`. This is set to `false` by default. |

### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/projects/35263/deploy' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "environment_type": ":environment_type",
            "title": ":title",
            "description": ":description",
            "include_tags": :true_or_false
          }'
```

</api-code>

### Sample response

```json
{
    "id": 3905,
    "created_at": "2024-03-10T13:08:53.344-08:00",
    "updated_at": "2024-03-10T13:08:53.344-08:00",
    "title": "My deployment",
    "description": "Description of my deployment",
    "project_build_id": 6544,
    "environment_type": "test",
    "project_id": "35263",
    "state": "pending",
    "performed_by_name": "Barnaby",
    "assets": null
}
```

## List eligible reviewers for a deployment

Retrieve a list of eligible reviewers that can be assigned to review a deployment in a customer workspace. Reviewers must be collaborators with review permissions in both the DEV environment and the target deployment environment. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id/eligible_reviewers
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| id | **integer** _required_ | The unique identifier of the deployment. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id/eligible_reviewers \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "reviewers": [
        {
            "id": 29036,
            "name": "Jie",
            "avatar_url": ""
        },
        {
            "id": 30143,
            "name": "Alex",
            "avatar_url": ""
        },
        {
            "id": 31836,
            "name": "Charlie",
            "avatar_url": ""
        }
    ]
}
```

## Assign reviewers to a deployment

Assigns reviewers to a deployment in a customer workspace. You can assign reviewers either before or after submitting the deployment for review. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

This endpoint can also be used to unassign reviewers. To unassign a reviewer, call the endpoint again and provide only the IDs of the users who should remain assigned to the deployment. Unassigning a reviewer removes their review from the deployment.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id/assign_reviewers
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| id | **integer** _required_ | The unique identifier of the deployment. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| reviewer\_ids | **array of strings** _required_ | An array of user IDs to assign as reviewers for the deployment. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id/assign_reviewers \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "reviewer_ids": [":reviewer_id"]
          }'
```

</api-code>

### Response

```json
{
    "reviews": [
        {
            "deployment_id": 6390,
            "reviewer_id": 29036,
            "status": "pending",
            "comment": "",
            "updated_at": "2024-10-11T10:54:26.075-07:00"
        },
        {
            "deployment_id": 6390,
            "reviewer_id": 30143,
            "status": "pending",
            "comment": "",
            "updated_at": "2024-10-11T10:31:07.047-07:00"
        },
        {
            "deployment_id": 6390,
            "reviewer_id": 31836,
            "status": "pending",
            "comment": "",
            "updated_at": "2024-10-11T10:54:26.099-07:00"
        }
    ],
    "authors": [
        {
            "id": 29036,
            "name": "Jie",
            "avatar_url": ""
        },
        {
            "id": 30143,
            "name": "Alex",
            "avatar_url": ""
        },
        {
            "id": 31836,
            "name": "Charlie",
            "avatar_url": ""
        }
    ]
}
```

## Submit a deployment for review

Submits a deployment in a customer workspace for review. Before calling this endpoint, use the [Build a project](#build-a-project) and [Deploy a downloaded package](#deploy-a-downloaded-package) endpoints to generate and retrieve the deployment ID. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id/submit_for_review
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| id | **integer** _required_ | The unique identifier of the deployment to submit for review. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id/submit_for_review \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "success": true
}
```

  

> **REVIEW ACTIONS IN A CUSTOMER WORKSPACE**
> 
> To accept, reject, or reset a review in a customer workspace, the Embedded customer must take action either through the UI or by using the [Developer API endpoints](/en/workato-api/projects#approve-a-deployment). The Embedded partner can't perform these actions through the Embedded API.

## Deploy an approved deployment

Deploys an approved deployment in a customer workspace. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id/deploy
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| id | **integer** _required_ | The unique identifier of the approved deployment to deploy. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| include\_tags | **boolean** _optional_ | Specify whether the deployment should include tags. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/deployments/:id/deploy \
      -H 'Authorization: Bearer <api_token>'
      -H 'Content-Type: application/json' \
      -d '{
            "include_tags": :true_or_false
          }'
```

</api-code>

### Response

```json
{
    "id": 6390,
    "created_at": "2024-10-11T13:16:58.170-07:00",
    "updated_at": "2024-10-11T13:47:31.254-07:00",
    "title": "",
    "description": "",
    "project_build_id": 9104,
    "environment_type": "test",
    "project_id": "44946",
    "state": "pending",
    "detailed_state": "deploy_started",
    "performed_by_name": "Alex",
    "assets": [
        {
            "id": null,
            "name": "My Salesforce account",
            "type": "connection",
            "state": "new",
            "folder": "Sample deployment"
        },
        {
            "id": null,
            "name": "My Zendesk account",
            "type": "connection",
            "state": "new",
            "folder": "Sample deployment"
        },
        {
            "id": null,
            "name": "New Salesforce account will create Zendesk organization",
            "type": "recipe",
            "folder": "Sample deployment"
        },
    ],
    "review_state": "review_approved",
    "reviews": [
        {
            "status": "approved",
            "comment": "Looks good!",
            "reviewer_name": "Jie"
        }
    ]
}
```

---
