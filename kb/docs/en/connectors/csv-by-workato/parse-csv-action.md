---
url: 'https://docs.workato.com/en/connectors/csv-by-workato/parse-csv-action.md'
description: >-
  This action parses a CSV-formatted string into an array of lines for use in
  recipes.
---

# CSV tools by Workato - Parse CSV action (batch)

The **Parse CSV** batch action parses a CSV-formatted string into an array of lines. Each line becomes a row of datapills you can use in recipe steps. This action can extract tabular data from plain text and automate imports, transformations, and data transfers across systems.

## Input

| Input fields | Description |
| --- | --- |
| CSV contents | Paste the raw CSV string or map a File content datapill. **A maximum of `50,000` lines is supported.** |
| Column delimiter | Select the character that separates columns in the CSV file. Defaults to **comma**. |
| CSV contents contain header line? | Set to **Yes** if the first row of the CSV is a header and should not be parsed as data. |
| Header schema | Enter the column names that define the structure of the CSV. Click **Add column name** to add each column. Alternatively, use a sample CSV file to populate all headers at once. |
| Keep track of columns by | Choose **Column order** if your CSV has a fixed column order. Choose **Column name** if your CSV has fixed column names but not a fixed order. |
| Quote character | Select the character used to quote cell values. Set to **None** if no quote character is used. |
| Encoding of the file content | Specify the encoding format. Defaults to **UTF-8** if left blank. |

## Output

| Output fields | Description |
| --- | --- |
| Lines | An array of lines parsed from the CSV content. Each line contains columns mapped according to the provided header schema. |

### Example usage

This example recipe monitors Dropbox for new or updated CSV files. When a new or updated file is detected, the recipe downloads the file contents and uses the **Parse CSV** action to extract structured rows from the raw text. Each row contains product data, such as `Model`, `Unit Cost`, and `Tax` information. The recipe then loops through each row and creates a new inventory item in NetSuite.

![Parse CSV](/assets/download-file-and-parse-csv.Bya-WACD.png)_Recipe that parses a CSV file and creates inventory items in NetSuite. View the [sample recipe](https://www.workato.com/recipes/492685)._

---
