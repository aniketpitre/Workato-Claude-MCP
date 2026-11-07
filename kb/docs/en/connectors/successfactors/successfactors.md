---
url: 'https://docs.workato.com/en/connectors/successfactors/successfactors.md'
description: >-
  Set up and connect SAP SuccessFactors in Workato, including creating an
  integration system user and registering an OAuth 2.0 client application.
---

# SAP SuccessFactors

[Video](https://www.youtube.com/embed/0chBqyOWpZo)

[SAP SuccessFactors](https://www.sap.com/products/hcm.html) provides cloud-based human capital management software. The SAP SuccessFactors connector enables you to create integrations with the following products:

- SuccessFactors Employee Central Core HR
- SuccessFactors Performance & Goals
- SuccessFactors Recruiting
- SuccessFactors Onboarding
- SuccessFactors Learning
- SuccessFactors JAM Social Collaboration
- SuccessFactors Succession and Development
- SuccessFactors Workforce Planning
- SuccessFactors Workforce Analytics
- SuccessFactors Compensation

The SAP SuccessFactors connector has successfully passed the Application Readiness Check (ARC) required by SAP PartnerEdge. Read the [SAP Application Readiness Check Guide](https://www.sap.com/documents/2018/05/e282ab65-077d-0010-87a3-c30de2ffd8ff.html) to learn more about the ARC.

## API version

The SAP SuccessFactors connector supports both [OData API v2](https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v2/about-sap-successfactors-odata-apis-v2) and [OData API v4](https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v4/about-odata-api-reference-guide-v4).

## Prerequisites

To connect to SAP SuccessFactors, you must complete the following prerequisite steps:

1. [Create an integration system user (ISU)](#create-isu)
2. [Register an OAuth 2.0 client application](#register-oauth-app)

### Create an integration system user

Complete the following steps to create an integration system user (ISU) in SAP SuccessFactors:

1. Sign in to your SAP SuccessFactors instance.
   
2. Configure an integration service user (ISU). This is a unique user, whose sole purpose is connecting to Workato.
   
3. Assign the ISU a role that includes the following permissions:
   
   - **General User Permission**
     
     - User login – _describe_
     - SFAPI user login – _describe_
     - Login method (password) – _describe_
   - **Manage System Properties**
     
     - Picklist management – _describe_
     - Picklists mappings set up – _describe_
   - **Employee Central API**
     
     - Employee central foundation SOAP API – _describe_
     - Employee central HRIS SOAP API – _describe_
     - Employee central foundation OData API (read-only) – _describe_
     - Employee central HRIS OData API (read-only) – _describe_
     - Employee central foundation OData API (editable) – _describe_
     - Employee central HRIS OData API (editable) – _describe_
   - **Manage Integration Tools**
     
     - Allow admin to access OData API through basic authentication – _describe_
   - **Recruiting Permissions**
     
     - OData API job requisition create – _describe_
   - **Manage User**
     
     - User account OData entity – _describe_

Refer to [Role-based permissions in SAP](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/1411316651974a7dae4b09a104172dc2.html) for more information on configuring permission roles and groups.

### Register an OAuth 2.0 client application

Complete the following steps to register Workato as an OAuth 2.0 client application:

1. Go to **Admin Center > API Center > OAuth Configuration for OData**. You can also access the tool by searching **Manage OAuth2 Client Applications** in the action search.
   
2. Click **Register Client Application**.
   
3. Provide a callback URL in the **Application URL** field. Use one of the following URLs:
   
   - `https://www.workato.com/oauth/callback`
   - `https://app.workato.com/oauth/callback`
4. Select **Bind to user**, then enter the ISU user ID.
   
5. Click **Generate X.509 Certificate** and complete the required fields.
   
6. Click **Generate**, then download and save the certificate.
   
7. Click **Register** to save your registration. Save the **API Key**, which serves as the client ID.
   

Refer to [Registering Your OAuth 2.0 Client Application](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/6b3c741483de47b290d075d798163bc1.html) for more information.

> **OAUTH 2.0**
> 
> These steps are required if you plan to connect to SAP SuccessFactors using [OAuth 2.0 authentication](#oauth-2).

## How to connect to SAP SuccessFactors

The SAP SuccessFactors connector supports the following authentication methods:

- [OAuth 2.0](#oauth-2) (recommended)
- [Basic](#basic)

### OAuth 2.0 authentication

Complete the following steps to connect to SAP SuccessFactors using OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `SAP SuccessFactors` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to SAP SuccessFactors](/assets/oauth-2.DUXE_jI2.png)_Connect to SAP SuccessFactors_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Specify whether to use a cloud or on-prem connection in the **Connection type** drop-down menu.
   
6. Select **OAuth 2.0** from the **Authentication type** drop-down menu.
   
7. Select an API version to use from the **OData version** drop-down menu. Options include **OData V2** and **OData V4**. Defaults to **OData V2** if left blank.
   
   > **ODATA V4 REQUIRES OAUTH 2.0**
   > 
   > **OData V4** is only available when you select **OAuth 2.0** as the authentication type.
   
8. Enter the company ID in the **Company ID** field. You can find the company ID by selecting **Show version information** under the profile drop-down menu, or by looking for the term `company=` in the URL.
   
9. Enter the SAP SuccessFactors user ID in the **User ID** field.
   
10. Enter the [OAuth client ID](#register-oauth-app) in the **Client ID** field.
    
11. Enter the X.509 private key used to sign SAML assertion in the **Private key** field. It can be the private key of a self-signed X.509 certificate or the private key of an X.509 certificate generated by SAP SuccessFactors. The private key is a base64-encoded string enclosed between `-----BEGIN ENCRYPTED PRIVATE KEY-----` and `----- END ENCRYPTED PRIVATE KEY-----`. Enter only the enclosed string without the beginning and ending lines to prevent errors.
    
12. Select your corresponding SAP SuccessFactors environment from the **Environment** drop-down menu.
    
    Alternatively, you can click the **Environment** field's toggle and provide the endpoint URL for accessing the OData API. For example, `https://api4.successfactors.com`.
    
13. Optional. Fill in the **Application interface key** field. Defaults to Workato's application interface key when left blank.
    
14. Optional. Select the API server standard UTC timezone in the **API server timezone** field. For example, `-0500` for DC8 Production environment. Alternatively, you can click this field's toggle to enter the timezone manually.
    
    Refer to the SAP documentation for more information on [tenant and server time zones](https://help.sap.com/docs/SAP_SUCCESSFACTORS_RELEASE_INFORMATION/8e0d540f96474717bbf18df51e54e522/d5e86fa8bb564058820592217d3a21d4.html?locale=en-US).
    
15. Click **Connect**.
    

### Basic authentication

Complete the following steps to connect to SAP SuccessFactors using basic authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `SAP SuccessFactors` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to SAP SuccessFactors](/assets/basic-auth.CkN-WEFB.png)_Connect to SAP SuccessFactors_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Specify whether this connection is a cloud or on-prem connection in the **Connection type** field.
   
6. Select **Basic** from the **Authentication type** drop-down menu.
   
7. Enter the company ID in the **Company ID** field. You can find it in **Show version information** under the profile drop-down menu or by looking for the term `company=` in the URL.
   
8. Enter the SAP SuccessFactors user ID in the **User ID** field.
   
9. Enter the password for your SAP SuccessFactors account in the **Password** field.
   
10. Select your corresponding SAP SuccessFactors environment from the **Environment** drop-down menu.
    
    Alternatively, you can click the **Environment** field's toggle and provide the endpoint URL for accessing the OData API. For example, `https://api4.successfactors.com`.
    
11. Optional. Fill in the **Application interface key** field. Defaults to Workato's application interface key when left blank.
    
12. Optional. Select the API server standard UTC timezone in the **API server timezone** field. For example, `-0500` for DC8 Production environment. Alternatively, you can click this field's toggle to enter the timezone manually.
    
    Refer to the SAP documentation for more information on [tenant and server time zones](https://help.sap.com/docs/SAP_SUCCESSFACTORS_RELEASE_INFORMATION/8e0d540f96474717bbf18df51e54e522/d5e86fa8bb564058820592217d3a21d4.html?locale=en-US).
    
13. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-nav-fields.md
description: >-
  Use navigation fields in the SAP SuccessFactors connector to retrieve related
  records or associate records when you create or update them.
---

# SAP SuccessFactors - Use navigation fields

Navigation fields are a powerful way to either retrieve records related to the one you're retrieving, or create associations between records when you create or update them. For example, use navigation fields in the SuccessFactors connector to retrieve records related to a user, such as their manager or biographical information. You can also use navigation fields when creating or updating a user to associate them with a new manager or set of biographical information. The following steps describe how to configure navigation fields.

## Pull information from SuccessFactors

The following actions support navigation fields:

- [Search records](/en/connectors/successfactors/successfactors-search-action) (OData V2 connections only)
- [Search records using OData query](/en/connectors/successfactors/successfactors-advanced-search-action) (OData V2 connections only)
- [Get record details](/en/connectors/successfactors/successfactors-get-action)

The navigation fields drop-down list appears when you select an object that has navigation properties.

> **TRIGGERS DON'T SUPPORT NAVIGATION FIELDS**
> 
> The [New or updated object](/en/connectors/successfactors/successfactors-triggers#new-or-updated-object) and [New or updated objects in batch](/en/connectors/successfactors/successfactors-triggers#new-or-updated-objects-in-batch) triggers don't support navigation fields. Pair the trigger with the **Get record details** action to retrieve related records for a trigger event. Map the trigger's key datapill to the action's record key properties, then select the navigation fields on the action. Map each key property for objects with composite keys (such as **Position**, which requires both `code` and `effectiveStartDate`).
> 
> You can also pair triggers with the **Search records** or **Search records using OData query** actions on OData V2 connections. For **Search records**, filter on the object's key under additional attributes. For **Search records using OData query**, add the key to the **Query** field (for example, `userId eq '...'`). Then select the navigation fields.

1. Select the related records that you want to retrieve together with the object.
   
   ![Navigation field](/assets/navigation_retrieve.BFXQSAmY.png)_Use the navigation field to select the user's manager._
   
2. After you select the related navigation field, the output datatree of the action updates with new datapills.
   
   ![Navigation field](/assets/navigation_retrieve_output.-rR7FwG2.png)_The datatree now contains datapills related to the user's manager._
   

## Push information into SuccessFactors

In actions that push information into SuccessFactors, navigation properties appear as input fields where you provide the link to the related records.

To link one record to another, you must know the target record's key properties. It consists of one or more properties that make it unique across your entire SuccessFactors instance. These properties change from object to object in SuccessFactors.

1. To find the key properties of an object, use the [Get record details](/en/connectors/successfactors/successfactors-get-action) action.
   
2. When selecting a specific object, the required fields in the action indicate the object's key properties. There are two types of objects: with one key property, or with two key properties.
   
   Here are examples of each situation:
   
   - Objects with one key property
     
   - When working with objects that have only one key property, you can enter the value of the key property surrounded by single quotation marks(').<
     
     **Example:** the **User** object has one key property, `userId`.
     
     _To relate a specific Time Type record, enter the key property 'External code' in the input field. Remember to wrap it in single quotation marks(')._
     
   - Objects with two key properties
     
   - For objects with more than one key property, you must specify the key properties along with the entered value.
     
     **Example**: the **Position** object has two key properties, `code` and `effectiveStartDate`.
     
     _To relate a specific Position record, provide the key properties `code` and `effectiveStartDate` and their values in the input field. Remember to wrap values in single quotation marks(')._

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-triggers.md
description: >-
  Explore SAP SuccessFactors connector triggers in Workato, including the New or
  updated object polling trigger that runs when an object is created or updated.
---

# SAP SuccessFactors - Triggers

## New or updated object

This [polling trigger](/en/recipes/triggers#polling-triggers) runs the recipe when you create or update a specific SuccessFactors object, such as a user.

- Trigger poll interval
  
- Enter a value to instruct the recipe how frequently to check for new events. If you leave this blank, the recipe defaults to checking every 10 minutes.
  
  This is an optional field.
  
- Object
  
- Select a SuccessFactor object from the drop-down list. Because many objects have identical names, the list includes the object's internal names.
  
- Object unique key
  
- Select the ID that the recipe uses to identify the monitored object.
  
- When first started, this recipe should pick up events from
  
- Specify the date and time for the trigger to start monitoring for events, using the format `MM/DD/YYYY HH:MM am/pm`.
  
  If you leave this field empty, the default condition is one hour: the recipe retrieves records that were created or updated one hour ago.
  
  You cannot change this value after you run or test the recipe.
  
  This is an optional field. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
  
- Output fields
  
- By default, Workato will fetch all available fields in the selected record. You may use this input to filter for only the output fields you need.
  
  This is an optional field.
  
- Query
  
- Enter the OData query filters.
  
  See [SAP documentation](https://help.sap.com/doc/7efdca36492e47c7b20ab92c4ca6323c/2211/en-US/SF_EC_OData_API_REF.pdf#page=36) to learn more about filtering with the OData v2 API.
  
  This is an optional field.
  
- From date
  
- Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from “from date” to the effective end date. You must not use “from date” together with “as of date”.
  
  This is an optional field.
  
- To date
  
- Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from the effective start date to the “to date”. You must not use “to date” together with “as of date”.
  
  This is an optional field.
  
- As of date
  
- Pick a date or enter it in MM/DD/YYYY format. You must not use "as of date" together with “from date” or “to date”.
  
  This is an optional field.
  
- Set trigger condition
  
- Set a [Trigger condition](/en/recipes/triggers.html#trigger-conditions) to define additional rules for trigger events to run a recipe.
  
  This is an optional field.
  

## New or updated objects in batch

This [batch trigger](/en/recipes/triggers#batch-triggers) retrieves a list of records created or updated after the last time the recipe was triggered.

- Trigger poll interval
  
- Enter a value to instruct the recipe how frequently to check for new events. If you leave this blank, the recipe defaults to checking every 10 minutes.
  
  This is an optional field.
  
- Object
  
- Select a SuccessFactor object from the drop-down list. Because many objects have identical names, the list includes the object's internal names.
  
- Object unique key
  
- Select the ID that the recipe uses to identify the monitored object.
  
- When first started, this recipe should pick up events from
  
- Specify the date and time for the trigger to start monitoring for events, using the format `MM/DD/YYYY HH:MM am/pm`.
  
  If you leave this field empty, the default condition is one hour: the recipe retrieves records that were created or updated one hour ago.
  
  You cannot change this value after you run or test the recipe.
  
  This is an optional field. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field.
  
- Batch size
  
- Specifies the maximum number of records per trigger event. Minimum is 1, maximum is 500, default is 500.
  
  This is an optional field.
  
- Output fields
  
- By default, Workato will fetch all available fields in the selected record. You may use this input to filter for only the output fields you need.
  
  This is an optional field.
  
- Query
  
- Enter the OData query filters.
  
  See [SAP documentation](https://help.sap.com/doc/7efdca36492e47c7b20ab92c4ca6323c/2211/en-US/SF_EC_OData_API_REF.pdf#page=36) to learn more about filtering with the OData v2 API.
  
  This is an optional field.
  
- From date
  
- Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from “from date” to the effective end date. You must not use “from date” together with “as of date”.
  
  This is an optional field.
  
- To date
  
- Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from the effective start date to the “to date”. You must not use “to date” together with “as of date”.
  
  This is an optional field.
  
- As of date
  
- Pick a date or enter it in MM/DD/YYYY format. You must not use "as of date" together with “from date” or “to date”.
  
  This is an optional field.
  
- Set trigger condition
  
- Set a [Trigger condition](/en/recipes/triggers.html#trigger-conditions) to define additional rules for trigger events to run a recipe.
  
  This is an optional field.

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-create-action.md
description: >-
  The Create record action in the SAP SuccessFactors connector creates a record
  for the selected object using the values you provide.
---

# SAP SuccessFactors - Create record action

Creates a record in SuccessFactors with the provided values for the selected object.

## Input

- Object
  
- Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names.
  
- Additional attributes
  
- Depending on the object you select and your SuccessFactors configuration, subsequent fields appear where you define additional attributes for the record, such as ID, start date, and status.
  
  A common attribute is a navigation field, which associates this record with other records through a URI, such as a user to their manager. See [Using navigation fields](/en/connectors/successfactors/successfactors-nav-fields.html).
  

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-get-action.md
description: >-
  Use the Get record details action to retrieve a specific record by searching
  with its key columns in SAP SuccessFactors.
---

# SAP SuccessFactors - Get record details action

Retrieve the details of a specific record by searching using the key columns.

## Input

| Field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |
| Record key properties | The required inputs that identify a specific record. The fields shown depend on the selected object. Refer to [Record key properties](#record-key-properties) for more information. |
| Navigation fields | Select the related records to include in the output. Navigation fields appear only on objects with navigation properties. Refer to [Use navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information. |
| Output fields | Workato fetches all available fields in the selected record by default. Use this input to filter for only the output fields you need. Optional field. |

### Record key properties

The record key properties are the required inputs that identify a specific record. The fields shown depend on the selected object's key definition:

- Single-key objects, such as **User**, display one input matching the key name. For example, **User ID** (`userId`).
- Composite-key objects, such as **Position**, display multiple required inputs. For example, **Code** (`code`) and **Effective start date** (`effectiveStartDate`).

Provide a value for all key inputs. The action returns an error if the record isn't found.

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-merge-action.md
description: >-
  The Merge record action in the SAP SuccessFactors connector updates specific
  properties in a record, leaving fields unchanged when no new value is given.
---

# SAP SuccessFactors - Merge record action

Update specific properties in a record.

If you do not provide a new value, the field value does not change.

Contrast this with the [Update action](/en/connectors/successfactors/successfactors-update-action); it sets the field to its default value if you do not provide a value.

## Input

- Object
  
- Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names.
  
- Additional attributes
  
- Depending on the object you select and your SuccessFactors configuration, subsequent fields appear where you define additional attributes for the record, such as ID, start date, and status.
  

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-search-action.md
description: >-
  Use the Search records action to retrieve a list of records that match your
  search criteria for the selected object in SAP SuccessFactors.
---

# SAP SuccessFactors - Search records action

Retrieves a list of the records that match your search criteria, such as users who work remotely.

## Input

| Field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |
| Navigation fields | Select the related records to include in the output. Navigation fields appear only when the connection uses OData V2 and the object has navigation properties. Refer to [Use navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information. |
| Additional attributes | Per-field search filters generated from the selected object. The fields depend on the selected object and your SuccessFactors configuration. Enter a value in any field to filter the search by that attribute. For example, selecting the **User** object exposes inputs such as **Display name**, **Email**, **User ID**, and **Username**. |
| Output fields | Workato fetches all available fields in the selected record by default. Use this input to filter for only the output fields you need. Optional field. |

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-advanced-search-action.md
description: >-
  Use the Search records using OData query action to retrieve records that match
  a specific OData query in SAP SuccessFactors.
---

# SAP SuccessFactors - Search records using OData query action

Retrieves the records that match a specific OData query.

## Input

| Field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |
| Query | Enter the OData query filter. Required. Refer to the [SAP documentation](https://help.sap.com/doc/7efdca36492e47c7b20ab92c4ca6323c/2211/en-US/SF_EC_OData_API_REF.pdf#page=36) to learn more about filtering with the OData v2 API. |
| Output fields | Workato fetches all available fields in the selected record by default. Use this input to filter for only the output fields you need. Optional field. |
| Page size | Specify the maximum number of records to return. Default: 100. Maximum: 1000. Optional field. |
| Offset | Specify the number of records to skip. Default: 0. Optional field. |
| Order by | Order the returned records by a field. For example, `lastModified asc` or `lastModified desc`. Optional field. |
| From date | Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from "from date" to the effective end date. You can't use "from date" together with "as of date". This field isn't supported on OData V4 connections. Optional field. |
| To date | Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from the effective start date to the "to date". You can't use "to date" together with "as of date". This field isn't supported on OData V4 connections. Optional field. |
| As of date | Pick a date or enter it in MM/DD/YYYY format. You can't use "as of date" together with "from date" or "to date". This field isn't supported on OData V4 connections. Optional field. |
| Navigation fields | Select the related records to include in the output. Navigation fields appear only when the connection uses OData V2 and the object has navigation properties. Refer to [Use navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information. |

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-update-action.md
description: >-
  The Update record action in the SAP SuccessFactors connector updates a record
  with specified values, reverting omitted fields to their default values.
---

# SAP SuccessFactors - Update record action

Updates a record with specified values. If you do not provide a value for a field, that field reverts to its default value.

Contrast this with the [Merge action](/en/connectors/successfactors/successfactors-merge-action), that does not change the value of the field if you do not provide a new value.

## Input

- Object
  
- Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names.
  
- Object unique key
  
- Select the column that contains the object ID.
  
- Additional attributes
  
- Depending on the object you select and your SuccessFactors configuration, subsequent fields appear where you define additional attributes for the record, such as ID, start date, and status.
  
- You may also select additional optional attributes to update.
  
- A common attribute is a navigation field, which associates this record with other records through a URI, such as a user to their manager. See [Using navigation fields](/en/connectors/successfactors/successfactors-nav-fields.html).
  

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-upsert-action.md
description: >-
  The Upsert record action in the SAP SuccessFactors connector finds a record by
  object ID, then updates it or creates a new record if none exists.
---

# SAP SuccessFactors - Upsert record action

The **Upsert record** action searches for a record by the object ID. If a record exists, the action updates it to the specified value. Otherwise, the action creates a new record.

The batch version processes up to 200 records each time the recipe runs.

> **UPSERT ACTION RESPONSE BEHAVIOR**
> 
> The **Upsert record** action returns a `200 OK` response from SAP SuccessFactors even when individual record updates fail. This behavior is expected because the SuccessFactors API includes each record's result in the response body instead of the HTTP status code.
> 
> Check the `Http code` value in the action output to verify if each record succeeded. You can use an **If** condition in your recipe to detect `Http code` values other than `200` and handle those records as needed.
> 
> The job completes successfully because the API returns `200 OK` when it processes the request, even if some records fail internally.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |

> **ADDITIONAL ATTRIBUTES**
> 
> Depending on the object and your SuccessFactors configuration, additional fields appear where you define more attributes for the record. You can also select optional attributes to update. A common attribute is a navigation field that links this record to another record through a URI, such as a user to their manager. Refer to [Using navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information.

## Output

The output fields vary depending on the object you select. Review the output datatree in your recipe to view available datapills.

> **DATETIME FIELDS**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-upsert-single.md
description: >-
  The Upsert records (single object) batch action searches for multiple records
  by a specified field and updates or creates them in bulk.
---

# SAP SuccessFactors - Upsert records (single object) batch action

The **Upsert records (single object)** batch action searches for records in SAP SuccessFactors by a specified field (primary key). The action updates it with the provided data if a record exists. Otherwise, it creates the record with the provided data.

This action processes up to 200 records each time the recipe runs and only supports OData V2.

> **UPSERT ACTION RESPONSE BEHAVIOR**
> 
> The **Upsert records (single object)** batch action returns a `200 OK` response from SAP SuccessFactors even when individual record updates fail. This behavior is expected because the SuccessFactors API includes each record's result in the response body instead of the HTTP status code.
> 
> Check the `Http code` value in the action output to verify if each record succeeded. You can use an **If** condition in your recipe to detect `Http code` values other than `200` and handle those records as needed.
> 
> The job completes successfully because the API returns `200 OK` when it processes the request, even if some records fail internally.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |
| Object source list | Insert a list datapill. See [List input datapills](/en/features/list-management#list-batch-action). |

> **ADDITIONAL ATTRIBUTES**
> 
> Depending on the object and your SuccessFactors configuration, additional fields appear where you define more attributes for each record. You can also select optional attributes to update. A common attribute is a navigation field that links this record to another record through a URI, such as a user to their manager. Refer to [Using navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information.

## Output

The output fields vary depending on the object you select. Review the output datatree in your recipe to view available datapills.

> **DATETIME FIELDS**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).

---

---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-upsert-multiple.md
description: >-
  The Upsert records (multiple objects) batch action performs simultaneous
  operations on multiple SuccessFactors objects with transactional behavior.
---

# SAP SuccessFactors - Upsert records (multiple objects) batch action

The **Upsert records (multiple objects)** batch action performs simultaneous operations on one or more SuccessFactors objects. It follows transactional behavior. The entire batch fails when one operation fails. This action only supports OData V2.

> **UPSERT ACTION RESPONSE BEHAVIOR**
> 
> The **Upsert record (multiple objects)** batch action returns a `200 OK` response from SAP SuccessFactors even when individual record updates fail. This behavior is expected because the SuccessFactors API includes each record's result in the response body instead of the HTTP status code.
> 
> Check the `Http code` value in the action output to verify if each record succeeded. You can use an **If** condition in your recipe to detect `Http code` values other than `200` and handle those records as needed.
> 
> The job completes successfully because the API returns `200 OK` when it processes the request, even if some records fail internally.

## Input

| Input field | Description |
| --- | --- |
| Objects | Select one or more SuccessFactors objects. Because objects can have similar names, the list includes their internal names. For example, `User`. |
| Object attributes | For each selected object, define the required key fields, such as `ID` or `Key`. The action updates existing records if the keys exist or creates new records otherwise. |

> **ADDITIONAL ATTRIBUTES**
> 
> Depending on the object and your SuccessFactors configuration, additional fields appear where you define more attributes for the record. You can also select optional attributes to update. A common attribute is a navigation field that links this record to another record through a URI, such as a user to their manager. Refer to [Using navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information.

## Output

| Output field | Description |
| --- | --- |
| Batch ID | Unique identifier for the batch operation. |
| Objects | Contains object-level results for each record included in the batch. |

---
