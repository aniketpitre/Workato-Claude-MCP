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
