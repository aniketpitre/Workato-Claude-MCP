---
url: >-
  https://docs.workato.com/en/connectors/dynamics-crm/actions/get-object-schema.md
description: >-
  The Get object schema action in the Microsoft Dynamics 365 connector retrieves
  an object's name and field schema to replicate to a database.
---

# Microsoft Dynamics 365 - Get object schema action

This action retrieves the name and schema of a specific object in Microsoft Dynamics 365. Use this action to retrieve a schema and replicate it to a database or data warehouse.

* * *

## How It Works

- [Basics](#basics)
- [Data typing](#data-typing)

### Basics

When the action runs, Workato requests the schema of the object you specify from the Microsoft Dynamics 365 API.

If the request is successful, the Microsoft Dynamics 365 API will respond with the object's `name`, `label`, and a list of `fields` that it contains.

For example: An `account` object contains `name`, `emailaddress`, and `alternate_address` fields. Click below to view the JSON response for this example object.

See example JSON response

```json
{
   "name":"account",
   "label":"Account",
   "fields":[
      {
         "name":"name",
         "label":"Name",
         "length":100,
         "scale":0,
         "precision":0,
         "original_type":"#Microsoft.Dynamics.365.StringAttributeMetadata",
         "mapped_type":"STRING",
         "custom":false
      },
      {
         "name":"emailaddress",
         "label":"Email address ",
         "length":100,
         "scale":0,
         "precision":0,
         "original_type":"#Microsoft.Dynamics.365.StringAttributeMetadata",
         "mapped_type":"STRING",
         "custom":false
      },
      {
         "name":"alternate_address",
         "label":"Alternate Address",
         "length":0,
         "precision":0,
         "scale":0,
         "original_type":"#Microsoft.Dynamics.365.PicklistAttributeMetadata",
         "mapped_type":"STRING",
         "custom":true,
         "fields":[
            {
               "name":"label",
               "label":"Label",
               "length":0,
               "scale":0,
               "precision":0,
               "original_type":null,
               "mapped_type":"STRING",
               "custom":false
            },
            {
               "name":"value",
               "label":"Internal value",
               "length":0,
               "scale":0,
               "precision":0,
               "original_type":null,
               "mapped_type":"INTEGER",
               "custom":false
            }
         ]
      }
   ]
}
```

### Data Typing

Every `field` object also contains `original_type` and `mapped_type` properties. These properties indicate the data type of the field in Microsoft Dynamics 365 and the data type it maps to in Workato. These properties determine how data is typed when loaded into a database.

For example:

```json
{
   "name":"budget_amount",
   "label":"Budget Amount",
   "length":1000,
   "scale":0,
   "precision":10000,
   "original_type":"#Microsoft.Dynamics.365.MoneyAttributeMetadata",
   "mapped_type":"DECIMAL",
   "custom":false
}
```

In this example, the `budget_amount` field is typed as `MoneyAttributeMetadata` in Microsoft Dynamics 365 and maps to `DECIMAL` in Workato.

Refer to the [Data type mapping section](#data-type-mapping) for more info.

* * *

## Input

| Field | Description |
| --- | --- |
| **Object** | The object to retrieve from Microsoft Dynamics 365. You can select from a list of available objects or enter the name of an object. **If entering the name of an object**, you may need to retrieve it from your app first.
> View steps for app In your Dynamics 365 app, navigate to **Settings (gear icon) > Advanced Settings**.; In the **Settings** menu, click **Customization > Customizations**.; Next, select **Customize the System**, then **Entities**.; In the navigation on the left side of the page, locate and select the entity.; In the **General** tab for the entity, locate the **Name** field.

 |

* * *

## Output

The **Output** of this recipe will be an object detailing the Microsoft Dynamics 365 object's schema. This object contains a list of **Field** objects that describe the object's fields.

- [Object schema](#object)
- [Fields schema](#fields)

To view an example JSON object, refer to the [Basics](#basics) section.

### Object

| Field | Description |
| --- | --- |
| **Name** | The name of the object. For example: `account` |
| **Label** | The display label of the object. For example: `Account` |
| **Custom** | If `true`, the object was created by a user. |
| **Fields** | A list of fields the object contains. Refer to the [Field object](#field-object) section to view the schema fields have. |

### Fields

Every field in the retrieved [object](#object) will contain the following fields:

| Field | Description |
| --- | --- |
| **Name** | The name of the field. For example: `emailaddress` |
| **Label** | The display label of the field. For example: `Email Address` |
| **Length** | The maximum number of characters the field can hold. This value will be `0` for `BOOLEAN` fields or fields without a limit. |
| **Scale** | The maximum number of digits to the right of the decimal point. This value will be `0` for non-numeric fields. |
| **Precision** | The maximum number of digits that the column can store, including numbers to the left and right of the decimal point. This value will be `0` for non-numeric fields. |
| **Original type** | The data type of the field in Microsoft Dynamics 365. For example: `StringAttributeMetadata` |
| **Mapped type** | The data type that `original_type` maps to in Workato. This type is used to determine the column's data type when it's loaded into a database. [Learn more](#data-type-mapping). |
| **Custom** | If `true`, this field was created by a user. |
| **Fields** | **Applicable only to fields with an `Original type` value of `BooleanAttributeMetadata`, `PicklistAttributeMetadata`, `StatusAttributeMetadata`, or `StateAttributeMetadata`.** When present, the `fields` property will contain two nested fields: `label` and `value`. These fields have the same schema as a top-level field. For example:
{
   \[...\],
   "fields":\[
      {
         "name":"label",
         "label":"Label",
         "length":0,
         "scale":0,
         "precision":0,
         "original\_type":null,
         "mapped\_type":"STRING",
         "custom":false
      },
      {
         "name":"value",
         "label":"Internal value",
         "length":0,
         "scale":0,
         "precision":0,
         "original\_type":null,
         "mapped\_type":"INTEGER",
         "custom":false
      }
   \]
}

**Note**: The `mapped_type` value for a nested field is dependent on the `name` of the nested field: `label` - This value will be `STRING`; `value` - If the parent field has an `Original type` value of `BooleanAttributeMetadata`, this value will be `BOOLEAN`. Otherwise, this value will be `INTEGER`. |

* * *

## Reference

- [Data type mapping](#data-type-mapping)

### Data Type Mapping

The following table details how Microsoft Dynamics 365 data types map to Workato data types.

The columns in this table are as follows:

- **Microsoft Dynamics 365 Data Type** - The field's `original_type` value
- **Workato Mapping Type** - The field's `mapped_type` value

For example: A field with a `original_type: BigIntAttributeMetadata` value maps to a `mapped_type: BIGINT` value.

| Microsoft Dynamics 365 Data Type | Workato Mapping Type |
| --- | --- |
| BigIntAttributeMetadata | BIGINT |
| BooleanAttributeMetadata | STRING |
| DateTimeAttributeMetadata | DATETIME\_TZ |
| DecimalAttributeMetadata | DECIMAL |
| DoubleAttributeMetadata | FLOAT |
| EntityNameAttributeMetadata | STRING |
| FileAttributeMetadata | STRING |
| ImageAttributeMetadata | STRING |
| IntegerAttributeMetadata | INTEGER |
| LookupAttributeMetadata | STRING |
| MemoAttributeMetadaMemoAttributeMetadatata | STRING |
| MoneyAttributeMetadata | DECIMAL |
| MultiSelectPicklistAttributeMetadata | STRING |
| PicklistAttributeMetadata | STRING |
| StateAttributeMetadata | STRING |
| StatusAttributeMetadata | STRING |
| StringAttributeMetadata | STRING |
| UniqueIdentifierAttributeMetadata | STRING |
