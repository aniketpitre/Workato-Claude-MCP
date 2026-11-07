---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/canva-mcp-server.md'
description: >-
  Use the Canva MCP server to connect your LLM to Canva with repeatable,
  structured management of designs, assets, folders, and brand templates.
---

# Canva MCP server

The Canva MCP server enables LLMs to interact with Canva for structured design and content operations through natural conversation. It provides tools to search designs, retrieve design metadata, organize designs and assets into folders, upload reusable assets, export designs into shareable formats, and generate branded designs from templates without requiring direct interaction with the Canva interface.

## Uses

Use the Canva MCP server to perform the following actions:

- Search for existing designs using keywords and filters
- Retrieve metadata and access links for a specific design
- Export a design in a shareable format
- Upload reusable assets from a URL
- Create folders for asset organization
- List the contents of a folder
- Track the status of export and asset upload jobs
- Track the status of autofill jobs (requires Canva Enterprise)
- Discover brand templates (requires Canva Enterprise)
- Retrieve the dataset schema that defines a brand template's autofill fields (requires Canva Enterprise)
- Generate a branded design by autofilling a template with structured data (requires Canva Enterprise)

### Example prompts

Use the following example prompts to invoke Canva MCP server tools:

- `Find all designs that mention our Q3 product launch.`
- `Get the metadata and shareable link for the design titled Sales Deck Template.`
- `What export formats are available for this design?`
- `Export this design as a PDF and give me the download link.`
- `Check the status of the export job I started for the campaign deck.`
- `Upload this logo image from the URL and make it available in Canva.`
- `Show me everything inside the Marketing Assets folder.`
- `Create a new folder called Q3 Campaign and move these designs into it.`
- `Move this asset into the Brand Library folder.`
- `Get the metadata for the asset I just uploaded.`
- `Get the design created by the autofill job I started.`
- `Show me the brand templates I can use to generate a sales deck.`
- `Generate a branded design from the Q3 Sales template using this account data.`
- `Check the status of the autofill job for the account deck.`

## Canva MCP server tools

The Canva MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_designs](#search-designs-tool) | Searches Canva designs using keywords and filters. |
| [get\_design](#get-design-tool) | Retrieves metadata and access links for a Canva design. |
| [get\_design\_export\_formats](#get-design-export-formats-tool) | Retrieves available export formats for a Canva design. |
| [create\_design\_export\_job](#create-design-export-job-tool) | Initiates an export job for a Canva design. |
| [get\_design\_export\_job](#get-design-export-job-tool) | Retrieves the status and result of a Canva design export job. |
| [upload\_asset\_from\_url](#upload-asset-from-url-tool) | Uploads an image or video asset to Canva from a URL. |
| [get\_asset\_upload\_job](#get-asset-upload-job-tool) | Retrieves the status and result of an asset upload job. |
| [get\_asset](#get-asset-tool) | Retrieves metadata for a Canva asset. |
| [list\_folder\_items](#list-folder-items-tool) | Lists the contents of a Canva folder. |
| [create\_folder](#create-folder-tool) | Creates a folder in Canva. |
| [move\_to\_folder](#move-to-folder-tool) | Moves a design, asset, or folder to another folder. |
| [list\_brand\_templates](#list-brand-templates-tool) | Lists available Canva brand templates. Requires Canva Enterprise. |
| [get\_brand\_template\_dataset](#get-brand-template-dataset-tool) | Retrieves the dataset schema for a Canva brand template. Requires Canva Enterprise. |
| [create\_design\_autofill\_job](#create-design-autofill-job-tool) | Creates a new design by autofilling a Canva brand template. Requires Canva Enterprise. |
| [get\_design\_autofill\_job](#get-design-autofill-job-tool) | Retrieves the status and result of a Canva autofill job. Requires Canva Enterprise. |

## Install the Canva MCP server

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
    

## Canva Connect connection setup

View Canva Connect connection setup steps

The Canva Connect connector uses OAuth 2.0 authentication.

### Install Canva Connect from the community library

View install Canva Connect from the community library steps

Complete the following steps to install the Canva Connect connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Minimum and default scopes

View minimum and default scopes

Canva Connect grants the connection every available scope if you don't select any scopes when you connect. Available scopes include:

- `Asset:read`
- `Asset:write`
- `Brandtemplate:content:read`
- `Brandtemplate:meta:read`
- `Collaboration:event`
- `Comment:read`
- `Comment:write`
- `Design:content:read`
- `Design:content:write`
- `Design:meta:read`
- `Design:permission:read`
- `Design:permission:write`
- `Folder:permission:read`
- `Folder:permission:write`
- `Folder:read`
- `Folder:write`
- `Profile:read`

### Canva Connect setup for OAuth 2.0 authentication

View Canva Connect setup for OAuth 2.0 authentication steps

Complete the following steps to create a Canva integration and generate credentials for Workato:

1. Sign in to Canva and go to the [Connect API integrations](https://www.canva.com/developers/integrations/connect-api) in the Canva Developer Portal.
   
2. Click **Create an integration** to create a new integration.
   
3. Select the **Integration type**.
   
4. Provide a name for your integration in the **Name** field.
   
5. Scroll down to the **Credentials** tab to access your **Client ID** and **Client secret**.
   
6. Copy the **Client ID** and save it securely.
   
7. Click **Generate secret** to reveal your **Client secret**.
   
8. Copy the **Client secret** and save it securely.
   
9. Click the **Scopes** tab and provide any scopes you plan to use. Refer to [Minimum and default scopes](#scopes) for more information.
   

### Connect to Canva Connect using OAuth 2.0 authentication

View connect to Canva Connect using OAuth 2.0 authentication steps

Complete the following steps to connect to Canva Connect in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Canva Connect` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your client ID in the **Client ID** field.
   
6. Enter your client secret in the **Client secret** field.
   
7. Optional. Select the **Scopes** to request for this connection. Refer to [Minimum and default scopes](#scopes) for more information.
   
8. Click **Connect**.
   
9. Sign in to Canva when prompted and click **Allow** to authorize the connection.
   

## How to use Canva MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_designs tool

The **search\_designs** tool searches Canva designs using keywords and filters. Your LLM uses this tool to locate existing designs by topic, name, or other criteria so it can retrieve, export, or organize them in subsequent steps.

**Try asking**:

- `Find all designs related to our summer campaign.`
- `Search for designs that mention onboarding.`
- `Show me the most recent designs that include the word webinar.`

### get\_design tool

The **get\_design** tool retrieves metadata and access links for a Canva design. Your LLM uses this tool to inspect a specific design's details and obtain links to view or share it after identifying it through a search.

**Try asking**:

- `Get the details for the design titled Q3 Sales Deck.`
- `Give me the shareable link for this design.`
- `What's the metadata for the design I just found?`

### get\_design\_export\_formats tool

The **get\_design\_export\_formats** tool retrieves available export formats for a Canva design. Your LLM uses this tool to determine which formats a design can be exported into before initiating an export job.

**Try asking**:

- `What export formats are available for this design?`
- `Can I export this design as a PDF?`
- `List the file types I can export this deck to.`

### create\_design\_export\_job tool

The **create\_design\_export\_job** tool initiates an export job for a Canva design. Your LLM uses this tool to start exporting a design into a chosen shareable format for distribution.

**Try asking**:

- `Export this design as a PDF.`
- `Start an export job for this deck in PNG format.`
- `Create an export of the campaign design so I can share it.`

### get\_design\_export\_job tool

The **get\_design\_export\_job** tool retrieves the status and result of a Canva design export job. Your LLM uses this tool to check whether an export has completed and to obtain the resulting download links.

**Try asking**:

- `Check the status of my export job.`
- `Is the PDF export finished yet?`
- `Get the download link for the completed export.`

### upload\_asset\_from\_url tool

The **upload\_asset\_from\_url** tool uploads an image or video asset to Canva from a URL. Your LLM uses this tool to bring reusable assets into Canva so they can be referenced across designs and templates.

**Try asking**:

- `Upload this logo image from the URL into Canva.`
- `Add this product photo from this link as an asset.`
- `Upload the video at this URL to Canva.`

### get\_asset\_upload\_job tool

The **get\_asset\_upload\_job** tool retrieves the status and result of an asset upload job. Your LLM uses this tool to confirm that an asset upload has completed and to obtain the resulting asset reference.

**Try asking**:

- `Check the status of my asset upload.`
- `Has the logo finished uploading?`
- `Get the result of the upload job I started.`

### get\_asset tool

The **get\_asset** tool retrieves metadata for a Canva asset. Your LLM uses this tool to inspect the details of an existing asset before reusing it in a design or moving it into a folder.

**Try asking**:

- `Get the metadata for the asset I just uploaded.`
- `Show me the details of this asset.`
- `What are the properties of this image asset?`

### list\_folder\_items tool

The **list\_folder\_items** tool lists the contents of a Canva folder. Your LLM uses this tool to review the designs, assets, and subfolders stored in a folder when organizing or locating content.

**Try asking**:

- `Show me everything inside the Marketing Assets folder.`
- `List the designs in the Q3 Campaign folder.`
- `What's stored in this folder?`

### create\_folder tool

The **create\_folder** tool creates a folder in Canva. Your LLM uses this tool to set up new folders for organizing designs and assets.

**Try asking**:

- `Create a folder called Q3 Campaign.`
- `Make a new folder named Brand Library.`
- `Set up a folder for our webinar assets.`

### move\_to\_folder tool

The **move\_to\_folder** tool moves a design, asset, or folder to another folder. Your LLM uses this tool to reorganize content by relocating items into the appropriate folder.

**Try asking**:

- `Move this design into the Q3 Campaign folder.`
- `Relocate this asset to the Brand Library folder.`
- `Move these designs into the Archive folder.`

### list\_brand\_templates tool

The **list\_brand\_templates** tool lists available Canva brand templates. Your LLM uses this tool to discover templates so it can generate branded designs from structured data or answer user questions. This tool requires a Canva Enterprise plan.

**Try asking**:

- `Show me the brand templates I can use to generate a sales deck.`
- `List the Canva templates that support autofill.`
- `Find brand templates for marketing campaigns.`

### get\_brand\_template\_dataset tool

The **get\_brand\_template\_dataset** tool retrieves the dataset schema for a Canva brand template. Your LLM uses this tool to determine which fields a template requires, and their types, before generating a design through autofill. This tool requires a Canva Enterprise plan.

**Try asking**:

- `What fields does this brand template need for autofill?`
- `Get the dataset schema for the Q3 Sales template.`
- `Show me the required inputs for this template.`

### create\_design\_autofill\_job tool

The **create\_design\_autofill\_job** tool creates a new design by autofilling a Canva brand template. Your LLM uses this tool to generate a branded design by applying structured data and image assets to a template's dataset fields. This tool requires a Canva Enterprise plan.

**Try asking**:

- `Generate a branded design from the Q3 Sales template using this account data.`
- `Autofill this template with the customer details and create a design.`
- `Create a sales deck from the brand template with these values.`

### get\_design\_autofill\_job tool

The **get\_design\_autofill\_job** tool retrieves the status and result of a Canva autofill job. Your LLM uses this tool to check whether an autofill job has completed and to obtain the generated design. This tool requires a Canva Enterprise plan.

**Try asking**:

- `Check the status of my autofill job.`
- `Is the generated design ready yet?`
- `Get the design created by the autofill job I started.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/clay-contact-company-explorer-mcp-server.md
description: >-
  Read-only lookups for company and contact data from Clay, covering
  firmographics, funding, and professional profiles for prospecting and account
  research.
---

# Clay Contact & Company Explorer MCP server

The Clay Contact & Company Explorer MCP server enables LLMs to interact with Clay for prospecting, research, and qualification workflows through natural conversation. It provides tools to retrieve enriched company profiles, funding information, and contact details without requiring direct interaction with the Clay interface.

## Uses

Use the Clay Contact & Company Explorer MCP server to perform the following actions:

- Research a company's profile and funding before outbound calls
- Look up a contact's role and background using their name and company
- Qualify companies against your ideal customer profile (ICP) criteria
- Explore account information for expansion and upsell opportunities
- Identify stakeholders and decision-makers within target accounts
- Discover companies matching specific industry, size, or technology criteria
- Retrieve firmographic data including industry, employee size, and location
- Get a company's total funding and revenue range for account prioritization

### Example prompts

Use the following example prompts to invoke Clay Contact & Company Explorer MCP server tools:

- `Tell me about acme.com's total funding and industry`
- `What's the background of Kai Chen at AcmeCo.com?`
- `Find engineering managers at AcmeCo.com`
- `List companies in the SaaS industry with 50-500 employees`
- `Is AcmeCo.com a good fit for our ICP?`
- `Who are the C-suite executives at AcmeCo.com?`
- `What companies use Salesforce in the healthcare industry?`
- `What's the company size and location for AcmeCo?`
- `Find companies in New York with over $50M in total funding`

## Clay Contact & Company Explorer MCP server tools

The Clay Contact & Company Explorer MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_company\_profile](#get-company-profile-tool) | Retrieve firmographic details for a company using its domain or name. |
| [get\_company\_funding](#get-company-funding-tool) | Retrieve a company's total funding amount range and estimated annual revenue range. |
| [get\_person\_profile](#get-person-profile-tool) | Retrieve a professional profile for an individual using their full name and company. |
| [search\_people](#search-people-tool) | Search for people at a company by title, seniority, name, and location. |
| [search\_companies](#search-companies-tool) | Search for companies by industry, employee size, funding amount, company type, technology, and location. |

## Install the Clay Contact & Company Explorer MCP server

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
    

## Clay Contact & Company Explorer connection setup

View Clay Contact & Company Explorer connection setup steps

Ensure you complete the following steps before using the Clay connector in Workato:

- [Download Clay from the community](#download-clay-from-the-community)
- [Retrieve API key in Clay](#retrieve-api-key-in-clay)

### Download Clay from the community

View Download Clay from the community steps

Complete the following steps to install the Clay connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Retrieve API key in Clay

Refer to the Clay [Find your API key](https://university.clay.com/docs/guide-find-clay-api-key) guide to retrieve your Clay API key.

### Connect to Clay on Workato

View Connect to Clay on Workato steps

Complete the following steps to connect your Clay account to Workato:

1. Click **Create > Connection**.
   
2. Search for `Clay` and select it as your connection on the **New Connection** page.
   
3. Enter a name for the connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter the Clay **API key**. Refer to [Retrieve API key in Clay](#retrieve-api-key-in-clay) to obtain this value.
   
6. Click **Connect**.
   

### Clay role requirements

Each tool's availability depends on the access scope and entitlement tier of your connected Clay account. If the connected account lacks the required entitlement for a tool, that tool returns a permission-denied outcome instead of a partial result. The Clay Contact & Company Explorer MCP server doesn't perform additional user-level permission checks beyond what the Clay API enforces. Refer to Clay's [Roles and permissions](https://university.clay.com/docs/roles-and-permissions) guide for the complete list of role capabilities.

## How to use Clay Contact & Company Explorer MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_company\_profile tool

The **get\_company\_profile** tool retrieves firmographic details for a company using its domain or name. Your LLM uses this tool to gather core company information including industry, employee size, location, description, and available funding and revenue range indicators.

**Try asking**:

- `What industry is Acme Inc in and how many employees do they have?`
- `Tell me about AcmeCo's headquarters location and company description`
- `Get the company profile for example.com`

### get\_company\_funding tool

The **get\_company\_funding** tool retrieves a company's total funding amount range and estimated annual revenue range using its domain or LinkedIn company URL. Your LLM uses this tool to gauge company maturity as a growth signal for account prioritization and qualification.

**Try asking**:

- `What's the total funding and revenue range for AcmeCo.com?`
- `How much capital has techstart.com raised in total?`
- `Is AcmeCo.com a mature, well-funded company?`

### get\_person\_profile tool

The **get\_person\_profile** tool retrieves a professional profile for an individual using their full name together with their company's domain or LinkedIn URL. Your LLM uses this tool to understand a contact's title, location, and LinkedIn profile for personalized outreach and account planning. This tool doesn't accept email addresses or personal LinkedIn URLs as identifiers, so your LLM pairs the person's full name with their company.

**Try asking**:

- `Tell me about Dana Patel at acme.com`
- `Who is Alex Nguyen at AcmeCo.com?`
- `Get the professional profile for Taylor Park at acme.com`

### search\_people tool

The **search\_people** tool searches for people at a company by title, seniority, name, and location. Your LLM uses this tool to identify decision-makers, influencers, and relevant personas for multi-threaded outreach and stakeholder mapping within target accounts.

**Try asking**:

- `Find engineering managers at AcmeCo.com`
- `Who are the C-suite executives at AcmeCo.com?`
- `Find VP of Sales roles across multiple companies`
- `Find finance directors in New York`

### search\_companies tool

The **search\_companies** tool searches for companies by industry, employee size, funding amount, company type, technology, and location. Your LLM uses this tool to discover prospects matching your ideal customer profile, identify companies using specific technologies, and support prospect research and lead generation workflows.

**Try asking**:

- `List companies in the SaaS industry with 50-500 employees`
- `Find companies in healthcare that use Salesforce`
- `What software companies in California have raised over $50M in funding?`
- `Search for fintech companies with more than 1,000 employees`

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
