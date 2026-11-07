---
url: 'https://docs.workato.com/en/accelerator-elt-pipeline-search.md'
description: >-
  Search for a pipeline from the ELT Pipeline app homepage by control ID,
  creator, date, status, or source to find the pipeline you need.
---

# Search for a pipeline

You can search for a pipeline from the **App homepage**.

1. From the app homepage, select **Search Pipeline**.
   
2. Configure the **Search Pipeline** interface.
   
   <dl><dt>ELT Control ID</dt><dd><em>Optional</em>. This is the pipeline's automatically generated UUID.</dd><dd><dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>9c3b7d37-f960-4ef0-ad8b-045f8c7803bd</code></dd></dl></dd><dt>Created by</dt><dd>Search for the creator using an email address.</dd><dd><dl class="horizontal-dl"><dt>Sample value:</dt><dd>lucy@example.com</dd></dl></dd><dt>Search from</dt><dd><em>Optional</em>. Start date for pipeline creation.</dd><dd><dl class="horizontal-dl"><dt>Sample value:</dt><dd><code>2021-01-04</code></dd></dl></dd><dt>Status</dt><dd>Filter pipelines by their status. Extract pipelines have a unique status.</dd><dd><dl class="horizontal-dl"><dt>Can be one of:</dt><dd><ul><li>Active</li><li>Inactive</li><li>Pending</li><li>Error</li><li>In progress</li><li>Extract</li></ul></dd></dl></dd><dt>Source</dt><dd><em>Optional</em>. Filter pipelines by their source system. Search results depend on sources defined using the <strong>Create pipeline</strong> interface.</dd><dd><dl class="horizontal-dl"><dt>Sample value:</dt><dd>Salesforce</dd></dl></dd></dl>
   
3. Click **Submit**.
   

The ELT Pipeline bot returns the following fields for each pipeline:

- Pipeline name
- ELT control ID
- Created by
- Load type
- Status
- Last successful job URL
- Pipeline created date
- Next run date

> **RETRY BUTTON**
> 
> The **Search pipeline** output truncates to the top five (5) search results. Click the **Retry** button to search again with different criteria.

## Pin a pipeline

You can only pin pipelines after searching for them. To pin a pipeline to your home page, select the **Follow** button.

You can edit and activate or deactivate a pinned pipeline using the [view](/en/accelerator-elt-pipeline-edit) interface.

---
