---
url: 'https://docs.workato.com/en/connectors/insightly/create-organization-action.md'
description: >-
  The Create organization action in the Insightly connector lets you create a
  new organization with email, phone, website, and address details.
---

# Insightly - Create organization action

This action creates a new organization in your Insightly instance.

## Input

| Field | Description |
| --- | --- |
| Organization name | The name of the organization. |
| Background | The background of the organization. |
| Visible to | The visibility of the organization. |
| Visible user IDs | The visible user IDs of the organization. |
| Work email | The work email of the organization. |
| Personal email | The personal email of the organization. |
| Other email | The other email of the organization. |
| Work phone | The work phone of the organization. |
| Mobile | The mobile phone of the organization. |
| Home phone | The home phone of the organization. |
| Website | The website of the organization. |
| Email domain | The email domain of the organization. |
| Addresses | The addresses of the organization. |
| Addresses source list | The source list from which the addresses of the organization are derived. This field accepts a [list datapill](/en/features/list-management#list-batch-action) as input. |
| Address type | The type of address (for example, work, home, postal, or other). |
| Street | The street part of the organization's address. |
| City | The city of the organization's address. |
| State | The state of the organization's address. |
| Post code | The postal code of the organization's address. |
| Country | The country of the organization's address. |

## Output

The output of this action is a datatree that contains information about the [organization](https://api.insightly.com/v3.1/Help#!/organizations/GetEntity) created.

---
