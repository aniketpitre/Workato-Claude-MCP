---
url: 'https://docs.workato.com/en/connectors/azure-ad/new-updated-user-trigger.md'
description: >-
  The New/updated user trigger in the Microsoft Entra ID connector fires when a
  user is created or updated in your directory.
---

# Microsoft Entra ID - New/updated user trigger

The **New/updated user** trigger detects when a Microsoft Entra ID user is created or updated.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for new events. |
| When first started, this recipe should pick up events from | Choose a start date and time to retrieve trigger events. Leave blank to start with events from one hour ago. |
| Output fields | Choose fields to include in the response. Leave blank to return default fields. |
| Additional fields | Add fields with JSON or enter them manually. |
| Set trigger condition | Define conditions to filter trigger events before processing. |

## Output

The response includes fields based on the selections in the input.

Refer to the [User schema](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0#properties) for field definitions.

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-ad/add-remove-user-license-action.md
description: >-
  Add or remove subscriptions for the user. You can also enable and disable
  specific plans associated with a subscription.
---

# Microsoft Entra ID - Add or remove user license action

The **Add or remove user license** action adds or removes subscriptions for a user. You can enable and disable specific plans associated with a subscription.

## Input

| Input field | Description |
| --- | --- |
| User | Select a user to add or remove a license. Alternatively, enter a custom value if the user is not in the drop-down menu. |
| SKU ID | Enter the specific GUID assigned to a licensing plan in Microsoft Entra ID. |
| Service disabled plans | List unique identifiers for disabled plans. |
| Remove licenses | Enter GUIDs of licenses to remove. |
| Output fields | Choose fields to include in the response. Leave blank to return default fields. |

## Output

| Output field | Description |
| --- | --- |
| License ID | The GUID that identifies the license. |
| SKU ID | A globally unique identifier (GUID) for the licensing plan. |
| SKU part number | A string identifier for the product. |
| Service plan ID | A GUID that identifies each service plan. |
| Service plan name | The name of a specific service or feature in the licensing plan. |
| Provisioning status | Displays the service plan’s status within a subscription or license. |
| Applies to | Defines the service plan’s scope. |

---
