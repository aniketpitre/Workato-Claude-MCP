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
