---
url: 'https://docs.workato.com/en/wel.md'
description: >-
  WEL is Workato's transformation language, including 250 built-in functions, 16
  data types, and exact decimal arithmetic and runs natively alongside your
  recipe.
---

# Workato Expression Language

WEL (Workato Expression Language) is Workato's transformation language. It reshapes data as it moves between systems, renaming and restructuring fields, joining and aggregating records, converting types, and formatting values for the destination.

WEL is part of the Workato platform, so there's nothing to install, nothing to connect to, and no runtime to manage. WEL runs on Workato's [data plane](#where-wel-runs) alongside your recipes.

## Why WEL exists

Integration is a translation problem. Systems agree on what an object is and disagree on its format. For example:

- The source sends a full name and the destination expects two fields.
- The source sends `"12.50"` as a string and the destination expects an exact decimal.
- The source sends a UTC timestamp and the destination expects a local calendar date.

Translating well requires more than field mapping. Using a general-purpose scripting language for translations presents problems, such as a runtime to secure, dependencies to keep current, and code that only its author can safely change.

WEL is built and scoped for transformations, so you can integrate systems without encountering the security and maintenance issues of a general-purpose language.

## What makes WEL a language

Four properties make WEL a language rather than a mapping tool, and each prevents a class of bug that field mapping cannot:

- [16 data types](/en/wel/language/data-types): Exact decimals and zone-aware temporal types keep business data from quietly changing shape in transit.
  
- [250 built-in functions](/en/wel/stdlib): They span strings, lists, maps, temporal arithmetic, numeric rounding, encoding, escaping, Unicode, and cryptography, all in the language rather than in a library you add.
  
- [Composition](/en/wel/language/operators#pipeline): The pipeline operator `>>` lets a multi-step transformation read in the order it happens rather than inside-out:
  
  ```wel
  _.orders
    >> filter_by(o ~> o.status == 'open')
    >> sort_by(o ~> o.total)
    >> reverse
    >> take(3)
  ```
  
- [Strictness](/en/wel/stdlib#types-are-strict): By default, WEL doesn't coerce a value to make an expression succeed and a `List` or `Map` doesn't become a string by accident. WEL raises a [numbered error](/en/wel/errors) for mismatches instead of producing a plausible wrong answer.
  

## Use cases

Use WEL when the transformation is more than a field mapping:

- Reshape a nested API response into the flat record a destination expects.
- Group, deduplicate, or aggregate a batch of records.
- Calculate money, where the difference between exact and approximate arithmetic reaches an invoice.
- Normalize dates, time zones, and text arriving from systems that disagree.
- Build a formatted string safely, such as a CSV row, a query, a URL, or a message body.
- Validate a payload and route what fails, instead of passing bad data on.

You don't need WEL for a straight one-to-one field mapping.

## Where WEL runs

WEL runs on Workato's data plane. The data plane is the part of the platform that processes your data while a recipe runs.

You can construct and run WEL expressions in the following locations:

- **In recipe steps**: Use the [Transform data](/en/wel/workato-expression-language-connector) action to define and run WEL expressions in a recipe step. **Transform data** returns data output by the formula as datapills for downstream recipe steps.
  
- **In reusable maps**: Use [formula nodes](/en/features/transformation-maps/create-map#formula-transformations) to run WEL expressions in a reusable [transformation map](/en/features/transformation-maps) that centralizes mapping and transformation logic across recipes. Transformation maps return data you define in their output schema as datapills for downstream recipe steps. This can include input fields mapped directly to output fields without passing through a WEL formula.
  

## Next steps

Use the following resources to start using WEL alongside your recipes.

- [Quickstart](/en/wel/quickstart): Follow along with an example showing different WEL workflows.
- [Transform data](/en/wel/workato-expression-language-connector): Use WEL in recipes through a connector.
- [Data types](/en/wel/language/data-types): Understand the 16 WEL data types and when to use each one.
- [Standard library](/en/wel/stdlib): Learn all 250 WEL functions.
- [Cookbook](/en/wel/cookbook): View examples of common integration problems.
- [Error codes](/en/wel/errors): Troubleshoot job failures.

---
