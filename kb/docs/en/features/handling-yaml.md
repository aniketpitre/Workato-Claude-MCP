---
url: 'https://docs.workato.com/en/features/handling-yaml.md'
description: >-
  Learn how Workato handles YAML content, using YAML tools by Workato to parse
  files and extract structured values during recipe execution.
---

# Handling YAML

YAML (YAML Ain’t Markup Language) is a human-readable format for structured data. It uses `key: value` pairs and supports lists, nested objects, and dictionaries. YAML is commonly used in configuration files and metadata headers.

Some integrations provide YAML files or embed YAML in multi-format documents. You can use Workato to extract structured values from this content during recipe execution.

## YAML tools by Workato

Use [YAML tools by Workato](/en/connectors/yaml-by-workato) when you need to extract values from raw YAML content. You can parse YAML files from Dropbox, SFTP, or Google Drive, or extract metadata from document headers written in YAML. It also supports reading YAML content from any step that outputs file content.

YAML tools by Workato provides the [Parse YAML document](/en/connectors/yaml-by-workato/parse-yaml-action) action. This action uses a sample YAML snippet to define the output structure and returns structured datapills based on the file content.

---
