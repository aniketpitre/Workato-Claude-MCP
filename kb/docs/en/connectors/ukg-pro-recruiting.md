---
url: 'https://docs.workato.com/en/connectors/ukg-pro-recruiting.md'
description: >-
  The UKG Pro (Recruiting) connector enables you to automate recruiting and
  onboarding workflows, simplifying hiring for recruiters and managers.
---

# UKG Pro (Recruiting)

[UKG Pro™ Recruiting](https://www.ukg.com/resources/product-info/ukg-pro-recruiting) is a recruiting system that simplifies recruiting for both recruiters and hiring managers. This connector automates key recruitment tasks, allowing your team to focus on creating a more engaging and immersive employee experience.

## Prerequisites

Before using the UKG Pro (Recruiting) connector in Workato, ensure you have an active UKG Pro (Recruiting) account with appropriate permissions to access APIs. The following information is required to establish a connection in Workato to the UKG Pro Recruiting and Onboarding APIs:

- Identity Host – Domain name of the instance of identity associated with the tenant.
  
- Tenant Alias – A tenant name. It may be seen in the browser bar when signed into UKG Pro Recruiting.
  
- Client ID – Unique identifier of the identity client provided to you by UKG.
  
- Client Secret – A client secret associated with the client ID provided to you by UKG.
  
- Grant Type – Method for obtaining an access token.
  

Contact the UKG support team or the UKG Identity team if you require community library access. Refer to [UKG's permissions documentation](https://developer.ukg.com/hcm/docs/onboarding-and-recruiting-authorization-and-permissions) for more information. Access to the community library is required to view UKG's permissions documentation.

## Connection Setup

Workato supports OAuth authentication to connect to UKG Pro (Recruiting). Complete the following steps to establish a connection to UKG Pro (Recruiting) in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **UKG Pro (Recruiting)** as your connection on the **New Connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
   ![UKG Pro (Recruiting) connection setup](/assets/connection-setup.kckgN4eU.png)_UKG Pro (Recruiting) connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID**, **Client Secret**, and **Tenant** for your UKG Pro (Recruiting) account, which are provided by the UKG team.
   
6. Select the necessary **Environment** and **OAuth scopes** required for your integration.
   
7. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-recruiting/new-or-updated-records-trigger.md
description: >-
  The New or updated records trigger monitors UKG Pro (Recruiting) for newly
  created or updated records.
---

# UKG Pro (Recruiting) - New or updated records trigger

The **New or updated records** trigger monitors UKG Pro (Recruiting) for newly created or updated records.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to monitor. Additional fields load dynamically based on the object you select. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. Defaults to 1 hour ago if left blank. You can't change this value after the recipe runs or tests successfully. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the **Candidate** object has the following output schema:

| Output field | Description |
| --- | --- |
| ID | The unique ID of a candidate in GUID format. |
| Creator | The creator of a candidate record. |
| Created at | The date and time a candidate was created. |
| Util person ID | The UKG Pro person ID. |
| EEID | The employee identifier. |
| Preferred locale | The preferred language of the candidate. |
| Integration user ID | The user ID used in 3rd party integrations, such as background check integrations. |
| Is internal | An indicator of whether or not a candidate is an internal employee. |
| Is active | An indicator of whether or not a candidate is an active employee. |
| Updated at | The date and time a candidate was last updated |

---

---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-recruiting/create-record-action.md
description: The Create record action creates a new record in UKG Pro (Recruiting).
---

# UKG Pro (Recruiting) - Create record action

The **Create record** action creates a new record in UKG Pro (Recruiting).

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to create. Additional fields load dynamically based on the object you select. |

Workato dynamically populates additional fields depending on the object you select. For example, the **Candidate** object has the following input fields:

| Input fields | Description |
| --- | --- |
| First | Provide the first name of the candidate. |
| Last | Provide the last name of the candidate. |
| Middle | Provide the middle name of the candidate. |
| Former | Provide the former name of the candidate. |
| Preferred name | Provide the preferred name of the candidate. |
| Prefix | Provide the prefix for the candidate's name. |
| Suffix | Provide the suffix for the candidate's name. |
| Contact information | Provide the contact information of the candidate. |
| Provider | Provide the provider details. |
| Integration user ID | Provide the ID of the integration user. |
| Is willing to relocate | Specify whether the candidate is willing to relocate. |
| Is internal | Specify whether the candidate is an internal employee. |
| Is active | Specify whether the candidate is an active employee. |
| Work experience | Provide details about the applicant's work experience. |
| Education | Provide details about the applicant's education. |
| Skills | Provide details about the applicant's skills. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the **Candidate** object has the following output schema:

| Output field | Description |
| --- | --- |
| ID | The unique ID of a candidate in GUID format. |
| Creator | The creator of a candidate record. |
| Created at | The date and time a candidate was created. |
| Util person ID | The UKG Pro person ID. |
| EEID | The employee Identifier. |
| Preferred\_locale | The preferred language of the candidate. |
| Integration user ID | The user ID used in 3rd party integrations, such as background check integrations. |
| Is internal | indicator of whether or not a candidate is an internal employee. |
| Is active | indicator of whether or not a candidate is an active employee. |
| Updated at | The date and time a candidate was last updated. |

---
