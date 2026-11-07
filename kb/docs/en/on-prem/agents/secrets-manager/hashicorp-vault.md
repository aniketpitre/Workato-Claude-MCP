---
url: 'https://docs.workato.com/en/on-prem/agents/secrets-manager/hashicorp-vault.md'
description: >-
  Configure HashiCorp Vault as a secrets engine for Workato on-prem agent cloud
  profiles, without manually editing the config.yml file.
---

# Configuring HashiCorp Vault for on-prem agent

On-prem agent [v2.19](/en/on-prem/agents/versions) and later supports using [HashiCorp Vault](https://www.hashicorp.com/products/vault) as a secrets engine for [cloud profiles](/en/on-prem/agents/connection/cloud).

To set up HashiCorp Vault for OPA, follow either of the guides below. However, when you get to **Step 3**, select an on-prem group from the **Connection type** picklist instead of _Cloud_. The rest of the setup is identical.

- [Setting up HashiCorp Vault secrets engines for workspaces](/en/security/data-protection/secrets-management/setting-up-workspace-level-hashicorp-vault-secrets-engine)
- [Setting up HashiCorp Vault secrets engines for projects](/en/security/data-protection/secrets-management/setting-up-project-level-hashicorp-vault-secrets-engine)

When you configure HashiCorp Vault for cloud profiles, you do not need to manually edit the `config.yml` file.

* * *

> **FURTHER READING**
> 
> - [Using HashiCorp Vault secrets to authenticate to connections](/en/security/data-protection/secrets-management/using-hashicorp-secrets-in-connections)
> - [HashiCorp Vault policies](/en/security/data-protection/secrets-management/hashicorp-vault-policies)

---
