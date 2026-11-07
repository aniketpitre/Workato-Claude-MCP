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
