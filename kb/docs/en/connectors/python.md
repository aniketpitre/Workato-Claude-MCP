---
url: 'https://docs.workato.com/en/connectors/python.md'
description: >-
  The Python snippets by Workato connector enables you to write and run custom
  Python code in recipes to transform data and convert file formats.
---

# Python snippets by Workato

The Python snippets by Workato connector allows you to write and execute custom [Python](https://www.python.org/) code in your recipes.

Python is a popular programming language used for web applications, data pipelines, and machine learning.

Workato's Python snippets by Workato connector enables you to perform the following tasks:

- Transform data, such as converting date formats.
- Convert file formats, such as CSV to JSON.
- Process large datasets by breaking batches into smaller chunks, such as splitting 5,000 records into chunks of 500 to prevent API timeouts.

Learn more about [executing Python code](/en/connectors/python/actions/execute-python-code).

## Use cases

Use Python to automate complex workflows, process data, and enhance integrations across your business applications. The Python snippets by Workato connector provides flexibility and control to generate reports, transform datasets, and script custom automations. Explore our [use cases](/en/getting-started/workato-use-cases) to discover how you can improve automation with Python:

- [Export Workday workers to a CSV file](/en/getting-started/use-cases/workday-python-google-drive) with Python and upload the file to Google Drive.

## Supported features

- [Runtime version](#runtime-version)
- [Libraries](#libraries)

### Runtime version

The Python snippets by Workato connector runs on Python 3.9 or later.

### Libraries

The connector supports the [standard libraries included in Python 3.9 or later](https://docs.python.org/3.9/library/index.html) and the following additional libraries:

| Library | Supported version |
| --- | --- |
| [bcrypt](https://github.com/pyca/bcrypt/) | `5.0.0` |
| [certifi](https://github.com/certifi/python-certifi) | `2026.1.4` |
| [cffi](https://cffi.readthedocs.io/) | `2.0.0` |
| [charset-normalizer](https://charset-normalizer.readthedocs.io/) | `3.4.4` |
| [cryptography](https://cryptography.io/) | `46.0.5` |
| [et\_xmlfile](https://pypi.org/project/et-xmlfile/) | `2.0.0` |
| [idna](https://github.com/kjd/idna) | `3.11` |
| [lxml](https://lxml.de/) | `6.0.2` |
| [msgpack](https://msgpack.org/) | `1.1.2` |
| [msoffcrypto-tool](https://github.com/nolze/msoffcrypto-tool) | `5.4.2` |
| [numpy](https://numpy.org/) | `2.0.2` |
| [olefile](https://olefile.readthedocs.io/) | `0.47` |
| [openpyxl](https://openpyxl.readthedocs.io/) | `3.1.5` |
| [pandas](https://pandas.pydata.org/) | `2.3.3` |
| [pillow](https://python-pillow.org/) | `11.3.0` |
| [pycparser](https://github.com/eliben/pycparser) | `2.23` |
| [pypdf](https://pypdf.readthedocs.io/) | `6.7.1` |
| [python-dateutil](https://dateutil.readthedocs.io/) | `2.9.0.post0` |
| [python-pptx](https://python-pptx.readthedocs.io/) | `1.0.2` |
| [pytz](https://pythonhosted.org/pytz/) | `2025.2` |
| [pyxlsb](https://pypi.org/project/pyxlsb/) | `1.0.10` |
| [requests](https://docs.python-requests.org/) | `2.32.5` |
| [six](https://six.readthedocs.io/) | `1.17.0` |
| [typing\_extensions](https://typing-extensions.readthedocs.io/) | `4.15.0` |
| [tzdata](https://pypi.org/project/tzdata/) | `2025.3` |
| [urllib3](https://urllib3.readthedocs.io/) | `2.6.3` |
| [xlrd](https://xlrd.readthedocs.io/) | `2.0.2` |
| [xlsxwriter](https://xlsxwriter.readthedocs.io/) | `3.2.9` |

Additional libraries aren't currently supported.

## Quotas

The Python snippets by Workato connector has the following quotas:

| Description | Quota | Notes |
| --- | --- | --- |
| Memory quota for Python connector actions, including libraries, temporary memory, and inputs | 256 MB | NA |
| Timeout for Python connector actions | 90 seconds | NA |
| Maximum code field size (scripts) for Python connector actions | 1 MB | NA |
| Maximum size quota for PDF files processed with the pypdf library | 35 MB | NA |
| Maximum size quota for CSV files processed with the Pandas library | 20 MB | This quota accounts for Pandas’ temporary storage requirements. |
| Maximum size quota for Excel files processed with the Pandas library | 5 MB | Uncompressing Excel files requires additional memory. |
| Read request timeout for Python evaluation in actions | 90 seconds | This quota applies to the following action: **Invoke custom Python code** action |

Additionally, user-provided [libraries](#libraries) are not supported.

## Actions

The Python snippets by Workato connector supports the following action:

- [Execute Python code](/en/connectors/python/actions/execute-python-code)

## Connecting to Workato

The Python snippets by Workato connector doesn't require setup configuration. Search for **Python** in the **App** tab and click the icon to get started.

---
