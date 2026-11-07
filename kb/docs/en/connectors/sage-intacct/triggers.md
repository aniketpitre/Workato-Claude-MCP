---
url: 'https://docs.workato.com/en/connectors/sage-intacct/triggers.md'
description: >-
  Explore triggers in the Sage Intacct community connector for Workato,
  including new and updated AP bills, contracts, customers, invoices, and
  vendors.
---

# Sage Intacct (Custom) - Triggers

The Sage Intacct community connector supports the following triggers:

- New AP bill
- New contract
- New customer
- New purchasing transaction
- New purchasing transaction line
- New vendor
- New/updated AP bill
- New/updated contract
- New/updated customer
- New/updated invoice
- New/updated purchasing transaction
- New/updated purchasing transaction line
- New/updated vendor

The input and output fields dynamically load based on the trigger selected. For example, if you select the **New AP bill** trigger, the output schema is:

| Output field | Description |
| --- | --- |
| Record number | Unique identifier for the AP bill record. |
| Record type | Type of record. |
| Bill number | The bill invoice number. |
| Contact tax group | Tax grouping related to the contact/vendor. |
| Financial entity | The financial entity involved in the transaction. |
| State | Payment state or status of the bill. |
| Raw state | Raw status code of the bill. |
| Vendor entity | The vendor's entity reference. |
| Vendor ID | Unique identifier for the vendor. |
| Vendor name | Name of the vendor. |
| Vendor key | Internal key for the vendor. |
| Form 1099 type | 1099 tax form type associated with the vendor. |
| Form 1099 box | Specific box on the 1099 form. |
| Vendor type form 1099 type | Vendor classification for 1099 reporting. |
| Vendor due | Total amount due to the vendor. |
| Reference number | Reference number for the bill. |
| Description | Description or memo of the bill. |
| Document ID | Identifier for the related document. |
| Term | Payment terms. |
| Term key | Internal key for payment terms. |
| Term value | Detailed value of terms. |
| Date | Date of the bill document. |
| GL posting date | Date the transaction posts to the General Ledger. |
| Discount date | Date by which payment discounts apply. |
| Due date | Payment due date. |
| Date fully paid | Date when bill was fully paid. |
| Recommended to pay on | Recommended payment date. |
| Payment priority | Priority for payment. |
| Place this bill on hold | Indicates if the bill is on hold (true/false). |
| Base currency | Base currency of the transaction. |
| Transaction currency | Currency used in transaction. |
| Exchange rate date | Date used for exchange rate. |
| Exchange rate type | Type of exchange rate applied. |
| Exchange rate | Actual exchange rate value. |
| Total amount | Total amount of the bill. |
| Total selected | Total amount selected for payment. |
| Total paid | Total amount paid. |
| Total due | Total amount still due. |
| Total transaction amount | Total amount in transaction currency. |
| Total transaction amount selected | Amount selected in transaction currency. |
| Total transaction amount paid | Amount paid in transaction currency. |
| Total transaction amount due | Amount due in transaction currency. |
| Pay to | Vendor name to pay. |
| Return to | Vendor name to return goods/services. |
| Pay-to contact key | Internal contact key for payment. |
| Return-to contact key | Internal contact key for returns. |
| Summary | Summary description or batch info. |
| Summary key | Internal key for summary. |
| Module key | Module identifier. |
| Recurring schedule key | Key for recurring billing schedule. |
| System generated | Flag indicating if record was system generated (T/F). |
| Audit when created | Timestamp when the bill was created. |
| When modified | Timestamp when the bill was last modified. |
| Created by | User ID who created the bill. |
| Modified by | User ID who last modified the bill. |
| Due in | Number of days until due. |
| Record number | A unique number belonging to the AP bill record. |
| Inclusive taxes | Indicates if taxes are included in amounts. |
| Tax solution | Tax solution applied. |
| Default retainage percentage | Default retainage % for the bill. |
| Total txn amount retained | Amount retained from transaction. |
| Total txn amount released | Amount released from retainage. |
| Total retained amount | Total amount retained. |
| Attachment | Attachment information or link. |
| Bill back template | Template used for bill backs. |
| Bill back template use IET offset | Use of IET offset for bill back template. |
| Modified by | User who last modified. |
| Created by | User who created. |
| Source | Source of the bill data. |
| Import exceptions | Exceptions encountered during import. |
| Recipient email | Email address of recipient. |
| Sender email | Email address of sender. |
| Source module | Module from which the record originates. |
| Retainage release | Indicates if retainage has been released (true/false). |
| Invoice key | Key of the invoice related to the bill. |
| Retainage invoice type | Type of retainage invoice. |
| Created at - entity key | Entity key where the bill was created. |
| Created at - entity ID | Entity ID where the bill was created. |
| Created at - entity name | Name of the entity where bill was created. |
| Record URL | URL to access the record in Sage Intacct. |

---
