---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-project-level-hashicorp-vault-secrets-engine.md
description: >-
  Set up HashiCorp Vault KV secrets engines for project-level secrets management
  to scope connection credentials to individual Workato projects.
---

# Set up HashiCorp Vault secrets engines for projects

Switching to project-specific secrets management causes all previously configured external secret references to stop working.

## Prerequisites

To complete the steps in this guide, you must have the following:

- HashiCorp Vault Key-value (KV) secrets engine version 1 or 2.
- An account with [AppRole auth method](https://developer.hashicorp.com/vault/tutorials/auth-methods/approle#step-2-create-a-role-with-policy-attached) enabled.
- One or more [AppRole](https://developer.hashicorp.com/vault/docs/auth/approle?_gl=1*vnxfyv*_ga*MTM5ODQwMDE3My4xNjgxMjQzMzg2*_ga_P7S46ZYEKW*MTY4MTQxNzMxMS4xLjAuMTY4MTQxNzMxMS4wLjAuMA..#configuration)s configured.

## Select the scope for secrets management

1. Sign in to Workato.
   
2. Navigate to **Workspace admin > Settings > External secrets manager**.
   
3. Select the **Set up secrets management for each project individually** option from the **Scope** drop-down menu.
   
   ![Select scope](/assets/hashicorp-vault-secrets-scope.DHqVzoD9.png)_Select project-level secrets management_
   
4. Click **Save**.
   
5. If you switch secrets management scopes, Workato notifies you that existing external secret references scoped to the project level will no longer function.
   
   To proceed with switching from workspace-level to project-level secrets management, select the checkbox to acknowledge the impact and click **Use project-specific secrets**.
   
   ![Use project-specific secrets](/assets/use-project-specific-secrets.DgRlX7uh.png)_Use project-specific secrets_
   

## Select the project

1. In Workato, navigate to your projects.
   
2. Select the project that you plan to configure with secrets management.
   
3. In the project, navigate to **Settings > External secrets manager**.
   
4. Select **HashiCorp Vault** from the **Which secrets manager do you want to use?** drop-down menu.
   
   ![Secrets management interface of a project](/assets/select-hashicorp-projects.ffwTOmqZ.png)
   

## Configure the connection in Workato

![Configure connection](/assets/connect.e9rBNOtm.png)_Connect to HashiCorp Vault_

1. - Connection name
   - Name your HashiCorp Vault connection.
2. - Connection type
   - To connect to HashiCorp Vault using an [on-prem group](/en/on-prem/groups), select the group name from the drop-down menu. Otherwise, to use a direct connection, select **Cloud**.
3. - Authentication type
   - Select **AppRole** from the drop-down.
4. - Vault URL
   - Enter the **Vault URL** of your Hashicorp Vault instance. It should follow this form `https://<instance_name>.<company_name>.com:123`.
     - instance\_name
       
     - The name of your HashiCorp Vault instance.
       
     - company\_name
       
     - The name of your organization.
       
5. - Namespace
     
   - _Optional_. The name of the namespace that contains the secret(s) you plan to use in Workato. [Namespaces](https://developer.hashicorp.com/vault/docs/enterprise/namespaces) are a set of features that enable you to define granular control and secrets management within your organization.
     
     In our example, we grant Workato access to the `admin/HR` namespace.
     
6. - AppRole name
   - The **AppRole** you plan to use. An **AppRole** is a set of Vault policies and login constraints that determines which secrets you can access.

## Obtain the AppRole ID and AppRole Secret ID from HashiCorp Vault

AppRole is a login credential split into two parts- the **AppRole ID** and **AppRole Secret ID**. You must obtain both to authenticate to Workato. The AppRole ID can be considered similar to a username- its value remains constant and associated with its corresponding AppRole. On the contrary, the **AppRole Secret ID** is similar to a password or unique key and you can prompt HashiCorp Vault to refresh this credential, if needed.

1. In HashiCorp Vault click **\>\_** to open the control panel.
   
   ![Command icon](/assets/command-icon.DukO8fHa.png)_Open the control panel_
   
2. Enter the following command:
   
   ```
   vault read auth/<approle_name>/role/<role_name>/role-id
   ```
   
   - approle\_name
     
   - The AppRole you have configured in HashiCorp Vault.
     
   - role\_name
     
   - The name of the role (Workato) you plan to connect to.
     
   
   **Example:**
   
   ```
   vault read auth/workato_approle/role/workato/role-id
   ```
   
3. HashiCorp Vault returns the AppRole ID unique to your AppRole:
   
   ```
   Key     Value
   role_id 12a3bc45-6de7-8910-11fg-h4ij12XXXXXX
   ```
   
4. Copy and paste this value into the **AppRole ID** field in Workato.
   
5. Obtain the **AppRole Secret ID** by entering the following command to the control panel in HashiCorp Vault:
   
   ```
   vault write -force auth/<approle_name>/role/<role_name>/secret-id
   ```
   
   **Example:**
   
   ```
   vault write -force auth/workato_approle/role/workato/secret-id
   ```
   
6. HashiCorp Vault generates an AppRole Secret ID for your AppRole:
   
   ```
   Key                 Value
   secret_id           ed0a642f-2acf-c2da-232f-1b2130XXXXXX
   secret_id_accessor  a240a31f-270a-4765-64bd-94ba1fXXXXXX
   ```
   
7. Copy and paste the `secret_id` value into the **AppRole Secret ID** field in Workato.
   
8. Click **Connect**.
   

> **FURTHER READING**
> 
> - [Using HashiCorp Vault Secrets to authenticate to connections](/en/security/data-protection/secrets-management/using-hashicorp-secrets-in-connections)
