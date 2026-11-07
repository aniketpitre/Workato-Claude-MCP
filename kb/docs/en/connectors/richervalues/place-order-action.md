---
url: 'https://docs.workato.com/en/connectors/richervalues/place-order-action.md'
description: >-
  The Place order places a property evaluation, AVM, or inspection order in
  RicherValues.
---

# RicherValues - Place order action

The **Place order** action places a property evaluation, AVM, or inspection order in RicherValues.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of order to place from the drop-down menu. |

Input fields are dynamically loaded based on your selected **Object** type. For example, the following input schema uses **EVAL** as the **Object** type:

| Input fields | Description |
| --- | --- |
| Company token | Provide the company token for authorization. |
| Is property vacant land | Select whether the property is vacant land. |
| Is property partially completed | Select whether the property is partially completed. |
| Report type | Provide the type of evaluation report, such as `prop-value`. |
| Inspection type | Provide the type of inspection, such as `interior-w-exterior`. |
| Turnaround time | Provide the delivery timeframe, such as `rush` or `standard`. |
| Include gross living area | Select whether to include GLA (Gross Living Area). |
| Licensing required | Select whether licensing is required. |
| Client loan number | Provide the client loan number, such as `LN123456789`. |
| Closing date | Provide the loan closing date, such as `2023-10-30`. |
| Loan officer token | Provide the loan officer token, such as `LO123456789`. |
| Include flood certification | Select whether to include flood certification. |
| Is property on lockbox | Select whether the property is on lockbox. |
| Property address | Provide the property street address, such as `4325 Southwest 70th Terrace`. |
| Property address line 2 | Provide the property address line 2, such as `Apt 2B, Suite 100`. |
| City | Provide the property city, such as `Gainesville`. |
| State | Provide the property state, such as `FL` or `CO`. |
| Postal code | Provide the property ZIP code, such as `32608`. |
| Residential property type | Select the type of residential property from the drop-down menu or provide a custom value. |
| Property condition | Select the current property condition from the drop-down menu or provide a custom value. |
| Above grade square feet | Provide the above grade square footage, such as `2000`. |
| Below grade square feet | Provide the below grade square footage, such as `1000`. |
| Bedrooms | Provide the number of bedrooms. |
| Bathrooms | Provide the number of bathrooms. |
| Year built | Provide the year property was built. |
| Stories | Provide the number of stories. |
| Garage spaces | Provide the number of garage spaces. |
| Lot size square feet | Provide the lot size in square feet. |
| Report contact name | Provide the report contact name, such as `John Doe`. |
| Report contact email | Provide the report contact email, such as `useremail@domain.com`. |
| Report contact phone | Provide the report contact phone number, such as `3154487878`. |
| Property upload type | Select the upload type. |
| Historical effective date | Select the historical effective date, such as `Current Date` or `Historical Date`. |
| Effective date | Provide the report effective date, such as `2025-05-21`. |

## Output

The **Place order** action's output fields vary based on your selected **Object** type. For example, if the selected object is **EVAL**, then the output schema is as follows:

| Output field | Description |
| --- | --- |
| Success | Indicates whether the order was successfully placed. |
| Message | The status of the order submission. |
| Data | An object containing order details and next steps. |
| Payment link | A URL link to complete payment for the order. |
| Intake token | A unique token assigned to the order for tracking purposes. |
| Meta | An object containing additional metadata. |
| Errors | An array containing error messages for any issues that occurred during order placement. |

---
