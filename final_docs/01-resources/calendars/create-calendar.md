# Create Calendar

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/calendars/` |
| **Scopes Required** | `calendars.write` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `` | No |  |

### Path Parameters

N/A
### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **isActive** | `boolean` | No |  |
| **notifications** | `object[]` | Yes | 🚨 Deprecated! Please use 'Calendar Notifications APIs' instead. Array [ type string Calendar Notification Possible values: [ email ] Default value: email Example: email shouldSendToContact boolean required shouldSendToGuest boolean required shouldSendToUser boolean required shouldSendToSelectedUsers boolean required selectedUsers string required Comma separated emails Example: user1@testemail.com,user2@testemail.com ] |
| **type** | `string` | No |  |
| **shouldSendToContact** | `boolean` | No |  |
| **shouldSendToGuest** | `boolean` | No |  |
| **shouldSendToUser** | `boolean` | No |  |
| **shouldSendToSelectedUsers** | `boolean` | No |  |
| **selectedUsers** | `string` | No |  |
| **locationId** | `string` | No |  |
| **groupId** | `string` | No |  |
| **teamMembers** | `object[]` | Yes | Team members are required for calendars of type: Round Robin, Collective, Class, Service. Personal calendar must have exactly one team member. Array [ userId string required Example: ocQHyuzHvysMo5N5VsXc priority number Possible values: [ 0 , 0.5 , 1 ] Default value: 0.5 isPrimary boolean Marks a user as primary. This property is required in case of collective booking calendars. Only one user can be primary. locationConfigurations object[] Meeting location configuration for event calendar. Multiple locations are allowed only when one team member is selected. For Class booking and Collective calendars, only one location configuration is allowed for each team member. Array [ kind string required Type of meeting location. zoom_conference/google_conference/ms_teams_conference is not supported in event calendar type Possible values: [ custom , zoom_conference , google_conference , inbound_call , outbound_call , physical , booker , ms_teams_conference ] Example: custom location string Address for meeting location. Not applicable on "zoom_conference", "google_conference" and "ms_teams_conference" kind ] ] |
| **userId** | `string` | No |  |
| **priority** | `number` | No |  |
| **isPrimary** | `boolean` | No |  |
| **locationConfigurations** | `object[]` | Yes | Meeting location configuration for event calendar. Multiple locations are allowed only when one team member is selected. For Class booking and Collective calendars, only one location configuration is allowed for each team member. Array [ kind string required Type of meeting location. zoom_conference/google_conference/ms_teams_conference is not supported in event calendar type Possible values: [ custom , zoom_conference , google_conference , inbound_call , outbound_call , physical , booker , ms_teams_conference ] Example: custom location string Address for meeting location. Not applicable on "zoom_conference", "google_conference" and "ms_teams_conference" kind ] |
| **kind** | `string` | No |  |
| **location** | `string` | No |  |
| **eventType** | `string` | No |  |
| **name** | `string` | No |  |
| **description** | `string` | No |  |
| **slug** | `string` | No |  |
| **widgetSlug** | `string` | No |  |
| **calendarType** | `string` | No |  |
| **widgetType** | `string` | No |  |
| **eventTitle** | `string` | No |  |
| **eventColor** | `string` | No |  |
| **locationConfigurations** | `object[]` | Yes | Meeting location configuration for event calendar Array [ kind string required Type of meeting location. zoom_conference/google_conference/ms_teams_conference is not supported in event calendar type Possible values: [ custom , zoom_conference , google_conference , inbound_call , outbound_call , physical , booker , ms_teams_conference ] Example: custom location string Address for meeting location. Not applicable on "zoom_conference", "google_conference" and "ms_teams_conference" kind ] |
| **kind** | `string` | No |  |
| **location** | `string` | No |  |
| **slotDuration** | `number` | No |  |
| **slotDurationUnit** | `string` | No |  |
| **slotInterval** | `number` | No |  |
| **slotIntervalUnit** | `string` | No |  |
| **slotBuffer** | `number` | No |  |
| **slotBufferUnit** | `string` | No |  |
| **preBuffer** | `number` | No |  |
| **preBufferUnit** | `string` | No |  |
| **appoinmentPerSlot** | `number` | No |  |
| **appoinmentPerDay** | `number` | No |  |
| **allowBookingAfter** | `number` | No |  |
| **allowBookingAfterUnit** | `string` | No |  |
| **allowBookingFor** | `number` | No |  |
| **allowBookingForUnit** | `string` | No |  |
| **openHours** | `object[]` | Yes | While we will support this property for backward compatibility, it is recommended to use 'Availability' APIs instead. Array [ daysOfTheWeek number[] required Possible values: <= 6 hours object[] required Array [ openHour number required Possible values: <= 23 openMinute number required Possible values: <= 60 closeHour number required Possible values: <= 23 closeMinute number required Possible values: <= 60 ] ] |
| **daysOfTheWeek** | `number[]` | No |  |
| **hours** | `object[]` | Yes | Array [ openHour number required Possible values: <= 23 openMinute number required Possible values: <= 60 closeHour number required Possible values: <= 23 closeMinute number required Possible values: <= 60 ] |
| **openHour** | `number` | No |  |
| **openMinute** | `number` | No |  |
| **closeHour** | `number` | No |  |
| **closeMinute** | `number` | No |  |
| **enableRecurring** | `boolean` | No |  |
| **recurring** | `object` | No | freq string Possible values: [ DAILY , WEEKLY , MONTHLY ] count number Number of recurrences Possible values: <= 24 bookingOption string This setting contols what to do incase a recurring slot is unavailable Possible values: [ skip , continue , book_next ] bookingOverlapDefaultStatus string This setting contols what to do incase a recurring slot is unavailable Possible values: [ confirmed , new ] |
| **freq** | `string` | No |  |
| **count** | `number` | No |  |
| **bookingOption** | `string` | No |  |
| **bookingOverlapDefaultStatus** | `string` | No |  |
| **formId** | `string` | No |  |
| **stickyContact** | `boolean` | No |  |
| **isLivePaymentMode** | `boolean` | No |  |
| **autoConfirm** | `boolean` | No |  |
| **shouldSendAlertEmailsToAssignedMember** | `boolean` | No |  |
| **alertEmail** | `string` | No |  |
| **googleInvitationEmails** | `boolean` | No |  |
| **allowReschedule** | `boolean` | No |  |
| **allowCancellation** | `boolean` | No |  |
| **shouldAssignContactToTeamMember** | `boolean` | No |  |
| **shouldSkipAssigningContactForExisting** | `boolean` | No |  |
| **notes** | `string` | No |  |
| **pixelId** | `string` | No |  |
| **formSubmitType** | `string` | No |  |
| **formSubmitRedirectURL** | `string` | No |  |
| **formSubmitThanksMessage** | `string` | No |  |
| **availabilityType** | `number` | No |  |
| **availabilities** | `object[]` | Yes | While we will support this property for backward compatibility, it is recommended to use 'Availability' APIs instead. Array [ date string required Formulate the date string in the format of <YYYY-MM-DD in local timezone>T00:00:00.000Z . Example: 2023-09-24T00:00:00.000Z hours object[] required Array [ openHour number required Possible values: <= 23 openMinute number required Possible values: <= 60 closeHour number required Possible values: <= 23 closeMinute number required Possible values: <= 60 ] deleted boolean Default value: false ] |
| **date** | `string` | No |  |
| **hours** | `object[]` | Yes | Array [ openHour number required Possible values: <= 23 openMinute number required Possible values: <= 60 closeHour number required Possible values: <= 23 closeMinute number required Possible values: <= 60 ] |
| **openHour** | `number` | No |  |
| **openMinute** | `number` | No |  |
| **closeHour** | `number` | No |  |
| **closeMinute** | `number` | No |  |
| **deleted** | `boolean` | No |  |
| **guestType** | `string` | No |  |
| **consentLabel** | `string` | No |  |
| **calendarCoverImage** | `string` | No |  |
| **lookBusyConfig** | `object` | Yes | Look Busy Configuration enabled boolean required Apply Look Busy Default value: false Example: true LookBusyPercentage number required Percentage of slots that will be hidden |
| **enabled** | `boolean` | No |  |
| **LookBusyPercentage** | `number` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "calendar": {
    "isActive": true,
    "locationId": "ocQHyuzHvysMo5N5VsXc",
    "groupId": "BqTwX8QFwXzpegMve9EQ",
    "teamMembers": [
      {
        "userId": "ocQHyuzHvysMo5N5VsXc",
        "priority": 0.5,
        "isPrimary": true,
        "locationConfigurations": [
          {
            "kind": "custom",
            "location": "string",
            "meetingId": "my_conference_id"
          }
        ]
      }
    ],
    "eventType": "RoundRobin_OptimizeForAvailability",
    "name": "test calendar",
    "description": "this is used for testing",
    "slug": "test1",
    "widgetSlug": "test1",
    "calendarType": "round_robin",
    "widgetType": "classic",
    "eventTitle": "{{contact.name}}",
    "eventColor": "#039be5",
    "locationConfigurations": [
      {
        "kind": "custom",
        "location": "string",
        "meetingId": "my_conference_id"
      }
    ],
    "slotDuration": 30,
    "slotDurationUnit": "mins",
    "slotInterval": 30,
    "slotIntervalUnit": "mins",
    "slotBuffer": 0,
    "slotBufferUnit": "mins",
    "preBuffer": 0,
    "preBufferUnit": "mins",
    "appoinmentPerSlot": 1,
    "appoinmentPerDay": 0,
    "allowBookingAfter": 0,
    "allowBookingAfterUnit": "days",
    "allowBookingFor": 0,
    "allowBookingForUnit": "days",
    "enableRecurring": false,
    "recurring": {
      "freq": "DAILY",
      "count": 0,
      "bookingOption": "skip",
      "bookingOverlapDefaultStatus": "confirmed"
    },
    "formId": "string",
    "stickyContact": true,
    "isLivePaymentMode": true,
    "autoConfirm": true,
    "shouldSendAlertEmailsToAssignedMember": true,
    "alertEmail": "string",
    "googleInvitationEmails": false,
    "allowReschedule": true,
    "allowCancellation": true,
    "shouldAssignContactToTeamMember": true,
    "shouldSkipAssigningContactForExisting": true,
    "notes": "string",
    "pixelId": "string",
    "formSubmitType": "ThankYouMessage",
    "formSubmitRedirectURL": "string",
    "formSubmitThanksMessage": "string",
    "guestType": "count_only",
    "consentLabel": "string",
    "calendarCoverImage": "https://path-to-image.com",
    "lookBusyConfig": {
      "enabled": true,
      "LookBusyPercentage": 0
    },
    "id": "0TkCdp9PfvLeWKYRRvIz"
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **calendar** | `dict` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/calendars/ \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/calendars/', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
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
  method: 'post',
  url: 'https://services.leadconnectorhq.com/calendars/',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
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
  'method': 'POST',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/calendars/',
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
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/calendars/',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
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

unirest('POST', 'https://services.leadconnectorhq.com/calendars/')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/calendars/"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/calendars/', [
  'headers' => $headers,
  'body' => '{
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
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
    .uri(URI.create("https://services.leadconnectorhq.com/calendars/"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"isActive\": true,
  \"notifications\": \"string\",
  \"type\": \"string\",
  \"shouldSendToContact\": true,
  \"shouldSendToGuest\": true,
  \"shouldSendToUser\": true,
  \"shouldSendToSelectedUsers\": true,
  \"selectedUsers\": \"string\",
  \"locationId\": \"string\",
  \"groupId\": \"string\",
  \"teamMembers\": \"string\",
  \"userId\": \"string\",
  \"priority\": 123,
  \"isPrimary\": true,
  \"locationConfigurations\": \"string\",
  \"kind\": \"string\",
  \"location\": \"string\",
  \"eventType\": \"string\",
  \"name\": \"string\",
  \"description\": \"string\",
  \"slug\": \"string\",
  \"widgetSlug\": \"string\",
  \"calendarType\": \"string\",
  \"widgetType\": \"string\",
  \"eventTitle\": \"string\",
  \"eventColor\": \"string\",
  \"slotDuration\": 123,
  \"slotDurationUnit\": \"string\",
  \"slotInterval\": 123,
  \"slotIntervalUnit\": \"string\",
  \"slotBuffer\": 123,
  \"slotBufferUnit\": \"string\",
  \"preBuffer\": 123,
  \"preBufferUnit\": \"string\",
  \"appoinmentPerSlot\": 123,
  \"appoinmentPerDay\": 123,
  \"allowBookingAfter\": 123,
  \"allowBookingAfterUnit\": \"string\",
  \"allowBookingFor\": 123,
  \"allowBookingForUnit\": \"string\",
  \"openHours\": \"string\",
  \"daysOfTheWeek\": \"string\",
  \"hours\": \"string\",
  \"openHour\": 123,
  \"openMinute\": 123,
  \"closeHour\": 123,
  \"closeMinute\": 123,
  \"enableRecurring\": true,
  \"recurring\": \"string\",
  \"freq\": \"string\",
  \"count\": 123,
  \"bookingOption\": \"string\",
  \"bookingOverlapDefaultStatus\": \"string\",
  \"formId\": \"string\",
  \"stickyContact\": true,
  \"isLivePaymentMode\": true,
  \"autoConfirm\": true,
  \"shouldSendAlertEmailsToAssignedMember\": true,
  \"alertEmail\": \"string\",
  \"googleInvitationEmails\": true,
  \"allowReschedule\": true,
  \"allowCancellation\": true,
  \"shouldAssignContactToTeamMember\": true,
  \"shouldSkipAssigningContactForExisting\": true,
  \"notes\": \"string\",
  \"pixelId\": \"string\",
  \"formSubmitType\": \"string\",
  \"formSubmitRedirectURL\": \"string\",
  \"formSubmitThanksMessage\": \"string\",
  \"availabilityType\": 123,
  \"availabilities\": \"string\",
  \"date\": \"string\",
  \"deleted\": true,
  \"guestType\": \"string\",
  \"consentLabel\": \"string\",
  \"calendarCoverImage\": \"string\",
  \"lookBusyConfig\": \"string\",
  \"enabled\": true,
  \"LookBusyPercentage\": 123
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
  url := "https://services.leadconnectorhq.com/calendars/"
  payload := strings.NewReader(`{
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
}`)
  req, _ := http.NewRequest("POST", url, payload)
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

url = URI("https://services.leadconnectorhq.com/calendars/")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
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
  "isActive": true,
  "notifications": "string",
  "type": "string",
  "shouldSendToContact": true,
  "shouldSendToGuest": true,
  "shouldSendToUser": true,
  "shouldSendToSelectedUsers": true,
  "selectedUsers": "string",
  "locationId": "string",
  "groupId": "string",
  "teamMembers": "string",
  "userId": "string",
  "priority": 123,
  "isPrimary": true,
  "locationConfigurations": "string",
  "kind": "string",
  "location": "string",
  "eventType": "string",
  "name": "string",
  "description": "string",
  "slug": "string",
  "widgetSlug": "string",
  "calendarType": "string",
  "widgetType": "string",
  "eventTitle": "string",
  "eventColor": "string",
  "slotDuration": 123,
  "slotDurationUnit": "string",
  "slotInterval": 123,
  "slotIntervalUnit": "string",
  "slotBuffer": 123,
  "slotBufferUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "appoinmentPerSlot": 123,
  "appoinmentPerDay": 123,
  "allowBookingAfter": 123,
  "allowBookingAfterUnit": "string",
  "allowBookingFor": 123,
  "allowBookingForUnit": "string",
  "openHours": "string",
  "daysOfTheWeek": "string",
  "hours": "string",
  "openHour": 123,
  "openMinute": 123,
  "closeHour": 123,
  "closeMinute": 123,
  "enableRecurring": true,
  "recurring": "string",
  "freq": "string",
  "count": 123,
  "bookingOption": "string",
  "bookingOverlapDefaultStatus": "string",
  "formId": "string",
  "stickyContact": true,
  "isLivePaymentMode": true,
  "autoConfirm": true,
  "shouldSendAlertEmailsToAssignedMember": true,
  "alertEmail": "string",
  "googleInvitationEmails": true,
  "allowReschedule": true,
  "allowCancellation": true,
  "shouldAssignContactToTeamMember": true,
  "shouldSkipAssigningContactForExisting": true,
  "notes": "string",
  "pixelId": "string",
  "formSubmitType": "string",
  "formSubmitRedirectURL": "string",
  "formSubmitThanksMessage": "string",
  "availabilityType": 123,
  "availabilities": "string",
  "date": "string",
  "deleted": true,
  "guestType": "string",
  "consentLabel": "string",
  "calendarCoverImage": "string",
  "lookBusyConfig": "string",
  "enabled": true,
  "LookBusyPercentage": 123
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
