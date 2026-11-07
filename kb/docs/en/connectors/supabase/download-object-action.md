---
url: 'https://docs.workato.com/en/connectors/supabase/download-object-action.md'
description: >-
  Download a file from a Supabase storage bucket, as a public or authenticated
  download.
---

# Supabase - Download object action

The **Download object** action downloads a file from a storage bucket in Supabase.

## Input

| Input field | Description |
| --- | --- |
| Bucket | Select the storage bucket that holds the file. |
| Path | Enter the full path to the file inside the bucket, for example `folder/file.png`. |
| Public | Optional. Select **Yes** if the file is publicly accessible, or **No** to download with connection credentials. Defaults to **No** if left blank. |
| Save as | Optional. Enter the filename used when the browser saves the file, for example `report.pdf`. |

## Output

| Output field | Description |
| --- | --- |
| Content | The downloaded file's raw bytes. |
| Content type | The file's MIME type. The **Content type** field is only available when Supabase's response includes a `Content-Type` header. |

---

---
url: >-
  https://docs.workato.com/en/connectors/supabase/insert-or-upsert-rows-action.md
description: >-
  Insert one or more rows into a Supabase table, with an optional upsert when a
  unique key already exists.
---

# Supabase - Insert or upsert rows action

The **Insert or upsert rows** action inserts one or more rows into a table in Supabase, with an optional upsert when a unique key already exists.

## Input

Input fields dynamically generate based on the table you select.

| Input field | Description |
| --- | --- |
| Table | Select the table or view in the Supabase project. |
| Rows | Enter one or more rows to insert or upsert. |
| Resolution | Optional. Select whether to merge new values into the existing row or ignore the insert on a conflict. Requires **On conflict** columns. |
| On conflict | Optional. Select the unique column(s) for upsert conflicts. The **On conflict** field is required when **Resolution** is set. |
| Apply defaults for missing columns | Optional. Select **Yes** to use database defaults for blank columns, or **No** to leave blank columns unset. Defaults to **No** if left blank. |
| Select | Optional. Select the columns to return. Leave blank to return all columns. |

## Output

Output fields dynamically generate based on the table you select.

| Output field | Description |
| --- | --- |
| Rows | The inserted or upserted rows. |
| Location | The inserted row's URL. The **Location** field is only available when Supabase's response doesn't include row data. |

---
