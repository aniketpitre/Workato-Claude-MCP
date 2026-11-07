---
url: 'https://docs.workato.com/en/connectors/plusone-solutions.md'
description: >-
  The PlusOne Solutions connector lets you automate vendor management workflows:
  create, update, search, and retrieve records by ID.
---

# PlusOne Solutions

[PlusOne Solutions](https://www.plus1solutions.net/) is a comprehensive vendor management platform that streamlines compliance, screening, and relationship management for companies working with external vendors and contractors. The platform helps organizations manage the entire vendor lifecycle, from onboarding and compliance tracking to performance monitoring and relationship maintenance.

> **API ACCESS REQUIRED**
> 
> You must have an active PlusOne Solutions account with API access to connect to PlusOne Solutions in Workato. Contact your PlusOne Solutions administrator to ensure API access is enabled for your account. Refer to the [PlusOne Solutions API documentation](https://app.swaggerhub.com/apis-docs/PlusOne_Solutions/production-plusone-api/latest#/) for detailed information about available endpoints and data structures.

## How to connect to PlusOne Solutions

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **PlusOne Solutions** as your connection on the **New Connection** page.
   
3. Provide a **Connection name** that identifies which PlusOne Solutions instance Workato is connected to.
   
   ![PlusOne Solutions Connection](/assets/plusone-solutions-connection.Duhqq5pQ.png)_PlusOne Solutions Connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select the PlusOne Solutions **Environment** to connect to:
   
   - **Testing** - Connects to the test environment (api-test.plus1staging.net)
   - **Production** - Connects to the production environment (api.plus1solutions.net)
6. Enter the **Email address** associated with your PlusOne Solutions account. This is used for authentication and audit logging.
   
7. Enter the **Password** for your PlusOne Solutions account.
   
8. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/plusone-solutions/create-record-action.md
description: >-
  The Create record action creates a standard record, such as a company, in
  PlusOne Solutions.
---

# PlusOne Solutions - Create record action

The **Create record** action creates a standard record, such as a company, in PlusOne Solutions.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to create. |

Input fields load dynamically based on the selected **Object**. For example, the input schema is as follows if you select the **Company** object:

| Input fields | Description |
| --- | --- |
| PlusOne Client ID | Provide the unique 13-character identifier assigned to each client in the PlusOne Network. |
| PlusOne Username | Provide the username assigned to the individual making the request. This is used for audit log entries. Leave this field blank to use the email address specified during [connection setup](/en/connectors/plusone-solutions#connection-setup). |
| Tax ID | Provide the tax identifier for the company. A full tax ID should only be passed when a company is first created. |
| Tax ID Type | Provide the type of tax identifier, such as `SSN` or `EIN`. |
| Company Name | Provide the name of the company to create. |
| DBA | Provide the DBA (Doing Business As) name of the company. |
| Company Type | Provide the type of company structure, such as `CC`. |
| Minority Type | Provide the minority business classification, such as `MINOR`. |
| URL | Provide the company website URL. |
| State of Incorporation | Provide the state ID where the company is incorporated, such as `AL` for Alabama. |
| PENDOT ID | Provide the PENDOT identifier for the company. |
| Addresses | Provide an array of address objects containing the company's type, address lines, city, state, country, and ZIP code. |

## Output

Output fields load dynamically based on the selected **Object**. For example, the output schema is as follows if you select the **Company** object:

| Output field | Description |
| --- | --- |
| Company PlusOne ID | PlusOne's unique company identifier for the newly created company. |
| Company | Object containing details about the newly created company. |
| Client PlusOne ID | PlusOne's unique client identifier. |
| Company ID | Internal company identifier. |
| Company Registration Date | Date when the company was registered. |
| Company Contract Expiration | Contract expiration date. |

---

---
url: >-
  https://docs.workato.com/en/connectors/plusone-solutions/get-record-details-action.md
description: >-
  The Get record details by ID action retrieves specific record information from
  PlusOne Solutions using the record's unique identifier.
---

# PlusOne Solutions - Get record details by ID action

The **Get record details by ID** action retrieves specific record information from PlusOne Solutions using the record's unique identifier.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to retrieve. |

Input fields load dynamically based on the selected **Object**. For example, the input schema is as follows if you select the **Company details** object:

| Input fields | Description |
| --- | --- |
| PlusOne Company ID | Provide the unique 13-character identifier assigned to the company in the PlusOne Network. |
| PlusOne Username | Provide the username assigned to the individual making the request. This is used for audit log entries. Leave this field blank to use the email address specified during [connection setup](/en/connectors/plusone-solutions#connection-setup). |

## Output

Output fields load dynamically based on the selected **Object**. For example, the output schema is as follows if you select the **Company details** object:

| Output field | Description |
| --- | --- |
| PlusOne ID | Unique 13-character identifier assigned to the company in the PlusOne Network. |
| Company Name | Name of the company. |
| DBA | Doing Business As (DBA) name. |
| Tax ID | Tax identifier assigned to the company. |
| Tax ID Type | Type of tax identifier, such as `EIN` or `SSN`. |
| Company Type | Type of company structure, such as `CC`. |
| Minority Type | Minority business classification. |
| URL | Company website URL. |
| State of Incorporation | State where the company is incorporated. |
| PENDOT ID | PENDOT identifier. |
| Primary Location | Indicates whether this is the primary location. |
| Phone Numbers | Array of phone number objects with type, number, and extension. |
| Addresses | Array of address objects with complete address information. |
| Emails | Array of email objects with type and email address. |
| Industries | Array of industry classification objects. |
| Contacts | Array of contact objects with detailed contact information. |

---

---
url: >-
  https://docs.workato.com/en/connectors/plusone-solutions/search-records-action.md
description: >-
  The Search records action retrieves a list of records matching the specified
  criteria from PlusOne Solutions.
---

# PlusOne Solutions - Search records action

The **Search records** action retrieves a list of records matching the specified criteria from PlusOne Solutions.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to search for. |

Input fields load dynamically based on the selected **Object**. For example, the input schema is as follows if you select the **Company relationship** object:

| Input fields | Description |
| --- | --- |
| PlusOne Client ID | Provide the unique 13-character identifier assigned to each client in the PlusOne Network. |
| PlusOne Username | Provide the username assigned to the Individual making the request by PlusOne. Used to create audit log entries. Leaving this blank will use the email address from the connection. |
| PlusOne Client Company ID | Provide the unique identifier assigned to each company by the client. This can be different from the Company PlusOne ID. |
| Include Inactive | Select the boolean value from the drop-down menu. Choose 'Yes' to include inactive records or 'No' to exclude them. |
| Offset | Provide the number of records to skip from the beginning of the result set. |
| Page Size | Provide the number of records to return. Defaults to 1000 if not specified. |

## Output

Output fields load dynamically based on the selected **Object**. For example, the output schema is as follows if you select the **Company relationship** object:

| Output fields | Description |
| --- | --- |
| Records | Array of company relationship records. |
| Company PlusOne ID | PlusOne's unique company identifier for each record. |
| Client PlusOne ID | PlusOne's unique client identifier for each record. |
| Company ID | Internal company identifier for each record. |
| Company Registration Date | Date when the company was registered. |
| Company Contract Expiration | Contract expiration date. |
| Company | Object containing basic company information including name, DBA, tax information, and company type. |

---

---
url: >-
  https://docs.workato.com/en/connectors/plusone-solutions/update-record-action.md
description: The Update record action updates the specified record in PlusOne Solutions.
---

# PlusOne Solutions - Update record action

The **Update record** action updates the specified record in PlusOne Solutions.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to update. |

Input fields load dynamically based on the selected **Object**. For example, the input schema is as follows if you select the **Company relationship** object:

| Input fields | Description |
| --- | --- |
| PlusOne Client ID | Provide the unique 13-character identifier assigned to each client in the PlusOne Network. |
| PlusOne Company ID | Provide the unique 13-character identifier assigned to each company in the PlusOne Network. |
| PlusOne Username | Provide the username assigned to the individual making the request. This is used for audit log entries. Leave this field blank to use the email address specified during [connection setup](/en/connectors/plusone-solutions#connection-setup). |
| Jobscope Vendor Number | Provide a valid Jobscope vendor number for the update. |

## Output

Output fields load dynamically based on the selected **Object**. For example, the output schema is as follows if you select the **Company relationship** object:

| Output field | Description |
| --- | --- |
| Company PlusOne ID | PlusOne's unique company identifier. |
| Company | Updated company information object containing all company details. |
| Client PlusOne ID | PlusOne's unique client identifier. |
| Company ID | Internal company identifier. |
| Company Registration Date | Date when the company was registered. |
| Company Contract Expiration | Updated contract expiration date. |

---
