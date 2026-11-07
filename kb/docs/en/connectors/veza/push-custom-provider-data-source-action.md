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
