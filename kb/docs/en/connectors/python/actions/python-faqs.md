---
url: 'https://docs.workato.com/en/connectors/python/actions/python-faqs.md'
description: >-
  Answers to frequent questions about the Workato Python connector, including
  supported versions, libraries, actions, limitations, and setup.
---

# Python FAQs

Get answers to frequently asked questions about Python.

What can I do with the Python connector in Workato?

The [Python connector](/en/connectors/python#python) allows you to write and execute custom Python code as part of a recipe. You can use this connector to develop web applications, data pipelines, and machine learning projects.

What are common uses for the Python connector?

Common uses for the Python connector include:

- Data transformation (such as date formats)
- File format conversion (for example, CSV to JSON)
- Data set chunking to prevent API timeouts

Refer to [Use cases](/en/connectors/python#use-cases) for more ways to use Python.

Which version of Python does the Workato Python connector use?

The Python connector in Workato runs [Python 3.9 or later](/en/connectors/python#runtime-version).

What libraries are supported by the Workato Python connector?

The Python connector supports all standard [libraries](/en/connectors/python#libraries) included in Python 3.9 or later. The Python connector also supports the following libraries:

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

> **LIMITED LIBRARY SUPPORT**
> 
> The Python connector does not support user-provided libraries or libraries not listed in the preceding list.

Are there any limitations to using the Python connector in Workato?

Yes, you should consider the following [limitations](/en/connectors/python#limitations) when using the Python connector:

| Description | Quota | Notes |
| --- | --- | --- |
| Memory quota for Python connector actions, including libraries, temporary memory, and inputs | 256 MB | NA |
| Timeout for Python connector actions | 90 seconds | NA |
| Maximum code field size (scripts) for Python connector actions | 1 MB | NA |
| Maximum size quota for PDF files processed with the pypdf library | 35 MB | NA |
| Maximum size quota for CSV files processed with the Pandas library | 20 MB | This quota accounts for Pandas’ temporary storage requirements. |
| Maximum size quota for Excel files processed with the Pandas library | 5 MB | Uncompressing Excel files requires additional memory. |
| Read request timeout for Python evaluation in actions | 90 seconds | This quota applies to the following action: **Invoke custom Python code** action |

What actions are supported by the Python connector in Workato?

The primary [action](/en/connectors/python#actions) supported by the Python connector is `Execute Python code`. This allows you to run custom Python scripts within a recipe.

Do I need to perform any setup configuration to use the Python connector in Workato?

No specific [setup configuration](/en/connectors/python#connection-setup) is required for the Python connector. You can search for and select Python in the **Apps** tab to start using it.

---
