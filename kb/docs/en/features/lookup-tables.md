---
url: 'https://docs.workato.com/en/features/lookup-tables.md'
description: >-
  Lookup tables let Workato recipes store, reference, and manage frequently used
  data in a table of entry rows and value columns, like a cross-reference.
---

# Lookup tables

Lookup tables enable recipes to efficiently store, reference, and manage frequently used data using a table of entry rows and value columns, similar to a cross-reference table.

The **Lookup tables** page enables you to manually create, delete, update, and parse tables.

The **Lookup tables by Workato** connector enables you to create recipes that add, update, delete, and retrieve information about entry rows, as well as delete tables.

> **FEATURE AVAILABILITY**
> 
> The Lookup tables feature is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.
> 
> You must have one of the following to access the **Lookup tables** page:
> 
> - The [Lookup tables privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#environment-privileges).
> - The [**Environment admin**](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) or [**Environment manager**](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-manager) role.
> - The legacy [**Admin** or **Analyst** system role](/en/roles#system-roles) in workspaces using the legacy permissions model.
> 
> Collaborators without access to the **Lookup tables** page can still interact with Lookup tables through the **Lookup tables by Workato** connector if the recipe is within the table's [scope](#assign-to-project).

![Lookup table with timezones, times, and offsets](/assets/example-lookup-table.DFGH_K3a.png)_A Lookup table with timezones, times, and offsets_

## Usage inspiration

The following are examples of lookup table use cases:

- Look up zip codes using city names.
- Convert metric measurements to imperial for a downstream app.
- Create a cache for transient information such as business processes.
- Store frequently used static data to reduce API `GET` request costs.
- Store frequently used static data from slow or non-performant `GET` APIs.

> **INCOMPATIBLE USE CASES**
> 
> Lookup tables are not designed for the following use cases:
> 
> - **Relational database solution**: Lookup tables have enforced quotas, so they do not work as long-term, large relational databases.
> - **Large data in a single cell**: Do not store values larger than 10 kilobytes in a single lookup table cell.

* * *

## Lookup table quotas

Lookup tables have the following quotas:

| Description | Quota | Notes |
| --- | --- | --- |
| Maximum number of lookup tables in a workspace | 100 | NA |
| Maximum number of columns in a lookup table | 10 | NA |
| Maximum number of rows in a lookup table | 100,000 | The Lookup tables connector **Get all entries** action retrieves only the first 10,000 entries.; Tables with more than 50,000 entries can't be downloaded as a CSV file. |
| Maximum row size | 128 KB | NA |
| Maximum number of rows in a lookup table in Recipe lifecycle management imports and exports | 10,000 | NA |
| Maximum file size for a lookup table imported through Recipe lifecycle management | 10 MB | This quota applies independently of the row count quota. A lookup table can exceed 10 MB with fewer than 10,000 rows when rows contain large values. Imports that exceed this quota are blocked before the diff screen appears. |
| Maximum batch size in lookup table connector actions | 10,000 | This quota applies to the following connector actions: **Add entries (batch)** action, **Get all entries (batch)** action |

* * *

## Control Lookup table access

Control access to your workspace's Lookup tables using the following methods:

- [Modify collaborator roles](#role-permissions)
- [Scope Lookup tables](#assign-to-project) to specific projects

### Role-based access control for Lookup tables

You can use [role-based access control](/en/user-accounts-and-teams/role-based-access/#how-role-based-access-control-works) to manage access to the **Lookup tables** page.

Complete the following steps to modify a collaborator role's Lookup table privileges:

1. Go to **Workspace admin > Access control > Environment roles**.
   
2. Select the role you plan to modify or click **\+ Add environment role**.
   
3. Go to **Platform tools > Data storage**.
   
4. In the **Lookup tables** row, select the [privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#data-storage) to assign the role. ![Privileges for data storage](/assets/permissions-data-storage.B7iMMPfS.png)_Lookup table privileges_
   
5. Click **Save changes**. ![Save changes to role](/assets/save-changes-to-role._732gb6C.png)_Save changes to role_
   

> **SCOPE OF LOOKUP TABLE PRIVILEGES**
> 
> Role-based access control only manages access to the **Lookup tables** page. Collaborators can still interact with Lookup tables that are [scoped to projects they have access to](#assign-to-project) through the **Lookup tables by Workato** connector.

### Assign Lookup tables to specific projects

By default, Lookup tables are accessible from all projects. You can limit the scope to make a Lookup table accessible only within a specific project. Once scoped, the table is visible only to collaborators with [access to that project](/en/user-accounts-and-teams/role-based-access/access-control-v2#manage-project-access-and-roles).

Complete the following steps to restrict a Lookup table to a specific project:

1. Go to **Tools > Lookup tables**.
   
2. Select the Lookup table you plan to scope.
   
3. Click **Available in** to open the **Update availability** dialog. ![Update Lookup table scope](/assets/specify-table-scope.DZfRgv5M.png)_Update the scope of a Lookup table_
   
4. Use the **Choose a project** drop-down menu to restrict the Lookup table's access to a specific project.
   
5. Click **Update availability**.
   
6. Use [role-based project access](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-privileges) to restrict which collaborators can access the project.
   

> **CHANGING SCOPE CAN AFFECT RUNNING RECIPES**
> 
> Changing the scope of a Lookup table can affect its availability within currently running recipes.

HOW TO VIEW THE LOOKUP TABLES A USER CAN ACCESS USING THE CONNECTOR

1. Sign in to Workato as a user with the collaborator role you plan to check.
   
2. Open a project.
   
3. Create a new recipe. You can select **Run on a schedule** as your starting point.
   
4. Click **\+ Add step** and select **Action in app**.
   
5. Search for and select `Lookup tables by Workato` in the **Choose an app** search box.
   
6. Select any action.
   
7. Select the **Lookup table** drop-down menu to see which Lookup tables the user can access using the connector. ![Available Lookup tables](/assets/available-lookup-tables.DzMCcw6t.png)_Available Lookup tables_
   

* * *

## Set up your Lookup table

Complete the following steps to create a new Lookup table:

1. Go to **Tools > Lookup tables**.
   
2. Click **\+ New table**.
   
3. Click **Edit** (pencil icon) to enter a name for the Lookup table, and click **✓ Save** to save your changes.
   
4. Click **Import CSV** to upload a CSV file with a header row that defines the column names and structure for the Lookup table, or click **Add entries manually** to add entries directly.
   
5. Click **✓ Save** when finished.
   
   ![Save button highlighted in lookup table entry](/assets/save-button.CsQn4iQo.png)
   

* * *

## Add and update Lookup table data

You can add and edit Lookup table entries using the following methods:

- [Import a CSV file](#import-csv-file)
- [Add them manually, one at a time](#manual-changes)
- [Use a recipe action](#recipe-actions)

### Import a CSV file

Complete the following steps to import a CSV file into a Lookup table:

1. Go to **Tools > Lookup tables** and click **\+ New table**.
   
2. Click **Import CSV**.
   
3. In the **Specify action** section, select one of the following options:
   
   - **Add row entries**: Workato adds the CSV rows as new entries. Existing entries are not affected.
   - **Replace existing data**: Workato overwrites existing entries with rows from the new CSV file.
   
   ![Import CSV window](/assets/import-csv-window.CHFSmjrm.png)_Import CSV window_
   
4. Drag and drop a CSV file into the **Select CSV file** field, or click **upload from device** and select a CSV file.
   
5. Select the **Do not import the first row (header)** checkbox if you don't plan to import the first row of the CSV.
   
6. Click **Import CSV**.
   

### Add or edit entries manually

**Add entries manually**

Complete the following steps to add a new entry manually:

1. Click **Add entry**:
   
   ![Add entry button in the Lookup tables page](/assets/add-entry-button.BN2XV0fm.png)
   
2. Enter values in each column of the new row.
   
3. Click **✓ Save** when finished.
   
   ![Save button highlighted in Lookup table entry](/assets/save-button.CsQn4iQo.png)
   

**Edit entries manually**

Complete the following steps to edit an existing entry:

1. Hover over the last column in the entry row and click **Edit** (pencil icon) when it appears.
   
   ![Edit entry button in a Lookup table entry](/assets/edit-entry.BvXdV1ZU.png)
   
2. Update the entry row's values.
   
3. Click **✓ Save** when finished.
   

### Use recipe actions

To automatically add and update entries, use the [Add entry](#add-entry-action), [Add entries](#add-entries-action-batch), and [Update entry](#update-entry-action) recipe actions from the **Lookup tables by Workato** connector.

* * *

## Filter Lookup tables by project

Workato supports search filters to quickly find Lookup tables associated with different projects.

Complete the following steps to search Lookup tables using filters:

1. Navigate to **Tools > Lookup tables**.
   
2. Locate the project filter drop-down menu.
   
   ![Project filter](/assets/lookup-filter.CUbZcfpM.png)_Project filter drop-down menu_
   
3. Select the projects to filter Lookup tables by.
   
   ![Filter your projects](/assets/filter-projects.Dd63zRvh.png)_Select projects to filter_
   
4. Click **Apply**.
   

* * *

## Using the Lookup table connector

The **Lookup tables by Workato** connector allows you to interact with Lookup tables using the following recipe actions:

- [Add entry](#add-entry-action)
- [Add entries](#add-entries-action-batch)
- [Lookup entry](#lookup-entry-action)
- [Search entries](#search-entries-action-batch)
- [Get all entries](#get-all-entries-action-batch)
- [Update entry](#update-entry-action)
- [Delete entry](#delete-entry-action)
- [Delete multiple entries](#delete-multiple-entries-action-batch)
- [Truncate table](#truncate-table-action)

### Add entry action

The **Add entry** action adds a new entry to an existing Lookup table.

#### Input

| Field | Description |
| --- | --- |
| Lookup table | Select the Lookup table where you plan to create the entry. |
| Entry fields | This field includes a sub-field for each column in your Lookup table. Provide the contents of your new entry for each column. |

#### Output

| Output | Description |
| --- | --- |
| Entry ID | The ID of the new entry. |
| Entry | This object contains a string for each column of the Lookup table specifying the contents of the new entry. |

### Add entries action (batch)

The **Add entries** action adds new entries to a Lookup table in batches.

#### Input

| Field | Description |
| --- | --- |
| Lookup table | Select the Lookup table where you plan to create new entries. |
| Entries source list | Provide the list datapill that you plan to create entries from. |
| Entry fields | This field includes a sub-field for each column in your Lookup table. Specify the datapill from your list to use for each column in your new entry rows. |

#### Output

| Output | Description |
| --- | --- |
| Count | The number of new entries added to the Lookup table. |

### Lookup entry action

The **Lookup entry** action searches for a Lookup table entry by its column values and returns the first entry that matches the search criteria.

If Workato doesn't find an entry, the recipe returns an `Unable to find an entry matching search parameters` error.

Use the **Lookup entry** action when you expect only one entry to match the search criteria. To retrieve a list of matching entries or check whether specific values exist in a Lookup table, use the **[Search entries](#search-entries-action-batch)** action instead.

#### Input

| Field | Description |
| --- | --- |
| Lookup table | Select the Lookup table where you plan to look up an entry. |
| Search by | This field includes a sub-field for each column in your Lookup table. Provide the criteria to search by in each column. |

> **SEARCH BY MULTIPLE CRITERIA**
> 
> To search a column by multiple criteria in a single operation, switch the **Search by** field to [formula mode](/en/formulas/formula-mode) and input an array of strings in JSON format. The operation will return the first entry that matches one of the strings.

#### Output

| Output | Description |
| --- | --- |
| Entry ID | The ID of the found entry. |
| Entry | This object contains a string for each column of the Lookup table specifying the contents of the found entry. |

### Search entries action (batch)

The **Search entries** action searches for Lookup table entries by their column values and returns a list of all entries that match the search criteria.

Use the **Search entries** action when you expect a Lookup table to return multiple entries or need to check whether specific values exist in a Lookup table.

#### Input

| Field | Description |
| --- | --- |
| Lookup table | Select the Lookup table where you plan to search for entries. |
| Search by | This field includes a sub-field for each column in your Lookup table. Provide the criteria to search by in each column. |

> **SEARCH BY MULTIPLE CRITERIA**
> 
> To search a column by multiple criteria in a single operation, switch the **Search by** field to [formula mode](/en/formulas/formula-mode) and input an array of strings in JSON format. The operation will return a list of the entries that match one of the strings.

#### Output

| Output | Description |
| --- | --- |
| Entry ID | The ID of the found entry. |
| Entry | This object contains a string for each column of the Lookup table specifying the contents of the found entry. |
| List size | The number of entries found. |

### Get all entries action (batch)

The **Get all entries** action returns all entries from a Lookup table.

> **LIMITATIONS**
> 
> The **Get all entries** action returns up to a maximum of 10,000 entries.

#### Input

| Field | Description |
| --- | --- |
| Lookup table | Select the Lookup table you plan to return all entries from. |

#### Output

| Output | Description |
| --- | --- |
| Entry ID | The ID of the entry returned from the Lookup table. |
| Entry | This object contains a string for each column of the Lookup table specifying the contents of the returned entry. |
| List size | The number of entries returned from the Lookup table. |

### Update entry action

The **Update entry** action updates the contents of an existing entry.

#### Input

| Field | Description |
| --- | --- |
| Lookup table | Select the Lookup table where you plan to update an entry. |
| Entry ID | Specify the ID of the entry you plan to update. |
| Ignore if not found | Select whether to stop the job with an error if an entry with the given ID is not found. |
| Entry fields | This field includes a sub-field for each column in your Lookup table. Provide the contents of your entry for each column. |

#### Output

| Output | Description |
| --- | --- |
| Entry ID | The ID of the updated entry. |
| Entry | This object contains a string for each column of the Lookup table specifying the contents of the updated entry. |

### Delete entry action

The **Delete entry** action deletes a single entry from a Lookup table.

#### Input

| Field | Description |
| --- | --- |
| Lookup table | Select the Lookup table where you plan to delete an entry. |
| Entry ID | Specify the ID of the entry you plan to delete. |
| Ignore if not found | Select whether to stop the job with an error if an entry with the given ID is not found. |

#### Output

| Output | Description |
| --- | --- |
| Deleted entry ID | The ID of the deleted entry. |

### Delete multiple entries action (batch)

The **Delete multiple entries** action deletes multiple entries from a Lookup table.

#### Input

| Field | Description |
| --- | --- |
| Lookup table | Select the Lookup table where you plan to delete multiple entries. |
| Delete options | Select whether to delete entries by their IDs or by a search condition. |
| List of entry IDs source list | Provide a list datapill that contains the `Entry ID`s of entries you plan to delete. |
| Entry ID | Specify the datapills within your list that contain the `Entry ID`s of entries you plan to delete. |
| Delete entries | This field includes a sub-field for each column in your Lookup table. Provide the criteria to delete entries by for each column. |

#### Output

| Output | Description |
| --- | --- |
| Count | The number of entries deleted from the Lookup table. |

### Truncate table action

The **Truncate table** action permanently deletes all of a Lookup table's entries.

> **DATA DELETION IS PERMANENT**
> 
> Data deletion _can't be undone_, even if the action is run during a test job.

#### Input

| Field | Description |
| --- | --- |
| Lookup table | Select the Lookup table you plan to delete all entries from. |

#### Output

| Output | Description |
| --- | --- |
| Count | The number of entries deleted from the Lookup table. |

* * *

## Using formulas to look up entries

You can use the `lookup()` formula to perform the [Lookup entry action](#lookup-entry-action) within input fields.

The following template demonstrates how to use the formula:

```ruby
lookup("TABLE_NAME", "REFERENCE_COLUMN": datapill)["LOOKUP_COLUMN"]
```

In this template:

- `TABLE_NAME` is the name of the Lookup table where you plan to look up an entry.
- `REFERENCE_COLUMN` is the name of the column to search for matching values.
- `datapill` is the value the formula will search for in the `REFERENCE_COLUMN`.
- `LOOKUP_COLUMN` is the name of the column to return a value from in the row of the matching entry.

> **IN-MEMORY LOOKUP TABLES**
> 
> Use the **Entries** object, which contains the output of actions such as [**Search entries**](#search-entries-action-batch), in place of `TABLE_NAME` to create an in-memory Lookup table. The in-memory table searches entries more quickly and only searches the reduced list of entries obtained in the initial action. This can help save time when a recipe needs to call the lookup function on the same Lookup table thousands of times.

The following example uses the `Account IDs` table. It looks up the `Intacct account ID` of the first entry that matches the given `Salesforce account ID`:

```ruby
lookup("Account IDs", "Salesforce account ID": datapill)["Intacct account ID"]
```

To search multiple columns, enter additional reference columns within the parentheses and separate them with commas:

```ruby
lookup("TABLE_NAME", "REFERENCE_COLUMN": datapill, "REFERENCE_COLUMN_2": datapill2)["LOOKUP_COLUMN"]
```

---
