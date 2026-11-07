---
url: >-
  https://docs.workato.com/en/on-prem/agents/secrets-manager/microsoft-azure-key-vault.md
description: >-
  Configure Microsoft Azure Key Vault with the Workato on-prem agent to securely
  store and access secrets for cloud and connection profiles.
---

# Configuring Microsoft Azure Key Vault for on-prem agent

[Microsoft Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/) is a service that enables you to securely store and access secrets in the cloud. Workato supports Azure Key Vault for managing secrets for on-prem systems.

## Azure Key Vault support for OPA connection types

Azure Key Vault supports both [cloud profiles](/en/on-prem/agents/connection/cloud) and [connection profiles](/en/on-prem/agents/connection/profile), though the process of connecting to and using Azure Key Vault is different for each, as summarized in the following table:

| On-prem system connection type | Azure Key Vault setup | Azure Key Vault secret syntax |
| --- | --- | --- |
| [Cloud profile](#akv-cloud-profiles) **(recommended)** | Azure Key Vault connector in Workato | `{{workato:sm:<secret_name>}}` |
| [Connection profile](#akv-connection-profiles) | `secrets` section in `config.yml` | `{ secret: '<secret_name>' }` |

Configure and use Azure Key Vault according to the connection type of the on-prem system whose secrets are stored in Key Vault:

- [Using Azure Key Vault with on-prem systems configured as cloud profiles](#akv-cloud-profiles)
- [Using Azure Key Vault with on-prem systems configured as connection profiles](#akv-connection-profiles)

> **CONNECTION TYPES**
> 
> - [Cloud profiles](/en/on-prem/agents/connection/cloud) are set up directly in Workato, so you don't need to access the machine where the on-prem agent is installed.
> - [Connection profiles](/en/on-prem/agents/connection/profile) are set up manually in a `config.yml` file on the machine where the on-prem agent is installed.

## Using Azure Key Vault with cloud profiles

To set up and use Azure Key Vault to store credentials for an on-prem system configured as a [cloud profile](/en/on-prem/agents/connection/cloud), complete the following steps:

1. [Register an application with Microsoft Entra ID](/en/security/data-protection/secrets-management/azure-key-vault-app-registration). This enables Workato to retrieve secrets from Key Vault.
2. Set up Azure Key Vault for either [workspace-level secrets management](/en/security/data-protection/secrets-management/setting-up-workspace-level-azure-key-vault) or [project-specific secrets management](/en/security/data-protection/secrets-management/setting-up-project-level-azure-key-vault).
3. [Use Azure Key Vault secrets in connections](/en/security/data-protection/secrets-management/using-azure-key-vault-in-connections). In the **Connection type** field of the connection setup, select the name of the on-prem group that you set up as a [cloud profile](/en/on-prem/agents/connection#cloud-profile) (meaning directly in Workato).

## Using Azure Key Vault with connection profiles

In this guide, we'll show you how to use [Microsoft Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/secrets/about-secrets) with Workato's [on-prem agent (OPA)](/en/on-prem/agents) to store credentials for a database that is configured as a [connection profile](/en/on-prem/agents/connection/profile).

**Note**: We're focusing on using secrets to encrypt **passwords** in this tutorial, but secrets can be used to encrypt any connection value. This includes usernames, database names, and so on.

* * *

> **LEGACY CONNECTION CONFIGURATION**
> 
> Setting up Azure Key Vault with a `config.yml` file is a legacy connection configuration that will eventually be deprecated. We encourage you to migrate your connection profiles to cloud profiles, so you can set up Azure Key Vault using the connector directly in Workato.

### Prerequisites

To configure Azure Key Vault to work with OPA, you'll need:

- **The On-prem groups privilege in Workato.**
- **The following in Azure:**
  - **Permissions that allow you to:**
    - Create secrets
    - [Register and assign roles to applications](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#permissions-required-for-registering-an-app)
  - **An existing key vault**. Creating a key vault is outside the scope of this tutorial, but you can use [this Azure guide](https://docs.microsoft.com/en-us/azure/key-vault/general/quick-create-portal#create-a-vault) to create one.
  - **An existing service principal with read access to resources**. The Workato OPA uses [environment variables](https://docs.microsoft.com/en-us/java/api/overview/azure/identity-readme?view=azure-java-stable#environment-variables) to provide credentials in requests to Azure. Use [this Azure guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) to create a service principal with read access to your key vault.

> **Azure credentials encryption**
> 
> From on-prem agent version [2.14.0](/en/on-prem/agents/versions#v2-14) or later you can set your `AZURE_CLIENT_ID`, `AZURE_TENANT_ID` and `AZURE_CLIENT_SECRET` directly in the config.yml file instead of setting it as an environment variables. Additionally those values can be protected by using built in [encryptor](/en/on-prem/agents/password-encryption).  
>   
> In the example below only the `AZURE_CLIENT_SECRET` is encrypted:
> 
> ```yaml
> secrets:
>   provider: azure
>   vault: WorkatoSDKeyVault
>   tenant: <tenant-id>
>   clientId: <client-id>
>   clientSecret: {encrypted: 'RCVtuGPjJWNqwkFQvhT...'}
> ```

* * *

### Step 1: Create The Secret In Azure

1. Sign into the [Azure portal](https://portal.azure.com/).
   
2. Navigate to [Azure Key Vault](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.KeyVault%2Fvaults).
   
3. Open the key vault where you want to create the secret. In this example, the vault is `WorkatoSDKeyVault`.
   
4. In the left navigation pane, click **Settings > Secrets**.
   
5. On the **Secrets** page, click **\+ Generate/Import**:
   
   ![The + Generate/Import option in the Azure portal](/assets/key-vault-settings.e9QMJ9wH.png)
   
6. In the **Create a secret window** that displays, fill in the following:
   
   - **Upload options**: Select `Manual`
     
   - **Name**: Enter a name for the secret. For example: `sales-db-password`
     
     This name will be used as the `password` in the OPA config file to retrieve the secret and its `value`.
     
   - **Value**: Enter the value for the secret. This should be an actual password.
     
   - **Enabled**: If it isn't already, set this field to `Yes`
     
   
   The window should look similar to the following:
   
   ![Fully configured Create a secret window in the Azure portal](/assets/create-a-secret.Cfq1mhUJ.png)
   
7. When finished, click **Create**.
   

* * *

### Step 2: Configure The OPA Config File

In this step, you'll add info about the key vault you created to your OPA configuration file.

1. In your [OPA config file](/en/on-prem/agents/connection/profile), add a `secrets` section with `provider` and `vault` keys:
   
   ```yaml
   secrets:
     provider: azure
     vault: <VAULT_NAME>
   ```
   
2. For `provider`, enter `azure`.
   
3. Next, you'll define the `vault`. Workato supports the ability to specify multiple vaults in an OPA config file:
   
   - **To define a default vault**, enter the name of a vault for `vault`. If provided, the vault will be used for all secrets defined in the config file.
     
     In the following example, we've enter the name of the vault from [Step 1](#create-secret). In our case, this is `WorkatoSDKeyVault`:
     
     ```yaml
     secrets:
       provider: azure
       vault: WorkatoSDKeyVault
     ```
     
   - **To override the default or define a vault at the secret level,** use `{ secret: '<SECRET_NAME>', vault: '<VAULT>'}` in the database's connection profile. Refer to the [next section](#configure-database-profile) for an example.
     
4. Save the file.
   

* * *

### Step 3: Configure The Database Profile

To wrap things up, you'll specify which secret to use in the database's profile.

1. In the config file, navigate to the [database's profile](/en/on-prem/agents/connection/profile#database-profile).
   
2. **To use the [default vault](#configure-opa-file)**, use `{ secret: '<SECRET_NAME>' }` in the `password` key to specify the secret. The `<SECRET_NAME>` must match the name of the secret you created in [Step 1](#create-secret):
   
   ```yaml
   database:
     sales_database:
       adapter: sqlserver
       host: localhost
       port: 1433
       database: test
       username: sales_user
       password: { secret: 'sales-db-password-password' }
   ```
   
   **If using a vault other than the default**, use `{ secret: '<SECRET_NAME>', vault: '<VAULT>' }` in the `password` key to provide an override:
   
   ```yaml
   database:
     sales_database:
       adapter: sqlserver
       host: localhost
       port: 1433
       database: test
       username: sales_user
       password: { secret: 'sales-db-password-password', vault: 'other-vault' }
   ```
   
3. Save the file.
