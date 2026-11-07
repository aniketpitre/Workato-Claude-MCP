---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/secrets-management.md
description: >-
  Learn how external secrets management lets Workato store and retrieve
  connection credentials like passwords and API tokens from a secrets manager.
---

# Secrets management for connection credentials

To simplify the management of your connection credentials, you can use an external secrets manager to securely store and retrieve sensitive information like passwords and API tokens.

The External secrets management feature in Workato lets you use secrets in place of hardcoded connection credentials. Centralizing credential management can help you adopt security best practices, like password rotation, without manually updating credentials wherever they're in use.

In this guide, we discuss these topics:

- [How secrets management works](#how-it-works)
- [The secrets managers that Workato supports](#secrets-managers)
- [Using secrets to configure connections](#connection-configuration)
- [Workspace vs. Project level secrets management](#workspace-vs-project-secrets-management)

> **FEATURE AVAILABILITY**
> 
> External secrets management is available on specific pricing plans. Refer to your pricing plan and contract to learn more.

* * *

## How secret management works

With a secrets manager, you can use a **secret** instead of directly entering information into Workato. Secrets contain sensitive info like a password.

When you set up a connection, you need to manually retrieve and enter your credentials. Any time those credentials change - for example, when you reset your password - you'll need to update the password in every application that uses it.

However, if you use an external secrets manager instead, you'll only need to update the password in the secrets manager and refresh the connection in Workato. Applications using the reference will retrieve the secret's updated value, thus minimizing manual work, interruptions, and most importantly, security risk.

> **REFRESH THE CONNECTION IN WORKATO**
> 
> Refresh the connection by sending a request to the Workato API to [clear the secrets management cache](/en/workato-api/environment-management#clear-secrets-management-cache). This updates the connection with the latest credentials in your secrets manager. You do not need to disconnect and reconnect the connection.

At a high level, here's how using a secrets manager works with Workato for connection credential management:

1. You create a vault and secret in your external secrets manager. The secrets manager encrypts the credentials.
   
2. You grant Workato access to the secrets manager.
   
3. In Workato, you configure connections using the secrets instead of credentials.
   
   The following image demonstrates a Jira connection configured with a secret from Amazon Web Services (AWS) Secrets Manager:
   
   ![Jira connection in Workato configured with an AWS secret](/assets/workato-connection-example.CXvKENsX.png)
   
4. When Workato uses the connection, it performs the following tasks, in order:
   
   1. **Request secret**: Workato requests the secret from the secrets manager.
      
   2. **Retrieve and decrypt**: The secrets manager retrieves the secret and returns the decrypted secret value to Workato.
      
   3. **Authentication**: Workato uses the decrypted value to authenticate to the application.
      
   4. **Access**: If authentication is successful, the application grants access to Workato.
      

* * *

## Supported secrets managers

Workato's feature currently supports the following secrets managers:

- [AWS Secrets Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-aws-secrets-manager)
- [Azure Key Vault](/en/security/data-protection/secrets-management/setting-up-workspace-level-azure-key-vault)
- [CyberArk Conjur Secrets Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-cyberark-conjur)
- [Google Secret Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager)
- [HashiCorp Vault](/en/security/data-protection/secrets-management/setting-up-workspace-level-hashicorp-vault-secrets-engine)

* * *

## Using secrets to configure connections

How secrets are used in Workato connections depends on the type of secrets manager you're using. Refer to the guide for your secrets manager for more information:

- [Amazon Web Services (AWS) Secrets Manager](/en/security/data-protection/secrets-management/using-aws-secrets-in-connections)
- [Azure Key Vault](/en/security/data-protection/secrets-management/using-azure-key-vault-in-connections)
- [CyberArk Conjur Secrets Manager](/en/security/data-protection/secrets-management/using-cyberark-conjur-in-connections)
- [Google Secret Manager](/en/security/data-protection/secrets-management/using-google-secret-manager-in-connections)
- [HashiCorp Vault](/en/security/data-protection/secrets-management/using-hashicorp-secrets-in-connections)

* * *

## Workspace vs. Project secrets management

Typically, we configure secrets management for the entire workspace. If your organization requires more granular access control, you can configure it at the level of the individual projects. This enables you to specify the secrets inside the project, so that the connections in the projects can assume the role specified in the project settings.

For example, if your organization is configuring an S3 connection only for the use in your DevOps project, you can create a project-specific IAM role that has access to your S3 connection credentials. This replaces the generic IAM role that can be used by multiple projects.

> **INFO**
> 
> In Workato, secrets management can be used EITHER at the level of the Workspace, or at the level of Projects. We do not support a blended approach. For example, if you implement project-level secrets management for the DevOps project, you must change your secrets management protocol to project-level for ALL projects in the workspace.

* * *

## Formatting secrets

Certain types of secrets must be formatted correctly to be used in Workato. When adding secrets to your secrets manager, ensure you use the correct format.

### X.509 certificate

See the following X.509 certificate for an example of how to format an X.509 certificate in your secrets manager:

```
-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BA\nQEFAASCBKcwggSjAg\nxxxxxxxxxxxxxx\n-----END PRIVATE KEY-----\n
```

* * *

## Troubleshooting secrets manager connections

If you have configured a connection to use a secrets manager but the connection returns a `Permission denied` error, complete the following steps to troubleshoot the connection:

1. [Check credential validity](#step-1-check-credentials)
2. [Test retrieving secrets with provider API](#step-2-retrieve-secret)

### Check validity of credentials

Complete the following steps to check whether the credentials used to connect to your secrets manager are valid:

AWS SECRETS MANAGER

1. Log in to your AWS account.
   
2. Navigate to **IAM > Roles** and select the IAM role you assigned to Workato's Secrets Management feature.
   
3. Select the **Permissions** tab.
   
4. Ensure that the IAM policy attached to the role has the following permissions:
   
   - `ListSecrets`
   - `GetSecretValue`

HASHICORP VAULT

1. Use the [HashiCorp Vault CLI](https://developer.hashicorp.com/vault/docs/commands) to run the following [command](https://developer.hashicorp.com/vault/docs/commands/read) to check the ACL policy attached to the [AppRole](https://developer.hashicorp.com/vault/docs/auth/approle). Substitute your own values for `{approle-name}` and `{role-name}`:
   
   ```
   vault read auth/{approle-name}/role/{role-name}
   ```
   
   For example:
   
   ```
   vault read auth/workato_approle/role/workato
   ```
   
   The CLI output includes the name of the token policy attached to the AppRole.
   
2. Log in to the HashiCorp Vault UI.
   
3. Navigate to **ACL Policies** and select the policy name that the HashiCorp Vault CLI returned.
   
4. Ensure that the selected policy has the `read` and `list` capabilities for the appropriate secrets engine stored in your vault cluster.
   
5. Select the secrets engine in the Vault UI and navigate to the **Configuration** tab.
   
6. Ensure that the engine **Path** matches the `path` in the CLI output.
   

AZURE KEY VAULT

1. Log in to the Azure Portal.
   
2. Navigate to **Key Vault > Access control (IAM) > Role assignments**.
   
3. Ensure that the Service Principal you generated the `clientSecret` for holds the **Key Vault Secrets User** role.
   
4. Navigate to **Microsoft Entra ID > App Registrations** and select the app that you assigned the **Key Vault Secrets User** role to.
   
5. Navigate to **Certificates & Secrets** and ensure that the secret used in your Azure Key Vault connection is not expired.
   

GOOGLE SECRET MANAGER

1. Sign in to the [Google Cloud Console](https://console.cloud.google.com/) and select your project.
   
2. Go to **IAM & Admin > IAM**.
   
3. Locate the service account used by Workato and confirm it has the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) role assigned.
   
4. Go to **IAM & Admin > Service Accounts** and select the service account.
   
5. Open the **Keys** tab and confirm the key used in your Workato connection exists and has not been deleted or disabled.
   

### Test retrieving secrets with provider API

If the permissions you checked in [Step 1](#step-1-check-credentials) are still valid, use an API client such as Postman or curl to make an API call to your secrets manager to retrieve any secret. This should offer more insight about why your secrets manager connection is failing.

To make an API call to your secrets manager, refer to the following documentation:

- [AWS Secrets Manager API operations](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_Operations.html)
- [Azure Key Vault secret operations](https://learn.microsoft.com/en-us/rest/api/keyvault/#secret-operations-key-vault-only)
- [Google Secret Manager API operations](https://cloud.google.com/secret-manager/docs/reference/rest)
- [HashiCorp Vault API operations](https://developer.hashicorp.com/vault/api-docs#api-operations)
