---
url: 'https://docs.workato.com/en/workflow-apps/prefill-forms.md'
description: >-
  Prefill Workflow apps page input fields using URL parameters to pre-populate
  form content and streamline data collection.
---

# Prefill forms with URL parameters

Workflow apps allows you to prefill page input fields using URL parameters. This enables you to prefill form content and is useful in scenarios where the recipients of your forms must review pre-populated information, make necessary updates, and add additional details if required.

Incorporating prefilled values directly into the URL streamlines business processes and enhances user experience by making forms more dynamic and personalized. It also reduces the likelihood of errors and saves time. Additionally, it integrates seamlessly with automated workflows, making it a powerful tool for data collection and validation processes.

## How to prefill forms with URL parameters

You can prefill page input fields by appending a query parameter to the end of a Workflow app request page URL.

Complete the following steps to prefill fields in your Workflow apps forms:

1. Identify one or more components you plan to prefill.
   
2. Identify the **Title** of the component. This value is distinct from the component **Label**, which is visible to end-users in the [Workflow apps portal](/en/workflow-apps/portal-settings). Conversely, the component **Title** is only visible to builders within Workato and is located in the right column of the page editor.
   
   ![Identify the component title](/assets/component-title.CtvUxZhC.png)_Identify the component title_
   
3. Obtain the URL of the new request from the Workflow apps portal. For example, the following URL is for a new request in an expense report app:
   
   ```html
   https://example.workato.app/expense-reports/submit-request-in-expense-reports-12a3
   ```
   
4. Configure the `?prefilled_values=` parameter using JSON by determining the values you plan to prefill. The following example preconfigures the following fields:
   
   - **Name**
   - **Submission date**
   - **Total requested**
   - **Description**
   - **Supervisor**
   - **Department**
   - **Third party?**
   
   View JSON
   
   ```json
   {
     "Third party?": {
       "value": true
     },
     "Submission date": {
       "value": "2024-07-26"
     },
     "Total requested:": {
       "value": 10
     },
     "Description": {
       "value": "SKO"
     },
     "Supervisor": {
       "value": "Emily Benson"
     },
     "Department": {
       "value": "Sales"
     },
     "Name": {
       "value": "Peter Gallagher"
     }
   }
   ```
   
5. _Optional_. Add the `"disabled": "false"` parameter to make the component editable. Otherwise, the prefilled field is read-only by default.
   
   ```json
   {
     "Third party?": {
       "value": true,
       "disabled": false
     }
   }
   ```
   
6. URL encode the JSON and append it to the URL as a query parameter. The following example URL-encodes the preceding JSON and appends it to the URL for the submission page in our expense report app:
   
   ```html
   https://example.workato.app/expense-reports/submit-request-in-expense-reports-12a3??prefilled_values=%7B%0A%20%20%22Third%20party%3F%22%3A%20%7B%0A%20%20%20%20%22value%22%3A%20true%2C%0A%20%20%20%20%22disabled%22%3A%20false%0A%20%20%7D%2C%0A%20%20%22Submission%20date%22%3A%20%7B%0A%20%20%20%20%22value%22%3A%20%222024-07-26%22%0A%20%20%7D%2C%0A%20%20%22Total%20requested%3A%22%3A%20%7B%0A%20%20%20%20%22value%22%3A%2010%0A%20%20%7D%2C%0A%20%20%22Description%22%3A%20%7B%0A%20%20%20%20%22value%22%3A%20%22SKO%22%0A%20%20%7D%2C%0A%20%20%22Supervisor%22%3A%20%7B%0A%20%20%20%20%22value%22%3A%20%22Emily%20Benson%22%0A%20%20%7D%2C%0A%20%20%22Department%22%3A%20%7B%0A%20%20%20%20%22value%22%3A%20%22Sales%22%0A%20%20%7D%2C%0A%20%20%22Name%22%3A%20%7B%0A%20%20%20%20%22value%22%3A%20%22Peter%20Gallagher%22%0A%20%20%7D%0A%7D
   ```
   

## View and edit in the Workflow apps portal

Share the modified URL with your app users. They can view, edit, and submit the prefilled page in the Workflow apps portal, similar to a typical request.

![View/edit the prefilled page](/assets/prefilled-form.Clab4nFx.png)_View and edit the prefilled page in the Workflow apps portal._

## Compatible components

This functionality is compatible with the following [page components](/en/workflow-apps/page-components):

- Checkbox
- Date
- Date and time
- Decimal
- Description
- Drop-down
- Integer
- Text

### Sample JSON

View sample JSON for the page components this feature supports.

View JSON

```JSON
{
  "Checkbox": {
      "value": true,
      "disabled": false
  },
  "Date": {
      "value": "2024-07-26"
  },
  "Datetime": {
      "value": "2024-07-25 16:00"
  },
  "Decimal": {
      "value": 0.2
  },
  "Integer": {
      "value": 10
  },
  "Description": {
      "value": "Description"
  },
  "Text": {
      "value": "Peter"
  },
  "Dropdown manual": {
      "value": "Sales"
  },
  "Dropdown table": {
      "value": {
          "record_id": "2026e619-3304-42cf-804f-3146cdacaa6e",
          "value": "123"
      }
  }
}
```

## Limitations

Workflow apps supports a maximum of 8,000 characters in the URL.

---
