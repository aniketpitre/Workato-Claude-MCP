---
url: 'https://docs.workato.com/en/workato-api/resources.md'
description: >-
  Reference index of all Workato Developer API endpoints, including Agent
  Studio, API clients, projects, recipes, roles, and more.
---

# Developer API endpoints

## Agent Studio

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/agentic/genies](/en/workato-api/agent-studio#genies) | Returns a list of genies. |
| POST | [/api/agentic/genies](/en/workato-api/agent-studio#create-a-genie) | Creates a new genie. |
| PUT | [/api/agentic/genies/:id](/en/workato-api/agent-studio#update-a-genie) | Updates an existing genie. |
| GET | [/api/agentic/genies/:id](/en/workato-api/agent-studio#get-a-genie-by-id) | Returns the genie associated with the ID you specify. |
| DELETE | [/api/agentic/genies/:id](/en/workato-api/agent-studio#delete-a-genie) | Deletes a genie. |
| POST | [/api/agentic/genies/:id/start](/en/workato-api/agent-studio#start-a-genie) | Starts the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/stop](/en/workato-api/agent-studio#stop-a-genie) | Stops the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/assign\_skills](/en/workato-api/agent-studio#assign-a-skill-to-a-genie) | Assigns skills and MCP servers to the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/remove\_skills](/en/workato-api/agent-studio#remove-a-skill-from-a-genie) | Removes skills from the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/assign\_knowledge\_bases](/en/workato-api/agent-studio#assign-a-knowledge-base-to-a-genie) | Assigns knowledge bases to the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/remove\_knowledge\_bases](/en/workato-api/agent-studio#remove-a-knowledge-base-from-a-genie) | Removes knowledge bases from the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/assign\_user\_groups](/en/workato-api/agent-studio#assign-a-user-group-to-a-genie) | Assigns user group access to the genie associated with the ID you specify. |
| POST | [/api/agentic/genies/:id/remove\_user\_groups](/en/workato-api/agent-studio#remove-a-user-group-from-a-genie) | Removes user group access from the genie associated with the ID you specify. |
| GET | [/api/agentic/genies/clients](/en/workato-api/agent-studio#list-genie-clients) | Returns a list of genie clients. |
| POST | [/api/agentic/genies/clients](/en/workato-api/agent-studio#create-a-genie-client) | Creates a new genie client (API key or OAuth). |
| GET | [/api/agentic/genies/clients/:client\_id](/en/workato-api/agent-studio#get-a-genie-client) | Returns the genie client associated with the ID you specify. |
| PUT | [/api/agentic/genies/clients/:client\_id](/en/workato-api/agent-studio#update-a-genie-client) | Updates a genie client's name and OAuth redirect URLs. |
| DELETE | [/api/agentic/genies/clients/:client\_id](/en/workato-api/agent-studio#delete-a-genie-client) | Deletes a genie client. |
| POST | [/api/agentic/genies/clients/:client\_id/regenerate](/en/workato-api/agent-studio#regenerate-a-genie-client-key) | Regenerates the API key for a genie client. |
| POST | [/api/agentic/genies/clients/:client\_id/pause](/en/workato-api/agent-studio#pause-a-genie-client) | Pauses a genie client. |
| POST | [/api/agentic/genies/clients/:client\_id/start](/en/workato-api/agent-studio#start-a-genie-client) | Starts a paused genie client. |
| POST | [/api/agentic/genies/:id/clients](/en/workato-api/agent-studio#attach-a-client-to-a-genie) | Attaches a client to a genie. |
| DELETE | [/api/agentic/genies/:id/clients/:client\_id](/en/workato-api/agent-studio#detach-a-client-from-a-genie) | Detaches a client from a genie. |
| GET | [/api/agentic/genies/:genie\_id/interfaces](/en/workato-api/agent-studio#list-chat-interface-triggers) | Returns all chat interface triggers of a genie in a single list. |
| GET | [/api/agentic/genies/:genie\_id/conversations](/en/workato-api/agent-studio#list-conversations) | Returns a list of a genie's conversations. Doesn't include event-level detail. |
| GET | [/api/agentic/genies/:genie\_id/conversations/:conversation\_id](/en/workato-api/agent-studio#get-a-conversation) | Returns a genie conversation you specify. Doesn't include event-level detail. |
| GET | [/api/agentic/genies/:genie\_id/conversations/:conversation\_id/events](/en/workato-api/agent-studio#list-conversation-events) | Returns the full events of a single conversation. |
| GET | [/api/agentic/genies/:genie\_id/guardrails](/en/workato-api/agent-studio#get-a-genies-guardrail) | Returns the guardrail and its policies for the genie associated with the ID you specify. |
| PUT | [/api/agentic/genies/:genie\_id/guardrails/policies/:policy\_type](/en/workato-api/agent-studio#create-or-update-a-policy) | Creates or updates a single guardrail policy on the genie associated with the ID you specify. |
| GET | [/api/agentic/genies/guardrails/policies/pii\_entities](/en/workato-api/agent-studio#list-pii-entity-types) | Returns the list of PII entity type strings you can use in a `pii_detection` policy. |
| GET | [/api/agentic/knowledge\_bases](/en/workato-api/agent-studio#list-knowledge-bases) | Returns a list of knowledge bases. |
| POST | [/api/agentic/knowledge\_bases](/en/workato-api/agent-studio#create-a-knowledge-base) | Creates a new knowledge base. |
| GET | [/api/agentic/knowledge\_bases/:id](/en/workato-api/agent-studio#get-a-knowledge-base-by-id) | Returns the knowledge base associated with the ID you specify. |
| PUT | [/api/agentic/knowledge\_bases/:id](/en/workato-api/agent-studio#update-a-knowledge-base) | Updates an existing knowledge base. |
| DELETE | [/api/agentic/knowledge\_bases/:id](/en/workato-api/agent-studio#delete-a-knowledge-base) | Deletes a knowledge base. |
| GET | [/api/agentic/knowledge\_bases/:id/data\_sources](/en/workato-api/agent-studio#get-knowledge-base-data-sources) | Returns the data sources associated with the knowledge base ID you specify. |
| GET | [/api/agentic/knowledge\_bases/:id/recipes](/en/workato-api/agent-studio#get-knowledge-base-recipes) | Returns the recipes associated with the knowledge base ID you specify. |
| GET | [/api/agentic/skills](/en/workato-api/agent-studio#list-skills) | Returns a list of skills. |
| POST | [/api/agentic/skills](/en/workato-api/agent-studio#create-a-skill) | Creates a new skill. |
| GET | [/api/agentic/skills/:id](/en/workato-api/agent-studio#get-a-skill-by-id) | Returns the skill associated with the ID you specify. |

* * *

## API clients

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/developer\_api\_clients](/en/workato-api/api-client-apis#list-developer-api-clients) | List **Developer API Clients**. |
| POST | [/api/developer\_api\_clients](/en/workato-api/api-client-apis#create-developer-api-client) | Create a **Developer API Client**. |
| GET | [/api/developer\_api\_clients/:id](/en/workato-api/api-client-apis#get-developer-api-client-by-id) | Get a **Developer API Client by ID**. |
| PUT | [/api/developer\_api\_clients/:id](/en/workato-api/api-client-apis#update-developer-api-client) | Update a **Developer API Clients**. |
| DELETE | [/api/developer\_api\_clients/:id](/en/workato-api/api-client-apis#delete-developer-api-client) | Delete a **Developer API Client**. |
| POST | [/api/developer\_api\_clients/:id/regenerate](/en/workato-api/api-client-apis#regenerate-developer-api-client-token) | Regenerate a **Developer API Client token**. |
| GET | [/api/developer\_api\_client\_roles](/en/workato-api/api-client-apis#list-developer-api-client-roles) | List **Developer API Client roles**. |

* * *

## API platform

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/api\_collections](/en/workato-api/api-platform#list-api-collections) | List API collections. |
| POST | [/api/api\_collections](/en/workato-api/api-platform#create-api-collection) | Create an API collection. |
| PUT | [/api/api\_collections/:id](/en/workato-api/api-platform#update-api-collection) | Update an existing API collection. |
| DELETE | [/api/api\_collections/:id](/en/workato-api/api-platform#delete-api-collection) | Delete an API collection along with its endpoints. |
| GET | [/api/api\_collections/:id/openapi](/en/workato-api/api-platform#get-api-collection-openapi-specification) | Get the OpenAPI specification for an API collection. |
| GET | [/api/api\_endpoints](/en/workato-api/api-platform#list-api-endpoints) | List API endpoints in a collection. |
| POST | [/api/api\_collections/:id/api\_endpoints](/en/workato-api/api-platform#create-api-endpoint) | Create an API endpoint within a collection you specify. |
| PUT | [/api/api\_collections/:api\_collection\_id/api\_endpoints/:api\_endpoint\_id](/en/workato-api/api-platform#update-api-endpoint) | Update an existing API endpoint. |
| PUT | [/api/api\_endpoints/:id/enable](/en/workato-api/api-platform#enable-api-endpoint) | Enable an API endpoint in a collection. |
| PUT | [/api/api\_endpoints/:id/disable](/en/workato-api/api-platform#disable-api-endpoint) | Disable an API endpoint in a collection. |
| GET | [/api/api\_endpoints/:id/openapi](/en/workato-api/api-platform#get-api-endpoint-openapi-specification) | Get the OpenAPI specification for an API endpoint. |
| GET | [/api/api\_clients](/en/workato-api/api-platform#list-api-clients) | List API clients. We recommend that you migrate to the [List API clients (v2)](/en/workato-api/api-platform#list-api-clients-v2) endpoint to prepare for future deprecation. |
| GET | [/api/v2/api\_clients](/en/workato-api/api-platform#list-api-clients-v2) | List all **API clients**. Workato includes the `project_id` of the project associated with the API client in the response. |
| POST | [/api/api\_clients](/en/workato-api/api-platform#create-api-client) | Create an API client. We recommend that you migrate to the [Create API client (v2)](/en/workato-api/api-platform#create-api-client-v2) endpoint to prepare for future deprecation. |
| POST | [/api/v2/api\_clients](/en/workato-api/api-platform#create-api-client-v2) | Create a new **API client** within a project you specify. |
| GET | [/api/v2/api\_clients/:api\_client\_id](/en/workato-api/api-platform#get-api-client) | Retrieve details of an API client by ID. |
| PUT | [/api/v2/api\_clients/:api\_client\_id](/en/workato-api/api-platform#update-api-client) | Update an existing API client within a project you specify. |
| DELETE | [/api/v2/api\_clients/:api\_client\_id](/en/workato-api/api-platform#delete-api-client) | Delete an existing API client. |
| GET | [/api/api\_access\_profiles](/en/workato-api/api-platform#list-access-profiles) | List access profiles belonging to an API client. We recommend that you migrate to the [List API keys](/en/workato-api/api-platform#list-api-keys) endpoint to prepare for future deprecation. |
| GET | [/api/v2/api\_clients/:api\_client\_id/api\_keys](/en/workato-api/api-platform#list-api-keys) | List **API keys** for an API client. |
| POST | [/api/api\_access\_profiles](/en/workato-api/api-platform#create-access-profile) | Create an access profile belonging to an API client. We recommend that you migrate to the [Create API key](/en/workato-api/api-platform#create-an-api-key) endpoint to prepare for future deprecation. |
| POST | [/api/v2/api\_clients/:api\_client\_id/api\_keys](/en/workato-api/api-platform#create-an-api-key) | Create an **API key** for an API client. |
| PUT | [/api/api\_access\_profiles](/en/workato-api/api-platform#update-access-profile) | Update an access profile belonging to an API client. We recommend that you migrate to the [Update API key](/en/workato-api/api-platform#update-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id](/en/workato-api/api-platform#update-api-key) | Update an **API key** for an API client. |
| PUT | [/api\_access\_profiles](/en/workato-api/api-platform#enable-access-profile) | Enable an access profile belonging to an API client. We recommend that you migrate to the [Enable API key](/en/workato-api/api-platform#enable-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/enable](/en/workato-api/api-platform#enable-api-key) | Enable an **API key** for an API client. |
| PUT | [/api\_access\_profiles](/en/workato-api/api-platform#disable-access-profile) | Disable an access profile belonging to an API client. We recommend that you migrate to the [Disable API key](/en/workato-api/api-platform#disable-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/disable](/en/workato-api/api-platform#disable-api-key) | Disable an **API key** for an API client. |
| PUT | [/api/api\_access\_profiles/:id/refresh\_secret](/en/workato-api/api-platform#refresh-token-secret) | Refreshes access profile key or secret. We recommend that you migrate to the [Refresh API key secret](/en/workato-api/api-platform#refresh-api-key-secret) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/refresh\_secret](/en/workato-api/api-platform#refresh-api-key-secret) | Refresh the authentication token or OAuth 2.0 client secret for an API key. |
| DELETE | [/api/v2/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id](/en/workato-api/api-platform#delete-api-key) | Delete an existing API key. |
| GET | [/api/v2/api\_portals](/en/workato-api/api-platform#list-api-portals) | List all API portals associated with API clients in your workspace. |
| GET | [/api/cert\_bundles](/en/workato-api/api-platform#list-certificate-bundles) | List all certificate bundles. |
| POST | [/api/cert\_bundles](/en/workato-api/api-platform#create-a-certificate-bundle) | Create a new certificate bundle. |
| PUT | [/api/cert\_bundles/:id](/en/workato-api/api-platform#update-a-certificate-bundle) | Update a certificate bundle. |
| DELETE | [/api/cert\_bundles/:id](/en/workato-api/api-platform#delete-a-certificate-bundle) | Delete a certificate bundle. |
| GET | [/api/cert\_bundles/:id/download](/en/workato-api/api-platform#download-a-certificate-bundle) | Download the certificate bundle PEM file. |

* * *

## Collaborator groups

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/user\_groups](/en/workato-api/collaborator-groups#list-groups) | List collaborator groups. |
| GET | [/api/user\_groups/:id](/en/workato-api/collaborator-groups#get-group) | Get collaborator group details. |
| POST | [/api/user\_groups](/en/workato-api/collaborator-groups#create-group) | Create a collaborator group. |
| PUT | [/api/user\_groups/:id](/en/workato-api/collaborator-groups#update-group) | Update a collaborator group. |
| DELETE | [/api/user\_groups/:id](/en/workato-api/collaborator-groups#delete-group) | Delete a collaborator group. |
| GET | [/api/user\_groups/:id/members](/en/workato-api/collaborator-groups#list-members) | List collaborator group members. |
| POST | [/api/user\_groups/:id/members](/en/workato-api/collaborator-groups#add-members) | Add members to a collaborator group. |
| DELETE | [/api/user\_groups/:id/members](/en/workato-api/collaborator-groups#remove-members) | Remove members from a collaborator group. |
| GET | [/api/user\_groups/:id/project\_grants](/en/workato-api/collaborator-groups#list-collaborator-grants) | List a collaborator group's project grants. |

* * *

## Connections

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/connections](/en/workato-api/connections#list-connections) | Returns all connections and associated data. |
| POST | [/api/connections/:connection\_id/pick\_list](/en/workato-api/connections#get-picklist-values) | Gets picklist values for a connection. |
| POST | [/api/connections](/en/workato-api/connections#connections-create) | Creates a connection, including custom LLM and MCP server connections. |
| PUT | [/api/connections/:connection\_id](/en/workato-api/connections#update-a-connection) | Updates a connection. |
| POST | [/api/connections/:connection\_id/disconnect](/en/workato-api/connections#disconnect-a-connection) | Disconnects a connection. |
| DELETE | [/api/connections/:connection\_id](/en/workato-api/connections#delete-a-connection) | Deletes a connection. |

* * *

## Connectors

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/integrations](/en/workato-api/api-connectors#list-connector-metadata) | Returns a list of connectors and metadata specified in request. |
| GET | [/api/integrations/all](/en/workato-api/api-connectors#list-all-platform-connectors) | Returns a paginated list of all connectors and associated metadata in a non-embedded workspace. The response includes standard and platform connectors. |

* * *

## Cross-workspace sharing

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/cross\_workspace/grants](/en/workato-api/cross-workspace-sharing#list-outgoing-grants) | Retrieve a list of outgoing grants. |
| GET | [/api/cross\_workspace/grants/:handle](/en/workato-api/cross-workspace-sharing#get-an-outgoing-grant) | Get an outgoing grant by handle. |
| POST | [/api/cross\_workspace/grants](/en/workato-api/cross-workspace-sharing#create-a-grant) | Create a grant. |
| PUT | [/api/cross\_workspace/grants/:handle](/en/workato-api/cross-workspace-sharing#update-a-grant) | Update a grant. |
| DELETE | [/api/cross\_workspace/grants/:handle](/en/workato-api/cross-workspace-sharing#revoke-a-grant) | Revoke a grant. |
| GET | [/api/cross\_workspace/incoming\_grants](/en/workato-api/cross-workspace-sharing#list-incoming-grants) | Retrieve a list of incoming grants. |
| GET | [/api/cross\_workspace/incoming\_grants/:handle](/en/workato-api/cross-workspace-sharing#get-an-incoming-grant) | Get an incoming grant by handle. |
| GET | [/api/cross\_workspace/source\_environments](/en/workato-api/cross-workspace-sharing#list-source-environments) | Retrieve environments that can act as a grant source. |
| GET | [/api/cross\_workspace/target\_environments](/en/workato-api/cross-workspace-sharing#list-target-environments) | Retrieve environments grantable from a given source. |

* * *

## Custom connectors

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/custom\_connectors](/en/workato-api/custom_connectors#search-custom-connector) | Get custom connectors. |
| POST | [/api/sdk/validate\_code](/en/workato-api/custom_connectors#validate-custom-connector-code) | Validates custom connector code for syntax and semantic errors. |
| POST | [/api/sdk/generate\_schema/json](/en/workato-api/custom_connectors#generate-schema-from-json) | Generates Workato schema from a stringified JSON sample. |
| POST | [/api/sdk/generate\_schema/csv](/en/workato-api/custom_connectors#generate-schema-from-csv) | Generates Workato schema from a stringified CSV sample. |

* * *

## Custom OAuth profiles

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/custom\_oauth\_profiles](/en/workato-api/custom-oauth-profiles#list-custom-oauth-profiles) | List Custom OAuth profiles |
| GET | [/api/custom\_oauth\_profiles/:id](/en/workato-api/custom-oauth-profiles#get-custom-oauth-profile-by-id) | Get Custom OAuth profile by ID |
| POST | [/api/custom\_oauth\_profiles](/en/workato-api/custom-oauth-profiles#create-custom-oauth-profile) | Create Custom OAuth profile |
| PUT | [/api/custom\_oauth\_profiles/:id](/en/workato-api/custom-oauth-profiles#update-custom-oauth-profile) | Update Custom OAuth profile |
| DELETE | [/api/custom\_oauth\_profiles/:id](/en/workato-api/custom-oauth-profiles#delete-custom-oauth-profile) | Delete Custom OAuth profile |

* * *

## Data pipelines

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/data\_pipelines](/en/workato-api/data-pipelines#list-data-pipelines) | List data pipelines. |
| GET | [/api/data\_pipelines/:data\_pipeline\_id](/en/workato-api/data-pipelines#get-a-data-pipeline) | Get a data pipeline. |
| POST | [/api/data\_pipelines](/en/workato-api/data-pipelines#create-a-data-pipeline) | Create a data pipeline. |
| PUT | [/api/data\_pipelines/:data\_pipeline\_id](/en/workato-api/data-pipelines#update-a-data-pipeline) | Update a data pipeline. |
| DELETE | [/api/data\_pipelines/:data\_pipeline\_id](/en/workato-api/data-pipelines#delete-a-data-pipeline) | Delete a data pipeline. |
| POST | [/api/data\_pipelines/:data\_pipeline\_id/clone](/en/workato-api/data-pipelines#clone-a-data-pipeline) | Clone a data pipeline. |
| PUT | [/api/data\_pipelines/:data\_pipeline\_id/start](/en/workato-api/data-pipelines#start-a-data-pipeline) | Start a data pipeline. |
| PUT | [/api/data\_pipelines/:data\_pipeline\_id/stop](/en/workato-api/data-pipelines#stop-a-data-pipeline) | Stop a data pipeline. |
| GET | [/api/data\_pipelines/sources](/en/workato-api/data-pipelines#list-source-providers) | List source providers. |
| GET | [/api/data\_pipelines/destinations](/en/workato-api/data-pipelines#list-destination-providers) | List destination providers. |
| POST | [/api/data\_pipelines/source\_objects](/en/workato-api/data-pipelines#list-source-objects) | List the objects available from a source connection. |
| POST | [/api/data\_pipelines/source\_object\_fields](/en/workato-api/data-pipelines#list-source-object-fields) | List the fields of a source object. |
| POST | [/api/data\_pipelines/:data\_pipeline\_id/configuration](/en/workato-api/data-pipelines#get-configuration-schema) | Get the configuration schema for a pipeline and validate configuration values. |
| GET | [/api/data\_pipelines/:data\_pipeline\_id/objects](/en/workato-api/data-pipelines#list-pipeline-objects) | List the objects in a data pipeline. |
| POST | [/api/data\_pipelines/:data\_pipeline\_id/resync](/en/workato-api/data-pipelines#re-sync-objects) | Re-sync objects in a data pipeline. |
| GET | [/api/data\_pipelines/:data\_pipeline\_id/runs](/en/workato-api/data-pipelines#list-pipeline-runs) | List object runs for a data pipeline. |
| GET | [/api/data\_pipelines/:data\_pipeline\_id/runs/:run\_id](/en/workato-api/data-pipelines#get-a-pipeline-run) | Get an object run. |

* * *

## Data tables

### Table management APIs

Base URL: `https://app.workato.com`

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/data\_tables](/en/workato-api/data-tables#list-data-tables) | List all data tables. |
| GET | [/api/data\_tables/:data\_table\_id](/en/workato-api/data-tables#get-data-table-by-id) | Get data table by ID. |
| POST | [/api/data\_tables](/en/workato-api/data-tables#create-data-table) | Creates a data table. |
| PUT | [/api/data\_tables/:data\_table\_id](/en/workato-api/data-tables#update-data-table) | Updates a data table. |
| DELETE | [/api/data\_tables/:data\_table\_id](/en/workato-api/data-tables#delete-data-table) | Deletes a data table. |
| POST | [/api/data\_tables/:data\_table\_id/truncate](/en/workato-api/data-tables#truncate-data-table) | Truncates a data table. |

### Record manipulation APIs

Base URL: `https://data-tables.workato.com`

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v1/tables/:data\_table\_id/query](/en/workato-api/data-tables#query-records) | Queries records using filters you specify. |
| POST | [/api/v1/tables/:data\_table\_id/records](/en/workato-api/data-tables#create-record) | Creates a new record. |
| PUT | [/api/v1/tables/:data\_table\_id/records/:record\_id](/en/workato-api/data-tables#update-record) | Updates an existing record. |
| DELETE | [/api/v1/tables/:data\_table\_id/records/:record\_id](/en/workato-api/data-tables#delete-record) | Deletes a record you specify. |
| POST | [/api/v1/tables/:data\_table\_id/fields/:field\_id/file](/en/workato-api/data-tables#generate-link-to-upload-file) | Generates a link to upload a file. |
| GET | [/api/v1/tables/:data\_table\_id/records/:record\_id/fields/:field\_id/file](/en/workato-api/data-tables#download-file-from-the-record) | Generates a link to download a file. |

### Record import APIs

Base URL: `https://data-tables.workato.com`, except [Upload file](/en/workato-api/data-tables#upload-file), which posts to the signed URL returned by [Create file upload link](/en/workato-api/data-tables#create-file-upload-link).

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v1/tables/:data\_table\_id/records/import/file/upload\_link](/en/workato-api/data-tables#create-file-upload-link) | Creates a link to upload a file. |
| POST | [/sharing/files](/en/workato-api/data-tables#upload-file) | Uploads the file to the signed link. |
| DELETE | [/api/v1/tables/:data\_table\_id/records/import/file](/en/workato-api/data-tables#delete-uploaded-file) | Deletes the uploaded file. |
| GET | [/api/v1/tables/:data\_table\_id/records/import/file](/en/workato-api/data-tables#describe-uploaded-file) | Describes the uploaded file. |
| POST | [/api/v1/tables/:data\_table\_id/records/import/start](/en/workato-api/data-tables#start-import) | Starts importing records from the uploaded file. |
| DELETE | [/api/v1/tables/:data\_table\_id/records/import](/en/workato-api/data-tables#dismiss-import) | Dismisses or cancels the import. |

* * *

## Environment management

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/secrets\_management/clear\_cache](/en/workato-api/environment-management#clear-secrets-management-cache) | Clears the secrets management cache. |
| GET | [/api/activity\_logs](/en/workato-api/environment-management#get-audit-log) | Retrieves activity audit log records. |
| GET | [/api/tags](/en/workato-api/environment-management#list-tags) | Retrieves a list of tags. |
| POST | [/api/tags](/en/workato-api/environment-management#create-a-tag) | Creates a tag. |
| PUT | [/api/tags/:handle](/en/workato-api/environment-management#update-a-tag) | Updates a tag. |
| DELETE | [/api/tags/:handle](/en/workato-api/environment-management#delete-a-tag) | Deletes a tag. |

* * *

## Environment properties

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/properties](/en/workato-api/account-properties#list-properties-by-prefix) | Lists environment properties that matches a prefix. |
| POST | [/api/properties](/en/workato-api/account-properties#upsert-property) | Upserts environment properties. |

* * *

## Environment roles

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/environment\_roles](/en/workato-api/environment-roles#list-env-roles) | List environment roles. |
| GET | [/api/environment\_roles/:id](/en/workato-api/environment-roles#get-env-role) | Get environment role details. |
| POST | [/api/environment\_roles](/en/workato-api/environment-roles#create-env-role) | Create an environment role. |
| PUT | [/api/environment\_roles/:id](/en/workato-api/environment-roles#update-env-role) | Update an environment role. |
| DELETE | [/api/environment\_roles/:id](/en/workato-api/environment-roles#delete-env-role) | Delete an environment role. |

* * *

## Event streams

### Public APIs

| Type | Resource | Description |
| --- | --- | --- |
| POST | [event-streams.workato.com/api/v1/topics/:topic\_id/consume](/en/workato-api/pubsub#consume-messages) | Consume messages from a topic. |
| POST | [event-streams.workato.com/api/v1/topics/:topic\_id/publish](/en/workato-api/pubsub#publish-message) | Publish a message to a topic. |
| POST | [event-streams.workato.com/api/v1/batch/topics/:topic\_id/publish](/en/workato-api/pubsub#publish-a-batch-of-messages) | Publish a batch of messages to a topic. |

### Developer APIs

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/event\_streams/topics](/en/workato-api/event-streams#list-topics) | Retrieve a list of topics. |
| POST | [/api/event\_streams/topics](/en/workato-api/event-streams#create-a-topic) | Create a topic. |
| GET | [/api/event\_streams/topics/:topic\_id](/en/workato-api/event-streams#get-topic-by-id) | Get topic by ID. |
| PUT | [/api/event\_streams/topics/:topic\_id](/en/workato-api/event-streams#update-a-topic) | Update a topic. |
| PUT | [/api/event\_streams/topics/:topic\_id/purge](/en/workato-api/event-streams#purge-a-topic) | Purge a topic. |
| DELETE | [/api/event\_streams/topics/:topic\_id](/en/workato-api/event-streams#delete-a-topic) | Delete a topic. |

* * *

## Folders

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/folders](/en/workato-api/folders#list-folders) | List folders. |
| GET | [/api/projects](/en/workato-api/folders#list-projects) | List projects. |
| GET | [/api/folders/:folder\_id](/en/workato-api/folders#get-a-folder) | Get a folder. |
| POST | [/api/folders](/en/workato-api/folders#create-folder) | Create a project or folder. |
| PUT | [/api/folders/:folder\_id](/en/workato-api/folders#update-a-folder) | Update a folder. |
| PUT | [/api/projects/:project\_id](/en/workato-api/folders#update-a-project) | Update a project. |
| DELETE | [/api/folders/:folder\_id](/en/workato-api/folders#delete-a-folder) | Delete a folder. |
| DELETE | [/api/projects/:project\_id](/en/workato-api/folders#delete-a-project) | Delete a project. |

* * *

## Jobs

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/recipes/:recipe\_id/jobs](/en/workato-api/jobs#list-jobs-from-a-recipe) | List jobs belonging to recipe. |
| GET | [/api/recipes/:recipe\_id/jobs/:job\_handle](/en/workato-api/jobs#get-a-job) | Returns a single job's metadata. |
| POST | [/api/job/resume](/en/workato-api/jobs#job-resume) | Resumes a particular job based on the `resume_token` you provide. This endpoint returns HTTP status code 204, indicating successful request processing without any content included in the response. This endpoint is leveraged by [SDK Wait for resume actions](/en/developing-connectors/sdk/guides/building-actions/wait-for-resume-actions). |
| POST | [/api/recipes/:recipe\_id/repeat\_jobs](/en/workato-api/jobs#repeat-jobs) | Repeats jobs you specify. |
| POST | [/api/recipes/:recipe\_id/cancel\_jobs](/en/workato-api/jobs#cancel-jobs) | Cancels ongoing jobs you specify. |

* * *

## Legacy roles

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/roles](/en/workato-api/roles#list-custom-roles) | List custom roles. |
| PUT | [/api/roles/:role\_id](/en/workato-api/roles#update-custom-role) | Updates a custom role's project privileges. |
| POST | [/api/roles/:role\_id/copy](/en/workato-api/roles#copy-a-custom-role) | Makes a copy of a custom role. |

* * *

## Lookup tables

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/lookup\_tables](/en/workato-api/lookup-tables#list-lookup-tables) | List tables. |
| GET | [/api/lookup\_tables/:lookup\_table\_id/lookup](/en/workato-api/lookup-tables#lookup-row) | Look up a row |
| GET | [/api/lookup\_tables/:lookup\_table\_id/rows](/en/workato-api/lookup-tables#list-rows) | List rows. |
| GET | [/api/lookup\_tables/:lookup\_table\_id/rows/:row\_id](/en/workato-api/lookup-tables#get-row) | Get a row. |
| POST | [/api/lookup\_tables/:lookup\_table\_id/rows](/en/workato-api/lookup-tables#add-row) | Add a row. |
| POST | [/api/lookup\_tables](/en/workato-api/lookup-tables#lut-create) | Create a new lookup table. |
| POST | [/api/lookup\_tables/batch\_delete](/en/workato-api/lookup-tables#lut-delete) | Delete lookup tables in batch. |
| PUT | [/api/lookup\_tables/:lookup\_table\_id/rows/:row\_id](/en/workato-api/lookup-tables#update-row) | Update a row. |
| DELETE | [/api/lookup\_tables/:lookup\_table\_id/rows/:row\_id](/en/workato-api/lookup-tables#delete-row) | Delete a row. |

* * *

## MCP servers

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/mcp/mcp\_servers](/en/workato-api/mcp-servers#list-mcp-servers) | List MCP servers. |
| POST | [/api/mcp/mcp\_servers](/en/workato-api/mcp-servers#create-an-mcp-server) | Create an MCP server. |
| GET | [/api/mcp/mcp\_servers/:handle](/en/workato-api/mcp-servers#get-mcp-server-details) | Retrieve MCP server details. |
| PUT | [/api/mcp/mcp\_servers/:handle](/en/workato-api/mcp-servers#update-an-mcp-server) | Update an MCP server. |
| DELETE | [/api/mcp/mcp\_servers/:handle](/en/workato-api/mcp-servers#delete-an-mcp-server) | Delete an MCP server. |
| POST | [/api/mcp/mcp\_servers/:handle/token\_renew](/en/workato-api/mcp-servers#renew-mcp-server-authentication-token) | Renew MCP server authentication token. |
| POST | [/api/mcp/mcp\_servers/:mcp\_server\_handle/tokens](/en/workato-api/mcp-servers#create-a-hashed-token) | Create a hashed token. |
| DELETE | [/api/mcp/mcp\_servers/:mcp\_server\_handle/tokens/:id](/en/workato-api/mcp-servers#delete-a-hashed-token) | Delete a hashed token. |
| POST | [/api/mcp/mcp\_servers/:mcp\_server\_handle/tokens/:id/refresh](/en/workato-api/mcp-servers#refresh-a-hashed-token) | Refresh a hashed token. |
| POST | [/api/mcp/mcp\_servers/:handle/assign\_tools](/en/workato-api/mcp-servers#assign-tools-to-an-mcp-server) | Assign tools to an MCP server. |
| POST | [/api/mcp/mcp\_servers/:handle/assign\_user\_groups](/en/workato-api/mcp-servers#assign-user-groups-to-an-mcp-server) | Assign user groups to an MCP server. |
| POST | [/api/mcp/mcp\_servers/:handle/remove\_user\_groups](/en/workato-api/mcp-servers#remove-user-groups-from-an-mcp-server) | Remove user groups from an MCP server. |
| PUT | [/api/mcp/mcp\_servers/:handle/update\_folder](/en/workato-api/mcp-servers#move-mcp-server-to-a-different-folder) | Move an MCP server to a different folder. |
| GET | [/api/mcp/mcp\_servers/:mcp\_server\_handle/server\_policies](/en/workato-api/mcp-servers#get-server-policy-configuration) | Retrieve server policy configuration. |
| PUT | [/api/mcp/mcp\_servers/:mcp\_server\_handle/server\_policies](/en/workato-api/mcp-servers#update-server-policy-configuration) | Update server policy configuration. |
| GET | [/api/mcp/mcp\_servers/:mcp\_server\_handle/tools](/en/workato-api/mcp-servers#list-tools-for-an-mcp-server) | List tools for an MCP server. |
| PUT | [/api/mcp/mcp\_servers/:mcp\_server\_handle/tools/:id](/en/workato-api/mcp-servers#update-tool-description) | Update tool description for an MCP. |
| DELETE | [/api/mcp/mcp\_servers/:mcp\_server\_handle/tools/:id](/en/workato-api/mcp-servers#delete-a-tool) | Delete a tool. |
| GET | [/api/mcp/user\_groups](/en/workato-api/mcp-servers#list-identity-provider-user-groups) | List identity provider user groups. |
| GET | [/api/mcp/mcp\_servers/:mcp\_server\_handle/access\_assignments](/en/workato-api/mcp-servers#list-mcp-access-assignments) | List MCP access assignments. |
| POST | [/api/mcp/mcp\_servers/:mcp\_server\_handle/access\_assignments](/en/workato-api/mcp-servers#create-an-mcp-access-assignment) | Create an MCP access assignment. |
| GET | [/api/mcp/mcp\_servers/:mcp\_server\_handle/access\_assignments/:id](/en/workato-api/mcp-servers#get-an-mcp-access-assignment) | Retrieve an MCP access assignment. |
| PUT | [/api/mcp/mcp\_servers/:mcp\_server\_handle/access\_assignments/:id](/en/workato-api/mcp-servers#update-an-mcp-access-assignment) | Update an MCP access assignment. |
| DELETE | [/api/mcp/mcp\_servers/:mcp\_server\_handle/access\_assignments/:id](/en/workato-api/mcp-servers#delete-an-mcp-access-assignment) | Delete an MCP access assignment. |

* * *

## Projects

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/projects/:id/build](/en/workato-api/projects#build-a-project) | Builds a project. Use the [Deploy a project build](/en/workato-api/projects#deploy-a-project-build) endpoint to deploy the project to an environment. |
| GET | [/api/project\_builds/:id](/en/workato-api/projects#get-a-project-build) | Retrieves a project build by its unique ID. |
| POST | [/api/project\_builds/:id/deploy](/en/workato-api/projects#deploy-a-project-build) | Deploys a project build to an environment. Use the [Build a project](/en/workato-api/projects#build-a-project) endpoint to build the project first. |
| POST | [/api/projects/:id/deploy](/en/workato-api/projects#deploy-a-project) | Builds and deploys a project to an environment. |
| GET | [/api/deployments/:id](/en/workato-api/projects#get-a-deployment) | Retrieves a single deployment by its unique ID. |
| GET | [/api/deployments](/en/workato-api/projects#list-deployments) | Retrieves a list of deployments. Use query parameters to filter results by project, folder, or date range. |
| GET | [/api/deployments/:id/eligible\_reviewers](/en/workato-api/projects#list-eligible-reviewers-for-a-deployment) | Retrieves a list of eligible reviewers that can be assigned to review a deployment. |
| POST | [/api/deployments/:id/assign\_reviewers](/en/workato-api/projects#assign-reviewers-to-a-deployment) | Assigns reviewers to a deployment. |
| POST | [/api/deployments/:id/submit\_for\_review](/en/workato-api/projects#submit-a-deployment-for-review) | Submits a deployment for review. |
| POST | [/api/deployments/:id/approve](/en/workato-api/projects#approve-a-deployment) | Approves a deployment. |
| POST | [/api/deployments/:id/reject](/en/workato-api/projects#reject-a-deployment) | Rejects a deployment. |
| POST | [/api/deployments/:id/reopen](/en/workato-api/projects#re-open-a-deployment-for-review) | Re-opens a deployment for review. |
| POST | [/api/deployments/:id/update\_review\_comment](/en/workato-api/projects#update-a-deployment-review-comment) | Updates a deployment review comment. |
| POST | [/api/deployments/:id/deploy](/en/workato-api/projects#deploy-an-approved-deployment) | Deploys an approved deployment. |

* * *

## Project grants

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/project\_grants/:id](/en/workato-api/project-grants#get-grant) | Get a project grant. |
| PUT | [/api/project\_grants/:id](/en/workato-api/project-grants#update-grant) | Update a project grant. |
| DELETE | [/api/project\_grants/:id](/en/workato-api/project-grants#delete-grant) | Delete a project grant. |
| GET | [/api/projects/:id/project\_grants](/en/workato-api/project-grants#list-grants) | List project grants by project ID. |
| PUT | [/api/projects/:id/project\_grants](/en/workato-api/project-grants#add-grants-to-project) | Add or update project grants. |

* * *

## Project properties

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/properties](/en/workato-api/project-properties#list-project-properties) | List project-level properties that match a prefix and project ID. |
| POST | [/api/properties](/en/workato-api/project-properties#upsert-project-properties) | Upsert project-level properties. |

* * *

## Project roles

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/project\_roles](/en/workato-api/project-roles#list-project-roles) | List project roles. |
| GET | [/api/project\_roles/:id](/en/workato-api/project-roles#get-role) | Get project role details. |
| POST | [/api/project\_roles](/en/workato-api/project-roles#create-role) | Create a project role. |
| PUT | [/api/project\_roles/:id](/en/workato-api/project-roles#update-role) | Update a project role. |
| DELETE | [/api/project\_roles/:id](/en/workato-api/project-roles#delete-role) | Delete a project role. |

* * *

## Recipes

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/recipes/:id](/en/workato-api/recipes#get-recipe-details) | Get recipe details. |
| GET | [/api/recipes/job\_counts](/en/workato-api/recipes#list-recipe-job-counts) | Retrieve job success and failure counts for one or more recipes. |
| POST | [/api/recipes](/en/workato-api/recipes#create-a-recipe) | Create recipe. |
| POST | [/api/recipes](/en/workato-api/recipes#copy-a-recipe) | Copy recipe. |
| PUT | [/api/recipes/:id](/en/workato-api/recipes#update-a-recipe) | Update recipe. |
| GET | [/api/recipes](/en/workato-api/recipes#list-recipes-belonging-to-user) | List recipes belonging to user. |
| PUT | [/api/recipes/:id/start](/en/workato-api/recipes#start-recipe) | Start recipe. |
| PUT | [/api/recipes/:id/stop](/en/workato-api/recipes#stop-recipe) | Stop recipe. |
| DELETE | [/api/recipes/:id](/en/workato-api/recipes#delete-recipe) | Delete recipe. |
| POST | [/api/recipes/:recipe\_id/reset\_trigger](/en/workato-api/recipes#reset-recipe-trigger) | Reset recipe trigger. |
| PUT | [/api/recipes/:recipe\_id/connect](/en/workato-api/recipes#update-connection-for-recipe) | Update connection for an application in a stopped recipe. |
| POST | [/api/recipes/:recipe\_id/poll\_now](/en/workato-api/recipes#activate-polling-trigger-for-recipe) | Activate a polling trigger for a recipe. |
| POST | [/api/recipes/:recipe\_id/force\_run](/en/workato-api/recipes#force-run-a-recipe) | Force a recipe to run on demand. |
| GET | [/api/recipes/:recipe\_id/versions](/en/workato-api/recipes#get-recipe-versions) | Get recipe versions. |
| GET | [/api/recipes/:recipe\_id/versions/:id](/en/workato-api/recipes#get-a-specific-recipe-version) | Get details of a recipe version. |
| PATCH/PUT | [/api/recipes/:recipe\_id/versions/:id](/en/workato-api/recipes#update-a-recipe-version-comment) | Update a recipe version comment. |
| GET | [/api/recipes/:recipe\_id/health](/en/workato-api/recipes#get-recipe-health) | Retrieve the most recent optimization report for a recipe. |
| POST | [/api/recipes/:recipe\_id/health](/en/workato-api/recipes#start-analyzing-recipe-health) | Queue a performance scan using [Performance Copilot](/en/recipes/performance-copilot). |

* * *

## Recipe Lifecycle Management

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/export\_manifests/folder\_assets](/en/workato-api/recipe-lifecycle-management#manifest-folder-assets) | View assets in a folder. |
| POST | [api/export\_manifests](/en/workato-api/recipe-lifecycle-management#manifest-create) | Create an export manifest. |
| PUT | [api/export\_manifests/:id](/en/workato-api/recipe-lifecycle-management#manifest-update) | Update an export manifest. |
| GET | [api/export\_manifests/:id](/en/workato-api/recipe-lifecycle-management#manifest-view) | View an export manifest. |
| DELETE | [/api/export\_manifests/:id](/en/workato-api/recipe-lifecycle-management#manifest-delete) | Delete an export manifest. |
| POST | [/api/packages/export/:manifest\_id](/en/workato-api/recipe-lifecycle-management#export-package-based-on-a-manifest) | Export package based on a manifest. |
| POST | [/api/packages/import/:folder\_id](/en/workato-api/recipe-lifecycle-management#import-package-into-a-folder) | Import a package into a folder. |
| GET | [/api/packages/:id](/en/workato-api/recipe-lifecycle-management#get-package-by-id) | Get a package by its ID. |
| GET | [/api/packages/:id/download](/en/workato-api/recipe-lifecycle-management#download-package) | Download a package. |

* * *

## Resources

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/static\_assets/files](/en/workato-api/static-assets#list-resources) | List resources. |
| POST | [/api/static\_assets/files](/en/workato-api/static-assets#upload-a-resource) | Upload a resource. |
| GET | [/api/static\_assets/files/download](/en/workato-api/static-assets#download-a-resource) | Download a resource. |
| DELETE | [/api/static\_assets/files](/en/workato-api/static-assets#delete-a-resource) | Delete a resource. |

* * *

## Role migration

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/roles\_migration/system\_roles](/en/workato-api/role-migration#migrate-system-roles) | Migrate system roles. |
| POST | [/api/roles\_migration/custom\_role](/en/workato-api/role-migration#migrate-a-custom-role) | Migrate a custom role. |

* * *

## Tag assignments

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/tags\_assignments](/en/workato-api/tag-assignments) | Apply tags to or remove tags from assets in your workspace. |

* * *

## Test Automation

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/test\_cases/run\_requests](/en/workato-api/test-automation#request-run) | Run test cases. |
| GET | [/api/test\_cases/run\_requests/{id}](/en/workato-api/test-automation#run-result-get) | Get the current state of a test case run request. |
| GET | [/api/recipes/{recipe\_id}/test\_cases](/en/workato-api/test-automation#test-cases-get) | Get test cases. |

* * *

## Workspace collaborators

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/member\_invitations](/en/workato-api/team#invite-collaborator) | Invite a collaborator to a workspace. |
| GET | [/api/members](/en/workato-api/team#list-collaborators) | Get list of collaborators. |
| GET | [/api/members/:id](/en/workato-api/team#get-collaborator) | Get collaborator details. |
| PUT | [/api/members/:id](/en/workato-api/team#update-collaborator) | Update collaborator roles. |
| DELETE | [/api/members/:id](/en/workato-api/team#delete-collaborator) | Delete a collaborator. |
| GET | [/api/members/:id/project\_grants](/en/workato-api/team#list-project-grants) | List a collaborator's project grants. |
| GET | [/api/members/:id/privileges](/en/workato-api/team#get-privileges) | Get collaborator privileges. |
| GET | [/api/members/:id/projects\_privileges](/en/workato-api/team#get-project-privileges) | Get collaborator project privileges. |

* * *

## Workspace details

### Get details

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/users/me](/en/workato-api/users#auth-user-details-get) | Get details. |

### Workato Identity IAM

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/iam/users](/en/workato-api/workato-identity-iam#list-users) | List users in the workspace. |
| GET | [/api/iam/users/:user-id](/en/workato-api/workato-identity-iam#get-user-by-id) | Retrieve details for a specific user by ID. |
| POST | [/api/iam/users](/en/workato-api/workato-identity-iam#create-user) | Create one or more new users. |
| PUT | [/api/iam/users/:user-id](/en/workato-api/workato-identity-iam#update-user) | Update an existing user. |
| DELETE | [/api/iam/users/:user-id](/en/workato-api/workato-identity-iam#delete-user) | Delete a user from the workspace. |
| POST | [/api/iam/users/:user-id/add\_to\_group](/en/workato-api/workato-identity-iam#add-user-to-group) | Add a user to a specific group. |
| POST | [/api/iam/users/:user-id/remove\_from\_group](/en/workato-api/workato-identity-iam#remove-user-from-group) | Remove a user from a specific group. |
| GET | [/api/iam/user\_groups](/en/workato-api/workato-identity-iam#list-user-groups) | List user groups in the current environment. |
| GET | [/api/iam/user\_groups/:user-group-id](/en/workato-api/workato-identity-iam#get-user-group-by-id) | Retrieve details for a specific user group by ID. |
| POST | [/api/iam/user\_groups](/en/workato-api/workato-identity-iam#create-user-group) | Create a new user group. |
| PUT | [/api/iam/user\_groups/:user-group-id](/en/workato-api/workato-identity-iam#update-user-group) | Update an existing user group. |
| DELETE | [/api/iam/user\_groups/:user-group-id](/en/workato-api/workato-identity-iam#delete-user-group) | Delete a user group. |
| POST | [/api/iam/user\_groups/:user-group-id/add\_users](/en/workato-api/workato-identity-iam#add-users-to-group) | Add multiple users to a group. |
| DELETE | [/api/iam/user\_groups/:user-group-id/remove\_users](/en/workato-api/workato-identity-iam#remove-users-from-group) | Remove multiple users from a group. |
| GET | [/api/iam/user\_groups/:user-group-id/members](/en/workato-api/workato-identity-iam#list-group-members) | List all members of a user group. |
| GET | [/api/iam/app\_links](/en/workato-api/workato-identity-iam#list-app-links) | List app links in the current environment. |
| POST | [/api/iam/app\_links](/en/workato-api/workato-identity-iam#create-app-link) | Create an app link. |
| DELETE | [/api/iam/app\_links/:id](/en/workato-api/workato-identity-iam#delete-app-link) | Delete an app link by ID. |
| DELETE | [/api/iam/app\_links](/en/workato-api/workato-identity-iam#delete-app-links) | Delete app links by IDs. |

* * *

## XChange

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/xchange/packages](/en/workato-api/xchange#list-packages) | List packages visible to the caller. |
| GET | [/api/xchange/packages/:package\_id/versions](/en/workato-api/xchange#list-a-packages-versions) | List a package's versions. |
| GET | [/api/xchange/versions/:version\_id](/en/workato-api/xchange#get-a-package-version) | Get a package version. |
| PUT | [/api/xchange/versions/:version\_id](/en/workato-api/xchange#update-a-versions-metadata) | Update a version's metadata. |
| POST | [/api/xchange/packages/import](/en/workato-api/xchange#import-a-new-package-from-a-zip) | Import a new package from a `.zip`. |
| POST | [/api/xchange/packages/:package\_id/versions/import](/en/workato-api/xchange#import-a-new-package-version-from-a-zip) | Import a new package version from a `.zip`. |
| GET | [/api/xchange/versions/:draft\_id/version\_draft](/en/workato-api/xchange#get-version-creation-status) | Get version creation status. |
| GET | [/api/xchange/packages/versions/:version\_id/export](/en/workato-api/xchange#get-a-version-zip-download-url) | Get a version `.zip` download URL. |
| POST | [/api/xchange/versions/:version\_id/approve](/en/workato-api/xchange#approve-a-package-version) | Approve a package version. |
| POST | [/api/xchange/versions/:version\_id/reject](/en/workato-api/xchange#reject-a-package-version) | Reject a package version. |
| POST | [/api/xchange/versions/:version\_id/reset](/en/workato-api/xchange#reset-a-version-review) | Reset a version review. |
| PUT | [/api/xchange/versions/:version\_id/comment/:review\_id](/en/workato-api/xchange#update-a-review-comment) | Update a review comment. |
| PUT | [/api/xchange/packages/:package\_id/versions/:version\_id/publish](/en/workato-api/xchange#publish-a-version) | Publish a version. |
| PUT | [/api/xchange/packages/:package\_id/versions/:version\_id/unpublish](/en/workato-api/xchange#unpublish-a-version) | Unpublish a version. |
| GET | [/api/xchange/packages/:package\_id/consumers](/en/workato-api/xchange#list-package-consumers) | List the consumers of a package. |
| POST | [/api/xchange/distributions](/en/workato-api/xchange#create-a-distribution-batch) | Create and enqueue a distribution batch. |
| GET | [/api/xchange/distributions](/en/workato-api/xchange#list-distribution-batches) | List distribution batches. |
| GET | [/api/xchange/distributions/:id](/en/workato-api/xchange#get-a-distribution-batch-by-id) | Get a distribution batch by ID. |
| POST | [/api/xchange/distributions/:id/retry\_failed](/en/workato-api/xchange#retry-failed-distributions) | Retry failed distributions in a batch. |
| GET | [/api/xchange/packages/:package\_id/sharing/links](/en/workato-api/xchange#list-sharing-links) | List a package's sharing links. |
| POST | [/api/xchange/packages/:package\_id/sharing/links](/en/workato-api/xchange#create-sharing-links) | Create sharing links. |
| POST | [/api/xchange/packages/:package\_id/sharing/links/:link\_id/activate](/en/workato-api/xchange#activate-a-sharing-link) | Activate a sharing link. |
| POST | [/api/xchange/packages/:package\_id/sharing/links/:link\_id/deactivate](/en/workato-api/xchange#deactivate-a-sharing-link) | Deactivate a sharing link. |
| DELETE | [/api/xchange/packages/:package\_id/sharing/links/:link\_id](/en/workato-api/xchange#delete-a-sharing-link) | Delete a sharing link. |
| PUT | [/api/xchange/packages/:package\_id/versions/:version\_id/share](/en/workato-api/xchange#set-the-packages-shared-link-version) | Set the package's shared-link version. |
| DELETE | [/api/xchange/packages/:package\_id/versions/:version\_id/share](/en/workato-api/xchange#clear-the-packages-shared-link-version) | Clear the package's shared-link version. |
| GET | [/api/xchange/packages/:package\_id/stats](/en/workato-api/xchange#get-package-installation-statistics) | Get package installation statistics. |
| GET | [/api/xchange/packages/:package\_id/installations](/en/workato-api/xchange#get-per-workspace-installation-report) | Get per-workspace installation report. |

* * *

---
