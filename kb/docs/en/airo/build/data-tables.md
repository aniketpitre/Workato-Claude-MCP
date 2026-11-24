---
url: 'https://docs.workato.com/en/airo/build/data-tables.md'
description: Create data tables and define their schemas with AIRO Connect.
---

# Build data tables with AIRO Connect

Use [AIRO Connect](/en/airo/mcp) to create data tables and define their schemas. Describe the table's columns, specify each column's data type, and explain the table's relationships to other tables.

Refer to [Create a new table](/en/data-tables/user-interface/create) for the manual workflow in Workato.

> **AIRO DATA TABLE SUPPORT**
> 
> AIRO can create data tables and change data table schemas only through an MCP client connected to [AIRO Connect](/en/airo/mcp). Chatting with AIRO directly in Workato doesn't provide this functionality.
> 
> AIRO Connect can query records but can't create, update, or delete them. Refer to [Add or update records](#add-or-update-records) for record-management options.

## Prerequisites

You must have the following before you create data tables:

- AIRO enabled in the target workspace.
- An MCP client, such as Claude Code, Claude Desktop, or Cursor, connected to [AIRO Connect](/en/airo/mcp).
- The **Data tables** privilege, with **Create** and **Modify structure** access, in the target project. Refer to [Project asset privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets).

Confirm that your AIRO Connect connection points to the intended workspace and environment before you start. AIRO Connect exposes separate tools for table creation, schema changes, and record queries. Your MCP client may prompt you to approve each call.

## Example: Build a vendor contracts tracker

This example creates a "Vendor contracts" table to track active contracts and automatic renewals. The table relates to a "Vendor categories" table.

Create the related table first.

```text
Create a data table called "Vendor categories" with one column: name (short text, required).
```

Create the "Vendor contracts" table and define its relationship to "Vendor categories".

```text
Create a data table called "Vendor contracts". Columns: vendor name (short text, required), category (relate to the "Vendor categories" table), contract value (decimal), start date (date, required), renewal date (date, required), and status (short text, defaulting to "active").
```

AIRO uses a lookup tool to find the "Vendor categories" table ID and the ID of the target column, usually `name`. Confirm the resolved table and column before you continue. Relation columns can link only to short text or long text columns. A relation column can't be required or have a default value.

AIRO creates the table in your workspace. Review the returned schema, including each column's type and required status, before you use the table in a recipe.

## Update an existing table

Finance needs to identify contracts that renew automatically. Add an optional `auto renew` column to the existing `Vendor contracts` table:

```text
Add a column to "Vendor contracts" called "auto renew". Make it a yes/no column, optional, defaulting to no.
```

AIRO reads the current schema before submitting an update. Review the table's schema after the change to confirm that it retained the existing columns and added the new one.

AIRO doesn't populate the optional `auto renew` column for existing rows. Existing rows remain blank until you update them. Update those rows if each existing contract needs a value.

## Add or update records

AIRO Connect can query records but can't create, update, or delete them.

Use one of the following options to add or update records:

- The [Data tables interface](/en/data-tables/user-interface/edit)
- The [Data tables connector](/en/data-tables/data-table-connector) in a recipe
- The [Record manipulation APIs](/en/workato-api/data-tables#record-manipulation-apis), to add, update, or delete individual records
- The [Record import APIs](/en/workato-api/data-tables#record-import-apis), to bulk-add records or replace a table's entire data set; they can't update specific existing rows in place
- The [Developer API MCP server](/en/mcp/developer-api-mcp), if record endpoints are enabled for your API client role

## Query the table

Ask AIRO a plain-language question instead of writing a filter yourself.

```text
Which vendor contracts in "Vendor contracts" renew in the next 30 days and don't auto-renew?
```

AIRO translates the question into a query that uses the renewal date and auto renew columns, then returns matching records. A scheduled recipe using the [Data tables connector](/en/data-tables/data-table-connector) can run the same query and send procurement an alert in Slack or by email before a contract renews automatically.

Contracts created before you added the `auto renew` column have a blank value there, not `false`. Ask AIRO to also match blank values, or backfill the column first, so the query doesn't miss those contracts.

## Limitations

- AIRO Connect can query records but can't create, update, or delete them. The [Developer API MCP server](/en/mcp/developer-api-mcp) can create, update, or delete records if your API client role includes those endpoints.
- Relation columns require an existing target table with a short text or long text column.
- Default values on optional columns don't backfill existing rows.

## Troubleshooting

### AIRO in Workato can't create data tables or change schemas

AIRO can create data tables and change schemas only through an MCP client connected to AIRO Connect. Connect an MCP client, such as Claude Code, Claude Desktop, or Cursor, to continue.

### AIRO can't find the table or field to relate to

Give AIRO the target table's exact name, or ask it to list your data tables. Confirm the resolved target column before you continue; relation columns link to a specific column, not just a table.

### An update removes columns you didn't mean to change

Schema updates replace the complete column list, not only the column you named. Ask AIRO to show the current schema before it submits the update. Confirm that the request includes every existing column.

### AIRO Connect can't manage table records

AIRO Connect can query records but can't create, update, or delete them. Refer to [Add or update records](#add-or-update-records) for record-management options.

---
