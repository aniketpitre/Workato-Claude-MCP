---
url: 'https://docs.workato.com/en/connectors/redmine.md'
description: >-
  Connect Workato to Redmine with OAuth 2.0 to retrieve, search, create, and
  update issues.
---

# Redmine

[Redmine](https://www.redmine.org) is an open-source project management and issue tracking application. The Redmine connector enables you to retrieve, search, create, and update issues in Workato using the [Redmine REST API](https://www.redmine.org/projects/redmine/wiki/Rest_api).

## Install Redmine from the community library

Complete the following steps to install the Redmine connector from the [community library](https://www.workato.com/browse/connectors):

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

The Redmine connector uses OAuth 2.0 authentication with the authorization code grant.

Planio-hosted Redmine also supports other authentication methods, but this connector supports only OAuth 2.0.

### Minimum and default scopes

Select only the scopes you selected when you registered the application in Redmine. The **Scopes** field is optional. The connector doesn't request any scopes from Redmine if you don't select any scopes. However, actions require specific scopes. The actions fail with a 403 Forbidden error if you don't request the scopes required for the action you plan to use.

You need the following scopes to use all Redmine actions:

| Scope | Required for |
| --- | --- |
| **View issues** | Get record and Search records actions. |
| **Add issues** | Create record action. |
| **Edit issues** | Update record action. |
| **Add notes** | Adding a note with the Update record action. |

### Redmine setup

Complete the following steps to register Workato as an OAuth application in Redmine:

1. Sign in to your Redmine instance as an administrator.
   
2. Go to **Administration > Settings > API** and enable the **REST API**.
   
3. Go to **Administration > Applications** and click **New Application**.
   
4. Enter a **Name** for the application.
   
5. Enter `https://www.workato.com/oauth/callback` as the **Redirect URI**.
   
6. Select the required **Scopes** for the actions you plan to use. Refer to [Minimum and default scopes](#scopes) for more information.
   
7. Click **Save**, and then copy the **Application Id** and **Secret**.
   

Refer to the [Planio documentation](https://support.plan.io/projects/planio-support-en/wiki/Using_the_Redmine_REST_API_with_OAuth2_at_Planio) for more information about using Planio with Redmine.

### Connect to Redmine using OAuth 2.0

Complete the following steps to connect to Redmine in Workato:

1. Click **Create > Connection**.
   
2. Search for `Redmine` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the host of your Redmine account in the **Domain** field. Don't include `https://`. For example, `acme.plan.io`.
   
6. Enter the application ID you copied from Redmine in the **Application ID** field.
   
7. Enter the secret you copied from Redmine in the **Secret** field.
   
8. Optional. Use the **Scopes** drop-down menu to select the scopes to request. You must also select these scopes when you register the application in Redmine. Click **Use custom value** to enter space-separated scopes manually. For example, `view_issues add_issues`.
   
   Refer to [Minimum and default scopes](#scopes) for more information.
   
9. Click **Connect**.
   
10. Sign in to Redmine and authorize the application when prompted.

---
