---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/using-cyberark-conjur-in-connections.md
description: >-
  Configure Workato connections using secrets from CyberArk Conjur Cloud or
  self-hosted Conjur Enterprise.
---

# Use CyberArk Conjur secrets in connections

This guide demonstrates how to use secrets from CyberArk Conjur to configure Workato connections.

## Prerequisites

To complete the steps in this guide, you must have the following:

- **In Workato**:
  
  - An account with a successful [CyberArk Conjur Workspace-level](/en/security/data-protection/secrets-management/setting-up-workspace-level-cyberark-conjur) or [Project-level](/en/security/data-protection/secrets-management/setting-up-project-level-cyberark-conjur) connection.
  - A [user role](/en/roles) with **Create** and **Edit Connections** privileges.
- **CyberArk Conjur**:
  
  - **Conjur Cloud**: A [defined workload policy](https://docs.cyberark.com/conjur-cloud/latest/en/Content/Get%20Started/key_concepts/machine_identity.html).
  - **Self-hosted Conjur Enterprise**: A [host policy statement](https://docs.cyberark.com/conjur-enterprise/latest/en/Content/Operations/Policy/statement-ref-host.htm).

## Retrieve the secret's details from CyberArk Conjur

1. Authenticate to your Conjur Cloud or Conjur Enterprise server.
   
2. Retrieve the secret ID that you plan to use for the Workato connection.
   
   - **Conjur Cloud**: Include the name of the vault that it is stored: `data/vault/Partner-Workato/airtable/password`
   - **Conjur Enterprise**: Include the name of the policy where the variable is stored: `AutomationVault/db/password`
   
   > **NOT SUPPORTED: MULTILINE SECRETS**
   > 
   > Conjur Cloud does not support passing multiline secrets such as private keys or certificates to Workato.
   
3. Create a new connection or open the configuration page for an existing connection in your Workato account.
   
   ![Configure CyberArk Conjur connection](/assets/connection-setup.BL2Z8OX0.png)_Configure CyberArk Conjur connection_
   
4. Click the corresponding input field for connection parameters referencing an external secret. The **Add external secret** option appears.
   
5. Select **Add external secret** to open the **Add external secret** popup.
   
6. Enter the **Secret name** in the **Add external secret** popup.
   
   ![Add Conjur external secret](/assets/add-external-secret-conjur.CcJ7MQSn.png)_Add external secret_
   
7. Select **Done**. The secret appears as a masked datapill in the input field on the connection page.
   
   Select the datapill to edit the secret.
   
8. Click **Connect** and verify that this connection works.
   

If you prefer to add the secret with a secret mask, follow this syntax for the secrets used in Workato connection credentials:

```txt
{{workato:sm:<secret-name>}}
```

Replace `<secret-name>` with the secret ID as shown in Conjur.

## How to revoke access to secrets store on CyberArk Conjur

To revoke Workato's access to secrets stored on CyberArk Conjur, rotate the host's API key with a PUT request and ensure that the host ID is URL-encoded:

```shell
PUT {{conjurServer}}/authn/{{conjurOrganization}}/api_key?role=host:workato-conjur-demo/workato-us-2
```

Secrets are no longer accessible after sixty minutes.

To revoke access immediately, rotate the API key, then use the [clear\_cache](/en/workato-api/environment-management#clear-secrets-management-cache) API.

For more information, consult the Conjur documentation on [how to rotate host API keys](https://docs.cyberark.com/conjur-open-source/Latest/en/Content/Developer/Conjur_API_Rotate_Personal_API_Key.htm).

This process applies to both CyberArk Conjur Enterprise and CyberArk Conjur Open Source. Visit the [Cyberark Conjur Cloud-specific documentation](https://docs.cyberark.com/conjur-cloud/latest/en/Content/Developer/Conjur_API_Rotate_Other_API_Key.htm) for more information.

## Secrets cache behavior

Workato caches credentials retrieved from CyberArk Conjur for **60 minutes**. During this period, recipes continue to use the cached value, even if you update or rotate the secret.

After the cache expires, the next recipe execution retrieves the latest value from CyberArk Conjur. You can call the [Clear secrets management cache](/en/workato-api/environment-management#clear-secrets-management-cache) endpoint to apply changes immediately. This forces Workato to fetch the latest credentials without requiring you to disconnect and reconnect the connection.

## Troubleshooting

### Uninitialized variables and insufficient permissions

Ensure that your `host/host data/Workato/Workato-dev` has the necessary permissions and that your variable has been initialized.

- Secret is not initialized
  - The secret key is created on Conjur but no value has been assigned to it. Assign a value to the secret in Conjur.
- Host does not have permissions
  - The host (service account that you used to create the connection) must have the `[create, execute]` permissions for a specific secret. This enables Workato to retrieve its value and establish the connection successfully.

### Invalid credentials

Confirm that you entered the correct information into the required fields.

- **Server URL**
  - Ensure that it is in the form `https://<domain>` for a self-hosted Conjur Enterprise set up or `https://<subdomain>.secretsmgr.cyberark.cloud/api/` when connecting to Conjur Cloud.
- **Organization account name**
  - The name of the organization when first configuring the leader node in Conjur Enterprise, or `conjur` when connecting to Conjur Cloud.
- **Login ID**
  - The name of the host that has been assigned `[read, execute]` permissions on the variables or the name of the workload in Conjur Cloud.
- **API key**
  - The API key that was generated when the host / workload was initially created.
