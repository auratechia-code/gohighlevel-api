---
title: "Conversation"
source: "https://marketplace.gohighlevel.com/docs/webhook/ConversationUnreadWebhook"
generated_at: "2026-03-28T17:50:27.799263"
tags: ["docs", "concept"]
---

# Conversation

Conversation
Called whenever a conversations unread status is updated
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
"unreadCount"
:
{
"type"
:
"number"
}
,
"inbox"
:
{
"type"
:
"boolean"
}
,
"starred"
:
{
"type"
:
"boolean"
}
,
"deleted"
:
{
"type"
:
"boolean"
}
}
}
Example
​
{
"type"
:
"ConversationUnreadUpdate"
,
"locationId"
:
"ADVlSQnPsdq3hinusd6C3"
,
"id"
:
"MzKIpg0rEIH2ZUGKf6BS"
,
"contactId"
:
"zsYhPBOUsEHtrK508Wm9"
,
"deleted"
:
false
,
"inbox"
:
false
,
"starred"
:
true
,
"unreadCount"
:
0
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
{"type":"object","properties":{"type":{"type":"string"},"locationId":{"type":"string"},"id":{"type":"string"},"contactId":{"type":"string"},"unreadCount":{"type":"number"},"inbox":{"type":"boolean"},"starred":{"type":"boolean"},"deleted":{"type":"boolean"}}}
```

```prism-code
{"type":"ConversationUnreadUpdate","locationId":"ADVlSQnPsdq3hinusd6C3","id":"MzKIpg0rEIH2ZUGKf6BS","contactId":"zsYhPBOUsEHtrK508Wm9","deleted":false,"inbox":false,"starred":true,"unreadCount":0}
```

