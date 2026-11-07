---
url: 'https://docs.workato.com/en/resources/recipe-integration.md'
description: Use resources as data sources in recipe actions.
---

# Recipe integration

Refer to the following sections to use resources as data sources in recipes:

- [Supported actions](#supported-actions): How to use resources in the actions that support them.
- [Use cases](#use-cases): Common use cases for resources in recipes.
- [File references](#file-references): How a resource resolves relative and absolute references to other files.

> **VERSION UPDATES**
> 
> Resource references use the latest safe version at runtime. You can't prevent a reference from updating. Refer to [Restore a resource version](/en/resources/resource-management#restore-a-resource-version) to restore a resource to a previous version.

## Supported actions

Select **Use a resource** in the following actions' input fields to reference a resource as a data source:

- [Validate XML document with XSD](/en/features/validate-xml-with-xsd): Use resources as XSD schemas.
  
- [Transform XML using XSLT](/en/features/transform-xml-using-xslt): Use resources as XSLT stylesheets.
  
- [Generate XML document from a sample XML](/en/features/generate-xml-from-xml): Validate the generated XML against an XSD schema stored as a resource.
  
- [Execute Python code](/en/connectors/python/actions/execute-python-code): Use a resource as the Python snippet to run.
  
- [Execute Ruby code](/en/connectors/ruby-snippets-by-workato): Use a resource as the Ruby snippet to run.
  

## Use cases

The following examples are common use cases for resources:

- SOAP API management
  
- Manage WSDL files used by SOAP services. Workato stores uploaded WSDL files as resources to keep API recipes and service definitions in sync throughout the recipe lifecycle.
  
- XSLT transformation
  
- Transform XML documents using XSLT stylesheets stored as resources. You can optionally validate the transformation output against an XSD resource to ensure the result conforms to your expected schema.
  
- Generate XML with XSD
  
- Generate XML documents using an XSD resource to define the structure. You can optionally validate the generated output against the same or a different XSD resource.
  
- Parse XML documents
  
- Parse XML documents using generic parsing capabilities. You can optionally validate the source XML document against an XSD resource before processing.
  
- Local XSD reference resolution
  
- Resolve references across multi-file XSD setups stored within your Workato project folder structure. Resources follow relative and absolute file paths automatically, without accessing external internet locations.
  

## File references

Use the `schemaLocation` attribute to resolve paths in XSD files, or the `href` attribute to resolve paths in XSLT files. Relative paths start from the current file's location. Absolute paths start with `/` (forward slash) and resolve from the root of the Workato directory.

**XSD**

```xml
<s:import namespace="http://example.org/orders" schemaLocation="relative/path/orders.xsd"/>
<s:import namespace="http://example.org/common" schemaLocation="/absolute/path/common.xsd"/>
```

**XSLT**

```xml
<xsl:import href="relative/path/base.xslt"/>
<xsl:import href="/absolute/path/base.xslt"/>
```

Use `import` and `include` to reference external files within the current file:

**XSD**

Use `import` in an XSD file to reference a schema with a different namespace from the parent schema, and `include` to reference a schema with the same namespace.

```xml
<s:import namespace="http://different-namespace.org/products" schemaLocation="products.xsd"/>
<s:include schemaLocation="shared-types.xsd"/>
```

**XSLT**

Use `import` in an XSLT file to reference a stylesheet with lower precedence, and `include` to inline a stylesheet at the same precedence level.

```xml
<xsl:import href="base-templates.xslt"/>
<xsl:include href="shared-helpers.xslt"/>
```

---
