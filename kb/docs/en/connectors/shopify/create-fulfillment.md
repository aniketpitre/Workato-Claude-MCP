---
url: 'https://docs.workato.com/en/connectors/shopify/create-fulfillment.md'
description: >-
  The Create fulfillment action in the Shopify connector lets you create a
  fulfillment for one or more fulfillment orders assigned to a location.
---

# Shopify - Create fulfillment action

## New fulfillment order API architecture

This action creates a fulfillment for one or more fulfillment orders in Shopify. The fulfillment orders are associated with the same order and are assigned to the same location.

> **NO DUPLICATE FULFILLMENT ORDERS IN REQUESTS**
> 
> As part of our latest updates, we have implemented validation to prevent duplicate fulfillment orders in requests to create a fulfillment. It is now required that each fulfillment order ID is unique within the **Line items by fulfillment order** field.

### Input

| Field | Description |
| --- | --- |
| Line items by fulfillment order | The fulfillment order line items that have to be fulfilled. See below for the structure of each line item by fulfillment order. |
| Message | Optional. A message that's associated with the fulfillment request. |
| Notify customer? | Optional. Whether a notification should be sent to the customer when the fulfillment is created. Defaults to `false`. |
| Origin address | Optional. The address of the fulfillment location. See below for the structure of each origin address. |
| Tracking information | Optional. The tracking information for the fulfillment. See below for the structure of each tracking information. |

#### Line items by fulfillment order

| Field | Description |
| --- | --- |
| Line items by fulfillment order source list | Optional. The source list of the lines that you plan to upload. |
| Fulfillment order ID | The ID of the fulfillment order. |
| Fulfillment order line items | Optional. The fulfillment order line items and the quantity of each which should be fulfilled. If left blank, then all of the fulfillment order line items of the associated fulfillment order are fulfilled. See below for the structure for each line item. |

#### Fulfillment order line items

| Field | Description |
| --- | --- |
| Fulfillment order line items source list | Optional. The source list of the lines that you plan to upload. |
| ID | The ID of the fulfillment order line item. |
| Quantity | The quantity of the fulfillment order line item. |

#### Origin address

| Field | Description |
| --- | --- |
| Address (line 1) | Optional. The first line of the address. Typically the street address of the fulfillment location. |
| Address (line 2) | Optional. The second line of the address. Typically the number of the apartment, suite, or unit. |
| City | Optional. The city of the fulfillment location. |
| Country code | The two-letter country code ([ISO 3166-1 alpha-2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)s) of the fulfillment location. |
| Province code | Optional. The province of the fulfillment location. |
| Zip | Optional. The zip code of the fulfillment location. |

#### Tracking information

| Field | Description |
| --- | --- |
| Tracking company | Optional. The name of the tracking company. |
| Tracking number | Optional. The tracking number for the fulfillment. |
| Tracking URL | Optional. The URL to track the fulfillment. |

### Output

The output of the action above is the `Fulfillment` resource. Read the [Shopify documentation](https://shopify.dev/docs/api/admin-rest/2024-04/resources/fulfillment#resource-object) for more information.

## Legacy fulfillment API architecture

This action creates a fulfillment in Shopify.

> **DEPRECATION OF FULFILLMENT API IN THE 2022-04 RELEASE**
> 
> Shopify has deprecated the Fulfillment API in its 2022-04 REST Admin API release in favor of Fulfillment Orders. While we've implemented changes to ensure usability of the old action, we encourage you to update your recipes to the new "Create Fulfillment" action which uses the new Fulfillment Order API. We will also be deprecating the old action moving forward.

### Input

| Field | Description |
| --- | --- |
| Order ID | Provide the order ID. This can be found at the end of URL of the order page. |
| Location ID | Provide the unique location ID tied to the fulfillment. |
| Tracking company | Provide the tracking company. |
| Tracking numbers | Provide the tracking numbers. Multiple values should be separated by commas. |
| Line items | Provide the line items. Each line item has an **ID** and a **Quantity** |
| Tracking URLs | The URLs to track the fulfillment, multiple values should be separated by commas. |
| Notify customer | Select from the picklist or input your own value. |

### Output

| Field | Description |
| --- | --- |
| ID | The ID for the fulfillment. |
| Order ID | The unique numeric identifier for the order. |
| Status | The status of the fulfillment. |
| Created at | The data and time when the fulfillment was created. |
| Service | The type of service used. |
| Updated at | The date and time when the fulfillment was last updated. |
| Tracking company | The tracking company. |
| Tracking number | The tracking number for this fulfillment. |
| Tracking numbers | A list of tracking numbers, provided by the shipping company. |
| Tracking URL | The URL of tracking page for the fulfillment. |
| Tracking urls | The URLs of tracking pages for the fulfillment. |
| Receipt | A text field that provides information about the receipt. Each receipt contains information about **Testcase** status and the **Authorization code**. |
| Line items | A historical record of each item in the fulfillment. Each line item contains the following: - ID - Variant ID - Title - Quantity - Price |

---
