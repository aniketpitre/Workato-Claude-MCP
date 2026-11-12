---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-pipeline-sources.md
description: >-
  Configure a data pipeline source application to authenticate, select objects,
  and define a schema for extraction.
---

# Configure data pipeline sources

Select a source application and follow its configuration guide to authenticate, select objects, and define a schema. Sources are grouped by the type of business data they contain.

## CRM & sales

CRM and sales engagement sources contain accounts, contacts, opportunities, and sales activity such as calls, emails, and sequences. Sync this data to report on pipeline and rep activity, and combine it with marketing and finance data in your destination.

- [Salesforce](/en/data-orchestration/data-pipeline-recipe/configure-salesforce)
- [Apollo.io](/en/data-orchestration/data-pipeline-recipe/configure-apollo)
- [Gong](/en/data-orchestration/data-pipeline-recipe/configure-gong)
- [HubSpot](/en/data-orchestration/data-pipeline-recipe/configure-hubspot)
- [Outreach](/en/data-orchestration/data-pipeline-recipe/configure-outreach)
- [Pipedrive](/en/data-orchestration/data-pipeline-recipe/configure-pipedrive)
- [Salesloft](/en/data-orchestration/data-pipeline-recipe/configure-salesloft)
- [ZoomInfo](/en/data-orchestration/data-pipeline-recipe/configure-zoominfo)

## Databases

Database sources replicate tables from your databases and data warehouses. Use them to move table data into your destination for analytics and reporting.

- [Snowflake](/en/data-orchestration/data-pipeline-recipe/configure-snowflake-source)
- [MySQL](/en/data-orchestration/data-pipeline-recipe/configure-mysql-source)
- [Oracle](/en/data-orchestration/data-pipeline-recipe/configure-oracle)
- [SQL Server](/en/data-orchestration/data-pipeline-recipe/configure-sql-server-source)

## ERP & enterprise

ERP and enterprise sources contain general ledger, customer, vendor, and operational records from your core business systems. Sync this data to build financial and operational reporting, or to combine planning data with financial records from your ERP.

- [Microsoft Dynamics 365](/en/data-orchestration/data-pipeline-recipe/configure-dynamics-365)
- [Anaplan](/en/data-orchestration/data-pipeline-recipe/configure-anaplan)
- [Ellucian Banner](/en/data-orchestration/data-pipeline-recipe/configure-ellucian)
- [Microsoft Dynamics Business Central](/en/data-orchestration/data-pipeline-recipe/configure-business-central)
- [Oracle E-Business Suite](/en/data-orchestration/data-pipeline-recipe/configure-oracle-ebs)
- [Oracle Fusion Cloud](/en/data-orchestration/data-pipeline-recipe/configure-oracle-fusion)
- [SAP Table Reader](/en/data-orchestration/data-pipeline-recipe/configure-sap-agent)

## File storage

File storage sources load structured files, such as CSV and Parquet, from cloud storage, shared drives, and SFTP servers. Use them to load file-based exports into your destination alongside your application data.

- [Amazon S3](/en/data-orchestration/data-pipeline-recipe/configure-s3)
- [Azure Blob Storage](/en/data-orchestration/data-pipeline-recipe/configure-blob)
- [Google Cloud Storage](/en/data-orchestration/data-pipeline-recipe/configure-cloud)
- [Google Drive](/en/data-orchestration/data-pipeline-recipe/configure-drive)
- [Microsoft SharePoint](/en/data-orchestration/data-pipeline-recipe/configure-sharepoint)
- [OneDrive](/en/data-orchestration/data-pipeline-recipe/configure-onedrive)
- [SFTP](/en/data-orchestration/data-pipeline-recipe/configure-sftp)

## Finance & accounting

Finance and accounting sources contain invoices, payments, bills, journal entries, expenses, and vendor records. Sync this data to report on receivables, payables, and spend across your accounting systems.

- [QuickBooks Online](/en/data-orchestration/data-pipeline-recipe/configure-quickbooks)
- [Coupa](/en/data-orchestration/data-pipeline-recipe/configure-coupa)
- [NetSuite2](/en/data-orchestration/data-pipeline-recipe/configure-netsuite2)
- [Sage Intacct](/en/data-orchestration/data-pipeline-recipe/configure-sage-intacct)
- [SAP Concur](/en/data-orchestration/data-pipeline-recipe/configure-sap-concur)
- [Xero](/en/data-orchestration/data-pipeline-recipe/configure-xero)
- [Zuora](/en/data-orchestration/data-pipeline-recipe/configure-zuora)

## HR & recruiting

HR and recruiting sources contain employee records, job and compensation history, time off, and candidate pipelines. Sync this data to report on headcount, attrition, and hiring funnel metrics. These sources often contain PII and compensation data. Refer to [Field-level data protection](/en/data-orchestration/data-pipeline-recipe/concepts#data-masking) to hash sensitive fields.

- [Workday](/en/data-orchestration/data-pipeline-recipe/configure-workday)
- [BambooHR](/en/data-orchestration/data-pipeline-recipe/configure-bamboo-hr)
- [Cornerstone OnDemand](/en/data-orchestration/data-pipeline-recipe/configure-cornerstone-ondemand)
- [Greenhouse](/en/data-orchestration/data-pipeline-recipe/configure-greenhouse)
- [HiBob](/en/data-orchestration/data-pipeline-recipe/configure-hibob)
- [Workday RaaS](/en/data-orchestration/data-pipeline-recipe/configure-workday-raas)

## Marketing & advertising

Marketing and advertising sources contain campaigns, ad performance, audiences, email engagement, form responses, and web, search, and product analytics. Sync this data to measure campaign performance across channels, and combine it with CRM data in your destination.

- [Google Analytics](/en/data-orchestration/data-pipeline-recipe/configure-google-analytics)
- [Algolia](/en/data-orchestration/data-pipeline-recipe/configure-algolia)
- [Facebook](/en/data-orchestration/data-pipeline-recipe/configure-facebook)
- [Google Search Console](/en/data-orchestration/data-pipeline-recipe/configure-google-search-console)
- [Klaviyo](/en/data-orchestration/data-pipeline-recipe/configure-klaviyo)
- [LinkedIn](/en/data-orchestration/data-pipeline-recipe/configure-linkedin)
- [Marketo](/en/data-orchestration/data-pipeline-recipe/configure-marketo)
- [Mixpanel](/en/data-orchestration/data-pipeline-recipe/configure-mixpanel)
- [Pendo](/en/data-orchestration/data-pipeline-recipe/configure-pendo)
- [Salesforce Marketing Cloud](/en/data-orchestration/data-pipeline-recipe/configure-salesforce-marketing-cloud)
- [Typeform](/en/data-orchestration/data-pipeline-recipe/configure-typeform)
- [X](/en/data-orchestration/data-pipeline-recipe/configure-x)

## Payments & commerce

Payments and commerce sources contain transactions, orders, customers, subscriptions, refunds, and disputes. Sync this data to report on revenue, subscription changes, and order fulfillment.

- [Stripe](/en/data-orchestration/data-pipeline-recipe/configure-stripe)
- [Braintree](/en/data-orchestration/data-pipeline-recipe/configure-braintree)
- [Chargebee](/en/data-orchestration/data-pipeline-recipe/configure-chargebee)
- [Shopify](/en/data-orchestration/data-pipeline-recipe/configure-shopify)
- [Square](/en/data-orchestration/data-pipeline-recipe/configure-square)

## Productivity & collaboration

Productivity and collaboration sources contain projects, tasks, issues, pull requests, pages, messages, and spreadsheet data. Sync this data to track project delivery and development activity across tools.

- [Slack](/en/data-orchestration/data-pipeline-recipe/configure-slack)
- [Airtable](/en/data-orchestration/data-pipeline-recipe/configure-airtable)
- [Asana](/en/data-orchestration/data-pipeline-recipe/configure-asana)
- [Confluence](/en/data-orchestration/data-pipeline-recipe/configure-confluence)
- [GitHub](/en/data-orchestration/data-pipeline-recipe/configure-github)
- [Google Sheets](/en/data-orchestration/data-pipeline-recipe/configure-google-sheets)
- [Jira](/en/data-orchestration/data-pipeline-recipe/configure-jira)
- [Looker](/en/data-orchestration/data-pipeline-recipe/configure-looker)
- [Monday.com](/en/data-orchestration/data-pipeline-recipe/configure-monday)
- [Trello](/en/data-orchestration/data-pipeline-recipe/configure-trello)

## Support & service

Support and service sources contain tickets, conversations, incidents, on-call schedules, SLAs, and satisfaction ratings. Sync this data to report on response and resolution times, SLA compliance, and support volume, or join it with CRM data to view support activity by account.

- [Zendesk](/en/data-orchestration/data-pipeline-recipe/configure-zendesk)
- [Freshdesk](/en/data-orchestration/data-pipeline-recipe/configure-freshdesk)
- [Intercom](/en/data-orchestration/data-pipeline-recipe/configure-intercom)
- [PagerDuty](/en/data-orchestration/data-pipeline-recipe/configure-pagerduty)
- [ServiceNow](/en/data-orchestration/data-pipeline-recipe/configure-servicenow)
- [SurveyMonkey](/en/data-orchestration/data-pipeline-recipe/configure-surveymonkey)
