---
url: 'https://docs.workato.com/en/connectors/supabase/search-objects-action.md'
description: >-
  Search files in a Supabase storage bucket by folder prefix, name filter, and
  sort order.
---

# Supabase - Search objects action

The **Search objects** action searches files in a storage bucket in Supabase by folder prefix and name filter.

## Input

| Input field | Description |
| --- | --- |
| Bucket | Select the storage bucket to search. |
| Prefix | Optional. Enter the folder path to search, for example `invoices/`. Leave blank for the bucket root. |
| Limit | Optional. Enter the maximum number of objects to return. Valid values are 1-1000. The default is `100`. |
| Offset | Optional. Enter the number of objects to skip. The default is `0`. |
| Search | Optional. Enter a case-sensitive substring to filter by object name, for example `logo.png`. |
| Sort by | Optional. Sort settings for the searched objects. |
| Column (Sort by) | Select the property to sort by. Options are **Name**, **Updated at**, **Created at**, or **Last accessed at**. |
| Order (Sort by) | Select the sort direction. |

## Output

The following are a representative set of output fields. Refer to the Supabase [Storage](https://supabase.com/docs/guides/storage) documentation for a list of output fields.

| Output field | Description |
| --- | --- |
| Objects | The matching files. |
| Name (Objects) | The file's full path within the bucket. |
| ID (Objects) | The file's unique identifier. |
| Bucket ID (Objects) | The bucket the file belongs to. |
| Updated at (Objects) | The date and time the file was last updated. |
| Created at (Objects) | The date and time the file was created. |
| Metadata (Objects) | The file's storage metadata. |
| Size (Metadata) | The file's size, in bytes. |
| MIME type (Metadata) | The file's MIME type. |

---
