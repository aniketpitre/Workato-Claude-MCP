---
url: >-
  https://docs.workato.com/en/security/data-protection/encryption-key-management/enterprise-key-management.md
description: >-
  Learn how Workato Enterprise Key Management lets you control your workspace
  encryption keys by bringing your own key through a KMS.
---

# Enterprise Key Management

If you require additional control outside of the [robust security Workato offers by default](/en/security/data-protection/encryption-key-management/), you can utilize Workato's **Enterprise Key Management (EKM)** feature. EKM allows you to take complete control of your data by directly managing your workspace's encryption keys.

In this guide, we'll cover:

- [How EKM works](#how-it-works)
- [How EKM works with Environments](#environments)
- [How keys are managed](#key-management)
- [How to set it up](#supported-kms)
- [Troubleshooting resources](#troubleshooting)

> **FEATURE AVAILABILITY**
> 
> Enterprise Key Management is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.

* * *

## How it works

With Workato EKM, you directly control the workspace's top-level [Customer Main Key](/en/security/data-protection/encryption-key-management/#hierarchy-top-level-key), which Workato uses to encrypt other keys in your workspace's key hierarchy.

> **NEED A REFRESHER?**
> 
> Review the [Encryption Key Management guide](/en/security/data-protection/encryption-key-management/#how-it-works) for an overview of Workato's encryption key hierarchy.

Using a [Key Management Service (KMS)](#supported-kms) like Amazon Web Services (AWS) KMS, you maintain the key and grant access to Workato through an access policy. This is referred to as [bringing your own key (BYOK)](/en/security/data-protection/encryption-key-management/glossary#bring-your-own-key).

![Overview of Enterprise Key Management](/assets/full-ekm-overview.CJmfltcL.png)

To use EKM with your own key, generate a new key and grant Workato access. You can do this in one of the following ways:

- Configure an access policy in AWS KMS.
- Upload a key material file to Workato.

After key access is granted, Workato retrieves the key and uses it to encrypt other keys in the hierarchy. Workato's internal KMS completes this process automatically.

* * *

## Keys and environments

EKM works seamlessly with the [Environments feature](/en/features/environments). When used with EKM, you can configure each environment in your workspace with its own Customer Main Key:

> **NOTE**
> 
> This section is applicable if your account has the [Environments feature](/en/features/environments) enabled.

![Overview of Enterprise Key Management](/assets/ekm-with-environments.CRnDPuHd.jpg)

* * *

## Key management

Unlike the default Workato-managed key, bringing your own key allows you to maintain control over all aspects of your workspace's Customer Main Key:

- [Rotation](#key-rotation)
- [Access restriction](#key-access)
- [Revocation and deletion](#key-revocation-deletion)

> **USING ENVIRONMENTS?**
> 
> If you're using the [Environments feature](#environments), note that the information in this section applies to a single environment and not the entire workspace.

### Rotation

Key rotation and replacement is a manual process unless you enable auto-rotation in the KMS, which we recommend as a best practice.

When replacing a key in Workato, note that:

- Replacing a key in Workato is allowed once per 24-hour period.
- Workato [repacks](/en/security/data-protection/encryption-key-management/glossary#repack) the key hierarchy when a key is replaced. This process can take some time.
- If auto-rotation is enabled in the KMS, Workato automatically uses the latest generation of the key. No replacement in Workato is necessary.

### Access restriction

If key access is restricted, [encrypted data](/en/security/data-protection/encryption-key-management/#affected-data) will be available for a short time due to caching. The current time-to-live for the key cache is five (5) minutes.

### Revocation and deletion

When a key is deleted or revoked, [encrypted data](/en/security/data-protection/encryption-key-management/#affected-data) becomes unavailable to all users in the workspace.

* * *

## Supported key management services

Workato EKM currently supports the following:

- [Amazon Key Management Service (KMS)](/en/security/data-protection/encryption-key-management/guides/setting-up-amazon-key-management-service)
- [Custom Key](/en/security/data-protection/encryption-key-management/guides/setting-up-custom-kms-key)

* * *

## Troubleshooting

Need some help? For more information about troubleshooting, see the [EKM troubleshooting guide](/en/security/data-protection/encryption-key-management/troubleshooting).
