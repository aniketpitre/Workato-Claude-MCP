---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipeline-recipe/configure-chargebee.md
description: >-
  Configure Chargebee as a data pipeline source to extract subscription,
  billing, invoicing, and payment records and sync them to your destination.
---

# Configure Chargebee as a data pipeline source

Set up Chargebee as a data pipeline source to extract subscription, billing, invoicing, and payment records into your destination.

Use this guide to set up a connection, configure your pipeline, add objects, review sync behavior, and understand known limitations.

## Chargebee features supported

The following features are supported when you use Chargebee as a pipeline source:

- **Cloud connectivity**: Connect to Chargebee over HTTPS through your site's subdomain (`https://{subdomain}.chargebee.com`). On-prem agents aren't required.
- **Live and test site support**: Connect to either your live Chargebee site or its dedicated test site by providing the corresponding subdomain. Workato treats each site as a separate connection.
- **Full sync and incremental sync**: Supports full sync and incremental sync modes for objects that advertise incremental support. The cursor field varies by object. Refer to [Sync modes](#sync-modes) for more information.
- **Object-level selection**: Select Chargebee objects to sync as separate tables in your destination. Refer to [Supported objects](#supported-objects) for the full list.
- **Delete tracking**: Detect deletions for supported objects and mark deleted records in your destination. Refer to [Delete tracking](#delete-tracking) for the list of objects.
- **Custom field discovery**: Automatically syncs Chargebee custom fields (`cf_*`) for supported objects. Refer to [Custom fields](#custom-fields) for more information.
- **Schema drift detection and handling**: Detect and apply schema changes automatically with **Auto-sync new fields**, or keep the schema fixed with **Block new fields**.
- **Field-level data protection**: Hash or replicate sensitive fields as is before the data reaches your destination.
- **Configurable sync frequency**: Schedule syncs on a time-based interval or with a cron expression. The minimum supported interval is 15 minutes.

## Chargebee prerequisites

Connecting Chargebee as a data pipeline source requires:

- A Chargebee account, either live or on a dedicated test site.
- A **Read-only: All** API key generated from your Chargebee site. Refer to the Chargebee [API Keys](https://www.chargebee.com/docs/billing/2.0/site-configuration/api_keys) documentation for setup steps.
- Your Chargebee site subdomain
- The Product Catalog version your Chargebee site uses, either PC 1.0 or PC 2.0

> **REQUIRED PERMISSIONS**
> 
> Generate a **Read-only: All** key for this connection, not **Read-only: Restricted**, which excludes coupons, coupon sets, and coupon codes and blocks the `Coupon` and `CouponCode` objects. Each Chargebee site, including its dedicated test site, has its own independent set of API keys. Generate the key from the same site whose subdomain you plan to enter in the connection.

## Supported connection types

Chargebee data pipelines support one authentication method:

- **API key**: Provide a **Read-only: All** API key generated from your Chargebee site, along with your site subdomain and Product Catalog version. Chargebee doesn't support OAuth 2.0 for API access. Refer to [Prerequisites](#prerequisites) for setup requirements.

## Connect to Chargebee

Complete the following steps to connect Chargebee as a data pipeline source:

Connect to Chargebee

1. Select **Create > Connection** or press C twice.
   
2. Search for `Chargebee` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Paste the Chargebee API key you generated into the **API key** field.
   
6. Enter your Chargebee site name in the **Subdomain** field. For example, enter `acme` if you sign in to Chargebee at `https://acme.chargebee.com`. Enter the corresponding test site subdomain, which ends in `-test`, to connect to test data instead of live data.
   
7. Use the **Product catalog** drop-down menu to select the Product Catalog version your Chargebee site uses, either **PC 1.0** or **PC 2.0**.
   
8. Select **Connect** to verify and save the connection. Workato displays a success message when the connection is established.
   

> **DETERMINE YOUR PRODUCT CATALOG VERSION**
> 
> Chargebee sites created before May 5, 2021 use Product Catalog 1.0. Sites created on or after that date use Product Catalog 2.0. The version you select determines which catalog objects are available to add to your pipeline: `Plan` and `Addon` on Product Catalog 1.0 sites, or `ItemFamily`, `Item`, `ItemPrice`, `DifferentialPrice`, `PriceTier`, `SubscriptionItem`, and `Usage` on Product Catalog 2.0 sites. Check your Chargebee site settings if you're unsure which version applies to your account.

## Configure the pipeline

Complete the following steps to configure Chargebee as your data pipeline source:

1. Select **Create > Data pipeline** or press C+I.
   
2. Enter a name for the data pipeline in the **Data pipeline name** field.
   
   ![Data pipeline setup](/assets/set-up-pipeline.Cxx6hIk2.png)_Data pipeline setup_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the data pipeline.
   
4. Click **Start building**.
   
5. Click the **Extract new/updated records from source app** trigger. This trigger defines how the pipeline retrieves data from Chargebee.
   
   ![Configure the Extract new/updated records from source app trigger](/assets/choose-source-app.B2OOUpgY.png)_Configure the Extract new/updated records from source app trigger_
   
6. Use the **Your Connected Source Apps** drop-down menu to select **Chargebee**.
   
7. Choose the Chargebee connection you plan to use for this pipeline. Alternatively, click **\+ New connection** to create a new connection.
   
8. Click **Add object** to open the **Add new objects** panel.
   
   ![Add objects](/assets/add-objects-chargebee.CHUmESuO.png)_Add objects_
   
9. Search or browse the list of available Chargebee objects, select the objects you plan to sync, and click **Add**.
   
   > **CHILD OBJECTS SYNC AS FULL SYNC ONLY**
   > 
   > Objects that sync alongside a parent record, such as `SubscriptionItem`, `InvoiceLineItem`, `PriceTier`, and `QuotedSubscription`, appear with a **Full sync** tag in the object list and don't have an independent sync mode. Refer to [Supported objects](#supported-objects) for the full list of child objects.
   
10. Optional. Click the gear icon next to an object to open its **Sync mode** settings. Use the **Sync mode** drop-down menu to select **Full sync** or **Incremental**, then click **Save**.
    
    The sync mode defaults to **Full sync** for objects that don't support incremental sync, including objects without a usable cursor and child objects that sync with a parent. Refer to [Sync modes](#sync-modes) for more information.
    
11. Review and customize the schema for each selected object. The pipeline automatically fetches an object's schema when you select it. This ensures the destination matches the source.
    
    Expand an object to view associated fields. Keep all fields selected to extract all available data, or deselect specific fields to exclude them from data extraction and schema replication.
    
12. Optional. Configure field-level data protection by expanding an object and choosing how to handle each field:
    
    - **Replicate as is**: Data values at the source replicate identically to the destination.
    - **Hash**: Hash sensitive data values in the field before syncing to your destination.
    
    Workato recommends hashing personally identifiable information (PII) and other sensitive fields. Refer to [Sensitive data handling](#sensitive-data-handling) for a list of fields that commonly contain PII.
    
13. Click **Add object** again to add more objects. Repeat this step to include additional Chargebee objects in your pipeline.
    
14. Use the **Choose how to handle schema changes** drop-down menu to select a schema drift handling option:
    
    - **Auto-sync new fields**: Automatically detects and syncs new fields added in the source.
    - **Block new fields**: Keeps the schema fixed after the pipeline starts. You must add new fields manually. This option may cause the destination to fall out of sync if the source schema updates.
    
    Refer to [Schema replication and schema drift management](/en/data-orchestration/data-pipeline-recipe/concepts#schema-drift) for more information.
    
    Workato recommends **Auto-sync new fields** for Chargebee accounts that use custom fields (`cf_*`), so new custom fields sync automatically. Refer to [Custom fields](#custom-fields) for more information.
    
15. Optional. Enter a value in the **Concurrency limit** field to cap the number of concurrent operations. Leave the field blank to use the default limit set by Workato. The Chargebee implementation advertises `5` concurrent objects by default. The effective limit can't exceed the source-advertised limit.
    
16. Choose either a standard time-based schedule or define a custom cron expression in the **Frequency** field. This determines how often the pipeline syncs data from Chargebee to the destination.
    
    **Time-based schedule**
    
    1. Select the **Time unit**, such as **Minutes**, **Hours**, or **Days**.
       
    2. Specify the sync interval in the **Trigger every** field.
       
       For example, the pipeline syncs every 6 hours if you select **Hours** as the **Time unit** and enter `6` in the **Trigger every** field.
       
       The minimum interval you can set is 15 minutes.
       
    3. Select a start date for the historical data sync in the **When first started, this pipeline should pick up records from** field. This defines the earliest date from which the pipeline extracts records. The pipeline picks up all available records from the source if you leave this field blank.
       
       You can't change this value after you run the pipeline.
       
    4. Click **Save** to save your progress before you [configure your data pipeline destination](/en/data-orchestration/data-pipeline-recipe/configure-pipeline-destinations#configure‒how‒data‒is‒loaded‒in‒the‒workato‒data‒pipeline).
       
    
    **Cron-based scheduling**
    
    1. Use the **Time unit** drop-down menu to select **Custom schedule**.
       
    2. Enter an expression in the **Cron expression** field using the format:
       
       ```text
       [minute] [hour] [day of month] [month] [day of week]
       ```
       
       The minimum interval for cron schedules is 15 minutes.
       
       For example, enter the following expression to sync every day at 8:00 AM UTC:
       
       ```text
       0 8 * * *
       ```
       
    3. Optional. Select a **Timezone** for the cron expression. Leave blank to use `Etc/UTC`.
       
    4. Select a start date for the historical data sync in the **When first started, this pipeline should pick up records from** field. This defines the earliest date from which the pipeline extracts records. The pipeline picks up all available records from the source if you leave this field blank.
       
       You can't change this value after you run the pipeline.
       
    5. Click **Save** to save your progress before you [configure your data pipeline destination](/en/data-orchestration/data-pipeline-recipe/configure-pipeline-destinations#configure‒how‒data‒is‒loaded‒in‒the‒workato‒data‒pipeline).
       
    

## Supported Chargebee objects

Chargebee data pipelines sync data from the Chargebee API v2. The following tables list the supported objects, grouped by category. Each object syncs as a separate table in your destination, unless noted otherwise.

Your connection's Product Catalog version determines which catalog objects are available to add to your pipeline. `Subscription` and `Coupon` include fields from both catalog versions, but only the fields for your site's version contain data.

### Core account and billing objects

| Object | Sync modes | Delete tracking |
| --- | --- | --- |
| `Customer` | Full sync, incremental | Yes (soft) |
| `Subscription` | Full sync, incremental | Yes (soft) |
| `SubscriptionItem` | Full sync only (syncs with the parent `Subscription` object, PC 2.0 only) | No |
| `Invoice` | Full sync, incremental | Yes (soft) |
| `InvoiceLineItem` | Full sync only (syncs with the parent `Invoice` object) | No |
| `CreditNote` | Full sync, incremental | Yes (soft) |
| `Transaction` | Full sync, incremental | Yes (soft) |
| `PaymentSource` | Full sync, incremental | Yes (soft) |

`Subscription`, `Invoice`, and `CreditNote` expose a native `deleted` flag used for delete tracking, as well as a `status` value for their primary business lifecycle. Chargebee moves these records through statuses such as `cancelled` for a `Subscription` or `voided` for an `Invoice`. Treat `status` as the business-lifecycle signal, not as the connector's soft-delete signal.

### Discounts

| Object | Sync modes | Delete tracking |
| --- | --- | --- |
| `Coupon` | Full sync, incremental | Yes (soft) |
| `CouponCode` | Full sync | Yes (destination-inferred) |

### Product catalog: PC 1.0

Available only when your connection's Product Catalog version is PC 1.0.

| Object | Sync modes | Delete tracking |
| --- | --- | --- |
| `Plan` | Full sync, incremental | Yes (soft) |
| `Addon` | Full sync, incremental | Yes (soft) |

### Product catalog: PC 2.0

Available only when your connection's Product Catalog version is PC 2.0.

| Object | Sync modes | Delete tracking |
| --- | --- | --- |
| `ItemFamily` | Full sync, incremental | No |
| `Item` | Full sync, incremental | No |
| `ItemPrice` | Full sync, incremental | No |
| `DifferentialPrice` | Full sync | Yes (destination-inferred) |
| `PriceTier` | Full sync only (syncs with the parent `ItemPrice` or `DifferentialPrice` object, PC 2.0 only) | No |

### Orders, quotes, and other billing objects

| Object | Sync modes | Delete tracking |
| --- | --- | --- |
| `Order` | Full sync, incremental | Yes (soft) |
| `Gift` | Full sync | Yes (destination-inferred) |
| `UnbilledCharge` | Full sync | Yes (soft) |
| `Quote` | Full sync, incremental | Yes (soft) |
| `QuotedSubscription` | Full sync only (syncs with the parent `Quote` object) | No |
| `VirtualBankAccount` | Full sync, incremental | No |

`Quote` and `QuotedSubscription` require a Chargebee Performance or Enterprise plan. Refer to [Limitations](#limitations) for more information.

### Usage and events

| Object | Sync modes | Delete tracking |
| --- | --- | --- |
| `Usage` | Full sync only (append-only extraction, PC 2.0 only) | N/A |
| `Event` | Full sync, incremental (append-only extraction) | N/A |
| `Comment` | Full sync, incremental (append-only extraction) | N/A |
| `PromotionalCredit` | Full sync, incremental (append-only extraction) | N/A |

## Sync modes

Chargebee data pipelines support full sync and incremental sync. The sync mode is configured per object when you add it to your pipeline.

### Full sync

A full sync reads all available records from Chargebee for the selected object on every run. Full-sync-only objects include `CouponCode`, `Gift`, `DifferentialPrice`, `UnbilledCharge`, and `Usage`. Some are full-sync-only because they lack a usable cursor, while others have no safe primary key for incremental upserts. Child objects that sync with a parent, including `SubscriptionItem`, `InvoiceLineItem`, `PriceTier`, and `QuotedSubscription`, also only support full sync.

Objects with a primary key merge into the existing destination table, so records deleted in Chargebee stay in the table. Objects without a primary key overwrite the destination table on every run.

### Incremental sync

An incremental sync extracts only records created or updated since the last successful run, using an object-specific cursor. Most objects that support incremental sync use `updated_at`, `Event` uses `occurred_at`, and `Comment` and `PromotionalCredit` use `created_at`. `Usage` is full-sync-only, and its append-only endpoint filters by `updated_at` and sorts by `usage_date`. Append-only extraction inserts new rows and doesn't perform conflict resolution for existing rows.

Objects that sync alongside a parent record, such as `SubscriptionItem` and `InvoiceLineItem`, have no independent cursor. Workato extracts these rows whenever the parent object's row is extracted.

Refer to the [Supported objects](#supported-objects) tables to see the sync modes available for each object.

### Delete tracking

Workato reads Chargebee's `deleted` flag and sets the `_workato_is_deleted` column to `true` on the destination row for `Customer`, `Subscription`, `Invoice`, `CreditNote`, `Transaction`, `PaymentSource`, `Coupon`, `Order`, `UnbilledCharge`, and `Quote`. `Subscription`, `Invoice`, and `CreditNote` also expose `status`, but the connector treats it as a business-lifecycle field rather than a replacement for native delete tracking. For `Plan` and `Addon`, Workato derives `_workato_is_deleted` from `status == "deleted"`.

`CouponCode`, `Gift`, and `DifferentialPrice` don't provide a delete signal that the connector can observe during extraction. Workato compares each full sync against the previous run and marks records that no longer appear in Chargebee as deleted in the destination, because these objects only support full sync. Although `DifferentialPrice` has a raw `deleted` field, its list extraction does not expose deleted rows for native delete tracking.

Refer to the [Supported objects](#supported-objects) tables to see which objects support delete tracking.

## Schema and data type handling

The following considerations apply to schema and data types when you sync data from Chargebee.

### Monetary amounts

Chargebee stores monetary amounts as integers in the smallest currency unit of the relevant currency, such as cents for USD. Workato preserves these raw integer values and doesn't perform currency conversion. When Chargebee provides a decimal-form monetary field with an `_in_decimal` suffix, Workato preserves it as a string.

### Timestamps

Chargebee returns timestamps as Unix epoch integers. Workato preserves the raw epoch values in the destination and doesn't convert them to a timestamp format.

### Custom fields

Chargebee supports user-defined custom fields, which appear on objects with a `cf_` prefix, such as `cf_industry`. Workato automatically discovers and syncs custom fields for `Customer`, `Subscription`, `Invoice`, `CreditNote`, `Plan`, `Addon`, `Item`, and `ItemPrice`. Custom fields on other objects aren't synced.

Custom fields vary by account and change over time. Select **Auto-sync new fields** when you [configure the pipeline](#configure-the-pipeline) so new custom fields sync automatically.

### Nested objects and arrays

Chargebee objects can include nested objects and arrays, such as `billing_address` on `Customer` or `line_items` on `Invoice`. Workato stores these as a JSON column in the destination, except where the nested array corresponds to its own supported object. For example, `Invoice.line_items` syncs as the `InvoiceLineItem` object instead. Workato doesn't flatten nested fields into individual columns. For very large invoices, Chargebee can return a `line_items_next_offset` value. The connector extracts the inline `line_items` array but doesn't follow that overflow offset, so additional line items beyond the inline array aren't synced.

Workato syncs JSON fields to the destination's native JSON type, such as `VARIANT` in Snowflake. Workato serializes JSON fields as strings if the destination doesn't support a native JSON type.

### Synthetic columns

Workato adds the following synthetic column to destination tables for objects with delete tracking:

| Column | Type | Purpose |
| --- | --- | --- |
| `_workato_is_deleted` | Boolean | Set to `true` for deleted or removed records. Refer to [Delete tracking](#delete-tracking) for the list of objects this applies to. |

### Sensitive data handling

Chargebee objects can contain personally identifiable information (PII) and financial data. The following objects commonly contain sensitive fields:

| Object | Sensitive fields |
| --- | --- |
| `Customer` | `first_name`, `last_name`, `email`, `phone`, `company`, `billing_address`, `shipping_address`, `vat_number`, custom fields (`cf_*`) |
| `PaymentSource` | `masked_number` or `last4`, `card_type`, `expiry_month`, `expiry_year`, billing details |
| `Invoice`, `CreditNote` | `billing_address`, `shipping_address`, and customer name and email snapshots |
| `Transaction` | Gateway reference IDs and masked payment details |
| `VirtualBankAccount` | Account and routing references |

Chargebee doesn't return full card numbers or CVV values through its API, so Workato doesn't sync raw payment card data for `PaymentSource`.

Use the **Hash** option in field-level data protection during pipeline configuration to protect PII before it reaches your destination. Refer to the [Configure the pipeline](#configure-the-pipeline) steps for more information.

## Chargebee limitations

The following limitations apply when you use Chargebee as a data pipeline source:

### Quote and QuotedSubscription require a paid Chargebee plan

`Quote` and `QuotedSubscription` are only available on a Chargebee Performance or Enterprise plan. These two objects don't appear in the **Add new objects** panel if your account doesn't have this feature enabled.

### Business entities are not synced as a separate object

Workato doesn't sync a dedicated object listing your Chargebee site's business entities, because Chargebee doesn't expose a corresponding list endpoint. Objects that belong to an entity still carry a `business_entity_id` field if your site uses the Business Entities feature, and Workato preserves it as-is so you can segment records by entity.

### One connection per Chargebee site

A Chargebee API key is scoped to a single site, so create a separate connection for each Chargebee site you sync from, including a live site and its dedicated test site.

### Transaction records are re-imported daily

Chargebee can update a `Transaction` record's settlement status after Workato first extracts it. To capture these late updates, Workato re-imports the full `Transaction` table once every `24` hours, in addition to incremental syncs.

### Minimum sync frequency

The minimum supported sync interval is 15 minutes.
