---
url: 'https://docs.workato.com/en/connectors/facebook-ads/new-lead.md'
description: >-
  The New lead trigger in the Facebook Lead Ads connector fires when a user
  completes a lead ad form on a selected Facebook page.
---

# Facebook Lead Ads - New lead trigger

The **New Lead** trigger activates when a user completes a lead ad form on Facebook, providing immediate notifications. This trigger links to a specific Facebook page. Ensure you hold admin permissions for the page if it doesn't appear in the drop-down list. By selecting a form, you gain insights into the form's questions and can display datapills in Workato that correspond to these questions. If you don't specify a form, Workato captures all submissions from the page but cannot display the related datapills.

![New Lead Ad Form Response trigger](/assets/new-lead-trigger.iNOBrK2F.png)_Facebook Lead Ads - New lead trigger_

## Input

| Field | Description |
| --- | --- |
| Page | Select the Facebook page to monitor for new lead ad form submissions. If your page is not displayed, ensure you have the necessary admin permissions for it. |
| Form | Choose a specific lead ad form to track submissions. If no form is selected, the trigger captures submissions from all forms on the selected page. The drop-down lists up to 100 recently created forms. If your form is not listed, toggle to input the form ID directly. |
| Set trigger condition | Specify conditions to filter events that activate the trigger. |

## Output

| Field | Description |
| --- | --- |
| ID | The unique identifier for the lead. |
| Ad ID | The identifier for the ad. |
| Ad name | The name of the ad associated with the lead. |
| Adset ID | The identifier for the ad set. |
| Adset name | The name of the ad set. |
| Campaign ID | The identifier for the campaign. |
| Campaign name | The name of the campaign. |
| Created time | The time when the lead was created. |
| Custom disclaimer responses | Responses to custom disclaimers in the form. |
| Field data | Details provided in the form fields. |
| Form ID | The identifier for the form. |
| Home listing | Information about the home listing. |
| Is organic | Indicates if the lead is organic. |
| Partner name | The name of the partner associated with the lead. |
| Platform | The platform that captured the lead. |
| Retailer item ID | The identifier for the retailer item. |
| Vehicle | Details about the vehicle associated with the lead. |
| Leadgen ID | The identifier for the lead generation form. |
| List size | The total number of items in the list. |
| List index | The index of this item within the list. |

---
