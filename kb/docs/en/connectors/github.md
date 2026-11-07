---
url: 'https://docs.workato.com/en/connectors/github.md'
description: >-
  The GitHub connector enables you to build powerful automation around GitHub to
  help manage these software development processes and manage your agile
  sprints.
---

# GitHub

[GitHub](https://github.com/) is a popular version control application used by millions of developers and companies.

The GitHub connector enables you to build powerful automation around GitHub to help manage these software development processes and manage your agile sprints.

> **FEATURE AVAILABILITY**
> 
> The GitHub connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## Use cases

Integrate the GitHub connector with your collaboration and project management tools to automate development workflows. You can streamline release management, inform teams, and document critical updates across platforms. Explore our [use cases](/en/getting-started/workato-use-cases) to discover how you can enhance your GitHub processes:

- [Generate Confluence release notes](/en/getting-started/use-cases/openai-github-confluence) from merged GitHub PRs.
- [Create summarized Confluence notes and Jira comments](/en/getting-started/use-cases/github-jira-confluence) from closed GitHub PRs.
- [Post GitHub milestones](/en/getting-started/use-cases/github-workbot-for-slack) with Workbot for Slack.

## API version

This connector uses the GitHub [REST API v3](https://docs.github.com/en/free-pro-team@latest/rest).

## How to connect to GitHub on Workato

Connect to GitHub on Workato using one of the following methods:

- OAuth authentication. Workato recipes act on your behalf. Refer to [OAuth authentication](#oauth-authentication) for more information.
- GitHub Apps. Workato recipes act as the app. Refer to [GitHub App authentication](#github-app-authentication) .
- A personal access token

Refer to the [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/developers/apps/differences-between-github-apps-and-oauth-apps) for more information.

We recommend that you create GitHub Apps for access control. GitHub Apps don't assume any user's identity, which provides clear insight into your recipes' activity.

> **GITHUB APPS CONNECTION**
> 
> Each GitHub App connection links to a specific installation in an organization or user account.

## OAuth authentication

Complete the following steps to connect your GitHub to Workato using OAuth authentication:

1. Sign in to your Workato account and go to the project where you plan to add your GitHub connection.
   
2. Click **Create > Connection** (or press C twice), then select **GitHub** as your connection.
   
3. Provide a **Connection name** that identifies which GitHub instance Workato is connected to.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu and select **OAuth App**.
   
6. Optional. Click **Advanced configuration** to display the **Host name** field.
   
7. Optional. Enter a **Host name**. This is applicable when using Github Enterprise Server. Enter your Github subdomain. For example, if your host URL is `https://github.example-organisation.com`, the subdomain is `github.example-organisation.com`.
   
8. Click **Connect**. Workato redirects you to GitHub. The OAuth App requests authorization to access your GitHub account.
   

## GitHub App authentication

You must first [register the app](#register-your-github-app) in your GitHub account and retrieve its credentials to connect to GitHub using a GitHub App. Use this information to [configure the connection](#setup) in Workato.

![GitHub app auth](/assets/github-app-view.CmRUHryh.png)_Select Authentication type as GitHub app and collect details from your GitHub App!_

### Register your GitHub App

Complete the following steps to register your GitHub App and retrieve the credentials required to connect it to Workato:

1. Complete the [steps](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) in the GitHub documentation to register your GitHub App.
   
2. Retrieve your **GitHub App ID** in the **General** settings page of your GitHub app.
   
   ![app id](/assets/github-app-app-id.hjpO7iTw.png)_Save this App ID and place it into your connection_
   
3. Generate a **Private key** on the same page. GitHub automatically downloads this `.pem` file to your machine.
   
   ![Generate private key](/assets/github-app-private-key.Dqjm0LL8.png)_Generate the private key_
   
4. Open the `.pem` file in a text editor. The file should look similar to the following:
   
   ```
   -----BEGIN RSA PRIVATE KEY-----
   MIIEpAIBAAKCAQEAyL/wuiSaWoH0pyf366G5E7dbzzmON1qMMrWvls8RtZtgOLjb
   FBxj6gO2aUfoGbMCMqOYRV6xCn6tK118sGYMd5U/kCFu3IRPr/2GoEtcrf0TecQG
   ON+27ijH0Vpn62o8NzGejdy0AWujrtAl6F8xGZeze0PzrGvW6h/GnAdZO1gJnp8t
   wmEqEMXqAsPOQ0hkY+r+pE8RKQVsJCe+PIanBKp7RKWDi9usPFZQdQ==
   -----END RSA PRIVATE KEY-----
   ```
   
5. Copy the entire private key, including the `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----`. Use this private key when you set up the connection in Workato.
   
6. Retrieve your **Installation ID** from the organization or user where you installed your GitHub App:
   
   - Users accounts: Go to **Settings > Applications > Your GitHub App > Configure**.
   - Organizations: Go to your organization's GitHub homepage. Click **Settings > Installed GitHub Apps > Configure**.
   
   The installation ID appears in the URL. For example, if the URL is `https://github.com/settings/installations/13876669`, the installation ID is `13876669`.
   
7. Save the installation ID. Enter this ID when creating the GitHub App connection in Workato.
   

Next, complete the setup in Workato.

### Complete setup in Workato

Complete the following steps to finish setting up the GitHub App connection:

1. Sign in to your Workato account and go to the project where you plan to add your GitHub connection.
   
2. Click **Create > Connection** (or press C twice), then select **GitHub** as your connection.
   
3. Provide a **Connection name** that identifies which GitHub instance Workato is connected to.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu and select **GitHub App**.
   
6. Enter your **GitHub App ID**.
   
7. Enter your **Github App Private key**.
   
8. Enter your **Installation ID**.
   
9. Optional. Click **Advanced configuration** to display the **Host name** field.
   
10. Optional. Enter a **Host name** if using GitHub Enterprise Server. Use your GitHub subdomain. For example, if your host URL is `https://github.example-organisation.com`, the subdomain is `github.example-organisation.com`.
    
11. Optional. Enter a **Custom OAuth profile**. This selection ensures that all requests to the app use the specified profile.
    
12. Click **Connect**.
    

## Personal access token authentication

Retrieve your personal access token from GitHub to connect your GitHub account to Workato using a personal access token:

### Retrieve personal access token

1. Go to **Github account > Settings > Developer settings > Personal access tokens > Generate new token**.
   
2. Click **Generate new token**.
   
3. Copy the token. Enter this token in Workato to authenticate the connection.
   

### Complete setup in Workato

Complete the following steps to set up your GitHub connection using a personal access token:

1. Sign in to your Workato account and go to the project where you plan to add your GitHub connection.
   
2. Click **Create > Connection** (or press C twice), then select **GitHub** as your connection.
   
3. Provide a **Connection name** that identifies which GitHub instance Workato is connected to.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu and select **Personal Access Token**.
   
6. Optional. Click **Advanced configuration** to display the **Host name** field.
   
7. Optional. Enter a **Host name**. This is applicable when using Github Enterprise Server. Enter your Github subdomain. For example, if your host URL is `https://github.example-organisation.com`, your subdomain is `github.example-organisation.com`.
   
8. Enter your **Personal Access Token**.
   
9. Optional. Enter a **Custom OAuth profile**. This ensures all requests to the app use the specified profile.
   
10. Click **Connect**.

---
