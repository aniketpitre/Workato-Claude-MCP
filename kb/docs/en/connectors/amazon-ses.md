---
url: 'https://docs.workato.com/en/connectors/amazon-ses.md'
description: >-
  The Amazon SES connector enables you to use workflows like auto-responders,
  email unsubscribe systems, and applications that generate customer support
  tickets from incoming emails.
---

# Amazon SES

[Amazon SES](https://aws.amazon.com/ses/) is an email platform that provides an easy, cost-effective way for you to send and receive email using your own email addresses and domains.

The Amazon SES connector lets you use workflows like auto-responders, email unsubscribe systems, and applications that generate customer support tickets from incoming emails.

* * *

## API version

This connector uses the [Amazon SES API V2](https://docs.aws.amazon.com/ses/latest/APIReference-V2/Welcome.html).

* * *

## How to connect to Amazon SES on Workato

Workato supports the following authentication methods for Amazon SES:

- [IAM role ARN authentication](#iam-role)
- [Access Key ID authentication (Deprecated)](#access-key)

> **IAM ROLE AUTHENTICATION**
> 
> Workato recommends that you provision a dedicated integration role for this Workato connection. This helps to maintain permission boundaries, including controlled access and actions that are permitted by the third-party application (for example, Workato).
> 
> Refer to the Amazon documentation to learn how to [create an IAM User](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

### Permissions

When you create an IAM user and IAM role in Amazon SES, Workato performs operations in your Amazon SES user. To use the full set of Amazon SES connector actions, the IAM User must have `FullAccess` permissions to SES.

Example ARN Policy: `arn:aws:iam::aws:policy/AmazonSESFullAccess`.

* * *

## IAM role ARN authentication

For this authentication method, you must provide the [IAM role ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

Complete the steps in [Use IAM role-based authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#retrieve-iam-role-arn) to get the required IAM role Amazon Resource Name (ARN).

### Complete IAM role ARN setup in Workato

Complete the following steps to finish setting up your Amazon SES connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Amazon SES` as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select your **Connection type** from the drop-down menu.
   
6. Select **IAM role** from the **Authorization type** drop-down menu.
   
7. Enter the **IAM role ARN**.
   
8. Enter the **Region** of the SES account you are using.
   
9. Click **Connect**
   

## Retrieve access key information

This authentication method requires an access key. Refer to the [Amazon documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) to get the required access key information.

> **DEPRECATED**
> 
> Access key authentication is deprecated. Workato recommends using IAM role authentication.

### Complete access key setup in Workato

Complete the following steps to finish setting up your Amazon SES connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Amazon SES` as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select your **Connection type** from the drop-down menu.
   
6. Select **Access key** from the **Authorization type** drop-down menu.
   
7. Enter the **Access key ID**.
   
8. Enter the **Secret access key**.
   
9. Enter the **Region** of the SES account you are using.
   
10. Click **Connect**.

---
