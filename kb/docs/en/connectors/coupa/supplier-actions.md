---
url: 'https://docs.workato.com/en/connectors/coupa/supplier-actions.md'
description: >-
  The Get supplier sites by supplier action in the Coupa connector lets you
  retrieve all supplier sites associated with a supplier you specify.
---

# Coupa - Supplier actions

Workato supports the ability to get supplier sites by supplier in Coupa. More supplier actions are available in generic object actions. Use generic actions with a supplier object you specify to create, update, or query suppliers on Coupa. Refer to the [Coupa - Object actions](/en/connectors/coupa/object-actions) section for more information.

**Supplier specific actions**

- `Get supplier sites by supplier`

* * *

### Input fields for supplier actions

You must define which supplier you plan to retrieve the supplier site data from. You can select a supplier from a list or generate the supplier dynamically with datapills from recipe output steps. You must select **Use custom value** if using datapills to ensure you use the Coupa internal supplier ID instead of the supplier name to avoid any unexpected behavior in your recipes.

### Get supplier sites by supplier

This action searches Coupa for the supplier you specify and returns all supplier sites associated with the supplier.

### Output

This action returns a list of supplier sites associated with the supplier.

---
