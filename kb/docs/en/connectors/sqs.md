---
url: 'https://docs.workato.com/en/connectors/sqs.md'
description: >-
  Amazon SQS is a web service offered by Amazon Web Services that provides fully
  managed message queues for microservices, distributed systems, and serverless
  applications.
---

# Amazon SQS

[Amazon SQS](https://aws.amazon.com/sqs/) is a web service offered by Amazon Web Services that provides fully managed message queues for microservices, distributed systems, and serverless applications. The Amazon SQS connector enables you to use Amazon SQS capabilities with Workato.

## API version

The Amazon SQS connector uses the [Amazon SQS REST API](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html).

## How to connect to Amazon SQS on Workato

Workato supports the following authentication methods for Amazon SQS:

- [IAM role ARN authentication](#iam-role)
- [Access Key ID authentication](#access-key)

> **IAM ROLE AUTHENTICATION**
> 
> We recommend that you provision a dedicated integration role for this Workato connection. A dedicated integration role helps maintain permission boundaries, including controlled access and actions that are permitted by the third-party application, for example, Workato.
> 
> Refer to the Amazon documentation to the following documentation for more information about IAM role authentication in Workato:
> 
> - [Use IAM role-based authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#supported-connectors) in the Workato documentation.
> - [Create an IAM user in your AWS account](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in the Amazon documentation.

> **LEGACY ACCESS KEY AUTHENTICATION**
> 
> Access key authentication is a legacy authentication format. We highly recommend using IAM role authentication.

### Permissions

Workato performs operations in your Amazon SQS user account when you create an IAM user and IAM role in Amazon SQS. The IAM User must have `FullAccess` permissions to SQS to use the full set of Amazon SQS connector actions.

Example ARN Policy: `arn:aws:iam::aws:policy/AmazonSQSFullAccess`.

* * *

## IAM role ARN authentication

For this authentication method, you must provide the [IAM role ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

Complete the steps in [Use IAM role-based authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#retrieve-iam-role-arn) to get the required IAM role Amazon Resource Name (ARN).

### Complete IAM role ARN setup in Workato

Refer to [Use IAM role-based authentication for AWS Services](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws#create-an-iam-role) for more information IAM authentication.

Complete the following steps to finish setting up your Amazon SQS connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Amazon SQS` as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select your **Connection type** from the drop-down menu.
   
6. Use the **Authorization type** drop-down menu to select **IAM role**.
   
7. Enter the **IAM role ARN**.
   
8. Enter the **Region** of the SQS account you plan to use.
   
9. Click **Connect**.
   

## Retrieve access key information

This authentication method requires an access key. Refer to the [Amazon documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) to get the required access key information.

> **DEPRECATED**
> 
> Access key authentication is deprecated. Workato recommends using IAM role authentication.

### Complete access key setup in Workato

Complete the following steps to finish setting up your Amazon SQS access key in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Amazon SQS` as your connection in the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Authorization type** drop-down menu to select **Access key**.
   
7. Enter the **Access key ID**.
   
8. Enter the **Secret access key**.
   
9. Enter the **Region** of the SQS account you plan to use.
   
10. Click **Connect**.
    

## Terminology

The following [terminology](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-how-it-works.html) is important for understanding and working with Amazon SQS objects:

### Queues

The Workato SQS connector only supports standard queues.

Amazon SQS has two types of queues:

- Standard queues: This is the default queue type which supports at-least-once message delivery. Standard queues provide optimized-effort ordering which ensures that messages are delivered in the same order they're sent.
- FIFO queues - FIFO (First-In-First-Out) queues enhance messaging between applications when the order of operations and events is critical, or the messaging can't tolerate duplicates.

### Messages

Amazon SQS lets you include structured metadata, including timestamps, geospatial data, signatures, and identifiers with messages using message attributes. Each message can have up to 10 attributes. Message attributes are optional and separate from the message body, but are sent alongside it. Workato supports both message bodies and message attributes.

When a consumer receives and processes a message from a queue, the message remains in the queue. Amazon SQS doesn't automatically delete the message. Because Amazon SQS is a distributed system, there's no guarantee that the consumer receives the message. The Workato SQS connector allows you to delete messages automatically when you retrieve them in triggers. Alternatively, you can use the `Delete messages` action to delete messages after you process them in your recipe.

### Short and long polling

Due to SQS's distributed nature, a single request to SQS may not retrieve all messages in the queue. For example, a request to retrieve 10 messages may only retrieve 9 messages when there could be hundreds of messages in the queue. This is because SQS samples a subset of servers holding messages to return them.

Workato uses long polling with a wait timeout of 5 seconds to mitigate this. When Workato attempts to retrieve messages in triggers or actions, Workato waits for up to 5 seconds for messages to arrive at sampled servers. Configure this timeout for actions using the input `Wait time (seconds)`.

### Visibility timeout

Messages remain in the queue immediately after they are received. To prevent other users from processing the message again, Amazon SQS sets a visibility timeout, which Amazon SQS prevents other users from receiving and processing the message.

The Workato connector enables you to configure a visibility timeout with a maximum of 12 hours. If you leave the **Visibility Timeout** input field blank, the default Amazon SQS timeout is 30 seconds. If you provide a **Visibility Timeout** value, it must be between 0 to 12 hours. Messages are not visible to other users during this time.

This behavior minimizes the possibility of duplicate message processing while allowing timeout value flexibility.

### Dead letter queues

Only deleted messages in an SQS queue are considered processed. Message are moved to a dead-letter queue for debugging if the messages are left in a queue for a set amount of time or retrieved too many times.

Workato doesn't support storing messages stored in dead-letter queues. Workato recommends setting alarms to notify you when messages enter dead-letter queues. Refer to the [Amazon SQS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) for more information.

## Troubleshooting

Use the following troubleshooting information to fix visibility timeout issues.

### Duplicate messages across jobs

You may see duplicate messages across different jobs. This happens when jobs process too slowly and messages retrieved by Workato pass their visibility timeout and are eligible to retrieve again.

Increase the visibility timeout or delete messages as they're retrieved to prevent this.

---
