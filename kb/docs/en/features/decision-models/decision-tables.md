---
url: 'https://docs.workato.com/en/features/decision-models/decision-tables.md'
description: >-
  Learn how Workato decision tables automate business rules by evaluating rows
  of conditions in sequence and returning matching output values.
---

# Decision tables

Decision tables are an industry-standard tool for automating business rules that involve multiple conditions and a large number of possible combinations. The table's row-based format helps you verify that all possible conditions are covered in complex workflows.

Workato decision tables receive inputs from a preceding connected node, such as a **Model Inputs** node, another decision table, or a conditional branch. Each row in a decision table defines a complete rule, with conditions and corresponding outputs. The table evaluates rows in sequence. It begins at the top and checks each row to determine whether the input values meet all specified conditions. The table stops evaluation when the input values match all conditions in a row and returns the row's **Output** values for further processing by the model.

The table returns a **Default output** for each output field if no row matches. You configure these defaults during table setup. The outputs from a decision table are available as inputs for the next node in the model.

![Example decision table for routing marketing leads](/assets/decision-table.DubRYOmN.png)_Example decision table for routing marketing leads_

> **ADDITIONAL RESOURCES**
> 
> Refer to the following articles for more information about decision tables:
> 
> - [Decision models](/en/recipes/decision-models): An overview of decision models and their components.
> - [Set up a decision model](/en/features/decision-models/model-builder): Model creation and configuration instructions.
> - [Model fields](/en/features/decision-models/model-builder#model-fields): Information about model fields and how data moves through a decision model.
> - [Decision Models connector](/en/features/decision-models/decision-models-by-workato): Information about recipe integration.

## Limitations

Each decision table supports a maximum 2,000 rows, 20 input columns, and 20 output columns.

## Create a decision table

Complete the following steps to create a decision table:

1. Go to the toolbar and drag a **Decision table** node into the model builder.
   
2. Click and drag between edges to configure the order of nodes. You can hover over a node connection and click **Delete edge** to remove it.
   
   ![Add the node to the model flow](/assets/new-table-flow.DwB5VXZa.gif)_Add the node to the model flow_
   
3. Select the **Decision table** node.
   
4. Optional. Edit the automatically generated table **Name**.
   
   ![Decision model node configuration](/assets/configure-decision-table-node.ZkoXk-YU.png)_Decision model node configuration_
   
5. Optional. Enter a **Description** for the table.
   
6. Click **Configure table** to open the decision table.
   
7. Click **+** (Add inputs). Inputs provide data to evaluate using the table's business rules.
   
   ![Click Add inputs](/assets/add-inputs.B3nqbXny.png)_Click **+** (Add inputs)_
   
8. Select existing fields or create a new input field:
   
   **Select existing fields**
   
   1. Select existing fields to evaluate. You can select fields output by directly connected upstream nodes and all fields from the **Model Inputs** node.
      
      ![Select fields for the table to evaluate](/assets/select-inputs.B96dnVQG.png)_Select fields for the table to evaluate_
      
   2. Click **Add**.
      
   
   **Create a new input field**
   
   1. Click **\+ Create input**.
      
      ![Select fields for the table to evaluate](/assets/select-inputs.B96dnVQG.png)_Select fields for the table to evaluate_
      
   2. Enter a **Name** for the input field.
      
      ![Input field configuration](/assets/input-field-configuration.BlcsIYQK.png)_Input field configuration_
      
   3. Optional. Edit the automatically generated **Label** that identifies the field.
      
   4. Select the field's **Data type**. Refer to the [Available operators](/en/features/decision-models/decision-tables#available-operators) documentation to see the condition operators each data type supports.
      
   5. Optional. Enter a **Hint** that explains the field. Hints display in decision tables and help users understand the purpose of each field.
      
   6. Optional. Click the **Set as required** toggle to make the field mandatory when [calling the model from a recipe](/en/features/decision-models/decision-models-by-workato).
      
   7. Click **Create input**. The field becomes an input for the current table and you can add the field to other nodes in the model.
      
      To set the value of a model input field, you must configure the field in the recipe that calls the decision model. Refer to the [Model fields](/en/features/decision-models/model-builder#model-fields) section for more information.
      
   
9. Click **+** (Add outputs). Output fields pass values to the next node based on the table's decisions.
   
   ![Click Add outputs](/assets/add-outputs.B1uLIXJj.png)_Click **+** (Add outputs)_
   
10. Select existing fields or create a new model field:
    
    **Select existing fields**
    
    1. Select existing fields to output. You can select any model field as an output, including those already used as inputs in the same table.
       
       ![Select fields to pass from this table to the next node](/assets/select-outputs.DK8mAgIL.png)_Select fields to pass from this table to the next node_
       
    2. Click **Add**.
       
    
    **Create a new model field**
    
    1. Click **\+ Create output**.
       
       ![Select fields to pass from this table to the next node](/assets/select-outputs.DK8mAgIL.png)_Select fields to pass from this table to the next node_
       
    2. Enter a **Name** for the field.
       
    3. Optional. Edit the automatically generated **Label** that identifies the field.
       
    4. Select the field's **Data type**. Refer to the [Available operators](/en/features/decision-models/decision-tables#available-operators) documentation to see the condition operators each data type supports.
       
    5. Optional. Enter a **Hint** that explains the field. Hints display in decision tables and help users understand the purpose of each field.
       
    6. Click **Create output**. The model field is now an output for the table and can be added to other nodes in the model.
       
    

### Configure decision table rules

Complete the following steps to configure a decision table rule:

1. Select the **Decision table** node to configure. ![Decision model node configuration](/assets/configure-decision-table-node.ZkoXk-YU.png)_Decision model node configuration_
   
2. Click **Configure table** to open the decision table.
   
3. Create a new rule using one of the following methods:
   
   - Click **+**.
   - Press `Shift` and `Enter`.
   - Press `Ctrl` and click on a row's number, then click **Insert rule above** or **Insert rule below**.
   
   ![Create a new rule](/assets/add-new-rule.BZZ4cTYU.png)_Create a new rule_
   
4. Optional. Enter a name for the rule in the **Rule name** column. Naming rules helps verify coverage and simplifies maintenance.
   
5. Complete the following steps to configure cells in the **Conditions** section:
   
   1. Select the cell to configure.
      
   2. Select an operator from the drop-down menu. Refer to the [Available operators](#available-operators) section to see the operators available for each data type. Cells default to the `any` operator, which matches any inputs provided.
      
      ![Select an operator from the drop-down menu](/assets/operand-drop-down.D_2EvgfO.png)_Select an operator from the drop-down menu_
      
   3. Enter a value to compare against the input using the operator.
      
6. Enter output values for rules in the **Outputs** section.
   
7. Optional. Enter a **Default output** to return for each output field if no rules match the inputs provided or if the matching rule's output cell is blank. Meaningful default outputs help when your rules don't cover all possible inputs, or when inputs change unexpectedly as your workflows develop.
   
   ![Enter a Default output for each output field](/assets/default-outcomes.t15VMFrX.png)_Enter a **Default output** for each output field_
   

## Available operators

The operators available for a condition vary depending on the column's data type.

String

The following operators are available for the `String` data type:

- Any
- Contains
- Does not contain
- Starts with
- Does not start with
- Ends with
- Does not end with
- Equals
- Does not equal
- Is present
- Is not present

Number

The following operators are available for the `Number` data type:

- Any
- Equals
- Does not equal
- Greater than
- Greater than or equal to
- Less than
- Less than or equal to
- Is present
- Is not present
- Is between
- Is not between

Integer

The following operators are available for the `Integer` data type:

- Any
- Equals
- Does not equal
- Greater than
- Greater than or equal to
- Less than
- Less than or equal to
- Is present
- Is not present
- Is between
- Is not between

Boolean

The following operators are available for the `Boolean` data type:

- Any
- Is true
- Is false

Date

The following operators are available for the `Date` data type:

- Any
- Equals
- Does not equal
- Is before
- Is after
- Is on or before
- Is on or after
- Is present
- Is not present
- Is between
- Is not between

Date time

The following operators are available for the `Date time` data type:

- Any
- Equals
- Does not equal
- Is before
- Is after
- Is on or before
- Is on or after
- Is present
- Is not present
- Is between
- Is not between

---

---
url: >-
  https://docs.workato.com/en/features/decision-models/decision-models-by-workato.md
description: >-
  Use the Make a decision action in the Decision Models by Workato connector to
  call a decision model from a recipe and return its results.
---

# Decision Models by Workato connector - Make a decision action

The **Decision Models by Workato** connector allows you to use the **Make a decision** action to call an existing [decision model](/en/recipes/decision-models) from a recipe, including skill recipes used by genies and MCP servers. This behavior is similar to the [Recipe functions](/en/connectors/recipe-functions) connector, which calls an existing recipe. The decision model uses business logic to process the **Input values** you provide and returns the results for use in downstream recipe steps.

### Input

| Input field | Description |
| --- | --- |
| Model name | Select the model to call. |
| Input values | Provide values for the model's input fields. Refer to [Create an input field](/en/features/decision-models/model-builder#create-an-input-field) to configure a model's input schema. |

### Output

| Output field | Description |
| --- | --- |
| Model outputs | Contains fields defined in the model's output schema. The business logic of the model determines the values in these fields. Refer to [Configure output fields](/en/features/decision-models/model-builder#configure-output-fields) to configure a model's output schema. |
| Decision path | Contains the following information about each decision table or conditional node that was processed: **ID**: The unique identifier for the node., **Input**: Contains the fields that were passed to the node and their values., **Name**: The name of the node., **Output**: Contains the fields that were output by the node and their values., **List size**: The total number of nodes visited., **List index**: The position of the current node in the list. |

---
