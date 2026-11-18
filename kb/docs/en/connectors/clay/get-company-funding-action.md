---
url: 'https://docs.workato.com/en/connectors/clay/get-company-funding-action.md'
description: >-
  Retrieve funding signals for a company in Clay, including its total funding
  amount range.
---

# Clay - Get company funding action

The **Get company funding** action retrieves funding signals for a company in Clay. The action returns the total funding amount range. It doesn't return individual funding rounds or investors.

## Input

| Input field | Description |
| --- | --- |
| Company identifier | Enter the domain, such as `stripe.com`, or the LinkedIn URL of the company. The action doesn't accept company names. |

## Output

| Output field | Description |
| --- | --- |
| Name | The name of the company. |
| Domain | The domain of the company. |
| LinkedIn URL | The LinkedIn URL of the company. |
| Annual revenue | The annual revenue range of the company. |
| Total funding amount range (USD) | The total funding amount range of the company, in USD. |
| Period quota | The usage quota for your Clay account in the current period. |
| Limit (Period quota) | The total quota for the period. |
| Used (Period quota) | The amount of the quota your account has used in the period. |
| Remaining (Period quota) | The amount of the quota left in the period. |
| Resets at (Period quota) | The date and time the quota resets. |

---
