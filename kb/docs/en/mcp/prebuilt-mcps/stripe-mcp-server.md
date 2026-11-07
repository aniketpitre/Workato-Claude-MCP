---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/stripe-mcp-server.md'
description: >-
  Use the Stripe Billing Operations MCP server to connect your LLM to Stripe
  with a curated set of tools for customer lookup, payment troubleshooting,
  subscription management, invoice handling, and dispute visibility.
---

# Stripe Billing Operations

The Stripe Billing Operations MCP server enables developers and founders to manage Stripe billing operations through natural conversation. It provides tools for customer lookup, payment troubleshooting, subscription management, invoice handling, and dispute visibility without requiring direct interaction with the Stripe Dashboard.

## Uses

Use the Stripe Billing Operations MCP server when you plan to perform the following actions:

- Search for customers by email, name, or metadata
- Find and investigate payment history and failed charges
- Get detailed payment information including refund history
- Issue full or partial refunds for captured payments
- View subscription details and billing information
- Search for invoices by customer or status
- Send open invoices to customers through email
- Cancel subscriptions immediately or at period end
- Search for and manage payment disputes (chargebacks)
- Submit evidence to fight disputes or accept them

### Example prompts

Use the following example prompts to invoke Stripe MCP server tools:

- `Find the customer with email mei@acme.com.`
- `Search for failed payments from last week.`
- `Get the details for payment pi_123456.`
- `Refund $50 to the customer for payment ch_789012.`
- `What subscription plan is customer cus_ABC123 on?`
- `Find all unpaid invoices for Acme Corp.`
- `Send invoice in_XYZ789 to the customer.`
- `Cancel the subscription for customer cus_ABC123.`
- `Show me disputes that need a response.`
- `Get the evidence requirements for dispute dp_456789.`

## Stripe Billing Operations MCP server tools

The Stripe Billing Operations MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_customers](#search-customers-tool) | Finds Stripe customers by email, name, or custom metadata fields. |
| [search\_payments](#search-payments-tool) | Searches for payments by customer, status, amount range, date range, or metadata. |
| [get\_payment\_details](#get-payment-details-tool) | Retrieves complete payment details including refund history and failure information. |
| [refund\_payment](#refund-payment-tool) | Issues a full or partial refund for a captured payment. |
| [get\_subscription\_details](#get-subscription-details-tool) | Retrieves subscription status, plan details, and billing information. |
| [search\_invoices](#search-invoices-tool) | Searches for invoices by customer, status, or date range. |
| [send\_invoice](#send-invoice-tool) | Sends an open invoice to the customer through email. |
| [cancel\_subscription](#cancel-subscription-tool) | Cancels a customer's subscription either at period end or immediately. |
| [search\_disputes](#search-disputes-tool) | Searches for payment disputes (chargebacks) by status, date range, or associated payment. |
| [get\_dispute\_details](#get-dispute-details-tool) | Retrieves complete dispute details including evidence requirements. |
| [submit\_dispute\_evidence](#submit-dispute-evidence-tool) | Submits text evidence to fight a dispute. |
| [accept\_dispute](#accept-dispute-tool) | Accepts a dispute, allowing the customer to keep the disputed funds. |

## Install the Stripe Billing Operations MCP server

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
    

## Stripe connection setup

View Stripe connection setup steps

The Stripe connector supports the following authentication types:

- [API key](#api-key)
- [Authorization code grant](#authorization-code-grant)

> **LIMITATIONS**
> 
> Stripe allows only one connection per Stripe account and Stripe App pair. When you create a new App-based Stripe connection for the **same Stripe account**, it invalidates the tokens of any existing App-based connections for that account, making them inactive. However, if the connection is linked to a **different Stripe account**, existing connections remain unaffected.
> 
> This limitation doesn't impact pre-existing extension-based Stripe connections in Workato, which can coexist with App-based connections.

### API key

View API key steps

Use API key authentication to connect to Stripe using a secret key from your Stripe account.

#### Obtain an API key

Refer to [Create an API key](https://docs.stripe.com/keys#create-an-api-key) or [Reveal an API key](https://docs.stripe.com/keys#reveal-an-api-key) in the Stripe documentation.

Use your test mode secret key (`sk_test_...`) to test without affecting live data, or your live mode secret key (`sk_live_...`) to connect to your live Stripe account.

#### Connect to Stripe using API key

Complete the following steps to set up an API key connection to Stripe in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Stripe** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Stripe connection setup](/assets/connection-setup-api-key.ClloPCv7.png)_Stripe API key connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **API key**.
   
6. Enter your [API key](#api-key-setup) in the **API key** field.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   

### Authorization code grant

View Authorization code grant steps

Use authorization code grant to connect to Stripe by signing in through Stripe's authorization flow.

#### Connect to Stripe using authorization code grant

Complete the following steps to set up an authorization code grant connection to Stripe in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Stripe** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Stripe connection setup](/assets/connection-setup-auth-code-grant.DZieT5yZ.png)_Stripe authorization code grant connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
6. Use the **Demo** drop-down menu to select whether the Stripe account you plan to connect to is a demo account.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   
9. Sign in to your Stripe account when prompted and authorize the connection.
   

## How to use Stripe Billing Operations MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_customers tool

The **search\_customers** tool finds Stripe customers by email, name, or custom metadata fields. Your LLM uses this tool to find or look up a customer.

**Try asking**:

- `Find the customer with email sarah@acme.com.`
- `Search for customers named Josh Hernandez.`
- `Look up the customer with company metadata 'Acme Corp'.`
- `Find customers who signed up this month.`

### search\_payments tool

The **search\_payments** tool searches for payments by customer, status, such as succeeded, failed, or pending, amount range, date range, or metadata. Your LLM uses this tool to investigate payment history, find failed payments, or verify charges.

**Try asking**:

- `Search for failed payments from last week.`
- `Find all successful payments for customer cus_ABC123.`
- `Show me payments over $1000 from this month.`
- `Find pending payments that need attention.`

### get\_payment\_details tool

The **get\_payment\_details** tool retrieves complete payment details including amount, status, payment method, such as last4 or brand, detailed decline code and message for failed payments, full refund history, associated invoice, and metadata. Your LLM uses this tool to investigate why a payment failed, check refund status, or get full context on a specific charge.

**Try asking**:

- `Get the details for payment pi_123456789.`
- `Why did payment ch_987654321 fail?`
- `Show me the refund history for this payment.`
- `Get the complete information for the declined charge.`

### refund\_payment tool

The **refund\_payment** tool issues a full or partial refund for a captured payment. Your LLM uses this tool when you need to return funds to a customer. Payment must be captured because the LLM can't refund authorized-only payments. The refund appears on the customer's statement within 5-10 business days.

**Try asking**:

- `Refund payment pi_123456789 in full.`
- `Issue a partial refund of $50 for charge ch_987654321.`
- `Refund this payment due to customer request.`
- `Process a $25 refund marked as duplicate transaction.`

### get\_subscription\_details tool

The **get\_subscription\_details** tool retrieves subscription status, plan or product name, price, billing interval, current period dates, renewal date, and cancellation status. Your LLM uses this tool to answer questions about a customer's plan or renewal date.

**Try asking**:

- `What subscription plan is customer cus_ABC123 on?`
- `When does the subscription for sub_XYZ789 renew?`
- `Show me the subscription details for this customer.`
- `What's the billing interval for this subscription?`

### search\_invoices tool

The **search\_invoices** tool searches for invoices by customer, status, such as draft, open, paid, void, or uncollectible, or date range. Your LLM uses this tool when you need to find unpaid invoices, review billing history, or locate specific invoices for action.

**Try asking**:

- `Find all unpaid invoices for Acme Corp.`
- `Search for open invoices from this quarter.`
- `Show me draft invoices that need to be sent.`
- `Find paid invoices for customer cus_ABC123.`

### send\_invoice tool

The **send\_invoice** tool sends an open invoice to the customer by email. Your LLM uses this tool to send or resend invoices. Draft invoices are automatically finalized before sending. This tool only works for invoices with a draft or open status.

**Try asking**:

- `Send invoice in_123456 to the customer.`
- `Email the open invoice to Acme Corp.`
- `Send the draft invoice for approval.`
- `Email this invoice with the payment link.`

### cancel\_subscription tool

The **cancel\_subscription** tool cancels a customer's subscription either at period end or immediately. Your LLM uses this tool to cancel subscriptions. It doesn't automatically issue refunds.

**Try asking**:

- `Cancel the subscription for customer cus_ABC123 at period end.`
- `Immediately cancel subscription sub_XYZ789.`
- `End this customer's subscription when the current period finishes.`
- `Cancel the subscription right now.`

### search\_disputes tool

The **search\_disputes** tool searches for payment disputes by status, date range, or associated payment. Your LLM uses this tool to find disputes that require a response or review dispute history. Results are sorted by evidence deadline with the most urgent disputes listed first.

**Try asking**:

- `Show me disputes that need a response.`
- `Find all open disputes from last month.`
- `Search for disputes associated with payment pi_123456.`
- `What disputes are approaching their evidence deadline?`

### get\_dispute\_details tool

The **get\_dispute\_details** tool retrieves complete dispute details including amount, reason, status, evidence deadline, evidence requirements for this dispute type, evidence already submitted, and associated payment or customer information. Your LLM uses this tool to analyze and collect evidence before reviewing a dispute.

**Try asking**:

- `Get the evidence requirements for dispute dp_123456.`
- `Show me the details and deadline for this dispute.`
- `What evidence has been submitted for dispute dp_789012?`
- `What's the reason for this chargeback?`

### submit\_dispute\_evidence tool

The **submit\_dispute\_evidence** tool submits text evidence to fight a dispute. Your LLM uses this tool when you need to provide proof to challenge a chargeback. Evidence is saved as a draft by default.

**Try asking**:

- `Submit evidence for dispute dp_123456 with our tracking number and delivery confirmation.`
- `Add proof of delivery evidence to this dispute as a draft.`
- `Submit and finalize the evidence showing customer communication.`
- `Provide evidence that the service was delivered as promised.`

### accept\_dispute tool

The **accept\_dispute** tool accepts a dispute, allowing the customer to keep the disputed funds. Your LLM uses this tool to concede a dispute because you agree with it, lack evidence, or determine the amount isn't worth contesting.

**Try asking**:

- `Accept dispute dp_123456 because we agree with the customer.`
- `Concede this dispute since we don't have evidence.`
- `Accept the chargeback for this low-value transaction.`
- `Let the customer win this dispute.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/surveymonkey-authoring-mcp-server.md
description: >-
  Use the SurveyMonkey Authoring MCP server to connect your LLM to SurveyMonkey
  with tools to build and edit survey content through natural conversation.
---

# SurveyMonkey Authoring MCP server

The SurveyMonkey Authoring MCP server enables LLMs to interact with SurveyMonkey to build and maintain survey content through natural conversation. It provides tools to create surveys, read their structure, update survey-level settings, add and edit pages and questions, and discover templates without requiring direct interaction with the SurveyMonkey interface.

> **SERVER SCOPE**
> 
> The SurveyMonkey Authoring MCP server interacts with survey content. Use the [SurveyMonkey Distribution](/en/mcp/prebuilt-mcps/surveymonkey-distribution-mcp-server) MCP server to distribute surveys, send invitations, manage contacts, and read responses.

## Uses

Use the SurveyMonkey Authoring MCP server to perform the following actions:

- Create a blank survey, use a SurveyMonkey template, or a copy of an existing survey.
- Read a survey's full structure, including its pages and questions.
- Update survey-level settings, such as title and navigation button text.
- Add pages to a survey and edit their title, description, or position.
- Add questions to a page, including questions reused from the SurveyMonkey question bank.
- Revise an existing question's text, answer choices, or position.
- Reorder pages and questions by setting their position.
- List and filter existing surveys by title, then sort by title or modified date.
- Discover SurveyMonkey templates to base a new survey on.

### Example prompts

Use the following example prompts to invoke SurveyMonkey Authoring MCP server tools:

- `Create a new NPS survey from scratch.`
- `Start a customer-satisfaction survey from a SurveyMonkey template.`
- `Copy my last employee-engagement survey into a new one.`
- `What questions are already on this survey?`
- `Rename this survey to "Q3 Customer Feedback".`
- `Add a new page for demographic questions to my survey.`
- `Add a rating question to page 2.`
- `Change the answer choices on this multiple-choice question.`
- `Find a reusable NPS question in the question bank.`
- `Show me SurveyMonkey templates for event feedback.`

## SurveyMonkey Authoring MCP server tools

The SurveyMonkey Authoring MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_surveys](#list-surveys-tool) | Lists surveys in the account, optionally filtered by title or sorted. |
| [create\_survey](#create-survey-tool) | Creates a blank survey, or one from a SurveyMonkey template or a copy of an existing survey. |
| [get\_survey\_details](#get-survey-details-tool) | Retrieves a survey's full structure, including its pages and questions. |
| [update\_survey](#update-survey-tool) | Updates survey-level settings such as title and navigation button text. |
| [add\_page](#add-page-tool) | Adds a page to a survey. |
| [update\_page](#update-page-tool) | Updates a page's title, description, or position. |
| [add\_question](#add-question-tool) | Adds a question to a page on a survey. |
| [update\_question](#update-question-tool) | Updates an existing question's text, choices, or position. |
| [list\_question\_bank\_questions](#list-question-bank-questions-tool) | Lists SurveyMonkey question-bank questions available to reuse. |
| [list\_survey\_templates](#list-survey-templates-tool) | Lists available SurveyMonkey library templates. |

## Install the SurveyMonkey Authoring MCP server

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
    

## SurveyMonkey Authoring connection setup

View SurveyMonkey Authoring connection setup steps

Complete the following steps to connect to SurveyMonkey in Workato:

1. Provide a **Connection name** that identifies which SurveyMonkey account Workato is connected to.
   
2. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
3. Use the **Datacenter** drop-down menu to select the data center that hosts your SurveyMonkey account. Defaults to **United States**. You must use a [custom OAuth profile](/en/custom-oauth-profiles) to connect to a data center outside of the United States.
   
4. Optional. Use the **Custom OAuth profile** drop-down menu to select a [custom OAuth profile](/en/custom-oauth-profiles) for your connection. All requests to the app use the profile you specify here.
   
5. Click **Connect** to open the SurveyMonkey authorization window.
   
6. Sign in to SurveyMonkey with your account credentials. We recommend you use an admin account to avoid permission roadblocks.
   
7. Read the terms of service and click **Authorize** to complete the connection setup.
   
   > **VIEW ANSWERS REQUIREMENT**
   > 
   > Select `view answers along with responses` during authorization if you plan to use the `Completed survey response` trigger or the `Send survey invite via email and wait for response` action.
   
   ![Authorization grant](/assets/authorization_grant.mzHGoRrt.png)_Authorize Workato to access your SurveyMonkey account._
   

### SurveyMonkey Authoring role requirements

Each tool's availability depends on the plan and the OAuth scopes granted to the connected SurveyMonkey account. A request made without the required scope returns a permission-denied outcome rather than a partial result. Refer to SurveyMonkey's [OAuth scopes](https://developer.surveymonkey.com/api/v3/#scopes) documentation for the complete list of scopes and their capabilities.

## How to use SurveyMonkey Authoring MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_surveys tool

The **list\_surveys** tool lists surveys in the account, optionally filtered by title or sorted. Your LLM uses this tool to find a survey you plan to edit, copy, or inspect, narrowing a large account by a title fragment and ordering results by title or most-recently-modified date. This is a filter-and-sort list rather than a relevance-ranked search, so it presents results as a filtered list and offers to page through additional matches.

**Try asking**:

- `List my surveys sorted by most recently modified.`
- `Find surveys with "customer" in the title.`
- `Show me the surveys I can edit.`

### create\_survey tool

The **create\_survey** tool creates a blank survey, loads a SurveyMonkey template, or copies an existing survey. Your LLM uses this tool to start a new survey after you specify to create a blank survey or provide a source title, template ID, or survey ID. Blank surveys and copies of empty surveys still need at least one page and question before they can collect responses.

**Try asking**:

- `Create a blank survey called "Q3 Feedback".`
- `Start a new survey from the customer-satisfaction template.`
- `Copy my last event survey into a new one.`

### get\_survey\_details tool

The **get\_survey\_details** tool retrieves a survey's full structure, including its pages and questions. Your LLM uses this tool to read a survey's pages, questions, choices, and positions before editing so that changes target the correct page and question IDs.

**Try asking**:

- `What questions are on this survey?`
- `Show me the full structure of my onboarding survey.`
- `List the pages and questions before I make edits.`

### update\_survey tool

The **update\_survey** tool updates survey-level settings, such as title and navigation button text. Your LLM uses this tool to change a survey's title or navigation button labels after confirming which settings to change. This tool can't remove SurveyMonkey branding or the survey footer, which requires a paid plan.

**Try asking**:

- `Rename this survey to "Annual Employee Survey".`
- `Update the "Next" button label to "Continue".`
- `Change the "Done" button text on my survey.`

### add\_page tool

The **add\_page** tool adds a page to a survey. Your LLM uses this tool to organize questions across pages or create a page to hold new questions, placing it at a position you specify or appending it at the end after confirming the page title and location. Use the **add\_question** tool to add questions to the page.

**Try asking**:

- `Add a new page for demographic questions.`
- `Create a second page titled "Feedback".`
- `Add a page at the start of my survey.`

### update\_page tool

The **update\_page** tool updates a page's title, description, or position. Your LLM uses this tool to rename a page, revise its description, or reorder it within the survey after confirming exactly what changes. It doesn't add or remove questions.

**Try asking**:

- `Rename page 2 to "Contact Details".`
- `Move the demographics page to the end.`
- `Update the description on my intro page.`

### add\_question tool

The **add\_question** tool adds a question to a page on a survey. Your LLM uses this tool to add a fully specified question, its family, choices, and text, or to reuse a question from the SurveyMonkey question bank. Questions are placed at a position you choose or appended at the end. The add is rejected if the survey has reached the platform's survey-size limit.

**Try asking**:

- `Add a rating question to page 2.`
- `Add a multiple-choice question with these options.`
- `Add the standard NPS question from the question bank.`

### update\_question tool

The **update\_question** tool updates an existing question's text, choices, or position. Your LLM uses this tool to revise a question's wording, change its answer choices, or reorder it on its page after confirming exactly what changes. It can't move a question to another page or change its question type.

**Try asking**:

- `Change this question's wording to be more specific.`
- `Update the answer choices on my rating question.`
- `Move this question to the top of the page.`

### list\_question\_bank\_questions tool

The **list\_question\_bank\_questions** tool lists SurveyMonkey question-bank questions available to reuse. Your LLM uses this tool to find a reusable bank question and obtain its ID, which it then passes to the **add\_question** tool to place the question on a page. This tool is read-only and can be filtered by search text, locale, or custom questions.

**Try asking**:

- `Find a reusable NPS question in the question bank.`
- `Search the question bank for satisfaction questions.`
- `Show me question-bank questions I can add to this page.`

### list\_survey\_templates tool

The **list\_survey\_templates** tool lists available SurveyMonkey library templates. Your LLM uses this tool to find a SurveyMonkey template to base a new survey on and obtain its template ID for the **create\_survey** tool, optionally filtering by category or language. Only SurveyMonkey's library templates are available. Team and custom templates aren't listed.

**Try asking**:

- `Show me SurveyMonkey templates for event feedback.`
- `Find a customer-satisfaction survey template.`
- `List the available templates in French.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/surveymonkey-distribution-mcp-server.md
description: >-
  Use the SurveyMonkey Distribution MCP server to connect your LLM to
  SurveyMonkey with tools to publish surveys and track responses through natural
  conversation.
---

# SurveyMonkey Distribution MCP server

The SurveyMonkey Distribution MCP server enables LLMs to interact with SurveyMonkey to publish surveys to an audience and track the responses that come back through natural conversation. It provides tools to locate a survey to publish, create web-link, email, and SMS collectors, send email and SMS invitations, manage contact lists, track basic response records and counts, and manage webhook event subscriptions without requiring direct interaction with the SurveyMonkey interface.

> **SERVER SCOPE**
> 
> The SurveyMonkey Distribution MCP server provides survey distribution and basic response tracking capabilities. Use the [SurveyMonkey Authoring](/en/mcp/prebuilt-mcps/surveymonkey-authoring-mcp-server) MCP server to build and edit surveys, pages, and questions.
> 
> [delete\_webhook](#delete-webhook-tool) is the only destructive delete surfaced by this server.

## Uses

Use the SurveyMonkey Distribution MCP server to perform the following actions:

- Locate a survey to publish by name or ID, without leaving to build or edit it.
- Create a web-link collector and share its URL, or an email or SMS collector for invitations.
- List the collectors that already exist on a survey.
- Send an email or SMS invitation, reminder, or thank-you to recipients or a contact list.
- Create and populate reusable contact lists, and review their membership.
- Track responses at a basic level by listing records and counts and filtering by status.
- Read a single response's basic metadata.
- Subscribe to survey, collector, and response events through webhooks.
- List and read webhook subscriptions, and delete one to stop its event delivery.

### Example prompts

Use the following example prompts to invoke SurveyMonkey Distribution MCP server tools:

- `Give me a shareable link for my customer-satisfaction survey.`
- `Find the survey called "Q3 Feedback" so I can publish it.`
- `Create an SMS collector to text my survey to contacts.`
- `Email this survey to last quarter's attendees.`
- `Send a reminder invitation on my email collector.`
- `Create a contact list called "Fall Event Attendees".`
- `Add these email addresses to my contacts list.`
- `How many people have responded so far?`
- `Set up a webhook for when a response is completed.`
- `Delete the webhook feeding our old integration.`

## SurveyMonkey Distribution MCP server tools

The SurveyMonkey Distribution MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [find\_survey](#find-survey-tool) | Finds a survey to publish by name or ID and returns its ID, title, and question count. |
| [create\_collector](#create-collector-tool) | Creates a web-link, email, or SMS collector on a survey. |
| [list\_collectors](#list-collectors-tool) | Lists the collectors that exist on a survey. |
| [send\_invitation](#send-invitation-tool) | Creates and sends an email or SMS invitation for a collector. |
| [create\_contact\_list](#create-contact-list-tool) | Creates a named contact list for outreach. |
| [list\_contact\_lists](#list-contact-lists-tool) | Lists the account's contact lists. |
| [add\_contacts](#add-contacts-tool) | Adds one or more contacts to a contact list. |
| [list\_contacts](#list-contacts-tool) | Lists the contacts in a contact list. |
| [list\_responses](#list-responses-tool) | Lists basic response records and the count for a survey or collector. |
| [get\_response](#get-response-tool) | Retrieves the basic metadata for a single response. |
| [create\_webhook](#create-webhook-tool) | Subscribes to survey, collector, or response events. |
| [list\_webhooks](#list-webhooks-tool) | Lists the ID and name for existing webhook subscriptions. |
| [get\_webhook](#get-webhook-tool) | Retrieves one webhook subscription's full detail. |
| [delete\_webhook](#delete-webhook-tool) | Deletes a single webhook to stop its event delivery. |

## Install the SurveyMonkey Distribution MCP server

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
    

## SurveyMonkey Distribution connection setup

View SurveyMonkey Distribution connection setup steps

Complete the following steps to connect to SurveyMonkey in Workato:

1. Provide a **Connection name** that identifies which SurveyMonkey account Workato is connected to.
   
2. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
3. Use the **Datacenter** drop-down menu to select the data center that hosts your SurveyMonkey account. Defaults to **United States**. You must use a [custom OAuth profile](/en/custom-oauth-profiles) to connect to a data center outside of the United States.
   
4. Optional. Use the **Custom OAuth profile** drop-down menu to select a [custom OAuth profile](/en/custom-oauth-profiles) for your connection. All requests to the app use the profile you specify here.
   
5. Click **Connect** to open the SurveyMonkey authorization window.
   
6. Sign in to SurveyMonkey with your account credentials. We recommend you use an admin account to avoid permission roadblocks.
   
7. Read the terms of service and click **Authorize** to complete the connection setup.
   
   > **VIEW ANSWERS REQUIREMENT**
   > 
   > Select `view answers along with responses` during authorization if you plan to use the `Completed survey response` trigger or the `Send survey invite via email and wait for response` action.
   
   ![Authorization grant](/assets/authorization_grant.mzHGoRrt.png)_Authorize Workato to access your SurveyMonkey account._
   

### SurveyMonkey Distribution role requirements

Each tool's availability depends on the plan and the OAuth scopes granted to the connected SurveyMonkey account. A request made without the required scope returns a permission-denied outcome rather than a partial result. Refer to SurveyMonkey's [OAuth scopes](https://developer.surveymonkey.com/api/v3/#scopes) documentation for the complete list of scopes and their capabilities.

## How to use SurveyMonkey Distribution MCP server tools

Refer to the following sections for detailed information on available tools:

### find\_survey tool

The **find\_survey** tool finds a survey to publish by name or ID and returns its ID, title, and question count. Your LLM uses this tool to resolve the survey you plan to publish or track by a title fragment or a specific survey ID. Pages and questions aren't returned.

This tool is read-only. Use the [SurveyMonkey Authoring](/en/mcp/prebuilt-mcps/surveymonkey-authoring-mcp-server) MCP server to build or edit a survey's content.

**Try asking**:

- `Find the survey called "Q3 Feedback" so I can publish it.`
- `Look up the survey with this ID.`
- `Which of my surveys have "customer" in the title?`

### create\_collector tool

The **create\_collector** tool creates a web-link, email, or SMS collector on a survey. Your LLM uses this tool to publish a survey for collecting responses after confirming the survey and collector type with you. A web-link collector returns a shareable URL, while email and SMS collectors act as containers for invitations sent with the **send\_invitation** tool. The tool warns you that the collector won't gather anything if the survey's question count is available and reported as `0`.

**Try asking**:

- `Create a shareable link for my onboarding survey.`
- `Set up an email collector on my customer-satisfaction survey.`
- `Create an SMS collector to text my survey to contacts.`

### list\_collectors tool

The **list\_collectors** tool lists the collectors that exist on a survey. Your LLM uses this tool to find an existing collector, such as an email collector to send a reminder on or a web-link collector already created, before adding a duplicate. This tool is read-only.

**Try asking**:

- `What collectors already exist on this survey?`
- `Is there already a web link for my survey?`
- `Find the email collector I can send a reminder on.`

### send\_invitation tool

The **send\_invitation** tool creates and sends an email or SMS invitation for a collector. Your LLM uses this tool to send a survey through an email or SMS collector after confirming the collector, message type, message content, and recipients with you. It creates the message, adds the recipients through individual addresses or a contact list, and sends or schedules it in one call, then reports the send status as the API returns it. The tool reports the status rather than asserting delivery as delivery isn't guaranteed for unverified senders.

**Try asking**:

- `Email this survey to last quarter's attendees.`
- `Send an SMS invitation to my contact list.`
- `Schedule a thank-you message to go out tomorrow morning.`

### create\_contact\_list tool

The **create\_contact\_list** tool creates a named contact list for outreach. Your LLM uses this tool to stand up a reusable, empty contact list after confirming the name with you, which you then populate with the **add\_contacts** tool and reference when sending invitations.

**Try asking**:

- `Create a contact list called "Fall Event Attendees".`
- `Set up a new recipient list for my newsletter survey.`
- `Make a contacts list I can reuse for reminders.`

### list\_contact\_lists tool

The **list\_contact\_lists** tool lists the account's contact lists. Your LLM uses this tool to find a list made earlier, such as last quarter's recipients, or to get a contact list ID for the **send\_invitation** tool, rather than creating a duplicate. This tool is read-only.

**Try asking**:

- `Show me my contact lists.`
- `Find the recipient list I used last quarter.`
- `Which contact lists can I send this survey to?`

### add\_contacts tool

The **add\_contacts** tool adds one or more contacts to a contact list. Your LLM uses this tool to populate a list after confirming how many contacts and which list, adding them in bulk when more than one is supplied and reporting which succeeded and which failed. Each contact needs an email or a phone number. This tool doesn't deduplicate, so adding a contact already present may duplicate it.

**Try asking**:

- `Add these email addresses to my "Fall Event Attendees" list.`
- `Add jordan@example.com to my contacts list.`
- `Bulk-add this list of recipients to my newsletter list.`

### list\_contacts tool

The **list\_contacts** tool lists the contacts in a contact list. Your LLM uses this tool to review who is in a list before sending invitations, or to confirm contacts were added. This tool is read-only.

**Try asking**:

- `Who's in my "Fall Event Attendees" list?`
- `Show me the contacts on my newsletter list.`
- `Did my contacts get added to the list?`

### list\_responses tool

The **list\_responses** tool lists basic response records and the count for a survey or collector. Your LLM uses this tool to see how many people responded and the status of responses, reading the count from the result envelope's total and filtering by status when you ask. When both a survey and a collector are given, the collector takes precedence. It returns basic records, such as ID, status, and timestamps. It doesn't return answer text, which requires a paid plan.

**Try asking**:

- `How many people have responded so far?`
- `Show me the completed responses for my survey.`
- `How many responses came in through this collector?`

### get\_response tool

The **get\_response** tool retrieves the basic metadata for a single response. Your LLM uses this tool to read one response's status, collection mode, collector, and timestamps, identified by survey ID and response ID. It doesn't return answer text, which requires a paid plan.

**Try asking**:

- `Show me the details of this response.`
- `When was this response submitted, and is it complete?`
- `What's the status of this response?`

### create\_webhook tool

The **create\_webhook** tool subscribes to survey, collector, or response events. Your LLM uses this tool to set up an event-driven notification, such as when a response is completed, scoped to a survey or collector, after confirming the event type and target with you. Webhook payloads carry only IDs and timestamps, not answer content, so a downstream step calls the **list\_responses** or **get\_response** tool to fetch the record.

**Try asking**:

- `Set up a webhook for when a response is completed.`
- `Notify my integration whenever this survey gets a new response.`
- `Subscribe to updates on this collector.`

### list\_webhooks tool

The **list\_webhooks** tool lists an ID and name summary for existing webhook subscriptions. Your LLM uses this tool to find the ID of a webhook to read or delete, then calls the **get\_webhook** tool for full detail. This tool is read-only.

**Try asking**:

- `List my webhook subscriptions.`
- `What webhooks do I have set up?`
- `Find the webhook feeding our old integration.`

### get\_webhook tool

The **get\_webhook** tool retrieves one webhook subscription's full detail. Your LLM uses this tool to read a webhook's event type, what it watches, and its delivery URL, identified by the webhook ID from the **list\_webhooks** tool, typically to confirm exactly what a subscription does before deleting it. This tool is read-only.

**Try asking**:

- `Show me the full detail of this webhook.`
- `What event does this webhook subscribe to, and where does it deliver?`
- `Confirm what this subscription watches before I remove it.`

### delete\_webhook tool

The **delete\_webhook** tool deletes a single webhook to stop its event delivery. Your LLM uses this tool to remove a webhook subscription after identifying the exact webhook with the **list\_webhooks** and **get\_webhook** tools, presenting its details, and obtaining your explicit confirmation. It deletes only one identified webhook, not a bulk delete, and removes the subscription only, leaving survey and response data intact.

**Try asking**:

- `Delete the webhook feeding our old integration.`
- `Remove this webhook subscription.`
- `Stop event delivery to that retired endpoint.`

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
