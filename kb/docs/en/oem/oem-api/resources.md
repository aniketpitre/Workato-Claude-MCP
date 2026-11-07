---
url: 'https://docs.workato.com/en/oem/oem-api/resources.md'
description: >-
  Reference index of all Workato Embedded API endpoints, including customers,
  recipes, connections, projects, roles, and more.
---

# Embedded API endpoints

## API clients

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:id/developer\_api\_clients](/en/oem/oem-api/api-clients#list-developer-api-clients) | List all Developer API clients in a customer workspace. |
| POST | [/api/v2/managed\_users/:id/developer\_api\_clients](/en/oem/oem-api/api-platform#create-developer-api-client) | Create a new Developer API client in a customer workspace. |
| GET | [/api/v2/managed\_users/:id/developer\_api\_clients/:id](/en/oem/oem-api/api-clients#get-developer-api-client) | Retrieve details of a Developer API client by ID in a customer workspace. |
| PUT | [/api/v2/managed\_users/:id/developer\_api\_clients/:id](/en/oem/oem-api/api-clients#update-developer-api-client) | Update an existing Developer API client in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:id/developer\_api\_clients/:id](/en/oem/oem-api/api-clients#delete-developer-api-client) | Delete an existing Developer API client in a customer workspace. |
| POST | [/api/v2/managed\_users/:id/developer\_api\_clients/:id/regenerate](/en/oem/oem-api/api-clients#regenerate-a-developer-api-client-token) | Regenerate the token for a Developer API client in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_client\_roles](/en/oem/oem-api/api-clients#list-developer-api-client-roles) | List Developer API client roles in a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/developer\_api\_client\_roles/:id/copy](/en/oem/oem-api/api-clients#copy-developer-api-client-role) | Copy a Developer API client role in a customer workspace. |

## API platform

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:id/api\_collections](/en/oem/oem-api/api-platform#list-api-collections) | List **API collections** in a customer workspace. |
| POST | [/api/managed\_users/:id/api\_collections](/en/oem/oem-api/api-platform#create-api-collection) | Create **API collection** in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_collections/:api\_collection\_id](/en/oem/oem-api/api-platform#update-api-collection) | Update an existing **API collection** in a customer workspace. |
| DELETE | [/api/managed\_users/:id/api\_collections/:api\_collection\_id](/en/oem/oem-api/api-platform#delete-api-collection) | Delete an **API collection** along with its endpoints in a customer workspace. |
| GET | [/api/managed\_users/:id/api\_collections/:api\_collection\_id/openapi](/en/oem/oem-api/api-platform#get-api-collection-openapi-specification) | Get the OpenAPI specification for an **API collection** in a customer workspace. |
| GET | [/api/managed\_users/:id/api\_endpoints](/en/oem/oem-api/api-platform#list-api-endpoints) | List **API endpoints** in a collection. |
| POST | [/api/managed\_users/:id/api\_collections/:api\_collection\_id/api\_endpoints](/en/oem/oem-api/api-platform#create-api-endpoint) | Create an **API endpoint** within a collection in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_collections/:api\_collection\_id/api\_endpoints/:api\_endpoint\_id](/en/oem/oem-api/api-platform#update-api-endpoint) | Update an existing **API endpoint** in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_endpoints/:id/enable](/en/oem/oem-api/api-platform#enable-api-endpoint) | Enable an **API endpoint** in a collection. |
| PUT | [/api/managed\_users/:id/api\_endpoints/:id/disable](/en/oem/oem-api/api-platform#disable-api-endpoint) | Disable an **API endpoint** in a collection. |
| GET | [/api/managed\_users/:id/api\_endpoints/:id/openapi](/en/oem/oem-api/api-platform#get-api-endpoint-openapi-specification) | Get the OpenAPI specification for an **API endpoint** in a customer workspace. |
| GET | [/api/managed\_users/:id/api\_clients](/en/oem/oem-api/api-platform#list-api-clients) | List **API clients** in a customer workspace. We recommend that you migrate to the [List API clients (v2)](/en/oem/oem-api/api-platform#list-api-clients-v2) endpoint to prepare for future deprecation. |
| GET | [/api/v2/managed\_users/:id/api\_clients](/en/oem/oem-api/api-platform#list-api-clients-v2) | List all **API clients** in a customer workspace. Workato includes the `project_id` of the project to which the API client belongs in the response. |
| POST | [/api/managed\_users/:id/api\_clients](/en/oem/oem-api/api-platform#create-api-client) | Create **API client** in a customer workspace. We recommend that you migrate to the [Create API client (v2)](/en/oem/oem-api/api-platform#create-api-client-v2) endpoint to prepare for future deprecation. |
| POST | [/api/v2/managed\_users/:id/api\_clients](/en/oem/oem-api/api-platform#create-api-client-v2) | Create a new **API client** in a customer workspace within a project you specify. |
| GET | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id](/en/oem/oem-api/api-platform#get-api-client) | Retrieve details of an API client by ID in a customer workspace. |
| PUT | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id](/en/oem/oem-api/api-platform#update-api-client) | Update an existing API client within a project you specify in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id](/en/oem/oem-api/api-platform#delete-api-client) | Delete an existing API client in a customer workspace. |
| GET | [/api/managed\_users/:id/api\_access\_profiles](/en/oem/oem-api/api-platform#list-access-profiles) | List **access profiles** belonging to an API client in a customer workspace. We recommend that you migrate to the [List API keys](/en/oem/oem-api/api-platform#list-api-keys) endpoint to prepare for future deprecation. |
| GET | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys](/en/oem/oem-api/api-platform#list-api-keys) | List **API keys** for an API client in a customer workspace. |
| POST | [/api/managed\_users/:id/api\_access\_profiles](/en/oem/oem-api/api-platform#create-access-profile) | Create an **access profile** belonging to an API client in a customer workspace. We recommend that you migrate to the [Create API key](/en/oem/oem-api/api-platform#create-an-api-key) endpoint to prepare for future deprecation. |
| POST | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys](/en/oem/oem-api/api-platform#create-an-api-key) | Create an **API key** for an API client in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_access\_profiles](/en/oem/oem-api/api-platform#update-access-profile) | Update an **access profile** belonging to an API client in a customer workspace. We recommend that you migrate to the [Update API key](/en/oem/oem-api/api-platform#update-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id](/en/oem/oem-api/api-platform#update-api-key) | Update an **API key** for an API client in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_access\_profiles/:api\_access\_profile\_id/enable](/en/oem/oem-api/api-platform#enable-access-profile) | Enable an **access profile** belonging to an API client in a customer workspace. We recommend that you migrate to the [Enable API key](/en/oem/oem-api/api-platform#enable-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/enable](/en/oem/oem-api/api-platform#enable-api-key) | Enable an **API key** for an API client in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_access\_profiles](/en/oem/oem-api/api-platform#disable-access-profile) | Disable an **access profile** belonging to an API client in a customer workspace. We recommend that you migrate to the [Disable API key](/en/oem/oem-api/api-platform#disable-api-key) endpoint to prepare for future deprecation. |
| PUT | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/disable](/en/oem/oem-api/api-platform#disable-api-key) | Disable an **API key** for an API client in a customer workspace. |
| PUT | [/api/managed\_users/:id/api\_access\_profiles/:id/refresh\_secret](/en/oem/oem-api/api-platform#refresh-token-secret) | Refreshes an access profile **token or secret**. We recommend that you migrate to the [Refresh API key secret](/en/oem/oem-api/api-platform#refresh-api-key-secret) endpoint to prepare for future deprecation. |
| POST | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id/refresh\_secret](/en/oem/oem-api/api-platform#refresh-api-key-secret) | Refresh the authentication token or OAuth 2.0 client secret for an API key in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:id/api\_clients/:api\_client\_id/api\_keys/:api\_key\_id](/en/oem/oem-api/api-platform#delete-api-key) | Delete an existing API key in a customer workspace. |
| GET | [/api/v2/managed\_users/:id/api\_portals](/en/oem/oem-api/api-platform#list-api-portals) | List all API portals associated with API clients in a customer workspace. |
| GET | [/api/managed\_users/:id/cert\_bundles](/en/oem/oem-api/api-platform#list-certificate-bundles) | List all certificate bundles in a customer workspace. |
| POST | [/api/managed\_users/:id/cert\_bundles](/en/oem/oem-api/api-platform#create-a-certificate-bundle) | Create a new certificate bundle in a customer workspace. |
| PUT | [/api/managed\_users/:id/cert\_bundles/:id](/en/oem/oem-api/api-platform#update-a-certificate-bundle) | Update a certificate bundle in a customer workspace. |
| DELETE | [/api/managed\_users/:id/cert\_bundles/:id](/en/oem/oem-api/api-platform#delete-a-certificate-bundle) | Delete a certificate bundle in a customer workspace. |
| GET | [/api/managed\_users/:id/cert\_bundles/:id/download](/en/oem/oem-api/api-platform#download-a-certificate-bundle) | Download the certificate bundle PEM file in a customer workspace. |

## Collaborator groups

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/user\_groups](/en/oem/oem-api/collaborator-groups#list-groups) | List customer workspace collaborator groups. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id](/en/oem/oem-api/collaborator-groups#get-group) | Get customer workspace collaborator group details. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/user\_groups](/en/oem/oem-api/collaborator-groups#create-group) | Create a customer workspace collaborator group. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id](/en/oem/oem-api/collaborator-groups#update-group) | Update a customer workspace collaborator group. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id](/en/oem/oem-api/collaborator-groups#delete-group) | Delete a customer workspace collaborator group. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id/members](/en/oem/oem-api/collaborator-groups#list-members) | List collaborator group members in a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id/members](/en/oem/oem-api/collaborator-groups#add-members) | Add members to a customer workspace collaborator group. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id/members](/en/oem/oem-api/collaborator-groups#remove-members) | Remove members from a customer workspace collaborator group. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/user\_groups/:id/project\_grants](/en/oem/oem-api/collaborator-groups#list-collaborator-grants) | List a customer workspace collaborator group's project grants. |

## Connections

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/connections/:adapter\_name/input\_schema](/en/oem/oem-api/connections#get-connection-endpoint) | Returns input schema based on a connection's input. |
| GET | [/api/managed\_users/:managed\_user\_id/connections](/en/oem/oem-api/connections#list-connections) | Returns a list of connections in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/connections](/en/oem/oem-api/connections#create-a-connection) | Allows the Embedded vendor to add a shell connection in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/connections/:connection\_id](/en/oem/oem-api/connections#update-a-connection) | Updates a connection in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/connections/:connection\_id/disconnect](/en/oem/oem-api/connections#disconnect-a-connection) | Disconnects a connection in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/connections/:connection\_id](/en/oem/oem-api/connections#delete-a-connection) | Deletes a connection in a customer workspace. |

## Connectors

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/connectors/:connector\_name/input\_schema](/en/oem/oem-api/adapters#get-connector-endpoint) | Returns the base input schema. The schemas are static and don't take specific connection input into consideration. |
| GET | [/api/integrations](/en/oem/oem-api/adapters#list-connector-metadata) | Query connector metadata. |
| GET | [/api/integrations/all](/en/oem/oem-api/adapters#list-all-platform-connectors) | Returns a paginated list of all connectors and associated metadata in an Embedded partner's account. The response includes standard and custom connectors. |

## Custom connectors

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/custom\_connectors](/en/oem/oem-api/custom_connectors#search-custom-connectors) | Get custom connectors. |
| GET | [/api/custom\_connectors/:id](/en/oem/oem-api/custom_connectors#get-custom-connector-by-id) | Get custom connector by ID |
| POST | [/api/custom\_connectors/:id/oem\_share/:version](/en/oem/oem-api/custom_connectors#upsert-version-of-shared-connector) | Create or update a shared connector |
| POST | [api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/share](/en/oem/oem-api/custom_connectors#recipe-share) | Share a recipe containing a custom connector with Embedded partners. |
| DELETE | [/api/custom\_connectors/:id/suppress\_oem\_version](/en/oem/oem-api/custom_connectors#remove-shared-connector) | Remove a shared connector |

## Custom OAuth profiles

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users/:managed\_user\_id/custom\_oauth\_profiles/:id/assign](/en/oem/oem-api/custom-oauth-profiles#assign-custom-oauth-profile) | Assign a Custom OAuth profile to customer workspace |
| DELETE | [/api/managed\_users/:managed\_user\_id/custom\_oauth\_profiles/:id/unassign](/en/oem/oem-api/custom-oauth-profiles#unassign-custom-oauth-profile) | Unassigns a Custom OAuth profile to a customer workspace. |

## Customer managers

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/customer\_managers](/en/oem/oem-api/customer-managers#list-customer-managers) | List all customer managers. |
| PUT | [/api/customer\_managers/:id](/en/oem/oem-api/customer-managers#update-customer-manager) | Update a customer manager. |
| POST | [/api/customer\_managers](/en/oem/oem-api/customer-managers#create-customer-manager) | Create a new customer manager. |
| DELETE | [/api/customer\_managers/:id](/en/oem/oem-api/customer-managers#delete-customer-manager) | Delete a customer manager. |

## Customer workspace collaborators

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users/:id/member\_invitation](/en/oem/oem-api/team#invite-collaborator-to-managed-customer-account) | Invites a collaborator to a managed customer workspace. |

## Data retention

| Type | Resource | Description |
| --- | --- | --- |
| PUT | [/api/managed\_users/:managed\_user\_id/update\_data\_retention](/en/oem/oem-api/data-retention#update-data-retention) | Update a customer workspace's data retention period. |

## Data tables

### Table management APIs

Base URL: `https://app.workato.com`

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/data\_tables](/en/oem/oem-api/data-tables#list-data-tables) | List all data tables. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/data\_tables/:data\_table\_id](/en/oem/oem-api/data-tables#get-data-table-by-id) | Get data table by ID. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/data\_tables](/en/oem/oem-api/data-tables#create-data-table) | Creates a data table. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/data\_tables/:data\_table\_id](/en/oem/oem-api/data-tables#update-data-table) | Updates a data table. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/data\_tables/:data\_table\_id](/en/oem/oem-api/data-tables#delete-data-table) | Deletes a data table. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/data\_tables/:data\_table\_id/truncate](/en/oem/oem-api/data-tables#truncate-data-table) | Truncates a data table. |

### Record manipulation APIs

Base URL: `https://data-tables.workato.com`

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/query](/en/oem/oem-api/data-tables#query-records) | Queries records using filters you specify. |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records](/en/oem/oem-api/data-tables#create-record) | Creates a new record. |
| PUT | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/:record\_id](/en/oem/oem-api/data-tables#update-record) | Updates an existing record. |
| DELETE | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/:record\_id](/en/oem/oem-api/data-tables#delete-record) | Deletes a record you specify. |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/fields/:field\_id/file](/en/oem/oem-api/data-tables#generate-link-to-upload-file) | Generates a link to upload a file. |
| GET | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/:record\_id/fields/:field\_id/file](/en/oem/oem-api/data-tables#download-file-from-the-record) | Generates a link to download a file. |

### Record import APIs

Base URL: `https://data-tables.workato.com`, except [Upload file](/en/oem/oem-api/data-tables#upload-file), which posts to the signed URL returned by [Create file upload link](/en/oem/oem-api/data-tables#create-file-upload-link).

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import/file/upload\_link](/en/oem/oem-api/data-tables#create-file-upload-link) | Creates a link to upload a file. |
| POST | [/sharing/files](/en/oem/oem-api/data-tables#upload-file) | Uploads the file to the signed link. |
| DELETE | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import/file](/en/oem/oem-api/data-tables#delete-uploaded-file) | Deletes the uploaded file. |
| GET | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import/file](/en/oem/oem-api/data-tables#describe-uploaded-file) | Describes the uploaded file. |
| POST | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import/start](/en/oem/oem-api/data-tables#start-import) | Starts importing records from the uploaded file. |
| DELETE | [/api/v1/managed\_users/:managed\_user\_id/tables/:data\_table\_id/records/import](/en/oem/oem-api/data-tables#dismiss-import) | Dismisses or cancels the import. |

## Dynamic field mapping

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id /recipes/:recipe\_id/field\_map\_introspections](/en/oem/oem-api/dynamic-field-mapping#list-all-field-map-introspections-in-a-recipe) | List all field map introspections in a specific recipe. |
| GET | [/api/v2/managed\_users/:managed\_user\_id /recipes/:recipe\_id/field\_map\_introspections/:id](/en/oem/oem-api/dynamic-field-mapping#list-field-map-introspections-for-a-specific-field-map-schema) | List the field map introspections for a specific field map schema. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id /recipes/:recipe\_id/field\_map\_introspections/:id](/en/oem/oem-api/dynamic-field-mapping#update-field-map-introspections) | Update field mapping for a specific field map schema. |
| POST | [/api/v2/managed\_users/:managed\_user\_id /recipes/:recipe\_id/field\_map\_introspections/:id /refresh\_schema](/en/oem/oem-api/dynamic-field-mapping#refresh-field-map-schema) | Refresh a recipe’s schema to update field map introspections. |
| POST | [/api/v2/managed\_users/:managed\_user\_id /recipes/:recipe\_id/field\_map\_introspections/:id/pick\_list](/en/oem/oem-api/dynamic-field-mapping#retrieve-picklist-values-for-field-map-introspections) | Retrieve picklist values for specific fields within a field map introspection of a recipe. |

## Environment management

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:id/activity\_logs](/en/oem/oem-api/environment-management#get-audit-log) | Retrieves activity audit log records in a customer workspace. |
| GET | [/api/v2/managed\_users/:id/tags](/en/oem/oem-api/environment-management#list-tags) | Retrieves a list of tags in a customer workspace. |
| POST | [/api/v2/managed\_users/:id/tags](/en/oem/oem-api/environment-management#create-a-tag) | Creates a tag in a customer workspace. |
| PUT | [/api/v2/managed\_users/:id/tags/:handle](/en/oem/oem-api/environment-management#update-a-tag) | Updates a tag in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:id/tags/:handle](/en/oem/oem-api/environment-management#delete-a-tag) | Deletes a tag in a customer workspace. |

## Environment properties

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/properties](/en/oem/oem-api/account-properties#list-properties-by-prefix) | Returns a list of environment properties belonging to a customer workspace that matches a prefix. |
| POST | [/api/managed\_users/:managed\_user\_id/properties](/en/oem/oem-api/account-properties#upsert-property) | Upserts environment properties to a customer workspace. |

## Environment roles

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles](/en/oem/oem-api/environment-roles#list-env-roles) | List environment roles in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles/:id](/en/oem/oem-api/environment-roles#get-env-role) | Get an environment role from a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles](/en/oem/oem-api/environment-roles#create-env-role) | Create an environment role in a customer workspace. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles/:id](/en/oem/oem-api/environment-roles#update-env-role) | Update an environment role in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/environment\_roles/:id](/en/oem/oem-api/environment-roles#delete-env-role) | Delete an environment role in a customer workspace. |

## Environments

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users/:id/environments](/en/oem/oem-api/managed-users#provision-environments) | Provision Environments for an existing customer. Any existing assets in the customer workspace are placed in the **Development** environment after provisioning. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/environments](/en/oem/oem-api/managed-users#provision-environments-v2) | Provision Environments V2 for an existing customer. Any existing assets in the customer workspace are placed in the **Production** environment after provisioning. |
| GET | [/api/v2/managed\_users/environments\_provision\_tasks/:id](/en/oem/oem-api/managed-users#get-status-of-environment-provisioning) | Get the status of asynchronous environment provisioning. |

## Event streams

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/event\_streams/topics](/en/oem/oem-api/event-streams#list-topics) | List topics in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/event\_streams/topics](/en/oem/oem-api/event-streams#create-a-topic) | Create a topic in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/event\_streams/topics/:topic\_id](/en/oem/oem-api/event-streams#get-topic-by-id) | Get a topic by ID in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/event\_streams/topics/:topic\_id](/en/oem/oem-api/event-streams#update-a-topic) | Update a topic in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/event\_streams/topics/:topic\_id/purge](/en/oem/oem-api/event-streams#purge-a-topic) | Purge a topic in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/event\_streams/topics/:topic\_id](/en/oem/oem-api/event-streams#delete-a-topic) | Delete a topic in a customer workspace. |

## Folders

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/folders](/en/oem/oem-api/folders#list-folders) | List folders in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/folders](/en/oem/oem-api/folders#create-folder) | Create a folder in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/folders/:folder\_id](/en/oem/oem-api/folders#update-folder) | Update a folder in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/folders/:folder\_id](/en/oem/oem-api/folders#delete-folder) | Delete a folder in a customer workspace. |

## Jobs

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:id/recipes/:recipe\_id/jobs](/en/oem/oem-api/jobs#list-jobs) | List jobs for a recipe. |
| GET | [/api/managed\_users/:id/recipes/:recipe\_id/jobs/:job\_id](/en/oem/oem-api/jobs#get-job-details) | Get job details. |
| POST | [/api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/repeat\_jobs](/en/oem/oem-api/jobs#repeat-jobs) | Repeats jobs you specify in a customer workspace. |

## JWT direct link configurations

| Type | Resource | Description |
| --- | --- | --- |
| PUT | [/api/account/signature\_verification\_key](/en/oem/oem-api/jwt-direct-link-configurations) | Update JWT signature verification key. |

## Legacy roles

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:id/roles](/en/oem/oem-api/roles#list-custom-roles) | List custom roles in a customer workspace. |
| POST | [/api/managed\_users/:id/roles/:role\_id/copy](/en/oem/oem-api/roles#copy-a-custom-role) | Makes a copy of a custom role. |

## Lookup tables

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/lookup\_tables](/en/oem/oem-api/lookup-tables#list-lookup-tables) | List tables. |
| GET | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/lookup](/en/oem/oem-api/lookup-tables#lookup-row) | Look up rows. |
| GET | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows](/en/oem/oem-api/lookup-tables#list-rows) | List rows. |
| GET | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows/:row\_id](/en/oem/oem-api/lookup-tables#get-row) | List rows in a lookup table. |
| POST | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows](/en/oem/oem-api/lookup-tables#add-row) | Add a row to a lookup table. |
| POST | [/api/managed\_users/:managed\_user\_id/lookup\_tables](/en/oem/oem-api/lookup-tables#lut-create) | Create a new lookup table. |
| POST | [/api/managed\_users/:managed\_user\_id/lookup\_tables/batch\_delete](/en/oem/oem-api/lookup-tables#lut-delete) | Delete lookup tables in batch. |
| PUT | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows/:row\_id](/en/oem/oem-api/lookup-tables#update-row) | Update a row in a lookup table. |
| DELETE | [/api/managed\_users/:managed\_user\_id/lookup\_tables/:lookup\_table\_id/rows/:row\_id](/en/oem/oem-api/lookup-tables#delete-row) | Delete a row in a lookup table. |

## Manage customers

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users](/en/oem/oem-api/managed-users#create-customer-account) | Create a customer. |
| PUT | [/api/managed\_users/:id](/en/oem/oem-api/managed-users#update-customer-account) | Update a customer. |
| DELETE | [/api/managed\_users/:id](/en/oem/oem-api/managed-users#delete-customer-account) | Delete a customer. |
| GET | [/api/managed\_users/:id](/en/oem/oem-api/managed-users#get-customer-account) | Get a customer. |
| GET | [/api/managed\_users](/en/oem/oem-api/managed-users#get-list-of-customer-accounts) | List all customers. |
| GET | [/api/managed\_users/:id/members](/en/oem/oem-api/managed-users#get-list-of-customer-account-members) | Get a list of collaborators in a customer workspace. |
| GET | [/api/managed\_users/:id/members/:member\_id](/en/oem/oem-api/managed-users#get-customer-account-member) | Get customer workspace collaborator details. |
| POST | [/api/managed\_users/:id/members](/en/oem/oem-api/managed-users#add-member-to-customer-account) | Add collaborator to customer workspace. |
| PUT | [/api/managed\_users/:id/members/:member\_id](/en/oem/oem-api/managed-users#update-customer-account-member) | Update a customer workspace collaborator. |
| DELETE | [/api/managed\_users/:id/members/:member\_id](/en/oem/oem-api/managed-users#remove-member-from-customer-account) | Remove collaborator from customer workspace. |
| GET | [/api/managed\_users/:id/members/:member\_id/project\_grants](/en/oem/oem-api/managed-users#list-project-grants) | List a customer workspace collaborator's project grants. |
| GET | [/api/managed\_users/:id/connections](/en/oem/oem-api/managed-users#list-customer-connections) | List connections in a customer workspace. |
| GET | [/api/managed\_users/:id/members/:member\_id/privileges](/en/oem/oem-api/managed-users#get-list-of-customer-privileges) | Get privileges from a customer workspace collaborator. |
| GET | [/api/managed\_users/:managed\_user\_id/members/:id/projects\_privileges](/en/oem/oem-api/managed-users#get-project-privileges) | Get projects privileges from a customer workspace collaborator. |
| POST | [/api/v2/managed\_users/statistics/usage](/en/oem/oem-api/managed-users#get-usage-v2) | Retrieve usage metrics for customer workspaces with enhanced data granularity. |
| POST | [/api/v2/managed\_users/statistics/connection\_usage](/en/oem/oem-api/managed-users#get-connection-based-usage) | Retrieve connection-based usage metrics for specified customer workspaces. |
| GET | [/api/managed\_users/usage](/en/oem/oem-api/managed-users#get-monthly-usage) | Get task usage of all customers by month. |
| POST | [/api/managed\_users/:id/environments](/en/oem/oem-api/managed-users#provision-environments) | Provision Environments for an existing customer. |
| GET | [/api/v2/managed\_users/customer\_categories](/en/oem/oem-api/managed-users#get-list-of-customer-categories) | List customer categories in an Embedded partner's workspace. |
| POST | [/api/v2/managed\_users/customer\_categories](/en/oem/oem-api/managed-users#create-a-customer-category) | Create a customer category. |
| PUT | [/api/v2/managed\_users/customer\_categories/:id](/en/oem/oem-api/managed-users#update-a-customer-category) | Update a customer category. |
| DELETE | [/api/v2/managed\_users/customer\_categories/:id](/en/oem/oem-api/managed-users#delete-a-customer-category) | Delete a customer category. |
| POST | [/api/v2/managed\_users/customer\_categories/:id/assign](/en/oem/oem-api/managed-users#batch-assign-a-customer-category-to-workspaces) | Batch assign a customer category to workspaces. |
| POST | [/api/v2/managed\_users/customer\_categories/:id/unassign](/en/oem/oem-api/managed-users#batch-unassign-a-customer-category-from-workspaces) | Batch unassign a customer category from workspaces. |

## MCP servers

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers](/en/oem/oem-api/mcp-servers#list-mcp-servers-in-a-customer-workspace) | List MCP servers in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers](/en/oem/oem-api/mcp-servers#create-an-mcp-server-in-a-customer-workspace) | Create an MCP server in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle](/en/oem/oem-api/mcp-servers#get-mcp-server-details-in-a-customer-workspace) | Retrieve MCP server details in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle](/en/oem/oem-api/mcp-servers#update-an-mcp-server-in-a-customer-workspace) | Update an MCP server in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id</br/>mcp\_servers/:handle](/en/oem/oem-api/mcp-servers#delete-an-mcp-server-in-a-customer-workspace) | Delete an MCP server in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/token\_renew](/en/oem/oem-api/mcp-servers#renew-mcp-server-authentication-token-in-a-customer-workspace) | Renew an MCP server authentication token in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tokens](/en/oem/oem-api/mcp-servers#create-a-hashed-token-in-a-customer-workspace) | Create a hashed token in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tokens/:id](/en/oem/oem-api/mcp-servers#delete-a-hashed-token-in-a-customer-workspace) | Delete a hashed token in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tokens/:id/refresh](/en/oem/oem-api/mcp-servers#refresh-a-hashed-token-in-a-customer-workspace) | Refresh a hashed token in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/assign\_tools](/en/oem/oem-api/mcp-servers#assign-tools-to-an-mcp-server-in-a-customer-workspace) | Assign tools to an MCP server in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/assign\_user\_groups](/en/oem/oem-api/mcp-servers#assign-user-groups-to-an-mcp-server-in-a-customer-workspace) | Assign user groups to an MCP server in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/remove\_user\_groups](/en/oem/oem-api/mcp-servers#remove-user-groups-from-an-mcp-server-in-a-customer-workspace) | Remove user groups from an MCP server in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:handle/update\_folder](/en/oem/oem-api/mcp-servers#move-mcp-server-to-a-different-folder-in-a-customer-workspace) | Move an MCP server to a different folder in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/server\_policies](/en/oem/oem-api/mcp-servers#get-server-policy-configuration-in-a-customer-workspace) | Retrieve the server policy configuration in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/server\_policies](/en/oem/oem-api/mcp-servers#update-server-policy-configuration-in-a-customer-workspace) | Update the server policy configuration in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tools](/en/oem/oem-api/mcp-servers#list-tools-for-an-mcp-server-in-a-customer-workspace) | List tools for an MCP server in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tools/:id](/en/oem/oem-api/mcp-servers#update-tool-description-in-a-customer-workspace) | Update the tool description in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/tools/:id](/en/oem/oem-api/mcp-servers#delete-a-tool-in-a-customer-workspace) | Delete a tool in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/user\_groups](/en/oem/oem-api/mcp-servers#list-identity-provider-user-groups-in-a-customer-workspace) | List identity provider user groups in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments](/en/oem/oem-api/mcp-servers#list-mcp-access-assignments-in-a-customer-workspace) | List MCP access assignments in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments](/en/oem/oem-api/mcp-servers#create-an-mcp-access-assignment-in-a-customer-workspace) | Create an MCP access assignment in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments/:id](/en/oem/oem-api/mcp-servers#get-an-mcp-access-assignment-in-a-customer-workspace) | Retrieve an MCP access assignment in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments/:id](/en/oem/oem-api/mcp-servers#update-an-mcp-access-assignment-in-a-customer-workspace) | Update an MCP access assignment in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/mcp\_servers/:mcp\_server\_handle/access\_assignments/:id](/en/oem/oem-api/mcp-servers#delete-an-mcp-access-assignment-in-a-customer-workspace) | Delete an MCP access assignment in a customer workspace. |

## On-prem

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:id/on\_prem\_groups](/en/oem/oem-api/on-prem#list-on-prem-groups) | List on-prem groups in a customer workspace. |
| GET | [/api/v2/managed\_users/:id/on\_prem\_agents](/en/oem/oem-api/on-prem#list-on-prem-agents) | List on-prem agents in a customer workspace. |
| GET | [/api/v2/managed\_users/:id/on\_prem\_agents/:agent\_id](/en/oem/oem-api/on-prem#get-details-about-an-on-prem-agent) | Retrieve the details of a specific on-prem agent in a customer workspace using its ID. |

## Picklists

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users/:id/connections/:connection\_id/pick\_list](/en/oem/oem-api/picklists) | Obtains a list of picklist values for a specified connection in an Embedded customer workspace. |

## Project grants

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/project\_grants/:id](/en/oem/oem-api/project-grants#get-grant) | Get a customer workspace project grant. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/project\_grants/:id](/en/oem/oem-api/project-grants#update-grant) | Update a customer workspace project grant. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/project\_grants/:id](/en/oem/oem-api/project-grants#delete-grant) | Delete a customer workspace project grant. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/projects/:id/project\_grants](/en/oem/oem-api/project-grants#list-grants) | List grants from a specific project in a customer workspace. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/projects/:id/project\_grants](/en/oem/oem-api/project-grants#add-grants-to-project) | Add or update customer workspace project grants. |

## Project roles

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/v2/managed\_users/:managed\_user\_id/project\_roles](/en/oem/oem-api/project-roles#list-project-roles) | List project roles in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/project\_roles/:id](/en/oem/oem-api/project-roles#get-role) | Get a project role from a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/project\_roles](/en/oem/oem-api/project-roles#create-role) | Create a project role in a customer workspace. |
| PUT | [/api/v2/managed\_users/:managed\_user\_id/project\_roles/:id](/en/oem/oem-api/project-roles#update-role) | Update a project role in a customer workspace. |
| DELETE | [/api/v2/managed\_users/:managed\_user\_id/project\_roles/:id](/en/oem/oem-api/project-roles#delete-role) | Delete a project role from a customer workspace. |

## Projects

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/projects](/en/oem/oem-api/project-properties#list-projects) | List projects in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/folders](/en/oem/oem-api/project-properties#create-project) | Create a project in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/projects/:project\_id](/en/oem/oem-api/project-properties#update-project) | Update a project in a customer workspace. |
| DELETE | [/api/managed\_users/:managed\_user\_id/projects/:project\_id](/en/oem/oem-api/project-properties#delete-a-project) | Delete a project in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/properties](/en/oem/oem-api/project-properties#list-project-properties) | List project-level properties by prefix and project ID. |
| POST | [/api/managed\_users/:managed\_user\_id/properties](/en/oem/oem-api/project-properties#upsert-project-properties) | Upsert project-level properties. |
| GET | [/api/managed\_users/:managed\_user\_id/deployments](/en/oem/oem-api/project-properties#list-deployments) | Retrieve a list of deployments in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/deployments/:id](/en/oem/oem-api/project-properties#get-a-deployment) | Retrieve a single deployment in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/api/project\_builds/:id](/en/oem/oem-api/project-properties#get-a-downloaded-package) | Retrieve a downloaded package in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/projects/:id/build](/en/oem/oem-api/project-properties#build-a-project) | Build a project in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/project\_builds/:id/deploy](/en/oem/oem-api/project-properties#deploy-a-downloaded-package) | Deploy a downloaded package in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/projects/:project\_id/deploy](/en/oem/oem-api/project-properties#deploy-a-project) | Deploy a project in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/deployments/:id/eligible\_reviewers](/en/oem/oem-api/project-properties#list-eligible-reviewers-for-a-deployment) | Retrieve a list of eligible reviewers that can be assigned to review a deployment in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/deployments/:id/assign\_reviewers](/en/oem/oem-api/project-properties#assign-reviewers-to-a-deployment) | Assign reviewers to a deployment in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/deployments/:id/submit\_for\_review](/en/oem/oem-api/project-properties#submit-a-deployment-for-review) | Submit a deployment for review in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/deployments/:id/deploy](/en/oem/oem-api/project-properties#deploy-an-approved-deployment) | Deploy an approved deployment in a customer workspace. |

## Recipes

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:id/recipes](/en/oem/oem-api/recipes#list-recipes-in-a-customer-account) | List recipes belonging to a customer. |
| GET | [/api/managed\_users/:id/recipes/:recipe\_id](/en/oem/oem-api/recipes#get-recipe-in-a-customer-account) | Get details of a recipe belonging to a customer. |
| GET | [/api/managed\_users/:managed\_user\_id/recipes/job\_counts](/en/oem/oem-api/recipes#get-recipe-job-counts-in-a-customer-workspace) | Get job counts for one or more recipes belonging to a customer. |
| POST | [/api/managed\_users/:managed\_user\_id/recipes](/en/oem/oem-api/recipes#create-a-recipe) | Create a recipe in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/recipes/:id](/en/oem/oem-api/recipes#update-a-recipe) | Update a recipe in a customer workspace. |
| POST | [/api/managed\_users/:id/recipes/:recipe\_id/copy](/en/oem/oem-api/recipes#copy-recipe-in-a-customer-account) | Copy a recipe in a customer workspace. |
| DELETE | [/api/managed\_users/:id/recipes/:recipe\_id](/en/oem/oem-api/recipes#delete-recipe-in-a-customer-account) | Delete a recipe in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/start](/en/oem/oem-api/recipes#start-recipe-in-a-customer-account) | Start a recipe in a customer workspace. |
| PUT | [/api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/stop](/en/oem/oem-api/recipes#stop-recipe-in-a-customer-account) | Stop a recipe in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/reset\_trigger](/en/oem/oem-api/recipes#reset-recipe-trigger) | Reset the trigger for a recipe in a customer workspace. |
| POST | [/api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/poll\_now](/en/oem/oem-api/recipes#start-poll-now-recipe) | Start a poll-now recipe. |
| POST | [/api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/force\_run](/en/oem/oem-api/recipes#force-run-a-recipe) | Force a recipe to run on demand in a customer workspace. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/recipes/:recipe\_id/versions](/en/oem/oem-api/recipes#get-recipe-versions-in-a-customer-workspace) | Get versions of a recipe belonging to a customer. |
| GET | [/api/v2/managed\_users/:managed\_user\_id/recipes/:recipe\_id/versions/:id](/en/oem/oem-api/recipes#get-a-specific-recipe-version-in-a-customer-workspace) | Get details of a recipe version belonging to a customer. |
| PATCH/PUT | [/api/v2/managed\_users/:managed\_user\_id/recipes/:recipe\_id/versions/:id](/en/oem/oem-api/recipes#update-a-recipe-version-comment-in-a-customer-workspace) | Update a recipe version comment in a customer workspace. |

## Recipe lifecycle management

Looking for APIs to export packages? Refer to the [Workato API docs](/en/workato-api/recipe-lifecycle-management).

> **WHO CAN USE THESE ENDPOINTS?**
> 
> The endpoints in this guide are Embedded Partner APIs. Contact your Workato representative for more info.

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/managed\_users/:managed\_user\_id/export\_manifests/folder\_assets](/en/oem/oem-api/recipe-lifecycle-management#manifest-folder-assets) | View assets in a folder. |
| POST | [/api/managed\_users/:managed\_user\_id/export\_manifests](/en/oem/oem-api/recipe-lifecycle-management#manifest-create) | Create an export manifest. |
| PUT | [/api/managed\_users/:managed\_user\_id/export\_manifests/:id](/en/oem/oem-api/recipe-lifecycle-management#manifest-update) | Update an export manifest. |
| GET | [/api/managed\_users/:managed\_user\_id/export\_manifests/:id](/en/oem/oem-api/recipe-lifecycle-management#manifest-view) | View an export manifest. |
| DELETE | [/api/managed\_users/:managed\_user\_id/export\_manifests/:id](/en/oem/oem-api/recipe-lifecycle-management#manifest-delete) | Delete an export manifest. |
| POST | [/api/managed\_users/:managed\_user\_id/imports](/en/oem/oem-api/recipe-lifecycle-management#package-import) | Import a package into a folder located in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/recipes](/en/oem/oem-api/recipe-lifecycle-management#get-package-status) | Get status of an imported package. |
| POST | [/api/managed\_users/:managed\_user\_id/exports/:manifest\_id](/en/oem/oem-api/recipe-lifecycle-management#export-package) | Export package based on the manifest ID. Requires an Embedded workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/exports/:package\_id](/en/oem/oem-api/recipe-lifecycle-management#export-status-get) | Returns the status of a package export. Requires an Embedded workspace. |

## Role migration

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v2/managed\_users/:managed\_user\_id/roles\_migration/system\_roles](/en/oem/oem-api/role-migration#migrate-system-roles) | Migrate system roles from a customer workspace. |
| POST | [/api/v2/managed\_users/:managed\_user\_id/roles\_migration/custom\_role](/en/oem/oem-api/role-migration#migrate-a-custom-role) | Migrate a custom role from a customer workspace. |

## Tag assignments

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/v2/managed\_users/:id/tags\_assignments](/en/oem/oem-api/tag-assignments#manage-tag-assignments) | Apply or remove asset tags in a customer workspace. |

## Test Automation

| Type | Resource | Description |
| --- | --- | --- |
| POST | [/api/managed\_users/:managed\_user\_id/test\_cases/run\_requests](/en/oem/oem-api/test-automation#run-test-cases) | Run test cases in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/recipes/:recipe\_id/test\_cases](/en/oem/oem-api/test-automation#list-test-cases) | List test cases for a specific recipe in a customer workspace. |
| GET | [/api/managed\_users/:managed\_user\_id/test\_cases/run\_requests/:test\_id](/en/oem/oem-api/test-automation#run-a-test-case) | Get the current state of a test case run request in a customer workspace. |

---
