---
url: 'https://docs.workato.com/en/connectors/airwallex/config-operation-action.md'
description: >-
  The Config operation action enables you to query for active merchant
  configurations in Airwallex.
---

# Airwallex - Config operation action

The **Config operation** action enables you to query for active merchant configurations in Airwallex.

## Input

| Input field | Description |
| --- | --- |
| Operation | Specify the operation to perform. Fields load dynamically based on the operation you select. |

For example, if the selected operation is **Get available bank names**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Payment method type | Enter the payment method type to find available banks. |
| Country code | Specify the country code to filter available banks. |
| Page number | Enter the page number of the response, starting from 0. |
| Page size | Enter the number of banks to be returned per page. |

## Output

The output fields are determined by the operation selected in the input. Map the relevant datapill from the data tree to subsequent steps. Refer to the following example output fields for the **Get available bank names** operation:

| Output field | Description |
| --- | --- |
| Has more | Indicates whether more pages are available. |
| Items | List of all banks, including the following properties. |
| Bank name | Name of the bank. |
| Display name | Display name of the bank, used on the user interface. |
| Resources | Data about other resources available for the bank. |
| Logo URL | URL of the image that corresponds to the logo of the bank. |

---
