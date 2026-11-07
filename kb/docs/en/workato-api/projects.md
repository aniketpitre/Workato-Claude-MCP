---
url: 'https://docs.workato.com/en/workato-api/projects.md'
description: >-
  Reference for the Workato projects API to build, deploy, and manage projects
  across the environments in your workspace.
---

# Developer API - Projects

In Workato, [projects](/en/projects) are used to organize automation assets and control access. A project holds a set of related assets for your automations, including connections, recipes, and subfolders.

> **WHO CAN USE THESE APIS?**
> 
> Accounts with the [Environments](/en/features/environments) feature enabled can use the APIs in this guide. Requests sent from accounts without this feature will receive a `400 - Environments not provisioned` response.

The Project APIs enable you to programmatically manage and deploy projects to the environments provisioned in your workspace.

* * *

## Understanding project deployment

In Workato, there are two ways to deploy projects:

- **Build and then deploy**. This approach can be used if you want to commit the package to an external version control system. Steps for accomplishing this would be similar to the following:
  
  1. Build the project: `POST /api/projects/:id/build`
     
  2. Verify the project built successfully: `GET /api/project_builds/:id`
     
  3. If committing to a version control system like GitHub, use the `download_url` from Step 2's response to download the package.
     
  4. Commit the package to your version control system.
     
  5. Deploy the project build to an environment: `POST /api/project_builds/:id/deploy?environment_type=:environment_type`
     
  6. Verify the project deployed successfully: `GET /api/deployments/:id`
     
- **Build and deploy in one step**. If you don't need to commit the project to a version control system, you can use this approach:
  
  1. Build and deploy the project to an environment: `POST /api/projects/:id/deploy?environment_type=:environment_type`
     
  2. Verify the project deployed successfully: `GET /api/deployments/:id`
     

* * *

## Rate limits

Project resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Projects](/en/workato-api/projects.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/projects/:id/build](/en/workato-api/projects#build-a-project) | Builds a project. Use the [Deploy a project build](/en/workato-api/projects#deploy-a-project-build) endpoint to deploy the project to an environment. |
| GET | [/api/project\_builds/:id](/en/workato-api/projects#get-a-project-build) | Retrieves a project build by its unique ID. |
| POST | [/api/project\_builds/:id/deploy](/en/workato-api/projects#deploy-a-project-build) | Deploys a project build to an environment. Use the [Build a project](/en/workato-api/projects#build-a-project) endpoint to build the project first. |
| POST | [/api/projects/:id/deploy](/en/workato-api/projects#deploy-a-project) | Builds and deploys a project to an environment. |
| GET | [/api/deployments/:id](/en/workato-api/projects#get-a-deployment) | Retrieves a single deployment by its unique ID. |
| GET | [/api/deployments](/en/workato-api/projects#list-deployments) | Retrieves a list of deployments. Use query parameters to filter results by project, folder, or date range. |
| GET | [/api/deployments/:id/eligible\_reviewers](/en/workato-api/projects#list-eligible-reviewers-for-a-deployment) | Retrieves a list of eligible reviewers that can be assigned to review a deployment. |
| POST | [/api/deployments/:id/assign\_reviewers](/en/workato-api/projects#assign-reviewers-to-a-deployment) | Assigns reviewers to a deployment. |
| POST | [/api/deployments/:id/submit\_for\_review](/en/workato-api/projects#submit-a-deployment-for-review) | Submits a deployment for review. |
| POST | [/api/deployments/:id/approve](/en/workato-api/projects#approve-a-deployment) | Approves a deployment. |
| POST | [/api/deployments/:id/reject](/en/workato-api/projects#reject-a-deployment) | Rejects a deployment. |
| POST | [/api/deployments/:id/reopen](/en/workato-api/projects#re-open-a-deployment-for-review) | Re-opens a deployment for review. |
| POST | [/api/deployments/:id/update\_review\_comment](/en/workato-api/projects#update-a-deployment-review-comment) | Updates a deployment review comment. |
| POST | [/api/deployments/:id/deploy](/en/workato-api/projects#deploy-an-approved-deployment) | Deploys an approved deployment. |

* * *

> **PRIVATE BETA**
> 
> The following endpoints are in private beta:
> 
> - [List eligible reviewers for a deployment](#list-eligible-reviewers-for-a-deployment)
> - [Assign reviewers to a deployment](#assign-reviewers-to-a-deployment)
> - [Submit a deployment for review](#submit-a-deployment-for-review)
> - [Approve a deployment](#approve-a-deployment)
> - [Reject a deployment](#reject-a-deployment)
> - [Re-open a deployment for review](#re-open-a-deployment-for-review)
> - [Update a deployment review comment](#update-a-deployment-review-comment)
> - [Deploy an approved deployment](#deploy-an-approved-deployment)
> 
> Private beta features are available in production but only to selected customers. Customers must opt in and be accepted into the beta.
> 
> During the private beta, Workato may update its functionality or change its availability without prior notice.

## Build a project

Builds a project. Use the [Deploy a project build](#deploy-a-project-build) endpoint to deploy the project to an environment.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/projects/:id/build
```

</api-code>

### Request

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** _required_ | A project ID. This parameter accepts the following: A valid `project_id`. This is distinct from the project's `folder_id`. Use the [List projects endpoint](/workato-api/folders.html#list-projects) to retrieve these IDs.; A valid `folder_id`, formatted as `f{:folder_id}`. For example: `f660222`. Use the [List folders endpoint](/workato-api/folders.html#list-folders) to retrieve these IDs. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| **description** | **string** _optional_ | A brief description of the build. |
| **include\_test\_cases** | **boolean** _optional_ | Instructs the build to include test cases or not. |
| **include\_tags** | **boolean** _optional_ | Specifies whether to include tags assigned to assets in the build. Tags are excluded from the build when set to `false`. Set to `false` by default. |

#### Request examples

#### Using a project ID

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/projects/:id/build \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "description": ":description",
            "include_tags": :true_or_false
          }'
```

</api-code>

#### Using a folder ID

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/projects/:folder_id/build \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "description": ":description",
            "include_tags": :true_or_false
          }'
```

</api-code>

### Responses

200 OK

If successful, the API will return a `200 OK` status and a single project build object.

```json
{
    "id": 46,
    "created_at": "2021-12-09T22:09:29.997-08:00",
    "updated_at": "2021-12-09T22:09:30.004-08:00",
    "description": "Fixes bugs",
    "project_id": "10416",
    "state": "pending",
    "performed_by_name": "Finn the Human",
    "download_url": null
}
```

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** | The build ID. |
| **created\_at** | **timestamp** | The time the build was created. |
| **updated\_at** | **timestamp** | The time the build was last updated. |
| **description** | **string** | The build description. This is `null` if not provided in the request. |
| **include\_test\_cases** | **boolean** | Whether the build includes test cases or not. This is `null` if not provided in the request. |
| **project\_build\_id** | **integer** | The ID of the project build associated with the build. |
| **project\_id** | **string** | The ID of the project that was built. |
| **state** | **string** | The current state of the build. |
| **performed\_by\_name** | **string** | The name of the user who built the project. |
| **download\_url** | **string** | A URL from which the project build can be downloaded. |

400 BAD REQUEST - MISSING REQUIRED PARAMETERS

The API may return a `400 BAD REQUEST` status and the following errors if the request is malformed: Missing environment\_type parameter: `"message": "Missing parameter environment_type"`

404 NOT FOUND - INVALID PARAMETERS

The API may return a `404 NOT FOUND` status and a `Not found` error for the following reasons:

- Invalid `id`
- Invalid `environment_type`

404 NOT FOUND - INVALID URI

The API may return a `404 NOT FOUND` status and an `API not found` error for the following reasons:

- Unsupported method
- Incorrect URI

* * *

## Get a project build

Retrieves a project build by its unique ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/project_builds/:id
```

</api-code>

### Request

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** _required_ | The ID of the project build to retrieve. |

#### Request examples

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/project_builds/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

200 OK

If successful, the API will return a `200 OK` status and a single project build object.

```json
{
    "id": 72,
    "created_at": "2021-12-10T11:39:15.738-08:00",
    "updated_at": "2021-12-10T11:39:16.218-08:00",
    "description": null,
    "project_id": "10416",
    "state": "success",
    "performed_by_name": "Erin Cochran",
    "download_url": "https://workato-assets.s3.us-west-2.amazonaws.com/packages/zip_files/000/714/699/original/<PROJECT_NAME_DATE>.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=<CREDENTIAL>"
}
```

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** | The build ID. |
| **created\_at** | **timestamp** | The time the build was created. |
| **updated\_at** | **timestamp** | The time the build was last updated. |
| **description** | **string** | The build description. This will be `null` if not provided in the request that created the build. |
| **project\_id** | **string** | The ID of the project that was built. |
| **state** | **string** | The current state of the build. |
| **performed\_by\_name** | **string** | The name of the user who built the project. |
| **download\_url** | **string** | A URL from which the project build can be downloaded. |

404 NOT FOUND - INVALID PARAMETERS

The API may return a `404 NOT FOUND` status and a `Not found` error for the following reasons:

- Invalid project build `id`

404 NOT FOUND - INVALID URI

The API may return a `404 NOT FOUND` status and an `API not found` error for the following reasons:

- Unsupported method
- Incorrect URI

* * *

## Deploy a project build

Deploys a project build to an environment. Use the [Build a project](#build-a-project) endpoint to build the project first.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/project_builds/:id/deploy
```

</api-code>

### Request

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** _required_ | The ID of the build to be deployed. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| **environment\_type** | **string** _required_ | Specifies the deployment environment for the build. Accepted values include the following: `sandbox`, `test`, `stage`, `uat`, `preprod`, `prod` |
| **title** | **string** _optional_ | The title of the build. |
| **description** | **string** _optional_ | A brief description of the build. |
| **include\_tags** | **boolean** _optional_ | Specifies whether to include tags assigned to assets in the deployed build. Tags exist at the workspace level but are not applied to assets in the target environment when set to `false`. This is set to `false` by default. |

> **PAYLOAD FIELDS AS QUERY PARAMETERS**
> 
> The following payload fields can also be supplied as query parameters.

#### Request example

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/project_builds/:id/deploy \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "environment_type": ":environment_type",
            "include_tags": :true_or_false
          }'
```

</api-code>

### Responses

200 OK

If successful, the API will return a `200 OK` status and a single deployment object.

```json
{
    "id": 67,
    "created_at": "2021-12-10T11:59:03.426-08:00",
    "updated_at": "2021-12-10T11:59:03.426-08:00",
    "title": null,
    "description": null,
    "project_build_id": 46,
    "environment_type": "test",
    "project_id": "10416",
    "state": "pending",
    "detailed_state": "pending",
    "performed_by_name": "Alex",
    "assets": null
}
```

Initially, the `assets` field is set to `null` because the deployment process is still in progress. When you call this API, it returns the newly created deployment object and starts a background job to deploy the assets asynchronously. For details on the fields included in the `assets` array after the deployment is complete, see [Get a deployment](#get-a-deployment).

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** | The deployment ID. |
| **created\_at** | **timestamp** | The time the deployment was created. |
| **updated\_at** | **timestamp** | The time the deployment was last updated. |
| **title** | **string** | The deployment title. This will be `null` if not provided in the request. |
| **description** | **string** | The deployment description. This will be `null` if not provided in the request. |
| **project\_build\_id** | **integer** | The ID of the project build associated with the deployment. |
| **environment\_type** | **string** | The environment the build was deployed to. |
| **project\_id** | **string** | The ID of the project associated with the deployed build. |
| **state** | **string** | The current state of the deployment. |
| **detailed\_state** | **string** | A detailed description about the current state of the deployment. |
| **performed\_by\_name** | **string** | The name of the user who deployed the build. |
| **assets** | **array** | An array of assets included in the deployment. |

400 BAD REQUEST - MISSING REQUIRED PARAMETERS

The API may return a `400 BAD REQUEST` status and the following errors if the request is malformed: Missing environment\_type parameter: `"message": "Missing parameter environment_type"`

404 NOT FOUND - INVALID PARAMETERS

The API may return a `404 NOT FOUND` status and a `Not found` error for the following reasons:

- Invalid `id`
- Invalid `environment_type`

404 NOT FOUND - INVALID URI

The API may return a `404 NOT FOUND` status and an `API not found` error for the following reasons:

- Unsupported method
- Incorrect URI

* * *

## Deploy a project

Builds and deploys a project to an environment.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/projects/:id/deploy
```

</api-code>

### Request

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** _required_ | A project ID. This parameter accepts the following: A valid `project_id`. This is distinct from the project's `folder_id`. Use the [List projects endpoint](/workato-api/folders.html#list-projects) to retrieve these IDs.; A valid `folder_id`, formatted as `f{:folder_id}`. For example: `f660222`. Use the [List folders endpoint](/workato-api/folders.html#list-folders) to retrieve these IDs. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| **environment\_type** | **string** _required_ | Specifies the deployment environment. Accepted values include the following: `sandbox`, `test`, `stage`, `uat`, `preprod`, `prod` |
| **title** | **string** _optional_ | The title of the deployment. |
| **description** | **string** _optional_ | A brief description of the deployment. |
| **include\_tags** | **boolean** _optional_ | Specifies whether to include tags assigned to assets in the deployment. Tags exist at the workspace level but are not applied to assets in the target environment when set to `false`. This is set to `false` by default. |

> **PAYLOAD FIELDS AS QUERY PARAMETERS**
> 
> The following payload fields can also be supplied as query parameters.

#### Request examples

##### Using a project ID

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/projects/:id/deploy \
      -H 'Authorization: Bearer <api_token>'
      -H 'Content-Type: application/json' \
      -d '{
            "environment_type": ":environment_type",
            "include_tags": :true_or_false
          }'
```

</api-code>

##### Using a folder ID

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/projects/:folder_id/deploy \
      -H 'Authorization: Bearer <api_token>'
      -H 'Content-Type: application/json' \
      -d '{
            "environment_type": ":environment_type",
            "include_tags": :true_or_false
          }'
```

</api-code>

### Responses

200 OK

If successful, the API will return a `200 OK` status and a single deployment object.

```json
{
    "id": 47,
    "created_at": "2021-12-09T22:37:30.025-08:00",
    "updated_at": "2021-12-09T22:37:30.025-08:00",
    "title": null,
    "description": null,
    "project_build_id": 52,
    "environment_type": "test",
    "project_id": "10416",
    "state": "pending",
    "performed_by_name": "Alex",
    "assets": null
}
```

Initially, the `assets` field is set to `null` because the deployment process is still in progress. When you call this API, it returns the newly created deployment object and starts a background job to deploy the assets asynchronously. For details on the fields included in the `assets` array after the deployment is complete, see [Get a deployment](#get-a-deployment).

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** | The deployment ID. |
| **created\_at** | **timestamp** | The time the deployment was created. |
| **updated\_at** | **timestamp** | The time the deployment was last updated. |
| **title** | **string** | The deployment title. This is `null` if not provided in the request. |
| **description** | **string** | The deployment description. This will be `null` if not provided in the request. |
| **project\_build\_id** | **integer** | The ID of the project build associated with the deployment. |
| **environment\_type** | **string** | The environment the project was deployed to. |
| **project\_id** | **string** | The ID of the project that was deployed. |
| **state** | **string** | The current state of the deployment. |
| **detailed\_state** | **string** | A detailed description about the current state of the deployment. |
| **performed\_by\_name** | **string** | The name of the user who deployed the project. |
| **assets** | **array** | An array of assets included in the deployment. |

400 BAD REQUEST - MISSING REQUIRED PARAMETERS

The API may return a `400 BAD REQUEST` status and the following errors if the request is malformed: Missing environment\_type parameter: `"message": "Missing parameter environment_type"`

404 NOT FOUND - INVALID PARAMETERS

The API may return a `404 NOT FOUND` status and a `Not found` error for the following reasons:

- Invalid `id`
- Invalid `environment_type`

404 NOT FOUND - INVALID URI

The API may return a `404 NOT FOUND` status and an `API not found` error for the following reasons:

- Unsupported method
- Incorrect URI

* * *

## Get a deployment

Retrieves a single deployment by its unique ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/deployments/:id
```

</api-code>

### Request

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** _required_ | The ID of the deployment to be retrieved. |

#### Request example

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/deployments/:id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

200 OK

If successful, the API will return a `200 OK` status and a single deployment object.

```json
{
    // Fields related to reviews and approvals (for example, review_state, reviews, status, comment, reviewer_name)
    // are returned only when reviews and approvals are enabled.
    "id": 43,
    "created_at": "2024-10-15T12:28:40.779-07:00",
    "updated_at": "2024-10-15T12:29:21.292-07:00",
    "title": "Sample deployment",
    "description": "",
    "project_build_id": 46,
    "environment_type": "test",
    "project_id": "10416",
    "state": "success",
    "detailed_state": "deploy_finished",
    "performed_by_name": "Charlie",
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

| Name | Type | Description |
| --- | --- | --- |
| **id** | **integer** | The deployment ID. |
| **created\_at** | **timestamp** | The time the deployment was created. |
| **updated\_at** | **timestamp** | The time the deployment was last updated. |
| **description** | **string** | The deployment description. This will be `null` if not provided in the request that created the deployment. |
| **project\_build\_id** | **integer** | The ID of the project build associated with the deployment. |
| **environment\_type** | **string** | The environment associated with the deployment. |
| **project\_id** | **string** | The ID of the project associated with the deployment. |
| **state** | **string** | The current state of the deployment. |
| **detailed\_state** | **string** | A detailed description about the current state of the deployment. |
| **performed\_by\_name** | **string** | The name of the user who performed the deployment. |
| **assets** | **array** | An array of assets included in the deployment. |
| **assets\[id\]** | **integer** | The asset ID. This value is `null` for new assets not yet created in the target environment. Edited or removed assets contain a non-null ID. |
| **assets\[name\]** | **string** | The name of the asset. |
| **assets\[type\]** | **string** | The asset type. |
| **assets\[state\]** | **string** | The state of the asset. For example, `new`. |
| **assets\[folder\]** | **string** | The folder containing the asset. |

The `assets` array describes details about the deployment’s assets such as their names, types, folders, and states in the target environment.

Each asset's `id` field contains its unique identifier in the target environment. Assets with `"state": "new"` have `id: null` because they do not exist yet in the target environment. These assets receive an ID when they are created during deployment. Assets with `"state": "updated"` or `"state": "deleted"` already exist in the target environment and include their existing `id`.

For example, in the JSON response, the Salesforce and Zendesk connections are new assets, so their `id` values are `null`. These assets receive IDs when they are created in the target environment during deployment.

404 NOT FOUND - INVALID PARAMETERS

The API may return a `404 NOT FOUND` status and a `Not found` error for the following reasons:

- Invalid `deployment_id`
- Invalid `id`
- Invalid `environment_type`

404 NOT FOUND - INVALID URI

The API may return a `404 NOT FOUND` status and an `API not found` error for the following reasons:

- Unsupported method
- Incorrect URI

* * *

## List deployments

Retrieves a list of deployments. Query parameters may be used to filter results to a specific project, folder, date range, etc.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/deployments
```

</api-code>

### Request

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| **project\_id** | **string** _optional_ | A project ID. If provided, only deployments associated with the project will be included in the response. |
| **folder\_id** | **string** _optional_ | A folder ID, formatted as `f{:folder_id}`. For example: `f660222`. If provided, only deployments associated with the folder will be included in the response. Use the [List folders endpoint](/workato-api/folders.html#list-folders) to retrieve these IDs. |
| **environment\_type** | **string** _optional_ | An environment type. Only deployments associated with the specified environment are included in the response if provided. Accepted values include the following: `sandbox`, `test`, `stage`, `uat`, `preprod`, `prod` |
| **state** | **string** _optional_ | The state of the deployments to retrieve. If provided, only deployments with the provided state will be included in the response. Must be one of: `pending`, `success`, `failed` |
| **from** | **timestamp** _optional_ | Deployments created after this time will be included in the response. The value must be an ISO 8601 timestamp. |
| **to** | **timestamp** _optional_ | Deployments created after this time will be included in the response. The value must be an ISO 8601 timestamp. |
| **page** | **integer** _optional_ | The page number of the results to return. Defaults to `1`. |
| **per\_page** | **integer** _optional_ | The number of deployments to return in a single page. Defaults to `20`. Maximum value is `20`. |

#### Request examples

##### Without query parameters

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/deployments \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### With a folder ID

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/deployments?folder_id=:folder_id \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### With pagination

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/deployments?page=:page_value&per_page=:per_page_value' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

200 OK

If successful, the API will return a `200 OK` status and a list of deployment objects.

```json
{
  // Fields related to reviews and approvals (for example, review_state, reviews, status, comment, reviewer_name)
  // are returned only when reviews and approvals are enabled.
  "items": [
      {
          "id": 43,
          "created_at": "2024-10-15T12:28:40.779-07:00",
          "updated_at": "2024-10-15T12:29:21.292-07:00",
          "title": "Sample deployment",
          "description": "",
          "project_build_id": 46,
          "environment_type": "test",
          "project_id": "10416",
          "state": "success",
          "detailed_state": "deploy_finished",
          "performed_by_name": "Charlie",
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
      },
      {
          "id": 42,
          "created_at": "2024-10-14T12:28:40.779-07:00",
          "updated_at": "2024-10-14T12:29:21.292-07:00",
          "title": "",
          "description": "",
          "project_build_id": 45,
          "environment_type": "test",
          "project_id": "10416",
          "state": "pending",
          "detailed_state": "pending_review",
          "performed_by_name": "Charlie",
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
          "review_state": "pending_review",
          "reviews": [
              {
                  "status": "pending",
                  "comment": null,
                  "reviewer_name": "Alex"
              }
          ]
      },
  ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| items | **array** | A list of deployment objects. |
| id | **integer** | The deployment ID. |
| created\_at | **timestamp** | The time the deployment was created. |
| updated\_at | **timestamp** | The time the deployment was last updated. |
| title | **string** | The title of the deployment. |
| description | **string** | The deployment description. This will be `null` if not provided in the request that created the deployment. |
| project\_build\_id | **integer** | The ID of the project build associated with the deployment. |
| environment\_type | **string** | The environment associated with the deployment. |
| project\_id | **string** | The ID of the project associated with the deployment. |
| state | **string** | The current state of the deployment. |
| detailed\_state | **string** | Additional details about the current state of the deployment. |
| performed\_by\_name | **string** | The name of the user who performed the deployment. |
| assets | **array** | An array of assets included in the deployment. |
| assets\[id\] | **integer** | The asset ID. This value is `null` for new assets not yet created in the target environment. Edited or removed assets contain a non-null ID. |
| assets\[name\] | **string** | The name of the asset. |
| assets\[type\] | **string** | The asset type. |
| assets\[state\] | **string** | The state of the asset. For example, `new`. |
| assets\[folder\] | **string** | The folder containing the asset. |
| review\_state | **string** | The state of the review. Possible values include `pending_review`, `review_approved`, and `review_rejected`. |
| reviews | **array of objects** | An array of objects that represent reviews for the deployment. |
| status | **string** | The status of a specific review. Possible values include `pending`, `approved`, or `rejected`. |
| comment | **string** | The comment left by the reviewer, if available. |
| reviewer\_name | **string** | The name of the reviewer. |

404 NOT FOUND - INVALID URI

The API may return a `404 NOT FOUND` status and an `API not found` error for the following reasons:

- Unsupported method
- Incorrect URI

* * *

## List eligible reviewers for a deployment

Retrieves a list of eligible reviewers that can be assigned to review a deployment. Reviewers must be collaborators with review permissions in both the DEV environment and the target deployment environment. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/deployments/:id/eligible_reviewers
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The unique identifier of the deployment for which you plan to retrieve eligible reviewers. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/deployments/:id/eligible_reviewers \
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

* * *

## Assign reviewers to a deployment

Assigns reviewers to a deployment. You can assign reviewers either before or after submitting the deployment for review. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

This endpoint can also be used to unassign reviewers. To unassign a reviewer, call the endpoint again and provide only the IDs of the users who should remain assigned to the deployment. Unassigning a reviewer removes their review from the deployment.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/deployments/:id/assign_reviewers
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The unique identifier of the deployment where you plan to assign reviewers. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| reviewer\_ids | **array of strings** _required_ | An array of user IDs to assign as reviewers for the deployment. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/deployments/:id/assign_reviewers \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "reviewer_ids": [":reviewer_id_1", ":reviewer_id_2"]
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

* * *

## Submit a deployment for review

Submits a deployment for review. Before calling this endpoint, use the [Build a project](#build-a-project) and [Deploy a project build](#deploy-a-project-build) endpoints to generate and retrieve the deployment ID. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/deployments/:id/submit_for_review
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The unique identifier of the deployment to submit for review. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/deployments/:id/submit_for_review \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "success": true
}
```

* * *

## Approve a deployment

Approves a deployment. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/deployments/:id/approve
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The unique identifier of the deployment to approve. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| comment | **string** _required_ | A comment explaining the approval decision. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/deployments/:id/approve \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "comment": ":comment"
          }'
```

</api-code>

### Response

```json
{
    "review": {
        "deployment_id": 6390,
        "reviewer_id": 29036,
        "status": "approved",
        "comment": "Looks good!",
        "updated_at": "2024-10-11T13:39:22.857-07:00"
    }
}
```

* * *

## Reject a deployment

Rejects a deployment. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/deployments/:id/reject
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The unique identifier of the deployment to reject. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| comment | **string** _required_ | A comment explaining the reason for rejection. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/deployments/:id/reject \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "comment": ":comment"
          }'
```

</api-code>

### Response

```json
{
    "review": {
        "deployment_id": 6390,
        "reviewer_id": 29036,
        "status": "rejected",
        "comment": "",
        "updated_at": "2024-10-11T13:42:32.614-07:00"
    }
}
```

* * *

## Re-open a deployment for review

Re-opens a deployment for review. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/deployments/:id/reopen
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The unique identifier of the deployment to re-open. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/deployments/:id/reopen \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "success": true
}
```

* * *

## Update a deployment review comment

Updates a deployment review comment. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/deployments/:id/update_review_comment
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The unique identifier of the deployment. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| comment | **string** _required_ | The updated comment for the deployment review. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/deployments/:id/update_review_comment \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "comment": ":comment"
          }'
```

</api-code>

### Response

```json
{
    "review": {
        "deployment_id": 6390,
        "reviewer_id": 29036,
        "status": "approved",
        "comment": "Looks good!",
        "updated_at": "2024-10-11T13:43:19.547-07:00"
    }
}
```

* * *

## Deploy an approved deployment

Deploys an approved deployment. The **Require review and approval** toggle must be enabled in **Workspace admin > Settings > Deployments** to access this endpoint.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/deployments/:id/deploy
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _required_ | The unique identifier of the deployment. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| include\_tags | **boolean** _optional_ | Specify whether the deployment should include tags. |

### Sample request

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/deployments/:id/deploy \
      -H 'Authorization: Bearer <api_token>' \
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
