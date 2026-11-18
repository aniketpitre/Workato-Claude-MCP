---
url: 'https://docs.workato.com/en/connectors/clay/get-person-profile-action.md'
description: 'Retrieve a professional profile in Clay by full name, company, or both.'
---

# Clay - Get person profile action

The **Get person profile** action retrieves a professional profile in Clay. The action requires a full name, a company identifier, or both. It returns the first person that matches and doesn't support email lookup.

## Input

| Input field | Description |
| --- | --- |
| Full name | Optional. Enter the full name of the person. Leave blank to search by **Company identifier** only. |
| Company identifier | Optional. Enter the domain, such as `stripe.com`, or the LinkedIn URL of the person's company. The action doesn't accept company names. Leave blank to search by **Full name** only. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view the remaining fields.

| Output field | Description |
| --- | --- |
| Name | The full name of the person. |
| First name | The first name of the person. |
| Last name | The last name of the person. |
| LinkedIn URL | The LinkedIn URL of the person. |
| Company domain | The domain of the person's company. |
| Location | The location of the person. |
| City (Location) | The city of the person. |
| Country (Location) | The country of the person. |
| Latest experience title | The job title of the person's latest experience. |
| Latest experience company | The company of the person's latest experience. |

---
