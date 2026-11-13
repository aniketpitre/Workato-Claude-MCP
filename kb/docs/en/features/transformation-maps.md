---
url: 'https://docs.workato.com/en/features/transformation-maps.md'
description: >-
  Use transformation maps to visually map input fields to an output schema and
  transform values with formulas.
---

# Transformation maps

Transformation maps are project assets that centralize the logic for shaping and mapping data between systems, work otherwise split across recipe steps, formula mode, and custom code. You can test the mapping end-to-end directly in the editor before you save it, and reuse the same logic across multiple recipes.

Use [Workato Expression Language (WEL)](/en/wel) [formula nodes](/en/features/transformation-maps/create-map#formula-transformations) to transform data, or map an input directly to an output to pass the data unchanged.

![Transformation map overview](/assets/map-overview.CSrDKuVI.png)_Transformation map overview_

> **FEATURE AVAILABILITY**
> 
> The Transformation maps feature is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Use a transformation map in a recipe

Use the [Mapper by Workato](/en/connectors/mapper) connector to apply a saved transformation map in a recipe. Use the connector's **Map using** input field to select one of the following options to determine where the schema comes from:

- **Common data model > Object schema**: Select a [common data model](/en/features/common-data-model) object schema. This is the only option if the **Map using** field isn't visible in your workspace.
- **Transformation map > Transformation map**: Select a saved [transformation map](/en/features/transformation-maps).

Workato generates additional input fields based on your selected schema. Use these fields to populate the schema with data.

## Limitations

Transformation maps currently have the following limitations:

- Formula positions don't save. Workato places formulas automatically each time you open the map.
- Job history errors don't link to the specific transformation map version that produced them.

Transformation maps also enforce the following quotas per map:

| Description | Quota |
| --- | --- |
| Maximum number of input schema fields | 500 |
| Maximum number of output schema fields | 500 |
| Maximum number of formula node outputs | 200 |

---
