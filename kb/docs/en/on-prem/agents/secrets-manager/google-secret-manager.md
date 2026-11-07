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
