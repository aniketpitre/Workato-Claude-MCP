---
url: 'https://docs.workato.com/en/api-mgmt/api-collections/configure-settings.md'
description: >-
  Configure Workato API collection settings, including version, description,
  URL, sharing, and Postman sync for recipe, proxy, and AI gateway collections.
---

# Configure collection settings

You can configure API recipe, API proxy, and AI gateway collection settings, URL settings, sharing settings, and settings to sync to Postman. Complete the following steps to configure options for an API recipe collection, API proxy collection, or AI gateway collection:

1. Go to **Platform > API platform > API collections** and select the API collection you plan to configure.
   
2. Click the **Settings** tab and then select one of the following interfaces:
   
   - [Collection settings](#collection-settings)
   - [URL settings](#url-settings)
   - [Sharing](#sharing)
   - [Sync to Postman](/en/api-mgmt/api-collections/sync-postman)

## Collection settings

Complete the following steps to update the version and description of your API collection:

1. Go to **Platform > API platform > API collections** and select the API collection you plan to configure.
   
2. Click the **Settings** tab.
   
3. Select **Collection settings** from the sidebar.
   
   ![API collection settings tab](/assets/api-settings-tab.DNuSR2wR.png)_API collection settings tab_
   
4. Enter a **Version** number. This must be a unique 1–10 character identifier. Collections with the same name but different versions are treated as separate objects.
   
5. Add a **Description** to describe the purpose or usage of the collection.
   

## URL settings

You can use the URL settings to customize the path for your API collection. Available options vary based on the collection type.

> **OAUTH2 IS A RESERVED NAMESPACE**
> 
> `oauth2` is a reserved namespace. A collection path can't begin with `oauth2`.

### API proxy collection

Complete the following steps to configure URL settings for an API proxy collection:

1. Go to **Platform > API platform > API collections** and select the API proxy collection you plan to configure.
   
2. Click the **Settings** tab.
   
3. Select **URL settings**.
   
4. Define a custom URL path for this collection in the **Collection path** field. The **Proxy URL preview** updates as you type. Use this field to distinguish collections by function (for example, sales, marketing, or HR). The [domain](/en/api-mgmt/custom-domain)￼and [path prefix](/en/api-mgmt/api-prefix) prefix￼are configured through the API Platform's **Settings** tab, not the collection settings.
   
5. Click **Switch** in the **Target HTTP connection** section to select a different HTTP connection. The **Target URL preview** updates based on your selection.
   

### API recipe collection

Complete the following steps to configure URL settings for an API recipe collection:

1. Go to **Platform > API platform > API collections** and select the API recipe collection you plan to configure.
   
2. Click the **Settings** tab.
   
3. Select **URL settings**.
   
   ![API recipe collection URL settings](/assets/api-recipe-collection-url-settings.C88ZcgMY.png)_API recipe collection URL settings_
   
4. Define a custom URL path for this API recipe collection in the **Collection path** field. You can use this field to distinguish collections by team or use case. The [domain](/en/api-mgmt/custom-domain)￼and [path prefix](/en/api-mgmt/api-prefix) prefix￼are configured through the API Platform's **Settings** tab, not the collection settings.
   

## Sharing

New collections are hidden from the API library by default. Complete the following steps to update the visibility of your collection:

1. Go to **Platform > API platform > API collections** and select the collection you plan to manage.
   
2. Click the **Settings** tab, then select **Sharing**.
   
3. View the current visibility status. The message `Hidden from this workspace's API library` appears by default.
   
   ![API collection is hidden from the API library](/assets/api-collection-hidden-in-library.C4ZFKmM7.png)_API collection is hidden from the API library_
   
4. Click **Show in API library** to make the collection discoverable to everyone in your workspace. This enables users to find the collection and request access to use it.
   
   The UI updates to display the message **Discoverable in this workspace's API library** and lists the users who can see the collection.
   
   ![API collection is discoverable in the API library](/assets/api-collection-shown-in-library.s8gO-Kt4.png)_API collection is discoverable in the API library_
   
5. Select **Hide from API library** to hide the collection again.

---
