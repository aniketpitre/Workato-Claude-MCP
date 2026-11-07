---
url: >-
  https://docs.workato.com/en/security/data-protection/encryption-key-management/guides/setting-up-custom-kms-key.md
description: >-
  Configure Workato Enterprise Key Management with a custom key by generating
  your own encryption key and using it to set up EKM.
---

# Configuring Workato Enterprise Key Management (EKM) with a custom key

In addition to popular key management systems, [Workato Enterprise Key Management (EKM)](/en/security/data-protection/encryption-key-management/enterprise-key-management) also supports generating your own custom keys.

In this guide, we'll walk you through creating a custom key and using it to configure EKM in Workato.

* * *

## Prerequisites

To perform the tasks in this guide, you'll need:

- A Workato account with the [Enterprise Key Management](/en/security/data-protection/encryption-key-management/enterprise-key-management) feature enabled
- A Workato [user role](/en/roles) with the **Key management** privilege

* * *

## Step 1: Generate a custom key

First, generate a custom key and save it to a file.

The following example demonstrates how to use the [OpenSSL library](https://www.openssl.org/) to generate a 32 byte, base64-encoded, 256-bit symmetric key:

```shell
openssl rand -out WorkatoCustomKey.txt -base64 32
```

> **KEY REQUIREMENTS**
> 
> Custom keys must be 32 byte, base64-encoded, 256-bit symmetric keys.

The key is encoded using base64 encoding and saved to a file named `WorkatoCustomKey.txt`. For more information about the command (`rand`), see [OpenSSL documentation](https://www.openssl.org/docs/man1.0.2/man1/rand.html).

> **CREATE YOUR OWN CUSTOM KEY**
> 
> You can use other tools to generate custom keys as long as the keys meet the requirements listed above.
> 
> Note that keys must be generated using a cryptographically secure pseudo random number generator (CSPRNG). Any keys you generate must be strongly protected from unauthorized access because keys are highly sensitive material. For example, protect your key by storing it in a secure location.

* * *

## Step 2: Upload the key to Workato

1. Sign in to Workato if you haven't already.
   
2. Go to **Workspace admin > Settings > Encryption keys**.
   
3. In the **How do you want to encrypt your data?** field, select **Custom KMS key** from the drop-down.
   
4. In the **Key material file** field, drag and drop or upload the key file.
   
5. Click **Update key**.
