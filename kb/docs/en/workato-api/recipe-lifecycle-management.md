---
url: 'https://docs.workato.com/en/workato-api/recipe-lifecycle-management.md'
description: >-
  Reference for the Workato Recipe Lifecycle Management API to create export
  manifests and export, import, and download asset packages.
---

# Developer API - Recipe Lifecycle Management

- **Manifest:** A container of different assets, including recipes, lookup tables, connections, and more.
  
- **Package:** The build of a manifest. Contains the source code of each asset within a manifest. It includes the latest version of the asset available when the package was created.
  

## Rate limits

Recipe lifecycle management resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Import a package into a folder: [/api/packages/import/:folder\_id](/en/workato-api/recipe-lifecycle-management.html#import-package-into-a-folder) | 500 requests per hour per user ID. If this quota is exceeded, the system denies additional requests until the following hour when the request allowance resets. |
| All | All other [Recipe lifecycle management](/en/workato-api/recipe-lifecycle-management.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/export\_manifests/folder\_assets](#manifest-folder-assets) | View assets in a folder. |
| POST | [api/export\_manifests](#manifest-create) | Create an export manifest. |
| PUT | [api/export\_manifests/:id](#manifest-update) | Update an export manifest. |
| GET | [api/export\_manifests/:id](#manifest-view) | View an export manifest. |
| DELETE | [/api/export\_manifests/:id](#manifest-delete) | Delete an export manifest. |
| POST | [/api/packages/export/:manifest\_id](#export-package-based-on-a-manifest) | Export package based on a manifest. |
| POST | [/api/packages/import/:folder\_id](#import-package-into-a-folder) | Import package into a folder. |
| GET | [/api/packages/:id](#get-package-by-id) | Get package by ID. |
| GET | [/api/packages/:id/download](#download-package) | Download a package. |

* * *

## View assets in a folder

View assets in a folder. You can use this endpoint to help you create or update an export manifest.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/export_manifests/folder_assets
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| folder\_id | **integer** _optional_ | The ID of the folder containing the asset. Defaults to the root folder. |
| include\_test\_cases | **boolean** _optional_ | This parameter is currently not supported. Test cases are not included in the response. Defaults to `false.` |
| include\_data | **boolean** _optional_ | Includes data from the list of assets. Defaults to `false.` |

#### Sample request

<api-code>

```shell
curl -X GET 'https://YOUR_DATA_CENTER/api/export_manifests/folder_assets?folder_id=:folder_id_value' \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "result": {
    "assets": [
      {
        "id": 12,
        "name": "Copy of Recipeops",
        "type": "recipe",
        "version": 1,
        "folder": "",
        "absolute_path": "All projects",
        "root_folder": false,
        "unreachable": false,
        "zip_name": "copy_of_recipeops.recipe.json",
        "checked": true,
        "status": "added"
      },
      {
        "id": 13,
        "name": "My Salesforce account",
        "type": "connection",
        "version": 2,
        "folder": "Salesforce Integration Project",
        "absolute_path": "Salesforce Integration Project",
        "root_folder": false,
        "unreachable": false,
        "zip_name": "salesforce_account_v2.connection.json",
        "checked": true,
        "status": "updated"
      },
      {
        "id": 14,
        "name": "Submit request in New workflow app",
        "type": "page",
        "version": 1,
        "folder": "Workflow Automation Project",
        "absolute_path": "Workflow Automation Project",
        "root_folder": false,
        "unreachable": false,
        "zip_name": "submit_request_workflow_app.page.json",
        "checked": true,
        "status": "no change"
      }
    ]
  }
}
```

* * *

## Create an export manifest

Create an export manifest.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/export_manifests
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _required_ | Name of the new manifest. |
| assets | **object** _required_ | Dependent assets. Workato recommends reviewing the [View assets in a folder](#manifest-folder-assets) endpoint's response before using this endpoint. The **View assets in a folder** endpoint returns an `assets` object containing all assets in a specific folder. This can help you identify and format the assets you plan to include in your manifest. |
| id | **integer** _required_ | ID of the dependency. |
| type | **string** _required_ | Type of dependent asset. Refer to [Asset types](#create-manifest-types) to see all supported `type` values. |
| checked | **boolean** _optional_ | Determines if the asset is included in the manifest. Defaults to `true`. |
| version | **integer** _optional_ | The version of the asset. Defaults to the latest version. |
| folder | **string** _optional_ | The folder that contains the asset. Defaults to `""`. |
| absolute\_path | **string** _required_ | The absolute path of the asset. Defaults to root folder. |
| root\_folder | **boolean** _optional_ | Name root folder. Defaults to `false`. |
| unreachable | **boolean** _optional_ | Whether the asset is unreachable. Defaults to `false`. |
| zip\_name | **string** _optional_ | Name in the exported zip file. By default, Workato auto-generates a name with this structure: `asset_#{index}.#{type}.json`. |
| folder\_id | **integer** _optional_ | The ID of the folder containing the asset. Defaults to the root folder. |
| auto\_generate\_assets | **boolean** _optional_ | Auto-generates assets from a folder. Defaults to `false`. |
| include\_test\_cases | **boolean** _optional_ | Whether the manifest includes test cases from automatic asset generation. Defaults to `false`. |
| include\_data | **boolean** _optional_ | This parameter includes data from automatic asset generation. Defaults to `false`. |
| include\_tags | **boolean** _optional_ | Specifies whether to include tags assigned to assets in the export manifest. Tags are excluded from the manifest when set to `false`. Set to `false` by default. |

#### Asset types

Supported asset `type` values include:

- `recipe`
- `connection`
- `lookup_table`
- `workato_db_table`
- `account_property`
- `project_property`
- `workato_schema`
- `workato_template`
- `lcap_app`
- `lcap_page`
- `custom_adapter`
- `topic`
- `connection`
- `recipe`
- `api_group`
- `api_endpoint`

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/export_manifests' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "assets": [
                  {
                      "id": :asset_id,
                      "name": ":asset_name",
                      "type": ":type",
                      "version": :version,
                      "folder": ":folder",
                      "absolute_path": ":absolute_path",
                      "root_folder": :true_or_false,
                      "unreachable": :true_or_false,
                      "zip_name": ":zip_name",
                      "checked": :true_or_false
                  }
              ],
              "folder_id": :folder_id_value,
              "include_tags": :true_or_false
            }
          }'
```

</api-code>

### Response

```json
{
  "result": {
    "id": 12,
    "name": "Test Manifest",
    "last_exported_at": null,
    "created_at": "2023-02-27T02:44:59.447-08:00",
    "updated_at": "2023-02-27T02:44:59.447-08:00",
    "deleted_at": null,
    "project_path": "Folder 1",
    "status": "working"
  }
}
```

Create a manifest with multiple assets

You can pass multiple assets into the `assets` parameter to include them in the manifest.

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/export_manifests' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "assets": [
                {
                   "id": :asset_id_1,
                   "name": ":asset_name_1",
                   "type": ":asset_type_1",
                   "version": :asset_version_1,
                   "folder": ":asset_folder_1",
                   "absolute_path": ":asset_absolute_path_1",
                   "root_folder": :true_or_false,
                   "provider": ":asset_provider_1",
                   "unreachable": :true_or_false,
                   "zip_name": ":asset_zip_name_1",
                   "deps": [],
                   "checked": :true_or_false
                },
                {
                    "id": :asset_id_2,
                    "name": ":asset_name_2",
                    "type": ":asset_type_2",
                    "version": :asset_version_2,
                    "folder": ":asset_folder_2",
                    "absolute_path": ":asset_absolute_path_2",
                    "root_folder": :true_or_false,
                    "include_test_cases": :true_or_false,
                    "unreachable": :true_or_false,
                    "zip_name": ":asset_zip_name_2",
                    "deps": [],
                    "checked": :true_or_false
                  }
              ],
              "folder_id": :folder_id_value,
              "include_tags": :true_or_false
              }
            }'
```

</api-code>

##### Response

```json
{
    "result": {
        "id": 267546,
        "name": "Test Manifest with two assets",
        "created_at": "2025-03-21T07:50:29.488-07:00",
        "updated_at": "2025-03-21T07:50:29.488-07:00",
        "deleted_at": null,
        "last_exported_at": null,
        "project_path": "Home assets",
        "status": "working",
        "include_tags": true
    }
}
```

### Auto-generate assets

If you plan for Workato to auto-generate your assets, you can pass the parameter `auto_generate_assets` into the payload of the request. You must specify the `folder_id` you plan to have auto-generated. You can also choose to include test cases and data by adding the `include_test_cases` and `include_data` parameters. Note that test cases and data are excluded by default. Additionally, you can include `auto_run` in the payload to generate the package automatically.

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/export_manifests' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "folder_id": :folder_id_value,
              "auto_generate_assets": :true_or_false,
              "include_test_cases": :true_or_false,
              "include_data": :true_or_false,
              "auto_run": :true_or_false
            }
          }
          '
```

</api-code>

### Response

```json
{
  "result": {
    "id": 12,
    "name": "Test Manifest",
    "last_exported_at": null,
    "created_at": "2023-02-27T02:44:59.447-08:00",
    "updated_at": "2023-02-27T02:44:59.447-08:00",
    "deleted_at": null,
    "project_path": "Folder 1",
    "status": "working"
  }
}
```

#### Possible statuses

| Status | Definition |
| --- | --- |
| `working` | Active. |
| `archived` | Deleted. |

* * *

## Update an export manifest

Update an export manifest.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/export_manifests/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _string_ | The ID of the dependency. |

### Payload

Update the properties contained in `assets[]` to replace the assets previously defined.

| Name | Type | Description |
| --- | --- | --- |
| name | **string** _optional_ | Name of the manifest. Update this value to change the manifest name. Defaults to previous name. |
| assets | **object** _required_ | Dependent assets. Workato recommends reviewing the [View assets in a folder](#manifest-folder-assets) endpoint's response before using this endpoint. The **View assets in a folder** endpoint returns an `assets` object containing all assets in a specific folder. This can help you identify and format the assets you plan to update in your manifest. |
| id | **integer** _required_ | ID of the dependency. |
| type | **string** _required_ | Type of dependent asset. Refer to [Asset types](#update-manifest-types) to see all supported `type` values. |
| checked | **boolean** _optional_ | Determines if the asset is included in the manifest. Defaults to `true`. |
| version | **integer** _optional_ | The version of the asset. Defaults to the latest version. |
| folder | **string** _optional_ | The folder that contains the asset. Defaults to `""`. |
| absolute\_path | **string** _optional_ | The absolute path of the asset. Defaults to root folder. |
| root\_folder | **boolean** _optional_ | Name root folder. Defaults to `false`. |
| unreachable | **boolean** _optional_ | Whether the asset is unreachable. Defaults to `false`. |
| zip\_name | **string** _optional_ | Name in the exported zip file. By default, Workato auto-generates a name with this structure: `asset_#{index}.#{type}.json`. |
| folder\_id | **integer** _optional_ | The ID of the folder containing the asset. Defaults to the root folder. |
| auto\_generate\_assets | **boolean** _optional_ | Auto-generates assets from a folder. Defaults to `false`. |
| include\_test\_cases | **boolean** _optional_ | Whether the manifest includes test cases from automatic asset generation. Defaults to `false`. |
| include\_data | **boolean** _optional_ | This parameter includes data from automatic asset generation. Defaults to `false`. |

#### Asset types

Supported asset `type` values include:

- `recipe`
- `connection`
- `lookup_table`
- `workato_db_table`
- `account_property`
- `project_property`
- `workato_schema`
- `workato_template`
- `lcap_app`
- `lcap_page`
- `custom_adapter`
- `topic`
- `connection`
- `recipe`
- `api_group`
- `api_endpoint`

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/export_manifests/:id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "assets": [
                {
                  "id": :asset_id,
                  "name": ":asset_name",
                  "type": ":type",
                  "version": :version,
                  "folder": ":folder",
                  "absolute_path": ":absolute_path",
                  "root_folder": :true_or_false,
                  "unreachable": :true_or_false,
                  "zip_name": ":zip_name",
                  "checked": :true_or_false
                }
              ],
              "folder_id": :folder_id_value
            }
          }
          '
```

</api-code>

### Response

```json
{
  "result": {
    "id": 12,
    "name": "Test Manifest",
    "last_exported_at": null,
    "created_at": "2023-02-27T02:44:59.447-08:00",
    "updated_at": "2023-02-27T02:44:59.447-08:00",
    "deleted_at": null,
    "project_path": "Folder 1",
    "status": "working"
  }
}
```

Update a manifest with multiple assets

You can pass multiple assets into the `assets` parameter to update them in the manifest.

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/export_manifests/:id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "assets": [
                {
                   "id": :asset_id_1,
                   "name": ":asset_name_1",
                   "type": ":asset_type_1",
                   "version": :asset_version_1,
                   "folder": ":asset_folder_1",
                   "absolute_path": ":asset_absolute_path_1",
                   "root_folder": :true_or_false,
                   "provider": ":asset_provider_1",
                   "unreachable": :true_or_false,
                   "zip_name": ":asset_zip_name_1",
                   "deps": [],
                   "checked": :true_or_false
                },
                {
                    "id": :asset_id_2,
                    "name": ":asset_name_2",
                    "type": ":asset_type_2",
                    "version": :asset_version_2,
                    "folder": ":asset_folder_2",
                    "absolute_path": ":asset_absolute_path_2",
                    "root_folder": :true_or_false,
                    "include_test_cases": :true_or_false,
                    "unreachable": :true_or_false,
                    "zip_name": ":asset_zip_name_2",
                    "deps": [],
                    "checked": :true_or_false
                  }
              ],
              "folder_id": :folder_id_value
              }
            }'
```

</api-code>

##### Response

```json
{
    "result": {
        "id": 171350,
        "name": "Test Manifest with two assets",
        "created_at": "2025-03-19T07:45:50.915-07:00",
        "updated_at": "2025-03-21T09:26:46.348-07:00",
        "deleted_at": null,
        "last_exported_at": null,
        "project_path": "Home assets",
        "status": "working",
        "include_tags": true,
        "assets": [
            {
                "checked": true,
                "root_folder": false,
                "unreachable": false,
                "name": "Outreach",
                "zip_name": "API tests/outreach.connection.json",
                "id": 65008167,
                "type": "connection",
                "version": null,
                "folder": "API tests",
                "absolute_path": "All projects/API tests",
                "deps": []
            },
            {
                "checked": true,
                "root_folder": false,
                "unreachable": false,
                "name": "Test recipe",
                "zip_name": "API tests/test_recipe.recipe.json",
                "id": 86330482,
                "type": "recipe",
                "version": 4,
                "folder": "API tests",
                "absolute_path": "All projects/API tests",
                "include_test_cases": false,
                "deps": []
            }
        ],
        "diff_included": false
    }
}
```

### Auto-generate assets

If you plan for Workato to auto-generate your assets, you can pass the parameter `auto_generate_assets` into the payload of the request. You must specify the `folder_id` you plan to have auto-generated. You can also choose to include test cases and data by adding the `include_test_cases` and `include_data` parameters. Note that test cases and data are excluded by default. Additionally, you can include `auto_run` in the payload to generate the package automatically.

#### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/export_manifests/:id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "folder_id": :folder_id_value,
              "auto_generate_assets": :true_or_false,
              "include_test_cases": :true_or_false,
              "include_data": :true_or_false,
              "auto_run": :true_or_false
            }
          }
          '
```

</api-code>

### Response

```json
{
  "result": {
    "id": 12,
    "name": "Test Manifest",
    "last_exported_at": null,
    "created_at": "2023-02-27T02:44:59.447-08:00",
    "updated_at": "2023-02-27T02:44:59.447-08:00",
    "deleted_at": null,
    "project_path": "Folder 1",
    "status": "working"
  }
}
```

* * *

## View an export manifest

View an export manifest.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/export_manifests/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **integer** _string_ | The ID of the dependency. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/export_manifests/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "result": {
    "id": 12,
    "name": "Test Manifest",
    "last_exported_at": null,
    "created_at": "2023-02-27T02:44:59.447-08:00",
    "updated_at": "2023-02-27T02:44:59.447-08:00",
    "deleted_at": null,
    "project_path": "Folder 1",
    "status": "working"
  }
}
```

* * *

## Delete an export manifest

Delete an export manifest.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/export_manifests/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | Export manifest ID. |

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/export_manifests/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
    "result": {
        "success": true,
        "status": "destroyed"
    }
}
```

* * *

## Export a package based on a manifest

Export a package based on a manifest.

> **ENDPOINT PRIVILEGES ALSO PROVIDE ACCESS TO ASSETS**
> 
> When you provide an API client with privileges to this endpoint, the API client is also granted the ability to view other assets like recipes, lookup tables, Event topics, and message templates by examining the resulting zip file.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/packages/export/:id
```

</api-code>

This is an asynchronous request. Use [GET package by ID](#get-package-by-id) endpoint to get details of the exported package.

> **INCLUDE TAGS WHEN CREATING THE EXPORT MANIFEST**
> 
> To include tags in the exported package, set the `include_tags` attribute to `true` when calling the [Create an export manifest](#manifest-create) endpoint.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | Export manifest ID. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/packages/export/:manifest_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "id": 242,
  "operation_type": "export",
  "status": "in_progress",
  "include_tags": true,
  "export_manifest_id": 3,
  "download_url": null
}
```

> **RETRIEVE THE DOWNLOAD URL**
> 
> Use the [Get package by ID](#get-package-by-id) endpoint to monitor the export status. The download URL is available in the response after the process completes.

## Import a package into a folder

Import a package in zip file format into a folder. This endpoint allows an API client to create or update assets, such as recipes, lookup tables, event topics, and message templates, through package imports.

> **EVENT STREAM FOLDER PLACEMENT**
> 
> Event streams imported without folder information during the [transition period](/en/event-streams#event-streams-as-project-assets) are placed into the default **Event Streams Topics** project, which Workato creates the first time it's needed. You must specify a folder to import event stream packages after the transition period.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/packages/import/:id
```

</api-code>

This is an asynchronous request. Use [GET package by ID](#get-package-by-id) endpoint to get details of the imported the package.

The input (zip file) is a `application/octet-stream` payload containing package content. URL parameter **restart\_recipes** must be `true` if the running recipes need to be restarted upon import.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | Folder ID. |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| restart\_recipes | **boolean** _optional_ | Value must be `true` to allow the restarting of running recipes during import. Packages cannot be imported if there are running recipes and this parameter equals `false` or is not provided. |
| include\_tags | **boolean** _optional_ | Specifies whether to preserve tags assigned to assets when the package is imported into the folder. Tags are excluded from the import when set to `false`. Set to `false` by default. |
| folder\_id\_for\_home\_assets | **string** _conditionally required_ | The ID of a folder to store assets in instead of the root folder. The folder specified must be accessible to the API client and cannot be the root folder. Defaults to `""`. |

> **FOLDER\_ID\_FOR\_HOME\_ASSETS IS CONDITIONALLY REQUIRED**
> 
> The `folder_id_for_home_assets` parameter is required if:
> 
> - You are importing a package that contains root folder assets.
> - Your workspace **Home assets** folder has been converted to a **Home assets** project.
> 
> Refer to the [Home assets project](/en/projects#home-assets) section for more information.

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/packages/import/:folder_id?restart_recipes=:true_or_false&include_tags=:true_or_false' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/octet-stream' \
      --data-binary @'path/to/local/file.zip'
```

</api-code>

### Response

```json
{
   "id":251,
   "operation_type":"import",
   "status":"completed",
   "download_url":"https://www.workato-staging-assets.com/packages/zip_files/000/000/242/original/exportdemo.zip"
}
```

* * *

## Get package by ID

Get details of an imported or exported package.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/packages/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | Package ID. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/packages/:id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

- [Successful export](#successful-export)
- [Failed export](#failed-export)
- [Successful import](#successful-import)
- [Failed import](#failed-import)

#### Successful export

This response shows the result of retrieving a completed export manifest.

```json
{
   "id":242,
   "operation_type":"export",
   "status":"completed",
   "export_manifest_id":3,
   "download_url":"https://www.workato-staging-assets.com/packages/zip_files/000/000/242/original/exportdemo.zip"
}
```

#### Failed export

This response shows the result of retrieving a failed export manifest.

```json
{
   "id":242,
   "operation_type":"export",
   "status":"failed",
   "error":"error_message",
   "export_manifest_id":4,
   "download_url":null
}
```

#### Successful import

This response shows the result of retrieving a completed import package. The API response now includes `recipe_status.id` values immediately after the first import operation. Previously, the response contained only the IDs of updated recipes. Now, it includes the IDs of all recipes, including newly imported recipes. This response specifically returns only recipe IDs, not IDs of other assets within the package.

> **INFO**
> 
> For any completed import, it is important to also check each recipe's `import_result`. [Learn more about the possible import\_result values](#recipe-import-result-values).

```json
{
   "id": 242,
   "operation_type": "import",
   "status": "completed",
   "download_url": "https://www.workato-staging-assets.com/packages/zip_files/000/000/242/original/importdemo.zip",
   "recipe_status": [
      {
            "id": 12345,
            "import_result": "no_update_or_updated_without_restart"
      },
      {
            "id": 12346,
            "import_result": "restarted"
      },
      {
            "id": 12347,
            "import_result": "stopped"
      }
   ]
}
```

#### Failed import

This response shows the result of retrieving a failed import package.

> **INFO**
> 
> A failed import may return only a partial list in `recipe_status` if some recipes weren't updated before the failure occurred. [Learn more about the possible import\_result values.](#recipe-import-result-values).

```json
{
   "id": 242,
   "operation_type": "import",
   "status": "failed",
   "download_url": "https://www.workato-staging-assets.com/packages/zip_files/000/000/242/original/importdemo.zip",
   "recipe_status": [
      {
            "id": 12345,
            "import_result": "restart_failed"
      },
      {
            "id": 12346,
            "import_result": "restart_failed"
      },
      {
            "id": 12347,
            "import_result": "restart_failed"
      }
   ]
}
```

### Recipe import\_result values

There are a total of six possible results:

- `no_update_or_updated_without_restart`
  
- Indicates no restart was needed for the recipe. Either recipe could be updated without it or no update was made. **Successful import**
  
- `not_found`
  
- Unexpected error when recipe cannot be found. Should not often be seen. **Import has failed with no update to recipe.**
  
- `stop_failed`
  
- For recipes that need to be restarted, we attempt to stop the recipe. This state indicates we could not stop the recipe. **Import has failed with no update to recipe.**
  
- `stopped`
  
- Workato stopped the recipe but recipe was not restarted due to errors in the recipe. **Import has failed with recipe updated but not restarted**
  
- `restart_failed`
  
- Workato attempted to restart recipe but failed to do so. **Import has failed with recipe updated but not restarted**
  
- `restarted`
  
- Workato successfully restarted recipe after update. **Successful import**
  

* * *

## Download package

Downloads a package.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/packages/:id/download
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | Package ID. |

#### Sample request

<api-code>

```shell
curl  -L -X GET 'https://YOUR_DATA_CENTER/api/packages/:id/download' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

> **Follow redirects in cURL**
> 
> Use the `-L` flag to follow redirect paths.

### Response

If successful, you will be redirected to the package content. Returns `404` if package not found or doesn't have content.

---
