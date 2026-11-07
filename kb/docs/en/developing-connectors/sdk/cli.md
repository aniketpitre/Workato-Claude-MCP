---
url: 'https://docs.workato.com/en/developing-connectors/sdk/cli.md'
description: >-
  Use the Workato Connector SDK Ruby gem to develop and test connectors locally
  from the command line in your own IDE.
---

# SDK - CLI

Welcome to the SDK CLI! This section focuses on how you can use Workato's Connector SDK Ruby gem (SDK gem) to bring your connector development local.

## What is the SDK gem?

The SDK Gem is a Ruby software package that emulates how Workato would parse and execute your connector code.

The gem is:

- Easy to install
- Can be run on the command line
- Allows you to develop connectors from the comfort of your chosen IDE (integrated development environment)

## Prerequisites

To use the SDK gem, you should be familiar with:

1. The [Connector SDK](/en/developing-connectors/sdk) at an intermediate level
2. Command line tools and how to use them
3. RSpec for unit testing. Check out the [RSpec docs](https://rspec.info/documentation/) to learn more.
4. VCR. Check out this [general guide](https://dev.to/gathuku/testing-external-apis-with-vcr-in-rails-488m) to learn more about VCR, or this [getting started guide](https://relishapp.com/vcr/vcr/v/1-10-3/docs/getting-started) to dive right in.

## Benefits of using CLI

- Develop in your chosen IDE by bringing connector development local
- Enhanced debugging tools
- Improved collaboration with teammates
- Ability to implement unit tests and CI/CD processes, improving deployment stability
- Ability to implement automated deployments

## SDK gem features

Still not sure if the SDK gem is right for you? The following section describes the key differences between building a connector with the Cloud SDK **Test code** tab and the SDK gem.

|  | Cloud SDK Test code tab | SDK Gem |
| --- | --- | --- |
| **Testing specificity** | Able to test connections, actions and triggers in their entirety | Able to test specific keys of a connector separately. For example: `execute` and `output_fields` can be tested separately |
| **UI testing** | Able to test the exact look and feel of input and output fields. For example: Dynamic input and output fields | No UI, but able to quickly evaluate resultant Workato schema of input and output fields using CLI Utils |
| **Unit testing** | Not available | Able to convert CLI commands into unit tests quickly |
| **Test code tab properties and lookup tables** | No access to `account_properties` or lookup tables in Test code tab | Able to store `account_properties` and credentials in encrypted/unencrypted formats. Able to store lookup tables in unencrypted format. |

As we continue to improve on the SDK Gem and its capabilities, more features will be added.

## Connector development with the CLI

So, what does connector development look like for a team?

Below is an example process, though it could be modified to fit your team's specific needs and workflows.

![SLDC Connector with CLI](/assets/sldc_connector_cli.cT7lNBsc.png)

Let's look at this step by step:

1. **Local development.** Run your connector locally. The SDK gem's handy [CLI commands](/en/developing-connectors/sdk/cli/reference/cli-commands) can help you build, test, and debug your connector as you work.
   
2. **Test in your Workato workspace.** Ensuring functionality is important, but so is the UX of your connector. You can push your connector to your personal or team workspace, allowing you to test your connector in an actual recipe.
   
3. **Push to Git.** To collaborate with others, push your code to a Git repository. This might be GitHub, Gitlab, Bitbucket, or another provider.
   
4. **Review and test.** Review the changes made by your teammates and ensure the connector passes all unit tests.
   
5. **Automated push to DEV**. If desired, you can set up automated workflows in your repository to automatically push changes to your DEV workspace when pull requests are merged. This would allow you to trigger additional tests. For example: Recipe builders can conduct user acceptance testing to ensure the connector works as expected.
   
6. **Release to production.** Transition your connector through DEV > UAT > PROD environments through your standard recipe lifecycle management processes, ensuring that the connector - like your recipes - is fully tested before being released to production.
   

## Get started

Ready to start developing? Check out the [Getting Started](/en/developing-connectors/sdk/cli/guides/getting-started) guide to get up and running!

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/getting-started.md
description: >-
  Install the Workato SDK gem, create a connector project, set up testing, and
  push your local connector to your Workato workspace.
---

# Getting Started with the SDK Gem

In this guide, we'll show you how to:

- Install and run the SDK gem
- Create a new connector project
- Set up testing for your connector
- Push your local connector to your Workato workspace

## Prerequisites

To complete this tutorial, you'll need:

- **A Ruby version manager.** Depending on your operating system, you'll need to install a version of Ruby or a Ruby version manager.
  
  For Mac users, you can use [RVM (Ruby Version Manager)](http://rvm.io/) or another manager of your choice.
  
  For Windows users, you can use [Ruby Installer](https://rubyinstaller.org/).
  
  Refer to the [Ruby installation documentation](https://www.ruby-lang.org/en/documentation/installation/) for more information.
  
- **A supported version of Ruby**. We prefer `2.7.X`, but you can use versions `3.0.X` or `3.1.X`. If you don't have Ruby installed, [follow these instructions to install it](https://www.ruby-lang.org/en/documentation/installation/).
  
  You can verify your Ruby version by running the following command, or the appropriate command for your Ruby version manager (for example: `rvm current`):
  
  ```shell
  $ ruby -v
  ruby 2.7.X
  ```
  
  This command returns the version of Ruby currently installed on your computer. In this example, we're using `2.7.X`.
  

* * *

## Step 1: Install and run the SDK Gem

Complete the following steps to install SDK gem using the command line (CLI):

1. Run the following command to install the gem from [rubygems.org](https://rubygems.org/gems/workato-connector-sdk):
   
   ```shell
   $ gem install workato-connector-sdk
   ```
   
2. Verify that your gem is correctly installed by typing in the command `workato` in your terminal.
   
3. ```shell
   $ workato
   
   Commands:
     workato edit <PATH>            # Edit encrypted file, e.g. settings.yaml.enc
     workato exec <PATH>            # Execute connector defined block
     workato generate <SUBCOMMAND>  # Generates code from template
     workato help [COMMAND]         # Describe available commands or one specific command
     workato new <CONNECTOR_PATH>   # Inits new connector folder
     workato push <FOLDER>          # Upload and release connector's code
   
   Options:
     [--verbose], [--no-verbose]
   ```
   
     
   
   > **WINDOWS USERS ADDITIONAL INSTALLATION STEP**
   > 
   > If you use Windows, you may need to install tzinfo-data gem by running the command `gem install tzinfo-data`.
   
4. Optional. Run `gem which` to check the exact location of the gem:
   
   ```shell
   $ gem which workato-connector-sdk
   ```
   
   Additionally, you can use the [`workato`](/en/developing-connectors/sdk/cli/reference/cli-commands#workato) command to view the commands that are available during development. Find out more about individual keys by running `workato help edit`.
   

* * *

## Step 2: Create a new connector project

Now that you're all set up, let's dive into the exciting stuff: Making connectors.

1. Create a new connector project using the [`workato new`](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-new) command, replacing `<PATH>` with the path you'd like to use for the project:
   
   ```shell
   $ workato new <PATH>
   ```
   
   This creates the project in the directory you're currently in.
   
2. Complete the prompts about HTTP mocking behavior:
   
   ```shell
   Please select default HTTP mocking behavior suitable for your project?
   
   1 - secure. Cause an error to be raised for any unknown requests, all request recordings are encrypted.
               To record a new cassette you need set VCR_RECORD_MODE environment variable
   
               Example: VCR_RECORD_MODE=once bundle exec rspec spec/actions/test_action_spec.rb
   
   2 - simple. Record new interaction if it is a new request, requests are stored as plain text and expose secret tokens.
   ```
   
   Enter your choice using `1` or `2`:
   
   - `1 - secure` - **Recommended.** All HTTP requests are encrypted and recorded via VCR to ensure stability. We'll also provide you with an easy way to encrypt the recordings so credentials are not stored in plain text.
   - `2 - simple` - All HTTP requests are stored in plain text.

Refer to the [project directory reference](/en/developing-connectors/sdk/cli/reference/cli-project-directory-reference) for more info about the files the `workato new` command creates.

* * *

## Step 3: Build and test your connector

In this step, you'll build and test your connector. As how and what you build is up to you, we're only going to cover testing in this section:

- [Provide test credentials](#step-3-1-provide-test-credentials)
- [Test the connector](#step-3-2-test-the-connector)

### Step 3.1: Provide test credentials

Credentials are stored in your project's `settings.yaml.enc` or `settings.yaml` file.

1. Run the [`workato edit`](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-edit) command and replace `<EDITOR>` with your preferred editor **if you opted to encrypt your files**:
   
   Example - Mac users
   
   ```shell
   $ EDITOR="<EDITOR>" workato edit settings.yaml.enc
   ```
   
   Example - Windows users
   
   ```shell
   $ set EDITOR=notepad
   $ workato edit settings.yaml.enc
   ```
   
   When you run this command for the first time, the `settings.yaml.enc` and `master.key` files will be created.
   
2. Go to your project's `settings.yaml.enc` or `settings.yaml` file and add your credentials.
   
   We're going to use a single set of credentials for this example, so we can define them at the root level:
   
   ```yaml
   ## settings.yaml.enc
   
   api_key: [api_key]
   domain: [domain]
   ```
   
   Refer to the [settings file reference](/en/developing-connectors/sdk/cli/reference/cli-project-directory-reference#settings-yaml-enc-settings-yaml) for more info, including how to provide multiple sets of credentials.
   
3. Add `master.key` to your project's `.gitignore` or other similar file(s) **if committing your project**. This prevents your credentials from being checked into a repository, where anyone might have access to them.
   

### Step 3.2: Test the connector

Test your connector's connection, triggers, or actions with [`workato exec`](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-exec). This executes a connector's lambda block at the `PATH` you provide.

For example:

```shell
# Executes the execute block of the new_record action
$ workato exec actions.new_record.execute

# Invokes a polling trigger for the updated_record trigger
$ workato exec triggers.updated_record.poll

# Executes the get_record method with parameters from input.json
$ workato exec methods.get_record --args=input.json
```

Check out the [Running test lambda on CLI guide](/en/developing-connectors/sdk/cli/guides/cli/test) and for a detailed look testing on the CLI.

* * *

## Step 4: Push to your Workato workspace

You can push your connector code from your local environment to your Workato workspace when you're ready. Pushing to your Workato workspace allows you to test the functionality and UX of your connector to ensure you can iterate quickly. Complete the following steps to push your connector code to your Workato workspace:

1. Run the [`workato push`](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-push) command:
   
   ```shell
   $ workato push
   ```
   
2. Test in your Workato workspace. You can make changes locally and push to your Workato workspace as needed. You must supply your workspace's api-token and api-email for authorization.
   

> **API CLIENT PERMISSIONS**
> 
> This command requires you to assign a [Client role](/en/workato-api/api-clients#create-a-client-role) to the API client with the **Get details** permission enabled.
> 
> ENABLE THE GET DETAILS PERMISSION
> 
> 1. Enable permissions for your API client if you haven't done so already by going to **Workspace admin > API Clients > Client roles**.
>    
> 2. Edit an existing client role or create a new one.
>    
> 3. Go to **Admin > Workspace details > Get details**.
>    
>    ![Enable the get details permission](/assets/api-clients-get-details-permissions.DYvnCHAG.png)_Enable the Get details permission_
>    

* * *

## Step 5: Run RSpec tests for your connector

You can use unit testing to ensure that each iteration of your connector is performing as expected. Learn more about [writing test your connectors](/en/developing-connectors/sdk/cli/guides/rspec/connector_spec). Complete the following steps to run RSpec tests:

1. Ensure that your project structure is set up.
   
2. Open your CLI, go to your home directory, and run the following command:
   
   ```shell
   bundle exec rspec
   ```
   
   RSpec runs all spec files in your spec folder by default. You can run only specific tests at a time by running the following command, changing the line number (16) for your testing requirements:
   
   ```shell
   # Runs the test(s) at line 16 of your spec file.
   $ bundle exec rspec ./spec/connector_spec.rb:16
   ```
   

> **ENSURE RSPEC GEM VERSION MATCHES YOUR GEMFILE**
> 
> You can use the command `rspec` in place of `bundle exec rspec`, however, using `bundle exec rspec` ensures that the rspec Gem version you use for tests matches the version specified in your Gemfile.

### 5.1 Configure VCR

The Workato SDK Gem works with RSpec and VCR to provide you a way to write unit tests, store HTTP interactions (requests and responses) so that you can continue to run these unit tests without constantly having to send the request to the API. This also has the benefit of replaying the same responses so you needn't have to worry about changes of the actual data in the Application.

When you generate a project using Workato, these settings are automatically generated for you in the `spec_helper.rb` with some default VCR configurations. These VCR recordings also depend on your chosen security settings when you first set up the project. If you selected `secure`, your VCR recordings would be encrypted using your `master.key`.

Learn more about [using VCR](/en/developing-connectors/sdk/cli/guides/rspec/vcr).

* * *

## What's next?

- Learn about developing connector [actions](/en/developing-connectors/sdk/cli/guides/cli/actions), [triggers](/en/developing-connectors/sdk/cli/guides/cli/triggers), and [methods](/en/developing-connectors/sdk/cli/guides/cli/methods)
- Set up [CI/CD for your project on GitHub](/en/developing-connectors/sdk/cli/guides/rspec/enable-ci-cd-on-github)
- Learn more about [running lambda tests](/en/developing-connectors/sdk/cli/guides/cli/test)

---
