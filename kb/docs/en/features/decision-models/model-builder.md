---
url: 'https://docs.workato.com/en/features/decision-models/model-builder.md'
description: >-
  Set up a decision model in Workato to create and configure business logic that
  processes input values and returns decision results.
---

# Set up a decision model

Use the following sections to create and configure a [decision model](/en/recipes/decision-models):

- [Create a decision model](#create-a-decision-model)
- [Configure a decision model](#configure-a-decision-model)

## Create a decision model

Complete the following steps to create a decision model:

1. Go to **Projects > All assets**.
   
2. Click **Create > Decision model** or press C+D.
   
3. Enter a **Decision model name**.
   
   ![Enter a Decision model name](/assets/set-up-decision-model.JxRNtltV.png)_Enter a **Decision model name**_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the decision model.
   
5. Click **Start building**. The decision model builder opens.
   
6. Refer to the [Configure a decision model](#configure-a-decision-model) section to configure the model.
   

## Configure a decision model

You can access decision models from **Assets > Decision models** or from a specific project.

Refer to the following guides to configure a decision model:

Create an input field

### Create an input field

Input fields define the data that enters your model. This is usually the core data evaluated by **Decision table** nodes. Input fields are available to all nodes, including nodes not directly connected to the **Model Inputs** node.

> **RETURN INPUT FIELDS UNCHANGED**
> 
> You can select input fields in the [Model Outputs node](#configure-output-fields) to return them to the calling recipe. This helps in cases where the input value isn't otherwise available in the recipe, such as when a formula calculates the value in the input field.

Complete the following steps to create an input field using the **Model Inputs** node or the decision table's **Inputs** section:

**Model Inputs node**

1. Select the **Model Inputs** node.
   
2. Click **Create input** if there are no existing fields. Otherwise, click **+** (Create input).
   
   ![Create a new field](/assets/create-field.aWO80F_Z.png)_Create a new field_
   
3. Enter a **Name** for the input field.
   
   ![Input field configuration](/assets/input-field-configuration.BlcsIYQK.png)_Input field configuration_
   
4. Optional. Edit the automatically generated **Label** that identifies the field.
   
5. Select the field's **Data type**. Refer to the [Available operators](/en/features/decision-models/decision-tables#available-operators) documentation to see the condition operators each data type supports.
   
6. Optional. Enter a **Hint** that explains the field. Hints display in decision tables and help users understand the purpose of each field.
   
7. Optional. Click the **Set as required** toggle to make the field mandatory when [calling the model from a recipe](/en/features/decision-models/decision-models-by-workato).
   
8. Click **Create input**. You can now add the field to other nodes in the model as an input.
   

To set the value of a model input field, you must configure the field in the recipe that calls the decision model. Refer to the [Model fields](/en/features/decision-models/model-builder#model-fields) section for more information.

**Decision table**

1. Select the **Decision table** node to create the input field in. ![Decision model node](/assets/configure-decision-table-node.ZkoXk-YU.png)_Decision model node_
   
2. Click **Configure table** to open the decision table.
   
3. Click **+** (Add inputs).
   
   ![Click Add inputs](/assets/add-inputs.B3nqbXny.png)_Click **+** (Add inputs)_
   
4. Click **\+ Create input**.
   
   ![Select fields for the table to evaluate](/assets/select-inputs.B96dnVQG.png)_Select fields for the table to evaluate_
   
5. Enter a **Name** for the input field.
   
   ![Input field configuration](/assets/input-field-configuration.BlcsIYQK.png)_Input field configuration_
   
6. Optional. Edit the automatically generated **Label** that identifies the field.
   
7. Select the field's **Data type**. Refer to the [Available operators](/en/features/decision-models/decision-tables#available-operators) documentation to see the condition operators each data type supports.
   
8. Optional. Enter a **Hint** that explains the field. Hints display in decision tables and help users understand the purpose of each field.
   
9. Optional. Click the **Set as required** toggle to make the field mandatory when [calling the model from a recipe](/en/features/decision-models/decision-models-by-workato).
   
10. Click **Create input**. The field becomes an input for the current table and you can add the field to other nodes in the model.
    

To set the value of a model input field, you must configure the field in the recipe that calls the decision model. Refer to the [Model fields](/en/features/decision-models/model-builder#model-fields) section for more information.

Delete an input field

### Delete an input field

Complete the following steps to delete an input field:

> **REMOVE INSTANCES BEFORE DELETING**
> 
> You can't delete an input field that's in use. You must remove the field from all nodes before you can delete it.

1. Select the **Model Inputs** node.
   
2. Hover over the field to delete and click **...** (ellipsis).
   
   ![Click the ellipsis on the field to delete](/assets/select-field.CcxyQHOm.png)_Click the ellipsis on the field to delete_
   
3. Click **Delete** (trash icon).
   
   ![Click Delete](/assets/delete-field.D4wVTtUh.png)_Click **Delete** (trash icon)_
   
4. Click **Delete** again to confirm the deletion.
   

Create a model field

### Create a model field

[Model fields](#model-fields) define the data passed between nodes. Model fields are required even in simple single-table models, where they carry table outputs to the **Model Outputs** node, and become increasingly important in more complex models where they pass outputs between nodes as intermediate values.

> **OVERRIDING VALUES**
> 
> You can reuse a model field as an output in multiple nodes. Each node can overwrite the field value.

Complete the following steps to create a model field using the **Fields** sidebar or the decision table's **Outputs** section:

**Fields sidebar**

1. Go to the toolbar and click **Fields**. The **Fields** sidebar opens.
   
   ![The Fields sidebar](/assets/model-fields-sidebar.CsI82MNe.png)_The **Fields** sidebar_
   
2. Click **Create field** if there are no existing fields. Otherwise, click **+** (Create field).
   
3. Enter a **Name** for the field.
   
4. Optional. Edit the automatically generated **Label** that identifies the field.
   
5. Select the field's **Data type**. Refer to the [Available operators](/en/features/decision-models/decision-tables#available-operators) documentation to see the condition operators each data type supports.
   
6. Optional. Enter a **Hint** that explains the field. Hints display in decision tables and help users understand the purpose of each field.
   
7. Click **Create field**. You can now add this field to nodes in the model.
   

**Decision table**

1. Select the **Decision table** node to create the field in. ![Decision model node](/assets/configure-decision-table-node.ZkoXk-YU.png)_Decision model node_
   
2. Click **Configure table** to open the decision table.
   
3. Click **+** (Add outputs).
   
   ![Click Add outputs](/assets/add-outputs.B1uLIXJj.png)_Click **+** (Add outputs)_
   
4. Click **\+ Create output**.
   
   ![Select fields to pass from this table to the next node](/assets/select-outputs.DK8mAgIL.png)_Select fields to pass from this table to the next node_
   
5. Enter a **Name** for the field.
   
6. Optional. Edit the automatically generated **Label** that identifies the field.
   
7. Select the field's **Data type**. Refer to the [Available operators](/en/features/decision-models/decision-tables#available-operators) documentation to see the condition operators each data type supports.
   
8. Optional. Enter a **Hint** that explains the field. Hints display in decision tables and help users understand the purpose of each field.
   
9. Click **Create output**. The model field is now an output for the table and can be added to other nodes in the model.
   

Create a Decision table node

### Create a Decision table node

[Decision table](/en/features/decision-models/decision-tables) nodes define conditional business rules. They intake data (Input fields), evaluate it based on business logic you specify, and output results (Output fields) accordingly.

Complete the following steps to create a **Decision table** node:

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
       
    
11. Refer to the [Configure decision table rules](/en/features/decision-models/decision-tables#configure-decision-table-rules) documentation to configure decision table evaluation logic.
    

Configure output fields

### Configure output fields

Output fields define the data that the model returns to the [recipe that called it](/en/features/decision-models/decision-models-by-workato).

Complete the following steps to configure output fields:

1. Select the **Model Outputs** node.
   
2. Click **Add output** if there are no existing outputs. Otherwise, click **+** (Add output).
   
3. Select which input and model fields to return to the [recipe that called the model](/en/features/decision-models/decision-models-by-workato). All input fields are available. You can only select model fields from nodes directly connected to this node.
   
4. Click **Add**.
   

Create conditional branches

### Create conditional branches

Conditional branches define a set of conditions that control the flow of data in the model using business logic you specify. They allow you to route data to different decision tables based on prior decisions, input fields, or model fields passed from upstream nodes. This makes it possible to handle variations in business logic within a single model, ensuring consistency and ease of maintenance.

> **FIELDS ARE PASSED UNCHANGED**
> 
> The **Conditional branch** node passes all received fields unchanged to branches that evaluate to `True`.

Complete the following steps to add conditional branches to a decision model:

1. Go to the **Toolbar** and drag a **Conditional branch** node into the model builder.
   
2. Click and drag between edges to configure the order of nodes. You can hover over a node connection and click **Delete edge** to remove it.
   
   ![Add the conditional branch to the model flow](/assets/conditional-node-flow.1f8N0H26.gif)_Add the conditional branch to the model flow_
   
3. Use the node's drop-down menu to select one of the following options:
   
   - **Every matching condition**: Runs every branch that matches a condition.
   - **First matching condition**: Runs the first branch that matches a condition.
   
   ![The conditional branch drop-down menu](/assets/condition-matching.DOWZmph3.png)_The conditional branch drop-down menu_
   
4. Optional. Click **\+ Add condition** to add additional conditions.
   
   Each condition you create can contain multiple evaluation criteria. For example:
   
   ![Each condition you create can contain multiple evaluation criteria](/assets/multiple-evaluations.CTgeCxVB.png)_Each condition you create can contain multiple evaluation criteria._
   
5. Select a condition to open its configuration sidebar.
   
   ![The condition configuration sidebar](/assets/condition-configuration.-KpUxUMw.png)_The condition configuration sidebar_
   
6. Use the **Input** drop-down menu to select a field. All input fields are available. You can only select model fields from nodes directly connected to this node.
   
7. Use the **Condition** drop-down menu to select an operator. The condition is treated as `True` if you leave this field blank. Refer to [Available operators](/en/features/decision-models/decision-tables#available-operators) to see the operators available for each data type.
   
8. Enter a **Value** to compare against the **Input** using the **Condition**.
   
9. Optional. Click the **+** (plus) icon to create an additional condition, then select one of the following:
   
   - **AND**: Inputs are treated as `True` if they satisfy all conditions.
   - **OR**: Inputs are treated as `True` if they satisfy any condition.

### Model fields

Model fields define the data that moves between nodes in a decision model. Unlike input fields, which receive data [from the calling recipe](/en/features/decision-models/decision-models-by-workato), model fields store intermediate values produced by decision tables and pass them to downstream nodes.

The following describes how data flows through a decision model:

1. The calling recipe provides values for input fields.
2. Input fields are passed to the decision tables and conditional branches directly connected to the **Model Inputs** node.
3. Decision tables and conditional branches evaluate conditions using input fields or model fields from upstream nodes.
4. Decision tables write outputs to model fields and pass them to downstream nodes. Conditional branches pass all received fields unchanged to branches that evaluate to `True`.
5. The **Model Outputs** node returns selected input and model fields to the calling recipe.

Refer to [Create a model field](#create-a-model-field) to add fields to a model.

#### Troubleshooting

Refer to the following sections to troubleshoot issues related to model field sources:

- [Missing source](#missing-source)
- [Source conflict](#source-conflict)

##### Missing source

A field becomes invalid when its source is unavailable. This occurs when a connection breaks or an upstream node no longer outputs the field. Restore the source connection to make the field valid again.

**Invalid output field**

![An invalid output field](/assets/invalid-output-field.DOjXHOvE.png)_An invalid output field_

**Invalid input field**

![An invalid input field](/assets/invalid-condition-field.DEzVwNW9.png)_An invalid input field_

##### Source conflict

A source conflict occurs when multiple decision tables update the same field in a downstream node. The model continues to function, and the downstream node uses values from the decision table that appears first alphabetically. You can remove one of the sources to resolve this conflict.

![A source conflict](/assets/multiple-sources.lUg57zix.png)_A source conflict_

Alternatively, you can use conditional branches to ensure the source nodes are mutually exclusive. The conflict warning still appears, but only one path carries data at a time, so no conflict occurs at runtime.

![Mutually exclusive source nodes](/assets/mutually-exclusive-nodes.DjzpVT-f.png)_Mutually exclusive source nodes_

---
