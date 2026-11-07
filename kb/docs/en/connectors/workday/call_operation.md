---
url: 'https://docs.workato.com/en/connectors/workday/call_operation.md'
description: >-
  The Call operation action in the Workday connector lets you run SOAP-based
  Workday Web Services operations in a connected Workday instance.
---

# Workday - Call operation action

This action uses Workday Web Services (WWS) to execute SOAP-based operations in a connected Workday instance.

The full set of operations can be found on the [Workday Web Services Directory](https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html).

## Input (Simple)

1. Define the operation to run in your Workday instance.
   
2. Supply the data sent with the operation. The set of input fields depend on the type of the selected operation:
   

<dl><dt id="field-operation">Operation</dt><dd>Name of the Workday Web Services operation you plan to run.<br>You must select the operation, so Workato can determine the remaining input fields.</dd><dt id="field-attributes">Fields with attributes</dt><dd>Select the fields that must have attributes assigned to them.<br>These attributes are part of the XML tag of the selected field.<br><strong>Only</strong> for operations that have at least one field with attributes.</dd><dt id="field-multiple-values">Fields with multiple values</dt><dd>Select the fields that repeat in the operation data.<br><strong>Only</strong> for operations that have at least one repeating field.</dd></dl>

### Operation

![Select Maintain Contact Information](/assets/select_operation.CoAKlzc2.png)_Select Maintain Contact Information_

Full list of all operations in Workday Web Services. To find the operation that you want, use keywords to filter and reduce the list of possible matches.

In this example, you look for the [Maintain Contact Information](https://community.workday.com/sites/default/files/file-hosting/productionapi/Human_Resources/v29.0/Maintain_Contact_Information.html) operation. Here, we create a recipe to update the email address of a Workday record when the employee's email changes.

### Fields with attributes

![Selecting Email Address Data to include attribute values](/assets/select_fields_with_attributes.CGjEYUF3.png)_Selecting Email Address Data to include attribute values_

If you want to add new email addresses to a particular contact without replacing the existing email addresses, we can set the **Do\_Not\_Replace\_All** attribute of the **Email address data** field to `false`.

Select `Maintain Contact Information Data/Worker.../Email Address Data`. This generates all possible attributes for the **Email address data** field, including **Do\_Not\_Replace\_All**.

### Fields with multiple values

![Selecting Email Address Data field to be repeated](/assets/select_fields_with_multiple_values.hLaAp0pD.png)_Selecting Email Address Data field to be repeated_

If your use case involves more than one email address, you have to send multiple email addresses in a single operation.

Select `Maintain Contact Information Data/Worker.../Email Address Data`. This changes the **Email address data** into a list type input field. In further operations, you can map one or more email addresses using this list.

### Customizing reference fields

Each reference field value can be customized using the `customization:value` syntax. You can use this to customize the field type. For example, `Worker_Reference` is typically referenced using WID. If you'd like to reference it by its employee ID, you may type: `Employee_ID:21012`. This converts the field type from WID to employee ID, and the value we will use is 21012.

Take note to enclose any values containing comma, spaces, or colons with the `<!--no_split-->` syntax to avoid them being used as delimiter. For example: `<!--no_split-->value1,value2<!--no_split-->`.

## Input (user-defined payloads)

![Switching to a user-defined payload](/assets/switching_to_user_defined_payload.C3r1ZD9o.png)_Switching to a user-defined payload_

When you customize the XML payload sent to Workday, you can use the Workday connector's support for a user-defined payload.

Follow these steps to switch to user-defined XML payload from guided input:

1. Select the operation to perform.
   
2. Set the **Switch to user-defined payload** input field to `Yes` to enable user-defined payload mode. Use the multi-line text input field to edit the raw XML payload of the request directly.
   
3. Workato automatically populates all guided input fields configured before switching to user-defined payloads in the raw XML payload.
   

When working with the user-defined XML payload mode, keep the following considerations in mind:

- Workato will insert or replace the `Security` portion of the `Header` field with values based on the selected connection.
- Workato does not sync customizations made in user-defined payload mode back into the guided input mode. These customizations are not retrievable when switching back to a user-defined payload.
- You must check and fix any guided input fields configured using formula mode to ensure proper generation of the XML payload.

Here is an example of a valid custom XML payload:

```xml
<env:Envelope
	xmlns:xsd="http://www.w3.org/2001/XMLSchema"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:wsdl="urn:com.workday/bsvc"
	xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
	<env:Body>
		<wsdl:Get_Workers_Request>
			<wsdl:Request_References>
				<wsdl:Worker_Reference>
					<ID wsdl:type="Employee_ID">12345</ID>
				</wsdl:Worker_Reference>
			</wsdl:Request_References>
		</wsdl:Get_Workers_Request>
	</env:Body>
</env:Envelope>
```

## Output

The complete set of fields and attributes for the selected operation is available in the output datatree.

## Limitations

Based on the [Workday documentation](https://doc.workday.com/r/3DMnG~27o049IYFWETFtTQ/sGhnezv85Vfp9LabNN~EWw):

- The maximum number of instances in a web service response is 1 million.
- Responses with attachments/images, the maximum size of each attachment/image is 30MB.
- Rich text string responses have a size limit of 1,048,576 characters or 1MB.

---
