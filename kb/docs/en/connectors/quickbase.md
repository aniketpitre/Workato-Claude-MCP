---
url: 'https://docs.workato.com/en/connectors/quickbase.md'
description: >-
  The Quickbase connector lets you create, update, delete, and search records,
  download attachments, and trigger recipes on new or updated records.
---

# Quickbase

[Quickbase](https://www.quickbase.com/) is a cloud service that helps organizations manage their projects and workflows.

## Use cases

Integrate Quickbase with your business applications to streamline data management and automate workflows. You can keep records up to date, sync employee data, and trigger real-time notifications with automated workflows. Explore our [use cases](/en/getting-started/workato-use-cases) to discover how you can enhance your Quickbase workflows:

- [Update Quickbase records](/en/getting-started/use-cases/sftp-csv-by-workato-quickbase) from SFTP CSV files.
- [Sync Quickbase employees](/en/getting-started/use-cases/quickbase-oracle-ebs-slack) to Oracle EBS and notify your team in Slack.

## API version

The Quickbase connector uses the [Quickbase API](https://help.quickbase.com/api-guide/index.html).

## How to connect to Quickbase on Workato

Workato supports user-token authentication and username/password authentication for connecting to Quickbase:

- [User-token authentication](#authentication-user-token)
- [Username/password authentication](#authentication-username-password)

Workato recommends using user-token authentication for improved security in your connection. This also allows you to set up granular permissions to control resources Workato can access in Quickbase.

### Roles and permissions required to connect

Workato recommends that the user and API key used to connect to Workato have **Administrator** entitlements. Several triggers and actions require administrator privileges.

## User-token authentication

1. Log in to your Workato account and navigate to the project where you plan to add your Quickbase connection.
   
2. Click **Create > Connection** or press C+C. Select **Quickbase** as your connection.
   
3. Provide a unique **Connection name** that identifies to which Quickbase instance it is connected.
   
4. Enter your Quickbase **subdomain**. This is most often your company name.
   
5. Select the **Yes** option from the **User-token authentication?** drop-down menu.
   
6. Provide your **User token**. You can generate this token in Quickbase by completing the [following steps](#generate-user-token).
   

### Generate a user token

To generate a user token:

1. Sign in to your Quickbase account.
   
2. Navigate to **Your profile > My preferences > Manage User Tokens**.
   
3. Click **Create new user token** and follow the prompts to generate a new user token.
   
4. Copy the user token and enter it in Workato's [Quickbase connection settings](#authentication-user-token).
   

## Username/password authentication

1. Log in to your Workato account and navigate to the project where you plan to add your Quickbase connection.
   
2. Click **Create > Connection** or press C+C. Select **Quickbase** as your connection.
   
3. Provide a unique **Connection name** that identifies the Quickbase instance you plan to use.
   
4. Enter your Quickbase **subdomain**. This is most often your company name.
   
5. Select the **No** option from the **User-token authentication?** drop-down menu.
   
6. Provide your Quickbase username and password.

---
