---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-get-case-comments-action.md
description: >-
  The Get case comments action in the NetSuite SOAP connector retrieves the case
  comments of a specific case in NetSuite by its case ID.
---

# NetSuite SOAP - Get case comments action

The action `Get case comments` allows you to retrieve the case comments of a specific case in NetSuite by its case ID.

![Get case comments](/assets/case-comments.BLPUZFfg.png)

## Input

- Case ID
  
- The Netsuite case's ID
  
- Results list page size
  
- The number of records to return. The maximum is 200 and the default is 25.
  
- Search ID
  
- Returned from a previous "Get case comments" action
  
- Page number
  
- Used in conjunction with Search ID to page through results
  

## Output

- Search ID
  
- Used in a downstream "Get case comments" action to page through results
  
- Page number
  
- Used in a downstream "Get case comments" action to page through results
  
- Total pages
  
- Total pages of results in the search
  
- Messages
  
- An array of cases
  

## Page through results to retrieve all case comments

Using the `foreach` loop in Workato, you can easily page through all case comments and back them up into a database for storage.

Check out [this sample recipe](https://www.workato.com/recipes/1084569?st=517170) for more details.
