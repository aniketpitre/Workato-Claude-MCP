---
url: 'https://docs.workato.com/en/oem/oem-api/recipe-lifecycle-management.md'
description: >-
  Reference for Embedded Partner API endpoints to create export manifests and
  import or export packages in customer workspaces.
---

# Embedded API - Recipe lifecycle management

The following endpoints are available to Embedded partners only. These endpoints allow you to create and manage export manifests programmatically. You can also use these endpoints to import and export a package to or from a customer workspace using one set of API credentials.

If you plan to import or export packages to or from your own environments (not customer workspaces), use the endpoints listed in the [Developer API](/en/workato-api/recipe-lifecycle-management) documentation.

> **GLOSSARY**
> 
> - **Manifest:** A container of different assets, including recipes, lookup tables, connections, and more.
>   
> - **Package:** The build of a manifest. Contains the source code of each asset within a manifest. It includes the latest version of the asset available when the package was created.
>   

## Rate limits

Recipe lifecycle management resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| POST | Import package into a customer workspace: [/api/managed\_users/:managed\_user\_id /imports](/en/oem/oem-api/recipe-lifecycle-management.html#package-import) | 1,000 requests per minute |
| GET | Get status of package import: [/api/managed\_users/:managed\_user\_id /imports/:package\_id](/en/oem/oem-api/recipe-lifecycle-management.html#get-package-status) | 1,000 requests per minute |
| All | All other [Recipe lifecycle management](/en/oem/oem-api/recipe-lifecycle-management.html) endpoints | 60 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/export\_manifests/folder\_assets](#manifest-folder-assets) | View assets in a folder. |
| POST | [/api/managed\_users/:managed\_user\_id/export\_manifests](#manifest-create) | Create an export manifest. |
| PUT | [/api/managed\_users/:managed\_user\_id/export\_manifests/:id](#manifest-update) | Update an export manifest. |
| GET | [/api/managed\_users/:managed\_user\_id/export\_manifests/:id](#manifest-view) | View an export manifest. |
| DELETE | [/api/managed\_users/:managed\_user\_id/export\_manifests/:id](#manifest-delete) | Delete an export manifest. |
| POST | [/api/managed\_users/:id/imports](#package-import) | Import package into a folder in a customer workspace. |
| GET | [/api/managed\_users/:id/imports/:package\_id](#get-package-status) | Get status of an imported package. |
| POST | [/api/managed\_users/:managed\_user\_id/exports/:manifest\_id](#export-package) | Export package based on the manifest ID. Requires an Embedded workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/exports/:package\_id](#export-status-get) | Returns the status of a package export. Requires an Embedded workspace. |

* * *

## View assets in a folder

View assets in a folder. You can use this endpoint to help you create or update an export manifest.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests/folder_assets
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |
| folder\_id | **integer** _optional_ | The ID of the folder containing the asset. Defaults to the root folder. |
| include\_test\_cases | **boolean** _optional_ | This parameter includes test cases from the list of assets. Defaults to `false.` |
| include\_data | **boolean** _optional_ | This parameter includes data from the list of assets. Defaults to `false.` |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests?folder_id=:folder_id' \
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
        "checked": true
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
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

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
| absolute\_path | **string** _optional_ | The absolute path of the asset. Defaults to root folder. |
| root\_folder | **boolean** _optional_ | Name the root folder. Defaults to `false`. |
| unreachable | **boolean** _optional_ | Whether the asset is unreachable. Defaults to `false`. |
| zip\_name | **string** _optional_ | Name in the exported zip file. By default, Workato auto-generates a name with this structure: `asset_#{index}.#{type}.json`. |
| folder\_id | **integer** _optional_ | The ID of the folder containing the asset. Defaults to the root folder. |
| auto\_generate\_assets | **boolean** _optional_ | Auto-generates assets from a folder. Defaults to `false.` |
| include\_test\_cases | **boolean** _optional_ | This parameter includes test cases from automatic asset generation. Defaults to `false.` |
| include\_data | **boolean** _optional_ | This parameter includes data from automatic asset generation. Defaults to `false.` |
| auto\_run | **boolean** _optional_ | Starts export package generation automatically. Defaults to `false.` |
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
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "assets": [
                {
                  "id": ":id",
                  "name": ":name",
                  "type": ":type",
                  "version": ":version",
                  "folder": ":folder",
                  "absolute_path": ":absolute_path",
                  "root_folder": :true_or_false,
                  "unreachable": :true_or_false,
                  "zip_name": ":zip_name",
                  "checked": :true_or_false
                }
              ],
              "folder_id": ":folder_id",
              "include_tags": :true_or_false
            }
          }'
```

</api-code>

Create a manifest with multiple assets

You can pass multiple assets into the `assets` parameter to include them in the manifest.

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "assets": [
                {
                   "id": ":id",
                   "name": ":name",
                   "type": ":type",
                   "version": ":version",
                   "folder": ":folder",
                   "absolute_path": ":absolute_path",
                   "root_folder": :true_or_false,
                   "provider": ":provider",
                   "unreachable": :true_or_false,
                   "zip_name": ":zip_name",
                   "deps": [],
                   "checked": :true_or_false
                }
              ],
              "folder_id": ":folder_id",
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

If you plan for Workato to auto-generate your assets, you can pass the parameter `auto_generate_assets` into the payload of the request. You must specify the `folder_id` you plan to have auto-generated. You can also choose to include test cases and data by including the `include_test_cases` or `include_data` parameters. Otherwise, they are excluded by default. Additionally, you can include `auto_run` in the payload to generate the package automatically.

#### Sample request

<api-code>

```shell

curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "folder_id": ":folder_id",
              "auto_generate_assets": :true_or_false,
              "include_test_cases": :true_or_false,
              "include_data": :true_or_false,
              "auto_run": :true_or_false
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
PUT https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the dependency. |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

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
| auto\_generate\_assets | **boolean** _optional_ | Auto-generates assets from folder. Defaults to `false.` |
| include\_test\_cases | **boolean** _optional_ | Includes test cases in auto generation assets. Defaults to `false.` |
| include\_data | **boolean** _optional_ | Includes data in auto generation assets. Defaults to `false.` |
| auto\_run | **boolean** _optional_ | Starts export package generation automatically. Defaults to `false.` |

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
curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests/:id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "assets": [
                {
                  "id": ":id",
                  "name": ":name",
                  "type": ":type",
                  "version": ":version",
                  "folder": ":folder",
                  "absolute_path": ":absolute_path",
                  "root_folder": :true_or_false,
                  "unreachable": :true_or_false,
                  "zip_name": ":zip_name",
                  "checked": :true_or_false
                }
              ],
              "folder_id": ":folder_id"
            }
          }
          '
```

</api-code>

Update a manifest with multiple assets

You can pass multiple assets into the `assets` parameter to update them in the manifest.

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests/:id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "assets": [
                {
                   "id": ":id",
                   "name": ":name",
                   "type": ":type",
                   "version": ":version",
                   "folder": ":folder",
                   "absolute_path": ":absolute_path",
                   "root_folder": :true_or_false,
                   "provider": ":provider",
                   "unreachable": :true_or_false,
                   "zip_name": ":zip_name",
                   "deps": [],
                   "checked": :true_or_false
                }
              ],
              "folder_id": ":folder_id"
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

If you plan for Workato to auto-generate your assets, you can pass the parameter `auto_generate_assets` into the payload of the request. You must specify the `folder_id` you plan to have auto-generated. You can also choose to include test cases and data by including the `include_test_cases` or `include_data` parameters. Otherwise, they are excluded by default. Additionally, you can include `auto_run` in the payload to generate the package automatically.

#### Sample request

<api-code>

```shell

curl  -X PUT 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests/:id' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "export_manifest": {
              "name": ":name",
              "folder_id": ":folder_id",
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
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The ID of the dependency. |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests/:id' \
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
DELETE https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests/:id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | Export manifest ID. |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

#### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/export_manifests/:id' \
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

## Import package into a customer workspace

Import a package in zip file format into a specified folder in a customer workspace. This endpoint allows an API client to create or update assets, such as recipes, lookup tables, event topics, and message templates, through package imports.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/imports
```

</api-code>

This is an asynchronous request. Use the [Get package status](#get-package-status) endpoint to get details of the imported the package.

The input (zip file) is an `application/octet-stream` payload containing package content. The query parameter `restart_recipes` must be set to `true` if the running recipes need to be restarted upon import.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| folder\_id | **string** _required_ | Folder ID. |
| restart\_recipes | **boolean** _optional_ | Value must be `true` to allow the restarting of running recipes during import. Packages cannot be imported if there are running recipes and this parameter equals `false` or is not provided. |
| include\_tags | **boolean** _optional_ | Specifies whether to preserve tags assigned to assets when importing the package into the folder. Tags are excluded from the import when set to `false`. Set to `false` by default. |
| folder\_id\_for\_home\_assets | **string** _conditionally required_ | The ID of a folder to store assets in instead of the root folder. The folder specified must be accessible to the API client and cannot be the root folder. Defaults to `""`. |

> **FOLDER\_ID\_FOR\_HOME\_ASSETS IS CONDITIONALLY REQUIRED**
> 
> The `folder_id_for_home_assets` parameter is required if:
> 
> - You are importing a package that contains root folder assets.
> - The customer's workspace **Home assets** folder has been converted to a **Home assets** project.
> 
> Refer to the [Home assets project](/en/projects#home-assets) section for more information.

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/imports?folder_id=:folder_id&include_tags=:true_or_false' \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/octet-stream' \
      -F 'path/to/local/file.zip'
```

</api-code>

### Response

```json
{
   "id":251,
   "operation_type":"import",
   "status":"completed"
}
```

* * *

## Get status of package import

Get details of a package imported into a customer workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/imports/:package_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID or external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| package\_id | **string** _required_ | Package ID. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/imports/:package_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Responses

- [Successful import](#successful-import)
- [Failed import](#failed-import)

#### Successful import

The following response is returned when an import is completed successfully.

> **IMPORT RESULTS**
> 
> For any completed import, it is important to also check each recipe's `import_result`. [Learn more about the possible import\_result values.](#recipe-import-result-values)

```json
{
   "id":242,
   "operation_type":"export",
   "status":"completed",
   "recipe_status":[
      {
            "id": 12345,
            "import_result": "no_update_or_update_without_restart"
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

The following response is returned when an import fails.

> **IMPORT RESULTS**
> 
> For any failed import, not all recipes may be returned in `recipe_status` as they may not have been updated before the import failed. [Learn more about the possible import\_result values.](#recipe-import-result-values)

```json
{
   "id":198,
   "operation_type":"export",
   "status":"failed",
   "error":"error_message",
   "recipe_status":[
      {
            "id": 12345,
            "import_result": "no_update_or_update_without_restart"
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

### Recipe import\_result values

There are a total of six (6) possible results:

- `no_update_or_update_without_restart` - This indicates no restart was needed for the recipe. Either recipe could be updated without it or no update was made. **Successful import**
- `not_found` - Unexpected error when recipe cannot be found. Should not often be seen. **Import has failed with no update to recipe.**
- `stop_failed` - For recipes that need to be restarted, we attempt to stop the recipe. This state indicates we could not stop the recipe. **Import has failed with no update to recipe.**
- `stopped` - Workato stopped the recipe but recipe was not restarted due to errors in the recipe. **Import has failed with recipe updated but not restarted**
- `restart_failed` - Workato attempted to restart recipe but failed to do so. **Import has failed with recipe updated but not restarted**
- `restarted` - Workato successfully restarted recipe after update. **Successful import**

* * *

## Export package

Export a package using the manifest ID. This endpoint requires an Embedded workspace.

Use the [Get export status](#export-status-get) endpoint to retrieve details on the exported package.

> **WARNING**
> 
> Providing an API client with privilege to this endpoint indirectly gives it the ability to create/update other assets like recipes, lookup tables, Event topics and message templates by examining the resultant zip file.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/exports/:manifest_id
```

</api-code>

  

> **INCLUDE TAGS WHEN CREATING THE EXPORT MANIFEST**
> 
> To include tags in the exported package, set the `include_tags` attribute to `true` when calling the [Create an export manifest](#manifest-create) endpoint.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| manifest\_id | **string** _required_ | The ID of the manifest you plan to export. |

#### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/exports/:manifest_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
  "id": 365,
  "operation_type": "export",
  "status": "in_progress",
  "include_tags": true,
  "export_manifest_id": 508,
  "download_url": null
}
```

> **RETRIEVE THE DOWNLOAD URL**
> 
> Use the [Get export status](#export-status-get) endpoint to monitor the export status. The download URL is available in the response after the process completes.

* * *

## Get export status

Returns the status of an exported package. Requires an Embedded workspace.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/exports/:package_id
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer Account ID or External ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| package\_id | **string** _required_ | The ID of the package. |

#### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/exports/:package_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
{
      "id":370,
      "operation_type":"export",
      "status":"completed",
      "export_manifest_id":513,
      "download_url":"https://www.workato-staging-assets.com/packages/zip_files/000/000/242/original/exportdemo.zip"
}
```

---
