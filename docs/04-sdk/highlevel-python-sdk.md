---
title: "HighLevel Python SDK"
source: "https://marketplace.gohighlevel.com/docs/sdk/python"
generated_at: "2026-03-28T17:50:27.821508"
tags: ["docs", "concept"]
---

# HighLevel Python SDK

HighLevel Python SDK
The official
gohighlevel-api-client
package publishes a async client that speaks to every HighLevel endpoint with the same token automation, webhook helpers, and storage adapters you get on other platforms. Requires Python 3.8+.
Installation
​
pip
Pipenv
Poetry
pip install gohighlevel-api-client
pipenv install gohighlevel-api-client
poetry add gohighlevel-api-client
Quick Start
​
Initialize the client
​
from
highlevel
import
HighLevel
client
=
HighLevel
(
client_id
=
"your_client_id"
,
client_secret
=
"your_client_secret"
,
)
Make an API call
​
The SDK is async-first; wrap your logic in
asyncio.run()
when you are not already inside an async framework.
import
asyncio
from
highlevel
import
HighLevel
async
def
main
(
)
:
client
=
HighLevel
(
client_id
=
"your_client_id"
,
client_secret
=
"your_client_secret"
,
)
response
=
await
client
.
contacts
.
search_contacts_advanced
(
{
"locationId"
:
"zBG0T99IsBgOoXUrcROH"
,
"pageLimit"
:
5
,
}
)
print
(
response
)
asyncio
.
run
(
main
(
)
)
Session storage
​
Use in-memory storage for local testing or swap in MongoDB/Redis/etc. for production resiliency.
from
highlevel
.
storage
import
MongoDBSessionStorage
storage
=
MongoDBSessionStorage
(
connection_string
=
"mongodb://localhost:27017"
,
database_name
=
"ghl_sessions"
,
collection_name
=
"jwt_tokens"
,
)
client
=
HighLevel
(
client_id
=
"your_client_id"
,
client_secret
=
"your_client_secret"
,
session_storage
=
storage
,
)
Webhook integration
​
Hook up the middleware returned by
client.webhooks.subscribe()
to validate signatures, respond to INSTALL/UNINSTALL automatically, and keep session storage synchronized.
client
=
HighLevel
(
client_id
=
"your_client_id"
,
client_secret
=
"your_client_secret"
)
webhook_middleware
=
client
.
webhooks
.
subscribe
(
)
@app
.
post
(
"/api/webhooks/ghl"
)
async
def
handle_ghl_webhook
(
request
)
:
await
webhook_middleware
(
request
)
# you custom logic for webhook goes here
return
{
"status"
:
"success"
}
Additional resources
​
You can find some SDK & additional examples here:
SDK
pypi
Examples

## Code Snippets

```

```

```prism-code
pip install gohighlevel-api-client
```

```prism-code
pipenv install gohighlevel-api-client
```

```prism-code
poetry add gohighlevel-api-client
```

```prism-code
fromhighlevelimportHighLevelclient=HighLevel(client_id="your_client_id",client_secret="your_client_secret",)
```

```prism-code
importasynciofromhighlevelimportHighLevelasyncdefmain():client=HighLevel(client_id="your_client_id",client_secret="your_client_secret",)response=awaitclient.contacts.search_contacts_advanced({"locationId":"zBG0T99IsBgOoXUrcROH","pageLimit":5,})print(response)asyncio.run(main())
```

```prism-code
fromhighlevel.storageimportMongoDBSessionStoragestorage=MongoDBSessionStorage(connection_string="mongodb://localhost:27017",database_name="ghl_sessions",collection_name="jwt_tokens",)client=HighLevel(client_id="your_client_id",client_secret="your_client_secret",session_storage=storage,)
```

```prism-code
client=HighLevel(client_id="your_client_id",client_secret="your_client_secret")webhook_middleware=client.webhooks.subscribe()@app.post("/api/webhooks/ghl")asyncdefhandle_ghl_webhook(request):awaitwebhook_middleware(request)# you custom logic for webhook goes herereturn{"status":"success"}
```

