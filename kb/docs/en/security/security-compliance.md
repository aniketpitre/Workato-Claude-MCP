---
url: 'https://docs.workato.com/en/security/security-compliance.md'
description: >-
  Learn about the security compliance frameworks Workato maintains, including
  PCI-DSS Level 1, ISO 27001, and ISO 27701.
---

# Security compliance frameworks

Workato prioritizes data security and regulatory compliance, ensuring that users can rely on our platform to automate workflows and integrate applications without compromising sensitive data.

Workato maintains comprehensive security compliance frameworks to safeguard customer data. These frameworks meet global standards, ensuring our users can operate with confidence across industries.

> **SUMMARY**
> 
> Workato upholds rigorous security standards with the following frameworks:
> 
> - **PCI-DSS v4.0.1 − Level 1**: Secure cardholder data.
> - **ISO 27001, 27701 & 42001**: Information, privacy, and AI management aligned with global standards.
> - **SOC 1 Type II, SOC 2 Type II, and SOC 3**: Audited controls for financial and security integrity.
> - **HIPAA**: Healthcare data protection, with Business Associate Agreements (BAAs) available.
> - **IRAP**: Strict cybersecurity standards aligned to Australian government requirements.
> - **NIST 800-171A r2**: Controlled Unclassified Information (CUI) protection for federal contractors, partners, and subcontractors.
> 
> Workato empowers organizations in finance, healthcare, and government to securely manage data workflows and integrations with our security features and frameworks.

## PCI-DSS level 1

Workato is a PCI-DSS v4.0.1 − Level 1 service provider for Payment Card Industry Data Security Standards. These security standards ensure that data and data activities are protected:

- Cardholder data storage
- Data processing
- Data transmission

PCI-DSS v4.0.1 − Level 1 compliance allows financial services industry users to use the Workato platform for payment-related operations with confidence. We undergo an annual assessment by an approved Qualified Security Assessor (QSA) to maintain compliance.

_Attestation of Compliance (AoC) available upon request._

## ISO 27001

ISO 27001 certification specifies controls for establishing, implementing, and improving information security across Workato’s systems, making it the global standard for information security management systems (ISMS). This certification underlines our commitment to data security and operational resilience.

_AoC available upon request._

## ISO 27701

ISO 27701 extends ISO 27001 for Privacy Information Management Systems (PIMS), addressing the requirements for handling Personally Identifiable Information (PII) and aligning with global privacy regulations like GDPR.

_AoC available upon request._

## ISO 42001

Workato aligns with ISO/IEC 42001 by governing AI through defined oversight, lifecycle-based risk management, and responsible AI practices. AI risks such as bias, misuse, security, and privacy are assessed and mitigated before and after deployment. Secure-by-design controls, documentation, monitoring, incident response, and continuous improvement ensure AI is used responsibly, transparently, and in line with compliance expectations.

## SOC 1 Type II

Our SOC 1 Type II certification evaluates Workato’s controls related to customers’ financial reporting, specifically assessing the internal controls relevant to user entities’ financial statements. This compliance is essential for organizations that require financial statement audits, providing assurance on the impact of Workato’s services on their reporting.

_Audit reports available to customers under NDA._

## SOC 2 Type II

The SOC 2 Type II certification is aligned with the American Institute of CPAs (AICPA) Trust Services Criteria, and evaluates Workato’s effectiveness in the following data concerns:

- Security
- Availability
- Processing integrity
- Privacy
- Confidentiality

This certification reflects our ongoing commitment to robust data protection practices and transparent service delivery.

_Audit reports available to customers under NDA._

## SOC 3

Our SOC 3 certification provides independent validation of Workato's controls based on the same AICPA Trust Services Criteria as SOC 2:

- Security
- Availability
- Processing integrity
- Privacy
- Confidentiality

These controls ensure that integrations and data are managed securely and reliably. Unlike SOC 2, the SOC 3 audit report doesn't disclose specific testing details or controls, making it publicly available without an NDA.

_Audit reports available upon request._

## HIPAA

As a Business Associate, Workato is compliant with HIPAA standards, safeguarding Protected Health Information (PHI) for customers in healthcare. We can sign Business Associate Agreements (BAA) and undergo an annual HIPAA attestation from an independent auditing firm.

## IRAP

Workato has successfully completed an IRAP (Information Security Registered Assessors Program) assessment, which demonstrates compliance with the Australian government's ISM (Information Security Manual) at the PROTECTED level. This independent assessment confirms that Workato meets strict cybersecurity standards required for handling sensitive government data and delivering secure, trusted services.

## NIST 800-171A r2

Workato has successfully achieved attestation for compliance with NIST Special Publication 800-171A Revision 2. This independent assessment by a Certified Third-Party Assessment Organization (C3PAO) evaluated our cybersecurity practices and confirmed implementation of the required controls.

This attestation enables Workato to support federal contractors, partners, and subcontractors required to meet NIST standards for handling Controlled Unclassified Information (CUI), strengthening our role in the federal supply chain ecosystem.

_Attestation of Compliance (AoC) available upon request._

## More resources

Workato provides advanced security features to support highly regulated industries, enabling secure management of data, credentials, and integrations with the following security features:

- **[Enterprise Key Management](/en/security/data-protection/encryption-key-management/enterprise-key-management#enterprise-key-management)**: Customers can control their encryption keys, enhancing data security.
- **[External Secrets Management](/en/security/data-protection/secrets-management/secrets-management#secrets-management-for-connection-credentials)**: Integrate existing secret stores with Workato to strengthen credential management.
- **[Virtual Private Workato](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato)**: Deploy Workato in a dedicated AWS Virtual Private Cloud (VPC) for added data isolation and compliance.

---

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

---

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

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/encryption-key-management/guides/setting-up-amazon-key-management-service.md
description: >-
  Set up AWS Key Management Service with Workato Enterprise Key Management to
  bring your own encryption keys and meet compliance needs.
---

# Connect Amazon Key Management Service (KMS) to Workato EKM

Using Amazon Key Management Service (KMS) with [Workato Enterprise Key Management (EKM)](/en/security/data-protection/encryption-key-management/enterprise-key-management) allows you to bring your own encryption keys to Workato. In addition to meeting compliance and security requirements, you can view detailed activity logs in AWS KMS and stay informed of when and where you can access data.

This guide explains how to create a key in AWS KMS and configure EKM in Workato.

* * *

## Prerequisites

To perform the tasks in this guide, you'll need:

- **The following in Workato:**
  
  - An account with the [Enterprise Key Management](/en/security/data-protection/encryption-key-management/enterprise-key-management) feature enabled
  - A [user role](/en/roles) with the **Key management** privilege
- **The following in Amazon Web Services (AWS)**:
  
  - Permissions that allow you to create and update keys in AWS KMS. For more information, see [Permissions for creating KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-key-permissions).

* * *

## Step 1: Create and configure the key

- [Step 1.1: Retrieve the Workato key policy](#step-1-1)
- [Step 1.2: Configure the key in AWS](#step-1-2)
- [Step 1.3: Enable auto-rotation](#step-1-3)

### Step 1.1: Retrieve the Workato key policy

1. Sign in to Workato if you haven't already.
   
2. Go to **Workspace admin > Settings > Encryption keys**.
   
3. In the **How do you want to encrypt your data?** field, select **AWS KMS key** from the drop-down.
   
4. Click **Step 1** to access the key policy.
   
   ![The AWS Key policy on the Workato Key management settings page](/assets/aws-key-policy.BI5sVT-9.png)
   

You need this page to complete the next step.

### Step 1.2: Configure the key in AWS

Complete the following steps to configure a key in AWS:

> **NOTE**
> 
> While this tutorial explains how to create a new key, you can use an existing key.

1. Sign in to your AWS Management Console and open the [KMS console](https://console.aws.amazon.com/kms).
   
2. In the navigation pane, click **Customer managed keys**.
   
3. On the **Customer managed keys** page, click **Create key**.
   
4. On the **Step 1 - Configure key** page:
   
   1. Configure the following fields:
      
      - **Key type**: Select **Symmetric**. For more information about this key type, see the [AWS KMS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks).
      - **Advanced options > Key material origin**: Select **KMS**.
      
      ![The Configure key page in AWS KMS](/assets/aws-configure-key.Dz9zut7P.png)
      
   2. Click **Next**.
      
5. On the **Step 2 - Add labels** page:
   
   1. In the **Alias** field, enter a display name for the key.
      
   2. Configure other fields as needed.
      
   3. Click **Next**.
      
6. Proceed through the remaining steps in AWS, configuring fields as needed. Click **Next** to proceed to the next page.
   
7. When you reach the **Step 5 - Review** page:
   
   1. Return to the Workato workspace admin settings tab from [step 1.1](#step-1-1).
      
   2. Copy the contents of the **Permission to access key** field.
      
   3. In AWS, paste the contents into the `Statement` property of the default policy in the **Key policy** field.
      
      **Note**: If there are multiple objects in the `Statement` property you must keep, add commas (`,`) after all but the last object:
      
      Key policy with multiple Statement objects
      
      ```json
      {
          "Id": "key-consolepolicy-3",
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Sid": "Enable IAM User Permissions",
                  "Effect": "Allow",
                  "Principal": {
                      "AWS": "arn:aws:iam::TODO-ACCOUNTID:root"
                  },
                  "Action": "kms:*",
                  "Resource": "*"
              },	 /* Comma before next object */
              {
      	        "Sid": "Allow use of the key",
      	        "Effect": "Allow",
      	        "Principal": {
      	            "AWS": "arn:aws:iam::TODO - ACCOUNTID:role/Workato_EKM"
      	        },
      	        "Action": [
      	            "kms:Encrypt",
      	            "kms:Decrypt"
      	        ],
      	        "Resource": "*"
      	    }
          ]
      }
      ```
      
      Otherwise, the key policy is similar to the following:
      
      Key policy with a single Statement object
      
      ```json
      {
          "Id": "key-consolepolicy-3",
          "Version": "2012-10-17",
          "Statement": [
      	    {
      	        "Sid": "Allow use of the key",
      	        "Effect": "Allow",
      	        "Principal": {
      	            "AWS": "arn:aws:iam::TODO - ACCOUNTID:role/Workato_EKM"
      	        },
      	        "Action": [
      	            "kms:Encrypt",
      	            "kms:Decrypt"
      	        ],
      	        "Resource": "*"
      	    }
         ]
      }
      ```
      
   4. Click **Finish** to create the key.
      

### Step 1.3: Enable auto-rotation

Complete the following steps to enable auto-rotation:

> **NOTE**
> 
> Enabling [automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotating-keys-enable-disable) is a best practice, but not required.

1. Navigate to the **Customer managed keys** page.
   
2. Locate the key you created in the list and click to open.
   
3. Click the **Key rotation** tab.
   
4. Check the **Automatically rotate this KMS key every year** box:
   
   ![The Key rotation tab and enablement checkbox in the Key Details page of AWS](/assets/aws-auto-rotation.D6dyvpbm.png)
   
5. Click **Save**.
   

* * *

## Step 2: Add the key in Workato

- [Step 2.1: Retrieve the key ARN in AWS](#step-2-1)
- [Step 2.2: Set up the key in Workato](#step-2-2)

### Step 2.1: Retrieve the key ARN in AWS

1. Navigate to the **Customer managed keys** page, and click the key you created to open its details page.
   
2. On the key's details page, locate the **General configuration** section and the **ARN** field:
   
   ![Highlighted ARN field in the General Configuration section of the key details page in AWS](/assets/aws-arn.BoMtfI74.png)
   
3. Copy the ARN, as you'll need it to complete the next step.
   

### Step 2.2: Set up the key in Workato

1. Return to the **Workspace admin > Settings** tab.
   
2. Paste the ARN in the **Key ARN** field.
   
3. Click **Update key**.
   

* * *

## Troubleshoot key validation errors

If you encounter an error after clicking **Update key**, verify that:

- **You correctly added the key policy to the key in AWS KMS.** Verify that the [key policy](#step-1-2) is valid JSON and contained in the `Statement` property.
- **You pasted the correct key ARN into Workato.** Verify the [key ARN](#step-2-1) doesn't contain extra spaces or characters, and that you pasted the correct value into Workato.
- **AWS KMS isn't experiencing downtime.** If you've verified the key policy and ARN are correct, check the [AWS Health Dashboard](https://health.aws.amazon.com/health/status) for potential outages in KMS.

---

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

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/encryption-key-management/troubleshooting.md
description: >-
  Reference for Workato Enterprise Key Management errors, including causes,
  symptoms, and steps to resolve key management issues.
---

# Enterprise Key Management Troubleshooting

Need some help with [Enterprise Key Management (EKM)](/en/security/data-protection/encryption-key-management/enterprise-key-management)? This guide covers some common issues with EKM and how to troubleshoot them.

* * *

## Key Validation Failure

Workato is unable to validate the provided key.  
  
**Note:** If updating an existing key, data will remain encrypted until a new, valid key is provided.

<table style="display:table;" width="100%; fixed"><tbody><tr><td width="30%; fixed" style="background-color:#e4e8eb;vertical-align:top;"><strong>Error message</strong></td><td>Can't access the provided key</td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Applicable to</strong></td><td><span>AWS KMS, Custom keys</span></td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Occurs</strong></td><td><span>After clicking <strong>Update key</strong> in <strong>Workspace admin &gt; Settings &gt; Encryption keys</strong>.</span></td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Potential causes</strong></td><td><span>Workato is experiencing downtime; <strong>If using AWS KMS:</strong> <span>Insufficient permissions; Incorrect key configuration, such as using an asymmetric key type; Incorrect key ARN provided in Workato; AWS is experiencing downtime </span>; <strong>If using a custom key:</strong> <span>Invalid key format</span></span></td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Troubleshooting steps</strong></td><td><span>First, check if Workato is <a href="https://status.workato.com/?utm_source=docs.workato.com">experiencing downtime</a>. <strong>If using AWS KMS:</strong> <span>Verify that the key policy contains the <a href="/security/data-protection/encryption-key-management/guides/setting-up-amazon-key-management-service.html#step-1-2">required permissions.</a>, Verify that the key is <a href="/security/data-protection/encryption-key-management/guides/setting-up-amazon-key-management-service.html#step-1-2">correctly configured.</a>, Verify that the <a href="/security/data-protection/encryption-key-management/guides/setting-up-amazon-key-management-service.html#step-2-1">key ARN in Workato is correct.</a>, Verify that <a href="https://health.aws.amazon.com/health/status">AWS</a> isn't experiencing downtime. </span><strong>If using a custom key:</strong> <span>Verify that the key meets Workato's <a href="/security/data-protection/encryption-key-management/guides/setting-up-custom-kms-key.html#step-1">formatting requirements</a></span></span></td></tr></tbody></table>

* * *

## Data Encryption Failure

Workato was unable to successfully encrypt data using the provided key.

<table style="display:table;" width="100%; fixed"><tbody><tr><td width="30%; fixed" style="background-color:#e4e8eb;vertical-align:top;"><strong>Error message</strong></td><td>Data couldn't be encrypted with the provided key</td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Occurs</strong></td><td><span>After custom key material is uploaded in the <strong>Workspace admin &gt; Settings &gt; Encryption keys</strong> page.</span></td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Potential causes</strong></td><td><span>Custom key material doesn't meet Workato's formatting requirements.</span></td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Troubleshooting steps</strong></td><td><span>Verify that the key meets Workato's <a href="/security/data-protection/encryption-key-management/guides/setting-up-custom-kms-key.html#step-1">formatting requirements.</a></span></td></tr></tbody></table>

* * *

## Unavailable Key

Workato is unable to access the provided key. This can occur when Workato's access to the key is revoked or the key is deleted.  
  
**Note:** Data will remain encrypted when this occurs.

<table style="display:table;" width="100%; fixed"><tbody><tr><td width="30%; fixed" style="background-color:#e4e8eb;vertical-align:top;"><strong>Error message</strong></td><td>Can't access the provided key</td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Occurs</strong></td><td>When Workato's access to the key is revoked or the key is deleted</td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Symptoms</strong></td><td><span>Recipes failing to start or be tested, Recipes stopping after five consecutive trigger errors, Connection creation fails, Existing connections stop working, Job details page shows 'No data to show' message</span></td></tr><tr><td style="background-color:#e4e8eb;vertical-align:top;"><strong>Troubleshooting steps</strong></td><td><span><span><strong>If key access has been revoked</strong>, restore access if possible. Access to encrypted data and platform features (e.g., creating connections) will be restored.; <strong>If the key has been deleted</strong>, generate a new key and replace the existing key in Workato. You can also switch to using Workato KMS. <strong>Note</strong>: Data encrypted with the deleted key will become permanently inaccessible, including existing connections and jobs. Future data and platform features (e.g., creating connections, starting recipes) will become accessible.</span></span></td></tr></tbody></table>

---

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

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/secrets-management.md
description: >-
  Learn how external secrets management lets Workato store and retrieve
  connection credentials like passwords and API tokens from a secrets manager.
---

# Secrets management for connection credentials

To simplify the management of your connection credentials, you can use an external secrets manager to securely store and retrieve sensitive information like passwords and API tokens.

The External secrets management feature in Workato lets you use secrets in place of hardcoded connection credentials. Centralizing credential management can help you adopt security best practices, like password rotation, without manually updating credentials wherever they're in use.

In this guide, we discuss these topics:

- [How secrets management works](#how-it-works)
- [The secrets managers that Workato supports](#secrets-managers)
- [Using secrets to configure connections](#connection-configuration)
- [Workspace vs. Project level secrets management](#workspace-vs-project-secrets-management)

> **FEATURE AVAILABILITY**
> 
> External secrets management is available on specific pricing plans. Refer to your pricing plan and contract to learn more.

* * *

## How secret management works

With a secrets manager, you can use a **secret** instead of directly entering information into Workato. Secrets contain sensitive info like a password.

When you set up a connection, you need to manually retrieve and enter your credentials. Any time those credentials change - for example, when you reset your password - you'll need to update the password in every application that uses it.

However, if you use an external secrets manager instead, you'll only need to update the password in the secrets manager and refresh the connection in Workato. Applications using the reference will retrieve the secret's updated value, thus minimizing manual work, interruptions, and most importantly, security risk.

> **REFRESH THE CONNECTION IN WORKATO**
> 
> Refresh the connection by sending a request to the Workato API to [clear the secrets management cache](/en/workato-api/environment-management#clear-secrets-management-cache). This updates the connection with the latest credentials in your secrets manager. You do not need to disconnect and reconnect the connection.

At a high level, here's how using a secrets manager works with Workato for connection credential management:

1. You create a vault and secret in your external secrets manager. The secrets manager encrypts the credentials.
   
2. You grant Workato access to the secrets manager.
   
3. In Workato, you configure connections using the secrets instead of credentials.
   
   The following image demonstrates a Jira connection configured with a secret from Amazon Web Services (AWS) Secrets Manager:
   
   ![Jira connection in Workato configured with an AWS secret](/assets/workato-connection-example.CXvKENsX.png)
   
4. When Workato uses the connection, it performs the following tasks, in order:
   
   1. **Request secret**: Workato requests the secret from the secrets manager.
      
   2. **Retrieve and decrypt**: The secrets manager retrieves the secret and returns the decrypted secret value to Workato.
      
   3. **Authentication**: Workato uses the decrypted value to authenticate to the application.
      
   4. **Access**: If authentication is successful, the application grants access to Workato.
      

* * *

## Supported secrets managers

Workato's feature currently supports the following secrets managers:

- [AWS Secrets Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-aws-secrets-manager)
- [Azure Key Vault](/en/security/data-protection/secrets-management/setting-up-workspace-level-azure-key-vault)
- [CyberArk Conjur Secrets Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-cyberark-conjur)
- [Google Secret Manager](/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager)
- [HashiCorp Vault](/en/security/data-protection/secrets-management/setting-up-workspace-level-hashicorp-vault-secrets-engine)

* * *

## Using secrets to configure connections

How secrets are used in Workato connections depends on the type of secrets manager you're using. Refer to the guide for your secrets manager for more information:

- [Amazon Web Services (AWS) Secrets Manager](/en/security/data-protection/secrets-management/using-aws-secrets-in-connections)
- [Azure Key Vault](/en/security/data-protection/secrets-management/using-azure-key-vault-in-connections)
- [CyberArk Conjur Secrets Manager](/en/security/data-protection/secrets-management/using-cyberark-conjur-in-connections)
- [Google Secret Manager](/en/security/data-protection/secrets-management/using-google-secret-manager-in-connections)
- [HashiCorp Vault](/en/security/data-protection/secrets-management/using-hashicorp-secrets-in-connections)

* * *

## Workspace vs. Project secrets management

Typically, we configure secrets management for the entire workspace. If your organization requires more granular access control, you can configure it at the level of the individual projects. This enables you to specify the secrets inside the project, so that the connections in the projects can assume the role specified in the project settings.

For example, if your organization is configuring an S3 connection only for the use in your DevOps project, you can create a project-specific IAM role that has access to your S3 connection credentials. This replaces the generic IAM role that can be used by multiple projects.

> **INFO**
> 
> In Workato, secrets management can be used EITHER at the level of the Workspace, or at the level of Projects. We do not support a blended approach. For example, if you implement project-level secrets management for the DevOps project, you must change your secrets management protocol to project-level for ALL projects in the workspace.

* * *

## Formatting secrets

Certain types of secrets must be formatted correctly to be used in Workato. When adding secrets to your secrets manager, ensure you use the correct format.

### X.509 certificate

See the following X.509 certificate for an example of how to format an X.509 certificate in your secrets manager:

```
-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BA\nQEFAASCBKcwggSjAg\nxxxxxxxxxxxxxx\n-----END PRIVATE KEY-----\n
```

* * *

## Troubleshooting secrets manager connections

If you have configured a connection to use a secrets manager but the connection returns a `Permission denied` error, complete the following steps to troubleshoot the connection:

1. [Check credential validity](#step-1-check-credentials)
2. [Test retrieving secrets with provider API](#step-2-retrieve-secret)

### Check validity of credentials

Complete the following steps to check whether the credentials used to connect to your secrets manager are valid:

AWS SECRETS MANAGER

1. Log in to your AWS account.
   
2. Navigate to **IAM > Roles** and select the IAM role you assigned to Workato's Secrets Management feature.
   
3. Select the **Permissions** tab.
   
4. Ensure that the IAM policy attached to the role has the following permissions:
   
   - `ListSecrets`
   - `GetSecretValue`

HASHICORP VAULT

1. Use the [HashiCorp Vault CLI](https://developer.hashicorp.com/vault/docs/commands) to run the following [command](https://developer.hashicorp.com/vault/docs/commands/read) to check the ACL policy attached to the [AppRole](https://developer.hashicorp.com/vault/docs/auth/approle). Substitute your own values for `{approle-name}` and `{role-name}`:
   
   ```
   vault read auth/{approle-name}/role/{role-name}
   ```
   
   For example:
   
   ```
   vault read auth/workato_approle/role/workato
   ```
   
   The CLI output includes the name of the token policy attached to the AppRole.
   
2. Log in to the HashiCorp Vault UI.
   
3. Navigate to **ACL Policies** and select the policy name that the HashiCorp Vault CLI returned.
   
4. Ensure that the selected policy has the `read` and `list` capabilities for the appropriate secrets engine stored in your vault cluster.
   
5. Select the secrets engine in the Vault UI and navigate to the **Configuration** tab.
   
6. Ensure that the engine **Path** matches the `path` in the CLI output.
   

AZURE KEY VAULT

1. Log in to the Azure Portal.
   
2. Navigate to **Key Vault > Access control (IAM) > Role assignments**.
   
3. Ensure that the Service Principal you generated the `clientSecret` for holds the **Key Vault Secrets User** role.
   
4. Navigate to **Microsoft Entra ID > App Registrations** and select the app that you assigned the **Key Vault Secrets User** role to.
   
5. Navigate to **Certificates & Secrets** and ensure that the secret used in your Azure Key Vault connection is not expired.
   

GOOGLE SECRET MANAGER

1. Sign in to the [Google Cloud Console](https://console.cloud.google.com/) and select your project.
   
2. Go to **IAM & Admin > IAM**.
   
3. Locate the service account used by Workato and confirm it has the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) role assigned.
   
4. Go to **IAM & Admin > Service Accounts** and select the service account.
   
5. Open the **Keys** tab and confirm the key used in your Workato connection exists and has not been deleted or disabled.
   

### Test retrieving secrets with provider API

If the permissions you checked in [Step 1](#step-1-check-credentials) are still valid, use an API client such as Postman or curl to make an API call to your secrets manager to retrieve any secret. This should offer more insight about why your secrets manager connection is failing.

To make an API call to your secrets manager, refer to the following documentation:

- [AWS Secrets Manager API operations](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_Operations.html)
- [Azure Key Vault secret operations](https://learn.microsoft.com/en-us/rest/api/keyvault/#secret-operations-key-vault-only)
- [Google Secret Manager API operations](https://cloud.google.com/secret-manager/docs/reference/rest)
- [HashiCorp Vault API operations](https://developer.hashicorp.com/vault/api-docs#api-operations)

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-workspace-level-aws-secrets-manager.md
description: >-
  Set up AWS Secrets Manager at the workspace level to manage connection
  credentials for your Workato account from one secrets manager.
---

# Set up AWS Secrets Manager for workspaces

This guide explains how to configure secrets management for your Workato account at the workspace level using AWS Secrets Manager.

> **WARNING**
> 
> Switching to workspace-specific secrets management causes all previously-configured external secret references to stop working.
> 
> Ensure that the IAM role in Workato provides access using the workspace-level external ID, so all secrets currently in use continue working.

After your AWS Secrets Manager successfully connects to Workato, you can start using [secrets when configuring connections](/en/security/data-protection/secrets-management/using-aws-secrets-in-connections).

## Prerequisites

To complete the steps in this guide, you must have the following:

- Permissions that allow you to create and modify IAM permissions policies
- Permissions that allow you to create and modify IAM roles

## Select the scope for secrets management

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > External secrets manager**.
   
3. Click the **Use external secrets manager** toggle.
   
4. Select the **Set up secrets for the entire workspace** option from the **Scope** drop-down menu.
   
   ![Set up secrets for the entire workspace](/assets/secrets-management-scope-workspace.B_tXR5z3.png)_Set up secrets for the entire workspace_
   

## Select the secrets manager

1. In the **Which secrets manager do you want to use?** field, select **AWS Secrets Manager**.
   
   ![Choosing AWS workspace secrets manager](/assets/secrets-management-scope-workspace-aws.BkHbiv6v.png)
   
2. Workato displays guides for the next steps in the process:
   
   - Create a new permission policy and role in AWS
   - Add the role to your Workato account
   
   ![Next steps in Workato](/assets/secrets-management-scope-workspace-guides.Bv0xGsGP.png)
   

## Select the AWS Account ID and external ID

1. In the **Create a new permission policy and role in AWS** guide detail, Workato displays the IAM details. Note them to use in the following steps:
   
   - AWS Account ID
   - Copy the **AWS Account ID** for use in the ongoing secrets manager configuration.
   - External ID
   - Copy the **External ID** for use in the ongoing secrets manager configuration. The value should be in the format `workato_iam_external_id_wwwww`, where `wwwww` is the ID of the workspace.
   
   ![ID values for AWS workspace secrets manager](/assets/secrets-management-scope-workspace-aws-ids.Dae7KDQE.png)
   

## Create IAM role and ARN retrieval

Refer to the [IAM role-based authentication for AWS](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws) page for instructions on how to create an IAM role for Workato, create an IAM permissions policy, and retrieve your Amazon resource name (ARN).

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-project-level-aws-secrets-manager.md
description: >-
  Set up AWS Secrets Manager at the project level to scope connection
  credentials and IAM roles to individual Workato projects.
---

# Set up AWS Secrets Manager for projects

As an alternative to an individual secret for each user, you can manage access at the level of the project.

You must change secrets manager settings so that connections in the project can use the specified role in the project settings. Customers can then create project-specific IAM roles to limit the use of secrets to connections within the project.

> **WARNING**
> 
> Switching to project-specific secrets management causes all previously configured external secrets references to stop working. Projects that use secrets stored in AWS Secrets Manager must be set up individually in Project settings.

> **INFO**
> 
> In the example used in this article, we chose to demonstrate a simple example of configuring the AWS external role ID **without** changing the IAM permissions policy.
> 
> If your organization requires different roles scoped to different access permissions, we recommend that you configure these new permissions by setting the scope to specific secret resources. This enables you to have more granular control over which connection credentials to use in each project.

After your AWS Secrets Manager successfully connects to Workato, you can start using [secrets when configuring connections](/en/security/data-protection/secrets-management/using-aws-secrets-in-connections).

* * *

## Prerequisites

To complete the steps in this guide, you must have the following:

- Permissions that allow you to create and modify IAM permissions policies
- Permissions that allow you to create and modify IAM roles

## Select the scope for secrets management

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > External secrets manager**.
   
3. Click the **Use external secrets manager** toggle.
   
4. Select the **Set up secrets management for each project individually** option from the **Scope** drop-down menu.
   
   ![Workato secrets management, selecting project scope](/assets/secrets-management-scope-project.d-05a3me.png)
   
5. Click **Save**.
   
6. If you switch secrets management scopes, Workato notifies you that existing external secret references scoped to the project level will no longer function.
   
   To proceed with switching from workspace-level to project-level secrets management, select the checkbox to acknowledge the impact and click **Use project-specific secrets**.
   
   ![Workato secrets management, confirm project level](/assets/secrets-management-scope-project-confirm.Dnrb3Ljn.png)
   

Note that you must now set up secrets in each project individually.

## Select the project

1. Go to **Projects** and select the project that you plan to configure with secrets management.
   
2. Click **Settings**, then click **Secrets management**.
   
   ![Secrets management interface of a project](/assets/secrets-management-project-settings.Ci4qsd4F.png)
   
3. Click the **Use external secrets manager** toggle.
   
4. Select the **AWS Secrets Manager** option from the **Which secrets manager do you want to use?** drop-down menu.
   
5. Choose a guide for next steps in the process:
   
   - Create a new permission policy and role in AWS
   - Add the role to your Workato account
   
   ![Next steps in Workato](/assets/secrets-management-scope-project-guides.CncBZMXu.png)
   

## Select the AWS Account ID and external ID

1. In the **Create a new permission policy and role in AWS** guide detail, Workato displays the IAM details. Note them to use in the following steps:
   
   <dl><dt>AWS Account ID</dt><dd>Copy the <strong>AWS Account ID</strong> value, to use in ongoing configuration of the secrets manager.</dd><dt>External ID for ProjectName</dt><dd>Copy the value, to use in ongoing configuration of the secrets manager.</dd><dd>Here, we configure access to the project <strong>WorkatoDB_Project1</strong>.</dd><dd>The value should be of the form <code>workato_iam_external_id__</code>, where <code></code>is the ID of the Workato workspace, and <code></code>is the ID of the project.</dd></dl>
   
   ![ID values for AWS project secrets manager](/assets/secrets-management-scope-project-aws-ids.PZMTUT_q.png)
   

## Create an AWS IAM role for your Workato project

Refer to the [IAM role-based authentication for AWS](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws) for instructions on how to create an IAM role for Workato and an IAM permissions policy (if needed).

## Retrieve and add the role ARN in Workato

You must complete the following steps to finalize the setup:

- [Step 5.1: Retrieve the role ARN in AWS](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#retrieve-iam-role-arn)
- [Step 5.2: Add the role ARN in Workato](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#add-the-role-arn-in-workato)

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/using-aws-secrets-in-connections.md
description: >-
  Configure Workato connections using secrets stored in your AWS Secrets Manager
  vault, with workspace-level or project-level connections.
---

# Use AWS Secrets Manager in connections

Video guide: Set up connections safely with AWS Secrets Manager

[Video](https://www.youtube.com/embed/_Za-IzViAtk)

This guide explains how to use secrets from your Amazon Web Services (AWS) Secrets Manager vault to configure Workato connections.

## Prerequisites

To complete the steps in this guide, you must have the following prerequisites:

- **In Workato**:
  
  - A successful AWS Secrets Manager [workspace-level](/en/security/data-protection/secrets-management/setting-up-workspace-level-aws-secrets-manager) or [project-level](/en/security/data-protection/secrets-management/setting-up-project-level-aws-secrets-manager) connection.
  - A [user role](/en/roles) with **Create** and **Edit Connections** privileges.
- **In Amazon Web Services (AWS)**:
  
  - An existing secret in **JSON key/value pair** format. Workato doesn't support plaintext secrets. Refer to the AWS documentation for more information on how to [create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html).
  - Permissions that allow you to view secrets in AWS Secrets Manager.

## Retrieve the secret's details from AWS

Complete the following steps to retrieve the secret's details from AWS:

1. Sign in to your AWS Management Console and open the [Secrets Manager console](https://console.aws.amazon.com/secretsmanager).
   
2. In the navigation pane, click **Secrets**.
   
3. Click the secret you plan to use in Workato.
   
4. Copy and store the **Secret name** and **Secret ARN** securely. These values are required to configure the external secret in Workato.
   
   ![Highlighted secret name and ARN in AWS Secrets Manager](/assets/aws-secret-name-arn.43gEY7Lm.png)
   

## Configure a Workato connection

Complete the following steps to configure a connection in Workato using AWS Secrets Manager:

1. Create a new connection or open the configuration page for an existing connection in your Workato account.
   
2. Click or hover over the input field that requires an external secret, then click **\+ Add external secret**.
   
3. Enter the **Key name** and **Secret ARN** in the **Add external secret** dialog.
   
   ![Add AWS external secret](/assets/add-external-secret-aws.BWQsU5qc.png)_Add external secret_
   
4. Click **Done**. The secret appears as a masked datapill in the input field on the connection page.
   
   Select the datapill to edit the secret.
   
5. Click **Connect** and verify that this connection works.
   

If you prefer to add the secret with a secret mask, follow this syntax for the secrets used in Workato connection credentials:

```txt
{{workato:sm:<key name>:<secret ARN>}}
```

  

- `<key name>`
  
- Refers to the specific key name within a secret, not the secret name itself. For example, in a secret named `jira`, there may be a key/value pair where `prod.jira.secret.key` is the key name, and its value is the actual personal access token.
  
- `<secret ARN>`
  
- The Amazon Resource Name (ARN) for the secret in AWS Secrets Manager. For example:
  
  ```txt
  {{workato:sm:prod.jira.secret.key:arn:aws:secretsmanager:us-east-1:137149879143:secret:prod-jira-credentials-FsmeTs}}
  ```
  

In this example, `prod.jira.secret.key` is the key name in a secret named `jira`, and `arn:aws:secretsmanager:us-east-1:137149879143:secret:prod-jira-credentials-FsmeTs` is the `secret ARN`.

In the connection's configuration page, paste this entire value into the appropriate field. The following image shows a secret being used as the **Custom Service client secret** value in a Jira connection:

![JIRA connection in Workato configured with an AWS secret](/assets/workato-connection-example-updated.D_51gLvx.png)

## Complete your connection setup

Select **Connect** to authorize and complete your connection setup.

## Secrets cache behavior

Workato caches credentials retrieved from AWS Secrets Manager for **60 minutes**. During this period, recipes continue to use the cached value, even if you update or rotate the secret.

After the cache expires, the next recipe execution retrieves the latest value from AWS Secrets Manager. You can call the [Clear secrets management cache](/en/workato-api/environment-management#clear-secrets-management-cache) endpoint to apply changes immediately. This forces Workato to fetch the latest credentials without requiring you to disconnect and reconnect the connection.

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws.md
description: >-
  Use IAM role-based authentication to grant Workato scoped access to AWS
  services without sharing AWS security credentials.
---

# Use IAM role-based authentication for AWS Services

AWS IAM role authentication allows you to provide a dedicated role in your AWS instance for Workato to use. By provisioning a dedicated IAM profile, the owner of the AWS instance can grant Workato access to AWS resources without sharing AWS security credentials. This also helps to maintain permission boundaries, including controlled access to specific AWS services and actions that are permitted by the third-party application (for example, Workato). When configuring connections using IAM role-based authentication, the external ID's used can be scoped to either the **workspace or project level**.

Configuring the IAM role using external ID's scoped at the project level allows you to give individual projects more granular access to your AWS resources. For example, only allowing Amazon SQS access to your "DevOps" project instead of being accessible to all projects in your workspace.

## Supported connectors

We support IAM role-based authentication for the following AWS Services and universal connectors:

- Amazon Lex
- Amazon S3
- Amazon SES
- AWS Lambda
- AWS SQS
- AWS SNS
- Cloud Watch
- HTTP Universal Connector

## Prerequisites

You must have the following:

- **In Amazon Web Services (AWS)**:
  - Permissions that allow you to create and modify IAM permissions policies
  - Permissions that allow you to create and modify IAM roles

## Select the scope of IAM External ID

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > Amazon Web Services IAM**.
   
3. Use the **External ID scope** drop-down menu to select either **Single external ID for the workspace** or **Separate external ID for each project**.
   
   ![External scope for AWS access](/assets/secrets-management-aws-external-id-scope.DdWVuZbJ.png)_External scope_
   
   If you have existing connection credentials that use the workspace’s external ID, Workato prompts you to confirm your selection by displaying a list of active connections for which you must update the IAM roles. The reverse is true if you are switching from multiple project-level external ID's to a single external ID for the workspace.
   
   ![Confirm separate external IDs](/assets/secrets-management-aws-external-id-scope-confirm.CxmGbkXh.png)_Confirm external ID selection_
   
4. Click **Use separate external IDs** or **Use single external ID** to confirm your selection.
   

## Create an IAM role

To create an IAM role:

1. Navigate to the **AWS Console** and select **Security Credentials**.
   
   ![Security Credentials](/assets/security-credentials.-AMZzedD.png)_Security credentials_
   
2. Select **Roles > Create role**.
   
   ![Create role](/assets/create-role.CAwa2HEZ.png)_Create role_
   
3. Select **AWS account** under **Trusted entity type**.
   
4. Select **Another AWS account** and enter the **Workato AWS account ID**: `353360065216`.
   
5. Select the **Require external ID** check box and provide the Workato-generated **External ID**.
   
   - Every Workato user will have a unique **External ID** (for example, `workato-user-84762`). If you would like more granular control of how AWS is used in Workato, you may choose to configure the connection at the project level by changing the scope of the external ID. Refer to [secrets management](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws) for more information.
   
   ![Amazon Account ID](/assets/aws-account.Du3fyxDX.png)_Amazon account ID_
   
   FIND YOUR WORKATO EXTERNAL ID
   
   To find the external ID in Workato:
   
   1. Sign in to Workato.
      
   2. Go to **Workspace admin > Settings > Amazon Web Services IAM**.
      
   
   If you have switched the scope of external IDs from workspace level to project level or vice versa, you are required to update the external IDs for the role in order for your AWS connection in Workato to be valid. You may do so by selecting "Trust relationships" and changing the value of the accepted external ID. For example, replacing the external ID value from `workato_iam_external_id_12345` to a project level scoped external ID like `workato_iam_external_id_12345_6789`.
   
6. Select appropriate permissions for Workato to run automated workflows in your account.
   
7. Provide a **Role name** and **Description** for the IAM role.
   
   - Workato recommends that role name avoids using a non-guessable `resource-id` in the ARN and does not include the external ID.
8. Optional. At the **Select trusted entities** step, click **Edit** to add or edit policies for trusted entities.
   
9. Optional. At the **Add permissions** step, click **Edit** to add or edit permissions.
   
10. Optional. If you are using object tags, select an appropriate tag for this IAM role.
    
    ![Review and create](/assets/name-review-create.D0pP8MDc.png)_Review and create role_
    
11. Click **Create role**.
    

## Create an IAM permissions policy

1. Navigate to the **AWS Console** and open the [IAM console](https://console.aws.amazon.com/iam).
   
2. Select **Access management > Policies**.
   
3. Click **Create Policy**.
   
4. Find and select the AWS service that you plan to allow Workato to access.
   
5. Select the necessary permissions in the **Actions** field.
   
6. Specify the resources to which you plan to allow the role access to.
   
   > **BEST PRACTICE**
   > 
   > Workato recommends that you grant access to specific resources. Refer to [Amazon's documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) for more info about using condition keys to accomplish granting minimal permissions.
   > 
   > The page should look similar to the following:
   > 
   > ![Configured IAM access policy in the AWS Create Policy screen](/assets/aws-sqs-trust-policy.D0Re2X5f.png)
   
7. Click **Next** until you reach the **Review policy** page.
   
8. Enter the **Name** for the policy.
   
9. Click **Create policy** when finished.
   

## Retrieve IAM role ARN

To retrieve the **Role ARN** required for the connection setup:

1. Navigate to the **AWS Console > My Security Credentials > Roles**.
   
   ![Security Credentials](/assets/security-credentials.-AMZzedD.png)_Security credentials_
   
2. Use the search box to locate the IAM role with ARN you plan to use for the connection and then select the role to view the summary.
   
   ![Select IAM role](/assets/select-iam-role.CkEg9D9j.png)_Select IAM role_
   
3. Copy the **Role ARN**. You must use this in the connection setup when creating an Amazon connection in Workato.
   
   ![Copy role ARN](/assets/copy-arn.DgXJ_K95.png)_Copy role ARN_
   

### Add the Role ARN in Workato

1. Sign in to Workato.
   
2. Go the **Connections** tab and click **Create > Connection** or press C twice.
   
3. Search for and select a [supported connector](#supported-connectors) on the **New connection** page.
   
4. Enter a name for your connection in the **Connection name** field.
   
5. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
6. Select **IAM role** from the **Authorization type** drop-down menu.
   
7. Paste the ARN value in the **IAM Role ARN** field and complete any other required fields for the AWS service, for example **Region**.
   
   ![Add Role ARN to Workato](/assets/add-arn.DWHH2dy3.png)
   
8. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-workspace-level-azure-key-vault.md
description: >-
  Set up Azure Key Vault for workspace-level secrets management to manage
  connection credentials across your Workato account.
---

# Set up Azure Key Vault for workspace-level secrets management

Switching to workspace-specific secrets management causes external secrets references scoped to the project level to stop working.

## Prerequisites

To complete the steps in this guide, you must have the following:

- An existing [key vault](https://azure.microsoft.com/en-us/products/key-vault/).
- A [registered application](/en/security/data-protection/secrets-management/azure-key-vault-app-registration) with an appropriate role policy assigned:
  - For key vaults using [role-based access control (RBAC)](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide?tabs=azure-cli), the registered app must have the **Key Vault Secrets User** role.
  - For key vaults using [access policies](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal), the registered app must have the **Get** secret permission.

> **REGISTERING AN APPLICATION**
> 
> To learn how to register an application, see [Registering an application with Microsoft Entra ID](/en/security/data-protection/secrets-management/azure-key-vault-app-registration).

## Select the scope for secrets management

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > External secrets manager**.
   
3. Select the **Set up secrets for the entire workspace** option from the **Scope** drop-down menu.
   
   ![Set up secrets for the entire workspace](/assets/secrets-management-scope-workspace.B_tXR5z3.png)_Set up secrets for the entire workspace_
   

## Select the secrets manager

1. In the **Which secrets manager do you want to use?** field, select **Azure Key Vault**.
   
   ![Secrets management interface of a workspace](/assets/azure-key-vault-select-akv-workspace.BWCJ2J9p.png)_Secrets management interface of a workspace_
   
2. Click **Set up connection**.
   
3. In the **Connect to Azure Key Vault** modal, select **\+ Create a new connection**.
   
   ![Create a new Azure Key Vault connection](/assets/azure-key-vault-select-connection.DE_prRmn.png)_Create a new Azure Key Vault connection_
   

## Connect to Azure Key Vault

![Configure Azure Key Vault connection](/assets/azure-key-vault-connect.Dlx1jFQ0.png)_Configure Azure Key Vault connection_

1. - Connection name
   - Name your Azure Key Vault connection.
2. - Location
   - Select the project or folder to store your Azure Key Vault connection.
3. - Connection type
   - Specify whether this is a cloud or [on-prem connection](/en/on-prem/agents/connection). If you're connecting to an on-prem Azure Key Vault instance, select the appropriate on-prem group from the drop-down menu.
4. - Vault URL
   - Provide the URL of your key vault. Obtain this value by navigating to [**Azure portal > Key vaults**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.KeyVault%2Fvaults). Select the desired key vault and copy the **Vault URI** shown in the **Overview**. In our example, we connect to the vault URL `https://example.vault.azure.net/`.
5. - Tenant ID
   - Provide the ID of the tenant where your key vault and app registration are located. Azure refers to this as the **Directory (tenant) ID**. Obtain this value by navigating to [**Azure portal > App registrations**](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps). Select your [registered application](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#step-1) and copy the **Directory (tenant) ID** shown in the **Overview**.
6. - Client ID
   - Provide your client ID, which Azure refers to as the **Application (client) ID**. Obtain this value by navigating to [**Azure portal > App registrations**](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps). Select your [registered application](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#step-1) and copy the **Application (client) ID** shown in the **Overview**.
7. - Client Secret
   - Provide your client secret, which Azure refers to as the secret **Value**. Azure only displays this value when the secret is generated. If you need to generate a new secret, see [Registering an application with Microsoft Entra ID, Step 2](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#step-2).
8. Click **Connect**. Workato displays the name of the Azure Key Vault connection:
   
   ![Connection successful](/assets/azure-key-vault-workspace-connected.Xiva0kuv.png)_Connection successful_
   
9. Click **Save**.
   
10. If you switch secrets management scopes, Workato notifies you that existing external secret references scoped to the project level will no longer function.
    
    To proceed with switching from project-level to workspace-level secrets management, select the checkbox to acknowledge the impact and click **Use workspace-level secrets**.
    
    ![Use workspace-level secrets](/assets/azure-key-vault-use-workspace-specific-secrets.C1s2lr7h.png)_Use workspace-level secrets_
    

> **FURTHER READING**
> 
> - [Using Azure Key Vault secrets to authenticate to connections](/en/security/data-protection/secrets-management/using-azure-key-vault-in-connections)

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-project-level-azure-key-vault.md
description: >-
  Set up Azure Key Vault for project-level secrets management to scope
  connection credentials to individual Workato projects.
---

# Set up Azure Key Vault for project-level secrets management

Switching to project-specific secrets management causes external secrets references scoped to the workspace level to stop working.

## Prerequisites

To complete the steps in this guide, you must have the following:

- An existing [key vault](https://azure.microsoft.com/en-us/products/key-vault/).
- A [registered application](/en/security/data-protection/secrets-management/azure-key-vault-app-registration) with an appropriate role policy assigned:
  - For key vaults using [role-based access control (RBAC)](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide?tabs=azure-cli), the registered app must have the **Key Vault Secrets User** role.
  - For key vaults using [access policies](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal), the registered app must have the **Get** secret permission.

> **REGISTERING AN APPLICATION**
> 
> To learn how to register an application, see [Registering an application with Microsoft Entra ID](/en/security/data-protection/secrets-management/azure-key-vault-app-registration).

## Select the scope for secrets management

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > External secrets manager**.
   
3. Click the **Use external secrets manager** toggle.
   
4. Select the **Set up secrets management for each project individually** option from the **Scope** drop-down menu.
   
   ![Set up secrets management for each project individually](/assets/secrets-management-scope-project.d-05a3me.png)_Set up secrets management for each project individually_
   
5. Click **Save**.
   
6. If you switch secrets management scopes, Workato notifies you that existing external secret references scoped to the project level will no longer function.
   
   To proceed with switching from workspace-level to project-level secrets management, select the checkbox to acknowledge the impact and click **Use project-specific secrets**.
   
   ![Use project-specific secrets](/assets/azure-key-vault-use-project-specific-secrets.g38BqQ-T.png)_Use project-specific secrets_
   

## Select the project

1. In Workato, navigate to your projects.
   
2. Select the project that you plan to configure with secrets management.
   
3. In the project, go to **Workspace admin > Settings > External secrets manager**.
   
4. In the **Which secrets manager do you want to use?** field, select **Azure Key Vault**.
   
   ![Secrets management interface of a project](/assets/azure-key-vault-select-akv-projects.B-0kimKE.png)_Secrets management interface of a project_
   
5. Click **Set up connection**.
   
6. In the **Connect to Azure Key Vault** modal, select **\+ Create a new connection**.
   
   ![Create a new Azure Key Vault connection](/assets/azure-key-vault-select-connection.DE_prRmn.png)_Create a new Azure Key Vault connection_
   

## Connect to Azure Key Vault

![Configure Azure Key Vault connection](/assets/azure-key-vault-connect.Dlx1jFQ0.png)_Configure Azure Key Vault connection_

1. - Connection name
   - Name your Azure Key Vault connection.
2. - Location
   - Select the project or folder to store your Azure Key Vault connection.
3. - Connection type
   - Specify whether this is a cloud or [on-prem connection](/en/on-prem/agents/connection). If you're connecting to an on-prem Azure Key Vault instance, select the appropriate on-prem group from the drop-down menu.
4. - Vault URL
   - Provide the URL of your key vault. Obtain this value by navigating to [**Azure portal > Key vaults**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.KeyVault%2Fvaults). Select the desired key vault and copy the **Vault URI** shown in the **Overview**. In our example, we connect to the vault URL `https://example.vault.azure.net/`.
5. - Tenant ID
   - Provide the ID of the tenant where your key vault and app registration are located. Azure refers to this as the **Directory (tenant) ID**. Obtain this value by navigating to [**Azure portal > App registrations**](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps). Select your [registered application](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#step-1) and copy the **Directory (tenant) ID** shown in the **Overview**.
6. - Client ID
   - Provide your client ID, which Azure refers to as the **Application (client) ID**. Obtain this value by navigating to [**Azure portal > App registrations**](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps). Select your [registered application](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#step-1) and copy the **Application (client) ID** shown in the **Overview**.
7. - Client Secret
   - Provide your client secret, which Azure refers to as the secret **Value**. Azure only displays this value when the secret is generated. If you need to generate a new secret, see [Registering an application with Microsoft Entra ID, Step 2](/en/security/data-protection/secrets-management/azure-key-vault-app-registration#step-2).
8. Click **Connect**. Workato displays the name of the Azure Key Vault connection:
   
   ![Connection successful](/assets/azure-key-vault-projects-connected.DowFQuP8.png)_Connection successful_
   
9. Click **Save changes**.
   

> **FURTHER READING**
> 
> - [Using Azure Key Vault secrets to authenticate to connections](/en/security/data-protection/secrets-management/using-azure-key-vault-in-connections)

---

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

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/azure-key-vault-app-registration.md
description: >-
  Register an application in the Microsoft Entra admin center so Workato can
  retrieve secrets from your Azure Key Vault on your behalf.
---

# Register an Azure Key Vault app in Microsoft Entra ID

Before you can connect your [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/) to Workato, you must [register an application](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application) in the Microsoft Entra admin center.

Registering this [application](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals?tabs=browser#application-registration) and giving it the appropriate permissions enables Workato to retrieve secrets from your key vault on your behalf.

To register the application, complete the following steps:

1. [Create the app registration](#step-1)
2. [Create the client secret](#step-2)
3. [Grant permissions to the app](#step-3)

> **HAVE AN EXISTING SAML-BASED APPLICATION?**
> 
> If you have already registered a [SAML-based application](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/add-application-portal-setup-sso) that lets your users sign in to Workato with SAML SSO, you can use it to set up Workato's [Azure Key Vault connection](/en/security/data-protection/secrets-management/setting-up-project-level-azure-key-vault). When you configure the connector, simply enter your existing app's client ID and [generate a new secret](#step-2). Make sure the application also has the [required permissions](#step-3).

## Create the app registration

1. Sign in to the Azure portal and go to [App registrations](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps).
   
2. Select **\+ New registration**.
   
3. Name your application. This is the user-facing display name for this application, such as `workato-akv`. Microsoft allows you to change this name later.
   
4. In **Supported account types**, select **Accounts in this organizational directory only (Default Directory only - Single tenant)**.
   
5. Leave the **Redirect URI** field blank and select the **Register** button.
   
6. The next page displays an overview of the newly created app. Copy and store the **Application (client) ID** and the **Directory (tenant) ID**. You will need these values later to authenticate in Workato.
   
   ![App registration overview](/assets/azure-key-vault-app-registration-overview.CsUtBIaR.png)_App registration overview_
   

## Create the client secret

1. From the overview of your app registration, select **Certificates & secrets** in the left navigation sidebar.
   
2. On the **Client secrets** tab, select **\+ New client secret**.
   
3. In the **Description** field, enter a description for the client secret, such as `workatoAzureKeyVault`.
   
4. In the **Expires** field, select when the secret should expire. The default is after 180 days.
   
5. Select **Add**.
   
6. The Azure portal displays the new secret value and ID. Copy the **Value**.
   
   > **WARNING**
   > 
   > The secret value is only shown once. Make sure you copy it before leaving the page.
   
   ![Copy the secret value](/assets/azure-key-vault-copy-secret-value.Deh-MX9U.png)_Copy the secret value_
   

## Grant permissions to the app

Next, you must give the registered app permission to retrieve secrets from your key vault on Workato's behalf.

Azure offers two ways to grant permission to access key vaults:

- [Role-based access control (RBAC)](#rbac)
- [Access policies](#access-policy)

To see which model your key vault uses, navigate to **Key vaults > {key vault name} > Access configuration**.

### RBAC

If your key vault uses the [RBAC permission model](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide?tabs=azure-cli), you must assign the **Key Vault Secrets User** role to the registered application.

1. Navigate to **Key vaults > {key vault name} > Access control (IAM)**.
   
2. Select **Add > Add role assignment**.
   
3. Select the **Key Vault Secrets User** role and select **Next**.
   
4. In the **Assign access to** field, select **User, group, or service principal**.
   
5. In the **Members** field, choose **Select members** and search for the name of your registered application. When the application appears in the list, click the application name and choose **Select**.
   
6. Select **Next**.
   
7. In the **Review + assign** tab, select **Review and assign**.
   

### Access policy

If your key vault uses the [access policy permission model](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal), you must assign the **Get** secret permission to the registered application.

1. Navigate to **Key vaults > {key vault name} > Access policies**.
   
2. Select **Create**.
   
3. In the **Permissions** tab, select **Get** in the **Secret permissions** column, then select **Next**.
   
4. In the **Principal** tab, search for the name of the registered app. When the application appears in the list, select the application name and then select **Next**.
   
5. In the **Application (optional)** tab, select **Next**.
   
6. In the **Review + create** tab, select **Create**.
   

> **FURTHER READING**
> 
> - [Set up Azure Key Vault for workspaces](/en/security/data-protection/secrets-management/setting-up-workspace-level-azure-key-vault)
> - [Set up Azure Key Vault for projects](/en/security/data-protection/secrets-management/setting-up-project-level-azure-key-vault)

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-workspace-level-cyberark-conjur.md
description: >-
  Set up CyberArk Conjur for workspace-level secrets management to manage
  connection credentials across your Workato account.
---

# Set up CyberArk Conjur for workspace-level secrets management

Existing external secrets references that are scoped to the project level will stop working when you switch to workspace-specific secrets management.

* * *

> **FEATURE AVAILABILITY**
> 
> Secrets management is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.

* * *

## Conjur host configuration for Workato

Integration between Workato and Conjur is based on the host/workload API key authentication.

For Workato to retrieve a secret from your Conjur instance, an API authentication request is first sent to your Conjur server based on the parameters specified when configuring the CyberArk Conjur connector. If the credentials are valid, Conjur responds with a short-lived access token. Workato then uses this access token to retrieve the actual secret value stored in Conjur if the host has the necessary `execute` and `read` permissions.

Policies on Conjur are written as `.yml` files. Visit the CyberArk Conjur documentation for [policy best practices](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/policy-best-practices.htm). The following steps describe how to develop a policy file.

For more information on policy syntax operators, refer to the [CyberArk Conjur documentation](https://docs.cyberark.com/conjur-open-source/Latest/en/Content/Operations/Policy/policy-syntax.htm).

1. Declare a group at the root policy:
   
   ```yaml
   - !policy
     id: workato-app
     body:
       - !group workato-secret-users
   ```
   
2. Declare variables and assign the group `[read, execute]` permissions.
   
   This example creates the `sql-password-prod` and `sql-host-prod` variables which store the password for a SQL database as well as the host name:
   
   ```yaml
   - &variables
     - !variable
       id: sql-password-prod
       kind: password
     - !variable
       id: sql-host-prod
       kind: password
   - !permit
     role: !group /workato-app/workato-secret-users       # group declared earlier
     privileges: [read, execute]
     resources: *variables
   ```
   
3. Declare the host, a layer, and assign membership of the host into the layer:
   
   ```yaml
   - !host workato-us-prod-1
   - !layer workato-us-prod
   - !grant
        role: !layer workato-us-prod
        members:
           - !host workato-us-prod-1
   ```
   
   - [Host documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-host.htm)
   - [Layer documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-grant.htm)
4. Grant membership of the layer into the group:
   
   ```yaml
   - !grant
     role: !group workato-app/workato-secret-users
     member: !layer workato-app/ workato-us-prod
   ```
   
   - [Grant documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-grant.htm)
5. Create a new secret on Conjur:
   
   ```yaml
   - !variable
     id: ddog-api-key
     kind: password
   ```
   
   - [Variable documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-variable.htm)
6. Grant `execute` and `read` permissions to group on selected variables:
   
   ```yaml
   - !permit
     role: !group /workato-app/workato-secret-users     # layer declared earlier
     privileges: [read, execute]
     resources: !variable ddog-api-key
   ```
   
   - [Permit documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-permit.htm)

Expand for an example of a full policy

```yaml
- !policy
  id: workato-app-dev
  body:
    - !group workato-secrets-dev
    - &variables
        - !variable
            id: sql-password-prod
            kind: password
        - !variable
            id: sql-host-prod
            kind: password
    - !permit
        role: !group /workato-app-dev/workato-secrets-dev       # group declared earlier
        privileges: [read, execute]
        resources: *variables
    - !host workato-us-dev-1
    - !layer workato-us-dev
    - !grant
        role: !layer workato-us-dev
        members:
            - !host workato-us-dev-1
    - !grant
        role: !group workato-secrets-dev
        member: !layer workato-us-dev
```

To which the expected response would be:

```json
{
    "created_roles": {
        "workato:host:workato-app-dev/workato-us-dev-1": {
            "id": "workato:host:workato-app-dev/workato-us-dev-1",
            "api_key": "1q3ye3gxxxx"
        }
    },
    "version": 1
}
```

## Select the scope and set up CyberArk secrets management

1. Sign in to your Workato workspace.
   
2. Navigate to **Workspace admin > Settings > Security > External secrets manager**.
   
3. In **Scope**, select the option **Set up secrets management for the entire workspace**:
   
   ![Set up secrets management for the entire workspace](/assets/scope-workspace.Co0fyqQk.png)_Set up secrets management for the entire workspace_
   
4. In the **Which secrets manager do you want to use?** field, select **CyberArk Conjur**:
   
   ![Secrets management interface of a workspace](/assets/select-cyberark-conjur.CparkhRL.png)_Secrets management interface of a workspace_
   
5. Click **Set up connection**.
   
6. Configure the following fields in Workato:
   
   ![Configure CyberArk Conjur connection](/assets/setup.BJAAwE3z.png)_Configure CyberArk Conjur connection_
   
   - Connection name
     
   - Name your CyberArk Conjur connection.
     
   - Connection type
     
   - Workato supports both cloud and on-prem connection types. If you plan to use an on-prem group, select one from the drop-down.
     
   - Server URL
     
   - To connect to Conjur Cloud, the server URL must follow this format:
     
     ```html
     https://<subdomain>.secretsmgr.cyberark.cloud/api/
     ```
     
   - Organization account name
     
   - To connect to Conjur Cloud, input `conjur`.
     
   - Login ID
     
   - For host authentication, the ID must be prefixed with `host/`, for example: `host/workato-app/workato-user-1`.
     
   - API key
     
   - Conjur generates an API key for every user when the user resource is created. Learn more about generating an API key in [CyberArk Conjur's documentation](https://docs.cyberark.com/conjur-enterprise/latest/en/Content/Operations/Services/default_authn.htm).
     

## How to revoke access to secrets store on CyberArk Conjur

To revoke Workato's access to secrets stored on CyberArk Conjur, rotate the host's API key with a PUT request and ensure that the host ID is URL-encoded:

```shell
PUT {{conjurServer}}/authn/{{conjurOrganization}}/api_key?role=host:workato-conjur-demo/workato-us-2
```

Secrets are no longer accessible after sixty minutes.

To revoke access immediately, rotate the API key, then use the [clear\_cache](/en/workato-api/environment-management#clear-secrets-management-cache) API.

For more information, consult the Conjur documentation on [how to rotate host API keys](https://docs.cyberark.com/conjur-open-source/Latest/en/Content/Developer/Conjur_API_Rotate_Personal_API_Key.htm).

This process applies to both CyberArk Conjur Enterprise and CyberArk Conjur Open Source. Visit the [Cyberark Conjur Cloud-specific documentation](https://docs.cyberark.com/conjur-cloud/latest/en/Content/Developer/Conjur_API_Rotate_Other_API_Key.htm) for more information.

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-project-level-cyberark-conjur.md
description: >-
  Set up CyberArk Conjur for project-level secrets management to scope
  connection credentials to individual Workato projects.
---

# Set up CyberArk Conjur for project-level secrets management

Existing external secrets references that are scoped to the workspace level will stop working when you switch to project-specific secrets management.

* * *

> **FEATURE AVAILABILITY**
> 
> Secrets management is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Conjur host configuration for Workato

Integration between Workato and Conjur is based on the host/workload API key authentication.

For Workato to retrieve a secret from your Conjur instance, an API authentication request is first sent to your Conjur server based on the parameters specified when configuring the CyberArk Conjur connector. If the credentials are valid, Conjur responds with a short-lived access token. Workato then uses this access token to retrieve the actual secret value stored in Conjur if the host has the necessary `execute` and `read` permissions.

Policies on Conjur are written as `.yml` files. Visit the CyberArk Conjur documentation for [policy best practices](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/policy-best-practices.htm). The following steps describe how to develop a policy file.

For more information on policy syntax operators, refer to the [CyberArk Conjur documentation](https://docs.cyberark.com/conjur-open-source/Latest/en/Content/Operations/Policy/policy-syntax.htm).

1. Declare a group at the root policy:
   
   ```yaml
   - !policy
     id: workato-app
     body:
       - !group workato-secret-users
   ```
   
2. Declare variables and assign the group `[read, execute]` permissions.
   
   This example creates the `sql-password-prod` and `sql-host-prod` variables which store the password for a SQL database as well as the host name:
   
   ```yaml
   - &variables
     - !variable
       id: sql-password-prod
       kind: password
     - !variable
       id: sql-host-prod
       kind: password
   - !permit
     role: !group /workato-app/workato-secret-users       # group declared earlier
     privileges: [read, execute]
     resources: *variables
   ```
   
3. Declare the host, a layer, and assign membership of the host into the layer:
   
   ```yaml
   - !host workato-us-prod-1
   - !layer workato-us-prod
   - !grant
        role: !layer workato-us-prod
        members:
           - !host workato-us-prod-1
   ```
   
   - [Host documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-host.htm)
   - [Layer documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-grant.htm)
4. Grant membership of the layer into the group:
   
   ```yaml
   - !grant
     role: !group workato-app/workato-secret-users
     member: !layer workato-app/ workato-us-prod
   ```
   
   - [Grant documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-grant.htm)
5. Create a new secret on Conjur:
   
   ```yaml
   - !variable
     id: ddog-api-key
     kind: password
   ```
   
   - [Variable documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-variable.htm)
6. Grant `execute` and `read` permissions to group on selected variables:
   
   ```yaml
   - !permit
     role: !group /workato-app/workato-secret-users     # layer declared earlier
     privileges: [read, execute]
     resources: !variable ddog-api-key
   ```
   
   - [Permit documentation](https://docs.cyberark.com/conjur-enterprise/13.0/en/Content/Operations/Policy/statement-ref-permit.htm)

Expand for an example of a full policy

```yaml
- !policy
  id: workato-app-dev
  body:
    - !group workato-secrets-dev
    - &variables
        - !variable
            id: sql-password-prod
            kind: password
        - !variable
            id: sql-host-prod
            kind: password
    - !permit
        role: !group /workato-app-dev/workato-secrets-dev       # group declared earlier
        privileges: [read, execute]
        resources: *variables
    - !host workato-us-dev-1
    - !layer workato-us-dev
    - !grant
        role: !layer workato-us-dev
        members:
            - !host workato-us-dev-1
    - !grant
        role: !group workato-secrets-dev
        member: !layer workato-us-dev
```

To which the expected response would be:

```json
{
    "created_roles": {
        "workato:host:workato-app-dev/workato-us-dev-1": {
            "id": "workato:host:workato-app-dev/workato-us-dev-1",
            "api_key": "1q3ye3gxxxx"
        }
    },
    "version": 1
}
```

## Select project-level scope for secrets management

1. Sign in to your Workato workspace.
   
2. Navigate to **Workspace admin > Settings > Security > External secrets manager**.
   
3. In **Scope**, select the option **Set up secrets management for each project individually**.
   
   ![Set up secrets management for the entire workspace](/assets/scope-project.DXME4lQ2.png)_Set up secrets management for each project individually_
   
4. Select **Save**.
   

## Select the project

1. In Workato, navigate to your projects.
   
2. Select the project that you plan to configure with secrets management.
   
3. In the project, navigate to **Workspace admin > Settings > External secrets manager**.
   
4. In the **Which secrets manager do you want to use?** field, select **CyberArk Conjur**.
   
   ![Secrets management interface of a project](/assets/scope-project-settings.tUH09fCk.png)
   
5. Click **Set up connection**
   

## Configure the connection in Workato

1. Configure the following fields in Workato:
   
   ![Configure CyberArk Conjur connection](/assets/setup.BJAAwE3z.png)_Configure CyberArk Conjur connection_
   
   - Connection name
     
   - Name your CyberArk Conjur connection.
     
   - Connection type
     
   - Workato supports both cloud and on-prem connection types. If you plan to use an on-prem group, select one from the drop-down.
     
   - Server URL
     
   - To connect to Conjur Cloud, the server URL must follow this format:
     
     ```html
     https://<subdomain>.secretsmgr.cyberark.cloud/api/
     ```
     
   - Organization account name
     
   - To connect to Conjur Cloud, input `conjur`.
     
   - Login ID
     
   - For host authentication, the ID must be prefixed with `host/`, for example: `host/workato-app/workato-user-1`.
     
   - API key
     
   - Conjur generates an API key for every user when the user resource is created. Learn more about generating an API key in [CyberArk Conjur's documentation](https://docs.cyberark.com/conjur-enterprise/latest/en/Content/Operations/Services/default_authn.htm).

---

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

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager.md
description: Learn how to set up Google Secret Manager at the workspace level in Workato.
---

# Set up Google Secret Manager for your workspace

This guide explains how to set up Google Secret Manager at the workspace level in Workato.

> **SWITCHING SCOPES**
> 
> Existing project-level secret references stop working when you switch to workspace-level secrets management. You must reconfigure these references to use workspace-level secrets.

## Prerequisites

Ensure you have the following before you begin:

- **In Workato**:
  
  - Access to Workspace admin settings.
- **In Google Cloud**:
  
  - **Active GCP project**: You need an active Google Cloud project with billing enabled.
  - **Secret Manager setup**: You should have secrets already created in Secret Manager. Create them before configuring the connection if they don't exist.
  - **Service account**: You need a service account with the following roles assigned:
    - **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`)
    - **Secret Manager Viewer** (`roles/secretmanager.viewer`)
  - **Service account key**: You need the JSON key file for the service account.

Refer to [Set up a Google Cloud service account](/en/security/data-protection/secrets-management/google-service-account-setup) if you haven't created a service account.

## Enable Google Secret Manager at the workspace level

Complete the following steps to enable Google Secret Manager as your secrets management solution at the workspace level:

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > External secrets manager**.
   
3. Enable the **Use external secrets manager** toggle.
   
4. Use the **Scope** drop-down menu to select **Set up secrets management for the entire workspace**.
   
   ![Set up secrets for the entire workspace](/assets/secrets-management-scope-workspace.B_tXR5z3.png)_Set up secrets for the entire workspace_
   
5. Use the **Which secrets manager do you want to use?** drop-down menu to select **Google Secret Manager**.
   
6. Click **Set up connection**.
   

> **ABOUT SCOPES**
> 
> You can configure Google Secret Manager at the workspace level or the project level. The selected scope determines how secrets apply across projects:
> 
> - **Workspace level**: All projects inherit the workspace secrets manager configuration. This centralizes management but applies the same Secret Manager connection across all projects.
> - **Project level**: Each project uses its own secrets manager configuration, independent of other projects or workspace settings. This provides flexibility but requires per-project setup.

## Connect to Google Secret Manager

Complete the following steps to configure the connection between Workato and your Google Cloud project's Secret Manager:

1. Enter a name for this connection in the **Connection name** field.
   
   ![Connect to Google Secret Manager](/assets/connect.B53id9Sv.png)_Connect to Google Secret Manager_
   
2. Use the **Location** drop-down menu to select the project or folder where you plan to store this connection.
   
3. Use the **Connection type** drop-down menu to specify whether this is a cloud or on-prem connection.
   
4. Enter the ID of your project in Google Cloud in the **Project ID** field. You can find this in the GCP Console project selector or project dashboard.
   
5. Enter the service account email in the **Client email** field. The service account must have the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) and **Secret Manager Viewer** (`roles/secretmanager.viewer`) roles assigned.
   
6. Provide the **Private key** from your service account JSON key file.
   
   Retrieve your private key
   
   1. Open the JSON key file you downloaded when creating the service account.
      
   2. Locate the `private_key` field in the JSON file.
      
   3. Copy the entire private key value (including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` markers).
      
   4. Paste it into the **Private key** field.
      
   
7. Click **Connect**.
   

> **CONNECTION VALIDATION**
> 
> Check the following if the connection fails:
> 
> - Confirm the **Project ID** field contains the project ID, not the project number
> - Confirm the client email matches the service account email in Google Cloud
> - Confirm the private key contains no extra spaces or missing characters
> - Confirm the service account has the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) and **Secret Manager Viewer** (`roles/secretmanager.viewer`) roles
> - Confirm the Secret Manager API is enabled in the Google Cloud project

## Next steps

You can now proceed with the following:

- [Use Google Secret Manager secrets in connections](/en/security/data-protection/secrets-management/using-google-secret-manager-in-connections)

## Further reading

- [Set up a Google Cloud service account](/en/security/data-protection/secrets-management/google-service-account-setup)
- [Set up Google Secret Manager for a project](/en/security/data-protection/secrets-management/setting-up-project-level-google-secret-manager)
- [Google Secret Manager documentation](https://docs.cloud.google.com/secret-manager/docs)

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-project-level-google-secret-manager.md
description: Learn how to set up Google Secret Manager at the project level in Workato.
---

# Set up Google Secret Manager for a project

This guide explains how to set up Google Secret Manager at the project level in Workato.

> **SWITCHING SCOPES**
> 
> Existing workspace-level secret references in this project stop working when you switch to project-level secrets management. You must reconfigure these references to use project-level secrets.

## Prerequisites

Ensure you have the following before you begin:

- **In Workato**:
  
  - The **Create/Edit connections** privilege in the target project.
- **In Google Cloud**:
  
  - **Active GCP project**: You need an active Google Cloud project with billing enabled.
  - **Secret Manager setup**: You should have secrets already created in Secret Manager. Create them before configuring the connection if they don't exist.
  - **Service account**: You need a service account with the following roles assigned:
    - **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`)
    - **Secret Manager Viewer** (`roles/secretmanager.viewer`)
  - **Service account key**: You need the JSON key file for the service account.

Refer to [Set up a Google Cloud service account](/en/security/data-protection/secrets-management/google-service-account-setup) if you haven't created a service account.

## Enable project-level secrets management

Complete the following steps to enable project-level secrets management in workspace admin:

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > External secrets manager**.
   
3. Enable the **Use external secrets manager** toggle.
   
4. Use the **Scope** drop-down menu to select **Set up secrets management for each project individually**.
   
   ![Workato secrets management, selecting project scope](/assets/secrets-management-scope-project.d-05a3me.png)
   
5. Click **Save**.
   

> **ABOUT SCOPES**
> 
> You can configure Google Secret Manager at the workspace level or the project level. The selected scope determines how secrets apply across projects:
> 
> - **Workspace level**: All projects inherit the workspace secrets manager configuration. This centralizes management but applies the same Secret Manager connection across all projects.
> - **Project level**: Each project uses its own secrets manager configuration, independent of other projects or workspace settings. This provides flexibility but requires per-project setup.

## Enable Google Secret Manager for the project

Complete the following steps to enable Google Secret Manager for your project:

1. Select the project where you plan to configure Google Secret Manager.
   
2. Go to **Settings > Secrets management**.
   
3. Enable the **Use external secrets manager** toggle.
   
4. Use the **Which secrets manager do you want to use?** drop-down menu to select **Google Secret Manager**.
   
5. Click **Set up connection**.
   

## Connect to Google Secret Manager

Complete the following steps to configure the connection between Workato and your Google Cloud project's Secret Manager:

1. Enter a name for this connection in the **Connection name** field.
   
   ![Connect to Google Secret Manager](/assets/connect.B53id9Sv.png)_Connect to Google Secret Manager_
   
2. Use the **Location** drop-down menu to select the project or folder where you plan to store this connection.
   
3. Use the **Connection type** drop-down menu to specify whether this is a cloud or on-prem connection.
   
4. Enter the ID of your project in Google Cloud in the **Project ID** field. You can find this in the GCP Console project selector or project dashboard.
   
5. Enter the service account email in the **Client email** field. The service account must have the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) and **Secret Manager Viewer** (`roles/secretmanager.viewer`) roles assigned.
   
6. Provide the **Private key** from your service account JSON key file.
   
   Retrieve your private key
   
   1. Open the JSON key file you downloaded when creating the service account.
      
   2. Locate the `private_key` field in the JSON file.
      
   3. Copy the entire private key value (including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` markers).
      
   4. Paste it into the **Private key** field.
      
   
7. Click **Connect**.
   

> **CONNECTION VALIDATION**
> 
> Check the following if the connection fails:
> 
> - Confirm the **Project ID** field contains the project ID, not the project number
> - Confirm the client email matches the service account email in Google Cloud
> - Confirm the private key contains no extra spaces or missing characters
> - Confirm the service account has the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) and **Secret Manager Viewer** (`roles/secretmanager.viewer`) roles
> - Confirm the Secret Manager API is enabled in the Google Cloud project

## Next steps

You can now proceed with the following:

- [Use Google Secret Manager secrets in connections](/en/security/data-protection/secrets-management/using-google-secret-manager-in-connections)

## Further reading

- [Set up a Google Cloud service account](/en/security/data-protection/secrets-management/google-service-account-setup)
- [Set up Google Secret Manager for your workspace](/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager)
- [Google Secret Manager documentation](https://docs.cloud.google.com/secret-manager/docs)

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/using-google-secret-manager-in-connections.md
description: >-
  Learn how to reference secrets stored in Google Secret Manager in your Workato
  connections.
---

# Use Google Secret Manager secrets in connections

This guide explains how to use secrets from Google Secret Manager in your connections instead of storing credentials directly in Workato.

## Prerequisites

Ensure you have the following before you begin:

- **In Workato**:
  
  - **Secrets Manager configured**: You must have successfully set up Google Secret Manager at either the [workspace level](/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager) or [project level](/en/security/data-protection/secrets-management/setting-up-project-level-google-secret-manager).
  - **Create/Edit Connections privilege**: You need the Create/Edit Connections privilege in your Workato project.
- **In Google Cloud**:
  
  - **Secret Manager access**: You need permissions to create and manage secrets in your GCP project's Secret Manager.
  - **Service account permissions**: The service account used by Workato must have the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) role to read the secrets you create.

## Add a secret to Google Secret Manager

Complete the following steps to create a secret in Google Cloud Secret Manager:

1. Sign in to the [Google Cloud Console](https://console.cloud.google.com/).
   
2. Go to **Security > Secret Manager**.
   
3. Click **Create secret**.
   
4. Enter a unique identifier for your secret in the **Name** field. For example, `salesforce-api-key` or `workato-db-password`.
   
5. Enter your secret data in the **Secret value** field, such as an API key, password, or token. Alternatively, you can click **Upload file** to provide a text file containing the secret data.
   
   ![Create secret](/assets/create-secret.DipP6SwH.png)_Create secret_
   
6. Click **Create secret**.
   

Refer to [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) in the Google Cloud documentation for information about advanced configuration options such as replication policies, rotation schedules, and expiration settings.

> **SECRET VERSIONS**
> 
> Google Secret Manager automatically versions secrets. When you update a secret value, a new version is created. Workato retrieves the latest enabled version but caches the value for 60 minutes. If the latest version is disabled or destroyed, Workato won't fall back to an older enabled version and the connection will fail. Make sure the version you want Workato to use is set to **Enabled** in Google Cloud.
> 
> You can wait for the cache to expire or [clear the cache manually](/en/workato-api/environment-management#clear-secrets-management-cache) to use the updated value.

## Reference secrets in Workato connections

Complete the following steps to reference your Google Secret Manager secret in a Workato connection:

1. Sign in to Workato.
   
2. Select the project where you plan to create or edit a connection.
   
3. Create a new connection or edit an existing one.
   
4. Click **Add external secret** for any sensitive field (for example, API key, password, or client secret).
   
5. Enter the exact name of your secret from Google Secret Manager in the **Secret name** field and click **Done**.
   
   ![Enter the secret name from Google Secret Manager](/assets/add-external-secret.DzCkZFBV.png)_Enter the secret name from Google Secret Manager_
   
6. Complete the remaining connection fields.
   
7. Click **Connect**.
   
   ![Connect using a secret from Google Secret Manager](/assets/use-secret-manager-in-connection.CUDCBFj3.png)_Connect using a secret from Google Secret Manager_
   

## Secrets cache behavior

Workato caches credentials retrieved from Google Secret Manager for **60 minutes**. During this period, recipes continue to use the cached value, even if you update or rotate the secret.

After the cache expires, the next recipe execution retrieves the latest value from Google Secret Manager. You can call the [Clear secrets management cache](/en/workato-api/environment-management#clear-secrets-management-cache) endpoint to apply changes immediately. This forces Workato to fetch the latest credentials without requiring you to disconnect and reconnect the connection.

## Troubleshoot connection errors

If a connection that uses Google Secret Manager secrets fails, check the error message against the following:

| Error message | Fix |
| --- | --- |
| The secret version is disabled. Enable it in your Google Cloud project. | In Google Cloud Console, go to **Security > Secret Manager**, find the secret, and enable a version. |
| Secret not found. Verify the secret exists and has enabled versions. | Confirm the name exactly matches the secret name in Google Cloud (case-sensitive), and confirm at least one version is enabled. |
| Secret version is destroyed. Create a new version. | Create a new version with the correct value in Google Cloud. |
| Secret Manager API not enabled. Enable it in Google Cloud Console. | Go to **APIs & Services > Library** in Google Cloud Console, search for **Secret Manager API**, and click **Enable**. |
| The service account requires Secret Manager Secret Accessor role to be granted. | In Google Cloud IAM, assign the **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) role to the service account. |

## Further reading

- [Set up a Google Cloud service account](/en/security/data-protection/secrets-management/google-service-account-setup)
- [Set up Google Secret Manager for your workspace](/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager)
- [Set up Google Secret Manager for a project](/en/security/data-protection/secrets-management/setting-up-project-level-google-secret-manager)
- [Using on-prem agent with Google Secret Manager](/en/on-prem/agents/secrets-manager/google-secret-manager)
- [Google Secret Manager documentation](https://docs.cloud.google.com/secret-manager/docs)

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/google-service-account-setup.md
description: >-
  Learn how to create a Google Cloud service account and generate the JSON key
  file Workato needs to connect to Google Secret Manager.
---

# Set up a Google Cloud service account

This guide explains how to create a Google Cloud service account and generate credentials that allow Workato to access secrets in Google Secret Manager.

## Prerequisites

Ensure you have the following before you begin:

- An active Google Cloud project (GCP project) with billing enabled
  
- The following IAM permissions in your GCP project:
  
  - `serviceusage.services.enable`
  - `iam.serviceAccounts.create`
  - `iam.serviceAccountKeys.create`
  - `resourcemanager.projects.setIamPolicy`

## Enable the Secret Manager API

Complete the following steps to enable the Secret Manager API in your GCP project:

1. Sign in to the [Google Cloud Console](https://console.cloud.google.com/) and select your project.
   
2. Go to **APIs & Services > Library**.
   
3. Search for and select `Secret Manager API`.
   
4. Click **Enable**.
   
   ![Enable the Secret Manager API](/assets/enable-api.DO7pnAp3.png)_Enable the Secret Manager API_
   

## Create a service account

Complete the following steps to create a Google Cloud service account:

1. Go to **IAM & Admin > Service Accounts**.
   
2. Click **Create Service Account**.
   
3. Enter a descriptive **Service account name**. For example, `Workato Secrets Manager`. The **Service account ID** is auto-generated from the name.
   
4. Optionally, enter a **Service account description**. For example, `Service account for Workato to access Secret Manager`.
   
   ![Create the service account](/assets/create-service-account.C5Ci8f7A.png)_Create the service account_
   
5. Click **Create and continue**.
   

## Assign the Secret Manager IAM roles

Complete the following steps to grant the service account permission to access secrets in your project. The service account requires two roles:

- **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`)
- **Secret Manager Viewer** (`roles/secretmanager.viewer`)

1. Click the **Select a role** drop-down menu in the **Permissions** section.
   
2. Search for and select **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`).
   
3. Click **\+ Add another role**.
   
4. Search for and select **Secret Manager Viewer** (`roles/secretmanager.viewer`).
   
   ![Select the Secret Manager Secret Accessor permission](/assets/secret-manager-permission.BvFj_PTq.png)_Select the Secret Manager Secret Accessor permission_
   
5. Click **Continue**.
   
6. Click **Done** to skip the optional **Principals with access** section.
   

## Create and download a service account key

Complete the following steps to generate a JSON key file that Workato uses to authenticate as the service account:

1. Locate the service account you just created on the **Service Accounts** page.
   
2. Click the service account email address to open its details.
   
3. Click the **Keys** tab.
   
4. Click **Add Key > Create new key**.
   
5. Select **JSON** as the key type.
   
6. Click **Create**.
   

The JSON key file downloads automatically. The file contains the credentials Workato needs to authenticate to Google Secret Manager, including `project_id`, `private_key`, and `client_email`. Store the file securely and restrict access.

## Next steps

Refer to the following guides to complete the setup:

- [Set up Google Secret Manager for your workspace](/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager)
- [Set up Google Secret Manager for a project](/en/security/data-protection/secrets-management/setting-up-project-level-google-secret-manager)

## Further reading

- [Google Cloud Service Accounts documentation](https://cloud.google.com/iam/docs/service-accounts)
- [Secret Manager IAM roles and permissions](https://docs.cloud.google.com/secret-manager/docs/access-control)
- [Best practices for managing service account keys](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)

---

---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/setting-up-workspace-level-hashicorp-vault-secrets-engine.md
description: >-
  Set up HashiCorp Vault KV secrets engines for workspace-level secrets
  management to manage connection credentials across your Workato account.
---

# Set up HashiCorp Vault secrets engines for workspaces

Switching to workspace-specific secrets management causes all previously configured external secret references to stop working.

## Prerequisites

To complete the steps in this guide, you must have the following:

- HashiCorp Vault Key-value (KV) secrets engine version 1 or 2.
- An account with [AppRole auth method](https://developer.hashicorp.com/vault/tutorials/auth-methods/approle#step-2-create-a-role-with-policy-attached) enabled.
- One or more [AppRole](https://developer.hashicorp.com/vault/docs/auth/approle?_gl=1*vnxfyv*_ga*MTM5ODQwMDE3My4xNjgxMjQzMzg2*_ga_P7S46ZYEKW*MTY4MTQxNzMxMS4xLjAuMTY4MTQxNzMxMS4wLjAuMA..#configuration)s configured.

## Select the scope for secrets management

1. Sign in to Workato.
   
2. Go to **Workspace admin > Settings > External secrets manager**.
   
3. Select the **Set up secrets management for the entire workspace** option from the **Scope** drop-down menu.
   
   ![Workato secrets management, selecting workspace scope](/assets/secrets-management-scope-workspace.B_tXR5z3.png)
   

## Select the secrets manager

1. Select **HashiCorp Vault** from the **Which secrets manager do you want to use?** drop-down menu.
   
   ![Hashicorp Vault secrets](/assets/hashicorp-vault-secrets.4t0STmDF.png)
   

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
   
     
   
   - `<approle_name>`
     
   - The AppRole you have configured in HashiCorp Vault.
     
   - `<role_name>`
     
   - The name of the Workato role you plan to connect to.
     
   
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
   
8. Click **Connect**. Workato displays the name of the HashiCorp Vault connection:
   
   ![Connection successful](/assets/connected.BRI1CJby.png)_Connection successful_
   

> **FURTHER READING**
> 
> - [Using HashiCorp Vault Secrets to authenticate to connections](/en/security/data-protection/secrets-management/using-hashicorp-secrets-in-connections)

---

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

---

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

---

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

---
