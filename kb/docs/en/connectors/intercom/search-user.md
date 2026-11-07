---
url: 'https://docs.workato.com/en/connectors/intercom/search-user.md'
description: >-
  The Search user action in the Intercom connector lets you find a specific user
  record by their email, user ID, or internal Intercom ID.
---

# Intercom - Search user action

The **Search user** action allows you to search for a specific user record using their unique email, user ID, or Intercom internal ID.

![Search segments by user action](/assets/search-user-action.Df7ctG_M.png)_Intercom - Search user action_

## Input

- User ID
  
- Enter the unique identifier or email of the user.
  
- Internal Intercom ID
  
- Provide the internal identifier that Intercom uses to track users.
  

## Output

<dl><dt>Type</dt><dd>The entity type for the data returned.</dd><dt>ID</dt><dd>The unique identifier for the user in Intercom.</dd><dt>User ID</dt><dd>The user's identifier within the application.</dd><dt>Anonymous</dt><dd>Indicates whether the user is anonymous.</dd><dt>Email</dt><dd>The user's email address.</dd><dt>Name</dt><dd>The user's full name.</dd><dt>Avatar</dt><dd><dl><dt>Type</dt><dd>The type of avatar image.</dd><dt>Image URL</dt><dd>The URL of the user's avatar image.</dd></dl></dd><dt>App ID</dt><dd>The identifier for the app associated with the user within Intercom.</dd><dt>Companies</dt><dd><dl><dt>Type</dt><dd>The type of related entities.</dd><dt>Companies</dt><dd><dl><dt>Type</dt><dd>The type of company data.</dd><dt>Company ID</dt><dd>The unique identifier for the company.</dd><dt>ID</dt><dd>The unique identifier used within Intercom for the company.</dd><dt>Company name</dt><dd>The name of the company.</dd><dt>List size</dt><dd>The number of companies associated with the user.</dd><dt>List index</dt><dd>The index of a company in the list of associated companies.</dd></dl></dd></dl></dd><dt>Location data</dt><dd><dl><dt>Type</dt><dd>The type of location data provided.</dd><dt>City name</dt><dd>The city associated with the user's location.</dd><dt>Continent code</dt><dd>The continent code for the user's location.</dd><dt>Country name</dt><dd>The country name for the user's location.</dd><dt>Latitude</dt><dd>The latitude coordinate for the user's location.</dd><dt>Longitude</dt><dd>The longitude coordinate for the user's location.</dd><dt>Postal code</dt><dd>The postal code for the user's location.</dd><dt>Region name</dt><dd>The region name for the user's location.</dd><dt>Timezone</dt><dd>The timezone for the user's location.</dd><dt>Country code</dt><dd>The country code for the user's location.</dd></dl></dd><dt>Phone</dt><dd>The user's phone number.</dd><dt>Pseudonym</dt><dd>The pseudonym used by the user, if applicable.</dd><dt>Remote created at</dt><dd>The timestamp of when the user was created remotely.</dd><dt>Session Count</dt><dd>The total number of sessions logged by the user.</dd><dt>Owner ID</dt><dd>The ID of the owner or responsible user for the contact in Intercom.</dd><dt>Last request at</dt><dd>The timestamp of the last request made by the user.</dd><dt>Created at</dt><dd>The timestamp of when the user was created in Intercom.</dd><dt>Signed up at</dt><dd>The timestamp of when the user signed up.</dd><dt>Updated at</dt><dd>The timestamp of when the user's information was last updated.</dd><dt>Unsubscribed from emails</dt><dd>Indicates whether the user has unsubscribed from emails.</dd><dt>Marked email as spam</dt><dd>Indicates whether the user has marked an email as spam.</dd><dt>Has hard bounced</dt><dd>Indicates whether an email sent to the user has hard bounced.</dd><dt>Do not track</dt><dd>Indicates whether the user has enabled do not track.</dd><dt>Referrer</dt><dd>The URL of the referrer through which the user was acquired, if applicable.</dd><dt>Last Seen IP</dt><dd>The last known IP address of the user.</dd><dt>User Agent Data</dt><dd>Details about the user's browser and operating system.</dd><dt>Utm campaign</dt><dd>The UTM campaign parameter associated with the user.</dd><dt>Utm content</dt><dd>The UTM content parameter associated with the user.</dd><dt>Utm medium</dt><dd>The UTM medium parameter associated with the user.</dd><dt>Utm source</dt><dd>The UTM source parameter associated with the user.</dd><dt>Utm term</dt><dd>The UTM term parameter associated with the user.</dd><dt>Social profiles</dt><dd><dl><dt>Type</dt><dd>The type of social profiles associated with the user.</dd><dt>Social profiles</dt><dd><dl><dt>ID</dt><dd>The unique identifier for the social profile.</dd><dt>Name</dt><dd>The name of the social network.</dd><dt>Type</dt><dd>The type of social profile.</dd><dt>URL</dt><dd>The URL of the social profile.</dd><dt>Username</dt><dd>The username of the user on the social network.</dd><dt>List size</dt><dd>The total number of social profiles associated with the user.</dd><dt>List index</dt><dd>The index of the social profile in the list.</dd></dl></dd></dl></dd></dl>

---
