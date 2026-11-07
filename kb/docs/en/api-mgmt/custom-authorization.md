---
url: 'https://docs.workato.com/en/api-mgmt/custom-authorization.md'
description: >-
  Configure custom authorization to enforce additional claims on API endpoints,
  enabling role-based access control and custom business logic.
---

# Custom authorization

Custom authorization allows you to enforce an additional set of authorization claims on API endpoints for enhanced security. After an API request is made to an endpoint and authenticated with a valid token, Workato’s API Gateway evaluates the custom authorization expression. The request is authorized only if the claims expression evaluates to `true`.

This feature enables you to enforce security measures such as role-based access control, locale restrictions, and custom business logic.

## Configure custom authorization

Complete the following steps to configure custom authorization for an API endpoint:

1. Go to **Platform > API platform > API collections**.
   
2. Select the API collection with the endpoint where you plan to enforce custom authorization.
   
3. Click the relevant endpoint.
   
4. Open the **Settings** tab for the endpoint.
   
5. Go to the **Request authorization** field.
   
   ![Reference query parameters](/assets/request-auth.CN1vatU8.png)_Go to **Request authorization**_
   
6. Define your authorization claims using Workato formulas. Refer to the [Example formulas](#example-formulas) section for more information.
   
7. Click **Save** to validate and apply the claims.
   

### Reference API request datapills

When configuring custom authorization expressions, you can use datapills to reference different segments of an API request, such as Context, Request, and JWT Token. Specify the exact attribute or key you're targeting, and use Workato formulas to apply logic or validate inbound data.

The following sections apply this structure to specific scenarios, demonstrating how to access and validate key API request datapills in your custom authorization formulas:

#### JWT claims in validation formulas

To validate JWT claims, you can use the following structure:

![Reference JWT claim](/assets/jwt-auth.DYg9BVwn.png)_Reference JWT claim_

This example formula checks whether the `scope` claim includes `Users.read` and uses the following components:

- JWT claims: The datapill that refers to the JWT claims in the token.
- `scope`: The field that refers to the specific claim.
- `.include?('Users.read')`: The method that checks whether the `scope` claim includes the `Users.read` permission.

#### Headers in validation formulas

Header names follow canonical header key naming conventions. Request headers like `my-header` should be referenced with proper capitalization, such as `My-Header`. For example:

![Reference headers](/assets/header-auth.Dqb9pQCw.png)_Reference headers_

This formula uses the following components:

- Headers: The datapill that refers to the headers in the request.
- `My-Header`: The field that refers to the specific header.
- `.present?`: The method that checks whether the header is present in the request.

#### Query parameters in validation formulas

Query parameters are key-value pairs that can contain multiple values in an array. To reference a query parameter’s value in a formula, you must specify its position in the array. For example, to access the first value of a query parameter, use the [`.first` formula](/en/formulas/array-list-formulas#first), as shown in the following screenshot:

![Reference query parameters](/assets/query-auth.DpE0Y5g3.png)_Reference query parameters_

This formula uses the following components:

- Query: The datapill that refers to the query parameters in the request.
- `param`: The field that specifies the query parameter.
- `.first.starts_with?("value")`: The method that retrieves the first value in the query parameters array and checks if it starts with the string `value`.

### Supported formulas

A limited set of Workato formulas is supported when configuring custom authorization expressions. This list is non-exhaustive, and additional Ruby methods may be supported beyond those specified here. To request new formulas, reach out to your Customer Success Manager.

You can use the following in your expressions:

- Operators
  
- Use `==`, `!=`, `>`, `>=`, `<`, and `<=` to compare values in your formulas. These operators allow you to evaluate numeric, string, or boolean values in your formula.
  
- Mathematical operators
  
- Use `+`, `-`, `*`, `/`, `%`, and `**` to perform basic arithmetic in your expressions.
  
- Logical expressions
  
- Use `&&` (AND) and `||` (OR) to combine multiple conditions in your formula.
  
- Time units
  
- Use `seconds`, `minutes`, `hours`, `days`, `months`, and `years` to specify time intervals in expressions.
  
- `now`
  
- Use `now` to return the current date and time at runtime in Pacific Time (PT).
  
- `today`
  
- Use `today` to return the current date at runtime in Pacific Time (PT).
  
- `strftime`
  
- Use `strftime` to format a datetime input as a user-defined string.
  
- `ago`
  
- Use `ago` to return an earlier timestamp based on a specified time duration.
  
- `to_i`
  
- Use `to_i` to convert datetime values into epoch time (seconds since Unix epoch).
  
- `present`
  
- Use `present?` to check if a value is present in the input. This method returns `true` if the input contains a value and `false` if it is `nil`, `false`, an empty string, or an empty list. For example, use `present?` to ensure a claim exists before further validation.
  
- `include?`
  
- Use `include?` to check if a string contains a specific substring. For example, use `include?` to check if a role or permission exists within a claim.
  
- `starts_with?`
  
- Use `starts_with?` to check if a string begins with a specific substring. For example, use `starts_with?` to check if an email claim starts with a particular domain.
  
- `ends_with?`
  
- Use `ends_with?` to check if a string ends with a specific substring. For example, use `ends_with?` to validate that a claim ends with a known suffix.
  
- `length`
  
- Use `length` to return the number of characters within an input string, including whitespaces. For example, use `length` to check if a claim meets a length requirement.
  
- `upcase` or `downcase`
  
- Use `upcase` to convert text to uppercase and `downcase` to convert text to lowercase.
  
- `split`
  
- Use `split` to divide a string around a specified character, returning an array of substrings.
  
- `null`
  
- Use `null` to represent an empty or nil value in Workato formulas. This allows you to check if claims or fields are absent and is commonly used for strings, numbers, or lists.
  
- `true` or `false`
  
- Use `true` or `false` to validate boolean values. For example, use `true` to check whether a user has a specific role enabled.
  

### Example formulas

The following examples demonstrate how to use custom authorization for various purposes, such as enforcing access rules or validating conditions within an API request:

#### Role-based access

The following formula checks if the user has either the `admin` role or the `user:write` role. The system proceeds only if the `roles` claim is present and the user has one of these roles:

```ruby
claims['roles'].present? && (claims['roles'].include?('admin') || claims['roles'].include?('user:write'))
```

To restrict endpoint access to users with the `admin` role, use the following formula:

```ruby
claims['roles'].include?('admin')
```

#### Locale enforcement

The following formula ensures that only users with the `en-US` locale can access the endpoint. If the locale claim does not match, the system denies the request.

```ruby
claims['locale'] == 'en-US'
```

## Error handling

When a claim evaluates to `false`, the system rejects the request and returns a `401 Unauthorized` error code. Claim expressions that cannot be evaluated or parsed also return a `401 Unauthorized` error and include specific details about the error.

> **LIMITATIONS**
> 
> The following limitations apply when using custom authorization:
> 
> - The maximum length of a claim expression is 1000 characters.
> - Additional latency of 5-10ms per request may occur due to custom claims.

---
