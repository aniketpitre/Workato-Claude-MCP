---
url: 'https://docs.workato.com/en/developing-connectors/sdk/guides/trigger-limit.md'
description: >-
  Reference for Workato SDK trigger quotas, including polling throttling,
  consecutive poll caps, and email notifications for throttled recipes.
---

# SDK trigger quotas

Workato enforces specific quotas on SDK triggers to optimize performance and ensure system stability. We apply quotas to the following trigger processing functions:

> **DEFAULT QUOTAS**
> 
> The quotas on this page are defaults based on Workato best practices and are configured to enable optimal platform performance. Customers on Enterprise plans or above can contact their Customer Success Representative to request an extension of these quotas for their specific use cases.

| Description | Quota |
| --- | --- |
| [Maximum consecutive polling without any jobs produced](/en/developing-connectors/sdk/guides/trigger-limit.html#consecutive-polls-in-a-single-poll-cycle-without-jobs) | 600 |
| [Maximum number of events in a single poll](/en/developing-connectors/sdk/guides/trigger-limit.html#number-of-events-per-poll) | 1,000 |

## Consecutive polls in a single poll cycle without jobs

Without a quota, triggers can poll consecutively to retrieve valid results. The `can_poll_more` boolean attribute in the SDK trigger poll response controls this behavior. Workato enforces a quota on consecutive polls in a single poll cycle when no jobs are produced.

### Throttling mechanism

Workato throttles a trigger if it polls consecutively without producing any jobs. Throttling minimizes unnecessary polling and ensures system stability. Triggers are limited to 600 consecutive polls in a single poll cycle without jobs before Workato pauses polling for 5 minutes. This threshold gradually decreases over time to 50 consecutive polls.

Workato pauses polling for 5 minutes when your trigger exceeds this quota. Polling resumes after the pause automatically and the counter continues from where it left off. Workato pauses polling again for another 5 minutes if the next poll also produces no jobs. The counter resets to zero if a poll produces jobs.

This pattern repeats until the poll cycle ends when `can_poll_more` equals false. Triggers can only poll once every 5 minutes without producing jobs after reaching the quota.

### Throttling notification

Workato sends email notifications automatically when a recipe is throttled. These notifications provide relevant details and keep you informed about throttled recipes.

#### Throttling notification recipients

Workato sends the following notifications about throttled recipes to specific recipients based on their role:

- **Workspace admins:** notifications are sent directly to the admin of the workspace where the recipe runs.
- **Embedded partners:** notifications are sent to the Embedded partner’s workspace email. Embedded customers do not receive these notifications.

#### Throttling notification details

Workato provides notifications at two key points to keep you informed about throttled recipes. Workato sends an email that contains details about the throttling event when a recipe is throttled for the first time. This ensures you are immediately aware of any issues affecting your recipes.

Additionally, at the end of each month, Workato sends a summary email that lists all recipes throttled during that month. This email provides a comprehensive overview of throttled recipes and serves as a reminder.

## Number of events in a single poll

Without a quota, a single poll can fetch an unbounded number of records, which can result in excessive platform load. Workato limits the number of events generated from a single poll to 1,000 in SDK connector triggers.

### What counts as a poll and an event?

A poll is one request made by the trigger to check for new data from the external system. It is a single invocation of the poll block in your SDK trigger.

An event is one record in the events array returned in the response from the poll. Workato converts each event into a job. Typically, one event creates one job.

### Use pagination in your trigger

If your external API returns more than 1,000 records, you must implement pagination in your poll logic to divide the results across multiple polls.

This is typically done by:

- Setting an appropriate page size. For example, `request_page_size = 100`
- Tracking an offset, timestamp, or token with the `next_poll` key
- Setting `can_poll_more: true` to poll again immediately instead of waiting the default 5-minute interval

For example:

```ruby
poll: lambda do |connection, input, closure, _eis, _eos|
  updated_since = (closure || input['since']).to_time.utc.iso8601
  request_page_size = 100

  response = get("/records/endpoint").params(
    updated_since: updated_since,
    page_size: request_page_size
  )

  next_updated_since = response['data'].last['updated_at'] unless response['data'].blank?

  {
    events: response['data'],                         # Array of jobs
    next_poll: next_updated_since,                   # Pass cursor for next poll
    can_poll_more: response['total_records'] >= request_page_size # Trigger next poll immediately
  }
end
```

If there are 10,000 records, this configuration fetches them across 100 polls. Each poll returns up to 100 records, which generate 100 events and 100 jobs. This approach meets the 1,000-event-per-poll quota.

### Limiting mechanism

Workato stops a recipe if the trigger fetches an excessive number of events in a single poll. This prevents system overload and ensures stability. Starting June 9th, 2025, triggers are limited to `1000` events in a single poll. The recipe is stopped if your trigger exceeds this quota.

### Stopped recipe notification

Workato sends email notifications automatically when a recipe is stopped. These notifications provide relevant details and keep you informed about affected recipes.

#### Notification recipients

Workato sends the following notifications about stopped recipes to specific recipients based on their role:

- **Workspace admins:** notifications are sent directly to the admin of the workspace where the recipe runs.
- **Embedded partners:** notifications are sent to the Embedded partner’s workspace email. Embedded customers do not receive these notifications.

#### Notification details

Workato provides notifications at two key points to keep you informed about stopped recipes due to the quota.

Workato sends an email that contains information about the recipe when a recipe is stopped for the first time. This ensures you are immediately aware of issues affecting your recipe.

Additionally, Workato sends a monthly summary email listing all affected recipes. This summary gives a complete view of impacted recipes and serves as a reminder.

### Frequently asked questions

#### Does the quota apply to total events over time?

No. The quota applies to each individual poll, not the total number of events processed across time.

#### What if my trigger needs to process 100,000 events?

You can process them across multiple polls. For example, use 100 polls with 1,000 events each.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/streaming.md
description: >-
  Learn how the Workato file streaming library lets custom connectors transfer
  gigabytes of data between a source and destination in chunks.
---

# How-to guides - File Streaming

Utilizing Workato's file streaming library, you'll be able to build connectors that can transfer gigabytes of data between a source and destination. This is done by downloading a smaller chunk of the larger file, uploading that to the destination and looping over this process multiple times.

![File streaming](/assets/streaming-illustration.CyLcPq6_.jpg)

Many of Workato's standard platform connectors to common file storage locations have streaming enabled such as S3, Google Cloud Storage and Azure Blob. [Find the full list here.](/en/features/file-streaming#file-streaming)

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.
> 
> You can use the `checkpoint!` method with file streaming actions to transfer files that exceed the timeout limit. Refer to the [Using our multistep framework to extend upload times](/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-chunk-id#using-our-multistep-framework-to-extend-upload-times) section for additional information.

## Prerequisites

- Downloading files The API should respect the [HTTP RFC for Range headers](https://datatracker.ietf.org/doc/html/rfc7233) which allows us to download a specific byte range of the file.
  
- Uploading the file The API should support ways to upload a file in multiple discrete chunks. This could be via [Content-Range headers](https://www.ietf.org/rfc/rfc2616.txt) or via any other form chunked uploads such as [Azure's multipart upload with block IDs.](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block)
  

## Guides

The guides below details out the various ways to build file streaming actions depending on the API's capabilities:

1. [Download file via file streaming (Range headers)](/en/developing-connectors/sdk/guides/building-actions/streaming/download-stream)
2. [Upload file via file streaming (Content-Range headers)](/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-content-range)
3. [Upload file via file streaming (Chunk ID)](/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-chunk-id)

## What happens if your API does not meet the prerequisites?

If the API you work with does not allow for chunked uploads or downloads, you can still download and upload files in-memory but subject to limitations of both time and size. **This is not recommended unless absolutely necessary.**

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/streaming/download-stream.md
description: >-
  Build a custom connector action that downloads files from a target application
  through file streaming using HTTP Range headers.
---

# How-to guides - Download file via file streaming (Range headers)

In this segment, we will be going through the creation of actions that download files in a target application through file streaming.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) quota.
> 
> You can use the [checkpoint!](/en/developing-connectors/sdk/sdk-reference/ruby_methods#checkpoint) method with file streaming actions to transfer files that exceed the timeout limit. The `checkpoint!` method checks the duration of an action's execution. If it exceeds 120 seconds, Workato refreshes the timeout with a slight delay to ensure fair processing.

## Sample connector - Egnyte

```ruby
{
  title: 'My Egnyte connector',

  # More connector code here
  actions: {
    download_object: {
      title: 'Download file from selected folder',

      description: lambda do |input, picklist_label|
        "Download <span class='provider'>file</span> in <span class='provider'>Egnyte</span>"
      end,

      help: 'Download file contents from selected folder in Egnyte.',

      input_fields: lambda do |object_definitions|
        [
          {
            name: 'file_path',
            label: 'File path',
            hint: 'Select path of file.',
            optional: false,
            control_type: 'tree',
            pick_list: 'file_path',
            toggle_hint: 'Select file',
            toggle_field: {
              name: 'file_path',
              type: 'string',
              control_type: 'text',
              label: 'File path',
              optional: false,
              toggle_hint: 'Use file path',
              hint: "Provide complete path of file. Example: <b>/Private/Sample/file.csv</b>"
            }
          }
        ]
      end,

      execute: lambda do |connection, input|
        file_path = input['file_path']&.gsub(/%2F/, '/')

        # This API call retrieves metadata about the file. Not the file itself.
        file_details = get("/pubapi/v1/fs/#{file_path}")

        file_details['file_contents'] = workato.stream.out("download_file_by_path", { file_path: file_path, file_size: file_details['size'] })

        file_details
      end,

      output_fields: lambda do |object_definitions|
        [
          { name: 'path' },
          { name: 'name' },
          { name: 'size' },
          { name: 'file_contents' }
        ]
      end
    },
  }

  streams: {
    download_file_by_path: lambda do |input, starting_byte_range, ending_byte_range, requested_byte_size|
      # Example starting_byte_range = 0
      # Example ending_byte_range = 10485759
      # Example requested_byte_size = 10485760 (10MB)
      chunk = get("/pubapi/v1/fs-content/#{input['file_path']}").
                headers("Range": "bytes=#{starting_byte_range}-#{ending_byte_range}").
                response_format_raw
      # The output of the streaming callback should be an array.
      # Firstly, passing the chunk of file
      # Secondly, a boolean value that indicates if this is the final chunk
      [chunk, ending_byte_range >= input['file_size']]
    end
  }

  # More connector code here
}
```

## Step 1 - Action title, subtitle, description, and help

The first step to making a good action is to properly communicate what the actions does, how it does it and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#title)

## Step 2 - Define input fields

```ruby
  input_fields: lambda do |object_definitions|
    [
      {
        name: 'file_path',
        label: 'File path',
        hint: 'Select path of file.',
        optional: false,
        control_type: 'tree',
        pick_list: 'file_path',
        toggle_hint: 'Select file',
        toggle_field: {
          name: 'file_path',
          type: 'string',
          control_type: 'text',
          label: 'File path',
          optional: false,
          toggle_hint: 'Use file path',
          hint: "Provide complete path of file. Example: <b>/Private/Sample/file.csv</b>"
        }
      }
    ]
  end
```

![Download file input fields](/assets/download_file_input.Cgl7Q7ZV.png)_Download file input fields_

This component tells Workato what fields to show to a user trying to retrieve an object. In the case of finding a file in Egnyte for example, the user has to input the `file_path` of the file that a user wishes to download.

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the `object_definitions` key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 3 - Defining the execute lambda

The execute lambda contains the code that is invoked when the job execution reaches this particular step. In the case of file download actions, there are two main objectives - retrieving the relevant file details (such as name, path and file size) and instantiating a file stream that represents the actual stream of the file contents.

In our example, we first take the `file_path` given from the input and format it by replacing any URL encoded value with the actual intended character, in this case, we replace `%2F` with `/`. Next, we retrieve the `file_details` by sending a request to the `/pubapi/v1/fs/#{file_path}` endpoint. This retrieves all the relevant information we need about this particular file.

Next we add one more attribute to the `file_details` output called `file_contents` which is the instantiated file stream using the `workato.stream.out` method. In this method, we define the `stream` lambda function we want to use - `download_file_by_path` - as well as pass it a hash `{ file_path: file_path, file_size: file_details['size'] }` which will be passed as the input to the lambda function.

```ruby
  execute: lambda do |connection, input|
    file_path = input['file_path']&.gsub(/%2F/, '/')

    # This API call retrieves metadata about the file. Not the file itself.
    file_details = get("/pubapi/v1/fs/#{file_path}")

    file_details['file_contents'] = workato.stream.out("download_file_by_path", { file_path: file_path, file_size: file_details['size'] })

    file_details
  end,
```

## Step 4 - Defining output fields

This section tells us what datapills to show as the output of the trigger. The `name` attributes of each datapill should match the keys in the output hash of the `execute` lambda function.

```ruby
  output_fields: lambda do |object_definitions|
    [
      { name: 'path' },
      { name: 'name' },
      { name: 'size' },
      { name: 'file_contents' }
    ]
  end
```

To know more about the output fields key, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#output-fields)

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the `object_definitions` key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Step 5 - Defining the streaming lambda function

The instantiation of a file stream using `workato.stream.out` now needs to be coupled with the specified streaming callback `download_file_by_path`. This is a lambda function defined in the `streams` hash and the main objective of this lambda function is to download a specific chunk of the file given arguments passed to it. We utilize a GET request to the `/pubapi/v1/fs-content/#{file_path}` where we add the headers for `Range` to be from the `starting_byte_range` to the `ending_byte_range`. You must also add `response_format_raw` if the data sent back from the server is the pure binary data and not a JSON response.

Lastly, the output of the streaming callback should be an array of size 2:

1. The first index is the binary data
2. The second index is a boolean value that denotes the end of file. In this case, since we can retrieve the expected size (in bytes) of the file, we know that if the ending\_byte\_range is larger than the file's size, we are at the end of the file.

```ruby
  streams: {
    download_file_by_path: lambda do |input, starting_byte_range, ending_byte_range, requested_byte_size|
      # Example starting_byte_range = 0
      # Example ending_byte_range = 10485759
      # Example requested_byte_size = 10485760 (10MB)
      chunk = get("/pubapi/v1/fs-content/#{input['file_path']}").
                headers("Range": "bytes=#{starting_byte_range}-#{ending_byte_range}").
                response_format_raw
      # The output of the streaming callback should be an array.
      # Firstly, passing the chunk of file
      # Secondly, a boolean value that indicates if this is the final chunk
      [chunk, ending_byte_range >= input['file_size']]
    end
  }
```

> **TIP**
> 
> Understanding the streaming callback makes most sense when thinking about it alongside a stream consumer. Stream consumers control the streaming callback where it first requests a single chunk of data, uploads it to the downstream system, before reiterating on the process over and over until the entire file is streamed over. As such, the `starting_byte_range` and `ending_byte_range` represent the byte range requested from the streaming consumer. The `requested_byte_size` is a synthetic argument that is useful for comparing the stream producing endpoint has simply no more bytes to provide, indicating the end of file. This signal will be sent over to the stream consumer to continue on with the recipe.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-content-range.md
description: >-
  Build a custom connector SDK action that uploads files via file streaming
  using Content-Range headers to send chunks.
---

# How-to guides - Upload file via file streaming (Content-Range headers)

In this segment, we will be going through the creation of actions that uploads files in a target application through file streaming and utilizing Content-Range Headers.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.
> 
> You can use the `checkpoint!` method with file streaming actions to transfer files that exceed the timeout limit. Refer to the [Using our multistep framework to extend upload times](/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-chunk-id#using-our-multistep-framework-to-extend-upload-times) section for additional information.

## Sample connector

```ruby
{
  title: 'Upload file to URL',

  # More connector code here
  actions: {
    upload_to_url: {
      input_fields: lambda do |_object_definitions|
        [
          { name: "file_name", type: "string" },
          { name: "file", type: "stream" }, # field type must be stream
          { name: "url", label: "Any friendly URL" }
        ]
      end,

      execute: lambda do |_connection, input, _input_schema, _output_schema, closure|
        # Calling workato.stream.in runs in a loop where the input should be file.
        # It can accept both entire files or the output of a streaming-enabled download file action
        workato.stream.in(input["file"]) do |chunk, starting_byte_range, ending_byte_range, eof, next_starting_byte_range|
          put(input['url']).
            headers("Content-Range": "bytes #{starting_byte_range}-#{ending_byte_range}/*").
            request_body(chunk).presence
        end

        # This commits the upload
        post(input['url'], { "commit": true } )

      end,

      output_fields: lambda do |object_definitions|
        [
          { name: "file_name", type: "string" },
          { name: "file_path", type: "string" },
          { name: "file_size", type: "integer" }
        ]
      end
    }
  }
  # More connector code here
}
```

## Step 1 - Action title, subtitles, description, and help

The first step to making a good action is to properly communicate what the actions does, how it does it and to provide additional help to users. To do so, Workato allows you to define the title, subtitles, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#title)

## Step 2 - Define input fields

```ruby
  input_fields: lambda do |object_definitions|
    [
      { name: "file_name", type: "string" },
      { name: "file", type: "stream" }, # field type must be stream
      { name: "url", label: "Any friendly URL" }
    ]
  end,
```

This component tells Workato what fields to show to a user trying to upload an object. In the case of this connector, we collect the `file_name`, the `file` which must be defined with `type` as `stream` and the `url` input for a friendly URL that we can upload this file to.

## Step 3 - Defining the execute key

In the execute action, we define the `workato.stream.in` which takes in the `file` stream input.

After calling `workato.stream.in` you're required to define a block that signifies how to upload this particular chunk of data received. In this block, we send a PUT request to the URL alongside standard `Content-Range` headers to denote the part of the file we are uploading. `workato.stream.in` continues to loop over this block until the `stream` consumer dictates that the file has ended.

After the stream is consumed, we send a POST request to commit the entire upload as a new file.

```ruby
  execute: lambda do |_connection, input, _input_schema, _output_schema, closure|
    # Calling workato.stream.in runs in a loop where the input should be file.
    # It can accept both entire files or the output of a streaming-enabled download file action
    workato.stream.in(input["file"]) do |chunk, starting_byte_range, ending_byte_range, eof, next_starting_byte_range|
      put(input['url']).
        headers("Content-Range": "bytes #{starting_byte_range}-#{ending_byte_range}/*").
        request_body(chunk).
        presence # presence is required as a way to force the HTTP request to be sent.
    end

    # This commits the upload
    post(input['url'], { "commit": true } )

  end,
```

> **INFO**
> 
> Take note that we assume the API accepts `*` as a wildcard range, indicating that the total file size is not yet known. In some cases, APIs may not accept a wildcard range and you should add an input field to collect the total file size from the recipe builder.

## Step 4 - Defining output fields

This section tells us what datapills to show as the output of the trigger. The `name` attributes of each datapill should match the keys in the output of the `execute` key. Here, we assume the response from the final POST request returns the `file_name`, `file_path` and `file_size`.

```ruby
  output_fields: lambda do |object_definitions|
    [
      { name: "file_name", type: "string" },
      { name: "file_path", type: "string" },
      { name: "file_size", type: "integer" }
    ]
  end
```

## Variations

### Using our multistep framework to extend upload times

When defining the `workato.stream.in` method, you are able to define an additional named parameter for `from`, which can be used in conjunction with the `checkpoint!` method to extend the timeout of your upload action beyond Workato's default 180-second timeout limit.

When `checkpoint!` is called, it checks if action's current execution time is larger than 120 seconds, and if so, refreshes the action timeout after a short waiting period. This can be used in conjunction with the `from` argument to tell Workato's streaming library where to continue from the last byte offset.

```ruby
  execute: lambda do |_connection, input, _input_schema, _output_schema, closure|
    next_from = closure["next_from"].presence || 0
    # Calling workato.stream.in runs in a loop where the input should be file.
    # It can accept both entire files or the output of a streaming-enabled download file action
    workato.stream.in(input["file"], from: next_from) do |chunk, starting_byte_range, ending_byte_range, eof, next_starting_byte_range|
      put(input['url']).
        headers("Content-Range": "bytes #{starting_byte_range}-#{ending_byte_range}/*").
        request_body(chunk).
        presence # presence is required as a way to force the HTTP request to be sent.

        # Call checkpoint unless it is the end of file.
        checkpoint!(continue: { next_from: next_starting_byte_range }) unless eof
    end

    # This commits the upload
    post(input['url'], { "commit": true } )

  end
```

### Adjusting the default 10MB chunk size

When Workato attempts to retrieve a file chunk from an API, it defaults to requesting a 10MB chunk. In some cases, your API may require a larger minimum chunk size and you can override this default by declaring your own chunk size using the `frame_size` argument.

Take note that this does not guarantee that you will receive a chunk size of 20MB from all producers. You can make necessary precautions by storing a temporary buffer as well.

```ruby
  execute: lambda do |_connection, input, _input_schema, _output_schema, closure|
    # 20MB in bytes
    frame_size = 20971520
    next_from = closure["next_from"].presence || 0
    buffer = ""
    # Calling workato.stream.in runs in a loop where the input should be file.
    # It can accept both entire files or the output of a streaming-enabled download file action
    workato.stream.in(input["file"], from: next_from, frame_size: frame_size) do |chunk, starting_byte_range, ending_byte_range, eof, next_starting_byte_range|
      # save chunk to buffer
      buffer << chunk

      # If not end of file and buffer is less than require size, skip to next iteration
      if !eof && buffer.size < frame_size
        next
      end
      put(input['url']).
        headers("Content-Range": "bytes #{starting_byte_range}-#{ending_byte_range}/*").
        request_body(buffer).
        presence # presence is required as a way to force the HTTP request to be sent.

      #reset buffer
      buffer = ""

      # Call checkpoint unless it is the end of file.
      checkpoint!(continue: { next_from: next_starting_byte_range }) unless eof
    end

    # This commits the upload
    post(input['url'], { "commit": true } )

  end
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-chunk-id.md
description: >-
  Build a custom connector SDK action that uploads files via file streaming
  using chunk IDs, with an Azure Blob example.
---

# How-to guides - Upload file via file streaming (Chunk ID)

In this segment, we will be going through the creation of actions that uploads files in a target application through file streaming and utilizing assigning IDs to chunks. We will be going through [Azure Blob's API](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob) but this can be extended to many other cloud storage solutions.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.
> 
> You can use the `checkpoint!` method with file streaming actions to transfer files that exceed the timeout limit. Refer to the [Using our multistep framework to extend upload times](/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-chunk-id#using-our-multistep-framework-to-extend-upload-times) section for additional information.

## Sample connector

```ruby
{
  title: 'Upload to Azure Blob Friend URL',

  # More connector code here
  actions: {
    upload_to_url: {
      input_fields: lambda do |_object_definitions|
        [
          { name: "file", type: "stream" }, # field type must be stream
          { name: "url", label: "Any friendly URL" }
        ]
      end,

      execute: lambda do |_connection, input, _input_schema, _output_schema, closure|
        block_list = []
        # Calling workato.stream.in runs in a loop where the input should be file.
        # It can accept both entire files or the output of a streaming-enabled download file action
        workato.stream.in(input["file"]) do |chunk, starting_byte_range, ending_byte_range, eof, next_starting_byte_range|
          block_id = workato.uuid.encode_base64
          block_list << block_id
          put(input['url']).
            params("comp": "block", "blockid": block_id).
            request_body(chunk).
            presence # presence is required as a way to force the HTTP request to be sent.
        end

        payload = {
          "Latest": block_list
        }

        {
          "Etag" => put(input['url']).
                      params("comp": "blocklist").
                      payload(payload).
                      request_format_xml("BlockList").
                      response_format_raw.
                      after_response do |code, body, header|
                        header['Etag']
                      end
        }

      end,

      output_fields: lambda do |object_definitions|
        [
          { name: "Etag", type: "string" }
        ]
      end
    }
  }
  # More connector code here
}
```

### Step 1 - Action title, subtitles, description, and help

The first step to making a good action is to properly communicate what the actions does, how it does it and to provide additional help to users. To do so, Workato allows you to define the title, subtitles, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#title)

### Step 2 - Define input fields

```ruby
  input_fields: lambda do |object_definitions|
    [
      { name: "file", type: "stream" }, # field type must be stream
      { name: "url", label: "Any friendly URL" }
    ]
  end,
```

This component tells Workato what fields to show to a user trying to upload an object. In the case of this connector, we collect the `file_name`, the `file` which must be defined with `type` as `stream` and the `url` input for a friendly URL that we can upload this file to.

### Step 3 - Defining the execute key

In the execute action, we define the `workato.stream.in` which takes in the `file` stream input.

After calling `workato.stream.in` you're required to define a block that signifies how to upload this particular chunk of data received. In this block, we create a unique UUID that we base64 encode - as per Azure's requirements. We save this `block_id` in an array of blocks which we will send at the end to commit this entire file.

We then send a PUT request to the friendly Azure URL alongside this block\_id. `workato.stream.in` continues to loop over this block until the `stream` consumer dictates that the file has ended.

After the stream is consumed, we send a final PUT request with the entire blocklist. This is in XML format as dictated by Azure Blob's API.

```ruby
  execute: lambda do |_connection, input, _input_schema, _output_schema, closure|
    block_list = []
    # Calling workato.stream.in runs in a loop where the input should be file.
    # It can accept both entire files or the output of a streaming-enabled download file action
    workato.stream.in(input["file"]) do |chunk, starting_byte_range, ending_byte_range, eof, next_starting_byte_range|
      block_id = workato.uuid.encode_base64
      block_list << block_id
      put(input['url']).
        params("comp": "block", "blockid": block_id).
        request_body(chunk).
        presence
    end

    payload = {
      "Latest": block_list
    }

    {
      "Etag" => put(input['url']).
                  params("comp": "blocklist").
                  payload(payload).
                  request_format_xml("BlockList").
                  response_format_raw.
                  after_response do |code, body, header|
                    header['Etag']
                  end
    }

  end,
```

### Step 4 - Defining output fields

This section tells us what datapills to show as the output of the trigger. The `name` attributes of each datapill should match the keys in the output of the `execute` key.

```ruby
  output_fields: lambda do |object_definitions|
      output_fields: lambda do |object_definitions|
        [
          { name: "Etag", type: "string" }
        ]
      end
  end
```

## Variations

### Using our multistep framework to extend upload times

When defining the `workato.stream.in` method, you are able to define an additional named parameter for `from`, which can be used in conjunction with the `checkpoint!` method to extend the timeout of your upload action beyond Workato's default 180-second timeout limit.

When `checkpoint!` is called, it checks if action's current execution time is larger than 120 seconds, and if so, refreshes the action timeout after a short waiting period. This can be used in conjunction with the `from` argument to tell Workato's streaming library where to continue from the last byte offset.

```ruby
  execute: lambda do |_connection, input, _input_schema, _output_schema, closure|
    block_list = closure["block_list"].presence || []
    next_from = closure["next_from"].presence || 0

    # Calling workato.stream.in runs in a loop where the input should be file.
    # It can accept both entire files or the output of a streaming-enabled download file action
    workato.stream.in(input["file"], from: next_from, frame_size: frame_size) do |chunk, starting_byte_range, ending_byte_range, eof, next_starting_byte_range|

      block_id = workato.uuid.encode_base64
      block_list << block_id
      put(input['url']).p
        arams("comp": "block", "blockid": block_id).r
        equest_body(chunk).
        presence # presence is required as a way to force the HTTP request to be sent.

      # Call checkpoint unless it is the end of file.
      checkpoint!(continue: { next_from: next_starting_byte_range, block_list: block_list }) unless eof
    end

    payload = {
      "Latest": block_list
    }

    {
      "Etag" => put(input['url']).
                  params("comp": "blocklist").
                  payload(payload).r
                  equest_format_xml("BlockList").
                  response_format_raw.
                  after_response do |code, body, header|
                    header['Etag']
                  end
    }
  end
```

### Adjusting the default 10MB chunk size

When Workato attempts to retrieve a file chunk from an API, it defaults to requesting a 10MB chunk. In some cases, your API may require a larger minimum chunk size and you can override this default by declaring your own chunk size using the `frame_size` argument.

Take note that this does not guarantee that you will receive a chunk size of 20MB from all producers. You can make necessary precautions by storing a temporary buffer as well.

```ruby
  execute: lambda do |_connection, input, _input_schema, _output_schema, closure|
    # 20MB in bytes
    frame_size = 20971520
    block_list = closure["block_list"].presence || []
    next_from = closure["next_from"].presence || 0
    buffer = ""

    # Calling workato.stream.in runs in a loop where the input should be file.
    # It can accept both entire files or the output of a streaming-enabled download file action
    workato.stream.in(input["file"], from: next_from, frame_size: frame_size) do |chunk, starting_byte_range, ending_byte_range, eof, next_starting_byte_range|
      # save chunk to buffer
      buffer << chunk
      if !eof && buffer.size < frame_size
        next
      end
      block_id = workato.uuid.encode_base64
      block_list << block_id
      put(input['url']).p
        arams("comp": "block", "blockid": block_id).r
        equest_body(buffer).
        presence # presence is required as a way to force the HTTP request to be sent.

      #reset buffer
      buffer = ""

      # Call checkpoint unless it is the end of file.
      checkpoint!(continue: { next_from: next_starting_byte_range, block_list: block_list }) unless eof
    end

    payload = {
      "Latest": block_list
    }

    {
      "Etag" => put(input['url']).
                  params("comp": "blocklist").
                  payload(payload).r
                  equest_format_xml("BlockList").
                  response_format_raw.
                  after_response do |code, body, header|
                    header['Etag']
                  end
    }
  end
```

---
