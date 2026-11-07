---
url: >-
  https://docs.workato.com/en/security/data-protection/encryption-key-management/glossary.md
description: >-
  Reference for Workato Enterprise Key Management terms, including Customer Main
  Key, connection key, data key, and bring your own key.
---

# Enterprise Key Management glossary

This glossary covers terms related to Workato's [Enterprise Key Management (EKM)](/en/security/data-protection/encryption-key-management/) feature:

- [Bring Your Own Key (BYOK)](#bring-your-own-key)
- [Connection Key (CK)](#connection-key)
- [Custom KMS key](#custom-kms-key)
- [Customer-managed Key](#customer-managed-key)
- [Customer Main Key (CMK)](#customer-main-key)
- [Data Key (DK)](#data-key)
- [Hourly Key (HK)](#hourly-key)
- [Key Management System (KMS)](#key-management-system)
- [Repacking](#repack)
- [Workato KMS key](#workato-kms-key)
- [Workato-managed key](#workato-managed-key)

## Bring your own key (BYOK)

[**Bring your own key (BYOK)**](https://en.wikipedia.org/wiki/Bring_your_own_encryption) is an approach to data encryption that allows customers to use [their own encryption software](#key-management-system) and manage their keys externally.

In Workato, this means you can use a service like [Amazon Key Management Service (KMS)](/en/security/data-protection/encryption-key-management/guides/setting-up-amazon-key-management-service) to manage the [Customer Main Key (CMK)](#customer-main-key). Workato uses the CMK to perform data encryption.

## Connection key

**Connection keys (CK)** are keys used to encrypt connection data. A unique, connection-specific key encrypts each connection.

Connection keys are encrypted by the account's [Customer Main Key (CMK)](#customer-main-key).

## Custom KMS key

See [Customer-managed key](#customer-managed-key).

## Customer-managed key

A **Customer-managed key** is a key that you create, own, and manage ([BYOK](#bring-your-own-key)). Keys are created in a [key management service](#key-management-system) or through a library like OpenSSL.

When used in Workato EKM, Workato uses the key you provide as the [Customer Main Key](#customer-main-key) to encrypt and decrypt [data keys](#data-key).

## Customer Main Key (CMK)

A **Customer Main Key (CMK)** is a top-level key that encrypts [Connection](#connection-key) and [Hourly keys](#hourly-key).

In Workato, the CMK can be one of the following:

- [**Customer-managed**](#customer-managed-key) - The CMK is a key you generate and provide to Workato. You own and manage the key in the KMS, providing the reference to Workato.
- [**Workato-managed**](#workato-managed-key) - The CMK is a key generated and managed by Workato. Workato owns and manages the key on your behalf.

## Data Key (DK)

**Data keys (DK)** are keys used to encrypt job data. A unique, job-specific data key encrypts each job. An [Hourly key](#hourly-key) encrypts the job-specific data key.

## Hourly Key (HK)

**Hourly keys (HK)** are keys used to encrypt [job data keys](#data-key). A new key is generated on an hourly basis.

## Key Management System (KMS)

A **Key Management System (KMS)** is [a system for securely managing cryptographic keys](https://en.wikipedia.org/wiki/Key_management#key-management-system). For example: [Amazon Key Management Service (KMS)](/en/security/data-protection/encryption-key-management/guides/setting-up-amazon-key-management-service)

## Repacking

Synonymous with re-encryption, **repacking** occurs when the [Customer Main Key](#customer-main-key) is rotated or replaced, whether by you or Workato.

For example: _When a new custom key is uploaded to Workato, Workato will repack all connection, hourly, and data keys currently in use._

## Workato KMS key

See [Workato-managed key](#workato-managed-key).

## Workato-managed keys

A **Workato-managed key** is a key that Workato creates, owns, and manages on your behalf. A Workato-managed key is synonymous with [Workato KMS key](#workato-kms-key).

Unless [BYOK](#bring-your-own-key) is fully configured, Workato will use a Workato-managed key as your account's [Customer Main Key](#customer-main-key) to encrypt and decrypt [data keys](#data-key).

All Workato-managed keys are automatically rotated once per year. Currently, this rotation schedule can't be changed.
