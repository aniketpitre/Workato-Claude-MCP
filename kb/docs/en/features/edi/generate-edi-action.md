---
url: 'https://docs.workato.com/en/features/edi/generate-edi-action.md'
description: >-
  Use the Generate EDI action in EDI tools by Workato to create EDI documents
  from a transaction type or a sample document.
---

# EDI tools by Workato - Generate EDI action

The generate EDI action allows you to create an EDI document.

![Generate EDI action configuration](/assets/generate-edi-action.38Oilfdp.png)_Generate EDI action configuration_

To use this action, you must provide the necessary data for the EDI document. There are two ways to do this, and the action setup depends on the method you choose.

- [Set up using transaction type](#transaction-type)
- [Set up using a sample document](#sample-document)

## Input

| Input field | Description |
| --- | --- |
| How would you like to generate the EDI message? | Select whether you plan to generate a document based on the EDI transaction type or by providing a sample. |
| EDI standard | Specify the EDI standard of your document. The following choices are available: EDIFACT, HL7, and X12. |
| Standard subset/version | Specify the version of the EDI standard you plan to use. This field is available after you select the EDI standard and when the **How would you like to generate the EDI message?** field is set to **Manual configuration**. |
| Transaction type | Specify the transaction type. This is available after you select the subset/version. |
| Groups | Provide the necessary field values to generate the EDI document. Consult with your trade partner's guidelines as their requirements may differ from default ones. Keep in mind that required segments are marked with a red asterisk. The schema is populated after the transaction type is selected. Click **Show optional fields** to view additional fields. |
| EDI message sample | Provide a sample EDI document to populate the JSON sample. This field is used only during recipe design time, so datapills should not be mapped to this field. |
| JSON | JSON generated from the sample EDI document. Edit this field and add datapills to generate the actual EDI document. |

### Set up using transaction type

To use this method, you must choose a specific transaction type and then fill in the fields necessary for the specific document.

1. Use the **How would you like to generate the EDI message?** drop-down menu to select **Manual configuration**.
   
2. Choose the specific version of the EDI standard and the transaction type in the corresponding fields
   
3. Workato populates the **Groups** section based on the transaction type
   
4. Fill in the fields that are necessary for your transaction.
   

### Set up using a sample document

To use this method, you must provide a sample EDI document that is transformed into a JSON document with all the field descriptions. This option is convenient if you plan to alter only a small amount of fields each time.

1. Use the **How would you like to generate the EDI message?** drop-down menu to select **Sample and raw JSON edit**.
   
2. Paste a sample EDI document in the corresponding field.
   
3. Wait until the **JSON** field is populated.
   
4. Alter the JSON using datapills.

---
