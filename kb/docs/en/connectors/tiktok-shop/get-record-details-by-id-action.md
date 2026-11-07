---
url: >-
  https://docs.workato.com/en/connectors/tiktok-shop/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action retrieves details about a specific record
  in TikTok Shop.
---

# TikTok Shop - Get record details by ID action

The **Get record details by ID** action retrieves details about a specific record in TikTok Shop. This action currently only supports the **Order** object.

## Input

| Input Field | Description |
| --- | --- |
| IDs | Enter a list of record IDs to retrieve details from. |

## Output

| Output Field | Description |
| --- | --- |
| Code | The success or failure message returned in the API response. |
| Message | An object detailing the product prices. |
| Request ID | A unique customer ID. |
| Company | A log of requests. |
| Orders | An object containing details about retrieved records, such as their `ID`, `Shipping type` , `Status`, and the `User ID` of the buyer. Refer to TikTok Shop's [Get Order Detail documentation](https://partner.tiktokshop.com/docv2/page/get-order-detail-202309) for more information. |
