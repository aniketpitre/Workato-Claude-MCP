---
url: 'https://docs.workato.com/en/recipes/loops.md'
description: >-
  Learn how to build a Repeat while loop in Workato that runs steps at least
  once and continues while a condition is met, with page and count examples.
---

# Repeat while loop

A **Repeat while** loop executes actions inside a block of steps at least once and continues iterating while a condition is met. This type of [Repeat control statement](/en/recipes/steps#repeat-step) is also known as a [do-while loop](https://en.wikipedia.org/wiki/Do_while_loop): It _does_ one or more actions _while_ a condition is met.

To insert a Repeat while loop into a recipe, click the **+** (plus) button in the recipe editor to add a new step and select **Repeat while**.

![Select Repeat while](/assets/repeat-while-block-add-repeat-while-step.CBrYfR-g.png) _Select Repeat while_

Workato adds a block of steps to the recipe where you can configure the app and action to take while a condition is met.

For more detailed instructions, see [How to create a Repeat while conditional loop](#how-to-create).

![Repeat while loop](/assets/repeat-while-block.BVbY_E5o.png) _Repeat while loop_

You can use a Repeat while loop for use cases such as the following:

- Fetch pages of data, using an [offset](#loop-offset) value or a [next page token](#loop-next-page)
- Execute one or more actions a [fixed number of times](#loop-fixed-count)
- Repeat one or more actions [until a specific condition is met](#loop-conditional)

> **LOOP ITERATION LIMIT**
> 
> A Repeat while loop repeats steps up to 50,000 times. This quota is a defensive measure to prevent uncontrolled consumption of tasks. Ensure the condition you set allows the loop to exit when needed.
> 
> For example, suppose you set a condition that repeats an action while a variable is `true` but you do not include logic to change the variable to `false`. In this case, the loop cannot exit, and as a result, it maxes out the number of iterations.

## How to create a Repeat while conditional loop

Creating a Repeat while loop requires the following steps:

- [Step 1: Define actions to repeat](#step-1) (**REPEAT**)
- [Step 2: Define a condition to check](#step-2) (**WHILE**)

> **ACTIONS ARE EXECUTED AT LEAST ONCE**
> 
> Because it is a type of [do-while loop](https://en.wikipedia.org/wiki/Do_while_loop), the Repeat while conditional loop executes the body of the loop at least once. It then checks whether the condition is met, and if it is, the body of the loop is executed again and the cycle repeats.

### Step 1: Define actions to repeat

1. Sign in to your Workato account.
   
2. Go to **Projects**.
   
3. Click **Create > Recipe** or press C+R to create a new recipe, or click an existing recipe and select **Edit recipe**.
   
4. Click the **+** (plus) button under **Actions** to add a new step.
   
5. Select **Repeat while**.
   
   ![Select Repeat while](/assets/repeat-while-block-add-repeat-while-step.CBrYfR-g.png) _Select Repeat while_
   
   Workato adds a block of steps to the recipe and automatically selects the **Select an app and action** step.
   
   ![Select an app and action in the Repeat while loop](/assets/repeat-while-block-select-app.CsNVuoyF.png) _Select an app and action in the Repeat while loop_
   
6. Select the application, connection, and action you plan to repeat.
   
7. Fill out the relevant fields in the action setup.
   

### Step 2: Define a condition to check

1. Select **Set up condition to repeat steps** in the recipe editor.
   
   ![Set up condition to repeat steps in Repeat while loop](/assets/repeat-while-block-set-up-condition.bi-ec5Gb.png) _Set up condition to repeat steps in Repeat while loop_
   
2. Select a datapill from the **Recipe data** interface or manually enter a value in **Data field** (for example, the Index datapill).
   
   ![Data field in Repeat while loop](/assets/repeat-while-block-data-field.1kiFVALS.png) _Data field in Repeat while loop_
   
3. Select a condition from the **Condition** drop-down menu (for example, `less than`).
   
4. Select a datapill from the **Recipe data** interface or manually enter a value in the **Value** field (for example, `4`).
   
5. _Optional._ Click **+** (plus) underneath the **Value** field to add a **WHILE** condition, and select one of the following logical operators:
   
   - **AND**: All conditions must be met for the loop to continue.
   - **OR**: Any condition can be met for the loop to continue.
   
   You can add multiple conditions, but they must all use the same logical operator.
   
   ![Set up additional condition to repeat steps in Repeat while loop](/assets/repeat-while-block-add-condition.D6MEag6q.png) _Set up additional condition to repeat steps in Repeat while loop_
   

## Use cases and examples

The Repeat while conditional loop supports several loop patterns, such as the following:

- Fetch pages of data using an offset. [Learn more](#loop-offset) and see an [example](#offset-loop-example).
- Fetch pages of data using a next page token. [Learn more](#loop-next-page) and see an [example](#next-page-token-loop-example).
- Execute an action a fixed number of times. [Learn more](#loop-fixed-count) and see an [example](#fixed-count-loop-example).
- Repeat one or more actions until a specific condition is met. [Learn more](#loop-conditional) and see an [example](#conditional-loop-example).

### Fetch pages using offset

You can use a Repeat while loop with actions that support pagination through an offset. This enables you to retrieve pages of data by specifying which results are returned on each iteration. When there is no more data to retrieve, the loop exits.

Fetching pages using an offset requires you to use the Index datapill, which automatically keeps track of loop iterations and is provided in the output of the **REPEAT** step.

To specify an offset, multiply the Index datapill by the page size (number of items returned per page).

For example, if the page size is 100, you can set the **Page offset** to `Index*100`, where `Index` is the Index datapill.

![Multiply the loop Index by the page size to define an offset](/assets/repeat-while-block-offset-formula.Cw1IQU45.png) _Multiply the loop Index by the page size to define an offset_

Ensure you retrieve all pages of data by configuring the loop to execute while the list size of fetched items is greater than `0`.

To fetch pages using offset:

1. Sign in to your Workato account.
   
2. Go to **Projects**.
   
3. Click **Create > Recipe** or press C+R to create a new recipe, or click an existing recipe and select **Edit recipe**.
   
4. Click the **+** (plus) button and select the **Repeat while** step.
   
5. Configure the action(s) you plan to repeat in the loop block. To specify an offset in an action's **Page offset** field, use the Index datapill provided in the **REPEAT** step output and multiply it by the page size.
   
6. Set the condition in the **WHILE** step of the loop body to check whether the List size datapill from the list of fetched data is greater than `0`. If so, there is more data to retrieve and the loop repeats.
   
   ![Set the condition in a Repeat while block](/assets/repeat-while-block-offset-while-condition.D3HrAO-e.png) _Set the condition in a Repeat while block_
   

#### Example

You can use a Repeat while loop to retrieve all results from a Workato FileStorage search, which paginates through an offset.

![Repeat while example using pagination through offset](/assets/repeat-while-block-offset-example.BqPivKwc.png) _Repeat while example using pagination through offset_

EXAMPLE FILESTORAGE OFFSET INSTRUCTIONS

1. Create a recipe and set up a trigger, such as **Trigger on a specified schedule**.
   
2. Click the **+** (plus) button and click **Repeat while**. Workato adds a Repeat while block and highlights the **Select an app and action** step.
   
3. Select the **Workato FileStorage** connector and the **Search files** action.
   
4. Fill out the following fields:
   
   - Set **Directory path** to the path of the directory you plan to search.
   - Set **File name** to the intended pattern to fetch files with that name.
   - Set **Page size** to the number of results to fetch per page.
   - Set **Page offset** to the Index (Step 2) datapill multiplied by the page size. You can find the Index (Step 2) datapill in the **REPEAT** step output.
   
   ![Example input for a FileStorage search using pagination through offset](/assets/repeat-while-block-offset-example-input.CEPaVnnb.png) _Example input for a FileStorage search using pagination through offset_
   
5. Select the **+** (plus) inside the loop and click **Repeat for each**. Workato adds a Repeat for each block and highlights the **Set up list to repeat steps for each item** step.
   
6. Set the **Input list** field to the Files (Step 3) datapill from the **Search files** output.
   
7. Select the **Select app and action** step and configure it with the action you plan to take for each Workato FileStorage file in a page of search results.
   
   For example, to retrieve the contents of each file, you can select the **Get file contents** action from the **Workato FileStorage** connector and set **File path** to the File path (Step 4) datapill from the output of the **FOR EACH** step.
   
8. Select **Set up condition to repeat steps**.
   
9. Fill out the following fields:
   
   - Set **Data field** to the List size (Step 3) datapill from the output of the **Search files** action.
   - Set **Condition** to `greater than`.
   - Set **Value** to `0`.
   
   ![Set the condition in a Repeat while block](/assets/repeat-while-block-offset-while-condition.D3HrAO-e.png) _Set the condition in a Repeat while block_
   

### Fetch pages using next page token

You can use the Repeat while step with actions that support pagination through a next page token. This enables you to retrieve pages of data by setting a next\_page\_token variable to the next page token from the previous iteration's output. When there is not a next page to retrieve (meaning there is no more data), the loop exits.

Note that the initial value of the next\_page\_token variable must be blank.

For example, to retrieve all pages of data for an action that uses next page tokens, configure the loop to execute while the next\_page\_token variable is present (has a value).

1. Sign in to your Workato account.
   
2. Go to **Projects**.
   
3. Click **Create > Recipe** or press C+R to create a new recipe, or click an existing recipe and select **Edit recipe**.
   
4. Select the **Variables by Workato** connector and then select the **Create variable** action to create a string variable named next\_page\_token with the initial value left blank.
   
5. Click the **+** (plus) button and add a **Repeat while** step.
   
6. Configure the action you plan to repeat in the loop body. For example, if the action has a **Next page token** field, set its value to the Next page token datapill.
   
7. Click the **+** (plus) button and click **Action in an app** in the Repeat while loop body.
   
8. Select the **Variables by Workato** connector and then select the **Update variable** action to update the next\_page\_token variable to the value of the Next page token datapill. You can find this value in the output of the action you configured in the loop body.
   
   ![Update the next\_page\_token variable in a Repeat while block](/assets/repeat-while-block-next-page-token.BwP8IWxH.png) _Update the next\_page\_token variable in a Repeat while block_
   
9. Set the condition in the **WHILE** step of the loop block to check whether next\_page\_token is present (has a value). If a value is present, there is more data to retrieve and the loop repeats.
   
   ![Set the condition in a Repeat while block](/assets/repeat-while-block-next-page-token-while-condition.BCV8glK3.png) _Set the condition in a Repeat while block_
   

#### Example

You can use a Repeat while loop to retrieve all pages of results from a Google Drive search, which paginates through a next page token.

![Repeat while example using pagination through next page token](/assets/repeat-while-block-next-page-token-example.DD4gb3UY.png) _Repeat while example using pagination through next page token_

EXAMPLE GOOGLE DRIVE NEXT PAGE TOKEN INSTRUCTIONS

1. Create a recipe and set up a trigger, such as **Trigger on a specified schedule**.
   
2. Click the **+** (plus) button and click **Action in an app**.
   
3. Select the **Variables by Workato** connector and select the **Create variable** action to create a string variable named next\_page\_token with the initial value left blank.
   
4. Click the **+** (plus) button and click **Repeat while**. Workato adds a Repeat while block and highlights the **Select an app and action** step.
   
5. Select the **Google Drive** connector and the **Search files or folders** action.
   
6. Fill out the following fields:
   
   - Set **Files or folders** to **Files**.
   - Set **Folder ID** to the folder you plan to search.
   - Set **Query** to the query you plan to search by (for example, `modifiedTime < '2023-12-22T12:00:00'` to return files modified before 12 p.m. on December 22, 2023).
   - Set **Next page token** to the next\_page\_token datapill you created.
   
   ![Example input for a Google Drive search using pagination through next page token](/assets/repeat-while-block-next-page-token-example-input.CaUdm02H.png) _Example input for a Google Drive search using pagination through next page token_
   
7. Click the **+** (plus) button inside the loop and click **Repeat for each**. Workato adds a Repeat for each block and highlights the **Set up list to repeat steps for each item** step.
   
8. Set the **Input list** field to the Files datapill from the **Search files or folders** output.
   
9. Select the **Select app and action** step and configure it with the action you plan to take for each Google Drive file in a page of search results.
   
   For example, to download each file, you can select the **Download file** action from the **Google Drive** connector and set **File** to the ID datapill from the output of the **FOR EACH** step.
   
10. Click the **+** (plus) button to add a new step after the **Download file** action. It must be _inside_ the Repeat while **REPEAT the following steps** block, and _outside_ the Repeat for each **FOR EACH** block.
    
    ![Add a new step inside the Repeat while block](/assets/repeat-while-block-next-page-token-example-add-action.CsLIMhbO.png) _Add a new step inside the Repeat while block_
    
11. Select **Action in an app**.
    
12. Select the **Variables by Workato** connector and select the **Update variable** action to update the next\_page\_token variable to the value of the Next page token datapill from the output of the search step.
    
13. Select **Set up condition to repeat steps**.
    
14. Fill out the following fields:
    
    - Set **Data field** to the next\_page\_token datapill you created.
    - Set **Condition** to `is present`.
    
    ![Set the condition in a Repeat while block](/assets/repeat-while-block-next-page-token-while-condition.BCV8glK3.png) _Set the condition in a Repeat while block_
    

### Execute a fixed-count loop

A fixed-count loop iterates a specified number of times. Executing a fixed-count loop requires you to use the Index datapill, which automatically keeps track of loop iterations and is in the output of the **REPEAT** step.

When the value of Index reaches _the intended number of iterations minus 1_, the loop exits.

For example, to execute an action exactly five times, configure the loop to repeat while Index is less than `4`:

- **Data field:** Index datapill
- **Condition:** `less than`
- **Value:** `4` (the intended number of iterations minus 1)

![Use the Index datapill in a Repeat while block](/assets/repeat-while-block-fixed-count-index-datapill.C7sVKPK4.png) _Use the Index datapill in a Repeat while block_

To execute an action _n_ times, set the condition to be `less than` the value of _n - 1_.

1. Sign in to your Workato account.
   
2. Go to **Projects**.
   
3. Click **Create > Recipe** or press C+R to create a new recipe, or click an existing recipe and select **Edit recipe**.
   
4. Click the **+** (plus) button and add a **Repeat while** step.
   
5. Configure the action you plan to repeat in the loop block.
   
6. Set the condition in the **WHILE** step of the loop block to check whether the Index datapill from the output of the **REPEAT** step is `less than` the intended number of iterations minus one (-1). If so, the loop repeats.
   
   For example, to execute the action in the loop body five times, fill out the following fields:
   
   - Set **Data field** to the Index datapill.
   - Set **Condition** to `less than`.
   - Set **Value** to `4`.
   
   ![Set the condition for a fixed-count loop to iterate 5 times](/assets/repeat-while-block-fixed-count-while-condition.D7qelzTy.png) _Set the condition for a fixed-count loop to iterate five times_
   

#### Example

You can use a fixed-count loop to retrieve the first five pages of results from a Google Drive search, which paginates through a [next page token](#loop-next-page).

![Repeat while example using fixed-count loop and pagination through next page token](/assets/repeat-while-block-fixed-count-example.BvBf-67C.png) _Repeat while example using fixed-count loop and pagination through next page token_

EXAMPLE GOOGLE DRIVE FIXED-COUNT INSTRUCTIONS

Follow the instructions in the [next page token loop example](#next-page-token-loop-example), but fill out the following fields when you get to the final step, **Set up condition to repeat steps**:

- Set **Data field** to the Index datapill from the output of the **REPEAT the following steps** step.
- Set **Condition** to `less than`.
- Set **Value** to `4`.

This ensures that the loop retrieves only the first five pages of results from a Google Drive search.

![Set the condition for a fixed-count loop to iterate 5 times](/assets/repeat-while-block-fixed-count-while-condition.D7qelzTy.png) _Set the condition for a fixed-count loop to iterate five times_

### Repeat actions until a condition is met

You can use a Repeat while loop to repeat one or more actions until a specific condition is met. For example, you can send an HTTP request to an endpoint while its response code is not `200`. When the response code is `200`, the loop exits.

1. Sign in to your Workato account.
   
2. Go to **Projects**.
   
3. Click **Create > Recipe** or press C+R to create a new recipe, or click an existing recipe and select **Edit recipe**.
   
4. Click the **+** (plus) button and select the **Repeat while** step.
   
5. Configure the action(s) you plan to repeat in the loop block.
   
6. Set the condition in the **WHILE** step of the loop body to check whether a specific requirement is met. If the requirement is not met, the loop repeats.
   
   ![Set the condition in a Repeat while block](/assets/repeat-while-block-conditional-loop.e2ks2-zv.png) _Set the condition in a Repeat while block_
   

#### Example

You can use a Repeat while loop to attempt to create a product in Stripe when a product is created in Salesforce. Configure the recipe to send an HTTP request to Stripe until there is a `200` status code _or_ the request is sent five times, whichever comes first. This example incorporates a [fixed-count loop](#loop-fixed-count) to prevent maxing out the number of iterations.

![Repeat while example to repeat until a condition is met](/assets/repeat-while-block-conditional-loop-logical-or.DPNuOCNh.png) _Repeat while example to repeat until a condition is met_

EXAMPLE CONDITIONAL HTTP REQUEST INSTRUCTIONS

1. Create a recipe and select **Trigger from an app** as the starting point.
   
2. Select the **Salesforce** connector and then select the **New record** trigger.
   
3. Fill out the following fields:
   
   - Set **Object** to **Product**.
   - Set **Fields to retrieve** to the fields you plan to send to Stripe (for example, `Product ID`).
4. Click the **+** (plus) button and click **Repeat while**. Workato adds a Repeat while block and highlights the **Select an app and action** step.
   
5. Select the **HTTP** connector and then select the **Send request** action.
   
6. Set the **Request name** to `Create product in Stripe`.
   
7. Select **Start guided setup** to set up the action automatically using the request URL and request body, or select **Set up manually** to set up the action manually by configuring the fields in the **Request** and **Response** sections.
   
8. Select **Yes** from the **Mark non-2xx response codes as success?** drop-down menu. This ensures that the recipe continues executing the loop if it receives an error code.
   
9. Click the **+** (plus) button to add a new step after the **Send request via HTTP** action but before the **WHILE** condition.
   
   ![Add a new step inside the Repeat while block](/assets/repeat-while-block-conditional-loop-example-add-step.BZsehbCq.png) _Add a new step inside the Repeat while block_
   
10. Select **Action in an app**.
    
11. Select the **Scheduler by Workato** connector and then select the **Wait for time duration** action.
    
12. Select **5 minutes** from the **Interval** drop-down menu.
    
13. Select **Set up condition to repeat steps**.
    
14. Fill out the following fields:
    
    - Set **Data field** to the Status code (Step 3) datapill from the **Send request** step.
    - Set **Condition** to `does not equal`.
    - Set **Value** to `200`.
    
    ![Set the condition in a Repeat while block](/assets/repeat-while-block-conditional-loop.e2ks2-zv.png) _Set the condition in a Repeat while block_
    
15. Click the **+** (plus) button under the **WHILE** condition section and select the **OR** button to add another condition.
    
16. Fill out the following fields:
    
    - Set **Data field** to the Index (Step 2) datapill from the **REPEAT** step output.
    - Set **Condition** to `less than`.
    - Set **Value** to `4`.
    
    These logical **OR** conditions ensure that the loop exits after one successful HTTP request _or_ five iterations of unsuccessful requests, whichever comes first.
    
    ![Set up logical OR conditions for Repeat while loop](/assets/repeat-while-block-conditional-loop-example-or-condition.42Rpg7sZ.png) _Set up logical OR conditions for Repeat while loop_

---
