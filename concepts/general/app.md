---
title: "App"
source: "https://marketplace.gohighlevel.com/docs/webhook/AppUninstall"
generated_at: "2026-03-28T17:50:27.794262"
tags: ["docs", "concept"]
---

# App

App
Called whenever an app is uninstalled
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
"appId"
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
,
"locationId"
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
For Location Level App Uninstall
{
"type"
:
"UNINSTALL"
,
"appId"
:
"ve9EPM428h8vShlRW1KT"
,
"locationId"
:
"otg8dTQqGLh3Q6iQI55w"
}
For Agency Level App Uninstall
{
"type"
:
"UNINSTALL"
,
"appId"
:
"ve9EPM428h8vShlRW1KT"
,
"companyId"
:
"otg8dTQqGLh3Q6iQI55w"
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
{"type":"object","properties":{"type":{"type":"string"},"appId":{"type":"string"},"companyId":{"type":"string"},"locationId":{"type":"string"}}}
```

```prism-code
{"type":"UNINSTALL","appId":"ve9EPM428h8vShlRW1KT","locationId":"otg8dTQqGLh3Q6iQI55w"}
```

```prism-code
{"type":"UNINSTALL","appId":"ve9EPM428h8vShlRW1KT","companyId":"otg8dTQqGLh3Q6iQI55w"}
```

