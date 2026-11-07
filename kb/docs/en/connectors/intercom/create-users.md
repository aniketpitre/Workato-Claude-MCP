---
url: 'https://docs.workato.com/en/connectors/intercom/create-users.md'
description: >-
  The Create or update users action in the Intercom connector lets you create
  new users or update existing ones based on an email or user ID.
---

# Intercom - Create or update users action

The **Create or update users** action allows you to create new users or update existing users in Intercom based on an email or user ID that you search for. If a user is not found, the action creates a new user. Otherwise, it updates the user's details.

![Create users action](/assets/create-users-action.BnmC9K9h.png)_Intercom - Create or update users action_

## Input

- Parallel
  
- Specify the number of parallel requests to perform. Set a value between 1 and 10.
  
- Requests per minute
  
- Set the target request rate per minute. The rate is calculated on a 10-second interval basis. For detailed rate limits, refer to the [Intercom API rate limit documentation](https://developers.intercom.com/docs/references/introduction#rate-limiting). Setting this field to zero, or leaving it empty, removes rate limiting.
  
- Users
  
- Provide user details either directly or from a list.
  
  - Users source list
    
  - Input a list datapill if you are sourcing from a list input.
    
  - User ID
    
  - Enter the unique identifier for the user within Intercom.
    
  - Name
    
  - Input the user's full name.
    
  - Email
    
  - Provide the user's email address.
    
  - Unsubscribed from emails
    
  - Indicates whether the user has opted out of email communication.
    
  - Intercom ID of company
    
  - Enter the Intercom ID for the company associated with the user.
    
  - Company ID
    
  - Input the company's unique identifier.
    
  - Company name
    
  - Provide the company's name.
    
  - Company monthly spend
    
  - Enter the monthly spend associated with the company.
    
  - Custom attributes
    
  - Include any custom attributes for the user as necessary.
    

## Output

<dl><dt>Successful</dt><dd>Contains details of users successfully created or updated.</dd><dd><dl><dt>Type</dt><dd>The type of entity.</dd><dt>ID</dt><dd>The unique identifier for the user.</dd><dt>User ID</dt><dd>The identifier assigned to the user within Intercom.</dd><dt>Anonymous</dt><dd>Indicates if the user is anonymous.</dd><dt>Email</dt><dd>The email address of the user.</dd><dt>Name</dt><dd>The full name of the user.</dd><dt>Avatar</dt><dd>The avatar details of the user.</dd><dd><dl><dt>Type</dt><dd>The type of avatar.</dd><dt>Image URL</dt><dd>The URL link to the user's avatar image.</dd></dl></dd><dt>App ID</dt><dd>The identifier of the application within Intercom.</dd><dt>Companies</dt><dd>List of companies associated with the user.</dd><dd><dl><dt>Type</dt><dd>The type of associated entities.</dd><dt>Companies</dt><dd>The companies connected to the user.</dd><dd><dl><dt>Type</dt><dd>The type of company data.</dd><dt>Company ID</dt><dd>The unique identifier of the company.</dd><dt>ID</dt><dd>The unique identifier used within Intercom for the company.</dd><dt>Company name</dt><dd>The name of the company.</dd><dt>List size</dt><dd>The number of companies associated with the user.</dd><dt>List index</dt><dd>The index of the company in the associated list.</dd></dl></dd></dl></dd><dt>Location data</dt><dd>Contains geographic information about the user.</dd><dd><dl><dt>Type</dt><dd>The type of location data provided.</dd><dt>City name</dt><dd>The city associated with the user's location.</dd><dt>Continent code</dt><dd>The continent code for the user's location.</dd><dt>Country name</dt><dd>The country name for the user's location.</dd><dt>Latitude</dt><dd>The latitude coordinate for the user's location.</dd><dt>Longitude</dt><dd>The longitude coordinate for the user's location.</dd><dt>Postal code</dt><dd>The postal code for the user's location.</dd><dt>Region name</dt><dd>The region name for the user's location.</dd><dt>Timezone</dt><dd>The timezone for the user's location.</dd><dt>Country code</dt><dd>The country code for the user's location.</dd></dl></dd><dt>Phone</dt><dd>The phone number associated with the user.</dd><dt>Pseudonym</dt><dd>The pseudonym, if any, used by the user.</dd><dt>Remote created at</dt><dd>The timestamp of when the user was created remotely.</dd><dt>Session Count</dt><dd>The number of sessions the user has logged.</dd><dt>Owner ID</dt><dd>The identifier of the user who owns the account within Intercom.</dd><dt>Last request at</dt><dd>The timestamp of the last request made by the user.</dd><dt>Created at</dt><dd>The timestamp of when the user was created in Intercom.</dd><dt>Signed up at</dt><dd>The timestamp of when the user signed up.</dd><dt>Updated at</dt><dd>The timestamp of when the user's information was last updated.</dd><dt>Unsubscribed from emails</dt><dd>Indicates whether the user has unsubscribed from emails.</dd><dt>Marked email as spam</dt><dd>Indicates whether the user has marked an email as spam.</dd><dt>Has hard bounced</dt><dd>Indicates whether an email sent to the user has hard bounced.</dd><dt>Do not track</dt><dd>Indicates whether the user has enabled do not track.</dd><dt>Referrer</dt><dd>The referrer URL through which the user was acquired.</dd><dt>Last Seen IP</dt><dd>The last known IP address of the user.</dd><dt>User Agent Data</dt><dd>Information about the user's browser and operating system.</dd><dt>Utm campaign</dt><dd>The UTM campaign associated with the user.</dd><dt>Utm content</dt><dd>The UTM content parameter associated with the user.</dd><dt>Utm medium</dt><dd>The UTM medium parameter associated with the user.</dd><dt>Utm source</dt><dd>The UTM source parameter associated with the user.</dd><dt>Utm term</dt><dd>The UTM term parameter associated with the user.</dd><dt>Social profiles</dt><dd>Contains information about the social profiles linked to the user.</dd><dd><dl><dt>Type</dt><dd>The type of social profile information.</dd><dt>Social profiles</dt><dd>Detailed list of social profiles.</dd><dd><dl><dt>ID</dt><dd>The unique identifier for each social profile.</dd><dt>Name</dt><dd>The name of the social network.</dd><dt>Type</dt><dd>The type of the social network.</dd><dt>URL</dt><dd>The URL of the user's profile on the social network.</dd><dt>Username</dt><dd>The username of the user on the social network.</dd><dt>List size</dt><dd>The total number of social profiles associated with the user.</dd><dt>List index</dt><dd>The index of the social profile within the list.</dd></dl></dd></dl></dd><dt>Custom attributes</dt><dd>Custom data attributes associated with the user.</dd><dt>Tags list</dt><dd>A list of tags applied to the user.</dd><dt>Tags</dt><dd>Detailed information about the tags.<dl><dt>Sync</dt><dd>Indicates the synchronization status of the tags.</dd></dl></dd><dt>Segments list</dt><dd>A list of segments the user is part of.</dd><dt>Segments</dt><dd>Detailed information about the segments.<dl><dt>Active</dt><dd>Indicates if the segment is currently active.</dd><dt>New</dt><dd>Indicates if it is a new segment for the user.</dd><dt>Slipping Away</dt><dd>Indicates if the user is slipping away from the segment.</dd></dl></dd><dt>List size</dt><dd>The total number of records processed in the batch.</dd><dt>List index</dt><dd>The index of the current record in the batch.</dd></dl></dd><dt>Failed</dt><dd>Contains information about users that failed to create or update.<dl><dt>User</dt><dd>The user information for the failed action.<dl><dt>User ID</dt><dd>The unique identifier of the user within Intercom.</dd><dt>Email</dt><dd>The email address associated with the user.</dd></dl></dd><dt>Error</dt><dd>The error message associated with the failed action.</dd><dt>List size</dt><dd>The total number of failed records.</dd><dt>List index</dt><dd>The index of the current failed record within the list of all failed records.</dd></dl></dd><dt>All records in batch succeeded?</dt><dd>Indicates whether all records in the batch were successfully processed.</dd><dt>Number of records succeeded</dt><dd>The count of records that were successfully processed.</dd><dt>Number of records failed</dt><dd>The count of records that failed to process.</dd></dl>

---
