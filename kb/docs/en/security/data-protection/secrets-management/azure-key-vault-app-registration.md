---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/azure-key-vault-app-registration.md
description: >-
  Register an application in the Microsoft Entra admin center so Workato can
  retrieve secrets from your Azure Key Vault on your behalf.
---

# Register an Azure Key Vault app in Microsoft Entra ID

Before you can connect your [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/) to Workato, you must [register an application](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application) in the Microsoft Entra admin center.

Registering this [application](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals?tabs=browser#application-registration) and giving it the appropriate permissions enables Workato to retrieve secrets from your key vault on your behalf.

To register the application, complete the following steps:

1. [Create the app registration](#step-1)
2. [Create the client secret](#step-2)
3. [Grant permissions to the app](#step-3)

> **HAVE AN EXISTING SAML-BASED APPLICATION?**
> 
> If you have already registered a [SAML-based application](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/add-application-portal-setup-sso) that lets your users sign in to Workato with SAML SSO, you can use it to set up Workato's [Azure Key Vault connection](/en/security/data-protection/secrets-management/setting-up-project-level-azure-key-vault). When you configure the connector, simply enter your existing app's client ID and [generate a new secret](#step-2). Make sure the application also has the [required permissions](#step-3).

## Create the app registration

1. Sign in to the Azure portal and go to [App registrations](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps).
   
2. Select **\+ New registration**.
   
3. Name your application. This is the user-facing display name for this application, such as `workato-akv`. Microsoft allows you to change this name later.
   
4. In **Supported account types**, select **Accounts in this organizational directory only (Default Directory only - Single tenant)**.
   
5. Leave the **Redirect URI** field blank and select the **Register** button.
   
6. The next page displays an overview of the newly created app. Copy and store the **Application (client) ID** and the **Directory (tenant) ID**. You will need these values later to authenticate in Workato.
   
   ![App registration overview](/assets/azure-key-vault-app-registration-overview.CsUtBIaR.png)_App registration overview_
   

## Create the client secret

1. From the overview of your app registration, select **Certificates & secrets** in the left navigation sidebar.
   
2. On the **Client secrets** tab, select **\+ New client secret**.
   
3. In the **Description** field, enter a description for the client secret, such as `workatoAzureKeyVault`.
   
4. In the **Expires** field, select when the secret should expire. The default is after 180 days.
   
5. Select **Add**.
   
6. The Azure portal displays the new secret value and ID. Copy the **Value**.
   
   > **WARNING**
   > 
   > The secret value is only shown once. Make sure you copy it before leaving the page.
   
   ![Copy the secret value](/assets/azure-key-vault-copy-secret-value.Deh-MX9U.png)_Copy the secret value_
   

## Grant permissions to the app

Next, you must give the registered app permission to retrieve secrets from your key vault on Workato's behalf.

Azure offers two ways to grant permission to access key vaults:

- [Role-based access control (RBAC)](#rbac)
- [Access policies](#access-policy)

To see which model your key vault uses, navigate to **Key vaults > {key vault name} > Access configuration**.

### RBAC

If your key vault uses the [RBAC permission model](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide?tabs=azure-cli), you must assign the **Key Vault Secrets User** role to the registered application.

1. Navigate to **Key vaults > {key vault name} > Access control (IAM)**.
   
2. Select **Add > Add role assignment**.
   
3. Select the **Key Vault Secrets User** role and select **Next**.
   
4. In the **Assign access to** field, select **User, group, or service principal**.
   
5. In the **Members** field, choose **Select members** and search for the name of your registered application. When the application appears in the list, click the application name and choose **Select**.
   
6. Select **Next**.
   
7. In the **Review + assign** tab, select **Review and assign**.
   

### Access policy

If your key vault uses the [access policy permission model](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal), you must assign the **Get** secret permission to the registered application.

1. Navigate to **Key vaults > {key vault name} > Access policies**.
   
2. Select **Create**.
   
3. In the **Permissions** tab, select **Get** in the **Secret permissions** column, then select **Next**.
   
4. In the **Principal** tab, search for the name of the registered app. When the application appears in the list, select the application name and then select **Next**.
   
5. In the **Application (optional)** tab, select **Next**.
   
6. In the **Review + create** tab, select **Create**.
   

> **FURTHER READING**
> 
> - [Set up Azure Key Vault for workspaces](/en/security/data-protection/secrets-management/setting-up-workspace-level-azure-key-vault)
> - [Set up Azure Key Vault for projects](/en/security/data-protection/secrets-management/setting-up-project-level-azure-key-vault)
