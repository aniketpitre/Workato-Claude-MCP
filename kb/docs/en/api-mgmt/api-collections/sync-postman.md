---
url: 'https://docs.workato.com/en/api-mgmt/api-collections/sync-postman.md'
description: >-
  Sync a deployed Workato API collection to your Postman workspace to increase
  visibility and drive adoption through internal and external portals.
---

# Sync to Postman

You can make your API collection available beyond the original client after your API collection is successfully deployed and live. Increase the visibility of any API collection by syncing it to your [Postman](https://www.postman.com/) workspace. You can use the Postman internal and external portals to drive adoption.

1. Open the API collection that you plan to sync.
   
2. Go to the **Settings** tab and select **Sync to Postman**.
   
   ![Sync to Postman](/assets/sync-to-postman.VvN8M23R.png)_Sync to Postman_
   
3. Choose an existing Postman connection or create a new one to connect your Postman workspace.
   
4. Specify where to store the API collection in Postman:
   
   - Select **New API in Postman** to create a new API object.
   - Save this API collection in an existing Postman API.
   
   > **SAVE API collection IN AN EXISTING POSTMAN API**
   > 
   > You must provide a version name if you save this API collection into an existing Postman API. Workato recommends that you give this a distinct version name. You may choose to overwrite an existing version.
   
5. Click **Sync API collection** to complete the sync.
   

Workato sends the OpenAPI Specification of the collection to Postman and stores it as a new or existing version of the selected API. You can now configure this version for publishing within Postman to your developer community.

You can click **Refresh sync** to update the Postman API with the latest version of the collection after changes are made in Workato.

---
