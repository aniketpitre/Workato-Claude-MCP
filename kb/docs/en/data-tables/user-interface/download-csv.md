---
url: 'https://docs.workato.com/en/data-tables/user-interface/download-csv.md'
description: >-
  Download a Workato data table from the data tables interface as a CSV file to
  export your table data for use outside Workato.
---

# Download a new table as CSV

Complete the following steps to download a data table from the **Data tables** interface as a CSV file:

1. Select the data table you plan to download.
   
2. Click **Download as CSV**.
   
   ![Data tables Download](/assets/download-csv.CuGUa2Qz.png)_**Download as CSV**_
   
3. The system downloads the CSV file as `data_table_{name}.csv`. The `{name}` matches the data table name, with spaces replaced by underscores (`_`).
   

## Downloaded CSV characteristics

The **Download as CSV** feature exports data exactly as it appears in the **Data tables** interface. The downloaded CSV file reflects the data and formatting visible in the table. The following characteristics apply:

- Date and datetime formatting
  
- Dates use the format `YYYY-MM-DD`. Datetimes use the format `YYYY-MM-DD hh:mm:ss.sss`. Both formats follow the workspace timezone.
  
- Escaped values
  
- Values starting with `=` are prefixed with a single quote (for example, `'=10530`) to prevent spreadsheet formulas.
  
- Comma-containing values
  
- Values with commas, such as `"33 Main Rd, USA 01349"`, are enclosed in double quotes (`"`).
  
- Boolean representation
  
- Boolean values appear as `true` or `false`.
  
- Visible columns only
  
- The export includes only the columns currently visible in the data table.
  
- Column order
  
- The order of columns in the CSV matches the column order displayed in the data table.
  
- Multi-value columns
  
- Multi-value columns are exported as JSON strings. For example:
  
  ```csv
  Name,Apps Provisioned
  Stepan,"[""GitHub""]"
  Carly,"[""Jira"",""ServiceNow""]"
  Alex,"[""Jira"",""ServiceNow"",""Confluence""]"
  Gleb,"[""GitHub"",""Jira""]"
  Mike,"[""Workday""]"
  Andrey,"[""Box""]"
  ```

---
