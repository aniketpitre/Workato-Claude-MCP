---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/using-hashicorp-secrets-in-connections.md
description: >-
  Configure Workato connections using secrets from your HashiCorp Vault KV
  secrets engine with AppRole authentication.
---

# Use HashiCorp Vault secrets engine in connections

This guide demonstrates how to use secrets from your HashiCorp Vault secrets engine to configure Workato connections.

* * *

## Prerequisites

To complete the steps in this guide, you must have the following:

- **In Workato**:
  
  - An account with a successful [HashiCorp Vault secrets engine Workspace-level](/en/security/data-protection/secrets-management/setting-up-workspace-level-hashicorp-vault-secrets-engine) or [HashiCorp Vault secrets engine Project-level](/en/security/data-protection/secrets-management/setting-up-workspace-level-hashicorp-vault-secrets-engine) connection.
  - A [user role](/en/roles) with **Create** and **Edit Connections** privileges.
- **In HashiCorp Vault**:
  
  - HashiCorp Vault Key-value (KV) secrets engine version 1 or 2.
  - An account with [AppRole auth method](https://developer.hashicorp.com/vault/tutorials/auth-methods/approle#step-2-create-a-role-with-policy-attached) enabled.
  - One or more [AppRole](https://developer.hashicorp.com/vault/docs/auth/approle?_gl=1*vnxfyv*_ga*MTM5ODQwMDE3My4xNjgxMjQzMzg2*_ga_P7S46ZYEKW*MTY4MTQxNzMxMS4xLjAuMTY4MTQxNzMxMS4wLjAuMA..#configuration)s configured.
  - A [policy](/en/security/data-protection/secrets-management/hashicorp-vault-policies) that grants Workato read access to secrets engine configuration and to the secrets engine(s) you plan to use.
  - A secret engine that does not contain any [reserved characters](https://www.rfc-editor.org/rfc/rfc3986#section-2.2), such as `;`, `/`, `?`, `:`, `@`, `&`, `=`, `+`, `$`, `,`.

* * *

## Retrieve the secret's details from HashiCorp Vault

1. Sign in to your HashiCorp Vault instance and open the **Secrets** interface.
   
2. Select the **Secrets Engine** you plan to use. Take note of the name of the Secrets Engine you select. You will need this to complete the next step.
   
   In this example, the name of our Secrets Engine is **workato\_docs**.
   
   ![Select a Secrets Engine](/assets/secrets-engine.R-DSiTFf.png)_Select a Secrets Engine_
   
3. Select the **Secret** you plan to use. Secrets are key-value pairs.
   
   In our example, the secret name is **Zendesk**.
   
   ![Select a Secret](/assets/secret.BJRoDazT.png)_Select a Secret_
   
4. Keep this page open. You will need to reference it in the next step.
   

* * *

## Configure a Workato connection

1. Create a new connection or open the configuration page for an existing connection in your Workato account.
   
2. Click the corresponding input field for connection parameters referencing an external secret. The **Add external secret** option appears.
   
3. Select **Add external secret** to open the **Add external secret** popup.
   
4. Enter the **Secret engine name**, **Secret name**, and **Key name** in the **Add external secret** popup.
   
   ![Add HashiCorp external secret](/assets/add-external-secret-hashicorp.DQAZpaKM.png)_Add external secret_
   
5. Select **Done**. The secret appears as a masked datapill in the input field on the connection page.
   
   Select the datapill to edit the secret.
   
6. Click **Connect** and verify that this connection works.
   

If you prefer to add the secret with a secret mask, use the following syntax for Workato connection credentials:

```text
{{workato:sm:<key_name>:<secret_engine_name>:<secret_name>}}
```

- `<key_name>`
  
- The name of the key. Your secret stored in HashiCorp Vault can contain multiple key-value pairs.
  
- `<secret_engine_name>`
  
- The name of the secret engine you plan to use.
  
- `<secret_name>`
  
- The name of the secret you plan to use. Your secrets engine can contain multiple secrets.
  

For example:

```text
{{workato:sm:password:workato_docs:zendesk}}
```

Where `workato_docs` is the secrets engine and `zendesk` is the secret's name.

In the connection's configuration page, paste this entire value into the appropriate field.

* * *

## Complete your connection setup

Click **Connect** and verify that this connection is working.

## Secrets cache behavior

Workato caches credentials retrieved from HashiCorp Vault for **60 minutes**. During this period, recipes continue to use the cached value, even if you update or rotate the secret.

After the cache expires, the next recipe execution retrieves the latest value from HashiCorp Vault. You can call the [Clear secrets management cache](/en/workato-api/environment-management#clear-secrets-management-cache) endpoint to apply changes immediately. This forces Workato to fetch the latest credentials without requiring you to disconnect and reconnect the connection.
