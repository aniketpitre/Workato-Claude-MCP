---
url: 'https://docs.workato.com/en/wel/quickstart.md'
description: >-
  Get started with WEL three ways - in the Transform Data action, with an
  external AI client, or with the wel command-line binary for fast local
  iteration.
---

# WEL quickstart

[WEL](/en/wel) (Workato Expression Language) is Workato's transformation language. It runs alongside the rest of your recipe, on Workato's [data plane](/en/wel#where-wel-runs), with nothing to install and nothing to connect to.

This page uses [one example](#example) to showcase three methods of working with WEL:

- [In a recipe](#start-in-a-recipe): Get started quickly by creating recipe datapills with the Workato Expression Language connector.
- [With an AI client](#start-with-ai): Write WEL with an external AI client.
- [With the binary](#start-with-the-binary): Test changes to an expression quickly and without running a recipe.

## Example

A webhook delivers an order. The destination system expects a flat record with a normalized name and email, a calendar date, and an exact total.

**Input**

```json
{
  "order_id": "so-1001",
  "placed_at": "2026-03-15T09:30:00Z",
  "customer": {
    "first_name": "kalani",
    "last_name": "park",
    "email": " KALANI@Example.COM "
  },
  "line_items": [
    {"sku": "WID-1", "qty": 3, "unit_price": "12.50"},
    {"sku": "GAD-7", "qty": 1, "unit_price": "99.00"}
  ]
}
```

**Formula**

```wel
{
  order_id: upper(_.order_id),
  customer_name: f"{capitalize(_.customer.first_name)} {capitalize(_.customer.last_name)}",
  email: lower(trim(_.customer.email)),
  order_date: PlainDate(DateTime(_.placed_at)),
  item_count: count(_.line_items),
  total: _.line_items >> map_by(li ~> Decimal(li.unit_price) * li.qty) >> sum
}
```

This example uses the following components:

- `_` is the **input variable**, which contains the preceding payload. `_.order_id` reads the `order_id` field from it. Refer to [Input variables](/en/wel/language/expressions#input-variable) for details.
- `>>` pipes a value into a function, so the total reads left to right. The pipeline takes the line items, turns each into a price, and adds them up.
- `Decimal(li.unit_price)` keeps the money exact. The total is `136.50`, not `136.5`. The scale survives because `Decimal` is an exact type rather than a display format.
- `PlainDate(...)` produces a calendar date with no time zone, so it can't shift a day on its way to the destination.

**Output**

```json
{
  "order_id": "SO-1001",
  "customer_name": "Kalani Park",
  "email": "kalani@example.com",
  "order_date": "2026-03-15",
  "item_count": 2,
  "total": 136.50
}
```

## Start in a recipe

Recipes are the most common way to work with WEL. This connector doesn't require connection setup. [Create a recipe](/en/recipes#create-a-new-recipe) or open an existing one, then complete the following steps to run the preceding example:

1. Open the recipe where you plan to work with WEL.
   
2. Click **\+ Add step** and select **Action in app**.
   
   ![Add action](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Add action in app**_
   
3. Search and select the **Workato Expression Language** connector. The [Transform data (code)](/en/wel/workato-expression-language-connector) action loads automatically.
   
4. Enter a name for the WEL expression in the **Name** field. This label only shows in the recipe editor.
   
5. Go to the **Input fields** section and click **generate from JSON sample**.
   
6. Paste the following sample JSON:
   
   ```json
   {
     "order_id": "so-1001",
     "placed_at": "2026-03-15T09:30:00Z",
     "customer": {
       "first_name": "kalani",
       "last_name": "park",
       "email": " KALANI@Example.COM "
     },
     "line_items": [
       {"sku": "WID-1", "qty": 3, "unit_price": "12.50"},
       {"sku": "GAD-7", "qty": 1, "unit_price": "99.00"}
     ]
   }
   ```
   
7. Optionally select **Set all fields as required** to mark every detected field as required. You can adjust individual field requirements afterward.
   
8. Click **Next** to generate the field list automatically.
   
9. Review the inferred field types and correct any the designer got wrong.
   
   > **CHECK SCHEMA INFERENCES**
   > 
   > Schema inference reads a sample, so it can only see what the sample shows. Check for the following cases:
   > 
   > - **Numeric precision**: A sampled `12.50` infers as a floating-point number, not a `Decimal`. Set the type yourself if the field is a currency amount.
   > - **Dates and datetimes**: A sampled `2026-03-15T09:30:00Z` infers as a plain string, not a temporal type.
   > 
   > Refer to the [Transform data](/en/wel/workato-expression-language-connector) action for the full field list and more information about inference.
   
10. Click **Generate schema**. New input fields become available based on the schema.
    
11. Map data into the new fields, such as datapills from earlier steps or static values.
    
12. Go to the **Output schema** section and click **Use JSON**. This section configures the datapills the expression produces. A field that isn't in the output schema doesn't appear downstream, regardless of the expression's final values.
    
13. Paste the following sample output JSON:
    
    ```json
    {
      "order_id": "SO-1001",
      "customer_name": "Kalani Park",
      "email": "kalani@example.com",
      "order_date": "2026-03-15",
      "item_count": 2,
      "total": 136.50
    }
    ```
    
14. Optionally select **Set all fields as required** to mark every detected field as required. You can adjust individual field requirements afterward.
    
15. Click **Next** to generate the field list automatically.
    
16. Review the inferred field types and correct any the designer got wrong, using the same checks as the input fields step.
    
17. Click **Generate schema**. The order\_id, customer\_name, email, order\_date, item\_count, and total datapills defined in the output schema become available in downstream recipe steps, but don't have assigned values until you define the WEL **Code**.
    
18. Paste the following expression into the **Code** field to define the transformations to perform on input values to create output datapills:
    
    ```wel
    {
      order_id: upper(_.order_id),
      customer_name: f"{capitalize(_.customer.first_name)} {capitalize(_.customer.last_name)}",
      email: lower(trim(_.customer.email)),
      order_date: PlainDate(DateTime(_.placed_at)),
      item_count: count(_.line_items),
      total: _.line_items >> map_by(li ~> Decimal(li.unit_price) * li.qty) >> sum
    }
    ```
    

## Start with an external AI client

An external AI client that hasn't seen WEL will write something that looks plausible and doesn't run, usually by borrowing [lambda](/en/wel/language/expressions#lambdas) syntax from another language. WEL uses `~>` for a lambda, and `->` or `=>` are parse errors.

The WEL kit fixes that by providing the AI client a language reference and platform binary. This allows the AI to check generated code against the real engine and create an expression that reliably works.

> **DISTRIBUTION**
> 
> Distribution for the WEL kit and the `wel` binary isn't published here. Contact your Customer Success Representative for the current build or location for your platform.

An AI client with the WEL kit can create a transformation from your plain language description. Include the sample payload and what the destination needs. Ask it to verify the expression against the engine and return the sample output and formula that you can paste directly into the action.

> **VERIFY AI CODE**
> 
> Read AI generated code yourself. You can quickly check the generated code by verifying that the output matches what your destination expects.

## Start with the binary

A recipe run takes minutes to test an expression. The `wel` binary runs the engine locally instead, and answers in under a second. This is a better workflow for quickly iterating while you're still writing the expression.

> **DISTRIBUTION**
> 
> Distribution for the WEL kit and the `wel` binary isn't published here. Contact your Customer Success Representative for the current build or location for your platform.

Complete the following steps to work with the `wel` binary for the provided [example](#example):

1. Save the following files locally:
   
   Expression
   
   Save the following expression as `order.wel`:
   
   ```wel
   {
     order_id: upper(_.order_id),
     customer_name: f"{capitalize(_.customer.first_name)} {capitalize(_.customer.last_name)}",
     email: lower(trim(_.customer.email)),
     order_date: PlainDate(DateTime(_.placed_at)),
     item_count: count(_.line_items),
     total: _.line_items >> map_by(li ~> Decimal(li.unit_price) * li.qty) >> sum
   }
   ```
   
   Sample input
   
   Save the following sample input as `order.json`:
   
   ```json
   {
     "order_id": "so-1001",
     "placed_at": "2026-03-15T09:30:00Z",
     "customer": {
       "first_name": "kalani",
       "last_name": "park",
       "email": " KALANI@Example.COM "
     },
     "line_items": [
       {"sku": "WID-1", "qty": 3, "unit_price": "12.50"},
       {"sku": "GAD-7", "qty": 1, "unit_price": "99.00"}
     ]
   }
   ```
   
2. Run the following command:
   
   ```bash
   wel eval -f order.wel -I order.json
   ```
   
   The expression outputs the following:
   
   ```wel
   {order_id: "SO-1001", customer_name: "Kalani Park", email: "kalani@example.com", order_date: 2026-03-15, item_count: 2, total: 136.50}
   ```
   
3. Iterate by editing the `order.json` input file or `order.wel` expression file and running the command again until the expression produces the output your destination expects. The WEL engine runs identically in the binary and in your recipe, so an expression that works here works there too.
   

### Useful flags

The `wel` binary accepts additional flags for testing and validation:

| Flag | Purpose | Example |
| --- | --- | --- |
| `--now` | Fixes `now()` to a specific instant, so results are reproducible. | `wel eval 'now()' --now '2026-03-15T09:30:00Z'` |
| `validate` | Checks that an expression parses, without running it. | `wel validate -f order.wel` |

The `wel` binary has other flags and subcommands beyond these two, but they target developers building the host application that embeds the WEL engine, not recipe builders testing an expression.

## Next steps

- [Transform data](/en/wel/workato-expression-language-connector): The WEL connector integration and what schema inference doesn't catch.
- [Standard library](/en/wel/stdlib): Information about every WEL function.
- [Data types](/en/wel/language/data-types): Why `Decimal` and `PlainDate` were the right choices in the preceding example.
- [Cookbook](/en/wel/cookbook): Examples of common integration problems.
- [Error codes](/en/wel/errors): Troubleshoot job failures.

---
