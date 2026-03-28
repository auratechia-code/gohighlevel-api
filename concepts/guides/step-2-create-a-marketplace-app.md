---
title: "Step 2: Create a Marketplace App"
source: "https://marketplace.gohighlevel.com/docs/oauth/CreateMarketplaceApp"
generated_at: "2026-03-28T17:50:27.783759"
tags: ["docs", "concept"]
---

# Step 2: Create a Marketplace App

Step 2: Create a Marketplace App
This section walks you through creating a Marketplace App in HighLevel—from creating the app record in the Developer Portal, to completing your listing, generating OAuth credentials, and installing the app for testing.
1) Sign in to your Developer Account
​
Go to the
HighLevel Marketplace
and sign in to your Developer Account.
After logging in, go to My Apps.
Click Create App.
That’s it — you’re now inside the app builder where you’ll configure everything.
2) Configure basic app details
​
When you create your app, HighLevel will ask for core setup details. These choices affect who can install the app and how it appears.
App Name
​
Choose a clear, descriptive name.
This name is visible to users in the Marketplace (for
Public
apps).
App Type: Private vs Public
​
Private App
​
Intended for personal/internal use
Not listed in the Marketplace
Best for development/testing
Public App
​
Listed in the Marketplace
Installable by all users (once approved)
Recommendation:
Start with
Private
while you build and test. Switch to
Public
only when your app is stable, secure, and ready for wider distribution.
Target User
​
This defines who the app is built for (who will use it).
Recommended for most apps:
Sub-account
Works well for apps that operate at the individual location level.
Who Can Install
​
Controls who can see/install your app in the Marketplace UI.
Recommended:
Both Agency & Sub-account
Maximizes visibility and adoption.
Agencies Only
Useful if you’re building a fully white-labeled SaaS feature that agencies manage for their sub-accounts.
Listing Type
​
White-label
is commonly recommended (especially for marketing agencies).
This helps the app fit naturally into an agency’s branded experience.
3) Understand the app workspace
​
After you click
Create App
, you’ll land inside your app configuration area.
On the left navigation, you’ll see three major sections:
Build
Manage
Insights
Think of them like this:
Build
= what the app is + how it behaves
Manage
= versions + credentials/secrets
Insights
= performance/usage visibility
4) Build section
​
4.1 Profile
​
The
Profile
is your Marketplace listing content — what users see before installing.
Typical profile fields include:
App Logo
Category
Company Name
App Description
Preview Images / Screenshots
Tip:
Don’t rush this section. Clear text + good visuals reduce confusion and increase installs.
4.2 Pricing
​
This is where you configure pricing for your app.
4.3 Modules
​
Marketplace Modules are feature “building blocks” you can enable inside a HighLevel Marketplace App to integrate with specific parts of HighLevel (UI + behavior), not just REST APIs.
4.4 Advanced Settings
​
This is where you configure the technical plumbing required for authentication and events, including:
OAuth scopes
Redirect URLs
External Authentication
Webhooks
Advanced Settings includes three key sub-sections:
A) Auth (Scopes + Redirect URLs)
​
What are scopes?
Scopes define the level of access your app is requesting — what data it can read or actions it can perform.
How to add scopes:
Click the
Select Scope
dropdown.
Choose the scopes your app needs.
Use the documentation link in the UI to review the full scope list.
Best practice:
Request the minimum scopes required. Fewer scopes = better security, more user trust, and typically a smoother approval process.
What is a Redirect URL?
A Redirect URL (also called a Callback URL) is where HighLevel sends the authorization code after a user installs (or authorizes) your app.
How to add a redirect URL:
Enter your URL in the
Redirect URL
field.
Click
Add
to save it.
Your redirect URL should:
Use
HTTPS
Be controlled by your backend (not a front-end-only page)
Match exactly what your OAuth flow expects (even small differences can break installs)
B) Webhooks
​
HighLevel Marketplace allows you to subscribe to multiple webhook events.
In the
Webhooks
section:
Add your
Webhook URL
HighLevel will send event notifications in real time to that endpoint
C) External Authentication
​
External Authentication allows developers to authenticate HighLevel users using the developer’s system before they install the application in HighLevel.
5) Manage section
​
5.1 Versions
​
Marketplace supports app versioning so you can create and manage new versions.
You’ll use this for:
Releasing updates
Testing changes safely
Keeping stable versions available while you iterate
Good habit:
Treat versions like real software releases. Track changes, test upgrades, and avoid breaking behavior without a migration plan.
5.2 Secrets (Client Keys + Shared Secret Key)
​
This section is where you generate and manage:
Client Keys
(Client ID + Client Secret)
Shared Secret Key
(used for secure user context access via signed tokens)
Client Keys: Generate Client ID & Client Secret
​
Client credentials identify and authenticate your app during the OAuth token exchange.
How to generate them:
In
Client Keys
, click
Add
Provide a name for the client key pair
Save
HighLevel will generate:
Client ID
Client Secret
⚠️
Important (don’t ignore this):
Copy and store your
Client Secret
immediately. Once you click
OK
, it will not be shown again. Treat it like a password.
Shared Secret Key (Signed token user context)
​
HighLevel provides a secure mechanism for accessing authenticated user information through signed tokens. The
Shared Secret Key
is used to verify/validate that secured context.
6) Insights section: adoption and usage visibility
​
Insights is used for visibility into:
performance
installs
usage metrics

## Code Snippets

```

```

