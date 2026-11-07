---
url: 'https://docs.workato.com/en/connectors/ukg-pro-rest/update-record-action.md'
description: 'The Update record action updates a record in UKG Pro, such as a pending hire.'
---

# UKG Pro - Update record action

The **Update record** action updates a record in UKG Pro, such as a pending hire.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to update. |
| ID | Enter the ID of the specific object you plan to update. |

> **PENDING HIRE OBJECT**
> 
> Currently, Workato supports only the `Pending hire` object type. Refer to UKG Pro's [Pending Hire Service API Guide](https://library.ukg.com/a/207061) for more information on the `Pending hire` object type and its schema.

## Output

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the pending hire. |
| Is prehire | Indicates whether the candidate is in a pre-hire stage. |
| Offer ID | The unique identifier for the candidate’s job offer. |
| Requisition ID | The unique identifier for the job opening associated with the pending hire. |
| Candidate key | A unique identifier assigned to the candidate, used to track them throughout the hiring process. |
| Imported by | The user or system that imported the pending hire record into UKG Pro. |
| Import date | The date when the pending hire record was imported into the system. |
| Is company international | Indicates whether the company operates internationally. |

---
