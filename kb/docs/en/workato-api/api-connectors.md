---
url: 'https://docs.workato.com/en/workato-api/api-connectors.md'
description: >-
  Reference for the Workato developer API endpoints that return standard and
  platform connector metadata, useful for building an app marketplace.
---

# Developer API - Connectors

Use these API endpoints to obtain information about standard Workato connectors. This is useful if you plan to generate a marketplace of apps.

## Rate limits

Connector resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Connectors](/en/workato-api/api-connectors.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/integrations](#list-connector-metadata) | Returns a list of connectors and metadata specified in request. |
| GET | [/api/integrations/all](#list-all-platform-connectors) | Returns a paginated list of all connectors and associated metadata in a non-embedded workspace. The response includes standard and platform connectors. |

## List connector metadata

Returns a list of connectors and associated metadata specified in the API request.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/integrations
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| applications | **string** _required_ | Comma separated connector identifiers. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/integrations \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{
            "applications": ":applications"
          }'
```

</api-code>

### Sample response

View a sample response

```json
{
    "items": [
        {
            "name": "google_drive",
            "title": "Google Drive",
            "categories": [
                "Document/File",
                "Sales Enablement"
            ],
            "oauth": true,
            "deprecated": false,
            "secondary": false,
            "triggers": [
                {
                    "name": "new_file_in_subfolder",
                    "title": "New file or folder in folder hierarchy",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "new_file_or_folder",
                    "title": "New file or folder",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                }
            ],
            "actions": [
                {
                    "name": "__adhoc_http_action",
                    "title": "Custom action",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_folder",
                    "title": "Create folder",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "download_file_contents",
                    "title": "Download file",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "move_rename_file",
                    "title": "Rename or move file/folder",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "search_file_or_folder",
                    "title": "Search files or folders",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "upload_file",
                    "title": "Upload small file",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "upload_file_stream",
                    "title": "Upload large file",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                }
            ]
        },
        {
            "name": "service_now",
            "title": "ServiceNow",
            "categories": [
                "Customer Service",
                "IT Service Management"
            ],
            "oauth": true,
            "deprecated": false,
            "secondary": false,
            "triggers": [
                {
                    "name": "closed_incident",
                    "title": "Closed incident",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "new_incident",
                    "title": "New incident",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "new_object",
                    "title": "New record",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "new_object_webhook",
                    "title": "New record",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "new_sys_user",
                    "title": "New user",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "scheduled_query",
                    "title": "Scheduled record search",
                    "deprecated": false,
                    "bulk": false,
                    "batch": true
                },
                {
                    "name": "updated_incident",
                    "title": "New/updated incident",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "updated_object",
                    "title": "New/updated record",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "updated_object_webhook",
                    "title": "New/updated record",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "updated_sys_user",
                    "title": "New/updated user",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                }
            ],
            "actions": [
                {
                    "name": "__adhoc_http_action",
                    "title": "Custom action",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "assign_user_to_incident",
                    "title": "Assign user to incident",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_asset",
                    "title": "Create asset",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_catalog_task",
                    "title": "Create catalog task",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_change",
                    "title": "Create change",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_core_company",
                    "title": "Create core company",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_incident",
                    "title": "Create incident",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_object",
                    "title": "Create record",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_object_using_template",
                    "title": "Create record using a template",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_problem",
                    "title": "Create problem",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "create_user",
                    "title": "Create user",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "get_incident",
                    "title": "Get incident details by ID",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "get_user",
                    "title": "Get user details by ID",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "lookup_user",
                    "title": "Search users",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "search_assets",
                    "title": "Search assets",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "search_companies",
                    "title": "Search companies",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "search_objects",
                    "title": "Search records",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "search_objects_v2",
                    "title": "Search records",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "search_users",
                    "title": "Search users",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "search_using_query",
                    "title": "Search records using query",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "update_asset",
                    "title": "Update asset",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "update_company",
                    "title": "Update company",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "update_incident",
                    "title": "Update incident",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "update_object",
                    "title": "Update record",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "update_object_using_template",
                    "title": "Update record using a template",
                    "deprecated": false,
                    "bulk": false,
                    "batch": false
                },
                {
                    "name": "update_user",
                    "title": "Update user",
                    "deprecated": true,
                    "bulk": false,
                    "batch": false
                }
            ]
        }
    ]
}
```

## List all platform connectors

Returns a paginated list of all connectors and associated metadata in a non-embedded workspace. This includes both standard and platform connectors. Workato includes the total number of records at the end of the response.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/integrations/all
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| page | **integer** _optional_ | Page number. Defaults to 1. If the total number of connectors exceeds the record per page quota, call the next page to retrieve subsequent pages. |
| per\_page | **integer** _optional_ | Number of records per page. Defaults to 1 and has a maximum of 100. If you enter more than 100, Workato only returns 100 records in the response. |

### Sample request

<api-code>

```shell
curl  -X GET https://YOUR_DATA_CENTER/api/integrations/all?page=:page_value&per_page=:per_page_value \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Response

```json
    "count": 293,
    "page": 1,
    "per_page": 90
```

  

> **ABRIDGED RESPONSE**
> 
> The preceding response is abridged to display the total record count returned in the response. For an example of the connectors and associated metadata Workato returns for each record, see the [list connector metadata API.](#list-connector-metadata)

---
