---
url: 'https://docs.workato.com/en/workbot/legacy-slash-commands.md'
description: >-
  Set up legacy Slack slash commands and connect them to Workbot to run Workato
  recipes without creating an Enterprise Workbot app.
---

# Legacy slash commands

Slash commands using Slack's legacy Custom Integrations allows you to add slash commands to your workspace without having to create a Enterprise Workbot (i.e. a Slack app). However, legacy slash commands lack certain capabilities that come with the Enterprise Workbot slash commands. You can view a detailed comparison between the two in the [Enterprise Workbot slash commands vs Legacy slash commands](/en/workbot/custom-workbot-vs-legacy-slash-commands) document.

To use this feature, you first need to add the slash command custom integration to your Slack workspace.

This custom integration will work in conjunction with Workbot to execute your recipes.

### Adding the Slash Commands custom integrations to your Slack workspace

To do so, head over to [https://your-workspace.slack.com/apps/A0F82E8CA-slash-commands](https://your-workspace.slack.com/apps/A0F82E8CA-slash-commands) for example, [https://workato.slack.com/apps/A0F82E8CA-slash-commands](https://workato.slack.com/apps/A0F82E8CA-slash-commands).

![Add configuration](/assets/add-configuration.DbFML-Ab.png)

Select **Add Configuration**. Key in the name of your slash command. Slash commands should be named after the function it performs, for example,

```
/createissue, /listusers, /showcustomers
```

Next, select **Add Slash Command Integration**. You should now be at the Slash Command settings page. Scroll down to **Integration Settings**. Under **Token**, copy the value in the field for example, `UtsZHLeOKI4S7zqkG3YngwI1` - we'll need this when configuring the Workbot connection in Workato. Keep this tab open - we'll come back to it later.

![Integration Settings](/assets/integration-settings-no-url-1.CYaNsqeD.png)

#### Configuring the Workbot connection

From your Workato account, go to the Workbot connection you want to use slash commands with. Under the **Advanced** group, paste the **Token** value you copied earlier into the **Slash commands verification tokens** field. Click **Connect** and authorize the connection.

![Slash command verification token](/assets/slash-command-verification-token-1.DN9ku0kL.png) _A Workbot connection can support multiple legacy slash commands by comma-separating multiple slash command verification tokens._

As we're not using an Enterprise Workbot here, leave **Custom OAuth profile** empty. However, a Workbot connection can use both a legacy slash command (using the Slash commands verification token) as well as an Enterprise Workbot with a Custom OAuth profile.

Done! Workbot is now connected to the custom integration slash command. Next, we need to configure the Workbot recipe to talk to the custom integration slash command.

## Getting started

To get started, fill in the post command trigger fields as you normally would. Next, move on to the slash command configuration group.

### Slash command configuration group

#### Enable slash command

Toggle whether to enable slash command for this command trigger. When set to 'Yes', command can be invoked using a slash command.

![Enable slash command](data:image/png;base64,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)

#### Command name

This is the name of your slash command. Slash commands should be named after the function it performs, for example,

```
/createissue, /listusers, /showcustomers
```

Slash command actions must start with a slash and contain no spaces. This slash command will also need to be created in your Enterprise Workbot in Slack, but we'll get to that later.

![Slash command name example](/assets/slash-command-name.BKn3GEhQ.png)

#### Request URL

When slash commands are invoked from Slack, Slack will require a URL to send requests to. This request URL is generated by Workato, and will be needed when setting up your legacy slash command in Slack (we'll get to that [later](#creating-the-legacy-slash-command-on-slack)).

After **Enable slash command** is set to **Yes**, and a valid **Command name** is keyed in, then a **Request URL** is generated in the help box at the top of the post command trigger.

![Request URL](/assets/request-url.Ch7gFmMs.png)

#### Dialog for missing command input fields

Dialogs can't be invoked using legacy slash commands. To prompt a dialog to collect missing command input fields, use an [Enterprise Workbot slash command](/en/workbot/configuring-slash-commands).

![Dialog for missing command input fields](/assets/dialog-for-missing-command-input-fields-1.BeadhBdb.png)

If set to 'No', the command input fields will be collected from conversing with the user.

![Dialog for missing command input fields](/assets/dialog-for-missing-command-input-fields-no.YO5q8cKi.png)

#### Using slash commands with command input fields

If you've defined command input fields in your post command trigger, you can pass them into the slash command when you invoke it.

Command input fields in slash commands follow this format:

```
/slashcommand name1: value 1 name2: value 2 name3: value 3...
```

where `name` is the name of the command input field and `value` is the value of the field.

For example, in the JIRA create issue recipe above, we've defined **Title** and **Description** as command input fields. We can pass the respective values to the slash command invocation like so:

```
/createissue title: Button is misaligned description: At the registration page, the registration button is misaligned.
```

## Creating the legacy slash command on Slack

The trigger should now have all the info required to create the slash command in Slack.

Continuing from where we [left off earlier](#adding-the-slash-commands-custom-integrations-to-your-slack-workspace) (you kept the tab open, right?), you should now be at [https://your-workspace.slack.com/apps/A0F82E8CA-slash-commands](https://your-workspace.slack.com/apps/A0F82E8CA-slash-commands), under **Integration Settings**.

- Under **URL**, paste in the URL from the recipe trigger [earlier](#request-url).

![Integration Settings with URL](/assets/integration-settings-with-url-1.BcQhvt8f.png)

Next, scroll down to **Autocomplete help text**.

- Key in the **Description**. It should describe to the user how to use your slash command.
- Key in the **Usage hint**. It should describe how a user uses your slash command. Remember - you can pass command input fields into the slash command when it is invoked by following this format:  
  

```
/slashcommand name1: value 1 name2: value 2 name3: value 3...
```

where `name` is the name of the command input field and `value` is the value of the field. Hence, the **Usage hint** should enclose the command input fields (and their values) with square brackets, i.e.:  

```
/addissue [issue: Issue title] [description: Description of issue]
```

- Turn on **Escape channels, users, and links sent to your app** and
- Check the box for Translate global enterprise IDs to local workspace IDs.

![Autocomplete help text](/assets/autocomplete-help-text-1.BABjLgbo.png)

Select **Save Integration** to finish configuring the custom integrations slash command.

Try it out! Head to your Slack workspace and invoke the slash command to trigger your Workbot recipes.

To read up on how to configure Enterprise Workbot slash commands, see the [Configuring slash commands](/en/workbot/configuring-slash-commands) document.

---
