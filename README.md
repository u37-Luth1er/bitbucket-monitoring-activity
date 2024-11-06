![image](https://github.com/user-attachments/assets/48bbeb88-0fb5-4f12-ba4d-c6f9dc16a991)
**Summary:**
This script was developed with the purpose of monitoring the creation of new repositories within the organization globally, in addition to collecting important information such as:

- Recently created projects
- Projects without updates with a custom date filter
- Projects that have never been updated
- Projects that are receiving commits with a custom date filter.

The script has integration with sending Email and Channels Notification like Google Chats, Teams or Slack channel, automatically sending alerts for each new repository within the organization or for specific development teams.

Bitbucket, which is a Git code repository hosting platform, does not have a native function that sends automatic alerts when new repositories are created. Bitbucket provides features to notify repository members about specific activities, such as code pushes, pull requests, and other events, but does not have a native functionality to notify about the creation of new repositories across the entire instance.

However, you can create a custom flow to receive notifications about the creation of new repositories using other available tools and integrations. Here are a few ways to do this:

Custom Webhooks: You can set up custom webhooks in your Bitbucket instance to monitor repository creation events. When a new repository is created, the webhook can be triggered and send a notification to the messaging system or alert service of your choice.

Bitbucket API: You can use the Bitbucket API to create a script or application that periodically checks the list of repositories in your Bitbucket instance and detects new repositories. When a new repository is detected, the script can send notifications to interested parties.

Third-Party Integrations: Some third-party integration tools, such as Zapier or IFTTT, can be used to create custom notification streams based on Bitbucket events, including repository creation.

**Why APIs?**

Using APIs, we can write highly customizable code and also tailor the logic to fit our current scenario. For example...

Let's say you want to monitor only repositories from a specific BU (Business Unit) or Squad.

Then we must set the list of projects that this squad or BU works on.

The idea of ​​this script is to make life easier for the Application Security team when monitoring and evaluating coverage within the company's repositories.
