---
url: 'https://docs.workato.com/en/developing-connectors/sdk/guides/data-formats.md'
description: >-
  Learn how the Workato connector SDK handles JSON, XML, multipart form, and
  URL-encoded data formats when connecting to APIs.
---

# Handling different data formats

When looking to connect to an API, one of the first questions to ask is what data format the API supports. The Workato SDK supports the following data formats which should cover all but a small minority of APIs out there. The Workato Connector SDK allows you to send and receive data using various `Content-Types`:

- JSON
- XML
- Multipart Form
- URL Encoded Form

Before we start, it is also important to get familiar with the different types of [HTTP request methods](/en/developing-connectors/sdk/sdk-reference/http). These HTTP request methods are what give life to the actions that you are building.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/data-formats/json-format.md
description: >-
  Send and receive JSON data in connector SDK actions and triggers, the default
  format Workato applies to HTTP requests.
---

# How-to guides - JSON data format

The Workato SDK's default expected data format is JSON. Action and trigger inputs will be passed as JSON payloads if no data format is specified. A JSON parser error will be shown if the SDK expected JSON and got another data format.

When you declare any HTTP request, Workato assumes the outgoing request and incoming response is in JSON. We help you append the appropriate headers `Accept: application/json` and `Content-Type: application/json` to the outgoing request.

Below we have an example of an action titled `post_message`. This simple action collects input from the user based on fields defined in the `input_fields` key in the `post_message` action and when the action is executed in a recipe, the execute key is run that creates a `POST` HTTP call to `https://api.ciscospark.com/v1/messages` with `input` as its body.

## Sample code snippet

```ruby
{
  title: 'My cisco connector',

  connection: {
    # Some code here
  },
  test: {
    # Some code here
  },

  actions: {
    post_message: {
      input_fields: lambda do
        [
          {
            name: "roomId"
          },
          {
            name: "text"
          }
        ]
      end,

      execute: lambda do |connection,input|
        post("https://api.ciscospark.com/v1/messages", input)
      end,

      output_fields: lambda do
        [
          {
            name: "id"
          },
          {
            name: "roomId"
          },
          {
            name: "roomType"
          },
          {
            name: "text"
          },
          {
            name: "personId"
          },
          {
            name: "personEmail"
          },
          {
            name: "created"
          }
        ]
      end
    }
  },

  triggers: {
    # Some code here
  },
  object_definitions: {
    # Some code here
  },
  pick_lists: {
    # Some code here
  },
  methods: {
    # Some code here
  },
}
```

Here we have the resultant request that is sent when the `execute` key above is executed. We default your `Content-Type` header to `application/json` and also format your input as key-value pairs in a JSON formatted string. This minimizes the amount of pre and post request processing that you need to do.

## Request

Now lets go through what happens when we run the `post_message` action that we just defined. Below we go through the POST HTTP request we send out to [https://api.ciscospark.com/v1/messages](https://api.ciscospark.com/v1/messages)

> **HEADERS AND BODY SECTIONS**
> 
> `POST` HTTP requests are usually divided into two sections: `Headers` and `Body`. The request headers define the HTTP method and include metadata related to the request. The request body contains the actual content or payload.

### Request headers

Since no data format was declared in our action, Workato defaults to JSON and assigns `Content-Type` to `application/json`. This tells the API we sent the request to that our request body is in a JSON data format.

```http
POST https://api.ciscospark.com/v1/messages
Accept  application/json
Content-Type  application/json
Authorization Bearer ---
```

### Request body:

This request body is generated based on the user's input and transformed into a JSON format by Workato. This request body corresponds to a user's input for the `roomId` field being `1234` and `text` field being `testing`.

```json
{
  "roomId":"1234",
  "text":"testing"
}
```

## Response

Whenever you send a HTTP request, you expect a response back which contains a few components

### Response status code

The response status code is an important way to know whether your request to the API was good. `HTTP/1.1 200 OK`

### Response headers

This is similar to request headers and contains metadata about the response body.

### Response body:

The response body is where the API sends the most of information in response to your request.

```json
{
  "id":"1",
  "roomId":"1234",
  "roomType":"group",
  "text":"testing",
  "personId":"101",
  "personEmail":"eeshan@workato.com",
  "created":"2017-03-26T13:28:22.131Z"
}
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/data-formats/xml-format.md
description: >-
  Learn how to send and parse XML payloads in Workato Connector SDK actions
  using request_format_xml, response_format_xml, and format_xml.
---

# How-to guides - XML data format

XML data format can be specified using the following SDK methods:

| Method | Description |
| --- | --- |
| `request_format_xml` | Convert request body to XML format |
| `response_format_xml` | Expect response body in XML format |
| `format_xml` | Convert request and expect response body in XML format |

## Forming XML payload in request

Since custom connector actions receive data in the form of ruby hashes, you will have to convert these hashes into an XML by chaining one of the formatting methods to the end of the request. This example explores making requests to Intacct web services with XML data format.

According to the [Intacct documentation](https://developer.intacct.com/wiki/web-services-api-30-calls), all requests should be made to the same endpoint as a POST request: `https://api.intacct.com/ia/xml/xmlgw.phtml` where requests are expected to be in XML data formats.

### Sample code snippet

```xml
<request>
  <control>
    <senderid>SENDER_ID</senderid>
    <password>PASSWORD</password>
    <controlid>testControlId</controlid>
    <uniqueid>false</uniqueid>
    <dtdversion>3.0</dtdversion>
  </control>
  <operation>
    <authentication>
      <login>
        <userid>USER_ID</userid>
        <companyid>COMPANY_ID</companyid>
        <password>PASSWORD</password>
      </login>
    </authentication>
    <content>
      <function controlid="testControlId">
        <inspect>
          <object>USERINFO</object>
        </inspect>
      </function>
    </content>
  </operation>
</request>
```

Here is a sample action to retrieve GL Account information, **Get GL account**.

```ruby
get_GL_account: {
  input_fields: lambda do
    [
      {
        name: "key",
        label: "Record ID",
        optional: false
      }
    ]
  end,

  execute: lambda do |connection, input|
    response = post("https://api.intacct.com/ia/xml/xmlgw.phtml").
      payload(
        "control": [
          {
            "senderid": [{ "content!": connection["sender_id"] }],
            "password": [{ "content!": connection["sender_password"] }],
            "controlid": [{ "content!": "testControlId" }],
            "uniqueid": [{ "content!": false }],
            "dtdversion": [{ "content!": 3.0 }]
          }
        ],
        "operation": [
          {
            "authentication": [
              {
                "login": [
                  {
                    "userid": [{ "content!": connection["login_username"] }],
                    "companyid": [{ "content!": connection["company_id"] }],
                    "password": [{ "content!": connection["login_password"] }]
                  }
                ]
              }
            ]
            "content": [
              {
                "function": [
                  {
                    "@controlid": "testControlId",
                    "get_list": [
                      {
                      "@object": "glaccount",
                      "@maxitems": "1"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]).
        headers("Content-type": "x-intacct-xml-request").
        format_xml("request").
        dig("response", 0,
            "operation", 0,
            "result", 0,
            "data", 0,
            "glaccount", 0) || {}

    response.inject({}) do |hash (key, value)|
      hash.merge(
        {
          key => value.dig(0, "content!")
        })
    end
  end,

  output_fields: lambda do |object_definitions|
    object_definitions["budget"]
  end
}
```

That is a handful! Let's break it down. Firstly, we define a POST to request to the appropriate endpoint:

```ruby
post("https://api.intacct.com/ia/xml/xmlgw.phtml")
```

Next, we add a payload to the request in the form of a hash first:

```ruby
.payload("control": [
         {
           "senderid": [{ "content!": connection["sender_id"] }],
           "password": [{ "content!": connection["sender_password"] }],
           "controlid": [{ "content!": "testControlId" }],
           "uniqueid": [{ "content!": false }],
           "dtdversion": [{ "content!": 3.0 }]
         }
       ],
       "operation": [
         {
           "authentication": [
             {
               "login": [
                 {
                   "userid": [{ "content!": connection["login_username"] }],
                   "companyid": [{ "content!": connection["company_id"] }],
                   "password": [{ "content!": connection["login_password"] }]
                 }
               ]
             }
           ],
           "content": [
             {
               "function": [
                 {
                   "@controlid": "testControlId",
                   "get_list": [
                     {
                       "@object": "glaccount",
                       "@maxitems": "1"
                     }
                   ]
                 }
               ]
             }
           ]
         }
       ])
```

Elements are represented by arrays of hashes, since XML elements can repeat without any extra notation. Element data is defined using the `content!` key and attributes using `@` prefix (example: `@object` and `@maxitems`).

The resultant XML body looks like this:

```xml
<control>
  <senderid>SENDER_ID</senderid>
  <password>PASSWORD</password>
  <controlid>testControlId</controlid>
  <uniqueid>false</uniqueid>
  <dtdversion>3.0</dtdversion>
</control>
<operation>
  <authentication>
    <login>
      <userid>USER_ID</userid>
      <companyid>COMPANY_ID</companyid>
      <password>PASSWORD</password>
    </login>
  </authentication>
  <content>
    <function controlid="testControlId">
      <get_list object="glaccount" maxitems="1"/>
    </function>
  </content>
</operation>
```

Defining value for an XML element is done using the `content!` key. For example, to assign password to the `<senderid>` element, the hash looks like this:

```ruby
{
  "senderid": [{ "content!": connection["sender_id"] }]
}
```

Next, how do we form a complex XML element? First, let's form an XML element that has a single occurrence (object type). For example, the `<control>` element in the request body is a complex element type with a number of elements nested within. The resultant partial XML should look like this:

```xml
<control>
  <senderid>SENDER_ID</senderid>
  <password>PASSWORD</password>
  <controlid>testControlId</controlid>
  <uniqueid>false</uniqueid>
  <dtdversion>3.0</dtdversion>
</control>
```

To form this, the equivalent hash should not have `content!` defined immediately in the `control` hash. Instead, define an array of a single hash that contains nested keys, one for each element that belongs in the `<control>` element.

```ruby
"control": [
  {
    "senderid": [{ "content!": connection["sender_id"] }],
    "password": [{ "content!": connection["sender_password"] }],
    "controlid": [{ "content!": "testControlId" }],
    "uniqueid": [{ "content!": false }],
    "dtdversion": [{ "content!": 3.0 }]
  }
]
```

Notice that all elements immediately under the `<control>` element are primitive types. Each of these elements contain only a value and optionally, attributes.

Now, we know how to define values for primitive XML elements. What about XML attributes? Let's look at the `<content>` element in the XML body to see how it's done.

```xml
<content>
  <function controlid="testControlId">
    <get_list object="glaccount" maxitems="1"/>
  </function>
</content>
```

This XML element has attributes defined in 2 elements. First, in a complex element `<function>` as well as a primitive element `<get_list>`. To form this XML, the equivalent hash structure looks like this:

```ruby
"content": [
  {
    "function": [
      {
        "@controlid": "testControlId",
        "get_list": [
          {
            "@object": "glaccount",
            "@maxitems": "1"
          }
        ]
      }
    ]
  }
]
```

Attributes and nested elements in a complex XML element are defined with the same hierarchy, but with the `@` prefix to indicate an attribute. (`"get_list"` key for `<get_list>` element and `"@controlid"` key for `controlid` attribute)

Similarly, element value and attributes in a primitive XML element are defined with the same hierarchy. (`"content!"` key for value of `<get_list>` element and `"@object"` key for `object` attribute) In this example, the `<get_list>` element is not assigned a value. If we were to assign one, the equivalent hash will look like this:

```ruby
"content": [
  {
    "function": [
      {
        "@controlid": "testControlId",
        "get_list": [
          {
            "@object": "glaccount",
            "@maxitems": "1",
            "content!": input["key"]
          }
        ]
      }
    ]
  }
]
```

Which will be converted into this XML:

```xml
<content>
  <function controlid="testControlId">
    <get_list object="glaccount" maxitems="1">KEY_VALUE<get_list>
  </function>
</content>
```

Next, we add the necessary headers with the headers shorthand method:

```ruby
.headers("Content-type": "x-intacct-xml-request")
```

Finally, we use the `format_xml` method (since we require both request and response in XML) and pass it the root element name as an argument, `<request>`)

```ruby
.format_xml("request")
```

## Handling XML from response

Now, the response from the same request will be in this form:

```xml
<response>
  <control>
    <status>success</status>
    <senderid>SENDER_ID</senderid>
    <controlid>testControlId</controlid>
    <uniqueid>false</uniqueid>
    <dtdversion>3.0</dtdversion>
  </control>
  <operation>
    <authentication>
      <status>success</status>
      <userid>USER_ID</userid>
      <companyid>COMPANY_ID</companyid>
      <sessiontimestamp>2017-03-26T05:24:25-07:00</sessiontimestamp>
    </authentication>
    <result>
      <status>success</status>
      <function>get_list</function>
      <controlid>testControlId</controlid>
      <listtype start="0" end="0" total="107">glaccount</listtype>
      <data>
        <glaccount>
          <recordno>1</recordno>
          <glaccountno>1000</glaccountno>
          <title>Chase Operating Account</title>
          <normalbalance>debit</normalbalance>
          <accounttype>balancesheet</accounttype>
          <closingtype>closed to account</closingtype>
          <closingaccountno/>
          <whenmodified>06/03/2016 20:19:30</whenmodified>
          <status>active</status>
          <requiredept>false</requiredept>
          <requireloc>false</requireloc>
          <taxable>false</taxable>
          <taxcode/>
          <mrccode/>
          <alternativeaccount>None</alternativeaccount>
          <requireproject>false</requireproject>
          <requirecustomer>false</requirecustomer>
          <requirevendor>false</requirevendor>
          <requireemployee>false</requireemployee>
          <requireitem>false</requireitem>
        </glaccount>
      </data>
    </result>
  </operation>
</response>
```

Because `format_xml` was called in the request, Workato SDK returns an equivalent hash. Similar to request:

- elements are represented by arrays of hashes, since XML elements can repeat without any extra notation
- elements attributes has `@` prefixed with the same hierarchy as nested elements and element values
- element values are passed as values of the `"content!"` key

```ruby
{
  "response"=>[
    {
      "control"=>[
        {
          "status"=>[{ "content!"=>"success" }],
          "senderid"=>[{ "content!"=>"SENDER_ID" }],
          "controlid"=>[{ "content!"=>"testControlId" }],
          "uniqueid"=>[{ "content!"=>"false" }],
          "dtdversion"=>[{ "content!"=>"3.0" }]
        }
      ],
      "operation"=>[
        {
          "authentication"=>[
            {
              "status"=>[{ "content!"=>"success" }],
              "userid"=>[{ "content!"=>"USER_ID" }],
              "companyid"=>[{ "content!"=>"COMPANY_ID" }],
              "sessiontimestamp"=>[{ "content!"=>"2017-03-26T08:25:12-07:00" }]
            }
          ],
          "result"=>[
            {
              "status"=>[{ "content!"=>"success" }],
              "function"=>[{ "content!"=>"get_list" }],
              "controlid"=>[{ "content!"=>"testControlId" }],
              "listtype"=>[
                {
                  "@start"=>"0",
                  "@end"=>"0",
                  "@total"=>"107",
                  "content!"=>"glaccount"
                }
              ],
              "data"=>[
                {
                  "glaccount"=>[
                    {
                      "recordno"=>[{ "content!"=>"1" }],
                      "glaccountno"=>[{ "content!"=>"1000" }],
                      "title"=>[{ "content!"=>"Chase Operating Account" }],
                      "normalbalance"=>[{ "content!"=>"debit" }],
                      "accounttype"=>[{ "content!"=>"balancesheet" }],
                      "closingtype"=>[{ "content!"=>"closed to account" }],
                      "closingaccountno"=>[{}],
                      "whenmodified"=>[{ "content!"=>"06/03/2016 20:19:30" }],
                      "status"=>[{ "content!"=>"active" }],
                      "requiredept"=>[{ "content!"=>"false" }],
                      "requireloc"=>[{ "content!"=>"false" }],
                      "taxable"=>[{ "content!"=>"false" }],
                      "taxcode"=>[{}],
                      "mrccode"=>[{}],
                      "alternativeaccount"=>[{ "content!"=>"None" }],
                      "requireproject"=>[{ "content!"=>"false" }],
                      "requirecustomer"=>[{ "content!"=>"false" }],
                      "requirevendor"=>[{ "content!"=>"false" }],
                      "requireemployee"=>[{ "content!"=>"false" }],
                      "requireitem"=>[{ "content!"=>"false" }]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

Hence, we will need to extract the desired data using the `dig` method.

```ruby
.dig("response", 0,
     "operation", 0,
     "result", 0,
     "data", 0,
     "glaccount", 0)
```

This returns us the hash:

```ruby
{
  "recordno"=>[{ "content!"=>"1" }],
  "glaccountno"=>[{ "content!"=>"1000" }],
  "title"=>[{ "content!"=>"Chase Operating Account" }],
  "normalbalance"=>[{ "content!"=>"debit" }],
  "accounttype"=>[{ "content!"=>"balancesheet" }],
  "closingtype"=>[{ "content!"=>"closed to account" }],
  "closingaccountno"=>[{}],
  "whenmodified"=>[{ "content!"=>"06/03/2016 20:19:30" }],
  "status"=>[{ "content!"=>"active" }],
  "requiredept"=>[{ "content!"=>"false" }],
  "requireloc"=>[{ "content!"=>"false" }],
  "taxable"=>[{ "content!"=>"false" }],
  "taxcode"=>[{}],
  "mrccode"=>[{}],
  "alternativeaccount"=>[{ "content!"=>"None" }],
  "requireproject"=>[{ "content!"=>"false" }],
  "requirecustomer"=>[{ "content!"=>"false" }],
  "requirevendor"=>[{ "content!"=>"false" }],
  "requireemployee"=>[{ "content!"=>"false" }],
  "requireitem"=>[{ "content!"=>"false" }]
}
```

Lastly, we convert the hash here back to a recipe-friendly output schema:

```ruby
response.inject({}) do |hash, (key, value)|
  hash.merge(
    {
      key => value.dig(0, "content!")
    })
end
```

The output of this action is then:

```json
{
  "recordno": "1",
  "glaccountno": "1000",
  "title": "Chase Operating Account",
  "normalbalance": "debit",
  "accounttype": "balancesheet",
  "closingtype": "closed to account",
  "closingaccountno": null ,
  "whenmodified": "06/03/2016 20:19:30",
  "status": "active",
  "requiredept": "false",
  "requireloc": "false",
  "taxable": "false",
  "taxcode": null ,
  "mrccode": null ,
  "alternativeaccount": "None",
  "requireproject": "false",
  "requirecustomer": "false",
  "requirevendor": "false",
  "requireemployee": "false",
  "requireitem": "false"
}
```

## Example action in action

### Request

```
POST https://api.intacct.com/ia/xml/xmlgw.phtml
Accept  application/xml
Accept-Encoding gzip, deflate
Content-Type  application/xml
Authorization Bearer
Content-type  x-intacct-xml-request
```

Request body:

```xml
<request>
  <control>
    <senderid>SENDER_ID</senderid>
    <password>PASSWORD</password>
    <controlid>testControlId</controlid>
    <uniqueid>false</uniqueid>
    <dtdversion>3.0</dtdversion>
  </control>
  <operation>
    <authentication>
      <login>
        <userid>USER_ID</userid>
        <companyid>COMPANY_ID</companyid>
        <password>PASSWORD</password>
      </login>
    </authentication>
    <content>
      <function controlid="testControlId">
        <get_list object="glaccount" maxitems="1"></get_list>
      </function>
    </content>
  </operation>
</request>
```

### Response

Status: `200 OK`

Response body:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<response>
  <control>
    <status>success</status>
    <senderid>SENDER_ID</senderid>
    <controlid>testControlId</controlid>
    <uniqueid>false</uniqueid>
    <dtdversion>3.0</dtdversion>
  </control>
  <operation>
    <authentication>
      <status>success</status>
      <userid>USER_ID</userid>
      <companyid>COMPANY_ID</companyid>
      <sessiontimestamp>2017-03-26T05:24:25-07:00</sessiontimestamp>
    </authentication>
    <result>
      <status>success</status>
      <function>get_list</function>
      <controlid>testControlId</controlid>
      <listtype start="0" end="0" total="107">glaccount</listtype>
      <data>
        <glaccount>
          <recordno>1</recordno>
          <glaccountno>1000</glaccountno>
          <title>Chase Operating Account</title>
          <normalbalance>debit</normalbalance>
          <accounttype>balancesheet</accounttype>
          <closingtype>closed to account</closingtype>
          <closingaccountno/>
          <whenmodified>06/03/2016 20:19:30</whenmodified>
          <status>active</status>
          <requiredept>false</requiredept>
          <requireloc>false</requireloc>
          <taxable>false</taxable>
          <taxcode/>
          <mrccode/>
          <alternativeaccount>None</alternativeaccount>
          <requireproject>false</requireproject>
          <requirecustomer>false</requirecustomer>
          <requirevendor>false</requirevendor>
          <requireemployee>false</requireemployee>
          <requireitem>false</requireitem>
        </glaccount>
      </data>
    </result>
  </operation>
</response>
```

Which is extracted and converted into:

```json
{
  "recordno": "1",
  "glaccountno": "1000",
  "title": "Chase Operating Account",
  "normalbalance": "debit",
  "accounttype": "balancesheet",
  "closingtype": "closed to account",
  "closingaccountno": null ,
  "whenmodified": "06/03/2016 20:19:30",
  "status": "active",
  "requiredept": "false",
  "requireloc": "false",
  "taxable": "false",
  "taxcode": null ,
  "mrccode": null ,
  "alternativeaccount": "None",
  "requireproject": "false",
  "requirecustomer": "false",
  "requirevendor": "false",
  "requireemployee": "false",
  "requireitem": "false"
}
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/data-formats/form-url-encoded.md
description: >-
  Send URL-encoded form data from connector SDK actions, with a HubSpot form
  submission example you can adapt to other APIs.
---

# How-to guides - URL Encoded Form

This request format can be declared in any keys (`execute`, `acquire`, `fields` etc.) in your custom connector code.

## Sample code snippet

Let's use the submit data to a form endpoint in [HubSpot API](https://developers.hubspot.com/docs/methods/forms/submit_form) as an example. This endpoint accepts form data in form urlencoded format.

A cURL example looks like this:

```sh
curl \
  https://forms.hubspot.com/uploads/form/v2/12345/67890 \
  -X POST \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'firstname=TestContact&lastname=FormSub&email=formsub@hubspot.com&newcustomproperty=testing&hs_context=%7B%22hutk%22%3A%2260c2ccdfe4892f0fa0593940b12c11aa%22%2C%22ipAddress%22%3A%22192.168.1.12%22%2C%22pageUrl%22%3A%22http%3A%2F%2Fdemo.hubapi.com%2Fcontact%2F%22%2C%22pageName%22%3A%22Contact%2BUs%22%2C%22redirectUrl%22%3A%22http%3A%2F%2Fdemo.hubapi.com%2Fthank-you%2F%22%7D'
```

This cURL command can be replicated in Workato:

```ruby
{
  title: "HubSpot",

  connection: {
    # Some code here
  },

  test: {
    # Some code here
  },

  actions: {
    submit_form: {
      input_fields: lambda do
        [
          {
            name: "portal_id",
            type: "string"
          },
          {
            name: "form_guid",
            type: "string"
          },
          {
            name: "hutk",
            type: "string"
          },
          {
            name: "ipAddress",
            type: "string"
          },
          {
            name: "pageUrl",
            type: "string"
          },
          {
            name: "pageName",
            type: "string"
          },
          {
            name: "redirectUrl",
            type: "string"
          }
        ]
      end,

      execute: lambda do |connection, input|
        post("https://forms.hubspot.com/uploads/form/v2/#{input['portal_id']}/#{input['form_guid']}").
          request_body(
            input.reject { |k,v| k == 'portal_id' || k == 'form_guid' }
          ).
          request_format_www_form_urlencoded


      end
    },

    output_fields: { ... }
  },

  triggers: {
    # Some code here
  },
  object_definitions: {
    # Some code here
  },
  pick_lists: {
    # Some code here
  },
  methods: {
    # Some code here
  }
```

## Components

| cURL | Workato |
| --- | --- |
| `curl https://forms.hubspot.com/uploads/form/v2/{portal_id}/{form_guid} -X POST` | `post("https://forms.hubspot.com/uploads/form/v2/#{input['portal_id']}/#{input['form_guid']}")` |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | `.request_format_www_form_urlencoded` |
| `-d '{data}'` | `.request_body(input.reject { |k,v| k == 'portal_id' || k == 'form_guid' })` |

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/data-formats/request_format_multipart_form.md
description: >-
  Learn how to send multipart form data in Workato Connector SDK requests to
  upload large files using the Content-Type header.
---

# How-to guides - Multipart Form

[Multipart form request](https://www.w3.org/TR/html401/interact/forms.html#h-17.13.4.2) is typically used to send large files and data to a server.

This request format can be declared in any keys (`execute`, `acquire`, `fields` etc.) in your custom adapter code. This is done by embedding the data format inside the `Content-Type` header.

## Sample code snippet

Let's use the Convert document endpoint in [IBM Watson API](https://www.ibm.com/watson/developercloud/document-conversion/api/v1/#convert-document) as an example. This endpoint accepts a document in multipart/form-data format.

A cURL example looks like this:

```sh
curl \
  https://gateway.watsonplatform.net/document-conversion/api/v1/convert_document?version=2015-12-15 \
  -X POST \
  -u "{username}":"{password}" \
  -F config="{\"conversion_target\":\"answer_units\"}" \
  -F "file=@sample.pdf;type=application/pdf"
```

Workato:

```ruby
{
  title: "IBM Watson",

  connection: {
    # Some code here
  },

  test: {
    # Some code here
  },

  actions: {
    upload_file: {
      input_fields: lambda do
        [
          { name: "file_name", type: "string" },
          { name: "file_data", type: "string" },
          { name: "conversion_target", type: "string" }
        ]
      end,

      execute: lambda do |connection, input|
        post("https://gateway.watsonplatform.net/document-conversion/api/v1/convert_document").
          params(version: "2015-12-15").
          request_format_multipart_form.
          payload(file: [input['file_data'], 'application/pdf'],
                  file_name: input['file_name'],
                  config: "{\"conversion_target\":\"#{input['conversion_target']}\"}")
      end
    },

    output_fields: {
      # Some code here
    }
  },

  triggers: {
    # Some code here
  },
  object_definitions: {
    # Some code here
  },
  pick_lists: {
    # Some code here
  },
  methods: {
    # Some code here
  }
```

In the SDK, notice that the `file` key in the payload takes an array of length 2. This defines the request as form data. The first item in the array is the file data and the second item is the media type (MIME type) of the input file.

## Components

| cURL | Workato |
| --- | --- |
| `curl https://gateway.watsonplatform.net/document-conversion/api/v1/convert_document?version=2015-12-15 -X POST` | `post("https://gateway.watsonplatform.net/document-conversion/api/v1/convert_document")` `.params(version: "2015-12-15")` |
| `-u "{username}":"{password}"` | This is defined in the \[connection\](../authentication/basic-authentication.md) key and is automatically added onto the outgoing request. |
| `-F config="{\"conversion_target\":\"answer_units\"}"` `-F "file=@sample.pdf;type=application/pdf"` | `.request_format_multipart_form` `.payload(`     `file: [input['file_data'], 'application/pdf'],`     `file_name: input['file_name'],`     `config: "{\"conversion_target\":\"#{input['conversion_target']}\"}")` |

## Variations

Sometimes, the name of the file must be explicitly stated in the multipart form as part of the file payload, instead of a separate key-value pair, like the previous example. To satisfy this, you can adjust your payload to this.

> **FILE\_NAME IS DIFFERENT FROM FILE**
> 
> `file_name` in the following example is different from the payload key (`file`).

```ruby
execute: lambda do |connection, input|
  post("https://gateway.watsonplatform.net/document-conversion/api/v1/convert_document").
    params(version: "2015-12-15").
    request_format_multipart_form.
    payload(file: [input['file_data'], 'application/pdf', input['file_name']],
            config: "{\"conversion_target\":\"#{input['conversion_target']}\"}")
end
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions.md
description: >-
  Learn how to build actions that give custom connectors functionality, from
  creating and retrieving objects to file transfers and custom actions.
---

# Building actions

Once you have figured out how to connect to your applications, you can build actions for your connectors. Actions give your connectors functionality and purpose, without them, your connectors can't really do much. In this segment, we go through the building of various types of actions:

- Creating objects
- Updating objects
- Get (Retrieving) objects
- Download files/documents
- Upload files/documents
- Adding custom actions
- Multi-step actions that work with Asynchronous APIs
- Multi-threaded actions which support sending multiple requests

> **TIP**
> 
> Before we start, it is also important to get familiar with the different types of [HTTP request methods](/en/developing-connectors/sdk/sdk-reference/http) which power all actions.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) quota.
> 
> You can use the [checkpoint!](/en/developing-connectors/sdk/sdk-reference/ruby_methods#checkpoint) method with file streaming actions to transfer files that exceed the timeout limit. The `checkpoint!` method checks the duration of an action's execution. If it exceeds 120 seconds, Workato refreshes the timeout with a slight delay to ensure fair processing.

### General structure of actions

Refer to the `actions` key section in the [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions) for full details.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/create-objects.md
description: >-
  Build a custom connector action that creates objects in a target application
  using the POST HTTP request method.
---

# How-to guides - Creating objects

In this segment, we will be going through the creation of actions that help create objects in our target application. Typically, The `POST` HTTP request method is used to send requests to create objects.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.

## Sample connector - Zuora

```ruby
{
  title: 'My Zuora connector',

  # More connector code here
  actions: {
    create_account: {
      title: 'Create account',

      subtitle: "Creates an account in Zuora",

      description: lambda do |input, picklist_label|
        "Create <span class='provider'>account</span> in " \
        "<span class='provider'>Zuora</span>"
      end,

      help: "Creates a new account in Zuora",

      input_fields: lambda do |object_definitions|
        [
          {
            name: "AccountNumber",
            label: "Account Number",
            hint: "Unique account number assigned to the account. " \
            "Leave null to auto-generate."
          },
          {
            name: "AccountName",
            label: "Account name",
            hint: "The name of newly created account."
          },
          {
            name: "Currency",
            label: "Currency",
            hint: "Currency that the customer is billed in.",
            optional: false
          }
        ]
      end,

      execute: lambda do |connection, input|
        post("https://rest.zuora.com/v1/object/account", input).
          after_error_response(/.*/) do |_, body, _, message|
            error("#{message}: #{body}")
          end
      end,

      output_fields: lambda do |object_definitions|
        [
          { name: "Success", type: "boolean", control_type: "checkbox" },
          { name: "Id" },
          {
            name: "Errors",
            type: "array",
            of: "object",
            properties: [{ name: "Code" }, { name: "Message" }]
          }
        ]
      end,

      sample_output: lambda do |connection, input|
        {
          "success" => "true",
          "Id" => "107bb8280175668b1f47e51710214497"
        }
      end
    }
  }
  # More connector code here
}
```

![Selecting the create account action](/assets/create_overall.Cod89E_K.png)_Selecting the create account action_

## Step 1 - Action title, subtitle, description, and help

The first step to making a good action is to properly communicate what the actions does, how it does it and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#title)

## Step 2 - Define input fields

```ruby
  input_fields: lambda do |object_definitions|
    [
      {
        name: "AccountNumber",
        label: "Account Number",
        hint: "Unique account number assigned to the account. " \
        "Leave null to auto-generate."
      },
      {
        name: "AccountName",
        label: "Account name",
        hint: "The name of newly created account."
      },
      {
        name: "Currency",
        label: "Currency",
        hint: "Currency that the customer is billed in.",
        optional: false
      }
    ]
  end
```

![Create account input fields](/assets/create_account_input.BTV-4qR1.png)_Create account input fields_

This component tells Workato what fields to show to a user trying to create an object. In the case of creating an account in Zuora for example, the user has to input the `AccountNumber`, `AccountName` and `Currency` of the new account to be created. Do take note that for the `Currency` input field, the "optional" key is assigned the value "false", this means that users must provide a value of the currency that the customer is billed in, if not, the user cannot proceed in the building of the recipe.

Various other key value pairs exist for input/output fields other than the ones defined above. Refer to [Input fields](/en/developing-connectors/sdk/sdk-reference/actions#input-fields) for more information.

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 3 - Defining the execute key

The execute key tells Workato the endpoint to send the request to and using which HTTP request method. In this example, we send our request to `https://rest.zuora.com/v1/object/account` using the `POST` method. We also append the `after_error_response` method to the request to catch any errors and to display them to users to aid in the debugging during recipe building.

```ruby
  execute: lambda do |connection, input|
    post("https://rest.zuora.com/v1/object/account", input).
      after_error_response(/.*/) do |_, body, _, message|
        error("#{message}: #{body}")
      end
  end
```

![Create account error](/assets/create_error.B78gvRXW.png)_Error example_

To know more about the execute key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#execute)

## Step 4 - Defining output fields

This section tells us what datapills to show as the output of the trigger. The `name` attributes of each datapill should match the keys in the output of the `execute` key.

```ruby
  output_fields: lambda do |object_definitions|
    [
      { name: "Success", type: "boolean", control_type: "checkbox" },
      { name: "Id" },
      {
        name: "Errors",
        type: "array",
        of: "object",
        properties: [{ name: "Code" }, { name: "Message" }]
      }
    ]
  end
```

![Create account output fields](/assets/create_output.PgKTVjl-.png)_Create account output fields_

To know more about the output fields key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#output-fields)

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 5 - Defining sample output

A supplementary component to a connector, the sample output key nonetheless greatly improves a user's experience by telling users the general data type and format of output fields to expect. This allows users to build recipes more quickly.

```ruby
  sample_output: lambda do |connection, input|
    {
      "success" => "true",
      "Id" => "107bb8280175668b1f47e51710214497"
    }
  end
```

To know more about the sample output key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#sample-output)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/update-objects.md
description: >-
  Build a custom connector SDK action that updates objects in a target
  application using PUT requests, with a Zuora example.
---

# How-to guides - Updating objects

In this segment, we will be going through the creation of actions that help update objects in our target application. Typically, The `PUT` HTTP request method is used to send requests to update objects.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.

## Sample connector - Zuora

```ruby
{
  title: 'My Zuora connector',

  # More connector code here
  actions: {
    update_account: {
      title: "Update account",

      subtitle: "Updates an account in Zuora",

      description: lambda do |input, picklist_label|
        "Update <span class='provider'>account</span> in " \
        "<span class='provider'>Zuora</span>"
      end,

      help: "Updates an existing account in Zuora",

      input_fields: lambda do |object_definitions|
        [
          {
            name: "BillingDate",
            label: "Billing date",
            hint: "The date at which to bill an account."
          },
          {
            name: "AccountName",
            label: "Account name",
            hint: "The name of newly created account."
          },
          {
            name: "Currency",
            label: "Currency",
            hint: "Currency that the customer is billed in."
          }
        ]
      end,

      execute: lambda do |connection, input|
        put("https://rest.zuora.com/v1/object/account", input).
          after_error_response(/.*/) do |_, body, _, message|
            error("#{message}: #{body}")
          end
      end,

      output_fields: lambda do |object_definitions|
        [
          { name: "Success", type: "boolean", control_type: "checkbox" },
          { name: "Id" },
          {
            name: "Errors",
            type: "array",
            of: "object",
            properties: [{ name: "Code" }, { name: "Message" }]
          }
        ]
      end,

      sample_output: lambda do |connection, input|
        {
          "success" => "true",
          "Id" => "107bb8280175668b1f47e51710214497"
        }
      end
    }
  }
  # More connector code here
}
```

![Selecting the update account action](/assets/update_overall.D7c2Cftx.png)_Selecting the update account action_

## Step 1 - Action title, subtitle, description, and help

The first step to making a good action is to properly communicate what the actions does, how it does it and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#title)

## Step 2 - Define input fields

```ruby
  input_fields: lambda do |object_definitions|
    [
      {
        name: "id",
        label: "Account ID",
        hint: "ID of the account you wish to update.",
        optional: false
      },
      {
        name: "BillingDate",
        label: "Billing date",
        hint: "The date at which to bill an account."
      },
      {
        name: "AccountName",
        label: "Account name",
        hint: "The name of newly created account."
      },
      {
        name: "Currency",
        label: "Currency",
        hint: "Currency that the customer is billed in."
      }
    ]
  end
```

![Update account input fields](/assets/update_input.B8cN0yIe.png)_Update account input fields_

This component tells Workato what fields to show to a user trying to update an object. In the case of updating an account in Zuora for example, the user has to input the `id`, `BillingDate`, `AccountName` and `Currency` of the existing account to be updated.

Do note the differences from the [create object](/en/developing-connectors/sdk/guides/building-actions/create-objects) action, it is typical that the fields for different actions to differ, although the particular object involved remain the same. From the example provided, the `AccountNumber` of the account is not updatable, hence the field should not be available to users in this action. Also, the `Currency` field is now optional to fill in as there is already an existing currency attached to the account.

Various other key value pairs exist for input/output fields other than the ones defined above. Refer to [Input fields](/en/developing-connectors/sdk/sdk-reference/actions#input-fields) for more information.

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 3 - Defining the execute key

The execute key tells Workato the endpoint to send the request to and using which HTTP request method. In this example, we send our request to `https://rest.zuora.com/v1/object/account` using the `PUT` method. We also append the `after_error_response` method to the request to catch any errors and to display them to users to aid in the debugging during recipe building.

```ruby
  execute: lambda do |connection, input|
    post("https://rest.zuora.com/v1/object/account", input).
      after_error_response(/.*/) do |_, body, _, message|
        error("#{message}: #{body}")
      end
  end
```

![Update account error](/assets/update_error.DEzROAeT.png)_Error example_

To know more about the execute key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#execute)

## Step 4 - Defining output fields

This section tells us what datapills to show as the output of the trigger. The `name` attributes of each datapill should match the keys in the output of the `execute` key.

```ruby
  output_fields: lambda do |object_definitions|
    [
      { name: "Success", type: "boolean", control_type: "checkbox" },
      { name: "Id" },
      {
        name: "Errors",
        type: "array",
        of: "object",
        properties: [{ name: "Code" }, { name: "Message" }]
      }
    ]
  end
```

![Update account output fields](/assets/update_output.CsPvhWgm.png)_Update account output fields_

To know more about the output fields key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#output-fields)

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 5 - Defining sample output

A supplementary component to a connector, the sample output key nonetheless greatly improves a user's experience by telling users the general data type and format of output fields to expect. This allows users to build recipes more quickly.

```ruby
  sample_output: lambda do |connection, input|
    {
      "success" => "true",
      "Id" => "107bb8280175668b1f47e51710214497"
    }
  end
```

To know more about the sample output key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#sample-output)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/get-objects.md
description: >-
  Build a custom connector action that retrieves object details from a target
  application using the GET HTTP request method.
---

# How-to guides - Get (Retrieve) objects

In this segment, we will be going through the creation of actions that help retrieve information of an object in our target application. Typically, The `GET` HTTP request method is used to send requests to retrieve objects.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.

## Sample connector - Zuora

```ruby
{
  title: 'My Zuora connector',

  # More connector code here
  actions: {
    get_account: {
      title: "Get account",

      subtitle: "Retrieves details of an account in Zuora",

      description: lambda do |input, picklist_label|
        "Get an <span class='provider'>account</span> in " \
        "<span class='provider'>Zuora</span>"
      end,

      help: "Retrieves the information of an existing account in Zuora",

      input_fields: lambda do |object_definitions|
        [
          {
            name: "id",
            label: "Account ID",
            hint: "The ID of the specific account that you wish to retrieve."
          }
        ]
      end,

      execute: lambda do |connection, input|
        get("https://rest.zuora.com/v1/object/account/#{input["Id"]}", input).
          after_error_response(/.*/) do |_, body, _, message|
            error("#{message}: #{body}")
          end
      end,

      output_fields: lambda do |object_definitions|
        [
          # Various output fields
        ]
      end
    }
  }
  # More connector code here
}
```

![Selecting the get account action](/assets/get_overall.CQD8Yomy.png)_Selecting the get account action_

## Step 1 - Action title, subtitle, description, and help

The first step to making a good action is to properly communicate what the actions does, how it does it and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#title)

## Step 2 - Define input fields

```ruby
  input_fields: lambda do |object_definitions|
    [
      {
        name: "id",
        label: "Account ID",
        hint: "The ID of the specific account that you wish to retrieve."
      }
    ]
  end
```

![Get account input fields](/assets/get_input.Ca0v6_IF.png)_Get account input fields_

This component tells Workato what fields to show to a user trying to retrieve an object. In the case of retrieving an account in Zuora for example, the user has to input the ID of the account to be retrieved.

Various other key value pairs exist for input/output fields other than the ones defined above. Refer to [Input fields](/en/developing-connectors/sdk/sdk-reference/actions#input-fields) for more information.

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 3 - Defining the execute key

The execute key tells Workato the endpoint to send the request to and using which HTTP request method. In this example, we send our request to `https://rest.zuora.com/v1/object/account/#{input["Id"]}` using the `Get` method. We also append the `after_error_response` method to the request to catch any errors and to display them to users to aid in the debugging during recipe building.

For this get action, we append the `id` - Account ID input by the user to the API endpoint to tell Workato and subsequently Zuora, which specific account to retrieve.

```ruby
  execute: lambda do |connection, input|
    get("https://rest.zuora.com/v1/object/account/#{input["id"]}", input).
      after_error_response(/.*/) do |_, body, _, message|
        error("#{message}: #{body}")
      end
  end
```

![Get account error](/assets/create_error.B78gvRXW.png)_Error example_

To know more about the execute key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#execute)

## Step 4 - Defining output fields

This section tells us what datapills to show as the output of the trigger. The `name` attributes of each datapill should match the keys in the output of the `execute` key.

```ruby
  output_fields: lambda do |object_definitions|
    [
      # Various output fields
    ]
  end
```

![Get account output fields](/assets/get_output.DYNX9VYj.png)_Get account output fields_

To know more about the output fields key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#output-fields)

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/multistep-actions.md
description: >-
  Build custom connector actions that work with asynchronous APIs, using
  reinvoke_after to poll a long-running job until it completes.
---

# How-to guides - Multistep actions

In this segment, we will be going through the creation of actions that work with asynchronous APIs. Typically, when working with asynchronous APIs to kickstart a long running job or process in a target application, often times you'll send a request and expect an ID that corresponds to that job or process. Your action would then want to constantly check back with the API to see if the job is completed before retrieving results or moving on to the next step in the recipe.

For example, when you send a request to Google BigQuery to start a query, Google BigQuery might send you back the job ID. Your task would be to now regularly check back with Google BigQuery to see if the query is completed before retrieving the rows.

Rather than having the user configure this logic in the recipe, you can now embed this entire logic into a single action with "multi-step" actions on your custom connector. To use "multi-step" actions, the `continue` argument is used in conjunction with a dedicated method called `reinvoke_after`. Read on below on how to configure this!

> **DEBUGGING LIMITATION IN TEST CODE TAB**
> 
> You can't debug multistep actions in Workato's SDK **Test code** tab. This may trigger an `uncaught throw :return_from_action` error. Instead, use the [SDK Gem](/en/developing-connectors/sdk/cli) to debug multistep actions.
> 
> Release the latest version of your custom connector before testing it in the recipe editor. This applies any changes made during debugging.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.

## Sample connector - Google BigQuery

```ruby
{
  title: 'My Google BigQuery connector',

  # More connector code here
  actions: {
       query: {
        title: "Execute query",

        subtitle: "Execute query in BigQuery",

        description: "Run Query in BigQuery",

        help: "This query runs synchronously for 25 seconds. If the query takes longer than that, it turns into an asynchronous action. There is a limit of ~38 minutes for the query to complete. ",

        input_fields: lambda do
          [
            {
              name: "project_id",
              control_type: 'select',
              pick_list: 'projects',
              optional: false
            },
            {
              name: "query",
              optional: false
            },
            {
              name: 'wait_for_query',
              control_type: 'checkbox',
              sticky: true,
            },
            {
              name: "output_fields",
              extends_schema: true,
              schema_neutral: false,
              sticky: true,
              control_type: 'schema-designer',
              label: 'Output columns',
              hint: 'Provide your output fields for your query if you are providing datapills in your query',
              item_label: 'Design your output columns',
              sample_data_type: 'csv' # json_input / xml
            },
          ]
        end,

        execute: lambda do |connection, input, eis, eos, continue|
          continue = {} unless continue.present?
          current_step = continue['current_step'] || 1
          max_steps = 30
          step_time = current_step * 60 # This helps us wait longer and longer as we increase in steps
          # Minimum step time is 60 seconds

          if current_step == 1 # First invocation
            payload = {
              query: input['query'],
              timeoutMs: '25000',
              useLegacySql: false
            }
            url = "https://bigquery.googleapis.com/bigquery/v2/projects/#{input['project_id']}/queries"
            response = post(url, payload)

            # If user wants to wait for query to complete and
            # job isn't complete after 25s
            if response['jobComplete'] == false && input['wait_for_query'].is_true?
              reinvoke_after(
                seconds: step_time,
                continue: {
                  current_step: current_step + 1,
                  jobid: response['jobReference']['jobId']
                }
              )
            # If user doesn't want to wait for query to complete and
            # job isn't complete after 25s
            elsif response['jobComplete'] == false
              { jobId: response['jobReference']['jobId'] }
            # Job is complete after 25s
            else
              call('format_rows', response)
            end
          # Subsequent invocations
          elsif current_step <= max_steps
            url = "https://bigquery.googleapis.com/bigquery/v2/projects/#{input['project_id']}/jobs/#{continue['jobid']}"
            response = get(url)
            # If job is still running
            if response['status']['state'] == "RUNNING"
              reinvoke_after(seconds: step_time.to_i, continue: { current_step: current_step + 1, jobid: continue['jobid']})
            # If status is done but there is an error
            elsif response['status']['state'] == "DONE" && response.dig('status', 'errorResult').present?
              error(response.dig('status', 'errorResult'))
            # If status is done
            else
              results = get("https://bigquery.googleapis.com/bigquery/v2/projects/#{input['project_id']}/queries/#{continue['jobid']}")
              call('format_rows', results)
            end
          else
            error("Job took too long!")
          end
        end,

        output_fields: lambda do |object_definitions, config_fields|
          schema = [
            {
              name: "jobId"
            },
            {
              name: "totalRows"
            },
            {
              name: "pageToken"
            },
            {
              name: "rows",
              type: "array",
              of: "object",
              properties: object_definitions['query_output']
            }
          ]
        end,

        summarize_output: ['rows']
      },
}
```

## Step 1 - Action title, subtitle, description, and help

The first step to making a good action is to properly communicate what the actions does, how it does it and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#title)

## Step 2 - Define input fields

```ruby
  input_fields: lambda do
    [
      {
        name: "project_id",
        control_type: 'select',
        pick_list: 'projects',
        optional: false
      },
      {
        name: "query",
        optional: false
      },
      {
        name: 'wait_for_query',
        control_type: 'checkbox',
        sticky: true,
      },
      {
        name: "output_fields",
        extends_schema: true,
        schema_neutral: false,
        sticky: true,
        control_type: 'schema-designer',
        label: 'Output columns',
        hint: 'Provide your output fields for your query if you are providing datapills in your query',
        item_label: 'Design your output columns',
        sample_data_type: 'csv' # json_input / xml
      },
    ]
  end,
```

This component tells Workato what fields to show to a user trying to execute the multistep action. In the case of executing a query in BigQuery for example, the user has to provide us the following:

1. Google BigQuery GCP project ID
2. The query to execute in Google BigQuery
3. Whether the action should wait for the query to complete
4. And the output columns expected from the query

## Step 3 - Defining the execute key

The execute key tells Workato the endpoint to send the request to and using which HTTP request method and also controls the entire logic as to how this action should interact with this asynchronous API. When configuring multistep actions, you will need to utilize the `continue` argument together with the `reinvoke_after` method. This will allow you to first invoke the `execute` lambda function to insert the query in Google BigQuery, optionally put the job to sleep to be woken up later to check if the query is done.

When the job is woken up, the `execute` lambda function is invoked again with the `continue` passed to it from the previous `reinvoke_after` call. This `continue` argument should have the job id of the Google BigQuery job created. We then check if the job is done. If it is still running, we put the job to sleep again. If the job is done, we can retrieve the results and send it as the output of the action.

> **TIP**
> 
> Step time must be set to a minimum of 60 seconds. If anything lower is supplied, Workato default to 60 seconds.

```ruby
  execute: lambda do |connection, input, eis, eos, continue|
    continue = {} unless continue.present? #For the first invocation, continue is nil
    current_step = continue['current_step'] || 1 #Instantiate current_step so we know what step we are on
    max_steps = 30 #IMPORTANT. you should set the max number of steps so your action doesn't continue forever. This will cause performance degradation in your recipes
    step_time = current_step * 10 # This helps us wait longer and longer as we increase in steps
    # Minimum step time is 60 seconds

    if current_step == 1 # First invocation
      payload = {
        query: input['query'],
        timeoutMs: '25000',
        useLegacySql: false
      }
      #Request below sends the query to BigQuery
      response = post("https://bigquery.googleapis.com/bigquery/v2/projects/#{input['project_id']}/queries", payload)

      #if Wait for query is false, the user can get the jobID back and get the results manually.
      if response['jobComplete'] == false && input['wait_for_query'].is_true?
        # reinvoke_after accepts 2 arguments.
        # seconds is an integer that tells us how long to put the job to sleep for. MINIMUM 5 SECONDS
        # continue is a hash is passed to the next invocation of the execute block when the job is woken up
        reinvoke_after(seconds: step_time, continue: { current_step: current_step + 1, jobid: response['jobReference']['jobId'] })
      elsif response['jobComplete'] == false
        { jobId: response['jobReference']['jobId'] }
      else
        call('format_rows', response)
      end
    elsif current_step <= max_steps  # Subsequent invocations
      response = get("https://bigquery.googleapis.com/bigquery/v2/projects/#{input['project_id']}/jobs/#{continue['jobid']}")

      # If job is still running, put to sleep again
      if response['status']['state'] == "RUNNING"
        reinvoke_after(seconds: step_time.to_i, continue: { current_step: current_step + 1, jobid: continue['jobid']})
      # If job is done but there was an error, raise an error
      elsif response['status']['state'] == "DONE" && response.dig('status', 'errorResult').present?
        error(response.dig('status', 'errorResult'))
      # Reaching here means job is done and there are results.
      else
        results = get("https://bigquery.googleapis.com/bigquery/v2/projects/#{input['project_id']}/queries/#{continue['jobid']}")
        call('format_rows', results)
      end
    # if we reach step 31, we need to raise an error and cancel the job.
    else
      error("Job took too long!")
    end
  end,
```

## Step 4 - Defining output fields

This section tells us what datapills to show as the output of the trigger. The `name` attributes of each datapill should match the keys in the output of the `execute` key.

```ruby
output_fields: lambda do |object_definitions, config_fields|
  schema = [
    {
      name: "jobId"
    },
    {
      name: "totalRows"
    },
    {
      name: "pageToken"
    },
    {
      name: "rows",
      type: "array",
      of: "object",
      properties: object_definitions['query_output']
    }
  ]
end,
```

> **Object definitions**
> 
> In this example, we make use of the `output_fields` given to us by the user in their input fields. Here is the object definition of `query_output`.
> 
> ```ruby
> query_output: {
>   fields: lambda do |connection, config_fields, object_definitions|
>     next if config_fields['output_fields'].blank?
>     parse_json(config_fields['output_fields'])
>   end
> }
> ```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/multi-threaded-actions.md
description: >-
  Build custom connector actions that send API requests in parallel across
  multiple threads to increase throughput and reduce execution time.
---

# How-to guides - Multi-threaded actions

In this segment, we will be going through the creation of actions that allow you to send requests in parallel across multiple threads. Data throughput can be a key concern for users and in some cases, APIs themselves may only support singleton ingestion endpoints or the batch sizes for requests are simply too low!

For example, imagine that you have thousands of contacts you want to sync into an app like [Intercom](https://developers.intercom.com/intercom-api-reference/reference#create-contact) but the API only supports inserting a single contact at a time. You could ask the recipe builder to loop over these contacts and ingest them 1 by 1 but that may lead to slow record ingestion times.

Rather than looping over thousands of contacts, you can use Multi-threaded actions to process them in batches (for example, of batch size 1000) and send API requests in parallel to increase overall throughput and reduce execution time.

> **NOTE**
> 
> When you build multi-threaded actions on the SDK CLI tool, take note that requests will be sent sequentially instead of across parallel threads.
> 
> This allows you to inspect requests individually for easier debugging.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.

## Sample connector - Intercom

```ruby
{
  title: 'My Intercom connector',

  # More connector code here
  actions: {
    create_contact: {
        title: "Create contacts",

        subtitle: "Creates multiple contacts in Intercom",

        description: "Create contacts in Intercom",

        input_fields: lambda do
          [
            {
              name: "contacts",
              type: "array",
              of: "object",
              properties: [
                {
                  control_type: "text",
                  label: "Role",
                  type: "string",
                  name: "role"
                },
                {
                  control_type: "text",
                  label: "External ID",
                  type: "string",
                  name: "external_id"
                },
                {
                  control_type: "text",
                  label: "Email",
                  type: "string",
                  name: "email"
                },
                {
                  control_type: "text",
                  label: "Phone",
                  type: "string",
                  name: "phone"
                },
                {
                  control_type: "text",
                  label: "Name",
                  type: "string",
                  name: "name"
                }
              ]
            }
          ]
        end,

        execute: lambda do |connection, input, eis, eos|
          # Pre-processing of the data.
          # For multithreading, we need to create an array of requests which we do over here.
          number_of_batches = input['contacts'].size
          batches = input['contacts'].map do |contact|
            post("contacts", contact)
          end

          # Sending of the requests in simultaneously using the parallel method
          # The output of a method is an array with 3 indexes.
          # The first index is a boolean to indicate that all requests were successful.
          # The second index is an array of the successful responses. Failed requests are indicated
          results = parallel(
              batches, # Each index in the batch array represents a single request
              threads: 20, # The max number of threads. Defaults to 1 and max is 20
              rpm: 100, # How many requests to send per minute
              )


          # Post-processing
          # Boolean to tell the user that all records were successful
          success = results[0]
          # An array of all the responses for successful records
          records_ingested = results[1].compact
          # Collecting all the failed records into an array
          records_failed = []
          results[2].each_with_index do |item, index|
            next unless item
            failed_record = {
              code: item,
              record: input['contacts'][index]
            }
            records_failed << failed_record
          end

          {
            success: success,
            records_ingested: records_ingested,
            records_failed: records_failed
          }
        end,

        output_fields: lambda do |object_definitions, config_fields|
          object_definitions['insert_contacts_output']
        end

      },
}
```

## Step 1 - Action title, subtitle, description, and help

The first step to making a good action is to properly communicate what the actions does, how it does it and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#title)

## Step 2 - Define input fields

This component tells Workato what fields to show to a user trying to execute the insert batch action. In the case of inserting a batch of contacts in Intercom for example, the user has to provide us with an array (list) of contacts.

```ruby
  input_fields: lambda do
    [
      {
        name: "contacts",
        type: "array",
        of: "object",
        properties: [
          {
            control_type: "text",
            label: "Role",
            type: "string",
            name: "role"
          },
          {
            control_type: "text",
            label: "External ID",
            type: "string",
            name: "external_id"
          },
          {
            control_type: "text",
            label: "Email",
            type: "string",
            name: "email"
          },
          {
            control_type: "text",
            label: "Phone",
            type: "string",
            name: "phone"
          },
          {
            control_type: "text",
            label: "Name",
            type: "string",
            name: "name"
          }
        ]
      }
    ]
  end,
```

## Step 3 - Defining the execute lambda

The execute lambda is responsible for

1. Preparing the series of requests to send in parallel to the API
2. The actual sending of the request
3. Any post-processing of the data.

### 1\. Preparing the series of requests to send in parallel to the API

In the first part of the execute lambda, we first create an array of requests with a single request for each contact. Take note that the requests are not actually sent out at this point but only when the array of requests is passed to the `parallel` method.

```ruby
  # Pre-processing of the data.
  # For multithreading, we need to create an array of requests which we do over here.
  number_of_batches = input['contacts'].size
  batches = input['contacts'].map do |contact|
    post("contacts", contact)
  end
```

### 2\. Sending of the request

In the next step we call the parallel method which takes in the array of requests as well as parameters for the execution like the total number of threads and any throttling of requests required. Take note that `rpm` is optional and excluding it will result in no throttling of requests.

```ruby
results = parallel(
    batches, # Each index in the batch array represents a single request
    threads: 20, # The max number of threads. Defaults to 1 and max is 20
    rpm: 100, # How many requests to send per minute
    )
```

### 3\. Post-processing of the data

The output of the parallel method is an array which describes the successful and failed requests in the batch. This is done in the second and third index of the array which correspond to successful responses and failed responses for requests respectively. Take note that `null` values in either array indicate a value in the same position in its counterpart.

**Sample output of the parallel method**

```ruby
[
  false, # Boolean that indicates all requests were successful
  [
    null, # null indicates that this request was unsuccesful
    { ... }, # The response from a successful API call
    # ...
  ],
  [
    "409 Conflict", # the error message from a failed request
    null, # null indicates the request was successful
    # ...
  ],
]
```

Lastly, we need to do some transformations to ensure that the output of this action contains both the successfully ingested records and the failed records so the user can retry these failed records or store this somewhere.

```ruby
  # Post-processing
  # Boolean to tell the user that all records were successful
  success = results[0]
  # An array of all the responses for successful records
  records_ingested = results[1].compact
  # Collecting all the failed records into an array
  records_failed = []
  results[2].each_with_index do |item, index|
    next unless item
    failed_record = {
      code: item,
      record: input['contacts'][index]
    }
    records_failed << failed_record
  end

  {
    success: success,
    records_ingested: records_ingested,
    records_failed: records_failed
  }
```

## Step 4 - Defining output fields

This section tells us what datapills to show as the output of the trigger. The `name` attributes of each datapill should match the keys in the output of the `execute` key.

```ruby
output_fields: lambda do |object_definitions, config_fields|
  object_definitions['insert_contacts_output']
end
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/custom-action.md
description: >-
  Enable custom actions in a connector to give users a catch-all that inherits
  your authorization and token refresh logic.
---

# How-to guides - Enabling custom actions

In this segment, we will be going through the enabling of custom actions effectively. Custom actions are a great way to implement a "Catch All" for users of your connector. Take note that all requests sent from your custom action will inherit your authorization details like tokens as well as authorization logic for token refresh.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) quota.
> 
> You can use the [checkpoint!](/en/developing-connectors/sdk/sdk-reference/ruby_methods#checkpoint) method with file streaming actions to transfer files that exceed the timeout limit. The `checkpoint!` method checks the duration of an action's execution. If it exceeds 120 seconds, Workato refreshes the timeout with a slight delay to ensure fair processing.

## Sample connector code

```ruby
{
  title: 'Acme',
  connection: {
    fields: [
      {
        name: 'client_id',
        control_type: 'text',
        label: 'OAuth App Client ID',
        optional: 'false'
      },
      {
        name: 'client_secret',
        control_type: 'password',
        label: 'OAuth App Client secret',
        optional: 'false'
      },
      {
        name: 'advanced_settings',
        type: 'object',
        properties: [
          {
            name: 'oauth_scopes',
            control_type: 'multiselect',
            delimiter: ' ',
            hint: 'By default, only scopes for Reading and writing contacts are requested',
            options: [
              [ 'Read contacts', 'contacts.read' ],
              [ 'Write contacts', 'contacts.write' ],
              [ 'Read Invoices', 'invoices.read' ],
              [ 'Write Invoices', 'invoices.read' ],
            ]
          }
        ]
      }
    ],

    authorization: {
      type: 'oauth2',

      client_id: lambda do |connection|
        connection['client_id']
      end,

      client_secret: lambda do |connection|
        connection['client_secret']
      end,

      authorization_url: lambda do |connection|
        scopes = connection.dig('advanced_settings', 'oauth_scopes') || ['contacts.read', 'contacts.write'].join(" ")
        "https://api.acme.com/oauth/authorize?scopes=#{scopes}"
      end,

      token_url: lambda do |connection|
        "https://api.acme.com/oauth/token"
      end,

      apply: lambda { |connection, access_token|
        headers(Authorization: "Bearer #{access_token}")
      }
    },

    base_uri: lambda do |connection|
        "https://api.acme.com/"
    end
  },

  custom_action: true,

  custom_action_help: {
    learn_more_url: 'https://www.acme.com/api/reference',

    learn_more_text: 'Acme API documentation',

    body: 'Build your own Acme action with a HTTP request. The request will be authorized with your current connection.'
  }
}
```

## Step 1 - Configuring the connection

Since the authorization credentials dictate the scope and permission of the connection, it is important to consider what custom actions may be used for - some endpoints require different scopes and permissions. This may include additional scopes and permissions that are not necessary for default actions.

In the example above, we have included a simple example for OAuth2 where users may add additional OAuth scopes as needed for their custom actions in the future.

![OAuth connection with scopes](/assets/custom_action_connection.Sy7kNoIf.png)

## Step 2 - Define the custom action

```ruby
  custom_action: true,

  custom_action_help: {
    learn_more_url: 'https://www.acme.com/api/reference',

    learn_more_text: 'Acme API documentation',

    body: 'Build your own Acme action with a HTTP request. The request will be authorized with your current connection.'
  }
```

This component tells Workato that you want custom actions enabled for your connector as well as allows you to add additional guidance to users. In particular, you should add relevant help links to API documentation to make it easier for users to find a reference when configuring their custom actions.

### Security considerations

Because custom actions can allow inputs to the URL path, you must consider how custom actions will be used by users in your organization. Path traversal attacks are possible if you allow user provided inputs such as datapills in your path.

Refer to the [PortSwigger path traversal guide](https://portswigger.net/web-security/file-path-traversal) for more information on path traversal attacks.

Enhance your security posture by using the following mitigation strategies:

1. Within your organization, enforce that user-defined inputs (such as datapills representing data written by users) should not be supplied to URL path inputs or any other inputs that represent a path to a file
2. Inquire with your API vendor regarding their inputs about path traversal attacks. Understand how they mitigate such attacks and enforce further validations as needed in your recipes before allowing user inputs to be placed in sensitive fields.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/wait-for-resume-actions.md
description: >-
  Configure Wait for resume actions in the connector SDK to suspend a job, await
  an external request, and resume with a payload.
---

# Wait for resume actions

This article describes how to configure Wait for resume actions. This feature allows you to build actions capable of executing the following tasks:

- Send an API request to an external system to start a long-running process. For example, you can start a batch processing job or send a document for approval.
- Suspend the job in Workato after the request is sent.
- Wait for the external system to send an authenticated request back to Workato with a payload.
- Resume the job with the payload to continue downstream recipe steps.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.

## Example use cases

You can use Wait for resume actions to achieve the following use cases:

- Simulate a chat flow within a single recipe. This is similar to Workbot's "Wait for user input/action" feature.
- Wait for document approvals in an external system. When approved, the recipe continues immediately.
- Build process flows for records in an external system. For example, you can build a workflow that gathers leads from Marketo, and only proceeds when data collection is complete.

## Prerequisites

If you plan to use this action to send a request to an external system, the external system you choose must be able to send an authenticated request back to Workato's developer APIs.

Additionally, the external system must be able to store a resume token, which is sent alongside the authenticated request to Workato's developer APIs. This token indicates which job Workato should resume.

## How to implement Wait for resume actions

Two crucial components facilitate the functionality of Wait for resume actions:

- [SDK code](#sdk-code): Use SDK code within actions to suspend and resume recipe workflows.
- [API requests](#api-requests): Send API requests from third-party applications to Workato's developer APIs to resume jobs.

### SDK code

On the SDK level, there are new callbacks in actions that enable you to suspend and resume calls. Learn how it works in this [sample custom connector](https://app.workato.com/custom_adapters/497423/details?token=a0fc7274b82f4a75fc5f6867608cff1850fd32b29f99ea051df3677c5176f450).

Sample custom connector code

```ruby
{
  actions: {
    wait_for_webhook: {
      config_fields: [
        {
          name: 'url',
          label: 'API endpoint',
          hint: 'We will send a POST request to this endpoint with the resume token',
          optional: false
        },
        {
          name: 'payload_schema',
          optional: true,
          sticky: true,
          schema_neutral: true,
          control_type: 'schema-designer',
          sample_data_type: 'json_input',
        }
      ],
      execute: lambda do |_connection, input, _input_schema, _output_schema, continue|
        if continue.blank?
          # Calling suspend will put the job to sleep, after the request in the proc is executed.
          # in this case we send a POST request to the URL provided by the recipe builder
          # expires_at is configurable and once the time is reached, the job is resumed
          suspend(continue: { "state" => "suspended", "url" => input['url']}, expires_at: 10.minutes.from_now)
        elsif continue["state"] == "resumed"
          { "result" => "resumed", "payload" =>  continue["payload"]}
        elsif continue["state"] == "suspend_timeout"
          { "result" => "suspend_timeout" }
        else
          { "result" => "Unexpected state" }
        end
      end,
      # When suspend is called, this lambda is executed to suspend the job
      # The lambda receives 3 arguments
      # The resume token is an opaque token that must be stored in the external system. This will be used to identify the job to resume
      # expires_at is the time when the job resumes with a timeout
      # continue is the argument passed
      before_suspend: lambda do |resume_token, expires_at, continue|
        response = post(continue['url'], { expires_at: expires_at, resume_token: resume_token } )
      end,
      # Allows you to manipulate or add data before the resume.
      # We change the state of the "continue" argument
      # We also add the payload data into the "continue" argument
      # After this lambda is called, the "execute" lambda is called with the "continue" argument
      before_resume: lambda do |data, input, continue|
        if continue["state"] == "suspended"
          continue["state"] = "resumed"
          continue["payload"] = data
        else
          { "result" => "Unexpected state" }
        end
      end,
      # Allows you to manipulate or add data before the resume due to a timeout
      # We change the state of the "continue" argument
      # After this lambda is called, the "execute" lambda is called with the "continue" argument
      before_timeout_resume: lambda do |input, continue|
        if continue["state"] == "suspended"
          continue["state"] = "suspend_timeout"
        else
          { "result" => "Unexpected state" }
        end
      end,
      output_fields: lambda do |object_definition|
        object_definition['output']
      end
    }
  }
}
```

This guide does not elaborate on the details of the standard attributes of the action. Refer to our [SDK actions reference](/en/developing-connectors/sdk/sdk-reference/actions) documentation to learn about the basic structure of actions.

There are four lambdas in the action hash that are foundational for Wait for resume actions:

#### `execute`

This lambda operates similarly to standard [Multistep actions](/en/developing-connectors/sdk/guides/building-actions/multistep-actions). Its primary purpose is to preprocess data from user input and determine the final output of the action when it resumes. This is facilitated by the `continue` argument, which is `nil` the first time the action is invoked. The `continue` argument also contains the output of either the `before_resume` or `before_timeout_resume` lambdas when resumed.

For the Wait for resume action to function properly, the execute lambda must invoke the `suspend` method, which initiates the suspension of the job.

Refer to our [suspend method reference](/en/developing-connectors/sdk/sdk-reference/ruby_methods#suspend) documentation for more information.

#### `before_suspend`

This lambda is specific to Wait for resume actions and is invoked when the suspend method is called. It primarily registers the resume token with the external application, guiding it on how to resume this specific job.

View our [key reference](/en/developing-connectors/sdk/sdk-reference/actions#before-suspend) documentation for more information.

#### `before_resume`

This lambda is specific to Wait for resume actions and is invoked when Workato receives an API request to resume the job. Its primary purpose is to offer you a hook to manipulate data if necessary and manage the state of the `continue` argument before transferring execution to the `execute` lambda.

View our [key reference](/en/developing-connectors/sdk/sdk-reference/actions#before-resume) documentation for more information.

#### `before_timeout_resume`

This lambda is specific to Wait for resume actions and is invoked when the `expires_at` time passes before Workato receives an API request to resume the job. Its primary purpose is to offer you a hook to manipulate data if necessary and manage the state of the `continue` argument before transferring execution to the `execute` lambda.

View our [key reference](/en/developing-connectors/sdk/sdk-reference/actions#before-timeout-resume) documentation for more information.

### API requests

To resume the job from the external system, the external system must be capable of dispatching an authenticated API request to Workato's [developer API](/en/workato-api).

#### Resume job

The Resume job endpoint resumes a suspended job based on the `resume_token` you provide. The endpoint returns `204` responses with no content.

View our [Resume job](/en/workato-api/jobs#job-resume) API documentation to learn how to use this endpoint.

## Limitations

- API requests in the `execute` lambda must be called with `.presence`. Because API requests are lazy-loaded in the `execute` lambda, any request defined before the `suspend` method must be forced to execute using `.presence` chained after the request.
  
- Maximum time to suspend: The maximum time you can suspend a job is 60 days.
  
- Rate limits: The developer API has a rate limit of 100 requests each minute for this action.
  
- Resume payload maximum size: The maximum payload size is 50MB.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-triggers.md
description: >-
  Learn how to build triggers in the Workato connector SDK, including polling,
  static webhook, dynamic webhook, and hybrid triggers.
---

# Building triggers

Triggers are a crucial part of any connector. They allow users of your connector to trigger recipes in Workato based on events in your target application. There are multiple types of related triggers available in Workato:

- Polling triggers
- Static webhook triggers
- Dynamic webhook triggers
- Hybrid triggers (Webhooks + polling)

> **TIP**
> 
> Before we start, it is also important to get familiar with the different types of [HTTP request methods](/en/developing-connectors/sdk/sdk-reference/http) which power all triggers.

### General structure of triggers

You can find a full reference of the `triggers` key in our [SDK reference.](/en/developing-connectors/sdk/sdk-reference/triggers)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-triggers/poll.md
description: >-
  Build a polling trigger in the connector SDK that queries an API at fixed
  intervals for new records using a cursor.
---

# How-to guides - Polling Trigger

A poll trigger constantly executes a poll key for new events at fixed time intervals. This time interval defaults to every 5 minutes but can be changed by users when configuring the trigger in a recipe. Polling triggers function by executing a HTTP request every interval to query an API for new records or events since the last time it polled. This is possible via cursors embedded in the trigger logic.

## Sample connector - Freshdesk

```ruby
{
  title: 'My Freshdesk connector',

  # More connector code here
  triggers: {
    updated_ticket: {
      title: 'New/updated ticket',

      subtitle: "Triggers when a ticket is created or " \
      "updated in Freshdesk",

      description: lambda do |input, picklist_label|
        "New/updated <span class='provider'>ticket</span> " \
        "in <span class='provider'>Freshdesk</span>"
      end,

      help: "Creates a job when tickets are created or " \
      "updated in Freshdesk. Each ticket creates a separate job.",

      input_fields: lambda do |object_definitions|
        [
          {
            name: 'since',
            label: 'When first started, this recipe should pick up events from',
            type: 'timestamp',
            optional: true,
            sticky: true,
            hint: 'When you start recipe for the first time, it picks up ' \
            'trigger events from this specified date and time. Defaults to ' \
            'the current time.'
          }
        ]
      end,

      poll: lambda do |connection, input, closure, _eis, _eos|

        closure = {} unless closure.present?

        page_size = 100

        updated_since = (closure['cursor'] || input['since'] || Time.now ).to_time.utc.iso8601

        tickets = get("https://#{connection['helpdesk']}.freshdesk.com/api/v2/tickets.json").
                  params(order_by: 'updated_at',
                         order_type: 'asc',
                         per_page: page_size,
                         updated_since: updated_since)

        closure['cursor'] = tickets.last['updated_at'] unless tickets.blank?

        {
          events: tickets,
          next_poll: closure,
          can_poll_more: tickets.length >= page_size
        }
      end,

      dedup: lambda do |record|
        "#{record['id']}@#{record['updated_at']}"
      end,

      output_fields: lambda do |object_definitions|
        [
          {
            name: 'id',
            type: 'integer'
          },
          {
            name: 'email'
          },
          {
            name: 'subject'
          },
          {
            name: 'description'
          },
          {
            name: 'created_at'
          },
          {
            name: 'updated_at'
          }
        ]
      end,

      sample_output: lambda do |connection, input|
        {
          "id": 1234,
          "email": "John@acmestudios.com",
          "subject": "Account provisioning",
          "description": "I need access to my account"
        }
      end
    }
  }
  # More connector code here
}
```

## Step 1 - Trigger title, subtitle, description, and help

The first step to making a good trigger is to properly communicate what the trigger does and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#title)

## Step 2 - Define input fields

This component tells Workato what fields to show to a user configuring this trigger. In this case, we want a simple input field that allows a user to pick a timestamp value. This will be used in our trigger code later on to pull tickets created/updated before the recipe was started. This is a great tool to provide to users of your connector for retrospective syncs of data.

```ruby
  input_fields: lambda do |object_definitions|
    [
      {
        name: 'since',
        label: 'When first started, this recipe should pick up events from',
        type: 'timestamp',
        optional: true,
        sticky: true,
        hint: 'When you start recipe for the first time, it picks up ' \
        'trigger events from this specified date and time. Defaults to ' \
        'the current time.'
      }
    ]
  end
```

![New/updated ticket input fields](/assets/new_ticket_input.Cj3w4dQ5.png)_New/updated ticket input fields_

Various other key value pairs exist for input/output fields other than the ones defined above. Refer to [Input fields](/en/developing-connectors/sdk/sdk-reference/triggers#input-fields) for more information.

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 3 - Defining the poll key

The poll key tells Workato what to do every time interval. At every time interval, this `poll` lambda function will be invoked and expect to receive any applicable new/updated tickets.

```ruby
    poll: lambda do |connection, input, closure, _eis, _eos|

      closure = {} unless closure.present? # initialize the closure hash when recipe is first started.

      page_size = 100

      updated_since = (closure['cursor'] || input['since'] || Time.now ).to_time.utc.iso8601

      tickets = get("/tickets.json").
                params(order_by: 'updated_at',
                       order_type: 'asc',
                       per_page: page_size,
                       updated_since: updated_since)

      closure['cursor'] = tickets.last['updated_at'] unless tickets.blank?

      {
        events: tickets,
        next_poll: closure,
        can_poll_more: tickets.length >= page_size
      }
    end,
```

In the example above, we receive 3 arguments:

1. `connection` - Corresponds to the values given by the user when making the connection to Freshworks
2. `input` - Corresponds to the inputs of this trigger. In this case, it's a single input: `since`
3. `closure` - Corresponds to a hash that was passed from the previous poll. `nil` when the recipe is first started

Inside the `poll` lambda function, we go on to initialize the `closure` argument as an object before initializing a new variable `updated_since` as well. This `updated_since` variable is either assigned to `closure['cursor']` if it is present (indicating a cursor passed from a previous poll) or the `input['since']` indicating this is the first poll when a recipe was first started.

In the following lines, we send a GET request to the `/tickets.json` endpoint with query parameters to retrieve the relevant tickets. `closure['cursor']` is updated to the timestamp of the last ticket's `updated_at` attribute if there were any tickets.

The expected output of the `poll` lambda function is a object that should have 3 keys:

- `events` - The array of events, or data, should be passed into the events key. Each index in the array will be processed as a separate job.
- `next_poll` - This becomes the closure argument in the next poll of the trigger.
- `can_poll_more` - This tells the trigger to poll again immediately or poll during the next interval. This is used when there are 100 tickets returned from Freshdesk, indicating there might be more tickets that have been created/updated in the time since the previous poll.

To know more about the poll key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#poll)

## Step 4 - Defining output fields and dedup

This section tells us what datapills to show as the output of the trigger as well as how to prevent duplicate records to create duplicate jobs. To prevent a job from being repeated (this might happen due to a bug on the API end), use the `dedup` key which tells your connector how to create a unique signature for each record. This signature is stored for each recipe and if a record with the same signature is found, no job will be created.

For datapills, use the `output_fields` key. The `name` attributes of each datapill should match the keys of a single ticket record.

```ruby
    dedup: |record|
      "#{record['id']}@#{record['updated_at']}"
    end,

    output_fields: lambda do |object_definitions|
      [
        {
          name: 'id',
          type: 'integer'
        },
        {
          name: 'email'
        },
        {
          name: 'subject'
        },
        {
          name: 'description'
        }
      ]
    end
```

![New/updated ticket output fields](/assets/ticket_output.B1ihfv14.png)_New/updated ticket output fields_

```ruby
  # Entire tickets array assigned to the events key
  [
    {
      "id": 1234,
      "email": "John@acmestudios.com",
      "subject": "Account provisioning",
      "description": "I need access to my account"
    },
    {
      "id": 4321,
      "email": "sally@acmestudios.com",
      "subject": "Account deprovisioning",
      "description": "I want to cancel my account"
    },
    ...
  ]
```

To know more about the output fields key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#output-fields)

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 5 - Defining sample output

A optional supplementary component to a connector, the sample output key nonetheless greatly improves a user's experience by giving him/her some context to what the datapill's value could be. This allows users to build recipes more quickly.

```ruby
    sample_output: lambda do |connection, input|
      {
        "id": 1234,
        "email": "John@acmestudios.com",
        "subject": "Account provisioning",
        "description": "I need access to my account"
      }
    end
```

To know more about the sample output key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#sample-output)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-triggers/static-webhook.md
description: >-
  Build a static webhook trigger in the connector SDK that users register
  manually with a provided webhook URL.
---

# How-to guides - Static Webhook Trigger

A static webhook trigger is one that requires manual registration. This usually involves a user creating a webhook subscription in the application's UI with a provided webhook URL.

> **WARNING**
> 
> When you define a static webhook trigger for your connector, take note that you will not be able to define a dynamic webhook trigger. Only one type of webhook trigger is allowed in a single connector. You may have both a polling trigger and one type of webhook trigger in your connector.

## Sample connector - Greenhouse

```ruby
{
  title: 'My Greenhouse connector',

  # More connector code here
  webhook_keys: lambda do |params, headers, payload|
    "#{params['org_id']}@#{payload['action']}"
  end,

  triggers: {
    new_event: {
      title: 'New Candidate Event',

      subtitle: "Triggers when a Candidate event is received " \
      "from Greenhouse",

      description: lambda do |input, picklist_label|
        "New <span class='provider'>candidate event</span> " \
        "in <span class='provider'>Greenhouse</span>"
      end,

      help: lambda do |input, picklist_label, connection, webhook_base_url|
        next unless webhook_base_url.present?
        <<~HTML
        Creates an job when an event is received from Greenhouse. To set this webhook up,
        you will need to register the webhook below in Greenhouse under "settings" => "webhooks" => "new". <br>
        <b>Webhook endpoint URL</b>
        <b class="tips__highlight">#{webhook_base_url}?org_id=#{connection['org_id']}</b>
        HTML
      end,

      input_fields: lambda do |object_definitions|
        [
          {
            name: 'event_type',
            label: 'Event',
            control_type: 'select',
            pick_list: 'events',
            optional: false,
            hint: 'Select specific event.'
          }
        ]
      end,

      webhook_key: lambda do |connection, input|
        "#{connection['org_id']}@#{input['event_type']}"
      end,

      webhook_notification: lambda do |input, payload, extended_input_schema, extended_output_schema, headers, params|
        payload.dig('payload', 'candidate')
      end,

      dedup: lambda do |record|
        record['id']
      end,

      output_fields: lambda do |object_definitions|
        [
          {
            name: 'id'
          },
          {
            name: 'rejected_at'
          },
          {
            name: 'prospect'
          },
          {
            name: 'prospect_detail',
            type: 'object',
            properties: [
              {
                name: 'prospect_pool',
                type: 'object',
                properties: [
                  {
                    name: 'id',
                    type: 'integer',
                    control_type: 'integer'
                  },
                  {
                    name: 'name'
                  }
                ]
              },
            ]
          }
         ]
        end,

        sample_output: lambda do |connection, input|
          if input['event_type'] == "candidate_stage_change"
            get("v1/applications?per_page=1")&.dig(0) || {}
          else
            get("v1/#{input['object']&.pluralize}?per_page=1")&.dig(0) || {}
          end
        end
    }
  },

  pick_lists: {
    events: lambda do |connection|
      [
        ["Candidate Updated", "update_candidate"],
        ["Candidate Stage Changed", "candidate_stage_change"]
      ]
    end
  }
  # More connector code here
}
```

## Steps:

## Step 1 - Set up the webhook\_keys attribute and retrieve your connector static webhook URL

`webhook_keys` is a top level key (connector-wide definition). This lambda function is called for each webhook your connector receives via its assigned webhook URL and allows you to define a routing key for each incoming webhook. For example:

- With this definition

```ruby
    webhook_keys: lambda do |params, headers, payload|
      "#{params['org_id']}@#{payload['action']}"
    end,
```

- and an incoming webhook with the following shortened body from Greenhouse

```ruby
URL: https://www.workato.com/user/123/connector/abc?org_id=555
{
  "action": "candidate_stage_change",
  "payload": {
    "application": {
      "id": 265277,
      "rejected_at": null,
      "prospect": false,
      "status": "active",
      "applied_at": "2013-03-22T00:00:00Z",
      "last_activity_at": "2015-02-09T16:38:36Z",
      "url": "https://app.greenhouse.io/people/265772?application_id=265277",
      "source": {
        "id": 31,
        "name": "Agency"
      },
  # More information here
}
```

The resultant webhook\_keys output for this webhook payload should be `555@candidate_stage_change`. This key is used to route these events to the proper triggers as you may have multiple static webhook triggers.

To retrieve your connector's static webhook URL, head to the **Test code** tab under **Connector SDK > Source code**. You will find the static webhook URL in an expandable section labeled **Static webhook URI**.

![Static webhook URL](/assets/static_webhook_url.B8S2rZCc.png)_Static webhook URL in **Test code** environment_

## Step 2 - Trigger title, subtitle and description

The first step to making a good trigger is to properly communicate what the trigger does and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#title)

## Step 3 - Define your help with your static webhook url

Another important part of building a static webhook trigger is displaying the webhook url prominently so users can take this and register it. To do this, you can utilize the `help` lambda that allows you to display your connector's static webhook url. Additionally, you may add query parameters in the displayed webhook URL which can be utilized in conjunction with `webhook_key` and `webhook_keys` to route events to specific recipes.

```ruby
      help: lambda do |input, picklist_label, connection, webhook_base_url|
        next unless webhook_base_url.present?
        <<~HTML
        Creates an job when an event is received from Greenhouse. To set this webhook up,
        you will need to register the webhook below in Greenhouse under "settings" => "webhooks" => "new". <br>
        <b>Webhook endpoint URL</b>
        <b class="tips__highlight">#{webhook_base_url}?org_id=#{connection['org_id']}</b>
        HTML
      end,
```

In our case, we have used an input gained from the connection called `org_id` which represents the specific Greenhouse organization for the connection used in this recipe. This will be important to route this webhook to the correct recipes when there are multiple connections.

To know more about the `help`, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#help).

## Step 4 - Define input fields

This component tells Workato what fields to show to a user configuring this trigger. In this case, we want a simple input field that allows a user to pick the type of Candidate event. This will be used in our trigger code later on create the trigger's personal webhook key.

```ruby
    input_fields: lambda do |object_definitions|
      [
        {
          name: 'event_type',
          label: 'Event',
          control_type: 'select',
          pick_list: 'events',
          optional: false,
          hint: 'Select specific event.'
        }
      ]
    end,
```

![New event input fields](/assets/new_event_input.CQRxjKuE.png)_New event input fields_

Various other key value pairs exist for input/output fields other than the ones defined above. Refer to [Input fields](/en/developing-connectors/sdk/sdk-reference/triggers#input-fields) for more information.

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 5 - Defining the trigger webhook key

After defining the inputs from the end user, we can now move on to define the connector's `webhook_key` lambda function. This lambda function receives two arguments for the user's connection values as well as inputs from the `input_fields` of this trigger. This allows you to create a string that is a key that is specific to your webhook trigger.

With this `webhook_key` and `webhook_keys` in step 1, you now have 2 unique strings generated. When an incoming webhook is received to your connector's webhook URL, the resultant output string from the `webhook_keys` lambda function is matched against strings generated from `webhook_key` lambda functions within each trigger. If there is a match, the webhook is routed to this trigger (and all others that match).

```ruby
    webhook_key: lambda do |connection, input|
      "#{connection['org_id']}@#{input['event_type']}"
    end,
```

In our webhook example from step 1, you can see that the `webhook_keys` output string would be `555@candidate_stage_change`. If the output of `webhook_key` which utilizes the `connection['org_id']` and `input['event_type']` match, an event would be routed to this trigger.

## Step 6 - Defining how to handle the webhook

The `webhook_notification` lambda function describes what your connector should do with all webhooks routed to it. You have numerous arguments available which represent both the user's inputs to the trigger as well as the webhook itself. To send the payload of the webhook as a job, you can simply pass on the `payload` argument. You may also add on attributes from the `headers` if required. In the case of Greenhouse, we have stripped away some irrelevant details from the payload described in the [Greenhouse webhooks documentation](https://developers.greenhouse.io/webhooks.html#candidate-stage-change).

```ruby
    webhook_notification: lambda do |input, payload, extended_input_schema, extended_output_schema, headers, params|
      payload.dig('payload', 'application')
    end,
```

> **Webhook Validations**
> 
> - Workato performs validations on JSON based webhooks - denoted by the webhook's `Content-Type` header, to ensure that the payload is valid JSON. Otherwise, Workato responds with 400 bad request.
> - Incoming webhook payloads are expected to be UTF-8 compatible and Workato responds with 400 bad request if UTF-8 incompatible characters are found.

To know more about the `webhook_key` and `webhook_notification` key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#webhook-key)

## Step 7 - Defining output fields and dedup

This section tells us what datapills to show as the output of the trigger as well as how to prevent duplicate records to create duplicate jobs. To prevent a job from being repeated (this might happen when a webhook is sent twice), use the `dedup` key which tells your connector how to create a unique signature for each record. This signature is stored for each recipe and if a record with the same signature is found, no job will be created.

For datapills, use the `output_fields` key. The `name` attributes of each datapill should match the keys of a single webhook payload.

```ruby
    dedup: lambda do |record|
      record['id']
    end,

    output_fields: lambda do |object_definitions|
      [
        {
          name: 'id'
        },
        {
          name: 'rejected_at'
        },
        {
          name: 'prospect'
        },
        {
          name: 'prospect_detail',
          type: 'object',
          properties: [
            {
              name: 'prospect_pool',
              type: 'object',
              properties: [
                {
                  name: 'id',
                  type: 'integer',
                  control_type: 'integer'
                },
                {
                  name: 'name'
                }
              ]
            },
          ]
        }
       ]
    end,
```

![New event output fields](/assets/event_output.DvnJkNsb.png)_New event output fields_

```ruby
  # Sample output of the webhook_notification: lambda function
  {
    "id": "a1241",
    "rejected_at": "2020-01-12 10:57:03",
    "prospect": true,
    "prospect_detail": {
      "id": 12491,
      "name": "John Doe"
    }
  }
```

To know more about the output fields key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#output-fields)

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 8 - Defining sample output

A optional supplementary component to the trigger, the sample output key nonetheless greatly improves a user's experience by giving him/her some context to what the datapill's value could be. This allows users to build recipes more quickly.

```ruby
    sample_output: lambda do |connection, input|
      if input['event_type'] == "candidate_stage_change"
        get("v1/applications?per_page=1")&.dig(0) || {}
      else
        get("v1/#{input['object']&.pluralize}?per_page=1")&.dig(0) || {}
      end
    end
```

To know more about the sample output key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#sample-output)

## Step 9 - Secure your webhook events

Now that you're receiving webhooks, you can now consider adding [additional checks to verify the authenticity of incoming webhook events.](/en/developing-connectors/sdk/guides/building-triggers/securing-webhooks)

## Rate limits

This trigger is subject to our [webhook gateway's quotas.](/en/troubleshooting/webhook-gateway-limits)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-triggers/dynamic-webhook.md
description: >-
  Build a dynamic webhook trigger in the connector SDK that programmatically
  subscribes and unsubscribes webhooks in a target application.
---

# How-to guides - Dynamic Webhook Trigger

A dynamic webhook trigger is one that can programmatically be set up and torn down. This is something should be explicitly stated in the API of application that you are building a connector to. In the example below, you can define the process of setting up and tearing down webhooks in various blocks in the trigger object.

> **WARNING**
> 
> When you define a static webhook trigger for your connector, take note that you will not be able to define a dynamic webhook trigger. Only one type of webhook trigger is allowed in a single connector. You may have both a polling trigger and one type of webhook trigger in your connector.

## Sample connector - Cisco Webex

```ruby
{
  title: 'My Cisco Webex connector',

  # More connector code here
  triggers: {
    new_message: {
      title: 'New message',

      subtitle: "Triggers when a message event is " \
      "received from Cisco Webex",

      description: lambda do |input, picklist_label|
        "New <span class='provider'>message event</span> in " \
        "<span class='provider'>Cisco Webex</span>"
      end,

      help: "Triggers when webhook is sent from Cisco.",

      input_fields: lambda do |object_definitions|
        [
          {
            name: "id",
            label: "Room ID"
          }
        ]
      end,

      webhook_subscribe: lambda do |webhook_url, connection, input, recipe_id|
        post("https://api.ciscospark.com/v1/webhooks",
             name: "Workato recipe #{recipe_id}",
             targetUrl: webhook_url,
             resource: "messages",
             event: "created",
             filter: "roomId=#{input['id']}")
      end,

      webhook_notification: lambda do |input, payload, extended_input_schema, extended_output_schema, headers, params|
        payload["data"]
      end,

      webhook_unsubscribe: lambda do |webhook_subscribe_output, connection|
        delete("https://api.ciscospark.com/v1/webhooks/#{webhook_subscribe_output['id']}")
      end,

      dedup: lambda do |message|
        message["id"]
      end,

      output_fields: lambda do |object_definitions|
        [
          {
            name: "id"
          },
          {
            name: "roomId"
          },
          {
            name: "personId"
          },
          {
            name: "personEmail"
          },
          {
            name: "created"
          }
        ]
      end
    }
  },
  # More connector code here
}
```

## Step 1 - Trigger title, subtitle, description, and help

The first step to making a good trigger is to properly communicate what the trigger does and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#title)

## Step 2 - Define input fields

This component tells Workato what fields to show to a user configuring this trigger. In this case, we want a simple input field that allows a user to pick the type of Candidate event. This will be used in our trigger code later on create the trigger's personal webhook key.

```ruby
    input_fields: lambda do |object_definitions|
      [
        {
          name: "id",
          label: "Room ID"
        }
      ]
    end,
```

Various other key value pairs exist for input/output fields other than the ones defined above. Refer to [Input fields](/en/developing-connectors/sdk/sdk-reference/triggers#input-fields) for more information.

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 3 - Defining the trigger webhook subscription logic, webhook handling and teardown logic

When a recipe is started, a webhook subscription should be created. This webhook subscription should be given the "webhook url" specific to the recipe to receive and process as jobs. The `webhook_subscribe` lambda function is responsible for this and is executed whenever a recipe is started. To achieve this, the lambda function receives the following arguments:

1. `webhook_url` - The dynamically generated webhook URL specific to each recipe.
2. `connection` - Corresponds to the values given by the user when making the connection to Freshworks
3. `input` - Corresponds to the inputs of this trigger. In this case, its the single input - `id`.
4. `recipe_id` - Corresponds to the recipe id that uses this specific trigger. Useful for tracking webhook subscriptions.

Below we have the lambda function inside our `new_message` trigger that handles the subscription of our webhook\_url. Inside this block, we send a POST request to the Cisco spark API endpoint with the relevant details documented in the [Cisco Webex webhooks API](https://developer.webex.com/docs/api/v1/webhooks/create-a-webhook).

```ruby
    webhook_subscribe: lambda do |webhook_url, connection, input, recipe_id|
      post("https://api.ciscospark.com/v1/webhooks",
           name: "Workato recipe #{recipe_id}",
           targetUrl: webhook_url,
           resource: "messages",
           event: "created",
           filter: "roomId=#{input['id']}")
    end,
```

> **TIP**
> 
> If the HTTP request in the `webhook_subscribe` results in an error, this will be raised to the end user and prevent the recipe from being started.

The next step is to define the webhook handling in the `webhook_notifications` lambda function. You have numerous arguments available which represent both the user's inputs to the trigger as well as the webhook itself. To send the payload of the webhook as a job, you can simply pass on the `payload` argument. You may also add on attributes from the `headers` if required. In the case of Cisco, we have stripped away some irrelevant details from the payload described in the [Cisco Webex webhooks guide](https://developer.webex.com/docs/api/guides/webhooks#creating-a-webhook).

```ruby
    webhook_notification: lambda do |input, payload, extended_input_schema, extended_output_schema, headers, params|
      payload["data"]
    end,
```

> **Webhook Validations**
> 
> - Workato performs validations on JSON based webhooks - denoted by the webhook's `Content-Type` header, to ensure that the payload is valid JSON. Otherwise, Workato responds with 400 bad request.
> - Incoming webhook payloads are expected to be UTF-8 compatible and Workato responds with 400 bad request if UTF-8 incompatible characters are found.

The last part is to tear down this webhook subscription when the recipe is stopped. This is crucial for proper sanitization of webhooks in a target application. This is handled by the `webhook_unsubscribe` lambda function which is invoked when the recipe is stopped.. You have a single argument available which represents the output of the `webhook_subscribe` lambda function. In this case, it was the response from our initial request to the Cisco `/v1/webhooks` endpoint.

We can use this argument to discern the created subscription's `id` and send a matching `DELETE` request to the `v1/webhooks` endpoint to delete this webhook.

```ruby
    webhook_unsubscribe: lambda do |webhook_subscribe_output, connection|
      delete("https://api.ciscospark.com/v1/webhooks/#{webhook_subscribe_output['id']}")
    end,
```

To know more about the keys above, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#webhook-subscribe)

## Step 4 - Defining output fields and dedup

This section tells us what datapills to show as the output of the trigger as well as how to prevent duplicate records to create duplicate jobs. To prevent a job from being repeated (this might happen when a webhook is sent twice), use the `dedup` block which tells your connector how to create a unique signature for each record. This signature is stored for each recipe and if a record with the same signature is found, no job will be created.

For datapills, use the `output_fields` lambda function. The `name` attributes of each datapill should match the keys of a Hash that is the output of the `webhook_notifications` lambda function.

```ruby
    dedup: lambda do |message|
      message["id"]
    end,

    output_fields: lambda do |object_definitions|
      [
        {
          name: "id"
        },
        {
          name: "roomId"
        },
        {
          name: "personId"
        },
        {
          name: "personEmail"
        },
        {
          name: "created"
        }
      ]
    end
```

```ruby
  # Sample output of the webhook_notification: lambda function
  {
    "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
    "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
    "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
    "personEmail": "matt@example.com",
    "created": "2015-10-18T14:26:16.000Z"
  }
```

To know more about the output fields block, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/triggers#output-fields)

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 5 - \[OPTIONAL\] Configure how Workato responds to webhook events

If the webhook sender requires custom responses, you may configure additional attributes to do so. [Learn more](/en/developing-connectors/sdk/sdk-reference/triggers#webhook-response-body)

## Step 6 - Secure your webhook events

Now that you're receiving webhooks, you can now consider adding [additional checks to verify the authenticity of incoming webhook events.](/en/developing-connectors/sdk/guides/building-triggers/securing-webhooks)

## Rate limits

This trigger is subject to our [webhook gateway's quotas.](/en/troubleshooting/webhook-gateway-limits)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-triggers/hybrid-triggers.md
description: >-
  Build hybrid webhook plus polling triggers in the connector SDK to get
  real-time events while recovering any lost webhooks.
---

# How-to guides - Hybrid polling + webhook triggers

Webhooks open up a wide range of use cases that are time sensitive in nature, such as receiving the event when a customer makes a purchase. There are, however, scenarios where webhook events can be lost. This could be due to transient network errors that any HTTP requests can be susceptible to, or simply when the recipe is stopped for a short period of time and webhooks were sent during that period.

Hybrid polling + webhook triggers enable your triggers to function in real-time to produce jobs and pick up events even if the webhook is lost.

> **Before continuing**
> 
> The guide below builds on top of knowledge for both webhook and polling triggers. It is recommended that you read through the guides for those respective triggers first.

## Why implement Hybrid triggers

Hybrid triggers present numerous benefits over traditional webhook triggers through three key improvements:

1. Webhook events trigger a signal to Workato to pull new records from the target system. This lowers potential for spoofed webhooks from creating bad data and also ensures that potentially lost webhooks will still be retrieve when a new webhook is eventually received.
2. Allow your trigger output for each job to have all data needed, instead of a skinny payload that is often sent in the webhook.
3. Prevent job loss when a recipe is stopped for a period of time. When the recipe is started again, Workato executes a poll immediately to retrieve all records.

## Mechanics of Hybrid triggers

Hybrid trigger combine important lambdas from webhook triggers and polling triggers respectively. For static webhook hybrid triggers, you will need the `webhook_keys` and `webhook_key` lambdas, alongside the `poll` lambda. For dynamic webhook hybrid triggers, you will need the `webhook_subscribe` and `webhook_unsubscribe` lambdas, alongside the `poll` lambda.

When using hybrid triggers, the mechanics for pulling events change in 2 significant ways:

1. When a webhook event is received, the `poll` lambda is invoked to get new events based on the closure from the previous poll.
2. When a recipe is started/restarted, the `poll` lambda is invoked to get new events based on the closure from the previous poll.

> **TIP**
> 
> In the case of a burst of webhook events to a trigger, Workato's engine throttles polls intelligently to pull all records without having poll the API for each webhook event. This prevents rate limits from being hit from busy webhooks.
> 
> For example, when a burst of 100 webhook events are received over 1 minute, you can expect to receive 4-5 polls with the last poll being later than the time when the last webhook event was received.

Workato also executes the `poll` lambda every 12 hours to ensure that in case of webhook outages, records are still picked up with some delay.

## Sample connector - Chargebee

```ruby
{
  title: 'My Chargebee connector',

  webhook_keys: lambda do |params, headers, payload|
    # Chargebee events come in the form "subscription_changed", "subscription_renewed", "customer_changed" etc
    # Use .split to get the main object
    "#{payload['event_type']}".split("_").first
  end,

  # More connector code here
  triggers: {
    new_updated_subscription: {
      title: 'New/updated subscription',

      subtitle: "Triggers when a subscription is " \
      "created/updated in Chargebee",

      description: lambda do |input, picklist_label|
        "New/updated <span class='provider'>subscription</span> in " \
        "<span class='provider'>Chargebee</span>"
      end,

      help: lambda do |input, picklist_label, connection, webhook_base_url|
        next unless webhook_base_url.present?
        <<~HTML
        Creates a job immediately when a subscription is created/updated from Chargebee. To set this webhook up,
        you will need to register the webhook below in Chargebee under "settings" => "webhooks" => "new" and provide the events for subscription_changed and subscription_created. <br>
        <b>Webhook endpoint URL</b>
        <b class="tips__highlight">#{webhook_base_url}</b>
        HTML
      end,

      input_fields: lambda do
         [
           {
             name: 'since',
             type: :timestamp,
             optional: true
           }
         ]
      end,

      webhook_key: lambda do |connection, input|
        "subscription"
      end,

      poll: lambda do |connection, input, closure|
        page_size = 100
         closure = {} unless closure.present?
         closure['updated_since'] = (closure['updated_since'] || input['since'] || 1.hours.ago).to_time.utc.to_i

         params = {
            "sort_by[asc]": 'updated_at',
            limit: page_size,
            "updated_at[after]": closure['updated_since']
         }

         params['offset'] = closure['offset']

         response = get("/api/v2/subscriptions", params)

         if response['next_offset'].present?
           closure['offset'] = response['next_offset']
         else
           closure['offset'] = nil
           closure['updated_since'] = response['list'].last[input['object']]['updated_at'] unless response['list'].size == 0
         end

         {
           events: response['list'],
           next_poll: closure,
           can_poll_more: response['next_offset'].present?
         }
      end,

      dedup: lambda do |record|
        "#{record['subscription']['id']}@#{record['subscription']['updated_at']}"
      end,

      output_fields: lambda do |object_definitions|
        object_definitions['subscription']
      end
    }
  },
  # More connector code here
}
```

## Step 1 - Implement your chosen webhook trigger

Depending on what the app you are building the connector for, build the appropriate webhook trigger type. Dynamic webhooks are preferred as they minimize the amount of setup needed by the end user. In our example, Chargebee requires you to manually setup webhook subscriptions so we have used a static webhook trigger. Refer more to our guides on each of the types of webhooks to learn more.

For dynamic webhook triggers, you are expected to define the `webhook_subscribe` and `webhook_unsubscribe` lambda. For static webhook triggers, you are expected to define the `webhook_keys` and `webhook_key` lambda.

## Step 2 - Define the poll block

Instead of defining the `webhook_notification` lambda, building a hybrid trigger requires that you define the `poll` lambda instead. The `poll` lambda should function similar to any other polling trigger, whereby it needs an API endpoint to pull new records. [Refer to our polling trigger guides to understand more.](/en/developing-connectors/sdk/guides/building-triggers/poll)

```ruby
      poll: lambda do
        page_size = 100
         closure = {} unless closure.present?
         closure['updated_since'] = (closure['updated_since'] || input['since'] || 1.hours.ago).to_time.utc.to_i

         params = {
            "sort_by[asc]": 'updated_at',
            limit: page_size,
            "updated_at[after]": closure['updated_since']
         }

         params['offset'] = closure['offset']

         response = get("/api/v2/subscriptions", params)

         if response['next_offset'].present?
           closure['offset'] = response['next_offset']
         else
           closure['offset'] = nil
           closure['updated_since'] = response['list'].last[input['object']]['updated_at'] unless response['list'].size == 0
         end

         {
           events: response['list'],
           next_poll: closure,
           can_poll_more: response['next_offset'].present?
         }
      end,
```

In our example, we simply query Chargebee's subscription API to give us the subscriptions created/updated after the last time we polled.

## Step 4 - Defining output fields and dedup

When defining the output fields and dedup, take note that this should be based on the `poll` lambda's output and not the actual webhook payload. Essentially, the webhook payload is discarded in favor of the records received in the `poll` lambda.

```ruby
      dedup: lambda do |record|
        "#{record['subscription']['id']}@#{record['subscription']['updated_at']}"
      end,

      output_fields: lambda do |object_definitions|
        object_definitions['subscription']
      end
```

## Rate limits

This trigger is subject to our [webhook gateway's quotas.](/en/troubleshooting/webhook-gateway-limits)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-triggers/securing-webhooks.md
description: >-
  Secure connector SDK webhook triggers with signature verification to reject
  spoofed or tampered events, with a HubSpot example.
---

# How-to guides - Securing Webhook events

Webhook signature verification is a recommended practice that prevents malicious actors from spoofing events or allowing your connector to reject webhooks that were tampered with. There are many known signature verification methodologies which normally involve creating a signature from the webhook event and matching that against a signature in the webhook's headers. And this guide will show you one simple example of how to do so through [HubSpot's webhook V1 signature](https://developers.hubspot.com/docs/api/webhooks/validating-requests#validate-requests-using-the-v1-request-signature).

> **TIP**
> 
> This guide assumes you know the basics of creating static or dynamic webhook triggers. Please review those guides if you have not done so.

## Sample Connector - HubSpot Webhooks

```ruby
      webhook_payload_type: "raw", # Workato does a JSON.parse on incoming webhooks but we need to calculate the signature based on the raw payload

      webhook_notification: lambda do |input, payload, extended_input_schema, extended_output_schema, headers, params, connection, webhook_subscribe_output|
        original_payload = payload
        client_secret = connection['client_secret']
        if client_secret.present?
          source_string = client_secret + original_payload # Build the string to SHA256 which is a concatenation of client secret + payload
          v1_signature = source_string.encode_sha256.encode_hex
        end

        # If condition below verifies that the signature we calculated is the same as the X-Hubspot-Signature we got in the webhook event
        if (client_secret.present? && v1_signature == headers['X-Hubspot-Signature'])
          # Don't forget to parse the payload into JSON as we dictated that the payload would be `raw`
            {
              events: workato.parse_json(payload),
              headers: headers,
              webhook_validated: client_secret.present? ? true : false
            }
        end
      end,
```

[See the full connector in our community library](https://app.workato.com/custom_adapters/543633/details?community=true).

## Step 1 - Setting the webhook\_payload\_type to raw if needed

Workato's webhook gateway attempts to parse incoming payloads as JSON. In some cases, this may cause some of the payload's details to be lost which may result in a wrong signature being created. To avoid this, you can use the key `webhook_payload_type` to force Workato to provide the raw payload to the `webhook_notification` lambda.

## Step 2 - Computing the Webhook signature

Another important part of verifying the authenticity of a webhook is to compute your own webhook signature from the incoming webhook event. This is often done through an encryption algorithm such as SHA256 or HMAC algorithms using the payload and a secret that is only known by you and the webhook provider.

```ruby
  original_payload = payload
  client_secret = connection['client_secret']
  if client_secret.present?
    source_string = client_secret + original_payload # Build the string to SHA256 which is a concatenation of client secret + payload
    v1_signature = source_string.encode_sha256.encode_hex
  end
```

In the case of HubSpot, we create the key to be encrypted from the payload and the client secret before encrypting it with SHA256.

## Step 3 - Comparing the generated signature with the provided one in the webhook event

The next step would be to compare your generated signature in step 2 with the signature present in the webhook event. Normally, this would be contained in the header of the webhook event which you have access to in the `webhook_notification` lambda.

```ruby
        # If condition below verifies that the signature we calculated is the same as the X-Hubspot-Signature we got in the webhook event
        if (client_secret.present? && v1_signature == headers['X-Hubspot-Signature'])
          # Don't forget to parse the payload into JSON as we dictated that the payload would be `raw`
            {
              events: workato.parse_json(payload),
              headers: headers,
              webhook_validated: client_secret.present? ? true : false
            }
        end
```

---
