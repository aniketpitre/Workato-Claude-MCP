---
url: 'https://docs.workato.com/en/connectors/tiktok-shop/search-records-action.md'
description: >-
  The Search records action retrieves a list of TikTok Shop records that match
  your search criteria.
---

# TikTok Shop - Search records action

The **Search records** action retrieves a list of TikTok Shop records that match your search criteria. This action currently only supports the **Order** object.

## Input

| Input Field | Description |
| --- | --- |
| Page size | The maximum number of records to return in a single response. |
| Sort order | Select whether to sort the records in ascending or descending order. |
| Page token | An opaque token used to retrieve the next page of a paginated result set. |
| Sort field | Select a field to sort results by, such as `create_time` or `update_time`. |
| Order status | Specify an order status to filter results by, for example: `UNPAID` or `ON_HOLD`. |
| Create time greater than | Specify a Unix timestamp to only show orders created on or after that date and time. |
| Create time less than | Specify a Unix timestamp to only show orders created before that date and time. |
| Update time greater than | Specify a Unix timestamp to only show orders updated on or after that date and time. |
| Update time less than | Specify a Unix timestamp to only show orders updated before that date and time. |
| Shipping type | Select a delivery method to filter results by, such as `TIKTOK` or `SELLER`. |
| Buyer user ID | Specify the `user ID` of a buyer to filter results by. |
| Is buyer request cancel | Filter results by whether the buyer has initiated an order cancellation request. |
| Warehouse IDs | Specify a pickup or sales `warehouse ID` to filter results by. This field is only applicable if the multi-warehouse feature is enabled in TikTok Shop. |

## Output

| Output Field | Description |
| --- | --- |
| Code | The success or failure message returned in the API response. |
| Message | An object detailing the product prices. |
| Request ID | A unique customer ID. |
| Company | A log of requests. |
| Orders | An object containing details about retrieved records, such as their `ID`, `Shipping type` , `Status`, and the `User ID` of the buyer. Refer to TikTok Shop's [Get Order Detail documentation](https://partner.tiktokshop.com/docv2/page/get-order-detail-202309) for more information. |

---
