---
url: 'https://docs.workato.com/en/process-automation.md'
description: >-
  Workato process automation lets organizations design, run, and manage no-code
  workflows that connect apps and data across cloud and on-premises systems.
---

# Process automation

Process automation in Workato allows organizations to streamline and automate complex business workflows across various applications and data systems. Workato's no-code/low-code approach enables teams to design, implement, and manage automated processes that can handle tasks ranging from simple data transfers to complex, multi-step workflows involving data transformation, decision-making logic, and integration with both cloud-based and on-premises systems.

This guide provides an overview of the following aspects of process automation:

- [Enterprise-wide connectivity](#enterprise-wide-connectivity)
- [Event-driven automation](#event-driven-automation)
- [Workflow orchestration](#workflow-orchestration)
- [Data transformation and processing](#data-transformation-and-processing)
- [Error and exception handling](#error-and-exception-handling)
- [Security and compliance](#security-and-compliance)
- [Scalability and performance](#scalability-and-performance)
- [Monitoring and analytics](#monitoring-and-analytics)
- [User and role management](#user-and-role-management)
- [Custom code support](#custom-code-support)
- [Reusable components](#reusable-components)
- [Version control and deployment](#version-control-and-deployment)

## Enterprise-wide connectivity

Workato can integrate and automate workflows across a wide range of enterprise applications, databases, and systems, both in the cloud and on-premises. This capability is crucial for businesses that rely on a diverse set of tools and data sources to operate efficiently and make data-driven decisions.

### Key aspects of enterprise-wide connectivity in Workato

- Pre-built connectors
  
- Workato offers a vast library of [pre-built connectors](/en/connectors/prebuilt-connectors) that facilitate integration with popular enterprise applications and services. These connectors cover various categories, including CRM, ERP, finance, HR, IT, marketing, sales, and support. This extensive library enables businesses to quickly and easily connect their applications without the need for custom coding.
  
- Custom connector SDK
  
- For applications or systems not covered by the existing pre-built connectors, Workato provides a [Connector SDK (Software Development Kit)](/en/developing-connectors) that allows developers to build custom connectors. This SDK supports the integration of any REST or SOAP API into Workato, enabling connectivity to virtually any application or system with an available API.
  
- On-premise connectivity
  
- Workato addresses the need for secure access to on-prem systems through [on-prem agents (OPA)](/en/on-prem). The OPA acts as a secure bridge between Workato's cloud platform and an organization's internal network, allowing for the integration and automation of workflows that involve on-prem databases, applications, and file systems without exposing them directly to the internet.
  
- API Management
  
- Beyond application integration, Workato offers [API management](/en/api-management) capabilities, allowing enterprises to create, manage, and deploy APIs. This facilitates not only internal integrations and automations, but also enables businesses to securely expose their services and data to external partners and developers.
  

## Event-driven automation

Event-driven automation is a powerful approach that allows workflows, or "recipes," to be triggered by specific events occurring within or across applications, systems, or services. This model is pivotal for creating responsive, efficient, and real-time integrations and automations across a variety of business processes.

### Key features of event-driven automation in Workato

- Triggers
  
- At the heart of event-driven automation in Workato are [triggers](/en/recipes/triggers#triggers). A trigger is an event in an application or system that starts a Workato recipe. These can be diverse, such as the creation of a new record in a database, a new file in a storage system, a message posted in a chat application, or a custom event from a web application through webhooks. Workato supports a wide array of triggers, enabling recipes to start based on real-time data changes or specific conditions.
  
- Real-time and polling triggers
  
- Workato offers both real-time and polling triggers. [Real-time triggers](/en/recipes/triggers#real-time-triggers) respond immediately to events as they happen, whereas [polling triggers](/en/recipes/triggers#polling-triggers) check for new data at specified intervals. This flexibility allows you to choose the most efficient way to initiate automations based on the criticality of tasks and the capabilities of the source systems.
  
- Webhooks
  
- For applications and systems that support [webhooks](/en/connectors/workato-webhooks), Workato can directly receive real-time data. This is an efficient way to implement event-driven automation, as it allows Workato recipes to be triggered instantly by external events without the need for polling.
  
- Customizable logic and actions
  
- Once an event triggers a recipe, Workato allows for complex logic to be applied to the incoming data, enabling [conditional actions](/en/recipes/steps#if-condition-step), [data transformation](/en/data-orchestration/data-transformation-capabilities), and integration with multiple systems within a single workflow. This means that based on the event, Workato can route data and perform a wide range of actions across connected applications.
  

## Workflow orchestration

Workflow orchestration is the coordinated execution of multiple recipes across various applications and services to accomplish complex business tasks. It's a strategic approach to streamline and automate workflows across an organization's entire ecosystem, ensuring that different systems work together seamlessly and efficiently.

### Key aspects of workflow orchestration in Workato

- Unified platform
  
- Workato offers a single, integrated platform with a wide range of capabilities, including Workflow apps, API management, Data orchestration, Event streams, Workbot, universal connectivity, and more. This unified approach simplifies the design, execution, and management of orchestrated workflows across different business functions such as sales, marketing, HR, finance, and IT operations.
  
- Intuitive design environment
  
- Workato's user-friendly interface allows users to visually design and map out their workflows, making complex orchestration tasks more accessible to both technical and non-technical users. The drag-and-drop interface, combined with a vast library of pre-built connectors and actions, enables rapid development of workflows.
  
- Support for complex workflows
  
- Workato supports complex workflows with conditional logic, loops, and parallel execution paths. This capability allows you to orchestrate workflows that dynamically respond to different scenarios, routing data, and executing different actions based on conditions you specify.
  

## Data transformation and processing

Data transformation and processing are core capabilities that enable seamless integration and automation across a multitude of applications and data sources. Workato is equipped with a wide array of built-in functions and features designed to support data validation, cleansing, enrichment, transformation, and merging. Additionally, its robust support for handling both structured and unstructured data formats makes it a versatile tool for businesses looking to automate their workflows efficiently.

### Built-in functions for data manipulation

- Data validation and cleansing
  
- Workato's ability to [validate and cleanse data](/en/features/sql-transformations-data-validation-cleansing) ensures accuracy and integrity across systems. It checks data formats, required fields, and predefined criteria while correcting inaccuracies and removing irrelevant data. This includes normalizing formats, trimming whitespace, and converting data types, improving data quality and workflow efficiency.
  
- Data enrichment
  
- [Enrichment functions](/en/features/sql-transformations-data-enrichment) in Workato enable users to augment data by adding additional information from external sources or [lookup tables](/en/features/lookup-tables). This is crucial for scenarios where more context or details are needed, such as adding product details based on product IDs or fetching customer information from a CRM system.
  
- Data transformation
  
- Workato offers a comprehensive set of [data transformation](/en/data-orchestration/data-transformation-capabilities) features. These include string manipulation, mathematical computations, data formatting, and conditional logic operations, allowing users to modify and transform data to meet the requirements of target systems or processes.
  
- Data merging
  
- The platform supports [merging data](/en/features/sql-transformations-cdc) from multiple sources, enabling users to consolidate information into a single record or dataset. This feature is particularly useful for creating unified views of data from disparate systems or for aggregating data before analysis.
  

### Support for structured and unstructured data formats

- Structured data
  
- Workato excels in handling structured data, such as [JSON](/en/features/handling-json), [XML](/en/features/handling-xml), and [CSV](/en/features/handling-csv-files) files, as well as data from relational databases and cloud applications. The platform provides native connectors and parsing capabilities that allow for easy manipulation and integration of structured data.
  
- Unstructured data
  
- For unstructured data, such as text files, emails, or social media posts, Workato offers tools to extract and process relevant information. This includes text parsing functions and the ability to [integrate with AI](/en/connectors/ai-by-workato#enable-ai-by-workato-in-your-workspace) for advanced data extraction and analysis.
  

## Error and exception handling

Workato helps you build reliable automations by detecting and managing errors during recipe execution. Errors may include invalid input, failed connections, API quotas, or system issues. Workato provides tools to detect these failures, define responses, and keep your processes stable.

These tools enable you to:

- Catch and manage errors in recipes using structured steps
- Retry actions or route to alternate logic
- Notify teams about issues
- Monitor job and system-wide failures
- Analyze patterns and debug execution history

Refer to the [Error handling and monitoring](/en/recipes/best-practices-error-handling) section for available tools and implementation steps.

## Security and compliance

Security and compliance are foundational elements of Workato's platform, ensuring that data and integrations are secure and adhere to regulatory standards, including GDPR and HIPAA. Workato's approach to security is comprehensive, covering data protection, access control, and compliance with industry regulations.

### How Workato addresses security and compliance

- Access and authentication
  
- Workato enhances user authentication integrity by storing only secure password hashes, and the platform supports customizable automatic logout to bolster security. The platform also employs [two-factor authentication (2FA)](/en/security/two-factor-authentication) for an extra security layer and uses distinct Workspaces to segregate resources for operational safety. It follows a secure multi-phase development lifecycle across separate environments for development, testing, and production, complemented by IP Allowlists to restrict service access, ensuring comprehensive protection against unauthorized access.
  
- Protocols and standards
  
- Workato adheres to the latest TLS and HTTPS standards for secure data transmission. The platform also supports [Single Sign-On (SSO)](/en/user-accounts-and-teams/single-sign-on) through SAML-compliant systems and third-party credentials like Google and Microsoft Office 365.
  
- User provisioning and authorization
  
- Workato allows [automatic creation of user accounts](/en/user-accounts-and-teams/just-in-time-provisioning) using SAML-based SSO, aligning with security policies. [Role-based access control (RBAC)](/en/user-accounts-and-teams/role-based-access/) implements the principle of least privilege, minimizing data exposure risk. Offers the ability to configure [custom roles](/en/user-accounts-and-teams/role-based-access/#creating-custom-roles) for precise access control to folders, recipes, and connections.
  
- Connecting to external systems
  
- Workato preferentially uses OAuth2 for connecting to external systems, reducing the need to store credentials. Workato also supports the creation of [custom OAuth profiles](/en/custom-oauth-profiles#custom-oauth-profiles) for greater control over app branding and permissions.
  
- Data protection and privacy
  
- All data in Workato is encrypted at rest using AES-256, with job history data double-encrypted. [Transaction-related data](/en/security#data-protection) is retained for a limited time, with the period varying by plan. Workato enables you to [mask sensitive data](/en/features/data-masking) in recipe configurations, preventing its display in the UI or job history.
  
- Audit and compliance
  
- Workato maintains the following compliance frameworks: PCI-DSS v4.0.1 − Level 1, ISO 27001, ISO 27701, ISO 42001, SOC 1 Type II, SOC 2 Type II, SOC 3, HIPAA, IRAP, and NIST 800-171A r2.
  
  In addition, Workato provides an [activity audit log](/en/features/activity-audit-log#activity-audit-log) to track user actions, supporting external analysis and data retention.
  

## Scalability and performance

Scalability and performance are key aspects of Workato's platform design, ensuring that it can handle the growing and evolving needs of businesses as they scale up their automation and integration workflows.

### Scalability

- Cloud-native architecture
  
- Workato's cloud-native architecture is built to automatically scale resources up or down based on demand. This means that as the volume of transactions or complexity of workflows increases, Workato dynamically allocates more resources to maintain high performance levels.
  
- Concurrent processing
  
- The platform is capable of running multiple processes concurrently. This allows for a significant number of tasks, recipes, and data transformations to be executed simultaneously without degradation in performance.
  
- Efficient workload management
  
- Workato provides tools and features for optimizing the execution of workflows, including the ability to prioritize tasks and manage the distribution of workloads across available resources effectively.
  

### Performance

- Real-time processing
  
- Workato supports real-time data processing, ensuring that workflows can operate with minimal latency. This is critical for time-sensitive operations, such as order processing, real-time analytics, and instant data synchronization across systems.
  
- Optimized integrations
  
- The platform utilizes optimized connectors and efficient data handling techniques to speed up the transfer and transformation of data between systems. This minimizes bottlenecks and reduces the time to complete integrations.
  
- Monitoring and optimization tools
  
- Workato offers monitoring tools, including [dashboards](/en/features/admin-dashboard) that provide visibility into the performance of integrations and workflows. Users can identify and troubleshoot any issues that may impact performance, and leverage insights to further optimize their processes.
  

## Monitoring and analytics

Monitoring and analytics provide users with insights into their operations and the health of their integrations. Workato offers a comprehensive set of tools and features designed to give users visibility into their automated processes, enabling them to track performance, troubleshoot issues, and make informed decisions based on real-time data.

### Key aspects of monitoring and analytics in Workato

- Real-time monitoring
  
- Workato's real-time monitoring capabilities provide immediate visibility into the operational status of recipes and [recipe jobs](/en/features/admin-dashboard#recipe-details-table). Users can track job success rates, identify errors quickly with detailed messages, and view performance metrics like execution times. This immediate insight is crucial for maintaining the smooth operation of automated processes and ensuring they run efficiently.
  
- Analytics
  
- Through analytics features, users gain access to in-depth analysis and reporting on the [usage](/en/features/admin-dashboard#plan-usage) and performance of their recipes over time. This includes usage reports to track task volumes, insights into recipe performance for identifying potential bottlenecks, and the ability to [create custom dashboards](/en/insights) for monitoring key metrics. These tools help users optimize their workflows and make data-driven decisions about their automation strategies.
  
- Job reports
  
- [Job reports](/en/recipes/jobs) in Workato offer a comprehensive record of every action performed within a recipe, including detailed data on each execution step and its outcome. These logs are invaluable for troubleshooting errors, debugging recipe flows, and complying with audit and regulatory requirements by providing a transparent, chronological record of all automation activities.
  
- Notifications and alerts
  
- Workato enables users to set up custom [notifications and alerts](/en/recipes/error-notifications), allowing for immediate communication when specific events occur, such as recipe failures or performance thresholds being exceeded.
  

## User and role management

User and role management in Workato revolves around controlling access to different parts of the platform based on specific users' roles and responsibilities. This gives you the flexibility to define roles and permissions for different types of users and supports collaboration among business users, IT staff, and developers.

### Key aspects of user and role management in Workato

- Users
  
- Workato allows you to invite team members to collaborate on workflows and integrations. Each user has a unique login and can be assigned specific roles and permissions.
  
- Environment roles
  
- Workato provides predefined [environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) under the [new permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2). These roles control access to projects, tools, and administrative settings within an environment. For example, an **Environment admin** has full control over environment settings, while a **Member** has view-only access. If your workspace still uses the [legacy permissions model](/en/roles), collaborator roles such as **Admin**, **Operator**, and **Analyst** remain visible until you migrate.
  
- Project roles
  
- Workato also provides predefined [project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles), which control access and actions within specific projects. For example, a **Project admin** has full permissions to manage content and settings, while a **Builder** can create and edit recipes but can't deploy them.
  
- Permissions
  
- Workato's [privileges system](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference) defines the specific actions users can perform based on their assigned role.
  
- Custom roles
  
- Workato supports [custom roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#custom-roles) at both the [environment](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#environment-privileges) and [project](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-privileges) levels. Custom roles allow you to define granular privileges tailored to your organization's needs.
  
- Role-based access control (RBAC)
  
- Workato's [RBAC](/en/user-accounts-and-teams/role-based-access/#managing-your-workspace-collaborators-with-role-based-access-control) system enables administrators to regulate access to features, functions, and folders based on a user's role in a workspace. This ensures that sensitive data and workflows remain accessible only to authorized users. RBAC encompasses controlling access to connections, API endpoints, integration configurations, and other critical aspects.
  
- Audit trails
  
- Workato logs user activities in the [activity audit log](/en/features/activity-audit-log#activity-audit-log), providing an audit trail that administrators can review to track changes, monitor usage, and ensure compliance with security policies.
  
- Integration with identity providers
  
- Workato [integrates with identity providers](/en/user-accounts-and-teams/single-sign-on), including Okta, Microsoft Entra ID, and Google Workspace for streamlined user authentication and management.
  

## Custom code support

Workato provides robust support for custom code, allowing users to extend the capabilities of their automation workflows beyond the platform's standard actions and triggers. This feature is particularly useful for complex data transformations, implementing custom logic, or integrating with systems that require specific handling not covered by Workato's pre-built connectors.

- Custom code transformations
  
- Workato continues to offer support for custom code transformations with pre-built connectors for Ruby, [Python](/en/connectors/python), and [JavaScript](/en/connectors/javascript). This allows users to perform data transformations using these languages.
  
- Serverless functions
  
- Users can utilize serverless functions including Azure Functions, or write [on-prem scripts](/en/connectors/on-prem-command-line-scripts) to be invoked using Workato's On-prem command-line script connector for custom automation needs.
  

## Reusable components

Reusable components are a foundational component of our design philosophy, enabling users to build automation workflows more efficiently and effectively. These components help streamline the development process, ensure consistency across automations, and facilitate easy updates.

### Key types of reusable components in Workato

- Connectors
  
- Workato offers over 1,200 [pre-built connectors](/en/connectors/prebuilt-connectors), a [community library](/en/developing-connectors/community/community#community-connectors) of pre-built recipes (workflows) and custom connectors, and the ability to create custom connectors using our [Connector SDK](/en/developing-connectors). You can reuse these connectors, actions, and workflows across different processes.
  
- Recipe functions
  
- [Recipe functions](/en/connectors/recipe-functions) are a powerful feature in Workato that allows users to invoke one recipe from another. This is especially useful for common tasks or functionalities that need to be executed in multiple workflows and aid in parallel processing. For example, you might have a standard process for validating customer data that is used across several different automations. By creating a callable recipe for this process, you can maintain the logic in a single place and call it from anywhere, ensuring consistency and reducing the need to duplicate efforts.
  
- Lookup tables
  
- [Lookup tables](/en/features/lookup-tables#lookup-tables) are used in Workato to store and manage static or semi-static data that can be referenced across multiple recipes. This feature is useful for maintaining consistent data across various parts of an organization's automation infrastructure, such as mapping codes to values or storing fixed configuration settings. Lookup tables help reduce hardcoding and duplication, making recipes easier to maintain and update.
  

### Share and manage reusable components

Workato offers tools and features that enable you to share and manage reusable components across your organization, including Environments, Recipe lifecycle management, and the ability to [share recipes and connectors publicly in the community library](/en/recipes/settings#community-library-publish) or [privately through URL](/en/recipes/settings#share-privately).

## Version control and deployment

Version control and deployment are integral features that enhance the platform's capability to manage, track, and deploy automation recipes efficiently and safely. These features are designed to support best practices in software development and deployment, making it easier for teams to collaborate, maintain consistency, and reduce errors in their automated processes.

### Key aspects of version control in Workato

- Recipe versions
  
- Workato allows users to create versions of their recipes. This is crucial for tracking changes over time, understanding the evolution of a recipe, and reverting to previous versions if needed.
  
- Change tracking
  
- Changes made to recipes are tracked, and detailed [activity audit logs](/en/features/activity-audit-log#activity-audit-log) are maintained. This helps users see what changes were made, by whom, and when, facilitating better collaboration and oversight.
  
- Cloning
  
- While Workato does not support branching in the same way as traditional version control systems like Git, it enables users to clone recipes. This feature can be used to manage different versions or variations of a recipe, simulating a branching mechanism for testing new features or changes without affecting the main workflow.
  
- Version control for custom connectors
  
- Custom connectors in Workato can be [version-controlled](/en/developing-connectors/sdk/quickstart/version-control#version-control), similar to how software development projects manage code changes. This is essential for maintaining consistency, tracking modifications, and ensuring that any updates to connectors do not disrupt existing integrations. Version control allows for safer iterations and updates to connectors, with the ability to roll back to previous versions if needed.
  

### Key aspects of deployment in Workato

- Environments
  
- Workato supports the use of different [Environments](/en/features/environments#environment-basics), including development, testing, and production. This allows users to test recipes thoroughly in a controlled environment before deploying them to production, minimizing the risk of errors affecting live operations.
  
- Recipe lifecycle management (RLCM)
  
- [RLCM](/en/recipe-development-lifecycle#recipe-lifecycle-management) facilitates the structured movement of recipes and their dependencies (assets) across different environments. It supports the export and import of packages containing recipes, connections, and other components necessary for the recipe to function, ensuring smooth transitions between development, testing, and production.
  
- Automated deployment
  
- Workato supports the ability to automate the deployment process with our [Recipe lifecycle management APIs](/en/workato-api/recipe-lifecycle-management#quick-reference) and features that streamline the deployment process. This includes the ability to quickly move or replicate recipes across environments or workspaces.

---
