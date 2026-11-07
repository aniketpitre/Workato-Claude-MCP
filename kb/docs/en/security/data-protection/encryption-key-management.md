---
url: >-
  https://docs.workato.com/en/security/data-protection/encryption-key-management.md
description: >-
  Learn how Workato encrypts data at rest and in transit using a multi-level key
  hierarchy with encryption keys unique to each workspace.
---

# Encryption key management

Data in Workato is encrypted at rest and in transit. At rest, data is encrypted using a top-level encryption key and a multi-level key hierarchy. Encryption keys are unique to each workspace, limiting vulnerabilities and ensuring your data is separate from other workspaces.

This guide covers the following topics:

- [How data encryption works in Workato](#how-it-works)
- [The data encryption effects](#affected-data)
- [How encryption keys are managed](#key-management)

> **FEATURE AVAILABILITY**
> 
> Encryption key management is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

## How it works

The foundation for Workato's encryption key management is a hierarchical key model. The key hierarchy consists of several levels of keys, where each key level encrypts the keys in the level beneath it:

![Encryption key management key hierarchy](/assets/key-hierarchy-top-level.DeZHfpor.jpg)

> **GLOSSARY**
> 
> For definitions of the terms used in this guide, refer to the [glossary](/en/security/data-protection/encryption-key-management/glossary).

This multi-level approach to encryption reduces the risk of exposure by limiting the data a single key can access. For example, if a data key for a job is compromised, the exposure is limited only to that specific job.

Workato's key hierarchy consists of three levels:

- [Top level](#hierarchy-top-level-key)
- [Intermediate level](#hierarchy-intermediate-level-key)
- [Data level](#hierarchy-data-level-key)

### Top level

At the top of the hierarchy is the [Customer Main Key (CMK)](/en/security/data-protection/encryption-key-management/glossary#customer-main-key), which is unique to the workspace and encrypts all other keys in the hierarchy.

The CMK can be one of the following:

- [Workato-managed](/en/security/data-protection/encryption-key-management/glossary#workato-managed-key), meaning Workato creates, owns, and manages the key on your behalf. Your workspace will use a Workato-managed key unless you [bring your own key](/en/security/data-protection/encryption-key-management/glossary#bring-your-own-key).
  
- [Customer-managed](/en/security/data-protection/encryption-key-management/glossary#customer-managed-key), meaning that you own and manage the key. You provide the key reference or material to Workato.
  

### Intermediate level

At the intermediate level, [hourly keys](/en/security/data-protection/encryption-key-management/glossary#hourly-key) act as an intermediary between the CMK and job data. A new key is generated each hour and is used to encrypt all job data that occurs during the following hour. This reduces potential exposure in case of key compromise to a single hour's worth of job data.

### Data level

The last level in the hierarchy consists of keys that encrypt your actual data:

- **Connection keys**: A unique, connection-specific key used to encrypt [connection data](#connection-data).
  
- **Data (job) keys**: A unique, job-specific key used to encrypt [job data](#job-data). Hourly keys encrypt data keys.
  
- **Log key**: A unique key used to encrypt [log data](#log-data).
  

## Keys and environments

If you're using Environments, Workato uses a unique Customer Main Key for each environment:

![Overview of Encryption Key Management with Environments](/assets/ekm-with-environments.CRnDPuHd.jpg)

> **ENVIRONMENTS**
> 
> This section applies to workspaces with the [Environments](/en/features/environments) feature enabled.

## Affected data

Encryption Key Management currently affects the following types of data in Workato:

- [Connection data](#connection-data)
- [Job data](#job-data)
- [Log data](#log-data)

> **DATA TABLES AND WORKFLOW APPS DATA**
> 
> [Data tables](/en/data-tables) and [Workflow apps](/en/workflow-apps) data use filesystem-level encryption instead of a Customer Main Key (CMK).

### Connection data

Connection data includes details about connections in the workspace. Connection data is encrypted using the following hierarchy:

![Key hierarchy for connection data](/assets/connection-key-hierarchy.DzymIn1t.jpg)

### Job data

Job data includes job metadata, such as title, completion, report, result, and details, such as snapshot and line information.

All job data, except for the trigger event, is encrypted using the following hierarchy:

![Key hierarchy for job data](/assets/job-key-hierarchy.DsOmw9y-.jpg)

Trigger events are only encrypted with an hourly key, while other job data is encrypted with an hourly key and a data key.

### Log data

Log data includes log entries in [Workato's Logging service](/en/features/logging-service).

![Key hierarchy for log data](/assets/log-key-hierarchy.BrNTHAWg.jpg)

## Key management

This section explains how key types are managed, including key replacement (rotation), revocation, access, and deletion.

- [Customer Main Key](#customer-main-key-management)
- [Hourly keys](#hourly-key-rotation)

> **USING ENVIRONMENTS?**
> 
> If you're using the [Environments](#environments) feature, note that the information in this section applies to a single environment and not the entire workspace.

### Customer Main Key

How a Customer Main Key is managed depends on whether you're using the [Enterprise Key Management](/en/security/data-protection/encryption-key-management/enterprise-key-management) feature to [bring your own key](/en/security/data-protection/encryption-key-management/glossary#bring-your-own-key):

- [Customer-managed key](#customer-managed-key-management)
- [Workato-managed key](#workato-managed-key-management)

#### Customer-managed key

All aspects of a customer-managed key are controlled by you.

- **Rotation**: Key rotation and replacement is a manual process unless auto-rotation is enabled in the KMS. If auto-rotation is enabled, which we recommend as a best practice, the KMS handles rotation, and no updates in Workato are necessary.
  
  If replacing a key in Workato, note that:
  
  - Replacing a key in Workato is allowed once per 24-hour period.
  - Workato will [repack](/en/security/data-protection/encryption-key-management/glossary#repack) the key hierarchy when a key is replaced. This process can take some time.
  - If auto-rotation is enabled in the KMS, Workato automatically uses the latest generation of the key. No replacement in Workato is necessary.
- **Access restriction**: If key access is restricted, [encrypted data](#affected-data) will be available for a short time due to caching. The current time-to-live for the key cache is five (5) minutes.
  
- **Revocation and deletion**: When a key is deleted or revoked, [encrypted data](#affected-data) is unavailable to all users in the workspace. **Note**: If the revocation or deletion is permanent, the data in Workato will be permanently inaccessible.
  

#### Workato-managed key

If using a Workato-managed key, Workato manages all aspects of the key.

- **Rotation**: Automatic. Workato will rotate the key at least once per year.
  
- **Access restriction**: Managed automatically by Workato.
  
- **Revocation and deletion**: Managed automatically by Workato.
  

### Hourly keys

To minimize vulnerabilities, Workato generates new hourly keys every hour. Hourly keys are used to encrypt data keys, which in turn encrypt [job data](#job-data).

Consider the following example:

1. **12:00 PM**: A new hourly key (`key1`) is generated. This key is considered the current active key and will be used to encrypt data from jobs that run during this hour or between **12:00 PM** and **1:00 PM**.
   
2. **12:05 PM**:
   
   - Two jobs, `job1` and `job2`, complete.
   - `key1` encrypts the data keys associated with these jobs.
3. **1:00 PM**:
   
   - `key1` becomes inactive. `key1` can now only decrypt data.
   - A new key, `key2`, is generated and becomes active.
4. **1:15 PM**:
   
   - Two jobs, `job3` and `job4`, complete.
   - `key2` encrypts the data keys associated with these jobs.
5. **2:00 PM**:
   
   - `key2` is rotated and becomes inactive. `key2` can now only decrypt data.
   - A new key, `key3`, is generated and becomes active.
