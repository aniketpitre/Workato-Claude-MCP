# Recipe design

195 pages. Paths are relative to the repository root.


## Recipe design

- **Data tables** - `kb/docs/en/data-tables.md` - Workato data tables store data referenced by recipes in a scalable, secure, spreadsheet-like interface, and power data storage for workflow apps.
- **Projects** - `kb/docs/en/projects.md` - Learn how to create and manage projects in Workato. Use projects to organize your integration assets by department, use case, or application.
- **Recipes** - `kb/docs/en/recipes.md` - Learn more about recipes in Workato.
- **Error handling best practices** - `kb/docs/en/recipes/best-practices-error-handling.md` - Learn how to handle errors and monitor Workato recipes using monitor blocks, conditional actions, stop actions, and custom alerts.
- **Recipe Design** - `kb/docs/en/recipes/building-recipes.md` - Learn how to design Workato recipes by planning the goal, data flow, apps, triggers, actions, logic, and error handling.
- **Recipe editor** - `kb/docs/en/recipes/editor.md` - An overview of the Workato recipe editor, including the recipe canvas, the toolbar, the step configuration panel, and how to refresh a recipe's schema.
- **Recipe quotas** - `kb/docs/en/recipes/limits.md` - Reference for Workato recipe design-time, run-time, and code size quotas, including how code size quotas vary across data centers.
- **Naming conventions** - `kb/docs/en/recipes/naming-conventions.md` - Apply consistent naming conventions for Workato projects and integration assets so teams understand each project's purpose and structure.
- **Recipe settings** - `kb/docs/en/recipes/settings.md` - Configure recipe settings in Workato, including concurrency, data retention, and sharing options from the Settings tab.
- **Tools** - `kb/docs/en/tools.md` - Explore Workato tools and platform capabilities for building recipes, integrating apps, managing workflows, data orchestration, event streams, and more.

## After you create your recipe

- **Cancel job** - `kb/docs/en/recipes/cancel-job.md` - Cancel a running Workato job from the job details page to stop a recipe that has a bug or appears stuck in processing.
- **Recipes - Jobs** - `kb/docs/en/recipes/jobs.md` - Learn how Workato jobs work, including job metadata, statuses, step details, durations, and tasks used to monitor and troubleshoot recipe runs.
- **Optimizing task usage** - `kb/docs/en/recipes/optimizing-task-usage.md` - Learn strategies to reduce Workato task usage, including poll frequency, scheduled jobs, and batch or bulk triggers and actions.
- **View a recipe** - `kb/docs/en/recipes/read-only-mode.md` - Learn how to view a recipe's steps, jobs, and version history in Workato without the risk of accidentally editing it.
- **Rerunning jobs** - `kb/docs/en/recipes/rerun-job.md` - Learn how to rerun jobs in Workato, including scenarios, limitations, and best practices.
- **Testing, starting, and stopping recipes** - `kb/docs/en/recipes/start-and-stop.md` - Learn how to test, start, and stop recipes in Workato, including how recipes resume processing and when Workato stops them.
- **Testing recipes** - `kb/docs/en/recipes/testing.md` - Test recipes in the Workato testing environment before starting them to confirm steps run correctly and data is processed accurately.
- **Viewing Jobs FAQs** - `kb/docs/en/recipes/viewing-jobs-faqs.md` - Answers to common questions about viewing Workato recipe jobs, including job reports, metadata, statuses, and data retention.
- **Test automation - overview** - `kb/docs/en/test-automation.md` - Workato Test Automation lets you test recipe functionality with mock data, create test cases, run tests, and integrate testing into your CI/CD pipeline.
- **Test automation - FAQ** - `kb/docs/en/test-automation/faq.md` - Answers to common questions about Workato test automation, including versioning, loops, RLCM packages, and cloning behavior.
- **Test automation quotas** - `kb/docs/en/test-automation/limits.md` - Reference for Workato test automation quotas, including the constraints that apply to test cases and recipe testing.
- **Test automation - Test case - Create** - `kb/docs/en/test-automation/test-case-create.md` - Create a recipe-level test case in Workato test automation and give it a unique, descriptive name to start testing your recipe.
- **Test automation - Test case - View results** - `kb/docs/en/test-automation/test-case-results.md` - View test case run results in Workato, including pass or fail status, the check that failed, and links to the test case run jobs.
- **Test automation - Test case - Run** - `kb/docs/en/test-automation/test-case-run.md` - Run a Workato test case to verify recipe functionality, with details on run priority, how mocked steps execute, and how data checks work.
- **Test automation - Test case - Set up** - `kb/docs/en/test-automation/test-case-set-up.md` - Set up a Workato test case by mocking the recipe trigger and steps, adding data checks, and validating the test before you run it.
- **Test automation - Test case - View** - `kb/docs/en/test-automation/test-case-view.md` - View a Workato test case and understand its mock and check badges, step input config, and other details for each recipe step.
- **Test automation - Test cases overview** - `kb/docs/en/test-automation/test-case.md` - Learn how Workato test cases use mock data and checks on specific recipe steps to verify that a recipe behaves as expected.

## Data tables

- **Data tables - Create record action** - `kb/docs/en/data-tables/connector/create-record-action.md` - The create record action creates a new record in a data table you specify.
- **Data tables - Create records action (batch)** - `kb/docs/en/data-tables/connector/create-record-batch-action.md` - The create records batch action creates new records in a data table you specify.
- **Data tables - Delete record action** - `kb/docs/en/data-tables/connector/delete-record-action.md` - The delete record action deletes a record you specify from a data table using its ID.
- **Data tables - Delete records action (batch)** - `kb/docs/en/data-tables/connector/delete-record-batch-action.md` - The delete records batch action deletes multiple records in a data table you specify.
- **Data tables - Delete records by condition action (batch)** - `kb/docs/en/data-tables/connector/delete-records-condition-action.md` - The delete records by condition batch action deletes records that match the filter conditions you specify, up to 200 records per run.
- **Data tables - New record trigger** - `kb/docs/en/data-tables/connector/new-record-trigger.md` - The new record trigger monitors a data table you specify in real-time for newly created records.
- **Data tables - New records trigger (batch)** - `kb/docs/en/data-tables/connector/new-records-batch-trigger.md` - The new records trigger checks for new records in a data table you specify in batches.
- **Data tables - New/updated record trigger** - `kb/docs/en/data-tables/connector/new-updated-record-trigger.md` - The new/updated record trigger monitors a data table you specify in real-time for newly created or updated records.
- **Data tables - New/updated records trigger (batch)** - `kb/docs/en/data-tables/connector/new-updated-records-batch-trigger.md` - The new/updated records trigger checks for new or updated records in a data table you specify in batches.
- **Data tables - Remove values from record action** - `kb/docs/en/data-tables/connector/remove-values-from-record-action.md` - The remove values from record action removes column values from a record you specify.
- **Data tables - Search records (batch) action** - `kb/docs/en/data-tables/connector/search-records-action.md` - The search records batch action retrieves a list of entries that match the search criteria you specify from a data table.
- **Data tables - Truncate table action (batch)** - `kb/docs/en/data-tables/connector/truncate-table-action.md` - The truncate table batch action permanently deletes all of a data table's records.
- **Data tables - Update record action** - `kb/docs/en/data-tables/connector/update-record-action.md` - The update record action updates a record you specify in a data table.
- **Data tables - Update records action (batch)** - `kb/docs/en/data-tables/connector/update-record-batch-action.md` - The update records batch action updates multiple records in a data table you specify.
- **Data tables - Upsert records action** - `kb/docs/en/data-tables/connector/upsert-record-action.md` - The upsert record action updates a record in a data table if it matches a primary key you specify.
- **Data tables - Upsert records action (batch)** - `kb/docs/en/data-tables/connector/upsert-record-batch-action.md` - The upsert records batch action updates or creates multiple records in a data table in a single batch operation.
- **Workato connectors - Data tables** - `kb/docs/en/data-tables/data-table-connector.md` - Learn how the Workato Data table connector provides triggers and actions to use your data tables in recipes, with selectable JSON output formats.
- **Data table interface** - `kb/docs/en/data-tables/data-table-interface.md` - Manage Workato data tables at the project level, where you can create, edit, rename, delete, and download tables and columns from the UI.
- **Data tables - Quotas** - `kb/docs/en/data-tables/data-table-limits.md` - Reference for Workato data table quotas, covering general table size, column, and connector trigger and action quotas.
- **Data tables - Permissions** - `kb/docs/en/data-tables/data-table-permissions.md` - Set up data table permissions in Workato with RBAC and custom roles to control who can create, view, edit, and delete tables.
- **Data tables - Data tables - activity audit** - `kb/docs/en/data-tables/user-interface/activity-audit.md` - Track changes to Workato data tables using the activity audit log, and filter activity for a specific table in shared workspaces.
- **Data tables - Create a column** - `kb/docs/en/data-tables/user-interface/column-create.md` - Create a new column in a Workato data table and set its name, column type, default value, and hint from the data tables interface.
- **Data tables - Delete a column** - `kb/docs/en/data-tables/user-interface/column-delete.md` - Delete a column from a Workato data table using the ellipsis menu. Column deletion is permanent and cannot be undone.
- **Data tables - Edit a column** - `kb/docs/en/data-tables/user-interface/column-edit.md` - Edit a Workato data table column to change its name, default value, and hint. Column type and required setting cannot be changed.
- **Data tables - Data tables - Supported column types** - `kb/docs/en/data-tables/user-interface/column-types.md` - Reference for the column data types supported in Workato data tables, with available operands for each type.
- **Data tables - Create a data table** - `kb/docs/en/data-tables/user-interface/create.md` - Create a new Workato data table within a project by building the table structure from scratch or by importing a CSV file.
- **Data tables - Delete data table** - `kb/docs/en/data-tables/user-interface/delete.md` - Delete a data table in the Workato data tables interface and review the warning that lists recipes affected by the change.
- **Data tables - Download a data table as CSV** - `kb/docs/en/data-tables/user-interface/download-csv.md` - Download a Workato data table from the data tables interface as a CSV file to export your table data for use outside Workato.
- **Data tables - Add/edit table data** - `kb/docs/en/data-tables/user-interface/edit.md` - Edit Workato data table data by adding, updating, and deleting rows using your mouse or keyboard shortcuts in the data tables interface.
- **Data tables - Keyboard shortcuts** - `kb/docs/en/data-tables/user-interface/keyboard-shortcuts.md` - Reference for Workato data table keyboard shortcuts on Mac and Windows for selecting, editing, and managing table data.
- **Data tables - Rename a data table** - `kb/docs/en/data-tables/user-interface/rename.md` - Rename a data table in the Workato data tables interface by editing the table name and saving your changes.
- **Data tables - View and sort table data** - `kb/docs/en/data-tables/user-interface/view.md` - View, filter, sort, and hide columns in Workato data tables to organize records in the data table interface.

## Error handling

- **Errors notifications emails** - `kb/docs/en/recipes/error-notifications.md` - Learn how Workato error notification emails work, including when alerts are sent, what triggers them, and how to manage recipients and alert scope.
- **Error type IDs** - `kb/docs/en/recipes/error-type-id.md` - Reference for Workato error type IDs and job error metadata fields used to detect, group, and target failures in Monitor actions for error blocks.
- **Monitor errors across recipes with RecipeOps** - `kb/docs/en/recipes/monitor-errors-recipeops.md` - Set up RecipeOps triggers to monitor failed jobs and recipes stopped by Workato across your workspace, then send alerts or restart workflows.

## Expand automation possibilities

- **CSV tools by Workato** - `kb/docs/en/connectors/csv-by-workato.md` - CSV tools by Workato is a utility connector that parses, transforms, and generates CSV files directly in recipes without external services.
- **CSV tools by Workato – Compose CSV action** - `kb/docs/en/connectors/csv-by-workato/compose-csv-action.md` - This action converts a list of objects into a CSV-formatted string for export or storage.
- **CSV tools by Workato – Parse CSV action** - `kb/docs/en/connectors/csv-by-workato/parse-csv-action.md` - This action parses a CSV-formatted string into an array of lines for use in recipes.
- **JSON tools by Workato** - `kb/docs/en/connectors/json-by-workato.md` - The JSON tools by Workato connector enables you to parse JSON documents and extract values into usable datapills from structured data sources.
- **JSON tools by Workato – Parse JSON action** - `kb/docs/en/connectors/json-by-workato/parse-json-action.md` - This action parses raw JSON into structured datapills based on a sample document.
- **PDF tools by Workato** - `kb/docs/en/connectors/pdf-tools-by-workato.md` - The PDF tools by Workato connector lets you convert, stamp, split, merge, and extract text from PDF documents directly within recipes.
- **PDF tools by Workato – Convert to PDF action** - `kb/docs/en/connectors/pdf-tools-by-workato/actions/convert-to-pdf.md` - The Convert to PDF action converts a source document to a PDF file.
- **PDF tools by Workato – Extract text from PDF action** - `kb/docs/en/connectors/pdf-tools-by-workato/actions/extract-text-from-pdf.md` - The Extract text from PDF action extracts raw text content from digital PDF documents, returning unstructured text.
- **PDF tools by Workato – Merge PDF action** - `kb/docs/en/connectors/pdf-tools-by-workato/actions/merge-pdf.md` - The Merge PDF action combines multiple PDF documents into a single PDF file.
- **PDF tools by Workato – Split PDF action** - `kb/docs/en/connectors/pdf-tools-by-workato/actions/split-pdf.md` - The Split PDF action splits a PDF document into multiple PDF files.
- **PDF tools by Workato – Stamp PDF action** - `kb/docs/en/connectors/pdf-tools-by-workato/actions/stamp-pdf.md` - The Stamp PDF action adds text or image stamps to PDF pages as overlays while preserving original content.
- **PGP tools by Workato** - `kb/docs/en/connectors/pgp-by-workato.md` - PGP tools by Workato is a utility connector that encrypts, decrypts, signs, and verifies data using the AES256 cipher and SHA256 digest.
- **PGP tools by Workato – Decrypt data action** - `kb/docs/en/connectors/pgp-by-workato/decrypt-data-action.md` - This action decrypts content using a private key and passphrase.
- **PGP tools by Workato – Encrypt data action** - `kb/docs/en/connectors/pgp-by-workato/encrypt-data-action.md` - This action encrypts data using a public key.
- **PGP tools by Workato – Sign a message action** - `kb/docs/en/connectors/pgp-by-workato/sign-message-action.md` - This action signs data using the private key and passphrase from the connection.
- **PGP tools by Workato – Verify a signed message action** - `kb/docs/en/connectors/pgp-by-workato/verify-signed-message.md` - This action verifies signed data using a public key.
- **XML tools by Workato** - `kb/docs/en/connectors/xml-tools-workato.md` - XML tools by Workato is a utility connector that parses, generates, transforms, and validates XML documents directly inside your recipes.
- **YAML tools by Workato** - `kb/docs/en/connectors/yaml-by-workato.md` - YAML tools by Workato is a utility connector that parses raw YAML content from files or documents into structured datapills for your recipes.
- **YAML tools by Workato – Parse YAML document action** - `kb/docs/en/connectors/yaml-by-workato/parse-yaml-action.md` - This action parses raw YAML content into structured datapills based on a sample document.
- **Environment properties** - `kb/docs/en/features/account-properties.md` - Learn how Workato environment properties store account-wide configuration parameters that all recipes can use as values in the data tree.
- **Callable recipes by Workato** - `kb/docs/en/features/callable-recipes.md` - Callable recipes are recipes invoked from another recipe to reuse a repeatable set of steps and keep recipes shorter and easier to maintain.
- **Callable Recipes - Call Recipe Actions** - `kb/docs/en/features/callable-recipes/call-recipe-action.md` - Reference for the Call recipe action in Callable recipes, covering synchronous and asynchronous input and output fields used to invoke a recipe.
- **Migrate to recipe functions and API recipes** - `kb/docs/en/features/callable-recipes/migrating-to-recipe-functions-api-recipes.md` - Migrate callable recipes to Recipe functions and API Platform, with guidance on the new recipe types and how their triggers and actions compare.
- **Callable Recipes - New Call For Recipe Trigger** - `kb/docs/en/features/callable-recipes/new-call-trigger.md` - Reference for the New call for recipe trigger in Callable recipes, which creates a job in real time when called from another recipe or REST endpoint.
- **Callable Recipes - Return Response From Recipe Action** - `kb/docs/en/features/callable-recipes/return-response-action.md` - Reference for the Return response from recipe action in Callable recipes, which replies to a recipe call with a status and any returned data.
- **Callable Recipes - Wait for async calls action** - `kb/docs/en/features/callable-recipes/wait-for-async-action.md` - Reference for the Wait for async calls action in Callable recipes, which holds a recipe until all asynchronous calls finish processing.
- **Callable Recipes - Walkthrough** - `kb/docs/en/features/callable-recipes/walk-through.md` - Walk through building a callable recipe that reuses shared logic, using a Salesforce to QuickBooks Online invoice scenario as the example.
- **SQL Collection by Workato FAQs** - `kb/docs/en/features/collection-faqs.md` - Answers to common questions about SQL Collection by Workato, including data transformation, large datasets, connection setup, and available actions.
- **SQL Collection by Workato** - `kb/docs/en/features/collection.md` - SQL Collection by Workato is a native app that manipulates table data, letting you run SQL queries to sync and transform data across systems.
- **Common data model** - `kb/docs/en/features/common-data-model.md` - Learn how the common data model defines a standard schema in Workato so integrations build on a canonical structure instead of individual apps.
- **File tools by Workato - Compress files action** - `kb/docs/en/features/compress-files.md` - Use the Compress files action in File tools by Workato to combine multiple files from any app into a single zip or gzip archive.
- **EDI tools by Workato** - `kb/docs/en/features/edi/edi-by-workato.md` - EDI tools by Workato let you generate and parse EDI documents in recipes, with support for the EDIFACT, HL7, and X12 standards.
- **Generate EDI action** - `kb/docs/en/features/edi/generate-edi-action.md` - Use the Generate EDI action in EDI tools by Workato to create EDI documents from a transaction type or a sample document.
- **Parse EDI action** - `kb/docs/en/features/edi/parse-edi-action.md` - Use the Parse EDI action in EDI tools by Workato to convert EDIFACT, HL7, or X12 documents into datapills for downstream recipe steps.
- **Data orchestration - ETL/ELT** - `kb/docs/en/features/etl-elt-guide.md` - Learn how to build ETL and ELT recipes in Workato to extract, transform, and load data from sources into a data warehouse or data lake.
- **Workato connectors - File streaming** - `kb/docs/en/features/file-streaming.md` - Learn how Workato file streaming transfers large files in chunks between apps, staying within source and destination memory quotas.
- **File tools by Workato** - `kb/docs/en/features/file-tools-by-workato.md` - Use the File tools by Workato connector to facilitate the handling and movement of files within your recipes.
- **Workato FileStorage connector - Append to file action** - `kb/docs/en/features/filestorage/append-to-file-action.md` - Reference for the Workato FileStorage Append to file action, including CSV schema, header, delimiter, and encoding input and output fields.
- **FileStorage connector - Create directory action** - `kb/docs/en/features/filestorage/create-directory-action.md` - Reference for the Workato FileStorage Create directory action, including directory name and path input fields and output fields.
- **FileStorage connector - Create file action** - `kb/docs/en/features/filestorage/create-file-action.md` - Reference for the Workato FileStorage Create file action, including file contents, CSV schema, and overwrite input and output fields.
- **FileStorage connector - Delete directory action** - `kb/docs/en/features/filestorage/delete-directory-action.md` - Reference for the Workato FileStorage Delete directory action, including the directory path input field and output fields.
- **FileStorage connector - Delete file action** - `kb/docs/en/features/filestorage/delete-file-action.md` - Reference for the Workato FileStorage Delete file action, including the file path input field and the deleted file path output field.
- **FileStorage connector** - `kb/docs/en/features/filestorage/filestorage-connector.md` - Store, manage, and process files within Workato recipes using the FileStorage connector, with triggers and actions for files and directories.
- **FileStorage UI** - `kb/docs/en/features/filestorage/filestorage-console.md` - Use the Workato FileStorage UI to upload, download, rename, move, delete, search, and manage files and directories with virus scanning.
- **FileStorage connector - Generate shareable file link action** - `kb/docs/en/features/filestorage/generate-shareable-link-action.md` - Reference for the Workato FileStorage Generate shareable file link action, including scope, file path, and expiry input and output fields.
- **FileStorage connector - Get file contents action** - `kb/docs/en/features/filestorage/get-file-contents-action.md` - Reference for the Workato FileStorage Get file contents action, including the file path input field and contents, size, and timestamp outputs.
- **FileStorage connector - Get lines from CSV file action** - `kb/docs/en/features/filestorage/get-lines-csv-action.md` - Use the Get lines from CSV file batch action to retrieve up to 50,000 CSV lines from a file in Workato FileStorage.
- **FileStorage connector - New CSV file trigger** - `kb/docs/en/features/filestorage/new-csv-file-trigger.md` - Trigger Workato recipes in real time when a new CSV file matching a column schema is created in Workato FileStorage, returning rows in batches.
- **FileStorage connector - New lines in CSV file trigger** - `kb/docs/en/features/filestorage/new-csv-lines-in-file-trigger.md` - Trigger Workato recipes in real time when new lines are added to a CSV file in Workato FileStorage, returning the rows in batches.
- **FileStorage connector - New file trigger** - `kb/docs/en/features/filestorage/new-file-trigger.md` - Trigger Workato recipes in real time when a new file is created or uploaded to a monitored directory in Workato FileStorage.
- **FileStorage connector - Rename/move file action** - `kb/docs/en/features/filestorage/rename-move-file-action.md` - Use the Rename/move file action to rename a file or move it to a new destination directory in Workato FileStorage.
- **FileStorage connector - Search files action** - `kb/docs/en/features/filestorage/search-files-action.md` - Use the Search files action to find files matching a name condition across directories and subdirectories in Workato FileStorage.
- **XML tools by Workato - Generate XML document from a sample XML action** - `kb/docs/en/features/generate-xml-from-xml.md` - The Generate XML document from a sample XML action infers the structure of an XML document from a sample payload and generates an XML document that matches that structure.
- **XML tools by Workato - Generate XML document from XSD action** - `kb/docs/en/features/generate-xml-from-xsd.md` - The Generate XML document from XSD action interprets an XSD file and generates a sample XML document that aligns with its structure and data types.
- **File tools by Workato - Get file from URL action** - `kb/docs/en/features/get-file-from-url.md` - Use the Get file from URL action to retrieve text or binary file contents from a public URL in Workato recipes, with file streaming support.
- **Handling binary files** - `kb/docs/en/features/handling-binary-files.md` - Learn how to move binary files across apps in Workato recipes using a public URL or by downloading and uploading file content.
- **Handle CSVs** - `kb/docs/en/features/handling-csv-files.md` - Learn how to process CSV files in Workato recipes using CSV tools by Workato or connector-specific triggers and actions to parse tabular data.
- **Handling JSON FAQs** - `kb/docs/en/features/handling-json-faqs.md` - Answers to common questions about handling JSON data in Workato recipes, including what JSON is and how Workato exposes it.
- **Handling JSON** - `kb/docs/en/features/handling-json.md` - Learn how to handle raw JSON in Workato recipes using JSON tools by Workato or custom connectors to extract datapills from name/value pairs.
- **Handling SOAP** - `kb/docs/en/features/handling-soap.md` - Learn how to parse and create SOAP messages in Workato recipes. SOAP tools by Workato is deprecated; migrate to Message Templates and XML tools.
- **XML tools by Workato** - `kb/docs/en/features/handling-xml.md` - Learn how to parse, transform, validate, and generate XML in Workato recipes using XML tools by Workato with files from Dropbox, SFTP, or Drive.
- **Handling YAML** - `kb/docs/en/features/handling-yaml.md` - Learn how Workato handles YAML content, using YAML tools by Workato to parse files and extract structured values during recipe execution.
- **Workato Logging Service** - `kb/docs/en/features/logging-service.md` - Workato Logging Service provides centralized storage to collect, search, and filter recipe log entries using the Logger by Workato connector.
- **Lookup tables by Workato** - `kb/docs/en/features/lookup-tables.md` - Lookup tables let Workato recipes store, reference, and manage frequently used data in a table of entry rows and value columns, like a cross-reference.
- **Message template by Workato** - `kb/docs/en/features/message-template.md` - Message template by Workato lets you build reusable Mustache templates that generate HTML, text, JSON, and XML messages for your recipes.
- **XML tools by Workato - Parse XML document (Deprecated) action** - `kb/docs/en/features/parse-xml-action.md` - This action extracts data from XML and converts it into datapills for use in recipes. This action is deprecated.
- **XML tools by Workato - Parse XML document action** - `kb/docs/en/features/parse-xml-document.md` - This action converts an XML document into structured output for use in recipes, with optional streaming for large payloads.
- **Encrypt and decrypt files with PGP** - `kb/docs/en/features/pgp-encryption.md` - Encrypt, decrypt, sign, and verify files with the PGP tools by Workato connector to secure data before transfer or storage in shared environments.
- **Project properties - FAQ** - `kb/docs/en/features/project-properties-faq.md` - Answers to common questions about project properties in Workato, including name conflicts and how moving recipes between projects affects values.
- **Project properties - Manage** - `kb/docs/en/features/project-properties-manage.md` - Create, edit, and delete project properties in Workato using the Project properties interface within a project's settings.
- **Project properties - use in recipes** - `kb/docs/en/features/project-properties-use-in-recipes.md` - Use project properties as datapills in Workato recipes within their scope by mapping them from the Recipe data menu into input fields.
- **Project properties** - `kb/docs/en/features/project-properties.md` - Learn how project properties store name-value configuration parameters scoped to a single Workato project for use across recipes and Workflow apps.
- **Features - Runtime user connections** - `kb/docs/en/features/runtime-user-connections.md` - Learn how runtime user connections let recipe users authenticate with their own credentials at runtime instead of the default connection.
- **Use runtime user connections in Recipe functions** - `kb/docs/en/features/runtime-user-connections/using-runtime-user-connections-in-recipe-functions.md` - Set up runtime user connections in recipe functions so actions run with each user's own credentials instead of the default recipe connection.
- **Use runtime user connections in Workbot recipes** - `kb/docs/en/features/runtime-user-connections/using-runtime-user-connections-in-workbot-recipes.md` - Set up runtime user connections in Workbot recipes so users authenticate with their own credentials in Slack or Microsoft Teams commands.
- **Scheduler by Workato** - `kb/docs/en/features/scheduler.md` - Run recipes at customized intervals using the Scheduler by Workato. Configure simple or complex schedules to trigger workflows independent of external app events.
- **Scheduler by Workato - Get current time action** - `kb/docs/en/features/scheduler/actions/get-current-time.md` - Use the Get current time action to retrieve the exact date and time at which a recipe step is executed during a job.
- **Scheduler by Workato - Wait for time duration action** - `kb/docs/en/features/scheduler/actions/wait-for-time-duration.md` - Use the Wait for time duration action to pause a job for a specified length of time before carrying out subsequent actions in the recipe.
- **Scheduler by Workato - Wait until specified time action** - `kb/docs/en/features/scheduler/actions/wait-until-specified-time.md` - Use the Wait until specified time action to specify the time to wait until before proceeding on to the next step.
- **Scheduler by Workato - New recurring event trigger** - `kb/docs/en/features/scheduler/triggers/new-recurring-event.md` - Use the New recurring event trigger to define the interval at which your recipe runs.
- **Secondary connectors** - `kb/docs/en/features/secondary-connectors.md` - Learn how secondary connectors let you connect two instances of the same app in Workato to move and sync data between them in a recipe.
- **File tools by Workato - Transform image file action** - `kb/docs/en/features/transform-image-file.md` - Use the Transform image file action from File tools by Workato to convert images to PNG or JPG and resize them to a set width and height.
- **XML tools by Workato - Transform XML using XSLT (Deprecated) action** - `kb/docs/en/features/transform-xml-using-xslt-deprecated.md` - This action applies an XSLT script to transform XML into another format. Supports XSLT 1.1 and earlier. This action is deprecated.
- **XML tools by Workato - Transform XML using XSLT action** - `kb/docs/en/features/transform-xml-using-xslt.md` - This action applies an XSLT script to transform XML into another format. Supports XSLT 1.1 and earlier.
- **Transformation maps** - `kb/docs/en/features/transformation-maps.md` - Use transformation maps to visually map input fields to an output schema and transform values with formulas.
- **Create a transformation map** - `kb/docs/en/features/transformation-maps/create-map.md` - Define transformation map input and output schemas, map and transform fields with formulas, and test a map before you use it in a recipe.
- **Example transformation maps** - `kb/docs/en/features/transformation-maps/map-examples.md` - Example transformation maps that reshape a list, aggregate a list by a key, chain formulas, flatten a nested array, and join two arrays.
- **File tools by Workato - Uncompress a file action** - `kb/docs/en/features/uncompress-files.md` - Use the Uncompress a file action from File tools by Workato to extract .zip, .tar.gz, and .gz files from any connected app.
- **XML tools by Workato - Validate XML document with XSD action** - `kb/docs/en/features/validate-xml-with-xsd.md` - Use XML tools by Workato to validate an XML document against an XSD schema, enforcing structure, element order, and data types.
- **Variables by Workato** - `kb/docs/en/features/variables.md` - Variables by Workato lets you declare mutable, typed datapills that hold and update values within the scope of a single recipe job.
- **Workato FileStorage** - `kb/docs/en/features/workato-filestorage.md` - Workato FileStorage lets you create, store, append to, and retrieve files within Workato recipes, and organize them into directories.
- **Handling files and attachments** - `kb/docs/en/handling-files-and-attachments.md` - Learn how Workato moves and parses files and attachments across FTP, file systems, APIs, and S3, handling both text and binary file formats.
- **Long actions** - `kb/docs/en/recipes/long-actions.md` - Learn how Workato long actions process bulk data over minutes to hours without timeout errors, including supported connectors and long pauses.
- **Regex overview** - `kb/docs/en/regex.md` - Learn how to use regex in Workato to match text patterns, extract information, and validate input across formulas, recipes, and Workflow apps.
- **Resources** - `kb/docs/en/resources.md` - Learn how Workato resources let you define common files once, including XSD, XSLT, and WSDL, and reference them across recipes.
- **Resources - Recipe integration** - `kb/docs/en/resources/recipe-integration.md` - Use resources as data sources in recipe actions.
- **Resources - Resource management** - `kb/docs/en/resources/resource-management.md` - Upload, view, update, download, delete, move, and version Workato resources using the Workato UI.

## Modify recipe data

- **Data types** - `kb/docs/en/data-types/data-types.md` - Reference for the data types Workato supports, including string, integer, date, list, object, boolean, and duration.
- **Duration data type** - `kb/docs/en/data-types/duration-data-type.md` - The duration data type converts duration to a number (in seconds).
- **Lists FAQs** - `kb/docs/en/features/list-management-faqs.md` - Answers to common questions about working with lists in Workato, including mapping list datapills, processing batches, and reading CSV files.
- **Lists** - `kb/docs/en/features/list-management.md` - Learn how to read, process, and write lists in Workato recipes, including how list datapills appear in the datatree and ways to map them.
- **Formulas** - `kb/docs/en/formulas.md` - Learn how Workato formulas transform and format data across strings, numbers, dates, lists, and complex types using allowlisted Ruby methods.
- **List and Hash Formulas** - `kb/docs/en/formulas/array-list-formulas.md` - Learn how to use Workato list and hash formulas to work with arrays, hashes, and lists of hashes when transforming complex data.
- **Complex data types** - `kb/docs/en/formulas/complex-data-types.md` - Learn how to use formula mode in Workato to map complex data types like objects and arrays, including JSON, in recipe input fields.
- **Formula mode - Add conditions to formulas** - `kb/docs/en/formulas/conditions.md` - Learn how to add conditional logic to Workato formulas using Ruby ternary syntax to handle missing values and unexpected data.
- **Date formulas FAQs** - `kb/docs/en/formulas/date-formulas-faqs.md` - Find answers to common questions about date and datetime formulas in Workato, including arithmetic, from_now, and wday.
- **Date formulas** - `kb/docs/en/formulas/date-formulas.md` - Learn how to use Workato date and datetime formulas to manipulate dates and perform date arithmetic with days, months, and years.
- **Formula mode** - `kb/docs/en/formulas/formula-mode.md` - Learn how to switch to formula mode in Workato to apply approved formulas, transform data, and format text in recipe input fields.
- **List and hash formulas FAQs** - `kb/docs/en/formulas/list-formula-faqs.md` - Find answers to common questions about list and hash formulas in Workato, including indexing, negative indexes, first, and last.
- **Number formulas** - `kb/docs/en/formulas/number-formulas.md` - Learn how to use Workato number formulas for integers and decimals, including arithmetic operations and how result types are returned.
- **Other formulas** - `kb/docs/en/formulas/other-formulas.md` - Reference for Workato formulas that work across data types, including null, clear, and accessing nested values with square brackets.
- **String formulas FAQs** - `kb/docs/en/formulas/string-formulas-faqs.md` - Answers to common questions about Workato string formulas, including conditionals, text manipulation, and checking for substrings.
- **String formulas** - `kb/docs/en/formulas/string-formulas.md` - Reference for Workato string formulas, allowlisted Ruby methods that manipulate text with conditionals, formatting, and substring checks.
- **Datapills and fields mapping** - `kb/docs/en/recipes/data-pills-and-mapping.md` - Learn how datapills work in Workato recipes as variables that map trigger and action output data between app fields.
- **Troubleshooting - Formula troubleshooting** - `kb/docs/en/troubleshooting/formula-troubleshooting.md` - Learn how to use Workato formulas to transform, validate, and process recipe data, with solutions for common formatting scenarios.

## Projects

- **Projects FAQs** - `kb/docs/en/recipes/projects-faqs.md` - Answers to common questions about Workato projects, including what they are, how to organize them, and their key components.
- **Tags for assets** - `kb/docs/en/recipes/tags.md` - Learn how tags in Workato categorize assets to organize and filter them across projects.

## Recipe editor

- **Collaboration safeguards** - `kb/docs/en/recipes/collaboration-safeguards.md` - Learn how Workato collaboration safeguards show when teammates are editing a recipe to prevent lost work and conflicting changes.
- **Recipe keyboard shortcuts** - `kb/docs/en/recipes/keyboard-shortcuts.md` - Reference for Workato recipe design keyboard shortcuts on Mac and Windows, covering zoom, save, undo, redo, comments, and skipping steps.

## Recipes

- **Connections** - `kb/docs/en/connections.md` - Learn how Workato connections authorize recipes to interact with apps through triggers and actions, and how to create and reuse them.
- **Custom OAuth profiles** - `kb/docs/en/custom-oauth-profiles.md` - Use custom OAuth profiles to connect Workato with your own OAuth apps for greater control over scopes, security, branding, and authentication.
- **Batch processing** - `kb/docs/en/features/batch-processing.md` - Learn how batch processing lets one Workato job handle multiple records at once to boost speed and throughput when moving large data volumes.
- **Conditions** - `kb/docs/en/features/conditions.md` - Learn how to build IF conditions in Workato recipes using a data field, condition, and value, and combine them with AND or OR operators.
- **IF control statements** - `kb/docs/en/features/if-conditions.md` - Learn how IF control statements add branching logic to Workato recipes using IF, ELSE IF, and ELSE conditions to direct recipe execution.
- **Actions** - `kb/docs/en/recipes/actions.md` - Learn how Workato recipe actions work, including create, update, upsert, search, get, and delete operations across connectors.
- **Recipes - Connection FAQs** - `kb/docs/en/recipes/connection-faqs.md` - Answers to common questions about Workato connections, including who can create them, how access works, and managing app instances.
- **Repeat while loop** - `kb/docs/en/recipes/loops.md` - Learn how to build a Repeat while loop in Workato that runs steps at least once and continues while a condition is met, with page and count examples.
- **Repeat for each loop** - `kb/docs/en/recipes/repeat-for-each.md` - Learn how the Repeat for each loop in Workato runs nested recipe actions once for every item in a list datapill.
- **Steps** - `kb/docs/en/recipes/steps.md` - Learn how recipe steps in Workato define automation logic with actions, IF conditions, Repeat steps, and error handling.
- **Recipe steps - Skip step** - `kb/docs/en/recipes/steps/skip-step.md` - Learn how to mark recipe steps as skipped in Workato to build and test automation logic incrementally at runtime.
- **Recipe steps - FAQs** - `kb/docs/en/recipes/steps/steps-faqs.md` - Answers to common questions about recipe steps in Workato, including action steps, conditional steps, and repeat steps.
- **Triggers** - `kb/docs/en/recipes/triggers.md` - Triggers define events for recipe execution, process data reliably, and operate using polling, real-time, scheduled, or change data capture mechanisms with single, batch, or bulk dispatches.
- **Recipe building - Copy paste steps** - `kb/docs/en/troubleshooting/tips-and-tricks/copy-paste.md` - Learn how to copy and paste steps within a Workato recipe or across recipes while preserving step order, logic, and app connections.
