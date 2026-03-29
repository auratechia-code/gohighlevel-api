---
title: "Getting Started with HighLevel SDKs"
source: "https://marketplace.gohighlevel.com/docs/sdk/GettingStartedSDK"
generated_at: "2026-03-28T17:50:27.820161"
tags: ["docs", "concept"]
---

# Getting Started with HighLevel SDKs

Getting Started with HighLevel SDKs
HighLevel now ships official SDKs for Node.js, Python, and PHP so you can stop hand-rolling API calls. All three clients deliver the same core features—automatic OAuth flows, PIT support, per-location token storage, webhook helpers, auto refresh tokens and typed service methods—so pick the runtime that matches your stack.
Pick your language
​
SDK
Package
Minimum runtime
Deep dive
Node.js
@gohighlevel/api-client
Node.js 18+
Node guide
Python
gohighlevel-api-client
Python 3.8+
Python guide
PHP
gohighlevel/api-client
PHP 7.4+
PHP guide
Installation quick reference
​
Node.js
Python
PHP
npm install @gohighlevel/api-client
# or
yarn add @gohighlevel/api-client
# or
pnpm add @gohighlevel/api-client
Read the
Node guide
when you are ready.
pip install gohighlevel-api-client
# or
poetry add gohighlevel-api-client
Continue with the
Python guide
.
composer require gohighlevel/api-client
Dive into the
PHP guide
.
What you get out of the box
​
Auto token rotation
– refresh happens transparently once storage is configured.
Webhook utilities
– signature validation plus automatic handling of webhook events (INSTALL and UNINSTALL).
Token for bulk installation
– if webhook is used, it will generate token for each location in which app is installed and store it in the db
Share your feedback
★
★
★
★
★

## Code Snippets

```

```

```prism-code
npm install @gohighlevel/api-client# oryarn add @gohighlevel/api-client# orpnpm add @gohighlevel/api-client
```

```prism-code
pip install gohighlevel-api-client# orpoetry add gohighlevel-api-client
```

```prism-code
composer require gohighlevel/api-client
```

