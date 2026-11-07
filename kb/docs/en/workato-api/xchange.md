---
url: 'https://docs.workato.com/en/workato-api/xchange.md'
description: >-
  Reference for the Workato XChange API to browse and create packages, review
  and approve versions, publish to the private library, distribute packages,
  manage sharing links, and view installation analytics.
---

# Developer API - XChange

Use this resource to manage [XChange](/en/xchange) packages programmatically. You can browse and author packages and versions, review and approve submitted versions, publish to the private library, distribute packages to workspaces, manage sharing links, and view installation analytics.

> **AVAILABILITY**
> 
> XChange APIs are available for workspaces with [XChange](/en/xchange) enabled. Requests from workspaces without owner or contributor access to XChange return a `404` error.

Ensure the necessary API client permissions are enabled to access these endpoints.

## Rate limits

XChange resources have the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [XChange](/en/workato-api/xchange.html) endpoints | 60 requests per second |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/xchange/packages](#list-packages) | List packages visible to the caller. |
| GET | [/api/xchange/packages/:package\_id/versions](#list-a-packages-versions) | List a package's versions. |
| GET | [/api/xchange/versions/:version\_id](#get-a-package-version) | Get a package version. |
| PUT | [/api/xchange/versions/:version\_id](#update-a-versions-metadata) | Update a version's metadata. |
| POST | [/api/xchange/packages/import](#import-a-new-package-from-a-zip) | Import a new package from a `.zip`. |
| POST | [/api/xchange/packages/:package\_id/versions/import](#import-a-new-package-version-from-a-zip) | Import a new package version from a `.zip`. |
| GET | [/api/xchange/versions/:draft\_id/version\_draft](#get-version-creation-status) | Get version creation status. |
| GET | [/api/xchange/packages/versions/:version\_id/export](#get-a-version-zip-download-url) | Get a version `.zip` download URL. |
| POST | [/api/xchange/versions/:version\_id/approve](#approve-a-package-version) | Approve a package version. |
| POST | [/api/xchange/versions/:version\_id/reject](#reject-a-package-version) | Reject a package version. |
| POST | [/api/xchange/versions/:version\_id/reset](#reset-a-version-review) | Reset a version review. |
| PUT | [/api/xchange/versions/:version\_id/comment/:review\_id](#update-a-review-comment) | Update a review comment. |
| PUT | [/api/xchange/packages/:package\_id/versions/:version\_id/publish](#publish-a-version) | Publish a version. |
| PUT | [/api/xchange/packages/:package\_id/versions/:version\_id/unpublish](#unpublish-a-version) | Unpublish a version. |
| GET | [/api/xchange/packages/:package\_id/consumers](#list-package-consumers) | List the consumers of a package. |
| POST | [/api/xchange/distributions](#create-a-distribution-batch) | Create and enqueue a distribution batch. |
| GET | [/api/xchange/distributions](#list-distribution-batches) | List distribution batches. |
| GET | [/api/xchange/distributions/:id](#get-a-distribution-batch-by-id) | Get a distribution batch by ID. |
| POST | [/api/xchange/distributions/:id/retry\_failed](#retry-failed-distributions) | Retry failed distributions in a batch. |
| GET | [/api/xchange/packages/:package\_id/sharing/links](#list-sharing-links) | List a package's sharing links. |
| POST | [/api/xchange/packages/:package\_id/sharing/links](#create-sharing-links) | Create sharing links. |
| POST | [/api/xchange/packages/:package\_id/sharing/links/:link\_id/activate](#activate-a-sharing-link) | Activate a sharing link. |
| POST | [/api/xchange/packages/:package\_id/sharing/links/:link\_id/deactivate](#deactivate-a-sharing-link) | Deactivate a sharing link. |
| DELETE | [/api/xchange/packages/:package\_id/sharing/links/:link\_id](#delete-a-sharing-link) | Delete a sharing link. |
| PUT | [/api/xchange/packages/:package\_id/versions/:version\_id/share](#set-the-packages-shared-link-version) | Set the package's shared-link version. |
| DELETE | [/api/xchange/packages/:package\_id/versions/:version\_id/share](#clear-the-packages-shared-link-version) | Clear the package's shared-link version. |
| GET | [/api/xchange/packages/:package\_id/stats](#get-package-installation-statistics) | Get package installation statistics. |
| GET | [/api/xchange/packages/:package\_id/installations](#get-per-workspace-installation-report) | Get per-workspace installation report. |

## Browse & create

The following endpoints let you list, view, create, import, and update packages and versions, and download a version export.

### List packages

Lists the packages visible to the caller.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/packages
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| status | **string** _optional_ | Filters packages by the status of their versions or publications. |
| builder\_id | **number** _optional_ | Filters packages by builder user ID. |
| tenant\_builder\_id | **number** _optional_ | Filters packages by tenant-builder workspace ID. |
| text | **string** _optional_ | Searches packages by name. |
| sort | **string** _optional_ | The field to sort by. Add a leading `-` to sort in descending order. |
| page\[number\] | **number** _optional_ | Page number. |
| page\[size\] | **number** _optional_ | Number of items per page. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/packages?text=sales&page[number]=1&page[size]=100' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

```json
{
    "data": [
        {
            "id": "1d2e3f4a-5b6c-4d7e-8f90-a1b2c3d4e5f6",
            "name": "Sales automation",
            "description": "Recipes and connections for sales automation.",
            "is_own": true,
            "is_published": true,
            "last_version": {
                "version": "1.2.0",
                "status": "published",
                "release_notes": "- New: Invoice sync recipe.\n- Improved: Connection error messages.",
                "connectors": [
                    "salesforce",
                    "netsuite"
                ]
            },
            "latest_activity": {
                "user_id": 45231,
                "user_name": "Ariel",
                "event_type": "package_version_created",
                "timestamp": "2026-07-10T09:15:32.000-07:00"
            }
        },
        {
            "id": "2e3f4a5b-6c7d-4e8f-9a0b-1c2d3e4f5a6b",
            "name": "Marketing sync",
            "description": "Recipes for marketing and CRM sync.",
            "is_own": true,
            "is_published": false,
            "last_version": {
                "version": "1.0.0",
                "status": "pending_review",
                "release_notes": "- Added: Lead sync recipe.\n- Improved: Field mapping.",
                "connectors": [
                    "hubspot"
                ]
            },
            "latest_activity": {
                "user_id": 45455,
                "user_name": "Dana",
                "event_type": "package_version_created",
                "timestamp": "2026-08-20T10:05:00.000-07:00"
            }
        }
    ],
    "page": {
        "number": 1,
        "size": 100
    },
    "total": 2
}
```

### List a package's versions

Lists a package's versions with per-version installation counts. These counts are a lightweight, counts-only surface. For the full statistics surface, use [Get package installation statistics](#get-package-installation-statistics).

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| builder\_id | **number** _optional_ | Filters versions by the builder who created them. |
| created\_at\_from | **string** _optional_ | Returns versions created on or after this date. Format: `YYYY-MM-DD`. |
| created\_at\_to | **string** _optional_ | Returns versions created on or before this date. Format: `YYYY-MM-DD`. |
| exclude\_rejected | **boolean** _optional_ | Set to `true` to exclude rejected versions from the response. |
| page\[number\] | **number** _optional_ | Page number. |
| page\[size\] | **number** _optional_ | Number of items per page. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions?exclude_rejected=true' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

```json
{
    "data": [
        {
            "id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
            "version": "1.2.0",
            "status": "published",
            "release_notes": "- New: Invoice sync recipe.\n- Improved: Connection error messages.\n- Fixed: Timeout on large syncs.",
            "created_at": "2026-07-10T09:15:32.000-07:00",
            "last_installed_at": "2026-07-16T08:41:15.000-07:00",
            "installations": {
                "direct": 12,
                "private_library": 4,
                "sharing_link": 1
            }
        },
        {
            "id": "8e7d6c5b-4a3f-4c2d-9e1a-0b8c7d6e5f4a",
            "version": "1.1.0",
            "status": "approved",
            "release_notes": "- Added: Initial CRM sync recipe.",
            "created_at": "2026-06-02T09:00:00.000-07:00",
            "last_installed_at": null,
            "installations": {
                "direct": 0,
                "private_library": 0,
                "sharing_link": 0
            }
        }
    ],
    "max_installations_count": 12,
    "page": {
        "number": 1,
        "size": 100
    },
    "total": 2
}
```

### Get a package version

Shows one version.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/versions/:version_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _required_ | The UUID of the version. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/versions/:version_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

The response includes `private_library_publication` only when the version is published to the private library.

```json
{
    "data": {
        "id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
        "version": "1.2.0",
        "status": "published",
        "builder_id": 45231,
        "builder": {
            "id": 45231,
            "name": "Ariel",
            "avatar_url": "https://www.workato.com/assets/avatars/ariel.png"
        },
        "description": "Sales automation starter package.",
        "release_notes": "- New: Invoice sync recipe.\n- Improved: Connection error messages.\n- Fixed: Timeout on large syncs.",
        "created_at": "2026-07-10T09:15:32.000-07:00",
        "project_handles": ["sales-automation"],
        "content": {
            "counters": {
                "recipe": 6
            },
            "connectors": [
                "salesforce",
                "netsuite"
            ]
        },
        "package": {
            "id": "1d2e3f4a-5b6c-4d7e-8f90-a1b2c3d4e5f6",
            "name": "Sales automation",
            "description": "Recipes and connections for sales automation."
        },
        "projects": [
            {
                "id": 7801234,
                "name": "Sales automation",
                "folder_id": 27180380
            }
        ],
        "installations": {
            "direct": 12,
            "private_library": 4,
            "sharing_link": 1
        },
        "private_library_publication": {
            "id": "4d5e6f7a-8b9c-4d0e-8f1a-2b3c4d5e6f7a",
            "card_description": "A starter package for sales automation.",
            "version": {
                "id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
                "version": "1.2.0"
            }
        },
        "review": {
            "id": "3c4d5e6f-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
            "status": "approved",
            "comments": "Approved for distribution.",
            "updated_at": "2026-07-16T11:02:10.000-07:00",
            "author": {
                "id": 45301,
                "name": "Bola",
                "avatar_url": "https://www.workato.com/assets/avatars/bola.png"
            }
        }
    }
}
```

### Update a version's metadata

Updates an existing version's editable metadata. The endpoint re-fetches and returns the full version.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/xchange/versions/:version_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _required_ | The UUID of the version to update. |

#### Payload

Only `version`, `description`, and `release_notes` are permitted. The endpoint ignores any other field in the request body.

| Name | Type | Description |
| --- | --- | --- |
| version | **string** _optional_ | The version label, for example `1.3.0`. |
| description | **string** _optional_ | The package version's description. |
| release\_notes | **string** _optional_ | The version's release notes. |

##### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/xchange/versions/:version_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "release_notes": "Adds the invoice sync recipe and fixes a connection timeout."
         }'
```

</api-code>

##### Response

The response returns the full version in the same format as the [Get a package version](#get-a-package-version-response) endpoint, with `release_notes` reflecting the update. The response includes `private_library_publication` only when the version is published to the private library.

```json
{
    "data": {
        "id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
        "version": "1.2.0",
        "status": "published",
        "builder_id": 45231,
        "builder": {
            "id": 45231,
            "name": "Ariel",
            "avatar_url": "https://www.workato.com/assets/avatars/ariel.png"
        },
        "description": "Sales automation starter package.",
        "release_notes": "Adds the invoice sync recipe and fixes a connection timeout.",
        "created_at": "2026-07-10T09:15:32.000-07:00",
        "project_handles": ["sales-automation"],
        "content": {
            "counters": {
                "recipe": 6
            },
            "connectors": [
                "salesforce",
                "netsuite"
            ]
        },
        "package": {
            "id": "1d2e3f4a-5b6c-4d7e-8f90-a1b2c3d4e5f6",
            "name": "Sales automation",
            "description": "Recipes and connections for sales automation."
        },
        "projects": [
            {
                "id": 7801234,
                "name": "Sales automation",
                "folder_id": 27180380
            }
        ],
        "installations": {
            "direct": 12,
            "private_library": 4,
            "sharing_link": 1
        },
        "private_library_publication": {
            "id": "4d5e6f7a-8b9c-4d0e-8f1a-2b3c4d5e6f7a",
            "card_description": "A starter package for sales automation.",
            "version": {
                "id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
                "version": "1.2.0"
            }
        },
        "review": {
            "id": "3c4d5e6f-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
            "status": "approved",
            "comments": "Approved for distribution.",
            "updated_at": "2026-07-16T11:02:10.000-07:00",
            "author": {
                "id": 45301,
                "name": "Bola",
                "avatar_url": "https://www.workato.com/assets/avatars/bola.png"
            }
        }
    }
}
```

### Import a new package from a .zip

Imports a `.zip` as a net-new package and its first version. The endpoint validates the file extension and a 100 MB size cap synchronously, then stages and enqueues an asynchronous import job. Poll the job's progress with [Get version creation status](#get-version-creation-status).

There's no `name` parameter. The draft package name comes from the uploaded filename. If you omit `version`, it defaults to `v1.0`.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/packages/import
```

</api-code>

#### Request body

Send the request as `multipart/form-data`.

| Name | Type | Description |
| --- | --- | --- |
| file | **file** _required_ | The package `.zip` file. Maximum size is 100 MB. |
| version | **string** _optional_ | The version label for the first version. Defaults to `v1.0`. |
| description | **string** _optional_ | The package's description. |
| release\_notes | **string** _optional_ | The first version's release notes. |

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/packages/import' \
      -H 'Authorization: Bearer <api_token>' \
      -F 'file=@/path/to/marketing_sync.zip' \
      -F 'version=v1.0' \
      -F 'description=Recipes for marketing and CRM sync.'
```

</api-code>

##### Response

The response returns the new draft's ID and a link to poll its status. Use [Get version creation status](#get-version-creation-status) to monitor the import.

```json
{
    "data": {
        "version_draft_id": 1576,
        "link": "/api/xchange/versions/1576/version_draft"
    }
}
```

### Import a new package version from a .zip

Imports a `.zip` as a new version of an existing package, using the same asynchronous pipeline as a net-new package import.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/import
```

</api-code>

> **REQUIRED VERSION**
> 
> `version` is required for this endpoint. A missing `version` returns a `400` error before the draft is created. An inaccessible or unknown `package_id` returns a `404` error.

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package to add the version to. |

#### Request body

Send the request as `multipart/form-data`.

| Name | Type | Description |
| --- | --- | --- |
| file | **file** _required_ | The package `.zip` file. Maximum size is 100 MB. |
| version | **string** _required_ | The version label, for example `1.3.0`. |
| description | **string** _optional_ | The version's description. |
| release\_notes | **string** _optional_ | The version's release notes. |

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/import' \
      -H 'Authorization: Bearer <api_token>' \
      -F 'file=@/path/to/sales_automation_v1.3.zip' \
      -F 'version=1.3.0' \
      -F 'release_notes=Adds the invoice sync recipe.'
```

</api-code>

##### Response

On success, the response returns the same shape as [Import a new package from a .zip](#import-a-new-package-from-a-zip-response). A missing `version` returns a `400` error instead:

```json
{
    "errors": [
        {
            "code": 400,
            "title": "A version is required"
        }
    ]
}
```

### Get version creation status

Polls the status of a version draft created by a `.zip` import. The response returns draft status only. It doesn't include generated asset contents or a diff.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/versions/:draft_id/version_draft
```

</api-code>

> **DRAFT OWNERSHIP**
> 
> A draft is scoped to the caller's environment and builder. A draft that isn't owned by the caller in the current environment returns a `404` error.

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| draft\_id | **integer** _required_ | The `version_draft_id` returned by the import endpoint. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/versions/:draft_id/version_draft' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

`error_message` is populated only when `status` is `failed`.

```json
{
    "data": {
        "version_draft_id": 1576,
        "status": "completed",
        "error_message": null,
        "package_id": "01a086c1-ae0a-7057-b66b-ee4d6b66467c",
        "version_id": "01a0b04e-e2d4-7694-855a-94aa08a4071e"
    }
}
```

### Get a version .zip download URL

Gets a short-lived, presigned download URL for a package version's `.zip`. The API doesn't stream the file directly. It returns a URL you can use to download it.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/packages/versions/:version_id/export
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _required_ | The UUID of the version to export. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/packages/versions/:version_id/export' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

```json
{
    "data": {
        "version_id": "01a086d3-de39-7e8a-85c2-35437eed7de4",
        "download_url": "https://file-storage.workato.com/sharing/files?sign=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9...<truncated>"
    }
}
```

## Review and approval

The following endpoints let the package owner approve, reject, reset, or comment on a submitted version:

### Approve a package version

Approves a submitted package version.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/versions/:version_id/approve
```

</api-code>

> **SELF-REVIEW RESTRICTION**
> 
> Builders can't approve or reject their own package versions unless auto-approval is enabled for the hub. A self-review attempt returns a `404` error.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _required_ | The UUID of the package version to approve. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| comments | **string** _required_ | Review comments to record with the approval. |

### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/versions/:version_id/approve' \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "comments": "Approved for distribution."
         }'
```

</api-code>

### Response

The response returns the full package version. The response includes `private_library_publication` only when the version is published to the private library.

```json
{
    "data": {
        "id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
        "version": "1.2.0",
        "status": "approved",
        "builder_id": 45231,
        "description": "Sales automation starter package.",
        "release_notes": "Adds the invoice sync recipe.",
        "created_at": "2026-07-10T09:15:32.000-07:00",
        "project_handles": ["sales-automation"],
        "package": {
            "id": "1d2e3f4a-5b6c-4d7e-8f90-a1b2c3d4e5f6",
            "name": "Sales automation",
            "description": "Recipes and connections for sales automation."
        },
        "content": {
            "counters": {},
            "connectors": []
        },
        "projects": [
            {
                "id": 7801234,
                "name": "Sales automation",
                "folder_id": 27180380
            }
        ],
        "installations": {
            "direct": 12,
            "private_library": 4,
            "sharing_link": 1
        },
        "review": {
            "id": "3c4d5e6f-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
            "status": "approved",
            "comments": "Approved for distribution.",
            "updated_at": "2026-07-16T11:02:10.000-07:00",
            "author": {
                "id": 45301,
                "name": "Bola",
                "avatar_url": "https://www.workato.com/assets/avatars/bola.png"
            }
        },
        "builder": {
            "id": 45231,
            "name": "Ariel",
            "avatar_url": "https://www.workato.com/assets/avatars/ariel.png"
        }
    }
}
```

### Reject a package version

Rejects a submitted package version.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/versions/:version_id/reject
```

</api-code>

> **SELF-REVIEW RESTRICTION**
> 
> Builders can't approve or reject their own package versions unless auto-approval is enabled for the hub. A self-review attempt returns a `404` error.

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _required_ | The UUID of the package version to reject. |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| comments | **string** _required_ | Review comments to record with the rejection. |

### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/versions/:version_id/reject' \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "comments": "Update the connection descriptions before you resubmit."
         }'
```

</api-code>

### Response

The response returns the full package version in the same format as the [Approve a package version](#approve-a-package-version-response) endpoint, with the version and review status reflecting the rejection.

### Reset a version review

Resets a submitted version's review to its pre-review state. The request takes no body.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/versions/:version_id/reset
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _required_ | The UUID of the version to reset. |

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/versions/:version_id/reset' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Update a review comment

Updates an existing review comment.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/xchange/versions/:version_id/comment/:review_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _required_ | The UUID of the version. |
| review\_id | **string** _required_ | The ID of the review to update. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| comments | **string** _required_ | The updated review comments. |

##### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/xchange/versions/:version_id/comment/:review_id' \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "comments": "Approved. Nice work on the connection cleanup."
         }'
```

</api-code>

## Private Library

The following endpoints let the package owner publish or unpublish a version to the Discovery Layer's private library.

### Publish a version

Publishes an approved version to the private library.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/:version_id/publish
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |
| version\_id | **string** _required_ | The UUID of the version to publish. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| card\_description | **string** _optional_ | The description shown on the package's private library card. |

##### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/:version_id/publish' \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "card_description": "A starter package for sales automation."
         }'
```

</api-code>

##### Response

The response returns the full version, including a `private_library_publication` object.

```json
{
    "data": {
        "id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
        "version": "1.2.0",
        "status": "published",
        "builder_id": 45231,
        "builder": {
            "id": 45231,
            "name": "Ariel",
            "avatar_url": "https://www.workato.com/assets/avatars/ariel.png"
        },
        "description": "Sales automation starter package.",
        "release_notes": "- New: Invoice sync recipe.\n- Improved: Connection error messages.\n- Fixed: Timeout on large syncs.",
        "created_at": "2026-07-10T09:15:32.000-07:00",
        "project_handles": ["sales-automation"],
        "content": {
            "counters": {
                "recipe": 6
            },
            "connectors": [
                "salesforce",
                "netsuite"
            ]
        },
        "package": {
            "id": "1d2e3f4a-5b6c-4d7e-8f90-a1b2c3d4e5f6",
            "name": "Sales automation",
            "description": "Recipes and connections for sales automation."
        },
        "projects": [
            {
                "id": 7801234,
                "name": "Sales automation",
                "folder_id": 27180380
            }
        ],
        "installations": {
            "direct": 12,
            "private_library": 4,
            "sharing_link": 1
        },
        "private_library_publication": {
            "id": "4d5e6f7a-8b9c-4d0e-8f1a-2b3c4d5e6f7a",
            "card_description": "A starter package for sales automation.",
            "version": {
                "id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
                "version": "1.2.0"
            }
        },
        "review": {
            "id": "3c4d5e6f-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
            "status": "approved",
            "comments": "Approved for distribution.",
            "updated_at": "2026-07-16T11:02:10.000-07:00",
            "author": {
                "id": 45301,
                "name": "Bola",
                "avatar_url": "https://www.workato.com/assets/avatars/bola.png"
            }
        }
    }
}
```

### Unpublish a version

Removes the package's private library publication. Existing installations remain.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/:version_id/unpublish
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |
| version\_id | **string** _required_ | The UUID of the published version. |

##### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/:version_id/unpublish' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

The response returns the full version with `status` reverted to `approved` and `private_library_publication` removed.

```json
{
    "data": {
        "id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
        "version": "1.2.0",
        "status": "approved",
        "builder_id": 45231,
        "builder": {
            "id": 45231,
            "name": "Ariel",
            "avatar_url": "https://www.workato.com/assets/avatars/ariel.png"
        },
        "description": "Sales automation starter package.",
        "release_notes": "- New: Invoice sync recipe.\n- Improved: Connection error messages.\n- Fixed: Timeout on large syncs.",
        "created_at": "2026-07-10T09:15:32.000-07:00",
        "project_handles": ["sales-automation"],
        "content": {
            "counters": {
                "recipe": 6
            },
            "connectors": [
                "salesforce",
                "netsuite"
            ]
        },
        "package": {
            "id": "1d2e3f4a-5b6c-4d7e-8f90-a1b2c3d4e5f6",
            "name": "Sales automation",
            "description": "Recipes and connections for sales automation."
        },
        "projects": [
            {
                "id": 7801234,
                "name": "Sales automation",
                "folder_id": 27180380
            }
        ],
        "installations": {
            "direct": 12,
            "private_library": 4,
            "sharing_link": 1
        },
        "review": {
            "id": "3c4d5e6f-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
            "status": "approved",
            "comments": "Approved for distribution.",
            "updated_at": "2026-07-16T11:02:10.000-07:00",
            "author": {
                "id": 45301,
                "name": "Bola",
                "avatar_url": "https://www.workato.com/assets/avatars/bola.png"
            }
        }
    }
}
```

## Direct Distribution

The following endpoints let the package owner mass-distribute a version to workspaces and list who consumes the package:

### List package consumers

Returns the consumers of a package. You can filter consumers by installation status and search by name or external ID.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/consumers
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| installation\_status | **string** _optional_ | Filters consumers by installation status. Accepted values: `not_installed`, `installed`. |
| version\_id | **string** _optional_ | The UUID of the package version. Required when `installation_status` is set to `installed`. |
| text | **string** _optional_ | Searches consumers by name or external ID. |
| page\[number\] | **number** _optional_ | Page number. |
| page\[size\] | **number** _optional_ | Number of items per page. Maximum is 500. |

##### Sample request

This request retrieves consumers of the package that installed a specific version.

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/consumers?installation_status=installed&version_id=:version_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

The `avatar_url` and `external_id` parameters must be set for the consumer to be included in the response.

```json
{
    "data": [
        {
            "id": 45231,
            "name": "Acme West",
            "avatar_url": "https://www.workato.com/assets/avatars/acme-west.png",
            "external_id": "acme-west-01"
        },
        {
            "id": 45232,
            "name": "Acme East"
        }
    ],
    "page": {
        "number": 1,
        "size": 100,
        "total": 2
    }
}
```

### Create a distribution batch

Creates a distribution batch for a package version and enqueues it for processing.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/distributions
```

</api-code>

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _required_ | The UUID of the package version to distribute. |
| environment\_ids | **array of integers** _required_ | The IDs of the target environments. |

##### Sample request

The following sample request distributes the package version to two target environments:

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/distributions' \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "version_id": ":version_id",
            "environment_ids": [40012, 40018]
         }'
```

</api-code>

##### Response

The endpoint returns a `201` response with the UUID of the new batch. Use the [Get a distribution batch by ID](#get-a-distribution-batch-by-id) endpoint to monitor the batch status.

```json
{
    "data": {
        "id": "6b7c8d9e-0f1a-4b2c-9d3e-4f5a6b7c8d9e"
    }
}
```

### List distribution batches

Returns a list of distribution batches, optionally scoped to a package.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/distributions
```

</api-code>

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _optional_ | The UUID of a package. Omit this parameter to list batches across all packages. |
| version\_id | **string** _optional_ | The UUID of a package version. |
| from | **timestamp** _optional_ | Returns batches created after this ISO 8601 timestamp. |
| to | **timestamp** _optional_ | Returns batches created before this ISO 8601 timestamp. |
| status | **string** _optional_ | Filters batches by status. Accepted values: `pending`, `in_progress`, `completed`. |
| active | **boolean** _optional_ | Set to `true` to return only `pending` and `in_progress` batches. |
| page\[number\] | **number** _optional_ | Page number. |
| page\[size\] | **number** _optional_ | Number of items per page. |

##### Sample request

The following sample request retrieves active distribution batches for a package version:

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/distributions?version_id=:version_id&active=true' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

```json
{
    "data": [
        {
            "id": "6b7c8d9e-0f1a-4b2c-9d3e-4f5a6b7c8d9e",
            "version_id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
            "version": "1.2.0",
            "status": "in_progress",
            "target_workspaces": {
                "total": 2,
                "pending": 1,
                "completed": 1,
                "failed": 0
            },
            "created_at": "2026-07-16T08:30:00.000-07:00"
        }
    ],
    "page": {
        "number": 1,
        "size": 100,
        "total": 1
    }
}
```

### Get a distribution batch by ID

Returns a distribution batch, optionally with per-target distribution details.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/distributions/:id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The UUID of the distribution batch. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| include\_details | **boolean** _optional_ | Set to `true` to include the per-target distribution details in the response. |
| page\[number\] | **number** _optional_ | Page number for the details list. Only applies when `include_details` is set to `true`. |
| page\[size\] | **number** _optional_ | Number of details per page. Only applies when `include_details` is set to `true`. |

##### Sample request

The following sample request retrieves a distribution batch with per-target details:

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/distributions/:id?include_details=true' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

The response includes the `details` array and the top-level `page` and `total` fields only when `include_details` is set to `true`. Each detail includes `error` only when the detail status is `failed`.

```json
{
    "data": {
        "id": "6b7c8d9e-0f1a-4b2c-9d3e-4f5a6b7c8d9e",
        "version_id": "9f8c2b1e-4a6d-4c2f-9e3a-7b5d1c0a8f21",
        "version": "1.2.0",
        "status": "completed",
        "target_workspaces": {
            "total": 2,
            "pending": 0,
            "completed": 1,
            "failed": 1
        },
        "created_at": "2026-07-16T08:30:00.000-07:00",
        "details": [
            {
                "id": "0a1b2c3d-4e5f-4a6b-8c7d-8e9f0a1b2c3d",
                "environment_id": 40012,
                "environment_name": "Acme West - prod",
                "environment_external_id": "acme-west-01",
                "status": "completed",
                "updated_at": "2026-07-16T08:41:15.000-07:00"
            },
            {
                "id": "5f6a7b8c-9d0e-4f1a-8b2c-3d4e5f6a7b8c",
                "environment_id": 40018,
                "environment_name": "Acme East - prod",
                "environment_external_id": "acme-east-01",
                "status": "failed",
                "error": "Connector version conflict in the target environment.",
                "updated_at": "2026-07-16T08:42:03.000-07:00"
            }
        ]
    },
    "page": 1,
    "total": 2
}
```

### Retry failed distributions

Retries and re-enqueues failed distributions in a batch for processing. The endpoint returns a `422` error if the batch doesn't contain failed distributions.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/distributions/:id/retry_failed
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| id | **string** _required_ | The UUID of the distribution batch. |

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/distributions/:id/retry_failed' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

##### Response

```json
{
    "data": {
        "id": "6b7c8d9e-0f1a-4b2c-9d3e-4f5a6b7c8d9e"
    }
}
```

## Link sharing

The following endpoints let the package owner manage a package's sharing links and its shared-link version:

### List sharing links

Lists a package's sharing links.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| status | **string** _optional_ | Filters links by status. Accepted values: `active`, `inactive`. |
| created\_by | **number** _optional_ | The numeric user ID of the link creator. |
| page\[number\] | **number** _optional_ | Page number. |
| page\[size\] | **number** _optional_ | Number of items per page. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links?status=active' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Create sharing links

Creates one public link, or one or more workspace-scoped links.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links
```

</api-code>

> **PUBLIC VS. WORKSPACE LINKS**
> 
> `name` is required for `public` links and rejected for `workspace` links. `workspace_ids` is required for `workspace` links, up to a maximum of 200, and rejected for `public` links.

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |

#### Payload

| Name | Type | Description |
| --- | --- | --- |
| kind | **string** _required_ | The type of link to create. Accepted values: `public`, `workspace`. |
| name | **string** _required for `public` links_ | A name for the public link. |
| workspace\_ids | **array of integers** _required for `workspace` links_ | The workspace IDs to create links for. Maximum 200. |

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links' \
      -H 'Authorization: Bearer <api_token>' \
      -H "Content-Type: application/json" \
      -d '{
            "kind": "public",
            "name": "Sales automation - partner preview"
         }'
```

</api-code>

### Activate a sharing link

Sets a link's status to `active`. You can call this endpoint multiple times without changing the result.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links/:link_id/activate
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |
| link\_id | **string** _required_ | The ID of the sharing link. |

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links/:link_id/activate' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Deactivate a sharing link

Sets a link's status to `inactive`. You can call this endpoint multiple times without changing the result.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links/:link_id/deactivate
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |
| link\_id | **string** _required_ | The ID of the sharing link. |

##### Sample request

<api-code>

```shell
curl  -X POST 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links/:link_id/deactivate' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Delete a sharing link

Permanently deletes a sharing link.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links/:link_id
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |
| link\_id | **string** _required_ | The ID of the sharing link to delete. |

##### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/sharing/links/:link_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Set the package's shared-link version

Marks a version that's `approved` or `published` as the package's shared-link version.

<api-code no-copy-method>

```
PUT https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/:version_id/share
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |
| version\_id | **string** _required_ | The UUID of the version to set as the shared-link version. |

##### Sample request

<api-code>

```shell
curl  -X PUT 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/:version_id/share' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Clear the package's shared-link version

Clears the package's shared-link version. This only succeeds when `version_id` in the URL matches the current shared-link version.

<api-code no-copy-method>

```
DELETE https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/:version_id/share
```

</api-code>

> **ACTIVE LINKS REMAIN**
> 
> Active sharing links remain in place after you clear the shared-link version. Consumer-side link resolution returns a `404` error until you set a new shared-link version. Passing a `version_id` that isn't the current shared-link version also returns a `404` error.

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |
| version\_id | **string** _required_ | The UUID of the current shared-link version. |

##### Sample request

<api-code>

```shell
curl  -X DELETE 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/versions/:version_id/share' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

## Analytics

The following endpoints return a package's installation statistics and per-workspace installation report:

### Get package installation statistics

Returns a package's installation statistics. The `summary` block is package-wide and isn't affected by the `version_id` filter or pagination. `by_version` is the paginated per-version breakdown.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/stats
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _optional_ | Filters the `by_version` breakdown to a single version. Doesn't affect `summary`. |
| page\[number\] | **number** _optional_ | Page number for the `by_version` breakdown. |
| page\[size\] | **number** _optional_ | Number of items per page for the `by_version` breakdown. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/stats' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Get per-workspace installation report

Returns a package's per-workspace installation report.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/installations
```

</api-code>

#### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| package\_id | **string** _required_ | The UUID of the package. |

#### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| version\_id | **string** _optional_ | Filters installations by version. |
| customer\_ids | **array of integers** _optional_ | Filters installations by consumer workspace ID. Omit this parameter to return all installations. An explicit empty array returns an empty page. |
| page\[number\] | **number** _optional_ | Page number. |
| page\[size\] | **number** _optional_ | Number of items per page. |

##### Sample request

<api-code>

```shell
curl  -X GET 'https://YOUR_DATA_CENTER/api/xchange/packages/:package_id/installations?version_id=:version_id' \
      -H 'Authorization: Bearer <api_token>'
```

</api-code>

---
