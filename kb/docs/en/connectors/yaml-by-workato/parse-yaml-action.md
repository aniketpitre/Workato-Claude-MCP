---
url: 'https://docs.workato.com/en/connectors/yaml-by-workato/parse-yaml-action.md'
description: >-
  This action parses raw YAML content into structured datapills based on a
  sample document.
---

# YAML tools by Workato - Parse YAML document action

The **Parse YAML document** action extracts values from raw YAML content and converts them into structured datapills for use in recipes. You can use this action to parse full YAML files or YAML headers embedded in other file formats.

## Input

| Input field | Description |
| --- | --- |
| Sample YAML document | Provide a sample YAML snippet that defines the structure of your content. Workato uses this to generate the output schema. |
| YAML content | Provide the actual YAML content to parse. This may come from a downloaded file or the output of a previous step. |

> **DOWNLOAD A YAML FILE**
> 
> You can use a download action from connectors such as [Dropbox](/en/connectors/dropbox) or [File tools by Workato](/en/features/file-tools-by-workato) to download a YAML file into Workato for this action's input.

## Output

Workato generates datapills based on the structure defined in the **Sample YAML document** field. These may include strings, lists, nested objects, and arrays.

## Example usage

This example parses a YAML structure that contains employee records. Each record includes simple fields, arrays, and nested lists or dictionaries.

```yaml
  - employee_1:
    Name: Martin Simon
    Age: 25
    Title: Technical Manager
    Employed: True
    Introduction_string:
        Hi i love to play football
    Responsibilities_list:
        - sales rep
        - fire safety committee
        - first aid
    Languages_NestedList:
        - [perl, elite]
        - [python, Elite]
        - [pascal, Fundamental]
    Education_dictionary:
        Bachelors:
          School : UCLA
          Degree : BSc in IoT
          GPA : 4.3
        PostGrad:
          School : MIT
          Degree : PhD in CS
          GPA : 4.2
```

Workato uses this as a sample structure and returns corresponding datapills for each key.

![Parse YAML content](/assets/YAML-parser-by-workato.imVTomwM.png)_Parse YAML content. Refer to the [sample recipe](https://www.workato.com/recipes/969549) for a working example._

You can also parse metadata stored in YAML headers within other file formats. These YAML headers appear at the top of a file, between `---` lines. For example:

```yaml
---
title: "Edinburgh Biodiversity"
author: John Doe
date: 22/Oct/2016
output: html_document
---
```

The action parses only the YAML block between the boundaries and ignores the rest of the file.

![Parse YAML content in other file types](/assets/parse-yaml-in-other-types.B1nJdGIL.png)_Parse YAML content in other file types_

---
