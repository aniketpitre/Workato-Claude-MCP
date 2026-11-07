---
url: 'https://docs.workato.com/en/accelerator-aiml-start.md'
description: >-
  Start the AIML accelerator recipes in your Workato workspace in the correct
  order to bring the solution online.
---

# Start the AIML accelerator

## Start the recipes

1. Navigate to **Projects > Home > AIML Accelerator**.
   
2. Start all of the recipes in the following folders in this order:
   
   1. API endpoints
   2. AWS S3
   3. AWS Sagemaker
   4. Functions

## Load your schema

The **AIML|Data Fields** lookup table saves the schema of the data model deployed on SageMaker. Workato sends data to Sagemaker to create and train a data model. Sagemaker then validates this data against the rules defined in the **AIML | Data Fields** lookup table.

![AIML Data fields](/assets/data-fields-lookup.D9_LGPb3.png)_Data fields lookup table_

There are two options to configure the **AIML | Data Fields** lookup table. The first option is to click **Add Entry** and manually configure each data field. The second option is to use the **AIML|REC-009|Load Model Schema** recipe to automate this process. This recipe also adds an entry to the **AIML | Model Profile** lookup table.

Follow these steps to use the **AIML | REC-009 | Load Model Schema** recipe:

1. In Workato, Navigate to **Projects > Home > AIML Accelerator > Bootstrap**.
   
2. Select **AIML | REC-009 | Load Model Schema**.
   
3. Configure the input fields in **Step 2**.
   
   ![Configure the input fields](/assets/load-schema-recipe.BPxkFBXc.png)_Configure input fields_
   
   <dl><dt>model_Identifier</dt><dd>Provide a unique, user-friendly name to identify the machine learning model.</dd><dt>headers</dt><dd>Provide the column names of the schema in CSV format without any spaces.</dd><dt>prediction_col_name</dt><dd>Provide the name of the prediction column.</dd><dt>datetime_format</dt><dd>If the data contains date-time values, provide the format to enable Workato to parse them. See <a href="/en/formulas/date-formulas.html#strftime">date-time formats</a> for a list of formats Workato supports.</dd></dl>
   
4. In **Step 3**, provide sample CSV data for the data model to consume.
   
   Example:
   
   ```
   id,first_name,last_name,email,ip_address
   1,Lucy,Carrigan,lcarrigan@example.com,123.45.678.900
   2,Jude,Feeney,jfeeney@example.com,987.65.43.210.012
   3,Sadie,Simmons,ssimmons@example.com,345.67.890.100
   ```
   
5. Click **Test** to run the recipe one time.
   
6. Navigate to the **AIML|Data Fields** lookup table to check for the updated values.
   
7. Manually provide the validation rules by configuring the input fields.
   
   <dl><dt>Workato data type</dt><dd>Provide the data type of the field. See <a href="/en/recipes/data-pills-and-mapping.html#data-types">Workato-supported data types</a> for a list of data types Workato supports.</dd><dt>Is required (true/false)</dt><dd>Set to <strong>true</strong> if the field is a required field. Set to <strong>false</strong> or leave blank if the field is not required.</dd><dt>Is unique (true/false)</dt><dd>Set to <strong>true</strong> if the field's value must be unique within the dataset used to train the model. Set to <strong>false</strong> or leave black if the value must not be unique.</dd><dt>Regex pattern</dt><dd>Workato checks data against this pattern.</dd></dl>
   

## Define model profile

The **AIML|Model Profile** lookup table stores the model profile of the machine learning model used by the solution. The recipes use these profiles to read the data and connect to the machine learning platform.

Follow these steps to define your model profile. If you used the **AIML|REC-009|Load Model Schema** recipe, you can skip to Step 3:

1. In Workato, navigate to **Tools > Lookup tables** and select the **AIML|Model Profile** lookup table from the available list of lookup tables.
   
2. Add an entry to the lookup table and provide a **Model Identifier** for the model. This **Model Identifier** must match the **Model Identifier** you provided in the **AIML|Data Fields** lookup table.
   
3. Provide an **AIML | Connection Profile** in JSON format. Workato requires these parameters to connect with the machine learning model.
   
   We have configured the following example for Sagemaker:
   
   ```json
   {
   	"endpoint_name":"{Unique Endpoint_name}",
   	"role_arn":"arn:aws:iam::xxxx:role/service-role/AmazonSageMaker-xxxxRole-xxxx"
   }
   ```
   
4. Provide a **Storage Source Connection Profile** in JSON format. Workato requires these parameters to connect with the source data storage location.
   
   We have configured the following example for AWS S3:
   
   ```json
   {
   	"accelerate": "false",
   	"region": "xx-xxx-x",
   	"bucket": "xxxx",
   	"object_name": "xxxxx_training_data.csv"
   }
   ```
   
5. Provide a **Storage Target Connection Profile** in JSON format. This is where Workato moves the target data after validation and passes it to SageMaker. Workato requires these parameters to connect with the storage location.
   
   We have configured the following example for AWS S3:
   
   ```json
   {
   	"accelerate": "false",
   	"region": "xx-xxx-x",
   	"bucket": "xxxx",
   	"object_name": "xxxxx_training_data.csv"
   }
   ```
   
6. Provide the **Number of ML Models**. This number defines the number of models the machine learning model creates.
   

> **NUMBER OF ML MODELS**
> 
> A higher number of ML models correlates to more computational resources and longer job time. A higher number also generally results in superior machine learning models.

---
