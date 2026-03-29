# Update Action

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId` |
| **Scopes Required** | `conversation-ai.write` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `` | No |  |

### Path Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **actionId** | `` | Yes | agentId string required |
| **agentId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **type** | `string` | No |  |
| **name** | `string` | No |  |
| **details** | `object` | Yes | Action-specific details. The structure depends on the action type. For TRIGGER_WORKFLOW use triggerWorkflowDto, for UPDATE_CONTACT_FIELD use updateContactFieldDto, for APPOINTMENT_BOOKING use appointmentBookingDto, for STOP_BOT use stopBotDto, for HUMAN_HAND_OVER use humanHandOverDto, for ADVANCED_FOLLOWUP use advancedFollowupDto, and for TRANSFER_BOT use transferBotDto. oneOf triggerWorkflowDto updateContactFieldDto appointmentBookingDto stopBotDto humanHandOverDto advancedFollowupDto transferBotDto workflowIds string[] required Array of workflow IDs to trigger Example: ["workflow123","workflow456"] triggerCondition string required Condition that triggers the workflow Example: When user requests appointment triggerMessage string Optional message to send when triggering the workflow Example: Workflow triggered successfully contactFieldId string required ID of the contact field in Contacts Table Example: 123 description string required Description of the contact field in Contacts Table Example: Business Name contactUpdateExamples string[] Contact update examples in Contacts Table. Not required when using standard fields, Monetory or Date Custom fields. Default value: [] Example: ["Example 1"] actionId string Optional action ID reference Example: action123 calendarId string required Calendar ID for appointment booking Example: calendar123 onlySendLink boolean required If true, only sends the appointment link without booking Example: false triggerWorkflow boolean required Whether to trigger a workflow after booking (cannot be true when onlySendLink is true) Example: true workflowIds string[] Workflow IDs to trigger after booking (required when triggerWorkflow is true) Example: ["workflow123"] sleepAfterBooking boolean required Whether to put the agent to sleep after booking (cannot be true when onlySendLink is true) Example: true sleepTimeUnit string Unit for sleep time (required when sleepAfterBooking is true) Possible values: [ days , hours , minutes ] Example: hours sleepTime number Sleep duration (required when sleepAfterBooking is true) Example: 24 transferBot boolean required Whether to transfer to another agent after booking (cannot be true when onlySendLink is true) Example: false transferAgent string Agent ID to transfer to (required when transferBot is true) Example: employee456 rescheduleEnabled boolean required Whether to allow appointment rescheduling (cannot be true when onlySendLink is true) Default value: false Example: true cancelEnabled boolean required Whether to allow appointment cancellation (cannot be true when onlySendLink is true) Default value: false Example: true stopBotDetectionType string required Type of stop bot detection - Goodbye or Custom Possible values: [ Goodbye , Custom ] Example: Custom stopBotTriggerCondition string required Condition that triggers stopping the bot Example: When the user says they no longer need assistance or want to end the conversation reactivateEnabled boolean required Whether the bot can be reactivated after being stopped Example: true sleepTimeUnit string Time unit for reactivation delay (required when reactivateEnabled is true) Possible values: [ days , hours , minutes ] Example: hours sleepTime number Time duration before reactivation (required when reactivateEnabled is true) Example: 24 enabled boolean required Whether this action is enabled for the agent Example: true stopBotExamples string[] required Example phrases that trigger stop bot action (minimum 2 required) Example: ["goodbye","thank you","no more questions"] finalMessage string required Final message sent when stopping the bot Example: Thank you for contacting us. Have a great day! tags string[] Tags to apply when stopping the bot Example: ["resolved","no-response"] enabled boolean required Whether human handover action is enabled Example: true triggerCondition string required Condition that triggers human handover Example: When the user requests to speak with a human agent or expresses frustration examples string[] Example phrases that trigger human handover (required when handoverType is custom or contactRequest) Example: ["speak to human","talk to agent","need help from person"] assignToUserId string ID of the user to assign the conversation to Example: user123 skipAssignToUser boolean Whether to skip assigning to a specific user Example: false createTask boolean Whether to create a task when handing over Example: true reactivateEnabled boolean required Whether the agent can be reactivated after handover Example: true sleepTimeUnit string Time unit for reactivation delay (required when reactivateEnabled is true) Possible values: [ days , hours , minutes ] Example: hours sleepTime number Time duration before reactivation (required when reactivateEnabled is true) Example: 24 finalMessage string required Final message sent when handing over to human Example: I am transferring you to a human agent who will assist you shortly. tags string[] Tags to apply during handover Example: ["escalated","human-requested"] handoverType string required Type of human handover detection Possible values: [ contactRequest , lackOfInformation , failedToResolveIssue , custom ] Example: contactRequest enabled boolean required Whether advanced followup is enabled Example: true scenarioId string required ID of the followup scenario Possible values: [ contactStoppedReplying , contactIsBusy , contactRequested ] Example: contactIsBusy followupSequence object[] required Sequence of followup actions to perform Array [ id number required Unique identifier for this followup step Example: 1 followupTimeUnit string required Time unit for followup delay Possible values: [ days , hours , minutes ] Example: hours followupTime number required Time duration before followup (max: 60 minutes, 24 hours, or 180 days depending on unit) Example: 2 aiEnabledMessage boolean Whether to use AI to generate the followup message Default value: true Example: true triggerWorkflow boolean Whether to trigger a workflow during this followup Default value: false Example: false customMessage string Custom message to send (when aiEnabledMessage is false) Example: Hi! Just following up on our previous conversation. Do you have any questions? workflowId string Workflow ID to trigger (when triggerWorkflow is true) Example: workflow789 contactRequested boolean Whether contact was requested in this followup Example: false ] followupSettings object Additional settings for followup behavior dynamicChannelSwitching boolean required Whether to dynamically switch channels for followups Default value: true Example: true followUpHours boolean Whether to respect working hours for followups Example: true workingHours object[] Working hours configuration for followups Array [ dayOfTheWeek number required Day of the week (0=Sunday, 1=Monday, etc.) Example: 1 intervals object[] Time intervals for this day Array [ startHour number required Start hour (24-hour format) Example: 9 startMinute number required Start minute Example: 0 endHour number required End hour (24-hour format) Example: 17 endMinute number required End minute Example: 30 ] ] timezoneToUse string Timezone to use for followups, contact or location Possible values: [ contact , business ] transferBotType string required Type of transfer - Default or Custom Possible values: [ Default , Custom ] Example: Custom transferToBot string required ID of the bot/agent to transfer to Example: employee789 enabled boolean required Whether this transfer action is enabled Example: true transferBotTriggerCondition string Condition that triggers the transfer (required for Custom type) Example: When the user asks to speak with sales or needs pricing information transferBotExamples string[] Example phrases that trigger transfer (required for Custom type, minimum 2) Example: ["talk to sales","pricing information","speak to specialist"] |
| **workflowIds** | `string[]` | No |  |
| **triggerCondition** | `string` | No |  |
| **triggerMessage** | `string` | No |  |
| **contactFieldId** | `string` | No |  |
| **description** | `string` | No |  |
| **contactUpdateExamples** | `string[]` | No |  |
| **actionId** | `string` | No |  |
| **calendarId** | `string` | No |  |
| **onlySendLink** | `boolean` | No |  |
| **triggerWorkflow** | `boolean` | No |  |
| **workflowIds** | `string[]` | No |  |
| **sleepAfterBooking** | `boolean` | No |  |
| **sleepTimeUnit** | `string` | No |  |
| **sleepTime** | `number` | No |  |
| **transferBot** | `boolean` | No |  |
| **transferAgent** | `string` | No |  |
| **rescheduleEnabled** | `boolean` | No |  |
| **cancelEnabled** | `boolean` | No |  |
| **stopBotDetectionType** | `string` | No |  |
| **stopBotTriggerCondition** | `string` | No |  |
| **reactivateEnabled** | `boolean` | No |  |
| **sleepTimeUnit** | `string` | No |  |
| **sleepTime** | `number` | No |  |
| **enabled** | `boolean` | No |  |
| **stopBotExamples** | `string[]` | No |  |
| **finalMessage** | `string` | No |  |
| **tags** | `string[]` | No |  |
| **enabled** | `boolean` | No |  |
| **triggerCondition** | `string` | No |  |
| **examples** | `string[]` | No |  |
| **assignToUserId** | `string` | No |  |
| **skipAssignToUser** | `boolean` | No |  |
| **createTask** | `boolean` | No |  |
| **reactivateEnabled** | `boolean` | No |  |
| **sleepTimeUnit** | `string` | No |  |
| **sleepTime** | `number` | No |  |
| **finalMessage** | `string` | No |  |
| **tags** | `string[]` | No |  |
| **handoverType** | `string` | No |  |
| **enabled** | `boolean` | No |  |
| **scenarioId** | `string` | No |  |
| **followupSequence** | `object[]` | Yes | Sequence of followup actions to perform Array [ id number required Unique identifier for this followup step Example: 1 followupTimeUnit string required Time unit for followup delay Possible values: [ days , hours , minutes ] Example: hours followupTime number required Time duration before followup (max: 60 minutes, 24 hours, or 180 days depending on unit) Example: 2 aiEnabledMessage boolean Whether to use AI to generate the followup message Default value: true Example: true triggerWorkflow boolean Whether to trigger a workflow during this followup Default value: false Example: false customMessage string Custom message to send (when aiEnabledMessage is false) Example: Hi! Just following up on our previous conversation. Do you have any questions? workflowId string Workflow ID to trigger (when triggerWorkflow is true) Example: workflow789 contactRequested boolean Whether contact was requested in this followup Example: false ] |
| **id** | `number` | No |  |
| **followupTimeUnit** | `string` | No |  |
| **followupTime** | `number` | No |  |
| **aiEnabledMessage** | `boolean` | No |  |
| **triggerWorkflow** | `boolean` | No |  |
| **customMessage** | `string` | No |  |
| **workflowId** | `string` | No |  |
| **contactRequested** | `boolean` | No |  |
| **followupSettings** | `object` | Yes | Additional settings for followup behavior dynamicChannelSwitching boolean required Whether to dynamically switch channels for followups Default value: true Example: true followUpHours boolean Whether to respect working hours for followups Example: true workingHours object[] Working hours configuration for followups Array [ dayOfTheWeek number required Day of the week (0=Sunday, 1=Monday, etc.) Example: 1 intervals object[] Time intervals for this day Array [ startHour number required Start hour (24-hour format) Example: 9 startMinute number required Start minute Example: 0 endHour number required End hour (24-hour format) Example: 17 endMinute number required End minute Example: 30 ] ] timezoneToUse string Timezone to use for followups, contact or location Possible values: [ contact , business ] |
| **dynamicChannelSwitching** | `boolean` | No |  |
| **followUpHours** | `boolean` | No |  |
| **workingHours** | `object[]` | Yes | Working hours configuration for followups Array [ dayOfTheWeek number required Day of the week (0=Sunday, 1=Monday, etc.) Example: 1 intervals object[] Time intervals for this day Array [ startHour number required Start hour (24-hour format) Example: 9 startMinute number required Start minute Example: 0 endHour number required End hour (24-hour format) Example: 17 endMinute number required End minute Example: 30 ] ] |
| **dayOfTheWeek** | `number` | No |  |
| **intervals** | `object[]` | Yes | Time intervals for this day Array [ startHour number required Start hour (24-hour format) Example: 9 startMinute number required Start minute Example: 0 endHour number required End hour (24-hour format) Example: 17 endMinute number required End minute Example: 30 ] |
| **startHour** | `number` | No |  |
| **startMinute** | `number` | No |  |
| **endHour** | `number` | No |  |
| **endMinute** | `number` | No |  |
| **timezoneToUse** | `string` | No |  |
| **transferBotType** | `string` | No |  |
| **transferToBot** | `string` | No |  |
| **enabled** | `boolean` | No |  |
| **transferBotTriggerCondition** | `string` | No |  |
| **transferBotExamples** | `string[]` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "data": {
    "id": "actionId123",
    "name": "Trigger Workflow",
    "type": "triggerWorkflow",
    "agentId": "agentId123",
    "details": {
      "workflowIds": [
        "workflow123",
        "workflow456"
      ],
      "triggerCondition": "When user requests appointment",
      "triggerMessage": "Workflow triggered successfully"
    }
  },
  "success": true
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **data** | `dict` |  |
| **success** | `bool` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
}'
```

### 2. NODE SDK

```javascript
const { HighLevel } = require('@gohighlevel/api-client');

const ghl = new HighLevel({
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET'
});

async function executeRequest() {
  try {
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
}
    });
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}
```

### 3. AXIOS

```javascript
const axios = require('axios');

const config = {
  method: 'put',
  url: 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
}
};

axios(config)
.then(response => console.log(JSON.stringify(response.data)))
.catch(error => console.log(error));
```

### 4. NATIVE NODE

```javascript
const https = require('follow-redirects').https;

const options = {
  'method': 'PUT',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/conversation-ai/agents/:agentId/actions/:actionId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
};

const req = https.request(options, (res) => {
  let chunks = [];
  res.on("data", (chunk) => chunks.push(chunk));
  res.on("end", () => console.log(Buffer.concat(chunks).toString()));
});

req.write(JSON.stringify({
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
})
};

request(options, (error, response) => {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

### 6. UNIREST NODE

```javascript
const unirest = require('unirest');

unirest('PUT', 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
}))
print(response.text)
```

### 8. PHP

```php
<?php
use GuzzleHttp\Client;
$client = new Client();
$headers = [
  'Authorization' => 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version' => '2021-07-28',
  'Content-Type' => 'application/json'
];
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId', [
  'headers' => $headers,
  'body' => '{
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
}'
]);
echo $response->getBody();
```

### 9. JAVA

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"type\": \"string\",
  \"name\": \"string\",
  \"details\": \"string\",
  \"workflowIds\": \"string\",
  \"triggerCondition\": \"string\",
  \"triggerMessage\": \"string\",
  \"contactFieldId\": \"string\",
  \"description\": \"string\",
  \"contactUpdateExamples\": \"string\",
  \"actionId\": \"string\",
  \"calendarId\": \"string\",
  \"onlySendLink\": true,
  \"triggerWorkflow\": true,
  \"sleepAfterBooking\": true,
  \"sleepTimeUnit\": \"string\",
  \"sleepTime\": 123,
  \"transferBot\": true,
  \"transferAgent\": \"string\",
  \"rescheduleEnabled\": true,
  \"cancelEnabled\": true,
  \"stopBotDetectionType\": \"string\",
  \"stopBotTriggerCondition\": \"string\",
  \"reactivateEnabled\": true,
  \"enabled\": true,
  \"stopBotExamples\": \"string\",
  \"finalMessage\": \"string\",
  \"tags\": \"string\",
  \"examples\": \"string\",
  \"assignToUserId\": \"string\",
  \"skipAssignToUser\": true,
  \"createTask\": true,
  \"handoverType\": \"string\",
  \"scenarioId\": \"string\",
  \"followupSequence\": \"string\",
  \"id\": 123,
  \"followupTimeUnit\": \"string\",
  \"followupTime\": 123,
  \"aiEnabledMessage\": true,
  \"customMessage\": \"string\",
  \"workflowId\": \"string\",
  \"contactRequested\": true,
  \"followupSettings\": \"string\",
  \"dynamicChannelSwitching\": true,
  \"followUpHours\": true,
  \"workingHours\": \"string\",
  \"dayOfTheWeek\": 123,
  \"intervals\": \"string\",
  \"startHour\": 123,
  \"startMinute\": 123,
  \"endHour\": 123,
  \"endMinute\": 123,
  \"timezoneToUse\": \"string\",
  \"transferBotType\": \"string\",
  \"transferToBot\": \"string\",
  \"transferBotTriggerCondition\": \"string\",
  \"transferBotExamples\": \"string\"
}"))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

### 10. GO

```go
package main
import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)
func main() {
  url := "https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId"
  payload := strings.NewReader(`{
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
}`)
  req, _ := http.NewRequest("PUT", url, payload)
  req.Header.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
  req.Header.Add("Version", "2021-07-28")
  req.Header.Add("Content-Type", "application/json")
  res, _ := http.DefaultClient.Do(req)
  defer res.Body.Close()
  body, _ := ioutil.ReadAll(res.Body)
  fmt.Println(string(body))
}
```

### 11. RUBY

```ruby
require 'net/http'
require 'uri'
require 'json'

url = URI("https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
})
response = http.request(request)
puts response.read_body
```

### 12. POWERSHELL

```powershell
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
$headers.Add("Version", "2021-07-28")
$headers.Add("Content-Type", "application/json")

$body = '{
  "type": "string",
  "name": "string",
  "details": "string",
  "workflowIds": "string",
  "triggerCondition": "string",
  "triggerMessage": "string",
  "contactFieldId": "string",
  "description": "string",
  "contactUpdateExamples": "string",
  "actionId": "string",
  "calendarId": "string",
  "onlySendLink": true,
  "triggerWorkflow": true,
  "sleepAfterBooking": true,
  "sleepTimeUnit": "string",
  "sleepTime": 123,
  "transferBot": true,
  "transferAgent": "string",
  "rescheduleEnabled": true,
  "cancelEnabled": true,
  "stopBotDetectionType": "string",
  "stopBotTriggerCondition": "string",
  "reactivateEnabled": true,
  "enabled": true,
  "stopBotExamples": "string",
  "finalMessage": "string",
  "tags": "string",
  "examples": "string",
  "assignToUserId": "string",
  "skipAssignToUser": true,
  "createTask": true,
  "handoverType": "string",
  "scenarioId": "string",
  "followupSequence": "string",
  "id": 123,
  "followupTimeUnit": "string",
  "followupTime": 123,
  "aiEnabledMessage": true,
  "customMessage": "string",
  "workflowId": "string",
  "contactRequested": true,
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string",
  "transferBotType": "string",
  "transferToBot": "string",
  "transferBotTriggerCondition": "string",
  "transferBotExamples": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/actions/:actionId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
