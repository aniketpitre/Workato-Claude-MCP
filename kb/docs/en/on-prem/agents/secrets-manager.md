---
url: 'https://docs.workato.com/en/on-prem/agents/secrets-manager.md'
description: >-
  Use an external secrets manager with the Workato on-prem agent to manage
  passwords without storing them in config files.
---

# On-prem agent - Secrets Manager

To simplify password management, use an external secrets manager with Workato's [on-prem agent (OPA)](/en/on-prem/agents).

This approach eliminates the need to store passwords in OPA config files, allowing you to rotate your passwords without re-configuring OPA.

* * *

## Connection types

The [on-prem connection type](/en/on-prem/agents/connection) determines which secrets managers are supported. Both connection types let you use OPA to connect your secrets manager to Workato from behind a corporate firewall.

- [Cloud profiles](/en/on-prem/agents/connection/cloud) support AWS Secrets Manager, Microsoft Azure Key Vault, and HashiCorp Vault. Cloud profiles are set up directly in Workato, so you don't need to access the machine where the on-prem agent is installed.
- [Connection profiles](/en/on-prem/agents/connection/profile) support AWS Secrets Manager, Microsoft Azure Key Vault, and Google Secret Manager. Connection profiles are set up manually in a config file on the machine where the on-prem agent is installed.

> **CLOUD CONNECTION**
> 
> If you want to connect a secrets manager but aren't using an on-prem agent, see [Secrets management for connection credentials](/en/security/data-protection/secrets-management/secrets-management).

* * *

## How it works

At a high level, here's how using a secrets manager works with OPA:

1. You create a vault and secret in your external secrets manager.
   
2. Configure Workato to use the secrets manager.
   
   - **For cloud profiles:** Set up a connection for the secrets manager you're using. If you're using HashiCorp Vault, you must also set the **Connection type** to your on-prem group instead of _Cloud_.
   - **For connection profiles:** Define the secrets manager in the config file on the machine where the on-prem agent is installed.
3. Specify the secret to retrieve from the secrets manager.
   
   - **For cloud profiles:** Specify the secret in the configuration page for the connection.
   - **For connection profiles:** Specify the secret in the appropriate [system profile](/en/on-prem/agents/connection/profile#system-types).
4. When fully configured, OPA retrieves the secret from the defined secrets manager.
   

* * *

## Supported secret managers

The table below lists the secret managers Workato currently supports for use with OPA. In the table, you'll find:

- **Name**: The name of the secrets manager and a link to a setup guide
- **Provider Value**: The `provider` value of the secrets manager, used in the [OPA config file](/en/on-prem/agents/connection/profile) (if applicable)
- **Profile**: The [on-prem connection type](/en/on-prem/agents/connection) ([cloud profile](/en/on-prem/agents/connection/cloud) or [connection profile](/en/on-prem/agents/connection/profile))

| Name | Provider Value | Profile |
| --- | --- | --- |
| [Amazon Web Services Secrets Manager](/en/on-prem/agents/secrets-manager/amazon-web-services-secret-manager) | `aws` | Cloud profile and connection profile |
| [Google Secret Manager](/en/on-prem/agents/secrets-manager/google-secret-manager) | `google` | Connection profile |
| [HashiCorp Vault](/en/on-prem/agents/secrets-manager/hashicorp-vault) | n/a | Cloud profile |
| [Microsoft Azure Key Vault](/en/on-prem/agents/secrets-manager/microsoft-azure-key-vault) | `azure` | Cloud profile and connection profile |

---

---
url: >-
  https://docs.workato.com/en/on-prem/agents/secrets-manager/amazon-web-services-secret-manager.md
description: >-
  Configure AWS Secrets Manager with the Workato on-prem agent to store secrets
  using cloud profiles or connection profiles.
---

# Configuring AWS Secrets Manager for on-prem agent

[Amazon Web Services (AWS) Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/asm_access.html) is a service that enables you to securely store and access secrets in the cloud. Workato supports AWS Secrets Manager for managing secrets for on-prem systems.

## AWS Secrets Manager support for OPA connection types

AWS Secrets Manager supports both [cloud profiles](/en/on-prem/agents/connection/cloud) and [connection profiles](/en/on-prem/agents/connection/profile), though the process of connecting to and using AWS Secrets Manager is different for each, as summarized in the following table:

| On-prem system connection type | AWS Secrets Manager setup | AWS Secrets Manager secret syntax |
| --- | --- | --- |
| [Cloud profile](#aws-cloud-profiles) **(recommended)** | AWS Secrets Manager setting in Workato | `{{workato:sm:<key_name>:<secret_ARN>}}` |
| [Connection profile](#aws-connection-profiles) | `secrets` section in `config.yml` | `{ secret: '<secret_name>' }` |

Configure and use AWS Secrets Manager according to the connection type of the on-prem system whose secrets are stored in Secrets Manager:

- [Using AWS Secrets Manager with on-prem systems configured as cloud profiles](#aws-cloud-profiles)
- [Using AWS Secrets Manager with on-prem systems configured as connection profiles](#aws-connection-profiles)

> **CONNECTION TYPES**
> 
> - [Cloud profiles](/en/on-prem/agents/connection/cloud) are set up directly in Workato, so you don't need to access the machine where the on-prem agent is installed.
> - [Connection profiles](/en/on-prem/agents/connection/profile) are set up manually in a `config.yml` file on the machine where the on-prem agent is installed.

## Using AWS Secrets Manager with cloud profiles

To set up and use AWS Secrets Manager to store credentials for an on-prem system configured as a [cloud profile](/en/on-prem/agents/connection/cloud), complete the following steps:

1. Set up AWS Secrets Manager for either [workspace-level secrets management](/en/security/data-protection/secrets-management/setting-up-workspace-level-aws-secrets-manager) or [project-specific secrets management](/en/security/data-protection/secrets-management/setting-up-project-level-aws-secrets-manager).
2. [Use AWS Secrets Manager secrets in connections](/en/security/data-protection/secrets-management/using-aws-secrets-in-connections). In the **Connection type** field of the connection setup, select the name of the on-prem group that you set up as a [cloud profile](/en/on-prem/agents/connection#cloud-profile) (meaning directly in Workato).

## Using AWS Secrets Manager with connection profiles

In this guide, we'll show you how to use [Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/asm_access.html) with Workato's [on-prem agent (OPA)](/en/on-prem/agents) to store credentials for a database that is configured as a [connection profile](/en/on-prem/agents/connection/profile).

When configured, OPA uses the [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html) to authenticate its requests to AWS, eliminating the need to store credentials in your OPA config file. See [Amazon Web Services (AWS) Secrets Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-aws-secrets-manager).

Alternatively, you can choose to manage access at the project level, changing secrets manager settings so that connections in the project can use the specified role in the project settings. So, customers can create project-specific IAM roles to limit the use of secrets to connections within the project. See [Amazon Web Services (AWS) Secrets Manager for projects](/en/security/data-protection/secrets-management/setting-up-project-level-aws-secrets-manager).

* * *

> **LEGACY CONNECTION CONFIGURATION**
> 
> Setting up AWS Secrets Manager with a `config.yml` file is a legacy connection configuration that will eventually be deprecated. We encourage you to migrate your connection profiles to cloud profiles, so you can set up AWS Secrets Manager directly in Workato.

### Prerequisites

To configure AWS Secrets Manager to work with OPA, you'll need:

- **The On-prem groups privilege in Workato.**
- **The following in AWS**:
  - **Permissions that allow you to:**
    - [Create and manage secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_available-policies.html)
    - Create and manage IAM access keys
  - **An existing IAM access key stored as an environment variable.** Workato uses the [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html) to authenticate requests to AWS. Creating an IAM access key and storing it is outside the scope of this tutorial, but you can use these AWS guides to complete this prerequisite:
    - [Create an IAM access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)
    - [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html)

* * *

### Step 1: Create the Secret in AWS

1. Log in to your AWS console.
   
2. Use the **search bar** at the top of the page to open the [AWS Secrets Manager](https://console.aws.amazon.com/secretsmanager/home).
   
3. Click the **Store a new secret** button.
   
4. On the **Step 1 - Choose secret type** page:
   
   1. In the **Secret type** section, click **Other type of secret**.
      
   2. In the **Key/value pairs** section, click the **Plaintext** option.
      
   3. In the **Plaintext** field, enter the password. OPA will retrieve this value and pass it as-is.
      
      Your configuration should look like the following:
      
      ![Configured Secret Type page in AWS Secrets Manager](/assets/secret-type.DWB6gzXG.png)_Configured Secret Type page in AWS Secrets Manager_
      
   4. Click **Next**.
      
5. On the **Step 2 - Configure secret** page:
   
   1. Fill in the following fields:
      
      - **Secret name**: Enter a name for the secret. You'll add this value to your OPA config file in the next section, which will allow OPA to retrieve the correct password.
      - **Description (optional)**: Enter a brief description of the secret.
      
      ![Configure Secret page in AWS Secrets Manager](/assets/configure-secret.BBLGkOEP.png)_Configure Secret page in AWS Secrets Manager_
      
   2. When finished, click **Next**.
      
6. **Optional**: On the **Step 3 - Configure rotation** page, configure rotation for the secret if desired. When finished, click **Next**.
   
7. On the **Step 4 - Review** page:
   
   1. Review the secret's details.
      
   2. If everything looks fine, click **Store** to create and store the secret.
      

* * *

### Step 2: Configure the OPA Config File

In this step, you'll add info about your secrets manager to your OPA configuration file.

> **NO CREDENTIALS NEEDED**
> 
> When configured, OPA will use the [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html) to authenticate its requests to AWS. This eliminates the need to store your credentials - either those for AWS Secrets Manager or a database - in your OPA config file.

1. In your [OPA config file](/en/on-prem/agents/connection/profile), add a `secrets` section with `provider` and `region` keys:
   
   ```yaml
   secrets:
     provider: aws
     region: <YOUR_REGION>
   ```
   
2. For `provider`, enter `aws`.
   
3. For `region`, enter the region your AWS instance is in:
   
   ```yaml
   secrets:
     provider: aws
     region: us-east-1
   ```
   
   You can find this info in your AWS console by clicking the **region menu** at the top of the page, located next to the user menu:
   
   ![Configure Secret page in AWS Secrets Manager](/assets/aws-region-menu.CcHGuN-8.gif)_Configure Secret page in AWS Secrets Manager_
   
   In this example, the region is `us-east-1`.
   
4. Save the file.
   

* * *

### Step 3: Configure the Database Profile

To wrap things up, you'll specify which secret to use in the database's profile.

1. In the config file, navigate to the [database's profile](/en/on-prem/agents/connection/profile#database-profile).
   
2. In the `password` key, use `{ secret: '<SECRET_NAME>'}` to specify the secret. The `<SECRET_NAME>` must match the name of the secret you created in [Step 1](#create-secret):
   
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
   
3. Save the file.

---

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

---

---
url: >-
  https://docs.workato.com/en/on-prem/agents/secrets-manager/google-secret-manager.md
description: >-
  Configure Google Secret Manager with the Workato on-prem agent to store
  database credentials for cloud profiles and connection profiles.
---

# Configuring Google Secret Manager for on-prem agent

In this guide, we demonstrate how to use [Google Secret Manager](https://cloud.google.com/secret-manager/docs) with Workato's [on-prem agent (OPA)](/en/on-prem/agents) to store database credentials.

## Google Secret Manager support for OPA connection types

Google Secret Manager supports both [cloud profiles](/en/on-prem/agents/connection/cloud) and [connection profiles](/en/on-prem/agents/connection/profile), with a different setup process for each:

| On-prem system connection type | Google Secret Manager setup | Secret reference |
| --- | --- | --- |
| [Cloud profile](#gsm-cloud-profiles) **(recommended)** | Google Secret Manager connector in Workato | Enter the secret name as defined in Google Secret Manager |
| [Connection profile](#gsm-connection-profiles) | `secrets` section in `config.yml` | `{ secret: '<secret_name>' }` |

> **CONNECTION TYPES**
> 
> - [Cloud profiles](/en/on-prem/agents/connection/cloud) are set up directly in Workato, so you don't need to access the machine where the on-prem agent is installed.
> - [Connection profiles](/en/on-prem/agents/connection/profile) are set up manually in a `config.yml` file on the machine where the on-prem agent is installed.

## Using Google Secret Manager with cloud profiles

Complete the following steps to set up and use Google Secret Manager to store credentials for an on-prem system configured as a [cloud profile](/en/on-prem/agents/connection/cloud):

1. [Set up a Google Cloud service account](/en/security/data-protection/secrets-management/google-service-account-setup). This enables Workato to retrieve secrets from Secret Manager.
   
2. Set up Google Secret Manager at the [workspace level](/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager) or [project level](/en/security/data-protection/secrets-management/setting-up-project-level-google-secret-manager). Select the name of the on-prem group that you set up as a [cloud profile](/en/on-prem/agents/connection#cloud-profile) in the **Connection type** field of the connection setup.
   
3. [Use Google Secret Manager secrets in connections](/en/security/data-protection/secrets-management/using-google-secret-manager-in-connections).
   

## Using Google Secret Manager with connection profiles

**Note**: In this tutorial, the focus in on using secrets to encrypt **passwords**. However, you can use secrets to encrypt any connection value, including usernames, database names, and so on.

* * *

### Prerequisites

To configure Google Secret Manager to work with OPA, you must have:

- **The On-prem groups privilege in Workato**
- **Privilege to set environment variable**
- **The permissions in Google Secret Manager to:**
  - Create secrets
  - [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts)

* * *

### Step 1: Create the secret in Google

1. Sign into the [Google Secret Manager](https://console.cloud.google.com/security/secret-manager).
   
2. Click `+ CREATE SECRET`
   
   ![Create secret](/assets/create-secret-1.BvXTg-W0.png)
   
3. Assign a name to the secret; this name is used in your OPA config file to look up the correct password. In this example, the name is `workato-sqlserver-password`.
   
   ![Secret created](/assets/create-secret-2.BNhF8Gup.png)
   
4. After creating the secret, note the project, secret name, and version. Use these to format the [Secret Version](https://cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#SecretVersion) and place it inside the OPA.
   
   In this example:
   
   - the project is `558965260687`,
   - secret name is `workato-sqlserver-password`,
   - version is `1`.
   
   That means that the composite value used in the OPA config file is `projects/558965260687/secrets/workato-sqlserver-password/versions/1`
   
   ![Secret version](/assets/secret-version.B-Pz7d6m.png)
   
   > **Using latest version for secret**
   > 
   > `projects/558965260687/secrets/workato-sqlserver-password/versions/latest` can also be used to reference the latest version of the secret.
   

* * *

### Step 2: Configure the OPA config file and connection to Google Secret Manager

Here, add the information about the secret provider to OPA configuration file, and set up the Google Secret Manager connection.

1. In your [OPA config file](/en/on-prem/agents/connection/profile), add a `secrets` section with `provider` key:
   
   ```yaml
   secrets:
     provider: google
   ```
   
2. For `provider`, enter `google`.
   
3. Save the file.
   

> **Storing Google connection credentials**
> 
> You do not have to store your Google connection credentials in the OPA config file. The OPA uses Application Default Credentials to authenticate its requests to Google. Create a [service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts) with read access to your secrets, and store the service account key in your [environment variable](https://cloud.google.com/docs/authentication/production#automatically).

* * *

### Step 3: Configure The Database Profile

To wrap things up, specify which secret to use in the database profile.

1. In the config file, navigate to the [database profile](/en/on-prem/agents/connection/profile#database-profile).
   
2. In your `password` key, specify the secret value that you created in [Step 1](#create-secret):
   
   ```yaml
   database:
     sql:
       adapter: sqlserver
       host: localhost
       port: 1433
       database: test
       username: db_user
       password: { secret: 'projects/558965260687/secrets/workato_opa_sqlserver_password/versions/latest' }
   ```
   
3. Save the file.

---
