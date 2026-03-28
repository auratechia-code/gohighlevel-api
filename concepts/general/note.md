---
title: "Note"
source: "https://marketplace.gohighlevel.com/docs/webhook/NoteDelete"
generated_at: "2026-03-28T17:50:27.805831"
tags: ["docs", "concept"]
---

# Note

Note
Called whenever a note is deleted
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
"body"
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
"NoteDelete"
,
"locationId"
:
"ve9EPM428h8vShlRW1KT"
,
"id"
:
"otg8dTQqGLh3Q6iQI55w"
,
"body"
:
"Loram ipsum"
,
"contactId"
:
"CWBf1PR9LvvBkcYqiXlc"
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
{"type":"object","properties":{"type":{"type":"string"},"locationId":{"type":"string"},"id":{"type":"string"},"body":{"type":"string"},"contactId":{"type":"string"},"dateAdded":{"type":"string"}}}
```

```prism-code
{"type":"NoteDelete","locationId":"ve9EPM428h8vShlRW1KT","id":"otg8dTQqGLh3Q6iQI55w","body":"Loram ipsum","contactId":"CWBf1PR9LvvBkcYqiXlc","dateAdded":"2021-11-26T12:41:02.193Z"}
```

