---
url: 'https://docs.workato.com/en/connectors/python/actions/execute-python-code.md'
description: >-
  The Execute Python code action in the Python connector runs a custom Python
  script in a recipe using your defined input and output fields.
---

# Python - Execute Python code action

This action executes a custom Python script.  
  

* * *

## Limitations

When using this action, note the following limitations:

| Description | Quota | Notes |
| --- | --- | --- |
| Memory quota for Python connector actions, including libraries, temporary memory, and inputs | 256 MB | NA |
| Timeout for Python connector actions | 90 seconds | NA |
| Maximum code field size (scripts) for Python connector actions | 1 MB | NA |
| Maximum size quota for PDF files processed with the pypdf library | 35 MB | NA |
| Maximum size quota for CSV files processed with the Pandas library | 20 MB | This quota accounts for Pandas’ temporary storage requirements. |
| Maximum size quota for Excel files processed with the Pandas library | 5 MB | Uncompressing Excel files requires additional memory. |
| Read request timeout for Python evaluation in actions | 90 seconds | This quota applies to the following action: **Invoke custom Python code** action |

Additionally, user-provided libraries aren't supported. Refer to the [Python connector overview](/en/connectors/python#libraries) for a list of supported libraries.

* * *

## Input

| Field | Description |
| --- | --- |
| **Name** | Enter a brief description of the step. For example: `Transform dates` |
| **Input fields** | Define the input fields to pass to your code. You can define the input by manually adding fields one at a time or providing a JSON sample. **Note:** `Date` and `datetime` data will be passed as `string`. [Check out an example](#working-with-datetime-data). |
| **Output fields** | Define the fields that will create the [Output datatree](#output). You can define the output by manually adding fields one at a time or providing a JSON sample. |
| **Python snippet source** | Select **Define manually** to write the Python snippet directly in this action, or select **Use a resource** to use a [resource](/en/resources.html) as the Python snippet. |
| **Python Snippet Resource** | Select the resource to use as the Python snippet. This field appears when you select **Use a resource** in the **Python snippet source** drop-down menu. |
| **Code** | Your custom Python script. This field appears when you select **Define manually** in the **Python snippet source** drop-down menu. When writing your script, note that: Code must be in the `main` function; The `main` function can only have one parameter. This parameter must be a Python dict that contains the variables defined as **Input fields**. [Check out an example](#working-with-input-and-output-data).; To pass data to **Output fields**, `return` a dictionary with keys that match the **Output** schema you defined. [Check out an example](#working-with-input-and-output-data).; This action has some [limitations](#limitations) |

### Examples

- [Working with input and output data](#working-with-input-and-output-data)
- [Working with datetime data](#working-with-datetime-data)

#### Working with input and output data

In this example, we'll demonstrate how **Input fields** data can be accessed in your script then passed to your defined **Output fields**.

Let's say the configuration for our action looks like this:

| Input Fields | Output Fields |
| --- | --- |
| The following fields are defined as **Input fields** for the action: **x**, **y**, **z** | The following fields are defined as **Output fields** for the action: **shape**, **dimensions** |

In this example, the parameter in our `main` function is named `input`. We'll use this to access the values of our action's defined **Input fields**.

To pass the resulting data to our **Output fields**, we'll include a dictionary with keys that match the output schema.

```python
import numpy as np

def main(input):
  # # Access the values of the action's Input fields
  x = input['x']
  y = input['y']
  z = input['z']
  size = (x, y, z)

  # Create a 3D NumPy array with random integers
  my3dArray = np.random.randint(low=0, high=100, size=size, dtype=int)
  print("/nRandom array/n", my3dArray)

  # Keep only elements that are multiples of 5
  modified3dArray = np.where(my3dArray % 5 == 0, my3dArray, 0)
  print("\Only multiples of 5\n", modified3dArray)

  shape = str(modified3dArray.shape)
  dimensions = modified3dArray.ndim

  # Pass shape and dimension values to Output fields
  return {"shape": shape, "dimensions": dimensions}
```

#### Working with datetime data

In this example, we'll demonstrate how to work with `datetime` data in your Python scripts.

**Input fields** typed as `Date` will be passed as `strings` to your Python code. To ensure data is formatted as you expect, we recommend accounting for this in your code.

```python
import datetime as dt

def main(input)
  when = dt.datetime.fromisoformat(input['when'])
  # use datetime object when
  # ...
  # convert to custom format
  when_converted = when.strftime("%d %b %Y %H:%M:%S")
  return {"when": when_converted}
```

* * *

#### Logging

To help with development and debugging, Workato supports logging intermediate values using `print` statements. Note that Workato only displays `print` statements inside the `main` function. Each `print` statement is displayed as a new line.

![print](/assets/print-functionality.7sGuOkFg.png)_Output of print statements inside main function_

## Output

Every field defined in the **Output fields** section creates a datapill in the action's [Output datatree](/en/workato-concepts#datatree-and-datapills).

For example: Let's say we defined the following as **Output fields**:

- **shape** (`integer`)
- **dimensions** (`integer`)

In this case, the action's Output datatree will look like this:

```shell
└── Output
    ├── shape (integer)
    └── dimensions (integer)
```

**Need help passing data to your Output fields?** Check out the [example](#working-with-input-and-output-data).

## Error stacktrace

When the "Execute Python code" action fails due to an error inside the `main` function, Workato displays the relevant error stacktrace to help you debug your code.

![Error stacktrace](/assets/python-error-stacktrace.Ca2CGITc.png)_Sample error stacktrace_

---
