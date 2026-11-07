---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-project-level-azure-key-vault.md
description: >-
  Set up Azure Key Vault for project-level secrets management to scope
  connection credentials to individual Workato projects.
---

# Set up Azure Key Vault for project-level secrets management

Switching to project-specific secrets management causes external secrets references scoped to the workspace level to stop working.

## Prerequisites

To complete the steps in this guide, you must have the following:

- An existing [key vault](https://azure.microsoft.com/en-us/products/key-vault/).
- A [registered application](/en/security/data-protection/secrets-management/azure-key-vault-app-registration) with an appropriate role policy assigned:
  - For key vaults using [role-based access control (RBAC)](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide?tabs=azure-cli), the registered app must have the **Key Vault Secrets User** role.
  - For key vaults using [access policies](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal), the registered app must have the **Get** secret permission.

> **REGISTERING AN APPLICATION**
> 
> To learn how to register an application, see [Registering an application with Microsoft Entra ID](/en/security/data-protection/secrets-management/azure-key-vault-app-registration).

## Select the scope for secrets management

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > External secrets manager**.
   
3. Click the **Use external secrets manager** toggle.
   
4. Select the **Set up secrets management for each project individually** option from the **Scope** drop-down menu.
   
   ![Set up secrets management for each project individually](/assets/secrets-management-scope-project.d-05a3me.png)_Set up secrets management for each project individually_
   
5. Click **Save**.
   
6. If you switch secrets management scopes, Workato notifies you that existing external secret references scoped to the project level will no longer function.
   
   To proceed with switching from workspace-level to project-level secrets management, select the checkbox to acknowledge the impact and click **Use project-specific secrets**.
   
   ![Use project-specific secrets](/assets/azure-key-vault-use-project-specific-secrets.g38BqQ-T.png)_Use project-specific secrets_
   

## Select the project

1. In Workato, navigate to your projects.
   
2. Select the project that you plan to configure with secrets management.
   
3. In the project, go to **Workspace admin > Settings > External secrets manager**.
   
4. In the **Which secrets manager do you want to use?** field, select **Azure Key Vault**.
   
   ![Secrets management interface of a project](/assets/azure-key-vault-select-akv-projects.B-0kimKE.png)_Secrets management interface of a project_
   
5. Click **Set up connection**.
   
6. In the **Connect to Azure Key Vault** modal, select **\+ Create a new connection**.
   
   ![Create a new Azure Key Vault connection](/assets/azure-key-vault-select-connection.DE_prRmn.png)_Create a new Azure Key Vault connection_
   

## Connect to Azure Key Vault

![Configure Azure Key Vault connection](/assets/azure-key-vault-connect.Dlx1jFQ0.png)_Configure Azure Key Vault connection_

1. - Connection name
   - Name your Azure Key Vault connection.
2. - Location
   - Select the project or folder to store your Azure Key Vault connection.
3. - Connection type
   - Specify whether this is a cloud or [on-prem connection](/en/on-prem/agents/connection). If you're connecting to an on-prem Azure Key Vault instance, select the appropriate on-prem group from the drop-down menu.
4. - Vault URL
   - Provide the URL of your key vault. Obtain this value by navigating to [**Azure portal > Key vaults**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.KeyVault%2Fvaults). Select the desired key vault and copy the **Vault URI** shown in the **Overview**. In our example, we connect to the vault URL `https://example.vault.azure.net/`.
5. - Tenant ID
   - Provide the ID of the tenant where your key vault and app registration are located. Azure refers to this as the **Directory (tenant) ID**. Obtain this value by navigating to [**Azure portal > App registrations**](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps). Select your [registered application](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#step-1) and copy the **Directory (tenant) ID** shown in the **Overview**.
6. - Client ID
   - Provide your client ID, which Azure refers to as the **Application (client) ID**. Obtain this value by navigating to [**Azure portal > App registrations**](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps). Select your [registered application](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#step-1) and copy the **Application (client) ID** shown in the **Overview**.
7. - Client Secret
   - Provide your client secret, which Azure refers to as the secret **Value**. Azure only displays this value when the secret is generated. If you need to generate a new secret, see [Registering an application with Microsoft Entra ID, Step 2](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#step-2).
8. Click **Connect**. Workato displays the name of the Azure Key Vault connection:
   
   ![Connection successful](/assets/azure-key-vault-projects-connected.DowFQuP8.png)_Connection successful_
   
9. Click **Save changes**.
   

> **FURTHER READING**
> 
> - [Using Azure Key Vault secrets to authenticate to connections](/en/security/data-protection/secrets-management/using-azure-key-vault-in-connections)
