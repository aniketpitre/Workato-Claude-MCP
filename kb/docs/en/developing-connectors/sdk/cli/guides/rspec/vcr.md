---
url: 'https://docs.workato.com/en/developing-connectors/sdk/cli/guides/rspec/vcr.md'
description: >-
  Set up VCR to record and replay HTTP interactions for stable connector unit
  tests, including encrypting recordings with your master key.
---

# How-to guides - Setting up VCR for your unit tests

In this segment, we will be going through how you can set up VCR to record HTTP interactions for your unit tests.

## Why do I need VCR for my unit tests?

The VCR gem works hand in hand with RSpec tests to record any HTTP interactions (requests) that are sent out when you are running your test suite and play back the same responses if the test suite is run again.

This is critical for stable RSpec tests especially when you're working with an environments where data could be changing constantly. For example, for the same `GET` request, you might get a different response when later on, but VCR will be able to play your tests back with the same HTTP response it saw earlier, so your tests can make the same assertions.

This removes one aspect of variability in your tests and ensures that you're only testing for changes in your code and nothing else.

[Learn more about VCR](https://relishapp.com/vcr/vcr/v/1-10-3/docs/getting-started).

## How do I get started?

When you generate a connector project using the command `workato new [PATH]`, VCR will be set up automatically.

If you set up the project with the `secure` option, the VCR recordings are also encrypted. We recommend you use the `secure` option. In any case, your `spec_helper.rb` contains all information about your VCR recording configurations. Setting your project to `secure` ensures your VCR recordings are encrypted with your `master.key`. Below you can find an example of a `spec_helper.rb` which includes encryption.

```ruby
# frozen_string_literal: true

require 'bundler/setup'
require 'json'
require "webmock/rspec"
require "timecop"
require "vcr"
require "workato-connector-sdk"
require "workato/testing/vcr_encrypted_cassette_serializer"
require "workato/testing/vcr_multipart_body_matcher"

RSpec.configure do |config|
  # Enable flags like --only-failures and --next-failure
  config.example_status_persistence_file_path = ".rspec_status"

  # Disable RSpec exposing methods globally on `Module` and `main`
  config.disable_monkey_patching!

  config.expect_with :rspec do |c|
    c.syntax = :expect
  end
end

VCR.configure do |config|
  config.cassette_library_dir = "tape_library"
  config.hook_into :webmock
  config.cassette_serializers[:encrypted] = Workato::Testing::VCREncryptedCassetteSerializer.new
  config.register_request_matcher :headers_without_user_agent do |request1, request2|
    request1.headers.except("User-Agent") == request2.headers.except("User-Agent")
  end
  config.register_request_matcher :multipart_body do |request1, request2|
    Workato::Testing::VCRMultipartBodyMatcher.call(request1, request2)
  end
  config.default_cassette_options = {
    record: ENV.fetch('VCR_RECORD_MODE', :none).to_sym,
    serialize_with: :encrypted,
    match_requests_on: %i[uri headers_without_user_agent body]
  }
  config.configure_rspec_metadata!
end
```

> **TIP**
> 
> **By default our record mode for secure is `none` which means no new VCR cassettes are recorded. To record new VCR cassettes, run the RSpec tests with the following command `VCR_RECORD_MODE=once bundle exec rspec spec/actions/test_action_spec.rb`.**

## Can I make modifications to the VCR settings?

You can do so in `spec_helper.rb`. You can modify the spec\_helper to suite your needs such as changing or relaxing the conditions as to how VCR matches your outgoing HTTP requests to previously recorded interactions.

Example: Relaxing VCR matching to accept different Authorization Headers by adjusting `spec_helper.rb`

```ruby
config.register_request_matcher :headers_without_user_agent do |request1, request2|
  request1.headers.except('User-Agent', 'Authorization') == request2.headers.except('User-Agent', 'Authorization')
end
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/rspec/connector_spec.md
description: >-
  Write RSpec tests for your custom connector's connection using the Workato SDK
  gem to validate authentication and connection logic.
---

# How-to guides - Writing tests for your connection

In this segment, we will be going through how you can write tests for your connector's connection.

## Sample connector

The code in `connector.rb`.

```ruby
{
  title: 'Chargebee-demo',

  connection: {
    fields: [
      {
        name: 'api_key',
        control_type: 'password',
        hint: 'You can find your API key final change3' \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: 'Your API Key'
      },
      {
        name: 'domain',
        control_type: 'subdomain',
        url: 'chargebee.com'
      }
    ],

    authorization: {
      type: 'basic_auth',

      apply: lambda do |connection|
        user(connection['api_key'])
      end
    },

    base_uri: lambda do |connect|
      "https://#{connect['domain']}.chargebee.com"
    end
  },

  test: lambda do |_connection|
    get('/api/v2/plans', limit: 1)
  end,
}
```

Credentials in `settings.yaml.enc`.

```yaml
api_key: valid_api_key
domain: valid_domain
```

## Generating your tests

Your project should have already come with a sample `connector_spec.rb` file if you generated the connector project using `workato new [PATH]`. If not, you should create this file to house your `test` lambda tests.

### Sample RSpec contents

The code in `connector_spec.rb`.

```ruby
RSpec.describe 'connector', :vcr do

  let(:connector) { Workato::Connector::Sdk::Connector.from_file('connector.rb', settings) }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }

  it { expect(connector).to be_present }

  describe 'test' do
    subject(:output) { connector.test(settings) }

    context 'given valid credentials' do
      it 'establishes valid connection' do
        expect(output).to be_truthy
      end

      it 'returns response that is formatted properly' do
        # large Test responses might also cause connections to be evaluated wrongly
        expect(output.to_s.length).to be < 5000
        expect(output['list']).to be_kind_of(::Array)
      end
    end
  end
end
```

Here, we have defined 2 tests for the `test` lambda but lets go over it step by step.

## Step 1 - Define your connector instance

To begin testing, you need to use the Workato SDK Gem to create an instance of your connector.

```ruby
  let(:connector) { Workato::Connector::Sdk::Connector.from_file('connector.rb', settings) }
```

## Step 2 - Define your settings instance

To begin testing, you need to use the Workato SDK Gem to create an instance of your settings. This is synonymous with your connection on Workato. Take note that, your connector instance previously defined also uses this settings instance.

```ruby
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }
```

To instantiate your settings from an alternative setting file, you can use `from_encrypted_file` or `from_file`.

```ruby
  let(:settings) { Workato::Connector::Sdk::Settings.from_encrypted_file('invalid_settings.yaml.enc') }
```

## Step 3 - Describe your tests and define your subject

Here, we describe the "family" of tests we are hoping to run. In this case, we use the keyword `test`. After that, we also define a `subject` of our tests. This is where we assign the value of `output` to our connector instance running the `test` lambda. This is done with the `connector.test(settings)` defined.

```ruby
  describe 'test' do
    subject(:output) { connector.test(settings) }
```

## Step 4 - Declare your assertions for individual tests

For a test to pass or fail, there needs to be a declared comparison.

Over here, we are declaring that we "expect" the output of the `test` lambda to be `truthy` to satisfy the test - "establishes valid connection".

We also "expect" that the output of the `test` lambda to be less than 5000 characters long and that its `list` attribute is an array. This satisfies the test - "returns response that is formatted properly"

```ruby
    context 'given valid credentials' do
      it 'establishes valid connection' do
        expect(output).to be_truthy
      end

      it 'returns response that is formatted properly' do
        # large Test responses might also cause connections to be evaluated wrongly
        expect(output.to_s.length).to be < 5000
        expect(output['list']).to be_kind_of(::Array)
      end
    end
```

## Step 5 - Run your RSpec tests

Now the last step is to run your RSpec tests. This is done with the `bundle exec rspec spec/connector_spec.rb` command.

```shell
$ bundle exec rspec spec/connector_spec.rb

connector
  is expected to be present
  test
    given valid credentials
      establishes valid connection
      returns response that is formatted properly

Finished in 0.04959 seconds (files took 1.04 seconds to load)
3 examples, 0 failures
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/rspec/writing_tests.md
description: >-
  Write RSpec tests for the triggers and actions in your custom connector,
  validating an action's execute lambda with the SDK gem.
---

# How-to guides - Writing tests for triggers/actions

In this segment, we will be going through how you can write tests for any lambda in your connector. For this, we will be writing tests for a single action's execute lambda. The same logic can be applied to the rest of the lambdas as well.

## Sample connector

The code in `connector.rb`.

```ruby
{
  title: 'Chargebee-demo',

  connection: {
    fields: [
      {
        name: 'api_key',
        control_type: 'password',
        hint: 'You can find your API key final change3' \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: 'Your API Key'
      },
      {
        name: 'domain',
        control_type: 'subdomain',
        url: 'chargebee.com'
      }
    ],

    authorization: {
      type: 'basic_auth',

      apply: lambda do |connection|
        user(connection['api_key'])
      end
    },

    base_uri: lambda do |connect|
      "https://#{connect['domain']}.chargebee.com"
    end
  },

  test: lambda do |_connection|
    get('/api/v2/plans', limit: 1)
  end,

  actions: {

    search_customers: {
      title: 'Search customers',
      subtitle: 'Search for customers using name',
      description: 'Search customer in Chargebee',

      input_fields: lambda do |_object_definitions|
        [
          {
            name: 'name',
            label: 'Name to query by',
            hint: 'Provide the name of the customer to query'
          },
          {
            name: 'id',
            label: 'Name to query by',
            hint: 'Provide the name of the customer to query'
          }
        ]
      end,

      execute: lambda do |_connection, input, _input_schema, _output_schema|
        get('/api/v2/customers', input)
      end,

      output_fields: lambda do |_object_definitions|
        [
          {
            name: 'first_name'
          },
          {
            name: 'last_name'
          },
          {
            name: 'id'
          }
        ]
      end
    }

  },

}
```

Credentials in `settings.yaml.enc` .

```yaml
api_key: valid_api_key
domain: valid_domain
```

## Generating your tests

You can create a separate spec file for each action or generate your tests based on your connector by using the `workato generate test` command. This will generate a spec file which will include most of the necessary stubs for your to start writing tests.

### Sample RSpec contents

```ruby
RSpec.describe 'actions/search_customers', :vcr do

  subject(:output) { connector.actions.search_customers(input) }

  let(:connector) { Workato::Connector::Sdk::Connector.from_file('connector.rb', settings) }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }
  let(:input) { JSON.parse(File.read('fixtures/actions/search_customers/input.json')) }

  let(:expected_output) { JSON.parse(File.read('fixtures/actions/search_customers/output.json')) }

  describe 'given valid input' do
    it 'gives expected output' do
      expect(output).to eq(expected_output)
    end
  end

  let(:action) { connector.actions.search_customers }

  describe 'execute' do
    subject(:output) { action.execute(settings, input) }
    let(:input) { JSON.parse(File.read('fixtures/actions/search_customers/input_parsed.json')) }
    let(:expected_output) { JSON.parse(File.read('fixtures/actions/search_customers/output.json')) }

    context 'given valid input' do
      it 'gives expected output' do
        expect(output).to eq(expected_output)
      end
    end
  end

  describe 'sample_output' do
    subject(:sample_output) { action.sample_output(settings, input) }

    pending 'add some examples'
  end

  describe 'input_fields' do
    subject(:input_fields) { action.input_fields(settings, config_fields) }

    pending 'add some examples'
  end

  describe 'output_fields' do
    subject(:output_fields) { action.output_fields(settings, config_fields) }

    pending 'add some examples'
  end
end
```

Here, you can see that we have stubs for various tests for this action. This is given when you generate tests using the Gem. We will be going through how to write tests for just the `execute` lambda.

## Step 1 - Define your connector instance

To begin testing, you need to use the Workato SDK Gem to create an instance of your connector.

```ruby
  let(:connector) { Workato::Connector::Sdk::Connector.from_file('connector.rb', settings) }
```

## Step 2 - Define your settings instance

Next, you need to use the Workato SDK Gem to create an instance of your settings. This is synonymous with your connection on Workato. Take note that, your connector instance previously defined also uses this settings instance.

```ruby
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }
```

## Step 3 - Define your action

After creating the related instances, we instantiate the `action` so we can reference it more easily in the rest of the tests.

```ruby
  let(:action) { connector.actions.search_customers }
```

## Step 3 - Describe your tests and define your subject

Here, we describe the "family" of tests we are hoping to run. In this case, we use the keyword `execute`. After that, we also define a `subject` of our tests. This is where we assign the value of `output` to our connector instance running the `execute` lambda of the `search_customers` action. This is done with the `action.execute(settings,input)` defined.

```ruby
  describe 'execute' do
    subject(:output) { action.execute(settings, input) }
```

> **TIP**
> 
> When you generate tests, you might be curious why you have 2 additional arguments for `execute` which are `extended_input_schema` and `extended_output_schema`. Similar to the `execute:` lambda when you define it in your connector, the `execute` here can accept the same 4 arguments. We've removed them for this action as they weren't needed.

## Step 4 - Declare your assertions for individual tests

For a test to pass or fail, there needs to be a declared comparison.

Over here, we are declaring that we "expect" the output of the `execute` lambda to be equals to a previously known response where we gave it a valid input. This was done by creating 2 new variables, `input` and `expected_output`. Generating `expected_output` doesn't need to be done manually but can be done when you run the CLI commands to invoke the `execute` lambda. For example, `workato exec actions.search_customers.execute --input='fixtures/actions/search_customers/input.json' --output='fixtures/actions/search_customers/output.json'`.

```ruby
  describe 'execute' do
    subject(:output) { action.execute(settings, input) }
    let(:input) { JSON.parse(File.read('fixtures/actions/search_customers/input.json')) }
    let(:expected_output) { JSON.parse(File.read('fixtures/actions/search_customers/output.json')) }

    context 'given valid input' do
      it 'gives expected output' do
        expect(output).to eq(expected_output)
      end
    end
  end
```

## Step 5 - Run your RSpec tests

Now the last step is to run your RSpec tests. This is done with the `bundle exec rspec spec/actions/search_customers_spec.rb` command.

```shell
$ bundle exec rspec spec/actions/search_customers_spec.rb

actions/search_customers
  execute
    given valid input
      gives expected output
  sample_output
    add some examples (PENDING: Not yet implemented)
  input_fields
    add some examples (PENDING: Not yet implemented)
  output_fields
    add some examples (PENDING: Not yet implemented)

Pending: (Failures listed here are expected and do not affect your suites status)

  1) actions/search_customers sample_output add some examples
     # Not yet implemented
     # ./spec/actions/search_customers_spec.rb:28

  2) actions/search_customers input_fields add some examples
     # Not yet implemented
     # ./spec/actions/search_customers_spec.rb:34

  3) actions/search_customers output_fields add some examples
     # Not yet implemented
     # ./spec/actions/search_customers_spec.rb:40


Finished in 0.03218 seconds (files took 0.90373 seconds to load)
4 examples, 0 failures, 3 pending
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/rspec/file_streaming.md
description: >-
  Write RSpec tests for actions and triggers that use Workato file streaming,
  including stubbing frame size and file stream inputs.
---

# How-to guides - Writing tests for streaming triggers/actions

This segment covers writing tests for actions that utilize Workato's file streaming capabilities, using the [generic upload file to URL connector example](/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-content-range) as a reference.

## Generating your tests

You can create a separate spec file for each action or generate your tests based on your connector by using the `workato generate test` command. This will generate a spec file which will include most of the necessary stubs for your to start writing tests.

### Sample RSpec contents

```ruby
RSpec.describe 'actions/upload_file_to_url', :vcr do

  let(:connector) { Workato::Connector::Sdk::Connector.from_file('connector.rb', settings) }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }

  before do
    stub_const('Workato::Connector::Sdk::Stream::Reader::DEFAULT_FRAME_SIZE', 5.kilobytes)
  end

  let(:action) { connector.actions.upload_file_to_url }

  describe 'execute' do
    subject(:output) { action.execute(settings, input) }

    let(:input) do
      {
          "file_name": "sample_file",
          "file": {
            "__stream__": true,
            "chunks": {
              "0": "abcd",
              "4": "efgh",
              "8": "ijkl",
              "12": "mn"
            }
          },
          "url": "https://www.friendly_s3_url.com/upload"
      }
    end

    it 'given simple stream' do
      it 'produces a file' do
        is_expected.to include(:file_size)
        expect(output.file_size).to eq(13)

        is_expected.to include(:file_path)

        is_expected.to include(:file_name)
      end
    end
  end

end
```

## Step 1 - Define your connector instance

To begin testing, you need to use the Workato SDK Gem to create an instance of your connector.

```ruby
  let(:connector) { Workato::Connector::Sdk::Connector.from_file('connector.rb', settings) }
```

## Step 2 - Define your settings instance

Next, you need to use the Workato SDK Gem to create an instance of your settings. This is synonymous with your connection on Workato. Take note that, your connector instance previously defined also uses this settings instance.

```ruby
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }
```

## Step 3 - Define your action

After creating the related instances, we instantiate the `action` so we can reference it more easily in the rest of the tests.

```ruby
  let(:action) { connector.actions.upload_file_to_url }
```

## Step 3 - Describe your tests, define your subject and input

Here, we describe the "family" of tests we are hoping to run. In this case, we use the keyword `execute`. Next, we make the subject the output which is the outcome of the execution of the action. Lastly, we declare the `input` which is a simple stream.

```ruby
  describe 'execute' do
    subject(:output) { action.execute(settings, input) }

    let(:input) do
      {
          "file_name": "sample_file",
          "file": {
            # this hash simulates a file stream which is
            # the output of a download file object
            "__stream__": true,
            "chunks": {
              "0": "abcd",
              "4": "efgh",
              "8": "ijkl",
              "12": "mn"
            }
          },
          "url": "https://www.friendly_s3_url.com/upload"
      }
    end
```

## Step 4 - Declare your assertions for individual tests

For a test to pass or fail, there needs to be a declared comparison.

Over here, we are declaring that we "expect" the output of the `execute` lambda to include keys `file_size`, `file_path` and `file_name`. Furthermore, we expect the `file_size` value to be 13.

```ruby
  it 'given simple stream' do
    it 'produces a file' do
      is_expected.to include(:file_size)
      expect(output.file_size).to eq(13)

      is_expected.to include(:file_path)

      is_expected.to include(:file_name)
    end
  end
```

## Variations to mock streams in RSpec

Alongside mocking simple streams within your RSpec tests, you have the ability mock other variations as well.

Mock streams with each chunk explicitly

```ruby
let(:input) do
  {
      file_name: 'sample_file',
      file: {
        __stream__: true,
        chunks: {
          0 => 'abcd',
          4 => 'efgh',
          8 => 'ijkl',
          12 => 'mn'
        }
      },
      url: 'https://www.friendly_s3_url.com/upload'
  }
end
```

Mock streams by utilizing a stream implemented for a download file action/trigger in the same connector

```ruby
let(:input) do
  {
      file_name: 'sample_file',
      file: {
        __stream__: true,
        name: 'global_stream',
        input: {
          file_path: '/path/to/sample/file'
        }
      },
      url: 'https://www.friendly_s3_url.com/upload'
  }
end
```

Mock streams by providing the inline definition of a stream with its own authentication

> **TIP**
> 
> Advanced mocks like these are only available in RSpec tests and not in CLI execution.

```ruby
let(:input) do
  {
      file_name: 'sample_file',
      file: {
        __stream__: true,
        name: 'mock_advanced_stream',
        input: {
          file_path: '/path/to/sample/file'
        },
        settings: {
          # optional
          # A connection settings for stream mock application
          # if the mock makes authorized requests to external apps
          # Also can use Workato::Connector::Sdk::Settings.from_file
          domain: 'acme.egnyte.com',
          api_key: 'api_key'
        },
        connection: {
          # optional
          # A connection definition for stream source applications
          # if the mock makes authorized requests to external apps
          # It supports the same blocks as connector's connection definition
          authorization: {
            type: 'api_key',

            apply: lambda do |connection|
              headers(api_key: connection['api_key'])
            end
        },
        },
        chunks: lambda do |input, _first_byte, last_byte, size|
          chunk = get("/pubapi/v1/fs-content/#{file_path}").
              headers("Range": "bytes=#{starting_byte_range}-#{ending_byte_range}").
              response_format_raw

          [chunk, chunk.size < requested_byte_size]
        end
      },
      url: 'https://www.friendly_s3_url.com/upload'
  }
end
```

Mock streams by providing a static stream

```ruby
let(:input) do
  {
      file_name: 'sample_file',
      file: {
        data: '1234567890',
        oef: true
      },
      url: 'https://www.friendly_s3_url.com/upload'
  }
end
```

Mock streams by providing a string

```ruby
let(:input) do
  {
      file_name: 'sample_file',
      file: 'qwertyuiop[]',
      url: 'https://www.friendly_s3_url.com/upload'
  }
end
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/rspec/enable-ci-cd-on-github.md
description: >-
  Set up CI/CD for SDK connector development with GitHub Actions to run
  connector unit tests automatically on every pull request.
---

# Enabling CI/CD on GitHub

To improve deployment stability, we recommend implementing CI/CD tools into your connector development workflow. This guide will go over the process if you're using Github and Github actions. This same logic, however, can be ported over to other Git tools and CI/CD tools.

## Prerequisites

- You have a Github repository
- Permissions in your GitHub repository that allow you to manage Actions
- Permissions in your Github repository to set repository secrets

## Setting up GitHub Actions

Next, you'll create a [GitHub Actions](https://docs.github.com/en/actions) file. This file is used to define the steps the action will execute.

In your repository's `.github/workflows` folder, create a new `ruby.yml` file. For example:

```yaml
name: Connector Unit Test

on:
  pull_request:
    branches: [ main ]

jobs:
  test:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        ruby-version: ['2.4.10', '2.5', '2.7']

    steps:
    - uses: actions/checkout@v2
    - name: Set up Ruby
      uses: ruby/setup-ruby@v1
      with:
        ruby-version: ${{ matrix.ruby-version }}
        bundler-cache: true
    - name: Run tests
      env: # Only needed if using encrypted files.
        WORKATO_CONNECTOR_MASTER_KEY: ${{ secrets.WORKATO_CONNECTOR_MASTER_KEY }}
      run: bundle exec rspec
```

In this example, our project is using encrypted settings ([`settings.yaml.enc`](/en/developing-connectors/sdk/cli/reference/cli-project-directory-reference#settings-yaml-enc-settings-yaml)). When using encryption, make sure to:

- Add your project's `master.key` file to `.gitignore`, and
- Set environment variables in your repository using [encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets). In this example, our variable is named `WORKATO_CONNECTOR_MASTER_KEY`.

## Adding other automated checks

You may choose to add other types of checks such as [Rubocop](https://docs.github.com/en/actions/guides/building-and-testing-ruby#linting-your-code) which is a easy way to maintain code style.

## Automate deployment to Workato

Now, you might also want to automate the deployment of your connector to your DEV environment such that whenever a PR is merged, its automatically deployed to your workspace!

In your repository's `.github/workflows` folder, create a new `ruby.yml` file. For example:

```yaml
name: Connector Unit Test & Deployment

on:
  push:
    branches: [ main ]

jobs:
  test:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        ruby-version: ['2.4.10', '2.5', '2.7']

    steps:
    - uses: actions/checkout@v2
    - name: Set up Ruby
      uses: ruby/setup-ruby@v1
      with:
        ruby-version: ${{ matrix.ruby-version }}
        bundler-cache: true
    - name: Run tests
      env: # Only needed if using encrypted files.
        WORKATO_CONNECTOR_MASTER_KEY: ${{ secrets.WORKATO_CONNECTOR_MASTER_KEY }}
      run: bundle exec rspec
    - name: Push to DEV workspace Use this to push to DEV. This can be enabled when a PR is merged.
      env: # Only needed if using encrypted files.
        WORKATO_API_TOKEN: ${{ secrets.WORKATO_DEV_ENVIRONMENT_API_TOKEN}}
      run: bundle exec workato push -n "${{ github.event.head_commit.message }}"
```

## What's next?

- Learn more about the [files in your connector project](/en/developing-connectors/sdk/cli/reference/cli-project-directory-reference)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/troubleshooting.md
description: >-
  Answers to common questions about Workato SDK CLI errors, including failed
  workato command, exec, and push runs and how to debug them.
---

# Troubleshooting - FAQ

Running the workato command in my terminal results in errors

Here is a quick checklist of things to verify:

1. First check that you have installed a valid version of ruby. You can do this by typing `ruby -v` into your terminal. It should be ruby version `2.4.10` `2.5.X` or `2.7.X`. Our preferred version is `2.7.X`.
2. Check that you have installed the SDK gem. You can do that by running `gem install workato-connector-sdk` in your terminal. You can also use `gem which workato-connector-sdk` to find out where the gem is installed.
3. Run `bundle install` in your connector project to ensure you have all dependencies installed.
4. Remove your gemfile.lock and run `bundle install`.

When I run a workato exec command, I get an error.

You may get this error if your connector receives a `400` bad request response from an API call. You may use options like `--verbose` to see the request, `--debug` to see the stacktrace of the SDK Gem and byebug to debug further.

When I try to use the workato push command, I get an error

The `workato push` command tries to release your connector on Workato. If there are syntax errors in your connector, the output of the command will relay that to you.

```
Unable to publish custom adapter Chargebee Demo1: Syntax [["method require not allowed", 1, 0, 1, 16]] and Publish Can not publish adapter with code errors
```

Where this is telling you that there is 1 error (denoted by 1 index in the root array) and the error is from line 1 position 0 to line 1 position 16.

When I run RSpec, VCR states that there is an VCR::Errors::UnhandledHTTPRequestError:

VCR records and matches HTTP requests based on your configurations in your `spec_helper.rb`. What RSpec is telling you is that it can't match the HTTP request you have sent to anything that has been recorded. There are a few reasons for this:

1. If you've set up your connector project using `secure`, the default VCR recording mode is set to `none`. This means that when you run RSpec, no new HTTP interactions will be recorded but only previous ones will be played back. To run your unit tests to record all new HTTP interactions, you can use the command `VCR_RECORD_MODE=once bundle exec rspec`.
2. Your previously recorded interactions may not match the ones your connector is currently attempting to make. This could be for a variety of reasons such as different headers due to a new access token in place of an earlier one. You can relax the matching for VCR recordings in the `spec_helper.rb`. [Learn more](https://relishapp.com/vcr/vcr/v/1-6-0/docs/cassettes/request-matching)

Example: Relaxing VCR matching to accept different Authorization Headers by adjusting `spec_helper.rb`

```ruby
config.register_request_matcher :headers_without_user_agent do |request1, request2|
  request1.headers.except('User-Agent', 'Authorization') == request2.headers.except('User-Agent', 'Authorization')
end
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/reference/cli-commands.md
description: >-
  Reference for Workato SDK gem CLI commands, including help, edit, exec, push,
  and other commands for building and testing connectors.
---

# CLI Command Reference

Learn more about the commands you can use in CLI after installing the SDK gem.

* * *

## workato

Root command of the Workato gem. Synonymous with [`workato help`](#workato-help).

### Usage

```shell
$ workato
```

### Output

Description of commands available in the Workato gem.

* * *

## workato edit

Creates or edits an encrypted file.

### Usage

```shell
$ workato edit <PATH>
```

### Input

| Input | Description |
| --- | --- |
| **EDITOR** | The editor you'll use to edit the file. For example: `nano` |
| **PATH** | The path to the file that should be created or updated, in dot notation. |

### Options

| Option | Description |
| --- | --- |
| **\--key, -k** | The path to the encrypt/decrypt key. If this isn't provided, defaults to `master.key`. If a `master.key` file doesn't exist and no option is provided, a new `master.key` file is created. |

### Result

Encrypted file is created or updated. `master.key` is created if the file didn't previously exist and an option wasn't provided.

### Example

```bash
For Windows:
  $ set EDITOR=notepad
  $ workato edit settings.yaml.enc
For Mac:
  $ EDITOR="nano" workato edit settings.yaml.enc
```

* * *

## workato exec

Executes a specific lambda function in your connector for testing.

### Usage

```bash
$ workato exec <PATH> <OPTIONS>
```

### Input

| Input | Description |
| --- | --- |
| **PATH** | The path to the lambda to execute, in dot notation. For example: `actions.search_customers.execute` would correspond to the action `search_customers` and the execute lambda. You may also simulate the entire action with the path `actions.search_customers`. |

### Options

| Option | Description |
| --- | --- |
| **\-c or --connector** | The path to the `connector.rb` file to execute. Defaults to `connector.rb` if not provided. |
| **\-s or --settings** | The path to the `settings.yaml` file that stores the credentials. Defaults to `settings.yaml.enc`, then `settings.yaml` if not provided. |
| **\-n or --connection** | The connection name in the `settings.yaml` file. Only required if there are multiple credential sets. |
| **\-i or --input** | The path to the JSON file that stores the input. Used for `execute`, `webhook_notification`, or `poll` lambdas. |
| **\--closure** | The path to the JSON file that stores the closure. Used for `poll` lambdas to simulate polls after the initial poll. |
| **\-a or --args** | The path to the JSON file that stores arguments for a method or picklists. Used for `methods` or `pick_lists` lambdas to simulate their invocation. An error may arise if arguments were expected but not provided. |
| **\--extended-input-schema and --extended-output-schema** | The path to the JSON file that stores the `extended_input_schema` and `extended_output_schema`. Used for `execute`, `webhook_notification`, or `poll` lambdas. |
| **\--config-fields** | The path to the JSON file that stores the `config_fields` data. Used for `object_definitions`, `input_fields`, or `output_fields` lambdas. |
| **\--continue** | The path to the JSON file that store the `continue` data. Used for `execute` lambdas that have multistep implemented. |
| **\--from** | The starting byte range for a specific stream invocation. Used for `streams` lambdas. |
| **\--frame\_size** | The requested framesize in bytes for a specific stream invocation. Used for `streams` lambdas. |
| **\--webhook-headers** | The path to the JSON file(s) that store incoming webhook header data. Used for `webhook_notification` lambdas. |
| **\--webhook-params** | The path to the JSON files that store incoming webhook parameter data. Used for `webhook_notification` lambdas. |
| **\--webhook-payload** | The path to the JSON files that store incoming webhook payload data. Used for `webhook_notification` lambdas. |
| **\--webhook-url** | The path to the file that stores the webhook URL. Used for `webhook_subscribe` lambdas. |
| **\-o or --output** | The path to the file that saves the output of the lambda function. |
| **\--oauth2-code** | The OAuth2 code used to invoke the `acquire` lambda function. |
| **\--redirect-url** | The redirect-url used to invoke the `refresh` lambda function. |
| **\--refresh-token** | The refresh-token used to invoke the `refresh` lambda function. |
| **\--verbose** | Include this option to make the execution verbose. This means that all HTTP requests and request payloads will be shown. Response bodies won't be shown but can be inspected with `byebug`. |
| **\--debug** | Include this option to show errors from the entire stacktrace, rather than just the last encountered error. |

### Result

The output of the lambda function.

### Examples

Invoke a specific method.

```bash
$ workato exec methods.sample_method --args='input/sample_method_input.json'
```

Invoke the acquire lambda. Connector and settings are all specified.

```bash
workato exec connection.authorization.acquire --connector='zoominfo.rb' --settings='settings.yaml' --connection='My Valid Connection' --verbose
```

Invoke the test lambda. Connector and settings are all specified.

```bash
workato exec test --connector='zoominfo.rb' --settings='settings.yaml' --connection='My Valid Connection' --verbose
```

Invoke a specific action and pass it inputs.

```bash
$ workato exec actions.search_customers.execute --input='input/search_customer_input.json' --verbose
```

Invoke a specific polling trigger and pass it inputs. This command simulates the trigger paginating through a series of records when `can_poll_more` is set to `true` in the closure.

```bash
$ workato exec triggers.new_updated_customers.poll --input='input/new_updated_customers_input.json' --verbose
```

Invoke a specific polling trigger and pass it inputs. Output will be a single page of the poll. This command simulates a single trigger poll and returns only the first page.

```bash
$ workato exec triggers.new_updated_customers.poll_page --input='input/new_updated_customers_input.json' --verbose
```

* * *

## workato generate

Generates Workato schema based on a given JSON or CSV or tests based on a given connector

### Usage

```bash
$ workato generate <SUBCOMMAND>
```

### Input

| Input | Description |
| --- | --- |
| **SUBCOMMAND** | The specific asset to be generated. Either \`schema\` or \`test\`. |

* * *

## workato generate schema

Takes a given JSON or CSV file and converts it into Workato Schema for use in your connector

### Usage

```bash
$ workato generate schema --api-token <API-TOKEN> <OPTIONS>
```

### Options

| Option | Description |
| --- | --- |
| **\--json** | The path to the JSON file to convert into Workato Schema |
| **\--csv** | The path to the CSV file to convert into Workato Schema |
| **\--col-sep** | The column separators in the CSV file provided. Default: comma. Possible values: comma, space, tab, colon, semicolon, pipe |
| **\--api-email** | DEPRECATED. API email and keys authentication has been succeeded with API Client authentication that is more secure. [Learn how to create an API client](https://docs.workato.com/workato-api/api-clients.html#api-clients). New versions of the SDK Gem will support deprecated API email and keys until 2023. |
| **\--api-token** | REQUIRED. The API token of an API client with the proper permissions. API email and keys authentication has been succeeded with API Client authentication that is more secure. [Learn how to create an API client](https://docs.workato.com/workato-api/api-clients.html#api-clients). Required API Client permissions: POST /api/sdk/generate\_schema/csv, POST /api/sdk/generate\_schema/json |

### Examples

Convert sample JSON payload to Workato schema

```bash
$ workato generate schema --api-token --json='fixtures/actions/search_customers/input.json'
```

Convert sample pipe delimited CSV file to Workato schema with

```bash
$ workato generate schema --api-token --csv='fixtures/actions/report/input.csv' --col-sep=pipe
```

* * *

## workato generate test

Takes a given connector and generates RSpec tests for specified features.

### Usage

```bash
$ workato generate test <OPTIONS>
```

### Options

| Option | Description |
| --- | --- |
| **\-c or --connector** | The path to the connector.rb file to execute. Defaults to connector.rb if not provided. |
| **\-a or --action** | The name of the specific Action to generate tests for. Generates tests for all features if not specified. |
| **\-t or --trigger** | The name of the specific Trigger to generate tests for. Generates tests for all features if not specified. |
| **\-p or --pick-list** | The name of the specific picklist to generate tests for. Generates tests for all features if not specified. |
| **\-o or --object-definition** | The name of the specific object\_definition to generate tests for. Generates tests for all features if not specified. |
| **\-m or --method** | The name of the specific method to generate tests for. Generates tests for all features if not specified. |

### Examples

Generate skeletal tests for all connector features

```bash
$ workato generate test
```

Generate skeletal tests for specific action

```bash
$ workato generate test action=get_customers
```

* * *

## workato help

Displays help for a specified SDK gem command.

### Usage

```bash
$ workato help <COMMAND>
```

### Input

| Input | Description |
| --- | --- |
| **COMMAND** | The command which you want to help displayed for. For example: `edit` |

### Output

Elaborated help for the specified SDK gem command.

### Example

```bash
$ workato help edit
Usage:
  workato edit PATH

Options:
  -k, [--key=KEY]                  # Path to file with encrypt/decrypt key. NOTE: key from WORKATO_CONNECTOR_MASTER_KEY has higher priority
      [--verbose], [--no-verbose]

Edit encrypted file, e.g. settings.yaml.enc
```

* * *

## workato new

Creates a new connector project in your chosen directory.  
  
When you create a new connector project, you will be asked if you want to select `secure` or `simple` for your HTTP mocking behavior:

```bash
Please select default HTTP mocking behavior suitable for your project?

1 - secure. Cause an error to be raised for any unknown requests, all request recordings are encrypted.
            To record a new cassette you need set VCR_RECORD_MODE environment variable

            Example: VCR_RECORD_MODE=once bundle exec rspec spec/actions/test_action_spec.rb

2 - simple. Record new interaction if it is a new request, requests are stored as plain text and expose secret tokens.
```

When you select `secure`, VCR recordings made for your unit tests are encrypted. **This is recommended.** You'll need to set your environment variable for `VCR_RECORD_MODE` as well.

### Usage

```bash
$ workato new <PATH>
```

### Input

| Input | Description |
| --- | --- |
| **PATH** | The path where the connector project should be created. |

### Result

Generates a new connector project.

### Example

```bash
$ workato new ~/Desktop/my-new-connector
```

* * *

## workato oauth2

Use this to implement the OAuth2 Authorization code grant flow for applicable connectors. Applicable connectors are ones where the connection hash has \`type: 'oauth2\`. For more information, check out this handy [Okta article](https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type).

> **GEM VERSION REQUIREMENT**
> 
> The command `workato oauth2` requires SDK Gem version 0.1.2 and above.

### Usage

```bash
$ workato oauth2 <OPTIONS>
```

### Options

| Option | Description |
| --- | --- |
| **\-c or --connector** | The path to the connector source code. Defaults to `connector.rb` if not provided. |
| **\-s or --settings** | The path to the `settings.yaml` file that stores the credentials. Defaults to `settings.yaml.enc`, then `settings.yaml` if not provided. |
| **\-n or --connection** | The connection name in the `settings.yaml` file. Only required if there are multiple credential sets. |
| **\--key, -k** | The path to the encrypt/decrypt key. If this isn't provided, defaults to `master.key`. If a `master.key` file doesn't exist and no option is provided, a new `master.key` file is created. |
| **\--port** | By default, the SDK Gem spins up a webserver at "http://localhost:45555/oauth/callback" which is used to receive the OAuth callback. Use this option to change the port. i.e. --port='3010' will spin up the webserver at "http://localhost:3010/oauth/callback" This is useful when your OAuth app is configured to a specific redirect uri. |
| **\--ip** | Allows you to override the default ip address. Defaults to "127.0.0.1" |
| **\--https, --no-https** | Allows you to start the webserver with a self-signed certificate. Required in cases where the OAuth App requires a redirect uri with a "https://" prefix. |
| **\--verbose** | Include this option to make the execution verbose. This means that all HTTP requests and request payloads will be shown. Response bodies won't be shown but can be inspected with `byebug`. |

### Result

Emulates the OAuth2 Authorization Code Grant Flow on Workato. Applicable connectors are ones where the connection hash has \`type: 'oauth2\`. For more information, check out this handy [Okta article](https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type).

### Example

```bash
$ workato oauth2
```

* * *

## workato push

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

Creates a new connector project in your chosen Workato folder.

> **PUSH TO A SPECIFIC FOLDER**
> 
> The `workato push` command does not push to a specific folder in your Workato workspace unless you use the `--folder` parameter. For example: `workato push --folder <folder ID>`.

### Usage

```bash
$ workato push --api-token <API-TOKEN> <OPTIONS>
```

### Options

| Option | Description |
| --- | --- |
| **\--api-email** | DEPRECATED. API email and keys authentication has been succeeded with API Client authentication that is more secure. [Learn how to create an API client](https://docs.workato.com/workato-api/api-clients.html#api-clients). New versions of the SDK Gem will support deprecated API email and keys until 2023. |
| **\--api-token** | REQUIRED. The API token of an API client with the proper permissions. API email and keys authentication has been succeeded with API Client authentication that is more secure. [Learn how to create an API client](https://docs.workato.com/workato-api/api-clients.html#api-clients). Required API Client permissions: GET /api/users/me, GET /api/packages/:id, POST /api/packages/import/:id |
| **\--folder** | The ID of the folder in your Workato workspace where you plan to push the connector. By default, the connector is not pushed to a specific folder unless you add the `--folder` parameter and folder ID. Folder IDs are located in the URL when you're viewing the folder. For example: if the URL is `https://app.workato.com/?fid=106070#assets`, the folder ID is `106070`. |
| **\-t or --title** | The title of your connector. Defaults to the title key in your connector code if not provided. |
| **\-d or --description** | The path to your connector's description, which could be a Markdown or plain text file. Defaults to `README.md` if not provided. |
| **\-l or --logo** | The link to the `png` or `jpeg` of your connector's logo. Defaults to `logo.png` if not provided. |
| **\-n or --notes** | The version notes attached to this uploaded version. |
| **\-c or --connector** | The path to the connector source code. Defaults to `connector.rb` if not provided. |
| **\--environment** | Use this data center-specific URL to push connector code. Defaults to the WORKATO\_BASE\_URL environment variable if not set. For example: - \`https://app.workato.com\` - \`https://app.eu.workato.com\` - \`https://app.jp.workato.com\` - \`https://app.sg.workato.com\` - \`https://app.au.workato.com\` - \`https://app.il.workato.com\` - \`https://app.workatoapp.cn\` - \`https://app.kr.workato.com\` - \`https://app.uk.workato.com\` - \`https://app.trial.workato.com\` |

### Example

```
workato push --api-token
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/reference/rspec-commands.md
description: >-
  Reference for setting up RSpec tests for SDK connectors, including creating
  connector and settings instances to run connector lambdas.
---

# RSpec Reference

Design tests to validate that your connectors can support day-to-day business and user scenarios and ensure the system is sufficient and correct for business usage.

## RSpec basic setup

In summary, the steps for any set of RSpec tests would be to:

1. Create a connector instance
2. Create a settings instance
3. Run related RSpec commands using your connector and settings instance.

```ruby
RSpec.describe 'methods/user_tenants', :vcr do
  let(:connector) { Workato::Connector::Sdk::Connector.from_file('connector.rb', settings) }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }

  subject(:result) { connector.methods.user_tenants(arg_1) }

  context 'when invoked' do
    ... # RSpec tests
  end
end
```

First, you will need to instantiate an instance of your connector using the Gem. This instance of your connector will then be used to call further commands to execute lambdas in your connector. This is the `let(:connector) ...` part of the sample above.

Second, you will also need to instantiate an instance of a connection. Think of this as an actual connection on Workato. Both the instance of your connector and instance of your settings will work together to ensure we can send valid HTTP requests whilst running RSpec. This is the `let(:settings) ...` part of the sample above.

Subsequently, the RSpec commands are provided in the `context` attribute.

## Creating a connector instance

### `from_file`

Instantiates a connector instance which can be used in your RSpec tests. This is the basic building block for any RSpec tests.

| Attribute | Description |
| --- | --- |
| Purpose | Instantiate a connector instance |
| Input | `path_to_file` - The path to the connector in your tests. `settings` - The path to the settings file. Used to instantiate a connector with a settings file preloaded. This is import |
| Output | Connector instance which can be used |
| Usage | `Workato::Connector::Sdk::Connector.from_file('connector.rb', settings)` |

* * *

## Creating a settings instance

There are 3 ways to create a settings instance.

1. [From the default file](#from-default-file)
2. [From a specified file](#from-file)
3. [From an encrypted file](#from-encrypted-file)

### `from_default_file`

Use this in most cases when you want to instantiate a settings instance to be used in your RSpec tests. This is the basic building block for any RSpec tests as well! This can be used for both encrypted and unencrypted files.

> **Do not use named connections**
> 
> Your settings file should not have named connections. In other words, there must only be one set of credentials. For example this is correct
> 
> ```yaml
> api_key: valid_api_key
> domain: valid_domain
> ```
> 
> This would be incorrect
> 
> ```yaml
> My Valid Connection:
>    api_key: valid_api_key
>    domain: valid_domain
> My invalid Connection:
>    api_key: invalid_api_key
>    domain: valid_domain
> ```

| Attribute | Description |
| --- | --- |
| Purpose | Instantiate a settings instance to be used with your connector instance. |
| Input | N/A |
| Output | settings instance which can be used |
| Usage | `Workato::Connector::Sdk::Settings.from_default_file` |

> **TIP**
> 
> When you use this, we first look for a `settings.yaml.enc` file as well as `master.key` file in the root directory where you are calling. If no `settings.yaml.enc` file can be found, we then default to your `setting.yaml` file.

### `from_file`

Instantiates a settings instance which can be used in your RSpec tests. This is the basic building block for any RSpec tests as well!

**Use this for unencrypted settings.yaml files!**

| Attribute | Description |
| --- | --- |
| Purpose | Instantiate a settings instance to be used with your connector instance. **Used for unencrypted settings.yaml files!** |
| Input | `path` - The path to the settings file. `name` - The name of the connection if there are multiple in your settings.yaml file |
| Output | settings instance which can be used |
| Usage | `Workato::Connector::Sdk::Settings.from_file('settings.yaml')` |

### `from_encrypted_file`

Instantiates a settings instance which can be used in your RSpec tests. This is the basic building block for any RSpec tests as well!

**Use this for encrypted settings.yaml.enc files!**

| Attribute | Description |
| --- | --- |
| Purpose | Instantiate a settings instance to be used with your connector instance. **Used for encrypted settings.yaml.enc files!** |
| Input | `path` - The path to the settings file. `name` - The name of the connection if there are multiple in your settings.yaml file `key` - The path to your `master.key` used to decrypt the `settings.yaml.enc` file. |
| Output | settings instance which can be used |
| Usage | `Workato::Connector::Sdk::Settings.from_encrypted_file('settings.yaml.enc', 'master.key')` |

* * *

## Testing your connection and test lambdas

Use `connector.connection.[path](settings)` to trigger the various lambdas in `connector_spec.rb`.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the various lambdas in your connection hash. |
| Input | `settings` - Your settings instance |
| Output | The output of various lambdas |
| Usage | `connector.connection.[path](settings)` e.g. `connector.connection.authorization.acquire` or `connector.connection.authorization.base_uri` |

You can also use `connector.test(settings)` to trigger the test lambda in `connector_spec.rb`.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the test lambda in your connector. |
| Input | `settings` - Your settings instance |
| Output | The output of your test lambda |
| Usage | `connector.test(settings)` |

> **WARNING**
> 
> When executing RSpec for your test lambda, keep in mind that any tokens retrieved from the `acquire` or `token_url` lambdas should already be updated in the settings file and valid. RSpec does not support the token refresh flow that happens when you run `workato exec test` via the CLI.

#### Example RSpec test - testing your connection and test lambda

```ruby
RSpec.describe 'connector', :vcr do
  let(:connector) { Workato::Connector::Sdk::Connector.from_file('connector.rb', settings) }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }

  it { expect(connector).to be_present }

  describe 'connection' do
    # Assign the output variable as the output of your test lambda
    subject(:output) { connector.connection.authorization.acquire(settings) }

    context 'given valid credentials' do
      it 'successfully retrieves token' do
        expect(output).to be_truthy
      end
    end
  end

  describe 'test' do
    # Assign the output variable as the output of your test lambda
    subject(:output) { connector.test(settings) }

    context 'given valid credentials' do
      it 'establishes valid connection' do
        expect(output).to be_truthy
      end

      it 'returns response that is not excessively large' do
        # large Test responses might also cause connections to be evaluated wrongly
        expect(output.to_s.length).to be < 5000
      end
    end

    context 'given invalid credentials' do
      let(:settings) { Workato::Connector::Sdk::Settings.from_encrypted_file('invalid_settings.yaml.enc') }

      it 'establishes invalid connection' do
        expect { output }
          .to raise_error('500 Internal Server Error')
      end
    end
  end
end
```

* * *

## Testing your actions

After the [basic RSpec setup](#rspec-basic-setup), you can call various lambdas in your connector. This is done by calling instance methods on your connector instance.

You can use the CLI command `workato generate test` to automatically generate stubs in your spec folder. Each action will get its own spec file.

### Testing your entire action

To test your entire action including schema, you simply need to make it the subject of your RSpec test by refering `subject(:output) { connector.actions.[action_name](input) }`

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the entire action of a specific connector including any related schema conversions, toggle fields. |
| Input | `input` - The JSON representation of the input json provided directly to the action from the recipe editor. |
| Output | The output of your action |
| Usage | `connector.actions.[action_name](input)` or `connector.actions.[action_name].invoke(input)` |

#### Example RSpec test - testing your entire action

```ruby
RSpec.describe "actions/search_customers", :vcr do

  # Spec describes the most commons blocks of an action. Remove describes that you don"t need.
  # Ref: https://docs.workato.com/developing-connectors/sdk/cli/guides/cli/actions.html for test examples

  subject(:output) { connector.actions.search_customers(input) }

  let(:connector) { Workato::Connector::Sdk::Connector.from_file("connector.rb") }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }
  let(:input) { JSON.parse(File.read('fixtures/actions/search_customers/input.json')) }

  let(:expected_output) { JSON.parse(File.read('fixtures/actions/search_customers/output.json')) }

  describe 'Run entire action with valid input' do
    it 'gives expected output' do
      expect(output).to eq(expected_output)
    end
  end
end
```

### Testing your execute lambda

Use `execute(**args)` to trigger a specific action in your connector instance.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the execute lambda of a specific connector |
| Input | `settings` - Your settings instance `input` - The JSON representation of the input argument provided to your execute lambda. `extended_input_schema` - The JSON representation of the extended input schema argument provided to your execute lambda. `extended_output_schema` - The JSON representation of the extended output schema argument provided to your execute lambda. NOTE: if these arguments aren't needed, you needn't define them. |
| Output | The output of your execute lambda |
| Usage | `connector.actions.[action_name].execute(settings, input, extended_input_schema, extended_output_schema)` |

#### Example RSpec test - testing your execute lambda

```ruby
RSpec.describe "actions/search_customers", :vcr do

  # Spec describes the most commons blocks of an action. Remove describes that you don"t need.
  # Ref: https://docs.workato.com/developing-connectors/sdk/unit-testing.html#action for test examples

  let(:connector) { Workato::Connector::Sdk::Connector.from_file("connector.rb") }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }

  let(:action) { connector.actions.search_customers }

  describe "execute" do
    subject(:output) { action.execute(settings, input) }
    let(:input) { JSON.parse(File.read('input/search_customer_input.json')) }
    let(:expected_output) { JSON.parse(File.read('output/search_customer_output.json')) }

    context 'given valid input' do
      it 'gives expected output' do
        expect(output).to eq(expected_output)
      end
    end
  end
end
```

### Testing your input\_fields lambda

Use `input_fields(**args)` to invoke the input\_fields lambda in a specific action in your connector instance.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the input\_fields lambda of a specific connector |
| Input | `settings` - Your settings instance `config_fields` - The JSON representation of any config field values passed from the `config_fields` lambda. NOTE: if these arguments aren't needed, you needn't define them. |
| Output | The output of your input\_fields lambda |
| Usage | `connector.actions.[action_name].input_fields(settings, config_fields)`) |
|  |  |

> **TIP**
> 
> You don't need to explicitly pass the `object_definitions` argument because it's automatically available from your connector instance.

### Testing your output\_fields lambda

Use `output_fields(**args)` to invoke the output\_fields lambda in a specific action in your connector instance.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the output\_fields lambda of a specific connector |
| Input | `settings` - Your settings instance `config_fields` - The JSON representation of any config field values passed from the `config_fields` lambda. NOTE: if these arguments aren't needed, you needn't define them. |
| Output | The output of your output\_fields lambda |
| Usage | `connector.actions.[action_name].output_fields(settings, config_fields)` |

> **TIP**
> 
> You don't need to explicitly pass the `object_definitions` argument because it's automatically available from your connector instance.

### Testing your sample\_output lambda

Use `sample_output(**args)` to invoke the sample\_output lambda in a specific action in your connector instance.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the sample\_output lambda of a specific connector |
| Input | `settings` - Your settings instance `input` - The JSON representation of the input argument provided to your execute lambda. NOTE: if these arguments aren't needed, you needn't define them. |
| Output | The output of your sample\_output lambda |
| Usage | `connector.actions.[action_name].sample_output(settings, input)` |

### Other action instance methods available:

- `summarize_input(**args)`
- `summarize_output(**args)`

* * *

## Testing your triggers

After the [basic RSpec setup](#rspec-basic-setup), you can call various lambdas in your connector. This is done by calling instance methods on your connector instance.

You can use the CLI command `workato generate test` to automatically generate stubs in your spec folder. Each trigger will get its own spec file.

Note that each trigger stub will have all possible lambdas for both webhooks and polling triggers. You will need to remove as needed.

### Testing your entire trigger

To test your entire trigger including schema, you simply need to make it the subject of your RSpec test by refering `subject(:output) { connector.triggers.[trigger_name](input) }`

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the entire trigger poll of a specific connector including any related schema conversions, toggle fields. |
| Input | `input` - The JSON representation of the input json provided directly to the action from the recipe editor. |
| Output | The output of your trigger including any schema conversions |
| Usage | `connector.triggers.[trigger_name](input)` or `connector.triggers.[trigger_name].invoke(input)` |

#### Example RSpec test - testing your entire action

```ruby
RSpec.describe "triggers/new_updated_object", :vcr do

  # Spec describes the most commons blocks of a trigger.
  # Depending on the type of your trigger remove describes that you don't need.
  # Learn more: https://docs.workato.com/developing-connectors/sdk/cli/reference/rspec-commands.html

  subject(:output) { connector.triggers.new_updated_object(input) }

  let(:connector) { Workato::Connector::Sdk::Connector.from_file("connector.rb") }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }
  let(:input) { JSON.parse(File.read('fixtures/triggers/new_updated_object/input.json')) }

  let(:expected_output) { JSON.parse(File.read('fixtures/triggers/new_updated_object/output.json')) }

  describe 'Run entire trigger with valid input' do
    it 'gives expected output' do
      expect(output).to eq(expected_output)
    end
  end
end
```

### Testing your poll lambda

Use `poll(**args)` to invoke the poll lambda in a specific trigger in your connector instance. This will retrieve paginated records for all events in the given time period, specified by the `since` input. See an example of a [paginated poll lambda](/en/developing-connectors/sdk/cli/guides/cli/triggers#running-your-poll-lambda-with-pagination).

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the poll lambda of a specific trigger in your connector and paginates |
| Input | `settings` - Your settings instance `input` - The JSON representation of the input argument provided to your execute lambda. `closure` - The JSON representation of a closure that may be passed from a previous invocation of the `poll` lambda. NOTE: if these arguments aren't needed, you needn't define them. |
| Output | The output of your poll lambda |
| Usage | `connector.triggers.[trigger_name].poll(settings, input, closure)` |

> **How this works**
> 
> This instance method simulates Workato's polling mechanism on the platform **including the pagination that might occur due to your `can_poll_more` attribute being `true`.** This is collected into a single output from multiple polls. For example: if the 1st poll's output is
> 
> ```ruby
> {
>   events: [
>     { 'id' => 2, 'title' => 'Post #2' },
>     { 'id' => 1, 'title' => 'Post #1' }
>   ],
>   next_poll: 2,
>   can_poll_more: true
> }
> ```
> 
> and the 2nd polls output is
> 
> ```ruby
> {
>   events: [
>     { 'id' => 4, 'title' => 'Post #4' },
>     { 'id' => 3, 'title' => 'Post #3' },
>   ],
>   next_poll: 4,
>   can_poll_more: false
> }
> ```
> 
> The final output of this method is
> 
> ```ruby
> {
>   events: [
>     { 'id' => 4, 'title' => 'Post #4' },
>     { 'id' => 3, 'title' => 'Post #3' },
>     { 'id' => 2, 'title' => 'Post #2' },
>     { 'id' => 1, 'title' => 'Post #1' }
>   ],
>   next_poll: 4,
>   can_poll_more: false
> }
> ```

### Testing your poll\_page lambda

Use `poll_page(**args)` to invoke the poll lambda in a specific trigger in your connector instance. This will only retrieve a single page, even if there are more events.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the poll lambda of a specific trigger in your connector and does not paginate |
| Input | `settings` - Your settings instance `input` - The JSON representation of the input argument provided to your execute lambda. `closure` - The JSON representation of a closure that may be passed from a previous invocation of the `poll` lambda. NOTE: if these arguments aren't needed, you needn't define them. |
| Output | The output of your poll lambda |
| Usage | `connector.triggers.[trigger_name].poll_page(settings, input, closure)` |

> **TIP**
> 
> This simulates a **single** poll given a specified closure. This instance method will not poll multiple times.

### Testing your webhook\_subscribe lambda

Use `webhook_subscribe(**args)` to invoke the webhook\_subscribe lambda in a specific trigger in your connector instance.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the webhook\_subscribe lambda of a specific trigger in your connector |
| Input | `webhook_url` - The webhook url passed as an argument. You may stub this with a request.bin url. `settings` - Your settings instance `input` - The JSON representation of the input argument provided to your webhook\_subscribe lambda. `recipe_id` - The simulated recipe ID. If not given, we default to a UUID. |
| Output | The output of your webhook\_subscribe lambda |
| Usage | `connector.triggers.[trigger_name].webhook_subscribe(webhook_url, settings)` |

### Testing your webhook\_unsubscribe lambda

Use `webhook_unsubscribe(**args)` to invoke the webhook\_unsubscribe lambda in a specific trigger in your connector instance.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the webhook\_unsubscribe lambda of a specific trigger in your connector |
| Input | `subscribe_output` - The JSON representation of the output of the `webhook_subscribe` lambda. |
| Output | The output of your webhook\_unsubscribe lambda |
| Usage | `connector.triggers.[trigger_name].webhook_unsubscribe(subscribe_output)` |

### Testing your webhook\_notification lambda

Use `webhook_notification(**args)` to invoke the webhook\_notification lambda in a specific trigger in your connector instance.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke the webhook\_notification lambda of a specific trigger in your connector |
| Input | `input` - The JSON representation of the input argument provided to your webhook\_subscribe lambda. `payload` - The webhook payload. You should pass an expected webhook payload to test. `extended_input_schema` - The JSON representation of the extended input schema argument provided to your execute lambda. `extended_output_schema` - The JSON representation of the extended output schema argument provided to your execute lambda. `header` - The webhook headers. `params` - The webhook query params . NOTE: if these arguments aren't needed, you needn't define them. |
| Output | The output of your webhook\_notification lambda |
| Usage | `connector.triggers.[trigger_name].webhook_notification(input, payload, extended_input_schema, extended_output_schema, header, params)` |

### Other trigger instance methods available:

- [input\_fields](#testing-your-input-fields-lambda)
- [output\_fields](#testing-your-output-fields-lambda)
- [sample\_output](#testing-your-sample-output-lambda)
- `summarize_input(**args)`
- `summarize_output(**args)`
- `dedup`

* * *

## Testing your method lambda

Use `connector.methods.<method_name>(**args)` to trigger the your method lambdas in `connector_spec.rb`.

After the [basic RSpec setup](#rspec-basic-setup), you can call various lambdas in your connector. This is done by calling instance methods on your connector instance.

You can use the CLI command `workato generate test` to automatically generate stubs in your spec folder. Each method will get its own spec file.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke a specific method lambda in your connector. |
| Input | **Configurable. Depends on your method** |
| Output | The output of your method lambda |
| Usage | `connector.methods.<method_name>(**args)`) |

#### Example RSpec test - testing your method lambda

```ruby
# frozen_string_literal: true

RSpec.describe "methods/make_schema_builder_fields_sticky", :vcr do
  let(:connector) { Workato::Connector::Sdk::Connector.from_file("connector.rb", settings) }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }

  subject(:result) { connector.methods.make_schema_builder_fields_sticky(schema) }

  context "given non-sticky schema" do
    let(:schema) { JSON.parse(File.read('fixtures/methods/make_schema_builder_fields_sticky/make_schema_builder_fields_sticky_input.json')) }
    let(:expected_output) { JSON.parse(File.read('fixtures/methods/make_schema_builder_fields_sticky/make_schema_builder_fields_sticky_output.json')) }
    it "makes all fields sticky" do
      expect(result).to eq(expected_output)
    end
  end
end
```

* * *

## Testing your object\_definitions lambda

Use `[object_definition_name].fields(**args)` to trigger the your object\_definitions lambdas in `connector_spec.rb`.

You can use the CLI command `workato generate test` to automatically generate stubs in your spec folder. Each object\_definitions lambda will get its own spec file.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke a specific object\_definitions lambda in your connector. |
| Input | `settings` - Your settings instance `config_fields` - The JSON representation of your `config_fields`. |
| Output | The output of your object\_definitions lambda |
| Usage | `connector.object_definitions.[object_definition_name].fields(settings, config_fields)` |

#### Example RSpec test - testing your object\_definition lambda

```ruby
# frozen_string_literal: true

RSpec.describe "object_definition/compound_type", :vcr do
  let(:connector) { Workato::Connector::Sdk::Connector.from_file("connector.rb", settings) }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }

  let(:object_definition) { connector.object_definition.compound_type }

  context 'Given event config input' do
    subject(:schema_fields) { object_definition.fields(settings, config_fields) }
    let(:config_fields) { { type: :event } }
    let(:expected_schema) { JSON.parse(File.read('fixtures/object_definitions/compound_type/definition_event.json')) }

    it 'returns schema definition' do
      expect(schema_fields).to be_kind_of(Array)
      expect(schema_fields).to match_array(expected_schema)
    end
  end
end
```

* * *

## Testing your pick\_lists lambda

Use `connector.pick_lists.<pick_list_name>(settings, **args)` to trigger the your pick\_lists lambdas in `connector_spec.rb`.

You can use the CLI command `workato generate test` to automatically generate stubs in your spec folder. Each pick\_lists lambda will get its own spec file.

| Attribute | Description |
| --- | --- |
| Purpose | Invoke a specific pick\_lists lambda in your connector. |
| Input | `settings` - Your settings instance **Configurable. Depends on your pick\_list arguments** |
| Output | The output of your pick\_lists lambda |
| Usage | `connector.pick_lists.<pick_list_name>(settings, **args)` |

#### Example RSpec test - testing your pick\_lists lambda

```ruby
# frozen_string_literal: true

RSpec.describe "pick_lists/events", :vcr do
  let(:connector) { Workato::Connector::Sdk::Connector.from_file("connector.rb", settings) }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }

  subject(:pick_list) { connector.pick_lists.events(settings, config_fields) }


  context 'Given configuration parameter' do
    let(:config_fields) { { type: :city } }
    let(:expected_picklist) { JSON.parse(File.read('fixtures/pick_lists/events/pick_list_city.json')) }

    it 'returns schema definition' do
      expect(pick_list).to be_kind_of(Array)
      expect(pick_list).to match_array(expected_picklist)
    end
  end
end
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/reference/cli-project-directory-reference.md
description: >-
  Reference for the files and folders in an SDK connector project, including
  connector.rb, fixtures, Gemfile, and master.key.
---

# SDK - Project Directory and File Reference

A typical connector project built with the SDK gem usually looks something like this:

```
. # root
├── connector.rb
├── fixtures
├── Gemfile
├── Gemfile.lock
├── logo.png
├── master.key
├── README.md
├── settings.yaml.enc
├── spec
|   ├── connector_spec.rb
|   └── spec_helper.rb
├── tape_library
├── .github
├── .gitignore
└── .rspec
```

An overview of what each file or directory does:

| File/directory | Created | Description |
| --- | --- | --- |
| **connector.rb** | Via workato new | Stores the actual connector code. This should be a replica of your connector code in Workato. |
| **fixtures** | Via workato new | Stores input and output JSON files for RSpec or CLI. See an example file in the [fixtures section](#fixtures). |
| **Gemfile** | Via workato new | Declares the gems (dependencies) required by the project. These are required to run RSpec. See an example file in the [Gemfile section](#gemfile). |
| **Gemfile.lock** | Via workato new | Stores gem dependency data, including versions and dependencies of dependencies. This file is automatically created when your project is built. |
| **logo.png** | By you | Your connector's logo. When synced with your Workato workspace via [`workato push`](/developing-connectors/sdk/cli/reference/cli-commands.html#workato-push), this will be used as the default for your connector's logo image. |
| **master.key** | Via workato new | Stores the encryption key used to encrypt your files. These files can include credentials and other sensitive data, such as environment properties. **Note**: Created only if `secure` was selected during project setup. |
| **README.md** | By you | Used to document what your connector does and how to use it. When synced with your Workato workspace via [`workato push`](/developing-connectors/sdk/cli/reference/cli-commands.html#workato-push), this will be used as the default file for your connector's description. |
| **settings.yaml.enc or settings.yaml** |  | Stores credentials used for testing the connector. See an example file in the [settings.yaml section](#settings-yaml-enc-settings-yaml). **Note**: If `secure` was selected during project setup, this will be a `.yaml.enc` file. Otherwise, this will be a `.yaml` file. |
| **spec** | Via workato new | Stores RSpec test files. [RSpec](/developing-connectors/sdk/cli/guides/rspec/vcr.html) is a Ruby testing tool that can be used in conjunction with the [SDK gem](/developing-connectors/sdk/cli.html) to define, write, and run unit tests for your connector. |
| **spec/connector\_spec.rb** | Via workato new | Stores all unit test for the connector. This is the main RSpec file. See an example file in the [connector\_spec.rb section](#connector-spec-rb). This file may be split into multiple files or folders if it helps you organize your tests. All spec tests can be run using the `bundle exec rspec` command. |
| **spec/spec\_helper.rb** | Via workato new | Stores all commands that should be set up prior to each RSpec run. See an example file in the [spec\_helper.rb section](#spec-helper-rb). |
| **tape\_library** | via RSpec | Stores [VCR cassettes](https://relishapp.com/vcr/vcr/v/6-0-0/docs/cassettes/cassette-format), which are files that contain all info about recorded API requests and subsequent responses. These requests are essential for stable unit tests. Check out the [VCR docs](https://relishapp.com/vcr/vcr/docs) to learn more. |
| **.github** | By you | **Applicable if using GitHub.** Stores information about your GitHub action workflows. |
| **.gitignore** | Via workato new | Stores the names of files and/or directories that shouldn't be pushed to Git. See an example file in the [.gitignore section](#gitignore). **Note**: If your project has a `master.key`, it should be added to this file as per our [security best practices](/developing-connectors/sdk/cli/guides/security-guidelines.html). |
| **.rspec** | Via workato new | Stores standard options to pass to RSpec when run. Some example flags: `--format documentation` - Allows tests to be grouped, `--color` - Enables coloring in the RSpec output, `--require spec_helper` - Tells RSpec runs to require `spec_helper.rb` prior to every run |

* * *

## connector\_spec.rb

Created when `workato new` is run, the `connector_spec.rb` file contains the unit tests for your connector.

An example file might look something like this:

```ruby
# frozen_string_literal: true

RSpec.describe 'connector', :vcr do
  let(:connector) { Workato::Connector::Sdk::Connector.from_file('connector.rb', settings) }
  let(:settings) { Workato::Connector::Sdk::Settings.from_default_file }

  it { expect(connector).to be_present }

  describe 'test' do
    subject(:output) { connector.test(settings) }

    context 'given valid credentials' do
      it 'establishes valid connection' do
        expect(output).to be_truthy
      end

      it 'returns response that is not excessively large' do
        # large Test responses might also cause connections to be evaluated wrongly
        expect(output.to_s.length).to be < 5000
      end
    end

    context 'given invalid credentials' do
      let(:settings) { Workato::Connector::Sdk::Settings.from_encrypted_file('invalid_settings.yaml.enc'}

      it 'establishes invalid connection' do
        expect { output }
          .to raise_error('500 Internal Server Error')
      end
    end
  end
end
```

You can also use [`workato generate test`](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-generate) to generate RSpec test stubs for you. This handles most of the heavy lifting, such as such as instantiating your connector or settings.

It's ultimately up to you how you want to write your unit tests. If you'd like some help getting started, [check out this tutorial](https://semaphoreci.com/community/tutorials/getting-started-with-rspec).

* * *

## fixtures

The `/fixtures` folders are used to store the input and output JSON files used to test parts of your connector. This includes actions, triggers, methods, and so on.

**Input** JSON files should be created and formed manually. You can design them yourself, or use the Cloud SDK's **Test code** tab to build them.

**Output** JSON files can be created from CLI commands by including the `--output` option. For example:

```shell
workato exec <PATH> --output
```

Your `/fixtures` folder might look something like this:

```shell
├── fixtures
│   ├── actions
│   │   └── search_customers
│   │       ├── input.json
│   │       └── output.json
│   ├── methods
│   │   └── sample_method
│   │       ├── input.json
│   │       └── output.json
│   ├── pick_lists
│   │   └── dependent
│   │       └── input.json
│   └── triggers
│       └── new_updated_object
│           ├── customer_config.json
│           ├── customer_input_poll.json
│           ├── customer_input_poll_page.json
│           ├── customer_output_fields.json
│           ├── customer_output_poll.json
│           └── customer_output_poll_page.json
```

* * *

## GEMFILE

```ruby
# frozen_string_literal: true

source 'https://rubygems.org'

gem 'rspec'
gem 'vcr'
gem 'workato-connector-sdk'
gem 'webmock'
gem 'timecop'
gem 'byebug'
gem 'rubocop' # Only if you want to use rubocop. Not added by default.
```

* * *

## settings.yaml.enc, settings.yaml

The `settings.yaml.enc`/`settings.yaml` file stores credentials used for testing. Data in this file must be valid YAML.

### Single credential set

If you only have one set of credentials, they can be defined at the root level:

```yaml
api_key: valid_key
domain: valid_domain
```

### Multiple credential sets

If you have multiple sets of credentials, your settings file should be structured similarly to the following:

```yaml
[one_connection_name]:
  api_key: valid_key
  domain: valid_domain
[second_connection_name]:
  api_key: invalid_key
  domain: invalid_domain
```

* * *

## spec\_helper.rb

Created when `workato new` is run, the `spec_helper.rb` file stores common attributes to be used in RSpec runs.

This file should require, at a minimum:

- `'bundler/setup'`
- `'workato-connector-sdk'`
- `'json'`

Learn more about additional RSpec configuration [here in the RSpec repository](https://github.com/rspec/rspec-core).

The following example shows the `spec_helper.rb` file that's created when the `secure` HTTP mocking behavior is selected for a project.

This file will encrypt all VCR recordings using the project's `master.key`.

However, by default the record mode for `secure` is `none`. This means that no new VCR cassettes will be recorded. To change this behavior, the `VCR_RECORD_MODE` environment variable to `once`.

```ruby
# frozen_string_literal: true

require 'bundler/setup'
require 'json'
require "webmock/rspec"
require "timecop"
require "vcr"
require "workato-connector-sdk"
require "workato/testing/vcr_encrypted_cassette_serializer"
require "workato/testing/vcr_multipart_body_matcher"

RSpec.configure do |config|
  # Enable flags like --only-failures and --next-failure
  config.example_status_persistence_file_path = ".rspec_status"

  # Disable RSpec exposing methods globally on `Module` and `main`
  config.disable_monkey_patching!

  config.expect_with :rspec do |c|
    c.syntax = :expect
  end
end

VCR.configure do |config|
  config.cassette_library_dir = "tape_library"
  config.hook_into :webmock
  config.cassette_serializers[:encrypted] = Workato::Testing::VCREncryptedCassetteSerializer.new
  config.register_request_matcher :headers_without_user_agent do |request1, request2|
    request1.headers.except("User-Agent") == request2.headers.except("User-Agent")
  end
  config.register_request_matcher :multipart_body do |request1, request2|
    Workato::Testing::VCRMultipartBodyMatcher.call(request1, request2)
  end
  config.default_cassette_options = {
    record: ENV.fetch('VCR_RECORD_MODE', :none).to_sym,
    serialize_with: :encrypted,
    match_requests_on: %i[uri headers_without_user_agent body]
  }
  config.configure_rspec_metadata!
end
```

* * *

## .gitignore

The `.gitignore` file contains a list of files and/or directories that shouldn't be pushed via Git.

**Note**: If your project has a `master.key` file, you should add it to this file to ensure it isn't accidentally committed to a repository.

```
/.bundle/
/.yardoc
/_yardoc/
/coverage/
/doc/
/pkg/
/spec/reports/
/tmp/
master.key

# rspec failure tracking
.rspec_status
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/security-guidelines.md
description: >-
  Secure your local SDK connector project with sandboxes, encrypted credential
  files, and encrypted VCR recordings to protect sensitive data.
---

# Securing Your Connector Project

When you build a connector locally, you bear all responsibility for securing credentials and application access. This is especially important if you push your code to git software, like GitHub.

Sounds scary, right? It doesn't have to be!

In this guide, we'll cover some tips that will help you mitigate risks when working with credentials or other sensitive information.

## Tip 1: Always use a sandbox

Whether you're building using the SDK gem or in Workato's cloud platform, **never use a production environment when developing.** We can't stress this enough.

You could make changes that negatively impact your business or potentially expose sensitive data. For this reason, use a sandbox environment.

## Tip 2: Always use encrypted files

To ensure credentials remain secure, use encrypted files for storage.

The SDK gem includes a command that allows you to easily create and update encrypted files. This means you can encrypt your credentials, ensuring they can't be used or decrypted without your `master.key`.

To start working with encrypted files, use the [`workato edit`](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-edit) command to create the encrypted `master.key` file. If your project doesn't have this file, one will automatically be created the first time the command is run.

## Tip 3: Always use encrypted VCR recordings

VCR recordings are crucial for stable tests but also present a security risk. By default, VCR recordings record all aspects of your HTTP requests, such as tokens in headers and request or response data. If you decide to sync this data to the cloud, the best practice is to encrypt your VCR recordings.

The SDK gem makes it easy to do this when you set up your connector project.

After you run [`workato new`](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-new), select `secure` at the HTTP binding prompt:

```shell
Please select default HTTP mocking behavior suitable for your project?

1 - secure. Cause an error to be raised for any unknown requests, all request recordings are encrypted.
            To record a new cassette you need set VCR_RECORD_MODE environment variable

            Example: VCR_RECORD_MODE=once bundle exec rspec spec/actions/test_action_spec.rb

2 - simple. Record new interaction if it is a new request, requests are stored as plain text and expose secret tokens.
```

This option also creates a `spec_helper.rb` file, which comes pre-loaded with your VCR configurations and encryption. To learn more about VCR, [check out the VCR guides](/en/developing-connectors/sdk/cli/guides/rspec/vcr).

## Tip 4: Add master.key to .gitignore

If your project contains a `master.key` file - [and we strongly recommend that it does](#tip-2-always-use-encrypted-files) - it should never pushed to your Git repository.

To ensure you don't accidentally commit this file, add it to your project's `.gitignore`.

Additionally, if you need to share the info in `master.key` with your teammates, ensure you're doing so securely.

## Tip 5: Use repository secrets to store credentials in the cloud

To run your RSpec tests in the cloud while securely storing your credentials, we recommend adding secrets to your repository.

> **GITHUB SECRETS**
> 
> Secrets are encrypted environment variables that you create in an organization, repository, or repository environment. Refer to GitHub's [Encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets) documentation for additional information.

Most git platforms support adding secrets to your repository, which is where we recommend storing your `master.key` for use during RSpec testing.

---
