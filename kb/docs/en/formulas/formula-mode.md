---
url: 'https://docs.workato.com/en/formulas/formula-mode.md'
description: >-
  Learn how to switch to formula mode in Workato to apply approved formulas,
  transform data, and format text in recipe input fields.
---

# Formula mode

To start using formulas, you must switch to formula mode. You can activate formula mode at the field level. Note that most, but not all, input fields support formula mode.

To switch from text mode to formula mode, click **Formula** in the input field in which you plan to add a formula. The background color changes to indicate that formula mode is active. Additionally, the type icon changes to the `fx` icon.

> **SUMMARY**
> 
> - To use formulas in Workato, activate formula mode at the field level.
> - Formula mode provides approved formulas and guidance for data manipulation.
> - The editor shows type-specific formulas based on the datapill type in an input field.
> - Text must be explicitly formatted in formula mode, unlike in text mode.
> - Ruby methods not found in Workato documentation are not allowlisted and, therefore, not supported. Contact your Customer Success Manager to request new formulas for the allowlist.

![Formula mode](/assets/formula-mode.DHcrYQgx.png)_Formula mode is displayed with the `fx` symbol_

In formula mode, the editor provides a set of approved formulas for data transformation and manipulation, along with guidance on how to use these formulas.

## Filter formulas displayed by data type

The formula editor displays type-specific formulas for your [datapills](/en/recipes/data-pills-and-mapping).

When a string-type datapill is mapped into an input field in formula mode, the editor shows the list of formulas applicable to strings.

![String formula list](/assets/string-formula-list.Cg3Wn_a5.png)_Formula editor showing the list of string formulas_

## Formula hints and syntax

After you select a formula, a detailed description of the formula appears. This description explains how to use the formula and provides examples.

![Formula editor hint](/assets/formula-editor-hint.Du3r4ZGp.png)_Detailed description and hints for the split formula_

## Text versus formula mode

Video guide: From text to formula mode

[Video](https://www.youtube.com/embed/e2vt8x5mHdM)

  

> **RUBY STRING INTERPOLATIONS NO LONGER SUPPORTED IN TEXT MODE**
> 
> Ruby string interpolations (for example, `#{now + 1.day}`) are no longer supported in text input mode. Only datapills are evaluated. All other expressions (including interpolations) will be processed as plain text, verbatim.
> 
> For expressions that previously relied on Ruby string interpolations, you can achieve the same functionality using formula mode.

You can use text mode to map text and datapills directly into input fields. The result appears exactly as you entered it in the field. In contrast, formula mode requires that you explicitly format text using formulas for proper evaluation and output.

### Example

Consider a recipe that sends an email to new leads in Salesforce. For instance, when a new lead named Madison Diaz is created, the following email is sent:

```text
Hi Madison,

Thanks for joining our mailing list! We're excited to have you!
```

In text mode, you can compose the **Message** directly:

![Welcome email in text mode](/assets/welcome-email-in-text.D6WCSs20.png)_Email in text mode. [Example recipe](https://www.workato.com/recipes/504766)_

In formula mode, you must format the text using proper string syntax:

![Welcome email in formula mode](/assets/welcome-email-in-formula.nOdUBqin.png)_Email in formula mode. [Example recipe](https://www.workato.com/recipes/496603)_

---
