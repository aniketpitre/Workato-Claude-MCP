---
url: 'https://docs.workato.com/en/connectors/tiktok.md'
description: >-
  Connect TikTok to Workato to read creator profiles, list videos, and publish
  videos or photo carousels through TikTok's Content Posting API.
---

# TikTok

[TikTok](https://www.tiktok.com) is a short-form video platform. The TikTok connector uses TikTok's Content Posting API and Display API to read a creator's profile and videos and publish posts in Workato.

Use the TikTok connector to:

- Get a user's profile or creator info.
- List a user's videos, or retrieve specific videos by video ID.
- Publish a video or photo carousel.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any TikTok API endpoint. Refer to the [TikTok API](https://developers.tiktok.com/doc/tiktok-api-v2-introduction) documentation for endpoint details.

## Install TikTok from the community library

Complete the following steps to install the TikTok connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The TikTok connector uses OAuth 2.0 authentication.

> **UNAUDITED APPS CAN'T POST PUBLICLY**
> 
> TikTok requires direct posts from unaudited developer apps to use the **Only me** privacy setting. Submit your app for a TikTok app audit to publish public posts.

### Minimum and default scopes

The TikTok connector requests the `user.info.basic` scope by default. Leave the **Scopes** field blank to also request the following scopes:

- `user.info.profile`
- `user.info.stats`
- `video.list`
- `video.publish`
- `video.upload`

Select one or more scopes to replace this default set. The connection then requests `user.info.basic` and only the scopes you select. Select the scopes your recipes need, including any extra scopes for custom actions:

- `user.info.profile`
- `user.info.stats`
- `video.list`
- `video.publish`
- `video.upload`
- `local.product.manage`
- `local.shop.manage`
- `local.voucher.manage`
- `portability.activity.ongoing`
- `portability.activity.single`
- `portability.all.ongoing`
- `portability.all.single`
- `portability.directmessages.ongoing`
- `portability.directmessages.single`
- `portability.postsandprofile.ongoing`
- `portability.postsandprofile.single`
- `research.adlib.basic`
- `research.data.basic`
- `research.data.u18eu`
- `research.data.vra`

### TikTok setup

Complete the following sections to create a TikTok developer app and generate credentials for Workato:

- [Create the app](#create-app)
- [Add app details](#app-details)
- [Add and configure products](#products)
- [Add scopes and submit](#scopes-and-submit)

#### Create the app

Complete the following steps to create the TikTok developer app and copy your credentials:

1. Sign in to [TikTok for Developers](https://developers.tiktok.com/).
   
2. Click **Developer Portal > Manage apps**.
   
3. Click **Connect an app**.
   
4. Select an **Ownership** option and click **Confirm**.
   
5. Enter a **Name** to display to TikTok users.
   
6. Select the **App type**. You can't change this value later.
   
7. Click **Create app**.
   
8. Copy the **Client key** and **Client secret** under **Credentials**. Save these credentials for use in Workato.
   

#### Add app details

Complete the following steps to add the app details TikTok requires for review:

1. Add or select the following required **Basic information**:
   
   - **App icon**
   - **Category**
   - **Description**
   - **Terms of Service URL**
   - **Privacy Policy URL**
   - **Platforms**
2. Add an explanation for your app submission under **App review**.
   
3. Upload a demo video.
   

#### Add and configure products

Complete the following steps to add the products your app uses and configure them:

1. Click **\+ Add products**.
   
2. Click **\+ Add** for **Login Kit**.
   
3. Click **\+ Add** for **Content Posting API**.
   
4. Click **Done**.
   
5. Enter `https://www.workato.com/oauth/callback` as the **Redirect URI** in the **Login Kit** configuration.
   
6. Enable direct posting in the **Content Posting API** configuration. Your app can only send drafts to the creator inbox if you skip this step. Refer to TikTok's [Content Posting API](https://developers.tiktok.com/doc/content-posting-api-get-started) documentation for more information.
   

#### Add scopes and submit

Complete the following steps to add scopes and submit your app for review:

1. Verify the domain or URL prefix that hosts your media files under **URL properties**. Refer to [Verify a domain or URL prefix](#url-verification) for more information.
   
2. Click **\+ Add scopes** to add scopes. The connector requests the `user.info.basic` scope by default. Refer to [Minimum and default scopes](#scopes) for more information.
   
3. Click **Submit for review**.
   

### Verify a domain or URL prefix

TikTok rejects media URLs that aren't on a domain or URL prefix you verified. The [Publish photo carousel](/en/connectors/tiktok/publish-photo-carousel-action) action requires verified URLs. The [Publish video](/en/connectors/tiktok/publish-video-action) action requires them when **Source** is **Pull from URL**.

Add the domain or URL prefix under **URL properties** in your TikTok app and verify ownership before you submit the app for review. Refer to TikTok's [Media Transfer Guide](https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide) for verification methods and detailed steps.

### Connect to TikTok using OAuth 2.0

Complete the following steps to set up a TikTok connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `TikTok` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![TikTok connection setup](/assets/tiktok-connection-setup.CGSfVXpb.png)_TikTok connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client key** and **Client secret**.
   
6. Optional. Use the **Scopes** drop-down menu to select the scopes to request. Refer to [Minimum and default scopes](#scopes) for more information.
   
7. Click **Connect**.
   
8. Sign in to TikTok when prompted to authorize the connection.

---
