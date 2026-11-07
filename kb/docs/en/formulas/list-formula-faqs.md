---
url: 'https://docs.workato.com/en/formulas/list-formula-faqs.md'
description: >-
  Find answers to common questions about list and hash formulas in Workato,
  including indexing, negative indexes, first, and last.
---

# List and hash formulas FAQs

Get answers to frequently asked list and hash formula questions.

How are lists used in Workato?

A [list in Workato](/en/formulas/array-list-formulas#lists-arrays) is an ordered, integer-indexed collection of objects, similar to arrays in other programming languages.

How do you access items inside a list in Workato?

You can [access items in a list](/en/formulas/array-list-formulas#lists-arrays) using indexing, starting at 0. For example, `number_list[0]` would access the first line item.

Does Workato support negative indexes for lists?

Yes, [Workato supports negative indexes](/en/formulas/array-list-formulas#lists-arrays) for lists. For example, `number_list[-1]` would access the last item in a list.

What do the first and last formulas do?

The [`first` formula](/en/formulas/array-list-formulas#first) returns the first item in a list. The [`last` formula](/en/formulas/array-list-formulas#last) returns the last item in a list.

What is a hash, and how does it differ from a list?

A [hash in Workato](/en/formulas/array-list-formulas#hashes) is a collection of unique keys and their corresponding values. Unlike lists, hashes allow you to use any object type as keys.

How are lists of hashes used?

[Lists of hashes](/en/formulas/array-list-formulas#lists-of-hashes) represent complex data structures where each item in the list is a hash with multiple key-value pairs. Lists of hashes are often used for organizing and processing structured data.

How do you access values in a hash?

You can [access values in a hash](/en/formulas/array-list-formulas#lists-of-hashes) using the keys. For example, `line_item["item_name"]` accesses the value associated with the `item_name` key.

Is there a direct union (&) operand for combining lists in Workato?

Workato doesn't support a direct union (&) operand. To achieve a similar result, you can combine lists using the [`concat` formula](/en/formulas/array-list-formulas#concat) and then remove duplicates with the [`uniq` formula](/en/formulas/array-list-formulas#uniq). [Learn how](/en/formulas/array-list-formulas#union).

How can you find the difference between two lists?

To find [the difference between two lists](/en/formulas/array-list-formulas#difference), you can use the subtraction (-) operand. For example, `list - updated_list` returns the items present in `list` but not in `updated_list`.

---
