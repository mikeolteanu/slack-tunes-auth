## Setup tokens

1.  Create an app from the [app management page](api.slack.com/apps).
1.  Copy the **Client ID** and write it to `config.go`.
1.  Click the **Show** button for the **Client secret**. Copy the secret value
    and write it to `config.go`.

[Be careful](https://api.slack.com/docs/oauth-safety) with these tokens. Treat
them like you would any other secret token. Do not store tokens in version
control or share them publicly.

## Setup OAuth

1.  Click **OAuth & permissions** item under the features heading on the
    left navigation.
1.  Add a new redirect URL. Set it to 
    `https://YOUR-PROJECT.appspot.com/callback`, replacing `YOUR-PROJECT`
    with your Google Cloud Project ID.
1.  Click the **Save URLs** button.

## Configure the app

Make config.yaml with the following:

    client_id: "CLIENT_ID_HERE"
    client_secret: "CLIENT_SECRET"
    scope: users.profile:write
    redirect_uri: "REDIRECT_URI"

## Build and Deploy

1.  Deploy the app to App Engine.

        gcloud app deploy -application your-project app.yaml

    Replace `your-project` with your Google Cloud Project ID.
1.  If this is not the first App Engine application you have deployed to this
    project, go to the [Google Cloud Platform
    Console](https://console.cloud.google.com/appengine/versions), select
    version 1 in the App Engine versions and click **Migrate traffic** to send
    requests to the deployed version.

## Activate distribution

1.  Go to the Slack [app management page](api.slack.com/apps) for your app.
1.  Click **Manage distribution** on the left navigation under the settings
    header.
1.  Verify you've completed all the steps in the **Share your apps with other
    teams** section.
1.  Click the **Activate public distribution** button.

