---
url: 'https://docs.workato.com/en/formulas/string-formulas-faqs.md'
description: >-
  Answers to common questions about Workato string formulas, including
  conditionals, text manipulation, and checking for substrings.
---

# String formulas FAQs

Get answers to frequently asked string formula questions.

What are string formulas in Workato?

Strings are sequences of text and characters. [String formulas](/en/formulas/string-formulas#string-formulas) in Workato are allowlisted Ruby methods that enable you to manipulate and work with strings.

What is the purpose of conditionals in string formulas?

Conditionals allow you to apply if-else logic to strings, which you can use to perform various actions based on conditions. Refer to [Conditionals](/en/formulas/conditions#conditionals) for more robust instructions on how to add conditionals to formulas.

How do I include and exclude work in string formulas?

The [`include?` formula](/en/formulas/string-formulas#include) checks if a specific substring is present in a string and returns `true` if it is found.

The [`exclude?` formula](/en/formulas/string-formulas#exclude) checks if a specific substring is _not_ present in a string and returns `true` if it is _not_ found.

Can I use text manipulation with string formulas?

Yes. You can manipulate text within strings with the following formulas:

- [`parameterize`](/en/formulas/string-formulas#parameterize)
  
  - Replaces special characters.
- [`strip`](/en/formulas/string-formulas#strip)
  
  - Removes white spaces from the beginning and end.
- [`upcase`](/en/formulas/string-formulas#upcase), [`downcase`](/en/formulas/string-formulas#downcase), [`capitalize`](/en/formulas/string-formulas#capitalize), and [`titleize`](/en/formulas/string-formulas#titleize)
  
  - Changes the case of strings depending on your required format.

Can I convert alpha-2 and alpha-3 content?

Yes. You can convert alpha-2 and alpha-3 country codes to country names or convert country names to country codes with the following formulas:

- [`to_country_alpha2`](/en/formulas/string-formulas#to-country-alpha2)
- [`to_country_alpha3`](/en/formulas/string-formulas#to-country-alpha3)
- [`to_country_name`](/en/formulas/string-formulas#to-country-name)

You can convert alpha-2 and alpha-3 country codes to currency codes or currency names with the following formulas:

- [`to_currency_code`](/en/formulas/string-formulas#to-currency-code)
- [`to_currency_name`](/en/formulas/string-formulas#to-currency-name)

What is the purpose of the ordinalize formula?

The [`ordinalize` formula](/en/formulas/string-formulas#ordinalize) turns a number into an ordinal string, such as 1st, 2nd, 3rd, and so on.

What formula should I use to convert data types?

You can use the [`to_s` formula](/en/formulas/string-formulas#to-s) to convert various data types, including numbers, dates, and more into string data types.

How do I convert the Ruby decrypt method output to a string?

The [Ruby decrypt method](/en/developing-connectors/sdk/sdk-reference/ruby_methods#decrypt) returns a byte array instead of a string by default. You can convert the decrypt method output to a string by appending the `.as_string()` or `.as_utf8` function to your formula.

---
