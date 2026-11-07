---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/using-azure-key-vault-in-connections.md
description: >-
  Configure Workato connections using secrets from Azure Key Vault, with
  workspace-level or project-level connections.
---

# Use Azure Key Vault secrets in connections

This guide demonstrates how to use secrets from your [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/) to configure Workato connections.

## Prerequisites

To complete the steps in this guide, you must have the following:

- **In Workato**:
  
  - An account with a successful [workspace-level](/en/security/data-protection/secrets-management/setting-up-workspace-level-azure-key-vault) or [project-level](/en/security/data-protection/secrets-management/setting-up-project-level-azure-key-vault) Azure Key Vault connection.
  - A [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles#project-admin) with **Create** and **Edit Connections** [privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets).
- **In Microsoft Azure**:
  
  - Permissions allowing you to create Azure Key Vault secrets.

## Add a secret to Azure Key Vault

1. Sign in to the Azure portal and navigate to **Key vaults > {key vault name} > Secrets**.
   
2. Select **+Generate/Import**.
   
3. Set **Upload options** to _Manual_ on the **Create a secret** page.
   
   ![Create a secret in Azure Key Vault](/assets/azure-key-vault-create-secret.BxmO8xGn.png)_Create a secret in Azure Key Vault_
   
4. Enter a name for your secret that will help you remember what application it is for, such as `airtable-api`.
   
5. Enter the secret value. This is typically a password, API key, or other sensitive information.
   
6. Optionally, set the **Content type**, **Activation date**, and/or **Expiration date**.
   
7. Ensure the **Enabled** toggle is set to **Yes**.
   
8. Select **Create**.
   

## Configure a Workato connection

1. Create a new connection or open the configuration page for an existing connection in your Workato account.
   
2. Click the corresponding input field for connection parameters referencing an external secret. The **Add external secret** option appears.
   
3. Select **Add external secret** to open the **Add external secret** popup.
   
4. Enter the **Secret name** in the **Add external secret** popup.
   
   ![Add Azure external secret](/assets/add-external-secret-azure.Dmi1XCTU.png)_Add external secret_
   
5. Select **Done**. The secret appears as a masked datapill in the input field on the connection page.
   
   Select the datapill to edit the secret.
   
6. Click **Connect** and verify that this connection works.
   

If you prefer to add the secret with a secret mask, use the following syntax for Workato connection credentials. Replace `<secret_name>` with the actual name of the secret you plan to use in Azure Key Vault:

```txt
{{workato:sm:<secret_name>}}
```

In the following example, the secret name is `airtable-api`:

```txt
{{workato:sm:airtable-api}}
```

Paste the entire value into the appropriate field on the connection's configuration page.

## Complete your connection setup

Click **Connect** and verify that this connection is working.

## Secrets cache behavior

Workato caches credentials retrieved from Azure Key Vault for **60 minutes**. During this period, recipes continue to use the cached value, even if you update or rotate the secret.

After the cache expires, the next recipe execution retrieves the latest value from Azure Key Vault. You can call the [Clear secrets management cache](/en/workato-api/environment-management#clear-secrets-management-cache) endpoint to apply changes immediately. This forces Workato to fetch the latest credentials without requiring you to disconnect and reconnect the connection.

## Troubleshooting

| Error message | How to fix it |
| --- | --- |
| The secret was not found in this key vault. | Ensure that your secret exists and you are connected to the right Azure Key Vault instance. |
| The secret `{{secret name}}` has been disabled. Please ensure that it is enabled before re-trying. | Ensure that your secret is set to **Enabled**. |
| Caller is not authorized to perform action on resource. | Ensure that your Microsoft Entra ID app has the sufficient [role](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#rbac) or [access policy](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#access-policy) and that your client secret is still valid. |
| Public network access to your Azure Key Vault is disabled. | Ensure that [public access to your key vault](https://learn.microsoft.com/en-us/azure/key-vault/general/network-security) is enabled. |
| Client address is not authorized and caller is not a trusted service. | Ensure that your network IP address has been added to your [key vault's allowlist](https://learn.microsoft.com/en-us/azure/key-vault/general/network-security#key-vault-firewall-enabled-ipv4-addresses-and-ranges---static-ips). |
| Secret is expired. | Create a new secret version with a valid expiration date. |
| Secret is not activated. | Ensure that your secret's activation date is before the current date. |
| Failed to fetch secret from your vault. | Ensure that your secret exists in your vault.; Ensure that your secret follows the format `{{workato:sm:<secret_name>}}`. Different secrets managers require different secret formats, so you may encounter this error if your secret is formatted for another secrets manager. |
