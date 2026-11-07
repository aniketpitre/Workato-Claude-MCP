---
url: 'https://docs.workato.com/en/oem/oem-api/tag-assignments.md'
description: >-
  Reference for the Embedded API endpoint that applies tags to or removes tags
  from recipes and connections in a customer workspace.
---

# Embedded API - Tag assignments

Use this endpoint to apply tags to or remove tags from assets in a customer workspace.

> **TAG APIS**
> 
> To create, retrieve, update, and delete tags programmatically, refer to our [Environment management](/en/oem/oem-api/environment-management) API documentation.

## Rate limits

The tag assignments resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Tag assignments](/en/oem/oem-api/tag-assignments.html) endpoints | 1,000 requests per minute |

### Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v2/managed\_users/:managed\_user\_id/tags\_assignments](#manage-tag-assignments) | Apply tags to or remove tags from assets in a customer workspace. |

## Manage tag assignments

Applies or removes tags from assets in a customer workspace. This endpoint can tag recipes and connections only. You can assign one or more tags to these assets or remove existing tags.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/tags_assignments
```

</api-code>

### URL parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. The External ID must be URL encoded and prefixed with an `E` (for example, `EA2300`). |

### Payload

| Name | Type | Description |
| --- | --- | --- |
| add\_tags | **array of strings** _optional_ | An array of tag handles to be added, for example `tag-Abx8sFmg-NWx3Lb-CD`. Use the tag handle, not the tag title. Each handle represents an existing tag to be applied to the specified assets. |
| remove\_tags | **array of strings** _optional_ | An array of tag handles to be removed. Each handle represents a tag to be removed from the specified assets. |
| recipe\_ids | **array of integers** _conditional_ | An array of recipe IDs to tag or untag. **Required** if `connection_ids` is not provided. |
| connection\_ids | **array of integers** _conditional_ | An array of connection IDs to tag or untag. **Required** if `recipe_ids` is not provided. |

> **USE TAG HANDLES, NOT TAG TITLES**
> 
> This endpoint accepts tag handles only, and a tag must exist before you can assign it. Retrieve the handle of an existing tag with the [List tags](/en/oem/oem-api/environment-management#list-tags) (`GET /api/v2/managed_users/:managed_user_id/tags`) endpoint or [Create a tag](/en/oem/oem-api/environment-management#create-a-tag) (`POST /api/v2/managed_users/:managed_user_id/tags`), which returns the tag `handle`.
> 
> The request returns `200 OK` and doesn't apply a tag when a value in `add_tags` or `remove_tags` doesn't match an existing tag handle. The response doesn't include an error. A request with both valid and unrecognized values applies the valid handles and ignores invalid input.

A tag is available in all environments of the customer workspace. Tag assignments apply only to the recipes and connections in the environment whose workspace ID you pass as `managed_user_id`.

Refer to [Create and assign a tag](#create-and-assign-a-tag) for a complete example that creates a tag, assigns it to a recipe, and verifies the result.

### Sample request

This request adds a tag to a connection and a recipe in Workato.

<api-code>

```shell
curl  -X POST "https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/tags_assignments" \
      -H "Authorization: Bearer <api_token>" \
      -H "Content-Type: application/json" \
      -d '{
            "add_tags": [":tag_handle"],
            "recipe_ids": [:recipe_id],
            "connection_ids": [:connection_id]
          }'
```

</api-code>

### Response

A `200 OK` status means Workato accepted the request. No content is returned in the response body.

The endpoint also returns `200 OK` when a tag handle isn't recognized, so a `200 OK` status doesn't confirm that the tag was applied. Refer to [Create and assign a tag](#create-and-assign-a-tag) for an example of retrieving the tags assigned to an asset.

### Create and assign a tag

This example creates a tag in a customer workspace, assigns it to a recipe, and confirms the assignment. Use `connection_ids` in place of `recipe_ids` to tag a connection.

1. Create the tag with the `POST /api/v2/managed_users/:managed_user_id/tags` endpoint. The `title` field is the only required field.
   
   <api-code>

   ```shell
   curl  -X POST "https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/tags" \
         -H "Authorization: Bearer <api_token>" \
         -H "Content-Type: application/json" \
         -d '{
               "title": "HR"
             }'
   ```

   </api-code>
   
   Copy the `handle` value from the response. The handle in this example is `tag-Abx8sFmg-NWx3Lb-CD`. The `description` is `null` because the request doesn't set one, and Workato assigns a random `color`.
   
   ```json
   {
     "data": {
       "handle": "tag-Abx8sFmg-NWx3Lb-CD",
       "title": "HR",
       "description": null,
       "color": "plum"
     }
   }
   ```
   
2. Assign the tag to the recipe by passing the handle from the previous step in `add_tags`, not the title `HR`.
   
   <api-code>

   ```shell
   curl  -X POST "https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/tags_assignments" \
         -H "Authorization: Bearer <api_token>" \
         -H "Content-Type: application/json" \
         -d '{
               "add_tags": ["tag-Abx8sFmg-NWx3Lb-CD"],
               "recipe_ids": [1234567]
             }'
   ```

   </api-code>
   
3. Verify the assignment by listing the tags assigned to the recipe with the `q[recipe_id_eq]` query parameter of the [List tags](/en/oem/oem-api/environment-management#list-tags) endpoint. The response includes the tag if the assignment succeeded.
   
   <api-code>

   ```shell
   curl  -X GET "https://YOUR_DATA_CENTER/api/v2/managed_users/:managed_user_id/tags?q[recipe_id_eq]=1234567" \
         -H "Authorization: Bearer <api_token>"
   ```

   </api-code>
   
   ```json
   {
     "data": {
       "tags": [
         {
           "handle": "tag-Abx8sFmg-NWx3Lb-CD",
           "title": "HR",
           "description": null,
           "color": "plum",
           "created_at": "2026-10-14T09:11:17.344-07:00",
           "updated_at": "2026-10-14T09:11:17.344-07:00"
         }
       ]
     }
   }
   ```
   
   An empty `tags` array means the tag wasn't applied. Check that `add_tags` contains the tag handle and not the title.

---
