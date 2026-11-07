---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/snowflake-mcp-server.md'
description: >-
  Use the Snowflake Data Explorer MCP server to connect your LLM to Snowflake
  with tools to discover, understand, and retrieve data.
---

# Snowflake Data Explorer MCP server

The Snowflake Data Explorer MCP server enables LLMs to discover, understand, and retrieve data from Snowflake through governed, read-only access. It provides tools to navigate databases, schemas, tables, and views, inspect schema metadata, sample data, and execute read-only SQL within configured safety and access boundaries. The server doesn't modify data, run administrative or DDL operations, or perform AI inference such as Snowflake Cortex functions.

## Uses

Use the Snowflake Data Explorer MCP server to perform the following actions:

- List Snowflake databases accessible within configured allowlists
- Explore schemas within specific databases
- Discover tables and views within schemas
- Search for tables and views by name-oriented criteria when the exact location is unknown
- Retrieve column names, data types, and available descriptions for tables or views
- Sample bounded sets of rows from tables or views to inspect values and formats
- Execute governed, read-only SQL queries with enforced row quotas, timeouts, and object allowlists

### Example prompts

Use the following example prompts to invoke Snowflake Data Explorer MCP server tools:

- `What databases are available in Snowflake?`
- `List the schemas in the SALES_DATA database.`
- `Show me tables in the CUSTOMER_ANALYTICS schema.`
- `Show me views in the CUSTOMER_ANALYTICS schema.`
- `Find tables related to subscriptions.`
- `Find views related to subscriptions.`
- `What columns are in the CUSTOMER_EVENTS table?`
- `Show me a sample of data from the activity logs table.`
- `Query the top 100 customers by revenue from last quarter.`

## Snowflake Data Explorer MCP server tools

The Snowflake Data Explorer MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_databases](#list-databases-tool) | Lists Snowflake databases accessible within the server's configured allowlists. |
| [list\_schemas](#list-schemas-tool) | Lists schemas in a specified database to navigate the Snowflake object hierarchy. |
| [list\_tables](#list-tables-tool) | Lists tables in a specified schema with metadata suitable for discovery. |
| [list\_views](#list-views-tool) | Lists views in a specified schema with metadata suitable for discovery. |
| [search\_tables](#search-tables-tool) | Searches for tables by name-oriented criteria when the exact location is unknown. |
| [search\_views](#search-views-tool) | Searches for views by name-oriented criteria when the exact location is unknown. |
| [get\_table\_schema](#get-table-schema-tool) | Retrieves column names, data types, and available descriptions for a specified table or view. |
| [get\_table\_sample](#get-table-sample-tool) | Returns a bounded sample of rows from a table or view to inspect values and formats before running full queries. |
| [execute\_query](#execute-query-tool) | Executes a read-only SQL query against Snowflake using the configured warehouse, subject to row quotas, timeouts, and access restrictions. |

## Install the Snowflake Data Explorer MCP server

Complete the following steps to install a prebuilt MCP server to your project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
5. Click **Use this server**.
   
6. Provide a name for your MCP server in the **Server name** field.
   
7. Use the **Location** drop-down menu to select the project for the MCP server.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the MCP server template.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   ![Select your connection type](/assets/connection-type.Cor-6PJN.png)_Select your connection type_
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Complete the app-specific connection setup steps in the following section.
    

## Snowflake connection setup

View Snowflake connection setup steps

Workato supports the following authentication methods for Snowflake connections:

- [OAuth 2.0](#configuring-oauth-2-0)
- [Key-pair authentication](#configure-private-key-authentication)

### Configure OAuth 2.0 authentication

View Configure OAuth 2.0 authentication steps

You must create a custom integration and generate a client ID and secret in Snowflake to use OAuth 2.0 authentication.

#### Snowflake setup for OAuth 2.0 authentication

Complete the following steps to create a custom integration and retrieve client credentials in Snowflake:

1. Run the following SQL command in Snowflake to register a custom OAuth integration:
   
   ```sql
   CREATE SECURITY INTEGRATION WORKATO_OAUTH
     TYPE = OAUTH
     ENABLED = TRUE
     OAUTH_CLIENT = CUSTOM
     OAUTH_CLIENT_TYPE = CONFIDENTIAL
     OAUTH_REDIRECT_URI = 'https://www.workato.com/oauth/callback'
     OAUTH_ISSUE_REFRESH_TOKENS = TRUE;
   ```
   
   > **REQUIRED PRIVILEGE**
   > 
   > Use the `ACCOUNTADMIN` role or a role with the global `CREATE INTEGRATION` privilege to run this command.
   
2. Run the following command to retrieve your client credentials:
   
   ```sql
   SELECT SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('WORKATO_OAUTH');
   ```
   
   Refer to the Snowflake [Configure Snowflake OAuth for custom clients](https://docs.snowflake.net/manuals/user-guide/oauth-custom.html) guide for more information.
   
3. Copy and save the **Client ID** and **Client secret** for use in Workato.
   

#### Connect to Snowflake with OAuth 2.0 authentication

Complete the following steps to set up an OAuth 2.0 authentication connection to Snowflake Data Explorer in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Snowflake` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Snowflake OAuth 2.0 connection](/assets/connection.BBLDp5Fr.png)_Snowflake OAuth 2.0 connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the Snowflake instance **Account identifier** in one of the supported formats:
   
   - **Account name**: `https://{org_name}-{account_name}`
   - **Connection name**: `https://{org_name}-{connection_name}`
   - **Account locator**: `https://{account_locator}.{region}.{cloud}`
   
   Refer to the Snowflake [Connecting to your accounts](https://docs.snowflake.com/en/user-guide/organizations-connect#connecting-with-a-url) guide for more information.
   
   > **ACCOUNT LOCATOR FORMAT**
   > 
   > Certain locations require you to include the `{region}` and `{cloud}` in your account locator URL. For example:
   > 
   > - **AWS US West (Oregon)**: `your-account-locator`
   > - **AWS US East (Ohio)**: `your-account-locator.us-east-2`
   > - **Azure West Europe**: `your-account-locator.west-europe.azure`
   > 
   > Refer to the Snowflake [Using an account locator as an identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier#using-an-account-locator-as-an-identifier) guide for more information.
   
6. Enter the **Warehouse** name to define the compute resources for this connection. Refer to [Warehouse considerations](/en/connectors/snowflake#warehouse-considerations) for more information.
   
7. Enter the **Database name** for the target Snowflake database.
   
8. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
9. Enter the **Client ID** and **Client secret**. Refer to [Snowflake setup for OAuth 2.0 authentication](#oauth2-setup) for information on how to retrieve these credentials.
   
10. Optional. Specify a **Role** for authentication. This role must be an existing role assigned to the user. If left blank, Snowflake uses the default role assigned to the user.
    
11. Optional. Enter the **Schema**. If left blank, the default schema is public.
    
12. Optional. Set the **Use improved datetime handling (Recommended)** to **Yes** to ensure correct timezone handling for timestamps.
    
13. Optional. Define the **Database timezone** to apply to timestamps without an assigned timezone. Defaults to your workspace's timezone if left blank.
    
14. Click **Connect**.
    
15. Click **Allow** to provision access to Workato.
    

### Configure key-pair authentication

View Configure key-pair authentication steps

Use key-pair authentication to connect to Snowflake without a password. This method uses a client-generated RSA key pair and provides strong security. You must use a command-line tool to generate the key pair.

#### Snowflake setup for key-pair authentication

Complete the following steps to create a key pair in Snowflake:

1. Run one of the following commands in a terminal to generate a private key.
   
   **Unencrypted**
   
   Generate an unencrypted private key:
   
   ```bash
   openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
   ```
   
   **Encrypted v1**
   
   Generate an encrypted private key using a `-v1` algorithm:
   
   ```bash
   openssl genrsa 2048 | openssl pkcs8 -topk8 -v1 <ALGORITHM> -inform PEM -out rsa_key.p8
   ```
   
   You can use the following `-v1` algorithms:
   
   - `PBE-SHA1-RC2-40`
   - `PBE-SHA1-RC4-40`
   - `PBE-SHA1-RC2-128`
   - `PBE-SHA1-RC4-128`
   - `PBE-SHA1-3DES`
   - `PBE-SHA1-2DES`
   
   **Encrypted v2**
   
   Generate an encrypted private key using a stronger `-v2` algorithm:
   
   ```bash
   openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 <ALGORITHM> -inform PEM -out rsa_key.p8
   ```
   
   You can use the following `-v2` algorithms:
   
   - `AES128`
   - `AES256`
   - `DES3`
   
   > **PRIVATE KEY PASSPHRASE**
   > 
   > If you generate an encrypted private key, you must enter the **Private key passphrase** when you configure the connection in Workato.
   
2. Copy and save the **PRIVATE KEY** for use in Workato. Copy everything from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----`.
   
3. Run the following command to create a public key from the private key. OpenSSL prompts you for the passphrase if you generated an encrypted private key.
   
   ```bash
   openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
   ```
   
4. Copy and save the **PUBLIC KEY** for use in the next step.
   
   Refer to the Snowflake [Key-pair authentication and key-pair rotation](https://docs.snowflake.com/en/user-guide/key-pair-auth) guide for more information.
   
5. Run the following SQL command in a Snowflake worksheet to assign the public key to your Snowflake user:
   
   ```sql
   ALTER USER <USERNAME> SET RSA_PUBLIC_KEY='<PUBLIC_KEY>';
   ```
   
   Replace `<USERNAME>` with your Snowflake user and `<PUBLIC_KEY>` with the key content. Exclude the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` lines.
   
   > **ROLE REQUIREMENT**
   > 
   > You must have the `SYSADMIN` or `SECURITYADMIN` role to run this command.
   

#### Connect to Snowflake with key-pair authentication

Complete the following steps to set up a key-pair authentication connection to Snowflake Data Explorer in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Snowflake` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Snowflake Key-pair connection](/assets/key-pair-connection.DhSthvSv.png)_Snowflake key-pair connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the Snowflake instance **Account identifier** in one of the supported formats:
   
   - **Account name**: `https://{org_name}-{account_name}`
   - **Connection name**: `https://{org_name}-{connection_name}`
   - **Account locator**: `https://{account_locator}.{region}.{cloud}`
   
   Refer to the Snowflake [Connecting to your accounts](https://docs.snowflake.com/en/user-guide/organizations-connect#connecting-with-a-url) guide for more information.
   
   > **ACCOUNT LOCATOR FORMAT**
   > 
   > Certain locations require you to include the `{region}` and `{cloud}` in your account locator URL. For example:
   > 
   > - **AWS US West (Oregon)**: `your-account-locator`
   > - **AWS US East (Ohio)**: `your-account-locator.us-east-2`
   > - **Azure West Europe**: `your-account-locator.west-europe.azure`
   > 
   > Refer to the Snowflake [Using an account locator as an identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier#using-an-account-locator-as-an-identifier) guide for more information.
   
6. Enter the **Warehouse** name to define the compute resources for this connection. Refer to [Warehouse considerations](/en/connectors/snowflake#warehouse-considerations) for more information.
   
7. Enter the **Database name** for the target Snowflake database.
   
8. Use the **Authentication type** drop-down menu to select **Key-pair authentication**.
   
9. Enter the **User name** and **Private key**. Refer to [Snowflake setup for key-pair authentication](#key-pair-setup) for information on how to retrieve these credentials.
   
10. Optional. Enter the **Private key passphrase** if you generated an encrypted private key.
    
11. Optional. Specify a **Role** for authentication. This role must be an existing role assigned to the user. If left blank, Snowflake uses the default role assigned to the user.
    
12. Optional. Enter the **Schema**. If left blank, the default schema is public.
    
13. Optional. Set the **Use improved datetime handling (Recommended)** to **Yes** to ensure correct timezone handling for timestamps.
    
14. Optional. Define the **Database timezone** to apply to timestamps without an assigned timezone. Defaults to your workspace's timezone if left blank.
    
15. Click **Connect**.
    

## How to use Snowflake Data Explorer MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_databases tool

The **list\_databases** tool lists Snowflake databases accessible within the server's configured allowlists. Your LLM uses this tool to discover available databases or begin navigating the Snowflake structure.

**Try asking**:

- `What databases are available in Snowflake?`
- `Show me all accessible databases.`
- `List the databases I can query.`
- `What data groupings exist in Snowflake?`

### list\_schemas tool

The **list\_schemas** tool lists schemas in a database you specify to navigate the Snowflake object hierarchy. Your LLM uses this tool to explore schemas within a known database.

**Try asking**:

- `List the schemas in the SALES_DATA database.`
- `What schemas exist in the ANALYTICS database?`
- `Show me available schemas in CUSTOMER_DATA.`
- `What namespaces are in this database?`

### list\_tables tool

The **list\_tables** tool lists tables in a schema you specify, with metadata suitable for discovery. Your LLM uses this tool to discover tables within a known schema.

**Try asking**:

- `Show me tables in the CUSTOMER_ANALYTICS schema.`
- `List all tables in the SALES schema.`
- `What tables can I query in MARKETING.CAMPAIGNS?`
- `Display available tables in this schema.`

### list\_views tool

The **list\_views** tool lists views in a schema you specify, with metadata suitable for discovery. Your LLM uses this tool to discover views within a known schema.

**Try asking**:

- `Show me views in the CUSTOMER_ANALYTICS schema.`
- `List all views in the SALES schema.`
- `What views can I query in MARKETING.CAMPAIGNS?`
- `Display available views in this schema.`

### search\_tables tool

The **search\_tables** tool searches for tables by name-oriented criteria when the exact location is unknown. Your LLM uses this tool to locate tables by topic or keyword rather than exact name.

**Try asking**:

- `Find tables related to subscriptions.`
- `Search for tables containing customer activity data.`
- `Look for tables about support tickets.`
- `Find any tables with 'revenue' in the name.`

### search\_views tool

The **search\_views** tool searches for views by name-oriented criteria when the exact location is unknown. Your LLM uses this tool to locate views by topic or keyword rather than exact name.

**Try asking**:

- `Find views related to subscriptions.`
- `Search for views containing customer activity data.`
- `Look for views about support tickets.`
- `Find any views with 'revenue' in the name.`

### get\_table\_schema tool

The **get\_table\_schema** tool retrieves column names, data types, and available descriptions for a specified table or view. Your LLM uses this tool to understand table structure before constructing a query.

**Try asking**:

- `What columns are in the CUSTOMER_EVENTS table?`
- `Show me the schema for SALES.TRANSACTIONS.`
- `What's the structure of the activity logs table?`
- `Get column definitions for the subscription data table.`

### get\_table\_sample tool

The **get\_table\_sample** tool returns a bounded sample of rows from a table or view to inspect values and formats before running full queries. Your LLM uses this tool to validate assumptions about data content.

**Try asking**:

- `Show me a sample of data from the activity logs table.`
- `Get some example rows from the customer events table.`
- `What does the data in the transactions table look like?`
- `Display a few sample records from subscriptions.`

### execute\_query tool

The **execute\_query** tool executes a read-only SQL query against Snowflake using the configured warehouse, subject to row quotas, timeouts, and access restrictions. Your LLM uses this tool to retrieve data using SQL, including filters, joins, and aggregations.

**Try asking**:

- `Query the top 100 customers by revenue from last quarter.`
- `Get all active subscriptions created in the last 30 days.`
- `Show me support tickets opened this week by priority.`
- `Find the total sales by region for January 2026.`

## Getting started

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/x-social-listening-and-research-mcp-server.md
description: >-
  Use the X Social Listening and Research MCP server to let LLMs monitor brand
  mentions, track competitors, and research X accounts.
---

# X Social Listening and Research MCP server

The X (formerly Twitter) Social Listening and Research MCP server enables LLMs to interact with X for social listening, brand monitoring, competitive intelligence, and content research workflows through natural conversation. It provides tools to monitor brand mentions, track competitors, compare metrics, explore trending topics, and research accounts without requiring direct interaction with the X interface.

## Uses

Use the X Social Listening and Research MCP server to perform the following actions:

- Search for tweets by keywords, hashtags, mentions, or phrases
- Retrieve specific tweets with full metadata
- Read conversation threads and reply chains
- Look up user profiles and verify accounts
- View recent tweets from specific accounts
- Discover accounts related to topics or industries
- Compare engagement metrics across multiple tweets
- Monitor brand mentions and competitor activity
- Research trending topics and conversations

### Example prompts

Use the following example prompts to invoke X Social Listening and Research MCP server tools:

- `Search for recent tweets mentioning our product.`
- `Get the details for this specific tweet.`
- `Show me the full thread for this conversation.`
- `Look up the @acme profile.`
- `What has @competitor been posting recently?`
- `Find X accounts that post about AI automation.`
- `Compare engagement metrics for these five tweets.`
- `Monitor mentions of our brand from the past week.`

## X Social Listening and Research MCP server tools

The X Social Listening and Research MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_tweets](#search-tweets-tool) | Searches public tweets matching a keyword, hashtag, mention, or phrase. |
| [get\_tweet](#get-tweet-tool) | Retrieves a single tweet with full metadata by tweet ID or URL. |
| [get\_tweet\_thread](#get-tweet-thread-tool) | Retrieves the full conversation thread for a tweet you specify. |
| [get\_user\_profile](#get-user-profile-tool) | Retrieves the public profile of an X account by handle or user ID. |
| [get\_user\_recent\_tweets](#get-user-recent-tweets-tool) | Retrieves the most recent public tweets posted by an X account you specify. |
| [search\_users](#search-users-tool) | Searches for X accounts matching a name, keyword, or topic description. |
| [batch\_get\_tweet\_metrics](#batch-get-tweet-metrics-tool) | Retrieves engagement metrics for a batch of tweet IDs in a single call. |

## Install the X Social Listening and Research MCP server

Complete the following steps to install a prebuilt MCP server to your project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
5. Click **Use this server**.
   
6. Provide a name for your MCP server in the **Server name** field.
   
7. Use the **Location** drop-down menu to select the project for the MCP server.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the MCP server template.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   ![Select your connection type](/assets/connection-type.Cor-6PJN.png)_Select your connection type_
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Complete the app-specific connection setup steps in the following section.
    

## X connection setup

View X connection setup steps

The X connector uses OAuth 1.0a authentication.

Complete the following steps to connect to X in Workato with 1.0a authentication:

#### Generate a consumer key and secret

View generate a consumer key and secret steps

Complete the following steps to generate a consumer key and secret in X:

1. Sign in to the [X Developer Console](https://console.x.com).
   
2. Click **Apps > Create App**.
   
3. Enter an **Application Name**.
   
4. Select an **Environment**.
   
5. Click **Create New Client Application**.
   
6. Copy and save the **Consumer Key** and **Secret Key** for use in Workato.
   
   > **SAVE YOUR CREDENTIALS**
   > 
   > The credentials only display once. If you lose them, you must generate new ones.
   

#### Generate an access token and secret

View generate an access token and secret steps

Complete the following steps to generate an access token and secret in X:

1. Sign in to the [X Developer Console](https://console.x.com).
   
2. Click **Apps**.
   
3. Click on the app you created in the preceding steps.
   
4. Under **OAuth 1.0 Keys**, click **Generate** for **Access Token**.
   
5. Copy and save the **Access Token** and **Access Token Secret** for use in Workato.
   
   > **SAVE YOUR CREDENTIALS**
   > 
   > The credentials only display once. If you lose them, you must generate new ones.
   

### Connect to X with OAuth 1.0a

View connect to X with OAuth 1.0a steps

1. Click **Create > Connection**.
   
2. Search for `X` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![X connection setup](/assets/x-connection-setup.C74ieFMu.png)_X connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Consumer key** and **Consumer secret**.
   
6. Enter the **Access token** and **Access token secret**.
   
7. Click **Connect**.
   

## How to use X Social Listening and Research MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_tweets tool

The **search\_tweets** tool searches public tweets matching a keyword, hashtag, mention, or phrase. Your LLM uses this tool to find tweets about specific topics, monitor brand mentions, track hashtags, or discover conversations.

**Try asking**:

- `Search for recent tweets mentioning our product.`
- `Find tweets about #AI automation from the past week.`
- `Look for tweets mentioning @acme.`
- `Search for conversations about low-code platforms.`

### get\_tweet tool

The **get\_tweet** tool retrieves a single tweet with full metadata by tweet ID. Your LLM uses this tool when you provide a specific tweet ID or URL to retrieve full details of a particular tweet, or to follow up after a search to get complete metadata on a specific result.

**Try asking**:

- `Get the details for tweet ID 1234567890.`
- `Show me the full metadata for this tweet.`
- `Retrieve the engagement metrics for this specific tweet.`
- `Get complete information about tweet 123456.`

### get\_tweet\_thread tool

The **get\_tweet\_thread** tool retrieves the full conversation thread for a tweet you specify. Your LLM uses this tool to understand the full context of a conversation, read a thread, see replies to a specific tweet, or to understand the full exchange when a search result appears to be part of a larger discussion.

**Try asking**:

- `Show me the full thread for this tweet.`
- `Read the entire conversation thread.`
- `Get all the replies in this X thread.`
- `Show me the complete discussion starting from this tweet.`

### get\_user\_profile tool

The **get\_user\_profile** tool retrieves the public profile of an X account by handle or user ID. Your LLM uses this tool to look up an X account, find information about a specific @handle, understand an account's reach and focus area, or verify an account.

**Try asking**:

- `Look up the @acme X profile.`
- `Get information about @competitor's account.`
- `What's the follower count for @brandaccount?`
- `Verify the profile for @influencer.`

### get\_user\_recent\_tweets tool

The **get\_user\_recent\_tweets** tool retrieves the most recent public tweets posted by an X account you specify. Your LLM uses this tool to see what a specific account has been posting recently, review an account's content, or to understand a competitor's recent messaging.

**Try asking**:

- `What has @competitor been posting recently?`
- `Show me @acme's recent tweets.`
- `Get the latest posts from @brandaccount.`
- `Review what @influencer has tweeted this week.`

### search\_users tool

The **search\_users** tool searches for X accounts matching a name, keyword, or topic description. Your LLM uses this tool to find accounts related to a topic, industry, or keyword rather than looking up a known handle, or for influencer discovery and finding brand accounts.

**Try asking**:

- `Find X accounts that post about AI automation.`
- `Search for accounts focused on B2B SaaS.`
- `Discover influencers in the marketing technology space.`
- `Find brand accounts related to customer success.`

### batch\_get\_tweet\_metrics tool

The **batch\_get\_tweet\_metrics** tool retrieves engagement metrics for a batch of tweet IDs in a single call. Your LLM uses this tool only when comparing or ranking engagement across 5 or more tweets where the tweet content has already been retrieved and only metrics are needed.

**Try asking**:

- `Compare engagement metrics for these five tweets.`
- `Which of these tweets performed best?`
- `Get the metrics for this batch of tweet IDs.`
- `Rank these tweets by engagement.`

## Getting started

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/zoominfo-b2b-intelligence-mcp-server.md
description: >-
  Use the ZoomInfo B2B Intelligence MCP server to connect your LLM to ZoomInfo
  with tools to search and enrich B2B company and contact data, discover buying
  intent, and research accounts through natural language.
---

# ZoomInfo B2B Intelligence MCP server

The ZoomInfo B2B Intelligence MCP server enables LLMs to search and enrich B2B company and contact data from ZoomInfo through natural conversation. It provides tools to find companies and contacts, discover accounts showing buying intent, enrich records with full profiles, retrieve intent signals, news, scoops, corporate hierarchy, organization charts, and technology stacks without requiring direct interaction with the ZoomInfo interface.

ZoomInfo operates on a credit-based model where search operations return free previews and enrichment operations consume credits. The server enforces a strict preview-then-enrich pattern in which search tools return identification-level data at no cost, and enrichment tools consume credits only when you explicitly approve.

## Uses

Use the ZoomInfo B2B Intelligence MCP server to perform the following actions:

- Look up valid filter values for search and enrichment parameters
- Check current API credit balance and usage quotas
- Search companies by firmographic and technographic criteria
- Search contacts by title, seniority, department, and company attributes
- Discover companies showing buying intent for specified topics
- Enrich a company record with its full ZoomInfo profile
- Enrich a contact record with full profile details
- Retrieve intent signals and recommended contacts for a known company
- Get recent news articles and proprietary scoops for a company
- Retrieve parent/subsidiary structure and company locations
- Map organizational reporting relationships at a company
- Retrieve the technology stack installed at a company

### Example prompts

Use the following example prompts to invoke ZoomInfo B2B Intelligence MCP server tools:

- `Find SaaS companies in Texas with 200–500 employees.`
- `Search for VP of Sales contacts at mid-market financial services firms.`
- `Which companies are showing buying intent for cybersecurity?`
- `Enrich the company profile for Acme Corp.`
- `Get full contact details for this lead before I reach out.`
- `What are the intent signals for Salesforce this week?`
- `What's in the news for HubSpot lately?`
- `Show me the corporate hierarchy for Microsoft.`
- `Who reports to the CTO at Stripe?`
- `What technologies does Shopify have installed?`
- `How many credits do I have remaining?`

## ZoomInfo B2B Intelligence MCP server tools

The ZoomInfo B2B Intelligence MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [lookup\_filter\_values](#lookup-filter-values-tool) | Returns valid filter values for ZoomInfo search and enrichment parameters. |
| [check\_usage](#check-usage-tool) | Returns current API credit balance, request quotas, and record quotas. |
| [search\_companies](#search-companies-tool) | Searches ZoomInfo companies by firmographic and technographic criteria. Returns free preview records. |
| [search\_contacts](#search-contacts-tool) | Searches contacts by title, seniority, department, and company attributes. Returns free previews. |
| [search\_intent](#search-intent-tool) | Discovers companies showing buying intent for topics you specify across the ZoomInfo database. |
| [enrich\_company](#enrich-company-tool) | Retrieves the full ZoomInfo company profile. Consumes 1 credit per new record. |
| [enrich\_contact](#enrich-contact-tool) | Retrieves the full ZoomInfo contact profile. Consumes 1 credit per new record. |
| [get\_intent\_signals](#get-intent-signals-tool) | Retrieves intent signal scores and recommended contacts for a specific company. Consumes 1 credit per company. |
| [get\_company\_news](#get-company-news-tool) | Retrieves recent news articles and proprietary scoops for a company. Consumes 1 credit per company. |
| [get\_corporate\_hierarchy](#get-corporate-hierarchy-tool) | Retrieves parent/subsidiary structure and company locations. Consumes 1 credit per company. Requires Advanced+ tier. |
| [get\_org\_chart](#get-org-chart-tool) | Retrieves organizational chart and reporting relationships at a company. Consumes 1 credit per company. Requires Advanced+ tier. |
| [get\_company\_technologies](#get-company-technologies-tool) | Retrieves the technology stack installed at a company. Consumes 1 credit per company. Requires Advanced+ tier. |

## Install the ZoomInfo B2B Intelligence MCP server

Complete the following steps to install a prebuilt MCP server to your project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
5. Click **Use this server**.
   
6. Provide a name for your MCP server in the **Server name** field.
   
7. Use the **Location** drop-down menu to select the project for the MCP server.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the MCP server template.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   ![Select your connection type](/assets/connection-type.Cor-6PJN.png)_Select your connection type_
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Complete the app-specific connection setup steps in the following section.
    

### ZoomInfo connection setup

View ZoomInfo connection setup steps

Complete the following steps to set up your ZoomInfo connection:

> **REQUIRED ZOOMINFO PERMISSIONS**
> 
> Your ZoomInfo account must have [ZoomInfo API](https://docs.zoominfo.com/reference/overview) access permissions to connect to Workato.

1. Enter a name for your connection in the **Connection name** field.
   
   ![Set up your ZoomInfo connection](/assets/zoominfo.BGW04mkl.png)_Set up your ZoomInfo connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store your connection.
   
3. Enter your ZoomInfo username in the **Username** field.
   
4. Enter your ZoomInfo password in the **Password** field.
   
5. Click **Connect**.
   

### Project property configuration

The ZoomInfo B2B Intelligence MCP server supports the following project-level properties to control behavior and defaults:

| Project-level property | Description |
| --- | --- |
| `max_search_results` | Maximum records per search call. Defaults to the maximum allowed: `25`. |
| `max_news_results` | Maximum news/scoop items per get\_company\_news call. Defaults to `25`. |
| `max_intent_topics` | Maximum intent topics per request. Defaults to the maximum allowed: `50`. |
| `default_output_fields` | Default field set for enrich tools when `output_fields` are omitted. |
| `credit_confirmation` | LLM must confirm with the user before calling credit-consuming tools. Estimate total cost and seek batch approval for multi-tool workflows. Set to `true` by default. |
| `credits_consumed_in_response` | All credit-consuming tools include a `credits_consumed` field in their response for running cost tracking. Set to `true` by default. |
| `smart_filter_resolution` | For common filters, such as industry or seniority, the server resolves natural-language terms internally. Subscription-scoped filters, such as intent topics, require explicit lookup. |
| `api_rate_limit` | ZoomInfo API rate limit. Server handles `429` with backoff. Defaults to `1500/min`. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/zendesk-knowledge-base-project-property.DGAT1hbT.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and make your changes. For example, set `max_search_results` to `15` or `max_intent_topics` to `25`.
   

## How to use ZoomInfo B2B Intelligence MCP server tools

Refer to the following sections for detailed information on available tools:

### lookup\_filter\_values tool

The **lookup\_filter\_values** tool returns valid filter values for ZoomInfo search and enrichment parameters. Your LLM uses this tool when you mention an industry, title, technology, or intent topic by name.

**Try asking**:

- `What industries are available as search filters?`
- `Show me valid intent topics for my subscription.`
- `What title filters can I use for contact search?`
- `Look up valid values for the technology filter.`

### check\_usage tool

The **check\_usage** tool returns your current API credit balance, request quotas, and record quotas. Your LLM uses this tool before running workflows that call multiple enrichment tools, or when you ask about remaining credits.

**Try asking**:

- `How many credits do I have left?`
- `Check my API usage before I run this enrichment.`
- `What are my current request limits?`
- `Am I close to hitting my record limits?`

### search\_companies tool

The **search\_companies** tool searches ZoomInfo companies by firmographic and technographic criteria and returns free preview records. Your LLM uses this tool to find companies by criteria, such as industry, size, location, or technology, and to build prospecting lists of target accounts.

**Try asking**:

- `Find SaaS companies in California with 200–500 employees.`
- `Search for manufacturing companies using Salesforce.`
- `Show me Series B startups in the healthcare industry.`
- `Build a list of logistics companies headquartered in Chicago.`

### search\_contacts tool

The **search\_contacts** tool searches contacts by title, seniority, department, and company attributes and returns free previews. Your LLM uses this tool to find people by role or department, locate decision-makers at companies, or build a contact list for outreach.

**Try asking**:

- `Find VP of Sales contacts at mid-market financial services firms.`
- `Search for IT decision-makers at enterprise healthcare companies.`
- `Show me marketing directors at companies using HubSpot.`
- `Find C-suite contacts at Series A startups in New York.`

### search\_intent tool

The **search\_intent** tool discovers companies showing buying intent for topics you specify across the ZoomInfo database. Your LLM uses this tool to find new accounts by intent signals and prioritize outreach by identifying high-intent accounts. Intent topics are subscription-scoped.

**Try asking**:

- `Which companies are showing buying intent for cybersecurity?`
- `Find accounts with high intent for cloud migration tools.`
- `Discover companies researching HR software right now.`
- `Show me high-intent accounts for data analytics.`

### enrich\_company tool

The **enrich\_company** tool retrieves the full ZoomInfo company profile. This tool consumes **1 credit per new record**. Your LLM confirms with you before calling this tool, and estimates total credits upfront when part of a multi-tool workflow.

**Try asking**:

- `Enrich the company profile for Acme Corp.`
- `Get full firmographic details for this account.`
- `I want the complete ZoomInfo profile for Stripe.`
- `Enrich this company record before the meeting.`

### enrich\_contact tool

The **enrich\_contact** tool retrieves the full ZoomInfo contact profile, including email, phone, and employment history. This tool consumes **1 credit per new record**. Your LLM confirms with you before calling this tool and estimates total credits upfront for batch enrichment.

**Try asking**:

- `Get full contact details for this lead before I reach out.`
- `Enrich this contact record with email and phone.`
- `I need the complete profile for this decision-maker.`
- `Enrich these 5 contacts before the outreach campaign.`

### get\_intent\_signals tool

The **get\_intent\_signals** tool retrieves intent signal scores and recommended contacts for a specific known company. This tool consumes **1 credit per company**. Your LLM calls **lookup\_filter\_values** first to confirm valid intent topics for your subscription.

**Try asking**:

- `What are the intent signals for Salesforce this week?`
- `Check buying signals for this target account.`
- `Show me intent scores and recommended contacts at HubSpot.`
- `What topics is this company researching right now?`

### get\_company\_news tool

The **get\_company\_news** tool retrieves recent news articles and proprietary scoops for a company. This tool consumes **1 credit per company**. Your LLM uses this tool when you ask what's happening at a company, need context for account briefings, or need to surface signals like funding rounds, leadership changes, or expansion activity.

**Try asking**:

- `What's in the news for HubSpot lately?`
- `Prepare an account briefing for Stripe with recent news.`
- `Has this company had any leadership changes recently?`
- `Show me recent funding or expansion news for this account.`

### get\_corporate\_hierarchy tool

The **get\_corporate\_hierarchy** tool retrieves parent/subsidiary structure and company locations for an account. This tool consumes **1 credit per company** and requires an **Advanced+ tier** subscription. Use this tool to understand corporate structure before multi-entity engagement. Use **get\_org\_chart** for reporting relationships between people.

If Advanced+ is unavailable, your LLM will suggest `enrich_company` as a fallback for basic parent company information.

**Try asking**:

- `Show me the corporate hierarchy for Microsoft.`
- `What subsidiaries does this enterprise account have?`
- `Who is the parent company of this organization?`
- `Map the corporate structure for this account before the deal review.`

### get\_org\_chart tool

The **get\_org\_chart** tool retrieves the organizational chart and reporting relationships at a company. This tool consumes **1 credit per company** and requires an **Advanced+ tier** subscription. Use this tool to map a buying committee or decision-making chain. Use **get\_corporate\_hierarchy** for parent/subsidiary corporate structure.

**Try asking**:

- `Who reports to the CTO at Stripe?`
- `Map the buying committee at this target account.`
- `Show me the org chart for the engineering division.`
- `Who are the direct reports to the VP of Marketing here?`

### get\_company\_technologies tool

The **get\_company\_technologies** tool retrieves the technology stack installed at a company. This tool consumes **1 credit per company** and requires an **Advanced+ tier** subscription. Use this tool for competitive displacement analysis or to assess solution fit based on existing tech. Use **search\_companies** with a tech filter to search for companies _by_ technology.

**Try asking**:

- `What technologies does Shopify have installed?`
- `Is this account running Salesforce or HubSpot?`
- `Check the tech stack at this company before the demo.`
- `Does this prospect use any of our competitor's products?`

## Getting started

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.

---
