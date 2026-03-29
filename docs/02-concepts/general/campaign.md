---
title: "Campaign"
source: "https://marketplace.gohighlevel.com/docs/webhook/CampaignStatusUpdate"
generated_at: "2026-03-28T17:50:27.797287"
tags: ["docs", "concept"]
---

# Campaign

Campaign
Called whenever a campaign status is updated
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
"locationId"
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
"contactId"
:
{
"type"
:
"string"
}
,
"status"
:
{
"type"
:
"string"
}
,
"templateId"
:
{
"type"
:
"string"
}
,
"replied"
:
{
"type"
:
"string"
}
,
"dateAdded"
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
"CampaignStatusUpdate"
,
"locationId"
:
"ve9EPM428h8vShlRW1KT"
,
"id"
:
"2hxvXh8Fjc69SvujEWMD"
,
"contactId"
:
"CWBf1PR9LvvBkcYqiXlc"
,
"status"
:
"paused"
,
"templateId"
:
"Y2I9XM7aO1hncuSOlc9L"
,
"replied"
:
"Loram ipsum"
,
"dateAdded"
:
"2021-11-26T12:41:02.193Z"
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
{"type":"object","properties":{"type":{"type":"string"},"locationId":{"type":"string"},"id":{"type":"string"},"contactId":{"type":"string"},"status":{"type":"string"},"templateId":{"type":"string"},"replied":{"type":"string"},"dateAdded":{"type":"string"}}}
```

```prism-code
{"type":"CampaignStatusUpdate","locationId":"ve9EPM428h8vShlRW1KT","id":"2hxvXh8Fjc69SvujEWMD","contactId":"CWBf1PR9LvvBkcYqiXlc","status":"paused","templateId":"Y2I9XM7aO1hncuSOlc9L","replied":"Loram ipsum","dateAdded":"2021-11-26T12:41:02.193Z"}
```

