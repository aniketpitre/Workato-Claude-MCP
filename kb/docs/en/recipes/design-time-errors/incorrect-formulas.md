---
url: 'https://docs.workato.com/en/recipes/design-time-errors/incorrect-formulas.md'
description: >-
  Learn how to find and fix formula and code action errors in Workato recipes,
  including syntax mistakes in SQL, Python, Ruby, and JavaScript steps.
---

# Incorrect formulas and code actions

Errors in formulas and code actions can prevent your recipe from starting or cause it to fail during execution. Ensure all formulas and code snippets in your recipe are free from syntax and logical errors.

## Incorrect formulas

While not every formula issue stops a recipe from starting, those with syntax or surface-level errors are detected before the recipe can run. Other issues may appear during execution.

![Empty action](/assets/formula-error.CfUA55Zp.png)_Formula error_

The following are common formula errors that you may encounter:

- Typographical errors.
- Incorrect spacing between formulas and operators, such as having two whitespaces instead of one.
- Using incorrect symbols, such as curly braces `{ }` instead of square brackets `[ ]`.
- Symbols copied from word processors such as OpenOffice and Microsoft Word may be formatted differently and cause recognition issues in the Workato formula editor.

To resolve incorrect formulas, review each formula for correct syntax, spelling, and proper spacing. Ensure that all symbols and operators are formatted correctly and recognized by the Workato formula editor.

* * *

## Incorrect code actions and SQL statements

Workato offers various actions that use different code languages, including:

- Execute Python code
- Execute Ruby code
- Execute JavaScript code
- Transform XML using XSLT
- Query lists in Collection
- Run custom SQL in JDBC source

![Action code languages](/assets/action-codes.C1YuIL5R.png)_Actions that use code languages_

Incorrect code in these actions can prevent your recipe from starting. Ensure your code is error-free before starting the recipe. Some errors may be caught immediately, while others may only appear during execution when the code is run. Ensure to check and test your code when using these actions.

Complete the following steps to resolve issues with incorrect code actions and SQL statements:

1. Check your code for syntax and logical errors.
   
2. Test each code action separately in a controlled environment to ensure it functions correctly.
   
3. Use SQL management tools to validate your SQL queries and scripts before implementing them in the recipe.
   

Ensuring that your code actions and SQL statements are free of errors prevents issues that can stop your recipe from running or cause it to fail during execution.

---
