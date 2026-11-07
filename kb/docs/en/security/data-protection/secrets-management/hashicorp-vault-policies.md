---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/hashicorp-vault-policies.md
description: >-
  Set up a HashiCorp Vault policy that grants Workato read access to your
  secrets engine configuration and the secrets you plan to use.
---

# HashiCorp Vault policies

In HashiCorp Vault, policies determine access to certain paths and operations within Vault. Because policies are configured to deny access by default, you must create a policy which gives Workato the ability to read your secrets engine configuration, as well as read access to the secrets you plan to use.

Policies are in JSON or HCL format. A typical policy contains the path(s) you plan to access in HashiCorp Vault and the capabilities you define for each path.

Note that the path differs according to the [Key-Value (KV) engine version](https://developer.hashicorp.com/vault/docs/secrets/kv) and whether the path is fully qualified. See [Vault policy permissions](#vault-policy-permissions) for details.

This document explains the paths and capabilities you must add to your policy to use HashiCorp Vault secrets in Workato.

[Learn more about policies](https://developer.hashicorp.com/vault/docs/concepts/policies) in HashiCorp Vault's documentation.

* * *

## Set up HashiCorp Vault policies

The following steps show how to set up a [restrictive](#vault-restrictive-policies) HashiCorp Vault policy for both [KV v1](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v1) and [KV v2](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2).

1. In your HashiCorp Vault instance, navigate to **Policies**.
   
2. Click **Create ACL policy** or edit one of your existing policies.
   
3. Enable Workato to read your secrets engine configuration by adding the following to your policy. We recommend adding short descriptive text preceding the path to help orient your users, denoted by `#`:
   
   ```
   # This allows read access to the secrets engine configuration, which is required to get the engine's version. Different versions have different APIs.
   
   path "sys/mounts/<secret_engine_name>" {
     capabilities = [ "read" ]
   }
   ```
   
   For example:
   
   ```
   # This allows read access to the secrets engine configuration, which is required to get the engine's version. Different versions have different APIs.
   
   path "sys/mounts/workato_docs" {
     capabilities = [ "read" ]
   }
   ```
   
4. Enable Workato to access your secrets engine(s) by adding the following to your policy, according to the [KV version](https://developer.hashicorp.com/vault/docs/secrets/kv) you're using:
   
   KV v1
   
   For [**KV v1**](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v1), use following syntax:
   
   ```
   path "<secret_engine_name>/<secret_name>" {
     capabilities = [ "read" ]
   }
   ```
   
   For example:
   
   ```
   # Read Zendesk secrets (KV v1)
   path "workato_docs/zendesk" {
     capabilities = [ "read" ]
   }
   ```
   
   KV v2
   
   For [**KV v2**](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2), you must include `data/` in the path, after the engine name:
   
   ```
   path "<secret_engine_name>/data/<secret_name>" {
     capabilities = [ "read" ]
   }
   ```
   
   For example:
   
   ```
   # Read Zendesk secrets (KV v2)
   path "workato_docs/data/zendesk" {
     capabilities = [ "read" ]
   }
   ```
   
5. Add additional secrets engines to your policy, if necessary.
   

* * *

## Vault policy permissions

You can fine-tune Workato's level of access to your secret(s) by specifying a restrictive policy, or give it broad access with a permissive policy. Syntax differs accordingly, as shown in the following sections.

* * *

### Restrictive policies

For fine-grained, restrictive policies, use a fully qualified path to specify the precise secret Workato can read.

Note that the fully qualified secret path differs according to the [KV version](https://developer.hashicorp.com/vault/docs/secrets/kv) you're using. Paths using the [KV v2](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2) engine must include `data/` after the engine name, but paths using [KV v1](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v1) must not.

For example, the following **KV v2** policy grants Workato read-only access to the `zendesk` secret in the `workato_docs` engine:

```
# Read Zendesk secrets (KV v2)
path "workato_docs/data/zendesk" {
  capabilities = [ "read" ]
}
```

The following **KV v1** policy is functionally identical:

```
# Read Zendesk secrets (KV v1)
path "workato_docs/zendesk" {
  capabilities = [ "read" ]
}
```

* * *

### Permissive policies

To write a more permissive policy, use a glob (`*`) in the secret path to grant Workato access to all secrets in an engine. For example, the following policy grants Workato read-only access to all of the secrets in the `workato_docs` engine:

```
# Read Zendesk secrets
path "workato_docs/*" {
  capabilities = [ "read" ]
}
```

In this case, you can use the same syntax for KV v1 and v2 because the policy does not use a fully qualified secret path.

* * *

## Example policy

The following is an example of a complete HashiCorp Vault policy granting Workato read-only access to multiple secrets engines:

```
# This allows read access to the secrets engine configuration, which is required to get the engine's version. Different versions have different APIs.

path "sys/mounts/workato_zendesk" {
  capabilities = [ "read" ]
}
path "sys/mounts/workato_jira" {
  capabilities = [ "read" ]
}
path "sys/mounts/workato_db" {
  capabilities = [ "read" ]
}

# Read Zendesk secrets (KV v2)
path "workato_zendesk/data/zendesk" {
  capabilities = [ "read" ]
}
# Read JIRA secrets (KV v1)
path "workato_jira/jira" {
  capabilities = [ "read" ]
}
# Read DB secrets
path "workato_db/*" {
  capabilities = [ "read" ]
}
```
