---
url: 'https://docs.workato.com/en/connectors/amazon-sns.md'
description: >-
  Amazon SNS is a fully managed messaging service for both
  application-to-application and application-to-person communication.
---

# Amazon SNS

[Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) is a fully managed messaging service for both application-to-application and application-to-person communication. It uses a simplified Pub/Sub paradigm to connect distributed systems, microservices, and node applications.

## API version

The Amazon SNS connector uses the [Amazon SNS API](https://docs.aws.amazon.com/sns/latest/api/Welcome.html).

## How to connect to Amazon SNS on Workato

Choose one of the following authentication methods to connect to Amazon SNS:

- [IAM role](#integration-system-role)
- [Access key ID and secret](#integration-system-user)

> **USE THE AWS IAM ROLE**
> 
> We recommend using the [AWS IAM role](#integration-system-role).
> 
> The AWS IAM role uses temporary credentials making this method secure and not requiring additional management compared to the AWS IAM user which uses permanent credentials that can be leaked and that have to be rotated by the user.

### Connect using an access key authentication

Complete the following steps to create a connection using an IAM user's access key:

1. Select the project where you plan to store the Amazon SNS connection.
   
2. Click **Create > Connection** or press C twice.
   
3. Search for and select the **Amazon SNS** connector.
   
4. Enter a name for your connection in the **Connection name** field.
   
   ![Connection setup](/assets/key-auth-setup.ChCe8Y2P.png)_Amazon SNS connection setup_
   
5. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
6. Use the **Authentication type** drop-down menu to choose **Access key auth**.
   
7. Enter the **Access key ID**. Go to **AWS account name > Security Credentials > Users** to retrieve this value. This is the IAM user's access key ID.
   
8. Enter the **Secret Access Key** from the same page.
   
9. Enter the **Region** of the SNS account. For example, if your SNS URL is `https://eu-west-1.console.aws.amazon.com`, use `us-east-1` as the **Region**.
   
10. Click **Connect**.
    

### Connect using IAM role authentication

Complete the following steps to create a connection using an AWS IAM role:

1. Select the project where you plan to store the Amazon SNS connection.
   
2. Click **Create > Connection** or press C twice.
   
3. Search for and select the **Amazon SNS** connector.
   
4. Enter a name for your connection in the **Connection name** field.
   
   ![Connection setup](/assets/iam-setup.BKTVjPWc.png)_Amazon SNS connection setup_
   
5. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
6. Use the **Authentication type** drop-down menu to select **IAM Role auth**.
   
7. Enter the **IAM role ARN** associated with your IAM role. For example, `arn:aws:iam::account_id:role/role-name-with-path`.
   
   Refer to the [IAM Role-based Authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws) page for instructions on how to create an IAM role for Workato and retrieve your Amazon resource name (ARN).
   
8. Enter the **Region** associated with your SNS account. For example, if your account URL is `https://eu-west-1.console.aws.amazon.com`, use `us-east-1` as the **Region**.
   
9. Click **Connect**.
   

## How to create an integration system role

Create an integration system role to apply consistent permissions and log all operations under a single account. Refer to the [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) documentation for more information.

You can also create an [integration system user](#integration-system-user) to control permissions independently of the integration system role.

## How to create an integration system user

Complete the following steps to create an integration system user (ISU) and generate access credentials to connect to Workato.

1. Go to **Identity and Access Management (IAM)** in your AWS console.
   
2. Select **Users** from the left panel.
   
3. Click **Add user**. ![Create IAM user](/assets/iam-add-user.DIOQ3f3D.png)_Create IAM user_
   
4. Set the **username**. Ensure that **Programmatic access** is selected. ![Set username](/assets/iam-username.DgDQtKZw.png)_Set username_
   
5. Skip selecting policies in the **Add permissions** view. You configure [permissions and polices in a later step](#create-inline-policy-for-isu). ![Set permissions](/assets/iam-permissions-skip.D-woK2Xy.png)_Skip setting permissions_
   
6. Click **Next**.
   
7. Add **Tags**. Review the IAM user configuration.
   
   > **USER HAS NO PERMISSION**
   > 
   > You may see a warning that this user has no permissions. This is expected. You will [assign permissions in a later step](#create-inline-policy-for-isu).
   
8. Download or copy the **Access key ID** and **Secret access key**. Use these credentials to [connect to Workato](#connection-setup). ![Save access key credentials](/assets/iam-save-access-key.DLD-g3xx.png)_Save access key credentials_
   
9. Return to **Identity and Access Management (IAM)** in your AWS console.
   
10. Select **Users** from the left panel and select the user that you created.
    
11. Click **Add inline policy**. ![Update IAM user policy](/assets/iam-update-policy.COgAqBVh.png)_Update IAM user policy_
    
12. **Adding permission for ISU**
    
    Select the **JSON** tab in the **Create policy** view. Enter the following IAM policy template:
    
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Action": [
                    "iam:GetUser",
                    "sns:ListTopics",
                    "sns:Subscribe",
                    "sns:Unsubscribe",
                    "sns:SetSubscriptionAttributes",
                    "sns:Publish"
                ],
                "Resource": "*"
            }
        ]
    }
    ```
    
    ![Review IAM user policy](/assets/iam-review-policy.Bxrjjx2b.png)_Review IAM user policy_
    
13. Click **Review policy**.
    
14. Enter a name for the policy in the **Review policy** view. For example, `workato_isu-sns_connector`.
    
15. Click **Create policy**. Use the access key credentials you saved earlier to [connect to Workato](#connection-setup).
    
    ![Create policy](/assets/iam-create-policy.DM_8RFER.png)_Create policy_

---
