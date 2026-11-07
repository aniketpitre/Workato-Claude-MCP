---
url: 'https://docs.workato.com/en/connectors/textract.md'
description: >-
  The Amazon Textract connector lets you extract structured data from documents
  using AWS's OCR and document analysis capabilities.
---

# Amazon Textract

[Amazon Textract](https://aws.amazon.com/textract/) is an AI-powered service from AWS that automatically extracts text, forms, tables, and other data from scanned documents. It uses OCR and machine learning to analyze and convert document content into structured data.

The Amazon Textract connector in Workato allows you to automate document workflows by extracting data from uploaded files and using it across your recipes.

## How to connect to Amazon Textract

Workato supports the following authentication methods for Amazon Textract:

- [IAM role ARN authentication](#iam-role)
- [Access Key ID authentication](#access-key)

> **IAM ROLE AUTHENTICATION**
> 
> Workato recommends that you provision a dedicated integration role for this Workato connection. This helps to maintain permission boundaries, including controlled access and actions that are permitted by the third-party application (for example, Workato).
> 
> Refer to the Amazon documentation to learn how to [create an IAM User](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

## IAM role ARN authentication

For this authentication method, you must provide the [IAM role ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

Complete the steps in [Use IAM role-based authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#retrieve-iam-role-arn) to get the required IAM role Amazon Resource Name (ARN).

### Complete IAM role ARN setup in Workato

Complete the following steps to finish setting up your Amazon Textract connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Amazon Textract` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select your **Connection type** from the drop-down menu.
   
6. Select **IAM role** from the **Authorization type** drop-down menu.
   
7. Enter the **IAM role ARN**.
   
8. Enter the **Region** of your Amazon Textract account.
   
9. Click **Connect**.
   

## Retrieve access key information

This authentication method requires an access key. Refer to the [Amazon documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) to get the required access key information.

### Complete access key setup in Workato

Complete the following steps to finish setting up your Amazon Textract connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Amazon Textract` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select your **Connection type** from the drop-down menu.
   
6. Select **Access key** from the **Authorization type** drop-down menu.
   
7. Enter the **Access key ID**.
   
8. Enter the **Secret access key**.
   
9. Enter the **Region** of your Amazon Textract account.
   
10. Click **Connect**.

---
