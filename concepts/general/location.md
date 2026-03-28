---
title: "Location"
source: "https://marketplace.gohighlevel.com/docs/webhook/LocationUpdate"
generated_at: "2026-03-28T17:50:27.804643"
tags: ["docs", "concept"]
---

# Location

Location
Called whenever a location is updated.
Available to Agency Level Apps for all sub-accounts or to specific sub-accounts.
Schema
​
{
"type"
:
"object"
,
"properties"
:
{
"type"
:
{
"type"
:
"string"
}
,
"id"
:
{
"type"
:
"string"
}
,
"name"
:
{
"type"
:
"string"
}
,
"email"
:
{
"type"
:
"string"
}
,
"stripeProductId"
:
{
"type"
:
"string"
}
,
"companyId"
:
{
"type"
:
"string"
}
}
}
Example
​
{
"type"
:
"LocationUpdate"
,
"id"
:
"ve9EPM428h8vShlRW1KT"
,
"companyId"
:
"otg8dTQqGLh3Q6iQI55w"
,
"name"
:
"Loram ipsum"
,
"email"
:
"mailer@example.com"
,
"stripeProductId"
:
"prod_xyz123abc"
}
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
{"type":"object","properties":{"type":{"type":"string"},"id":{"type":"string"},"name":{"type":"string"},"email":{"type":"string"},"stripeProductId":{"type":"string"},"companyId":{"type":"string"}}}
```

```prism-code
{"type":"LocationUpdate","id":"ve9EPM428h8vShlRW1KT","companyId":"otg8dTQqGLh3Q6iQI55w","name":"Loram ipsum","email":"mailer@example.com","stripeProductId":"prod_xyz123abc"}
```

