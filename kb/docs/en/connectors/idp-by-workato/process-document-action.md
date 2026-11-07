---
url: >-
  https://docs.workato.com/en/connectors/idp-by-workato/process-document-action.md
description: >-
  The Process document action in the IDP by Workato connector extracts
  structured data from uploaded files and returns the results as datapills.
---

# IDP by Workato - Process document using IDP by Workato action

The **Process document using IDP by Workato** action extracts structured data from uploaded files using Intelligent Document Processing (IDP) by Workato. Extracted data appears as datapills.

> **NEED AN EXAMPLE?**
> 
> Refer to the [Extract Google Slides data with IDP by Workato use case](/en/getting-started/use-cases/recipes/idp-by-workato-google-drive) for a step-by-step recipe example.

Complete the following steps to set up your IDP by Workato action:

1. Search for `IDP by Workato` and select it as your connector action after you have set up your trigger.
   
   ![Choose app](/assets/select-idp-connector.D-_4llIo.png)_Choose IDP by Workato as your app_
   
2. Select **Process document using IDP by Workato** as your action.
   
3. Provide **File contents** to process.
   
   ![Process document action](/assets/idp-doc-processing.B74PMpvh.png)_Process document action_
   
4. Enter the **File name** with its extension or specify the type in **File type**.
   
5. Use the **File type** drop-down menu to select the file type to process. This overrides the inferred type from **File name**. This connector supports `png`, `jpg`, `webp`, `gif`, and `pdf` file types. PDF files can contain up to 50 pages with IDP model v4. Earlier versions support up to 15 pages.
   
6. Use the **IDP version** drop-down menu to select the version you plan to use. New versions are released regularly. The action uses the selected version until you manually update it. Refer to [IDP model versions](/en/connectors/idp-by-workato/idp-versions) for more information.
   
7. Use the **Document type** drop-down menu to select the document type to process. Select `Documents` to provide your own schema or select one of the following options to use a predefined schema:
   
   - `Invoices`
   - `Receipts`
   - `Passport`
   - `Driver's License`
   - `Academic Transcript`
   - `Contract`
   - `Purchase order`
8. Add your JSON schema or enter **Fields to identify** manually.
   
   **Add JSON schema**
   
   1. Click the **Use JSON** button under **Fields to identify**.
      
   2. Paste the JSON sample you plan to use into the code box and then click **Next**. Alternatively, you can upload your JSON code by selecting **Upload sample JSON from your device** from the drop-down menu.
      
      ![Add or upload JSON](/assets/idp-add-json.DyJx1yl8.gif)_Paste or upload your JSON schema_
      
   3. Click **Next** and then review your JSON.
      
   4. Click **Generate schema**.
      
   
   **Add fields manually**
   
   1. Click **Add fields manually** under **Fields to identify**.
      
   2. **Name** your field.
      
      ![Add fields manually](/assets/add-fields-manually.Dr-bDtBy.png)_Add fields manually_
      
   3. Optional. Add a **Description**.
      
   4. Select the **Data type**.
      
   5. Use the **Optional** drop-down menu to determine if the field is optional or not.
      
   6. Optional. Use the **Nested** drop-down menu to determine if the field is nested under another field.
      
   7. Click **Add field**.
      
   
9. Click **Save**.
   

## Output

This action returns extracted values and confidence scores. Extracted values contain structured data from the document, while confidence scores indicate the accuracy of the extracted values.

### Extracted values

Extracted values include key details from the document, such as invoice numbers, dates, line items, and total amounts.

Example value output

```json
{
    "values": {
        "invoice_number": "I-N-V-50513188",
        "invoice_date": "17-Sep-2009",
        "due_date": "07-Mar-1996",
        "order_date": null,
        "total_amount": 722.84,
        "line_items": [
            {
                "description": "Cultural identify.",
                "quantity": 2,
                "price": 21.06,
                "product_code": null,
                "unit_price": 10.53
            },
            {
                "description": "Sister degree letter.",
                "quantity": 4,
                "price": 153.6,
                "product_code": null,
                "unit_price": 38.4
            },
            {
                "description": "Quite always item.",
                "quantity": 4,
                "price": 131.32,
                "product_code": null,
                "unit_price": 32.83
            },
            {
                "description": "Shoulder.",
                "quantity": 5,
                "price": 364,
                "product_code": null,
                "unit_price": 72.8
            },
            {
                "description": "Wall laugh.",
                "quantity": 5,
                "price": 38,
                "product_code": null,
                "unit_price": 7.6
            }
        ],
        "vendor_address": "8110 Lee Haven, West Michele, IN 23979 US",
        "recipient_address": "838 Harris Ferry, Matthew burgh, MP 10645 US",
        "vendor_phone": "+1(193)406-5197",
        "vendor_url": "www.Graham-Carrillo-and-Stark.com",
        "vendor_gst_number": "24H-D-E7487R-E-S-R-T4",
        "vendor_email": "g.hodges@example.org",
        "recipient_phone": "+1(362)455-4064",
        "recipient_url": "https://www.torres.biz/",
        "recipient_gst_number": null,
        "recipient_email": "bryan-scott@example.org",
        "purchase_order_number": null,
        "subtotal": 707.98,
        "tax_amount": 14.86,
        "discount": null,
        "payment_terms": null,
        "notes": null,
        "shipping_fee": null,
        "service_charge": null,
        "account_number": "16870634",
        "bank_code": null,
        "swift_number": "S-B-I-N-I-N-B-B250",
        "payment_method": null,
        "terms_and_conditions": "Terms and Conditions will be charged if payment is not made within the due date.",
        "remaining_calls": 99,
        "consumed_calls": 1,
        "reset_time": "2024-06-21T02:14:56.000000-07:00"
    }
}
```

### Confidence scores

Confidence scores indicate the model's confidence in the extracted values. A higher score (closer to 1.0) means greater accuracy.

Example confidence scores

```json
{

    "confidence_scores": {
        "invoice_number": 0.9999498764044592,
        "invoice_date": 0.9996482332742705,
        "due_date": 0.9999909854763569,
        "order_date": 0.9999952766598805,
        "total_amount": 0.9999833454831217,
        "line_items": [
            {
                "description": 0.9928496557986662,
                "quantity": 0.9137961392004543,
                "price": 0.9659621927727069,
                "product_code": 0.999996766699321
            },
            {
                "description": 0.9999201908481007,
                "quantity": 0.9999195718568064,
                "price": 0.9978151698276594,
                "product_code": 0.9999995679801468
            },
            {
                "description": 0.9998884805883848,
                "quantity": 0.9999804063791609,
                "price": 0.9999548387307367,
                "product_code": 0.9999996871837311
            },
            {
                "description": 0.9997998524901466,
                "quantity": 0.9999720029460075,
                "price": 0.9998689017394373,
                "product_code": 0.9999999031936844
            },
            {
                "description": 0.9999628251424393,
                "quantity": 0.9999601429370041,
                "price": 0.9998570904479072,
                "product_code": 0.9999998063873687
            }
        ],
        "vendor_phone": 0.9110792042231154,
        "vendor_url": 0.9452639023666751,
        "vendor_gst_number": 0.9992403800587537,
        "vendor_email": 0.9990823827609913,
        "recipient_phone": 0.9949677082415654,
        "recipient_url": 0.9963093776626322,
        "recipient_gst_number": 0.9997899093338881,
        "recipient_email": 0.9980467902735672,
        "purchase_order_number": 0.9999576695636125,
        "subtotal": 0.9999805851068317,
        "tax_amount": 0.9990580898021001,
        "discount": 0.9956880111711502,
        "payment_terms": 0.8990708766681919,
        "notes": 0.7962851560580655,
        "shipping_fee": 0.999827195289032,
        "service_charge": 0.9999335967675153,
        "account_number": 0.9943227138851094,
        "bank_code": 0.9813131412674407,
        "swift_number": 0.9913429312416263,
        "payment_method": 0.9992365566395588
    }
}
```

## Example use cases

The input fields for this action vary depending on the document type. The following examples demonstrate how to configure the input fields for invoices and general documents.

### Process an invoice

Invoices contain structured data such as invoice numbers, dates, line items, and total amounts. This example shows how to configure the **Process document using IDP by Workato** action to extract key invoice details:

Example invoice configuration

The input fields in this example are based on the following invoice:

![Invoice example](/assets/invoice-example.5lokRQ-v.png)_Invoice example_

The invoice is uploaded to Workato FileStorage. Use the [Get file contents in Workato FileStorage action](/en/features/filestorage/get-file-contents-action) to retrieve it, then process it using the **Process document using IDP by Workato** action with the following fields:

| Input field | Description |
| --- | --- |
| File contents | The invoice file. This example maps the File contents datapill from the **Get File contents** action. |
| File name | Enter the file name with its extension or specify the type in **File type**. |
| File type | Specify the file type of the document. Supported formats include `png`, `jpg`, `webp`, `gif`, and `PDF`. This example uses `png`. |
| Document type | Set the document type to `Invoices`. |
| Fields to identify | Define the fields to extract from the file. |

![Invoice input fields](/assets/invoice-input.C2PZ8DCg.png)_Invoice input fields_

### Process a general document

Documents may not follow a fixed structure like invoices. This example shows how to configure the **Process document using IDP by Workato** action to extract key details from an unstructured document.

Example document configuration

The input fields in this example are based on the following document:

![Document example](/assets/document-input-example.CGopj9kd.png)_Document example_

The document is uploaded to **Workato FileStorage**. Use the [Get file contents in Workato FileStorage](/en/features/filestorage/get-file-contents-action) action to retrieve it, then process it using the **Process document using IDP by Workato** action with the following fields:

| Input field | Description |
| --- | --- |
| File contents | The document file. This example maps the File contents datapill from the **Get file contents** action. |
| File name | Enter the file name with its extension or specify the type in **File type**. |
| File type | Specify the file type of the document. Supported formats are **png**, **jpg**, **webp**, **gif**, and **PDF**. This example uses **PDF**. |
| Document type | Set the document type to **Documents**. |
| Fields to identify | Define the fields to extract from the file. |

![Document input fields](/assets/documents-input-fields.CDynAdsi.png)_Document input fields_
