---
url: 'https://docs.workato.com/en/connectors/pipedrive-custom/new-record-trigger.md'
description: The New record trigger activates when a record is created in Pipedrive.
---

# Pipedrive - New record trigger

The **New record** trigger monitors Pipedrive for newly created records.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to monitor for new instances. |

## Output

| Output field | Description |
| --- | --- |
| Data | Contains information about the current state of the object. |
| ID | A unique identifier for the object. |
| Name | The name of the object. |
| Order number | The sequence number of the object. |
| Is deleted | Indicates whether the object was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for this object. |
| Add time | A timestamp indicating when this object was created. |
| Update time | A timestamp indicating when this object was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |
| Previous | Contains information about the previous state of the object. |
| ID | A unique identifier for the object. |
| Name | The name of the object. |
| Order number | The sequence number of the object. |
| Is deleted | Indicates whether the object was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for this object. |
| Add time | A timestamp indicating when this object was created. |
| Update time | A timestamp indicating when this object was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |
| Meta | Metadata about the newly created object. |

> **VARIABLE OUTPUT**
> 
> The **New record** trigger's output fields vary based on your selected **Object** type.

---

---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/updated-record-trigger.md
description: The Updated record trigger monitors Pipedrive for updated records.
---

# Pipedrive - Updated record trigger

The **Updated record** trigger monitors Pipedrive for updated records.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to monitor. |

## Output

The **Updated record** trigger's output fields vary based on your selected **Object** type. The following output table uses a **Pipeline** object as an example:

| Output field | Description |
| --- | --- |
| Data | Contains information about the current state of the pipeline. |
| ID | A unique identifier for the pipeline. |
| Name | The name of the pipeline. |
| Order number | The sequence number of the pipeline. |
| Is deleted | Indicates whether the pipeline was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for this pipeline. |
| Add time | A timestamp indicating when this pipeline was created. |
| Update time | A timestamp indicating when this pipeline was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |
| Previous | Contains information about the previous state of the pipeline. |
| ID | A unique identifier for the pipeline. |
| Name | The name of the pipeline. |
| Order number | The sequence number of the pipeline. |
| Is deleted | Indicates whether the pipeline was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for this pipeline. |
| Add time | A timestamp indicating when this pipeline was created. |
| Update time | A timestamp indicating when this pipeline was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |
| Meta | Metadata about the event triggered. |

---

---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/create-record-action.md
description: The Create record action creates an object in Pipedrive.
---

# Pipedrive - Create record action

The **Create record** action creates an object in Pipedrive.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to create. |
| Name | Enter the name of the object. |
| Is deal probability enabled | Specify whether deal probability is enabled. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. Use these fields to specify details for the new object.

## Output

The **Create record** action's output fields vary based on your selected **Object** type. The following output table uses a **Pipeline** object as an example:

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the pipeline. |
| Name | The name of the pipeline. |
| Order number | The sequence number of the pipeline. |
| Is deleted | Indicates whether the pipeline was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for this pipeline. |
| Add time | A timestamp indicating when this pipeline was created. |
| Update time | A timestamp indicating when this pipeline was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |

---

---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/delete-record-action.md
description: The Delete record action deletes a record you specify from Pipedrive.
---

# Pipedrive - Delete record action

The **Delete record** action deletes a record you specify from Pipedrive.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to delete. |
| ID | Enter the unique identifier for the object you plan to delete. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. Use these fields to specify the object to delete.

## Output

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the deleted object. |

> **VARIABLE OUTPUT**
> 
> The **Delete record** action's output fields vary based on your selected **Object** type.

---

---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action retrieves the details of a specific record
  in Pipedrive.
---

# Pipedrive - Get record details by ID action

The **Get record details by ID** action retrieves the details of a specific record in Pipedrive.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to retrieve. |
| ID | Enter the unique identifier for the object. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. Use these fields to specify the object to delete.

## Output

The **Get record details by ID** action's output fields vary based on your selected **Object** type. The following output table uses a **Pipeline** object as an example:

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the pipeline. |
| Name | The name of the pipeline. |
| Order number | The sequence number of the pipeline. |
| Is deleted | Indicates whether the pipeline was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for this pipeline. |
| Add time | A timestamp indicating when this pipeline was created. |
| Update time | A timestamp indicating when this pipeline was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |

> **VARIABLE OUTPUT**
> 
> The **Get record details by ID** action's output fields vary based on your selected **Object** type.

---

---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/search-records-action.md
description: >-
  The Search records action retrieves a list of records for an object in
  Pipedrive.
---

# Pipedrive - Search records action

The **Search records** action retrieves a list of records for an object in Pipedrive.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to retrieve. |
| Limit | Enter the maximum number of records to return. |
| Cursor | Provide the `next_cursor` value to retrieve the next page of results. Defaults to the first page if left blank. |
| Sort by | Select the object to use to sort results. |
| Sort direction | Select whether to sort records in ascending or descending order. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. Use these fields to specify details for the new object.

## Output

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the object. |
| Name | The name of the object. |
| Order number | The sequence number of the object. |
| Is deleted | Indicates whether the object was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for this pipeline. |
| Add time | A timestamp indicating when this object was created. |
| Update time | A timestamp indicating when this object was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |

> **VARIABLE OUTPUT**
> 
> The **Search records** action's output fields vary based on your selected **Object** type.

---

---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/search-records-by-query-action.md
description: >-
  The Search records by query action searches Pipedrive and returns a list of
  records that match the criteria you specify.
---

# Pipedrive - Search records by query action

The **Search records by query** action searches Pipedrive and returns a list of records that match the criteria you specify.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to retrieve from Pipedrive. |
| Term | Enter a search term to query by. |
| Fields to search | Select in which fields to compare the search **Term** and Pipedrive records. |
| Exact match | Select whether to search for exact or partial matches. |
| Limit | Enter the maximum number of records to return. |
| Cursor | Provide the `next_cursor` value to retrieve the next page of results. Defaults to the first page if left blank. |

## Output

The **Search records by query** action's output fields vary based on your selected **Object** type. The following output table uses an **Organization** object as an example:

| Output field | Description |
| --- | --- |
| Data | Contains information about the current state of the organization. |
| Items | Contains records from Pipedrive that match the search criteria. |
| Result score | Indicates whether the search was successful. |
| Item | The organization returned by the search. |
| ID | A unique identifier for the organization. |
| Name | Name of the organization |
| Type | Type of organization |
| Address | The address of the organization. |
| Visible to | The visibility rules set for this organization. |
| Owner | Contains information about the owner of the organization. |
| Custom fields | Contains additional information about the returned records. |
| Notes | Notes from the returned organization. |
| Next cursor | Cursor to use for pagination to fetch the next page. |

> **VARIABLE OUTPUT**
> 
> The **Search records by query** action's output fields vary based on your selected **Object** type.

---

---
url: >-
  https://docs.workato.com/en/connectors/pipedrive-custom/update-record-action.md
description: >-
  The Update record action enables you to update the details of a specific
  record in Pipedrive.
---

# Pipedrive - Update record action

The **Update record** action updates a record you specify in Pipedrive.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to update. |
| ID | Enter the unique identifier of the pipeline object to update. |
| Name | Enter a name for the object. |
| Is deal probability enabled | Select whether to enable deal probability for the object. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Object** selection. Use these fields to specify details for the new object.

## Output

The **Update record** action's output fields vary based on your selected **Object** type. The following output table uses a **Pipeline** object as an example:

| Output field | Description |
| --- | --- |
| ID | The pipeline's unique identifier. |
| Name | The name of the pipeline. |
| Order number | The sequence number of the pipeline. |
| Is deleted | Indicates whether the pipeline was deleted. |
| Is deal probability enabled | Indicates whether deal probability is enabled for the pipeline. |
| Add time | A timestamp indicating when this pipeline was created. |
| Update time | A timestamp indicating when this pipeline was last updated. |
| Is selected | Indicates whether this pipeline is the default pipeline for deals. |

> **VARIABLE OUTPUT**
> 
> The **Update record** action's output fields vary based on your selected **Object** type.

---
