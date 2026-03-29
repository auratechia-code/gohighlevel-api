---
title: "Conversation Providers"
source: "https://marketplace.gohighlevel.com/docs/marketplace-modules/ConversationProviders"
generated_at: "2026-03-28T17:50:27.822053"
tags: ["docs", "concept"]
---

# Conversation Providers

Conversation Providers
HighLevel provides conversation providers in marketplace applications for creating custom SMS, Email, and Call providers.
Setting up Custom Providers
​
Create a Marketplace Application
​
First you'll need to create a marketplace application:
Navigate to
https://marketplace.gohighlevel.com
Go to the Auth section
Add your scopes (see notes below)
Add redirect, client keys, then click save
Scopes
​
Below are the various scopes necessary to use custom conversation providers. Review all scope documentation here:
https://marketplace.gohighlevel.com/docs/oauth/Scopes
Scope
Purpose
conversations/message.write
Conversations Provider Outbound Message Webhook Events, Adding inbound messages. Add external outbound call logs. Upload attachments to conversations. Update message statuses.
conversations.readonly
Query conversations APIs
conversations.write
Create/Update/Delete conversation. One conversationId is maintained per contact.
contacts.readonly, contacts.write
Create/Update contacts
conversations/message.readonly
Recordings/Transcriptions and Outbound Message Webhook Event
Conversation Provider Configuration
​
After you create your provider you will have an "ID" which is the "conversationProviderId".
SMS (Replace default SMS provider)
​
Description: This enables a SMS provider to replace the default twilio/LC-Phone provider.
Enter a Name
Type: SMS
Delivery URL - Sends webhook events to the Conversation Provider Outbound Webhook
NOTE:
Do not checkbox "Is this a Custom Conversation Provider"
Add Inbound Message API: Use type "SMS". "conversationProviderId"
is not required
.
https://marketplace.gohighlevel.com/docs/ghl/conversations/add-an-inbound-message
Enable The Provider: Navigate to the sub-accounts Settings > Phone Numbers > Advanced Settings > SMS Provider. Click your provider and then click save to save it.
Workflows: Supports standard SMS modules.
Bulk Actions: Supported
SMS (Add new conversation channel)
​
Description: This adds an additional SMS custom conversation provider.
Enter a Name
Type: SMS
Delivery URL - Sends webhook events to the Conversation Provider Outbound Webhook
Checkbox "Is this a Custom Conversation Provider"
Conversations Tab - Optional - Checkbox "Always show this Conversation Provider" - If you want a tab in the conversations window to respond on the provider.
Alias - Optional - Changes the name of the provider in the conversations tab
Logo - Optional
Add Inbound Message API: Use type "SMS". "conversationProviderId"
is required
.
https://marketplace.gohighlevel.com/docs/ghl/conversations/add-an-inbound-message
Enable The Provider: Enabled upon installation. Visit Settings > Conversation Providers to review installed providers.
Workflows: You can build premium workflow actions in your marketplace application. SMS module is not currently supported.
Email Provider (default)
​
Description: This enables an Email provider to replace the default mailgun/LC-Email provider.
Enter a Name
Type: Email
Delivery URL - Sends webhook events to the Conversation Provider Outbound Webhook
NOTE:
Do not checkbox "Is this a Custom Conversation Provider"
Add Inbound Message API: Use type "Email". "emailMessageId" in the response is the thread to respond to. "conversationProviderId"
is not required
.
https://marketplace.gohighlevel.com/docs/ghl/conversations/add-an-inbound-message
Enable The Provider: Navigate to the sub-accounts Settings > Email Services > Click your provider and then click save to save it.
Workflows: Supports standard Email modules. Triggers are unsupported currently. Use premium workflow actions.
Bulk Actions: Supported
Email Provider (extra)
​
Description: This adds an additional Email custom conversation provider.
Enter a Name
Type: Email
Delivery URL - Sends webhook events to the Conversation Provider Outbound Webhook
Checkbox "Is this a Custom Conversation Provider"
Conversations Tab - Optional - Checkbox "Always show this Conversation Provider" - If you want a tab in the conversations window to respond on the provider.
Alias - Optional - Changes the name of the provider in the conversations tab
Logo - Optional
Add Inbound Message API: Use type "Custom". You can also set "altId". When you reply in the UI the conversation provider outbound payload will add "replyToAltId". "conversationProviderId"
is required
.
https://marketplace.gohighlevel.com/docs/ghl/conversations/add-an-inbound-message
Enable The Provider: Enabled upon installation. Visit Settings > Conversation Providers to review installed providers.
Workflows: You can build premium workflow actions in your marketplace application. Triggers and Email modules are unsupported currently.
Call Provider
​
Description: This adds a call provider. It is specifically for adding call logs and can also add attachments like voicemails to a conversation. It is not used to replace the voice/SIP connection.
Enter a Name
Type: Call
Delivery URL - Sends webhook events to the Conversation Provider Outbound Webhook
Add Inbound Message API: Use type "Call". Supply the call object payload and ensure the "from" phone matches an existing contact. Used for adding inbound call logs. "conversationProviderId"
is required
.
https://marketplace.gohighlevel.com/docs/ghl/conversations/add-an-inbound-message
Add an External Outbound Call API: Used to add outbound direction logs. Ensure the "to" phone number matches an existing contact.
https://marketplace.gohighlevel.com/docs/ghl/conversations/add-an-outbound-message
Webhook Events
​
Conversations Provider Outbound Message Webhook Events
https://marketplace.gohighlevel.com/docs/webhook/ProviderOutboundMessage
Purpose: Outbound events that are distinct from the Outbound Message Event payload.
Outbound Message Events
https://marketplace.gohighlevel.com/docs/webhook/OutboundMessage
Purpose: Monitors all outbound messages/channels
Additional Notes
​
Using Providers
​
Conversations Screen - Navigate to the conversations screen to send/receive messages if a provider is set as the default or if you have enabled the ability to see the provider.
Bulk Actions - Only supported on default providers at this time.
Workflows - Review notes on currently supported modules.
Mobile Application - Select your custom provider depending on type.
Update Message Status API
​
Message status updates are only able to be updated by the conversation provider marketplace application tokens. If you have additional marketplace applications installed in your account then they cannot update the message status.
https://marketplace.gohighlevel.com/docs/ghl/conversations/update-message-status
Share your feedback
★
★
★
★
★

## Code Snippets

```

```

