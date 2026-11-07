---
url: 'https://docs.workato.com/en/connectors/gumroad/search-records-action.md'
description: >-
  Search for Gumroad records, such as sales or subscribers, that match optional
  filters.
---

# Gumroad - Search records action

The **Search records** action searches for records, such as sales or subscribers, that match optional filters in Gumroad. The action returns a list of matching records.

## Input

Input fields dynamically generate based on the **Object** you select.

| Input field | Description |
| --- | --- |
| Object | Select the object type. Options are **Sale** or **Subscriber**. |
| Product ID | Select the product to search. Alternatively, enter the product ID or permalink. This field is required when **Object** is **Subscriber**. Leave blank to search sales for all products when **Object** is **Sale**. |
| Email | Optional. Enter a buyer or subscriber email address to filter by. Leave blank to return records for all email addresses. |
| After | Optional. Only return sales created after this date. Leave blank to apply no start date. The **After** field is only available when **Object** is **Sale**. |
| Before | Optional. Only return sales created before this date. Leave blank to apply no end date. The **Before** field is only available when **Object** is **Sale**. |
| Order ID | Optional. Enter the order number to filter sales. Leave blank to return sales for all orders. The **Order ID** field is only available when **Object** is **Sale**. |
| Paginated | Optional. Set to `true` to return results in pages of up to 100 records. The **Paginated** field is only available when **Object** is **Subscriber**. |
| Page key | Optional. Enter the **Next page key** from a previous search to retrieve the next page of results. Leave blank to start from the first page. |

## Output

Output fields dynamically generate based on the **Object** you select. Refer to the Gumroad [API](https://app.gumroad.com/api) documentation for more information on available output fields. The following fields are common to all objects:

| Output field | Description |
| --- | --- |
| Records | The list of records that match the search. |
| ID (Records) | The unique ID of the record. |
| Email (Records) | The email address of the buyer or subscriber. |
| Product ID (Records) | The unique ID of the product. |
| Product name (Records) | The name of the product. |
| Created at (Records) | The date and time the record was created. |
| License key (Records) | The license key issued for the record. |
| Next page key | The key to retrieve the next page of results. This field is blank when there aren't more pages. |

---
