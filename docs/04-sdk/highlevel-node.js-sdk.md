---
title: "HighLevel Node.js SDK"
source: "https://marketplace.gohighlevel.com/docs/sdk/node"
generated_at: "2026-03-28T17:50:27.820698"
tags: ["docs", "concept"]
---

# HighLevel Node.js SDK

HighLevel Node.js SDK
The official
@gohighlevel/api-client
package wraps every HighLevel REST endpoint with a typed, promise-based interface. You get automatic OAuth handling, token rotation, retries, and consistent errors without re-implementing request plumbing.
Installation
​
The SDK supports any modern Node.js runtime (v18+) and works with npm, yarn, or pnpm. Install it as a regular dependency so it is available anywhere you need to talk to HighLevel.
npm
yarn
pnpm
npm install @gohighlevel/api-client
yarn add @gohighlevel/api-client
pnpm add @gohighlevel/api-client
Quick Start
​
Initialize the client
​
Set your OAuth credentials (or PIT) through environment variables so that local development and deployments share the same configuration.
JavaScript
TypeScript
const
{
HighLevel
}
=
require
(
'@gohighlevel/api-client'
)
;
const
highLevel
=
new
HighLevel
(
{
clientId
:
process
.
env
.
HIGHLEVEL_CLIENT_ID
,
clientSecret
:
process
.
env
.
HIGHLEVEL_CLIENT_SECRET
,
}
)
;
import
{
HighLevel
}
from
'@gohighlevel/api-client'
;
const
highLevel
=
new
HighLevel
(
{
clientId
:
process
.
env
.
HIGHLEVEL_CLIENT_ID
??
''
,
clientSecret
:
process
.
env
.
HIGHLEVEL_CLIENT_SECRET
??
''
,
}
)
;
Make your first API call
​
Every service under
highLevel
mirrors the REST resources (contacts, opportunities, workflows, etc.). Provide the required
locationId
or
companyId
so the SDK can manage tokens for you.
async
function
listContacts
(
)
{
try
{
const
response
=
await
highLevel
.
contacts
.
searchContactsAdvanced
(
{
locationId
:
'zBG0T99IsBgOoXUrcROH'
,
pageLimit
:
5
,
}
)
;
console
.
log
(
response
)
;
}
catch
(
error
)
{
console
.
error
(
'HighLevel error:'
,
error
)
;
}
}
listContacts
(
)
;
Token storage and refresh
​
By default, tokens live in memory. In production, inject your own storage adapter (Redis, MongoDB, SQL, etc.) so tokens survive restarts:
import
{
HighLevel
,
MongoDBSessionStorage
}
from
'@gohighlevel/api-client'
;
const
highLevel
=
new
HighLevel
(
{
clientId
:
process
.
env
.
HIGHLEVEL_CLIENT_ID
,
clientSecret
:
process
.
env
.
HIGHLEVEL_CLIENT_SECRET
,
sessionStorage
:
new
MongoDBSessionStorage
(
{
dbUrl
:
'mongodb://localhost:27017'
,
dbName
:
'ghl_sessions'
}
)
}
)
;
The SDK will refresh expired access tokens on-demand and update your storage without extra work.
Webhook middleware
​
Use
highLevel.webhooks.subscribe()
to get an Express-compatible middleware that validates signatures, handles INSTALL/UNINSTALL events, and keeps session storage synchronized before your custom logic runs.
app
.
use
(
'/api/webhooks/ghl'
,
highLevel
.
webhooks
.
subscribe
(
)
)
;
app
.
post
(
'/api/webhooks/ghl'
,
(
req
,
res
)
=>
{
// Your business logic can rely on the tokens being current.
res
.
json
(
{
ok
:
true
}
)
;
}
)
;
Note
: If you use webhook middleware provided by SDK, in case of bulk installation it will generate and store the token for each location when it receives INSTALL event from highlevel.
Additional resources
​
You can find some SDK & additional examples here:
SDK
npm
Examples

## Code Snippets

```

```

```prism-code
npm install @gohighlevel/api-client
```

```prism-code
yarn add @gohighlevel/api-client
```

```prism-code
pnpm add @gohighlevel/api-client
```

```prism-code
const{HighLevel}=require('@gohighlevel/api-client');consthighLevel=newHighLevel({clientId:process.env.HIGHLEVEL_CLIENT_ID,clientSecret:process.env.HIGHLEVEL_CLIENT_SECRET,});
```

```prism-code
import{HighLevel}from'@gohighlevel/api-client';consthighLevel=newHighLevel({clientId:process.env.HIGHLEVEL_CLIENT_ID??'',clientSecret:process.env.HIGHLEVEL_CLIENT_SECRET??'',});
```

```prism-code
asyncfunctionlistContacts(){try{constresponse=awaithighLevel.contacts.searchContactsAdvanced({locationId:'zBG0T99IsBgOoXUrcROH',pageLimit:5,});console.log(response);}catch(error){console.error('HighLevel error:',error);}}listContacts();
```

```prism-code
import{HighLevel,MongoDBSessionStorage}from'@gohighlevel/api-client';consthighLevel=newHighLevel({clientId:process.env.HIGHLEVEL_CLIENT_ID,clientSecret:process.env.HIGHLEVEL_CLIENT_SECRET,sessionStorage:newMongoDBSessionStorage({dbUrl:'mongodb://localhost:27017',dbName:'ghl_sessions'})});
```

```prism-code
app.use('/api/webhooks/ghl',highLevel.webhooks.subscribe());app.post('/api/webhooks/ghl',(req,res)=>{// Your business logic can rely on the tokens being current.res.json({ok:true});});
```

