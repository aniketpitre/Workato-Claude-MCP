---
url: 'https://docs.workato.com/en/workato-api/insights.md'
description: >-
  Reference for the Workato Insights API to discover queryable Insights tables
  and run read-only SQL queries against your workspace data.
---

# Developer API - Insights

Use these endpoints to query [Insights](/en/insights) data with read-only SQL. You can load a weekly usage snapshot into a warehouse, schedule a chargeback report, or investigate the root cause of a usage spike with an AI agent.

## Rate limits

Insights resources have the following rate limits:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Insights](/en/workato-api/insights.html) endpoints | 60 requests per minute |

## Quick reference

| Type | Resource | Description |
| --- | --- | --- |
| GET | [/api/insights/v1/tables](#list-insights-schema-tables) | List the Insights tables the API client can read. |
| POST | [/api/insights/v1/schema](#get-insights-table-columns) | Return the columns of the named Insights tables. |
| POST | [/api/insights/v1/query](#execute-insights-sql-query) | Run a read-only SQL query and return the result as CSV or JSON. |

## How are Insights table names constructed?

Every Insights table has a fully qualified name made of three parts: a catalog, a schema, and the table. A catalog groups related tables. Queries and the [Get Insights table columns](#get-insights-table-columns) endpoint both expect the full name, such as `workato_data.public.recipes`. [List Insights schema tables](#list-insights-schema-tables) returns all three parts for every table it lists, though it doesn't list every table your API client can query. That section explains which tables it leaves out.

Refer to the [Insights data catalog](/en/workato-api/insights-catalog) for each table's columns, row grain, and join keys.

## Run your first query

Complete the following steps to run your first Insights query:

1. Create an [API client](/en/workato-api/api-clients) with a client role granting both privilege groups under **Tools > Insights**:
   
   - **Insights schema** lets the client look up table and column names.
   - **Insights Query** lets the client run queries.
   
   ![Insights privileges in a client role](/assets/insights-client-role-privileges.BAlXTve1.png)_Insights privileges in a client role_
   
   Grant the client access to the projects containing the data you plan to query.
   
2. Call [List Insights schema tables](#list-insights-schema-tables) to see which tables your API client can read.
   
3. Call [Get Insights table columns](#get-insights-table-columns) to see the columns of the tables you plan to query.
   
4. Call [Execute Insights SQL query](#execute-insights-sql-query) with your `SELECT` statement. Give every table its fully qualified name, for example `workato_data.public.recipes`. Leave `output_format` unset to get CSV, or set it to `json` to get column types with the result.
   
5. Check the truncation flag on the response. Narrow the query with filters or a shorter time range and run it again if the row cap cut the result. Refer to [Query limits](#query-limits) for more information.
   

## List Insights schema tables

Returns the names of the Insights tables available to the API client. Call this before you write a query, then call [Get Insights table columns](#get-insights-table-columns) for the columns of the tables you plan to use.

<api-code no-copy-method>

```
GET https://YOUR_DATA_CENTER/api/insights/v1/tables
```

</api-code>

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| catalog | **string** _optional_ | Return only the tables in this catalog. Use the catalog name as it appears in SQL. Refer to [Catalogs](#catalogs) below for the full list. |

The response leaves out data tables (`workato_db`) and Workflow apps tables (`lcap`) unless you name their catalog, for example `/api/insights/v1/tables?catalog=workato_db`. Custom job report tables (`job_history`) aren't listed by this endpoint, as each custom job report table is named dynamically per recipe. Refer to [Custom job report tables](#get-columns-of-a-custom-job-report-table) for more information.

### Catalogs

The `catalog` parameter accepts the following names:

| Catalog | Contains |
| --- | --- |
| `workato_data` | Core workspace structure: projects, recipes, folders, connections, and environments. |
| `users` | Workspace collaborators and embedded end users and end-user groups. |
| `usage` | Billing periods and plan usage/consumption figures. |
| `audit_log` | Compliance and activity events: logins, membership and role changes, recipe and connection updates. |
| `api_platform` | API Platform collections, endpoints, clients, keys, policies, and gateway request events. |
| `mcp` | MCP servers, tools, and gateway request events. |
| `data_orchestration` | Data pipelines and their run history. |
| `job_history_all` | Job history across every recipe. |
| `job_history` | Each recipe's own custom job report, named dynamically per recipe. There's no fixed list of these tables for this endpoint to return. Refer to [Custom job report tables](#get-columns-of-a-custom-job-report-table). |
| `workato_db` | Data tables. Each workspace's tables have their own columns, so there's no catalog-wide schema. Excluded by default unless named. |
| `lcap` | Workflow apps tables. Each app's tables have their own columns, so there's no catalog-wide schema. Excluded by default unless named. |

### Sample request

This request returns the Insights tables the API client can read.

<api-code>

```shell
curl -X GET https://YOUR_DATA_CENTER/api/insights/v1/tables \
     -H 'Authorization: Bearer <api_token>'
```

</api-code>

### Sample response

Each entry gives the three parts of the table's name, plus a `label` for display.

```json
{
  "data": {
    "tables": [
      {
        "catalog": "workato_data",
        "schema": "public",
        "table": "recipes",
        "label": "Recipes"
      },
      {
        "catalog": "workato_data",
        "schema": "public",
        "table": "projects",
        "label": "Projects"
      },
      {
        "catalog": "job_history_all",
        "schema": "public",
        "table": "job_history_all",
        "label": "Job History"
      }
    ]
  }
}
```

> **PARTIAL RESULTS ARE RETURNED WITHOUT NOTICE**
> 
> When a data source is temporarily unavailable, a request without `catalog` can return `200` with that source's tables omitted. The response doesn't have a completeness flag. If an expected table is missing, retry with `?catalog=<catalog>` or call the schema endpoint with the table name. These targeted requests return `503` on a recoverable source failure. Retry with backoff, then check feature availability and API client access if the table is still missing.

### Data scope

An API client reads data from its workspace. What it sees across that workspace depends on the source:

- **Workspace-scoped sources**: usage, API logs, compliance and activity logs, and integration data, such as projects, recipes, and jobs. A client role that includes the Insights privileges reads these across every environment in the workspace, not only the environment the token was created in. There isn't a per-source setting. For example, a platform admin can use one token to compare usage across environments and check whether a spike followed a deployment.
- **Project-scoped sources**: data tables and custom job reports. These are filtered to the projects the API client can access, using the same project access check as the rest of the Developer API.

A query that references a table outside that scope returns a `400`.

The `usage` catalog can widen beyond a single workspace, depending on the token. An Automation HQ or Embedded admin workspace token can aggregate billing and usage data across its managed or customer workspaces. A standalone or child workspace token still sees only its own workspace. Refer to [Usage and billing](/en/workato-api/insights-catalog#usage-and-billing) for how each `usage` table scopes that aggregation.

## Get Insights table columns

Returns the columns of the tables you name. Call [List Insights schema tables](#list-insights-schema-tables) first to find the table names.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/insights/v1/schema
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| tables | **array** _required_ | Fully qualified table names, each `catalog.schema.table`. Accepts at most 20 names in one request. |

### Sample request

This request asks for the columns of the `recipes` table, and of a table name that doesn't exist, to show the `not_found` field in the response.

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/insights/v1/schema \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "tables": ["workato_data.public.recipes", "workato_data.public.not_a_real_table"]
         }'
```

</api-code>

### Sample response

The response repeats the table's name and lists each of its columns with that column's type.

View response

```json
{
  "data": {
    "tables": [
      {
        "catalog": "workato_data",
        "schema": "public",
        "table": "recipes",
        "label": "Recipes",
        "columns": [
          {
            "name": "id",
            "label": "ID",
            "data_type": "BIGINT"
          },
          {
            "name": "name",
            "label": "Name",
            "data_type": "VARCHAR"
          },
          {
            "name": "project_id",
            "label": "Project ID",
            "data_type": "BIGINT"
          },
          {
            "name": "folder_id",
            "label": "Folder ID",
            "data_type": "BIGINT"
          },
          {
            "name": "environment_id",
            "label": "Environment ID",
            "data_type": "BIGINT"
          },
          {
            "name": "is_active",
            "label": "Is Active",
            "data_type": "BOOLEAN"
          },
          {
            "name": "recipe_type",
            "label": "Type",
            "data_type": "VARCHAR"
          },
          {
            "name": "created_at",
            "label": "Created at",
            "data_type": "TIMESTAMP"
          },
          {
            "name": "updated_at",
            "label": "Updated at",
            "data_type": "TIMESTAMP"
          },
          {
            "name": "tags",
            "label": "Tags",
            "data_type": "ARRAY<VARCHAR>"
          },
          {
            "name": "applications",
            "label": "Applications",
            "data_type": "ARRAY<VARCHAR>"
          },
          {
            "name": "trigger_application",
            "label": "Trigger Application",
            "data_type": "VARCHAR"
          }
        ]
      }
    ],
    "not_found": ["workato_data.public.not_a_real_table"]
  }
}
```

A column's `data_type` is one of the following:

- **Primitive types**: `BOOLEAN`, `DATE`, `TIMESTAMP`, `BIGINT`, `DOUBLE`, `VARCHAR`
- **Array types**: `ARRAY<VARCHAR>`, `ARRAY<BIGINT>`
- `UNKNOWN`

A table that doesn't exist, or that the API client can't access, is returned in `not_found` instead of raising an error.

### Custom job report tables

Each recipe's [custom job report](/en/recipes/jobs#customizing-job-reports) has its own table, which the table-listing endpoint doesn't return. `job_history_all` lists recipes that have run jobs, not specifically recipes with a custom job report. Confirm a specific recipe has a custom job report by opening the job details page, selecting **Customize job report**, and checking whether columns are already mapped.

Complete the following steps to get the table's columns:

1. Find the recipe's ID. The `recipe_id` column of `job_history_all.public.job_history_all` lists recipe IDs. For example, run the following through `POST /api/insights/v1/query`:
   
   ```sql
   SELECT DISTINCT recipe_id FROM job_history_all.public.job_history_all
   ```
   
2. Build the table name `job_history.public.RECIPE_ID`, replacing `RECIPE_ID` with that ID.
   
3. Pass the name to the `tables` payload of `POST /api/insights/v1/schema`, for example `job_history.public.1127731`. Pass the ID without quotes, as the payload is a JSON string, not SQL.
   

The response labels the table with the recipe's own name instead of a generic name.

To reference the table in a SQL query instead, quote the recipe ID, as it's numeric: `SELECT job_handle FROM job_history.public."1127731" LIMIT 10`.

## Execute Insights SQL query

Runs a read-only SQL query against any table whose columns [Get Insights table columns](#get-insights-table-columns) can return, including custom job report tables that [List Insights schema tables](#list-insights-schema-tables) doesn't list. Returns the result as CSV or JSON.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/insights/v1/query
```

</api-code>

### Payload

| Name | Type | Description |
| --- | --- | --- |
| sql | **string** _required_ | The SQL query to run. Must not be blank, and must be 10,000 characters or fewer. Refer to [Supported SQL](#supported-sql) for the accepted syntax. |
| output\_format | **string** _optional_ | The format of a successful result. Accepts `csv` or `json`. Defaults to `csv` if left blank. Error responses are JSON regardless of `output_format`. |

`output_format` is the only way to choose the response format. Setting an `Accept` header, such as `Accept: text/csv`, doesn't have an effect, and neither does adding a file extension to the URL, such as `/api/insights/v1/query.csv`.

### Sample requests

This section includes the following examples:

- **Example 1: Active recipes**: returns the ID and name of every active recipe, as JSON, to show the column types alongside the result.
- **Example 2: Investigate a recipe failure**: joins `job_history_all` to `recipes` to see which recipes failed in the last seven days and why, as CSV, which is the default if you omit `output_format`.

Example 1: Active recipes

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/insights/v1/query \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "sql": "SELECT id, name FROM workato_data.public.recipes WHERE is_active = true",
           "output_format": "json"
         }'
```

</api-code>

Example 2: Investigate a recipe failure

Use a quoted heredoc so the single quotes in `INTERVAL '7' DAY` reach the SQL parser instead of closing the shell string:

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/insights/v1/query \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     --include \
     -d @- <<'EOF'
{
  "sql": "SELECT r.name AS recipe_name, j.started_at, j.completed_at, j.error_type, j.error_message FROM job_history_all.public.job_history_all j JOIN workato_data.public.recipes r ON j.recipe_id = r.id WHERE j.is_complete_success = false AND j.completed_at >= CURRENT_TIMESTAMP - INTERVAL '7' DAY AND j.completed_at < CURRENT_TIMESTAMP ORDER BY j.completed_at DESC LIMIT 10"
}
EOF
```

</api-code>

### Sample responses

JSON output returns the columns, the rows, and the truncation flag. Each row is an array of values in column order. Each entry in `columns` has:

- `qualifier`: the column's SQL name, or the alias a query gives it.
- `label`: derived from `qualifier`, with the first letter capitalized, the rest lowercased, and underscores replaced with spaces.
- `hints`: how the column was computed. `AggregateResult` marks a `GROUP BY` key or aggregate value, `AggregateFunction` names the function applied, for example `SUM`, and `TruncatedDate` marks a date truncated to an interval, such as `DAY` or `MONTH`. A plain `SELECT` with no `GROUP BY` or aggregate function returns `[]`.

Example 1: Active recipes

```json
{
  "data": {
    "columns": [
      {
        "qualifier": "id",
        "label": "Id",
        "type": "BIGINT",
        "hints": []
      },
      {
        "qualifier": "name",
        "label": "Name",
        "type": "VARCHAR",
        "hints": []
      }
    ],
    "data": [
      [1, "Order sync"],
      [2, "Invoice reconciliation"]
    ],
    "has_more_rows": false
  }
}
```

Example 2: Investigate a recipe failure

`--include` prints the response headers above the body, confirming the default content type and the truncation header (some headers omitted below for brevity):

```
HTTP/1.1 200 OK
Content-Type: text/csv; charset=utf-8
X-Workato-Has-More-Rows: false

recipe_name,started_at,completed_at,error_type,error_message
"Greenhouse to Workday sync","2026-11-14T09:03:11.000+00:00","2026-11-14T09:03:12.400+00:00","Connection error","Timed out connecting to Workday"
"Greenhouse to Workday sync","2026-11-13T09:03:10.000+00:00","2026-11-13T09:03:10.850+00:00","Line input evaluation error",
```

### CSV output

CSV is the default `output_format`. This example sets it explicitly and adds `--include` to show the response headers:

<api-code>

```shell
curl -X POST https://YOUR_DATA_CENTER/api/insights/v1/query \
     -H 'Authorization: Bearer <api_token>' \
     -H 'Content-Type: application/json' \
     --include \
     -d '{
           "sql": "SELECT id, name, applications FROM workato_data.public.recipes",
           "output_format": "csv"
         }'
```

</api-code>

The response is UTF-8 CSV. The header row repeats the `qualifier` of each column from the JSON response, and each line after it is one row (some headers omitted below for brevity):

```
HTTP/1.1 200 OK
Content-Type: text/csv; charset=utf-8
X-Workato-Has-More-Rows: false

id,name,applications
1,"Order sync","[""Shopify"",""NetSuite""]"
2,"Invoice reconciliation","[""NetSuite"",""Workday""]"
```

CSV output differs from JSON output in the following ways:

- Array and object values are written as JSON.
- Null values are empty cells, and empty strings are written as `""`.
- Column types aren't included. The JSON response carries a `type` for every column, and CSV drops it, so a downstream consumer such as a warehouse loader must re-type the columns itself. Run the same query with `output_format` set to `json` to read the types.
- Truncation is reported through the `X-Workato-Has-More-Rows` response header rather than `data.has_more_rows`.

## Supported SQL

Queries run against a supported subset of ANSI SQL:2003. Joins, `GROUP BY`, aggregate functions, `CASE` expressions, common table expressions, and subqueries are supported. Catalog, schema, and table names must match the case returned by `GET /api/insights/v1/tables` and `POST /api/insights/v1/schema` exactly. A different case fails to resolve the object. Wrap an identifier in double quotes if it contains non-alphanumeric characters or starts with a digit, such as a custom job report table named after a recipe ID.

### Statement types

Only `SELECT` statements are accepted, including the `UNION`, `INTERSECT`, and `EXCEPT` set operations. `MINUS`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `ALTER`, `EXECUTE`, and `CALL` are rejected.

### Restrictions

Every query is validated before it runs, so a query that breaks one of the following restrictions is rejected without executing:

- A query must resolve to a single flat result. Common table expressions and subqueries are supported, as they still produce one flat result.
  
- Table functions, such as `TABLE()` expressions, are rejected. `UNNEST` isn't affected. Use it with `CROSS JOIN` to flatten an array column, for example:
  
  ```sql
  SELECT r.id, t.tag FROM workato_data.public.recipes r CROSS JOIN UNNEST(r.tags) AS t(tag)
  ```
  
- Queries can't read the query engine's internal metadata tables, such as `information_schema`.
  

### Allowed functions

The following functions are permitted. A rejected function is named in the error, so you know which function to remove:

`AVG`, `CAST`, `CEILING`, `CHAR_LENGTH`, `COUNT`, `COUNT_IF`, `CURRENT_TIMESTAMP`, `DATE_TRUNC`, `EXTRACT`, `FLOOR`, `LOWER`, `MAX`, `MIN`, `MOD`, `NULLIF`, `POSITION`, `REPLACE`, `ROUND`, `SUBSTRING`, `SUM`, `TRIM`, `UPPER`

This excludes window functions, such as `ROW_NUMBER` and `RANK`. Window functions are rejected the same way as any other disallowed function.

## Query limits

The query service caps each result at 5,000 rows and there is no pagination. A result that hits the cap says so instead of truncating silently:

- JSON output sets `data.has_more_rows` to `true`.
- CSV output sets the `X-Workato-Has-More-Rows` response header to `true`.

The API doesn't have a cursor or continuation token for paging past the cap. `ORDER BY ... LIMIT ... OFFSET ...` and `OFFSET ... ROWS FETCH NEXT ... ROWS ONLY` both run, but they only pick which rows within the 5,000-row result the query returns, not how much underlying data it scans, so they can't retrieve rows beyond the cap either. Narrow the query rather than paging to get the rest of the data. Add filters, shorten the time range, or pre-aggregate in the `SELECT` so the result fits under the cap.

A query that passes validation can still exceed the resource quotas that govern execution, or run longer than the query service allows, such as with an unbounded time range, an expensive join, or a slow-planning query. These return a `422` with `retryable` set to `false`. Narrow the query instead of retrying.

The `sql` value is capped at 10,000 characters. A longer query returns a `400` without running.

## Error responses

The Insights API returns errors in the following formats:

### Error format

Most errors return an `errors` array. Each error includes a `code` and a `title`, and can include a `detail` field and a `retryable` flag. For a query the query service rejects, `detail` can start with the line and column range of the problem in your SQL, followed by what's wrong and how to discover the correct tables and columns:

```json
{
  "errors": [
    {
      "code": 400,
      "title": "Query rejected",
      "detail": "Object 'foo' not found Use GET /insights/v1/tables to list the available tables (with catalog=workato_db or catalog=lcap for data tables and app tables) and POST /insights/v1/schema to get their columns.",
      "retryable": false
    }
  ]
}
```

`retryable` is present on errors raised by the query service. `true` means sending the identical query again can succeed on its own, such as after a throttled request or a data source that temporarily didn't respond. `false` means don't automatically retry the identical request. The fix depends on the error code and isn't always a change to the SQL itself. Refer to [Error codes](#error-codes) for what each code means. The flag is omitted on framework errors, such as rate limits and parameter validation.

Use `retryable` to decide whether to retry at all. When a `429` response includes a `Retry-After` header, use it to decide how long to wait before that retry. A `429` response without `Retry-After` can still be retried.

Error responses are JSON regardless of `output_format`, including when it's set to `csv`.

#### Unauthorized and parameter errors

`401` errors return a `message` field instead of an `errors` array. These responses can also include `details` and `reason` fields. `reason` is `authentication_failed` when the token is missing or invalid, and `missing_privilege` when the client role lacks the privilege for the endpoint:

```json
{
  "message": "Unauthorized",
  "reason": "missing_privilege"
}
```

The `sql` parameter missing from the request entirely returns a `message` field instead:

```json
{
  "message": "Missing parameter sql"
}
```

An empty `sql` value, or any other invalid parameter, returns an `errors` array instead, with a `code` and a `title` and no `retryable` flag:

```json
{
  "errors": [
    {
      "code": 400,
      "title": "sql is required"
    }
  ]
}
```

### Error codes

The Insights API returns the following error codes:

| Code | Description |
| --- | --- |
| 400 | Bad request, with `retryable` `false`: the query service rejected the SQL (syntax error, disallowed operation, unknown table or column). `retryable` is omitted instead for a framework parameter-validation error: a missing, blank, or over-10,000-character `sql`, a malformed JSON request body, or an invalid `output_format`. Narrow the query based on the error `detail` rather than retrying. |
| 401 | Unauthorized. The API token is missing or invalid, or the client role lacks the privilege for the endpoint. Refer to [Run your first query](#run-your-first-query) for the privileges each endpoint needs. |
| 409 | Conflict. The data source no longer matches the schema the query was written against. Changing the SQL doesn't resolve it. `retryable` is `false`. |
| 422 | The query is valid but couldn't be executed, such as when it exceeds the resource quotas or runs longer than allowed. `retryable` is `false`. Narrow the query rather than retrying it unchanged. |
| 429 | Too many requests. The query service throttled the query, in which case `retryable` is `true` and no `Retry-After` header is sent, or the API rate limit is exceeded, in which case the `Retry-After` header indicates when you can retry. |
| 500 | Internal server error. The query service failed, or an unexpected error occurred in the API framework. The `title` includes an error ID. `retryable` is `false` for query service errors. |
| 502 | The query service returned a response the API framework couldn't use. `retryable` is `false`. |
| 503 | The query service is temporarily unavailable, or a data source didn't respond to a catalog-filtered `GET /api/insights/v1/tables` request or to `POST /api/insights/v1/schema`. `retryable` is `true`. |
| 504 | The query service didn't respond before the gateway timed out. `retryable` is `true`. Retry with backoff. |

## Query Insights through the Developer API MCP

Use the [Developer API MCP server](/en/mcp/developer-api-mcp) to query Insights from an MCP client. A client role that includes the Insights privileges provides three tools, one for each endpoint: [List Insights schema tables](#list-insights-schema-tables), [Get Insights table columns](#get-insights-table-columns), and [Execute Insights SQL query](#execute-insights-sql-query).

The query tool returns JSON, regardless of `output_format`. Check `data.has_more_rows` to detect a truncated result.

---
