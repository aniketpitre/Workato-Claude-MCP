---
url: 'https://docs.workato.com/en/features/sql-transformations-output-fields.md'
description: >-
  Reference for the SQL Transformations Query CSV data action output fields,
  including FileStorage file path, CSV contents, and number of rows.
---

# Output fields

The Query CSV data action has three output fields. You can map these fields into downstream steps by selecting their datapills from the datatree.

<dl><dt>FileStorage file path</dt><dd>Provides the path of the output file. This field is only populated when you choose FileStorage file as the output type.</dd><dt>CSV contents</dt><dd>Provides the output content reference that can be passed to downstream actions to stream the data out. It is functional only when you choose the CSV content stream option as the output type.</dd><dt>Number of rows</dt><dd>Provides the number of rows in the output file.</dd></dl>

## Read next

See our guides for step-by-step instructions on how to leverage SQL Transformations for the following use cases:

- [Change data capture](/en/features/sql-transformations-cdc)
- [Data validation and cleansing](/en/features/sql-transformations-data-validation-cleansing)
- [Data enrichment](/en/features/sql-transformations-data-enrichment)

---
