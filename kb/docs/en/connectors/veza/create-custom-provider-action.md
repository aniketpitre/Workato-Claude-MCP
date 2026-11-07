---
url: 'https://docs.workato.com/en/connectors/veza/create-custom-provider-action.md'
description: >-
  The Create a custom provider action allows you to create a custom provider
  using the custom application template programmatically. This is useful for
  integrating third-party applications or custom data sources into Veza's access
  management platform.
---

# Veza - Create a custom provider action

The **Create a custom provider** action allows you to create a custom provider using the custom application template programmatically. This is useful for integrating third-party applications or custom data sources into Veza's access management platform.

## Input

| Input field | Description |
| --- | --- |
| Name | Provide the name of the custom provider to be created. |
| Custom template | The custom template you plan to use. |
| Provisioning | Use the drop-down menu to select the boolean value. |
| Push type | Provide the integer value to determine how data is pushed in Veza. |
| Internal app name | Provide an internal system name for the custom provider. |
| Configuration json | Provide a JSON-encoded string containing the configuration details for the custom provider. |
| Data plane ID | Provide identifier of the data plane where you plan to host this provider. |
| Custom templates | Provide a list of custom template identifiers associated with this provider. |
| Extended properties | Describe if additional fields are required as extended properties. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier for the provider, automatically assigned by Veza. |
| External ID | External reference ID for mapping the provider to an external system or integration. |
| Name | Human-readable display name of the custom provider as it appears in the Veza console. |
| Custom template | The primary template identifier defining the structure and attributes of the custom provider. |
| Custom templates | List of additional template identifiers that can be associated with the provider to extend or override schema definitions. |
| Application types | Application categories supported by the provider. |
| IdP types | Supported Identity Provider types relevant for identity mappings. |
| File system types | Supported file system or storage service categories. |
| HRIS types | Supported Human Resource Information System integrations. |
| Principal types | Types of principals managed by the provider. |
| Schema definition JSON | JSON structure describing the schema of entities and relationships. |
| Provisioning | Indicates whether Veza can write changes back to the external system. |
| Internal app name | Internal system-level identifier for the provider. This is used for API references and automation. |
| Configuration JSON | Key-value configuration parameters required for the provider. |
| Data plane ID | Identifier of the Veza data plane where the provider operates. This identifier is important in multi-data-plane deployments. |
| Team ID | Identifier of the Veza team that owns or manages this provider. This ID is used for access control and scoping. |

---

---
url: >-
  https://docs.workato.com/en/connectors/veza/push-custom-provider-data-source-action.md
description: >-
  The Push a custom provider datasource action in Veza allows you to send access
  and authorization data from a custom application or system to Veza. This is
  essential for maintaining visibility and governance over permissions within a
  custom provider.
---

# Veza - Push a custom provider data source action

The **Push a custom provider datasource** action in Veza allows you to send access and authorization data from a custom application or system to Veza. This is essential for maintaining visibility and governance over permissions within a custom provider.

## Input

| Input field | Description |
| --- | --- |
| Custom provider | The unique identifier of the custom provider where you plan to push data. |
| Data source | The name of the data source within the provider. |
| Data type | Type of the data that needs to be pushed. The data type should be either JSON or CSV. |
| CSV Data | Indicates whether CSV data must be pushed to the data source. |
| JSON Data | Indicates whether JSON data must be pushed to the data source. |
| Name | Human-readable name of the data source you plan to push. |
| Type | Type or category of the data source. |

## Output

| Output field | Description |
| --- | --- |
| Warnings | An array of objects that includes the field Message. |

---

---
url: >-
  https://docs.workato.com/en/connectors/veza/register-new-data-source-for-custom-provider-action.md
description: >-
  The Register a new data source for a custom provider action allows you to
  register a new data source under an existing custom provider in Veza. A data
  source represents a logical grouping of access data, such as user roles,
  permissions, and resources for a specific system.
---

# Veza - Register a new data source for a custom provider action

The **Register a new data source for a custom provider** action allows you to register a new data source under an existing custom provider in Veza. A data source represents a logical grouping of access data, such as user roles, permissions, and resources for a specific system.

## Input

| Input field | Description |
| --- | --- |
| Custom Provider | Select the unique identifier of the custom provider where you plan to register the data source. |
| Name of the data source | Provide the name of the new data source. |

## Output

| Output field | Description |
| --- | --- |
| ID | ID of the registered data source. |
| Name | The name of the new data source. |

---
